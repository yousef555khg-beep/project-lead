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
    "## Execution model routing": (
        "`model_routing_authority: approved | fixed_default | pending`",
        "Before every new objective, dispatch, or substantive follow-up",
        "Never inherit a previous objective's model",
        "Choose `gpt-5.3-codex-spark high` only when every condition is true",
        "If any Spark condition is false, unknown, or becomes false, select `gpt-5.6-terra high`",
        "same owner and task",
        "explicit `gpt-5.6-terra high` override",
        "A completed Spark objective does not authorize Spark for the next objective",
        "Execution-model routing never changes the review lane",
    ),
    "## Speed tier": (
        "The controller's own service tier is user-configured and grants no child authority",
        "Standard/default is mandatory for every new child task and child follow-up",
        "Model-routing authority never authorizes Fast/priority child service",
        "Fast requires separate explicit user approval for one child objective",
        "never infer it from the Low-risk lane, Spark, urgency, or the parent controller",
        "dispatch cannot set and verify a Standard child, stop and ask the user",
        "Prompt text cannot change the transport service tier",
    ),
    "## Architecture routing": (
        "Missing evidence means inspect or ask",
        "do not review every draft",
    ),
    "### Low-risk lane — default": (
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
        "immediately enter `wait_threads`",
        "Do not send a final answer while any promised target is accepted, queued, or running",
        "A timeout is not a state change; reuse the returned cursor",
        "relay it in commentary and keep waiting for the rest",
        "automatic relay cannot be guaranteed",
        "one project-scoped read-only Luna assistant task",
        "large or repetitive enough to materially reduce controller context or cost",
        "A Luna result is advisory",
        "cannot write or modify code, choose execution models or review lanes",
        "Do not use Luna for a few lines, routine updates, or to appear busy",
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
    inherited_model = re.compile(
        r"\b(?:reuse|inherit|carry|keep)\b[^.\n]{0,80}"
        r"\b(?:current|previous|existing)\b[^.\n]{0,40}\bmodel\b"
        r"[^.\n]{0,70}\b(?:next|new)\b[^.\n]{0,30}\bobjective\b"
    )
    for match in inherited_model.finditer(lowered):
        if not directly_negated(lowered, match.start()):
            errors.append(
                ValidationError(
                    "inherited-model",
                    f"line {line_number_at(text, match.start())}: execution model cannot carry into a new objective",
                )
            )

    fast_for_scope = re.compile(
        r"\b(?:use|enable|select|apply)\b[^.\n]{0,50}\b(?:fast mode|priority(?: child)? service tier)\b"
        r"[^.\n]{0,60}\b(?:every|all|new child|child task)\b"
        r"|\b(?:every|all|new child|child task)\b[^.\n]{0,60}\b(?:use|enable|select|apply)\b"
        r"[^.\n]{0,50}\b(?:fast mode|priority(?: child)? service tier)\b"
    )
    for match in fast_for_scope.finditer(lowered):
        if not directly_negated(lowered, match.start()):
            errors.append(
                ValidationError(
                    "fast-service-tier",
                    f"line {line_number_at(text, match.start())}: Fast cannot be the automatic service tier",
                )
            )

    fast_authority = re.compile(
        r"\b(?:automatic )?model[- ]routing authority\b[^.\n]{0,80}"
        r"\b(?:authorizes?|includes?|covers?)\b[^.\n]{0,45}"
        r"\b(?:fast(?:/priority)?(?: child)?(?: mode| service)?|priority(?: child)? service tier)\b"
    )
    for match in fast_authority.finditer(lowered):
        action = re.search(r"\b(?:authorizes?|includes?|covers?)\b", match.group(0))
        action_start = match.start() + (action.start() if action else 0)
        if not directly_negated(lowered, action_start):
            errors.append(
                ValidationError(
                    "fast-authority",
                    f"line {line_number_at(text, match.start())}: model routing cannot authorize Fast service",
                )
            )

    fast_inheritance = re.compile(
        r"\b(?:inherit|reuse|carry)\b[^.\n]{0,80}\b(?:parent|controller|current)\b"
        r"[^.\n]{0,60}\b(?:fast mode|priority service tier)\b[^.\n]{0,80}"
        r"\b(?:child|subagent|task|turn)\b"
        r"|\b(?:child|subagent)\b[^.\n]{0,60}\b(?:inherit|reuse|carry|use)\b"
        r"[^.\n]{0,80}\b(?:parent|controller|current)\b[^.\n]{0,60}"
        r"\b(?:fast mode|priority service tier)\b"
    )
    for match in fast_inheritance.finditer(lowered):
        if not directly_negated(lowered, match.start()):
            errors.append(
                ValidationError(
                    "fast-inheritance",
                    f"line {line_number_at(text, match.start())}: child speed cannot inherit Fast service",
                )
            )

    luna = re.compile(r"\bluna\b")
    luna_action = re.compile(
        r"\b(?:write|modify|implement|review|accept)\b"
        r"|\bmark\b[^.\n]{0,30}\bcomplete\b"
        r"|\bchoose\b[^.\n]{0,50}\b(?:execution models?|review lanes?)\b"
        r"|\bmake\b[^.\n]{0,30}\barchitecture decisions?\b"
        r"|\bcall\b[^.\n]{0,30}\bmutating tools?\b"
    )
    permission = re.compile(r"\b(?:may|can|should|will|must)\b")
    for obj in luna.finditer(lowered):
        start, end = clause_span(lowered, obj.start(), obj.end(), 140)
        clause = lowered[start:end]
        for action in luna_action.finditer(lowered, start, end):
            permitted = list(permission.finditer(lowered, start, action.start()))
            if permitted and not directly_negated(lowered, action.start()):
                errors.append(
                    ValidationError(
                        "luna-authority",
                        f"line {line_number_at(text, obj.start())}: Luna cannot receive execution, review, or acceptance authority",
                    )
                )
                break

        use_action = governing_action(lowered, obj.start(), obj.end(), re.compile(r"\b(?:use|invoke|call)\b"), 120)
        if (
            use_action
            and not directly_negated(lowered, use_action.start())
            and re.search(r"\b(?:always|every|all|routine|short)\b", clause)
        ):
            errors.append(
                ValidationError(
                    "luna-overuse",
                    f"line {line_number_at(text, obj.start())}: Luna cannot be mandatory for routine or short updates",
                )
            )

    early_exit = re.compile(
        r"(?:"
        r"\b(?:send|give|return|issue)\b[^.\n]{0,40}\bfinal answer\b"
        r"|\b(?:finish|end|close)\b[^.\n]{0,45}\bcontroller turn\b"
        r"|\breturn control\b[^.\n]{0,35}\buser\b"
        r"|\bcontroller\b[^.\n]{0,35}\bgo idle\b"
        r")[^.\n]{0,120}\b(?:accepted|queued|running|continues?)\b"
    )
    for match in early_exit.finditer(lowered):
        if not directly_negated(lowered, match.start()):
            errors.append(
                ValidationError(
                    "early-controller-exit",
                    f"line {line_number_at(text, match.start())}: controller cannot end while promised work is active",
                )
            )

    self_wake = re.compile(
        r"\b(?:luna|30[- ]minute (?:rule|fallback)|heartbeat|cron|timer|idle controller)\b[^.\n]{0,100}"
        r"\b(?:wake|wakes|waking|reactivate|reactivates)\b"
    )
    for match in self_wake.finditer(lowered):
        start, _ = clause_span(lowered, match.start(), match.end(), 150)
        prefix = lowered[start : match.end()]
        if not re.search(r"\b(?:cannot|can not|never|do not|does not)\b", prefix):
            errors.append(
                ValidationError(
                    "false-self-wake",
                    f"line {line_number_at(text, match.start())}: an idle controller cannot self-wake",
                )
            )
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
