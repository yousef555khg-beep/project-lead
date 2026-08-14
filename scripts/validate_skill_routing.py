#!/usr/bin/env python3
"""Validate Project Lead's risk lanes and deferred installation contract."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import NamedTuple


class ValidationError(NamedTuple):
    code: str
    message: str


EXPECTED_CONTRACT = {
    "contract_version": 1,
    "discovery_executor": "structured-read-only-search",
    "external_skill_dependency": False,
    "candidate_content_trust": "untrusted-data-only",
    "candidate_tree_review": "complete-static-closure",
    "candidate_code_execution": False,
    "approval_identity": "repository-commit-tree-skill-manifest-method-target",
    "candidate_lifecycle": "per-candidate",
    "install_hooks": False,
    "install_write_scope": "approved-target-and-transaction-staging-rollback-only",
    "target_path_binding": "realpath-device-inode-nofollow",
    "ancestor_traversal": "root-anchored-openat-nofollow-fstat",
    "commit_guard": "exclusive-parent-and-loader-quiescence",
    "installation_commit": "conditional-noreplace-or-exchange",
    "failure_state_machine": "precommit-fail-or-atomic-rollback-or-cleanup-required",
    "durable_recovery": "fsynced-transaction-record-loader-startup-gate",
    "crash_recovery": "reconcile-before-loader-enable",
    "content_durability": "fsync-files-directories-and-parent",
    "loader_transaction_namespace": "target-staging-rollback-gated-until-cleanup",
    "loader_terminal_states": "installed-or-rollback-verified-after-cleanup",
    "candidate_install_outcome": "installed-only-or-install-failed-after-rollback",
    "installed_verification": "full-tree-sha256-match",
    "blocker_model": "orthogonal-set",
    "same_candidate_second_opinion": "explicit-user-or-reviewer-quality-only",
}

CORE_REQUIRED = {
    "## Ownership and dispatch": (
        "one mutable scope or checkout under one owner",
        "controller may handle a brief, isolated, reversible change directly",
        "compact private ledger",
    ),
    "## Architecture routing": (
        "Missing evidence means inspect or ask",
        "do not review every draft",
    ),
    "### Fast lane — default": (
        "`independent_review: none`",
        "Do not create an independent reviewer",
        "controller verification is acceptance",
    ),
    "### Standard lane": (
        "`independent_review: one_batched_terra`",
        "one independent `gpt-5.6-terra high` review",
        "At most one automatic incremental re-review",
        "Minor findings never trigger return or re-review",
    ),
    "### Elevated lane": (
        "`independent_review: sol_required`",
        "independent `gpt-5.6-sol xhigh`",
        "privacy or regulated personal data",
        "cryptography or security compliance",
    ),
    "## Supporting skills and capability discovery": (
        "automatically decide whether an installed supporting skill is needed",
        "select and invoke one without asking the user to remember its name",
        "Ordinary bounded work selects `none`",
        "do not invoke `find-skills`",
        "Recommend at most three",
        "Read `references/skill-installation-safety.md` only after the user approves an exact candidate",
    ),
    "## Monitoring and blockers": (
        "After 30 minutes without substantive progress",
        "never create heartbeat, cron, or polling",
        "`blocked_on_user` and `blocked_on_capability` may coexist",
    ),
    "## Acceptance and reporting": (
        "已完成：<用户能理解的结果>",
        "当前结果：<能否使用或验证>",
        "阻塞：无 | <需要用户处理的唯一事项>",
        "下一步：<一个最有价值的动作>",
        "Do not expose ledger fields",
    ),
}

REFERENCE_REQUIRED = (
    "## Bind the candidate before approval",
    "## Fail-closed installation transaction",
    "O_DIRECTORY|O_NOFOLLOW",
    "atomic no-replace",
    "atomic exchange",
    "fsync` every file",
    "install_failed_cleanup_required",
    "loader-excluded namespace",
    "## Installation safety contract",
)

HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
CONTRACT_BLOCK = re.compile(
    r"^## Installation safety contract\s*$\n\s*```json\s*$\n(.*?)^```\s*$",
    re.MULTILINE | re.DOTALL,
)
CLAUSE_BOUNDARY = re.compile(
    r"[;,:.!?。！？；：，]|\s+[—–]\s+|\n\s*\n|\n(?=\s*(?:[-*+]|\d+[.)]|#{1,6})\s)"
)


def visible_text(text: str) -> str:
    return HTML_COMMENT.sub("", text)


def section(text: str, heading: str) -> str | None:
    lines = text.splitlines()
    try:
        start = lines.index(heading)
    except ValueError:
        return None
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = re.match(r"^(#{1,6})\s+", lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return "\n".join(lines[start:end])


def directly_negated(text: str, predicate_start: int) -> bool:
    prefix = text[max(0, predicate_start - 48) : predicate_start].lower()
    return bool(
        re.search(
            r"(?:\bdo not|\bdoes not|\bnever|\bmust not|\bcannot|\bcan not)\s+(?:ever\s+)?$",
            prefix,
        )
    )


def clause_span(text: str, object_start: int, object_end: int, window: int) -> tuple[int, int]:
    search_start = max(0, object_start - window)
    search_end = min(len(text), object_end + window)
    before = list(CLAUSE_BOUNDARY.finditer(text, search_start, object_start))
    after = CLAUSE_BOUNDARY.search(text, object_end, search_end)
    return (before[-1].end() if before else search_start, after.start() if after else search_end)


def governing_action(
    text: str,
    object_start: int,
    object_end: int,
    action_pattern: re.Pattern[str],
    window: int,
) -> re.Match[str] | None:
    start, end = clause_span(text, object_start, object_end, window)
    matches = list(action_pattern.finditer(text, start, end))
    preceding = [match for match in matches if match.end() <= object_start]
    if preceding:
        return max(preceding, key=lambda match: match.end())
    following = [match for match in matches if match.start() >= object_end]
    return min(following, key=lambda match: match.start()) if following else None


def line_number_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def unsafe_language_errors(text: str) -> list[ValidationError]:
    errors: list[ValidationError] = []
    lowered = text.lower()

    for line_number, line in enumerate(lowered.splitlines(), start=1):
        if re.search(r"\bnpx\b", line):
            errors.append(ValidationError("unsafe-npx", f"line {line_number}: package runner is forbidden"))

    find_object = re.compile(r"\bfind-skills\b")
    find_action = re.compile(r"\b(?:invoke|use|load|run|call|require|depend)\b")
    for obj in find_object.finditer(lowered):
        action = governing_action(lowered, obj.start(), obj.end(), find_action, 120)
        if action and not directly_negated(lowered, action.start()):
            errors.append(
                ValidationError(
                    "external-skill-dependency",
                    f"line {line_number_at(text, obj.start())}: find-skills cannot be a dependency",
                )
            )

    blocker = re.compile(r"\b(?:blocked_on_capability|capability[-_ ]blocked)\b")
    report = re.compile(r"\b(?:report|mark|treat|declare|label)(?:ed|s|ing)?\b")
    for obj in blocker.finditer(lowered):
        start, end = clause_span(lowered, obj.start(), obj.end(), 140)
        action = governing_action(lowered, obj.start(), obj.end(), report, 140)
        if action and re.search(r"\bcomplete(?:d)?\b", lowered[start:end]) and not directly_negated(lowered, action.start()):
            errors.append(
                ValidationError(
                    "blocked-completed",
                    f"line {line_number_at(text, obj.start())}: blocked scope cannot be complete",
                )
            )

    if re.search(r"\bevery\b[^.\n]{0,90}\b(?:requires?|must)\b[^.\n]{0,50}\bindependent (?:code )?review\b", lowered):
        errors.append(ValidationError("global-review", "independent review cannot be mandatory for every task"))
    if re.search(r"\bif\b[^.\n]{0,80}\b(?:evidence|information)\b[^.\n]{0,40}\bincomplete\b[^.\n]{0,80}\b(?:classify|treat|use)\b[^.\n]{0,40}\bsystem architecture\b", lowered):
        errors.append(ValidationError("automatic-system", "missing evidence cannot automatically escalate architecture"))
    if re.search(r"\bminor findings?\b[^.\n]{0,50}\b(?:requires?|must|always)\b[^.\n]{0,50}\b(?:return|re-review|repair)\b", lowered):
        errors.append(ValidationError("minor-rereview", "minor findings cannot force another review"))
    return errors


def validate_text(text: str) -> list[ValidationError]:
    errors: list[ValidationError] = []
    if HTML_COMMENT.search(text):
        errors.append(ValidationError("html-comment", "HTML comments are forbidden"))
    visible = visible_text(text)
    if len(visible.split()) > 1800:
        errors.append(ValidationError("context-budget", "core skill exceeds 1800 words"))
    for heading, phrases in CORE_REQUIRED.items():
        body = section(visible, heading)
        if body is None:
            errors.append(ValidationError("missing-section", f"missing section: {heading}"))
            continue
        for phrase in phrases:
            if phrase not in body:
                errors.append(ValidationError("missing-rule", f"{heading} is missing: {phrase}"))
    if "No lane may launch a third automatic review" not in visible:
        errors.append(ValidationError("review-cap", "automatic review loop cap is missing"))
    errors.extend(unsafe_language_errors(visible))
    return errors


def validate_reference_text(text: str) -> list[ValidationError]:
    errors: list[ValidationError] = []
    if HTML_COMMENT.search(text):
        errors.append(ValidationError("html-comment", "HTML comments are forbidden"))
    visible = visible_text(text)
    for phrase in REFERENCE_REQUIRED:
        if phrase not in visible:
            errors.append(ValidationError("missing-reference-rule", f"installation reference is missing: {phrase}"))
    matches = CONTRACT_BLOCK.findall(visible)
    if len(matches) != 1:
        errors.append(ValidationError("contract-count", f"expected one installation contract, found {len(matches)}"))
    else:
        try:
            contract = json.loads(matches[0])
        except json.JSONDecodeError as exc:
            errors.append(ValidationError("contract-json", f"invalid installation contract: {exc}"))
        else:
            if contract != EXPECTED_CONTRACT:
                errors.append(ValidationError("contract-value", "installation contract differs from enforced values"))
    return errors


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parents[1]
    core = Path(argv[1]) if len(argv) > 1 else root / "skills/project-lead/SKILL.md"
    reference = (
        Path(argv[2])
        if len(argv) > 2
        else core.parent / "references/skill-installation-safety.md"
    )
    if not core.is_file() or not reference.is_file():
        print(f"missing Project Lead core or reference: {core}, {reference}", file=sys.stderr)
        return 2
    errors = [
        *(ValidationError(f"core/{e.code}", e.message) for e in validate_text(core.read_text(encoding="utf-8"))),
        *(ValidationError(f"reference/{e.code}", e.message) for e in validate_reference_text(reference.read_text(encoding="utf-8"))),
    ]
    if errors:
        for error in errors:
            print(f"{error.code}: {error.message}", file=sys.stderr)
        return 1
    print("project-lead risk-lane and installation-reference checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
