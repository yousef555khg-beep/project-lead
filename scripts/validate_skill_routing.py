#!/usr/bin/env python3
"""Validate Project Lead's risk lanes and deferred installation contract."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
from typing import NamedTuple


class ValidationError(NamedTuple):
    code: str
    message: str


EXPECTED_CORE_SHA256 = "6a93fd54ab25bb970ef2ff070c0de2608f96d50479fc8cd07e8b5033cb72b090"


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
        "one mutable scope under one owner",
        "classify `work_location: controller | executor`",
        "Repository plans, designs, source, tests, configuration",
        "Do not split executor work into small direct steps",
        "Concurrency or convenience never moves executor work into the controller",
        "compact private ledger",
    ),
    "## Authority boundary": (
        "Approval follows the proposed action and missing authority",
        "Elevated alone never creates `blocked_on_user`",
        "the controller authorizes dispatch, local reversible preparation, focused checks, required independent review, and in-scope repair",
        "A real platform approval card is relayed only when the user must operate it",
        "Bind `blocked_on_user` to the objective, candidate or scope version, exact action or decision, and missing authority",
        "Never inherit it by label alone",
    ),
    "## Execution model routing": (
        "`model_routing_authority: approved | fixed_default | pending`",
        "Before every new objective, dispatch, or substantive follow-up",
        "`execution_route: {model, reasoning_effort, service_tier}`",
        "never inherit a previous route",
        "Spark uses `high`; use `xhigh` only when the dispatch tool exposes it",
        "Terra uses `high` by default, `xhigh` for non-obvious debugging, cross-module reasoning, or complex design",
        "`ultra` only for a large parallelizable objective with independent workstreams",
        "Luna uses `medium` for ordinary evidence extraction, `high` for dense multi-source evidence, and `xhigh` only for hard contradictions",
        "Only select combinations exposed by the dispatch tool; never invent a model or effort",
        "`fork_turns: none` or a bounded positive turn count",
        "never use `all` or omitted full-history inheritance",
        "Any independent reviewer also uses no or bounded history even when its route matches the controller",
        "If dispatch atomically exposes the resolved route, compare it before work",
        "Otherwise create a handshake-only task with no project reads, writes, or tool calls",
        "Send the substantive brief only after metadata confirms the route",
        "If the route cannot be observed, report `blocked_on_routing`",
        "A follow-up without model and effort fields cannot switch them",
        "hand off the same logical scope to one correctly routed replacement task",
        "Immediately before every creation or substantive follow-up, tell the user",
        "即将派发：<任务>｜模型：<model>｜档位：<reasoning_effort>｜速度：普通",
        "informational, never an approval gate",
        "dispatch immediately without waiting for a reply",
        "issue a corrected notice before redispatch",
        "Replace `普通` with `Fast` only for an exact objective already authorized below",
        "A completed objective authorizes nothing for the next",
        "Execution-model routing never changes the review lane",
    ),
    "## Speed tier": (
        "The controller's own service tier is user-configured and grants no child authority",
        "Standard/default is the child default unless the user explicitly requested Fast for that exact objective",
        "Model-routing authority never authorizes Fast/priority child service",
        "Never ask, suggest, recommend, or offer Fast",
        "When dispatch has no service-tier field, omit any Fast/priority override and dispatch with the platform default",
        "Absence of a speed field is not a reason to block or ask",
        "A new child objective resets to Standard/default",
        "observable evidence shows unexpected Fast/priority, stop further child follow-ups and report",
        "Prompt text cannot change the transport service tier",
    ),
    "## Architecture routing": (
        "Missing evidence means inspect or delegate evidence collection",
        "An Elevated trigger changes the review lane but does not by itself create an architecture phase",
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
        "Standard closes recorded findings from refreshed executor evidence plus one focused spot check",
        "unproven findings stay `RETURN`",
    ),
    "### Elevated lane": (
        "`independent_review: sol_required`",
        "independent `gpt-5.6-sol xhigh`",
        "privacy or regulated personal data",
        "cryptography or security compliance",
        "Elevated dispatches one in-scope root-cause repair and one final independent closure review without asking",
        "If that review returns, keep `RETURN`, report `blocked_on_quality`, and never launch a fourth review",
        "No lane repeats the same incremental review loop after two returns",
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
        "one project-scoped read-only Luna assistant scope",
        "large or repetitive enough to materially reduce controller context or cost",
        "A Luna result is advisory",
        "cannot write or modify code, choose execution models or review lanes",
        "Do not use Luna for a few lines, routine updates, or to appear busy",
        "After 30 minutes without substantive progress",
        "never create heartbeat, cron, or polling",
        "`blocked_on_user` and `blocked_on_capability` may coexist",
    ),
    "## Acceptance and reporting": (
        "Acceptance reconciles executor evidence and at most one focused spot check",
        "does not require the controller to rerun full suites or long manual validation",
        "已完成：<用户能理解的结果>",
        "当前结果：<能否使用或验证>",
        "阻塞：无 | <需要用户处理的唯一事项>",
        "下一步：<一个最有价值的动作>",
        "Outside the required route notice, do not expose ledger fields",
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
SENTENCE_BOUNDARY = re.compile(r"[.!?。！？]|\n")


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
    prefix = text[max(0, predicate_start - 72) : predicate_start].lower()
    return bool(
        re.search(
            r"(?:\bnever|\bcannot|\bcan not|\b(?:do|does|did|may|might|should|will|would|must) not)"
            r"\s+(?:(?:by itself|automatically|directly|ever|immediately|explicitly)\s+)?$",
            prefix,
        )
    )


def action_is_forbidden(text: str, predicate_start: int, predicate_end: int) -> bool:
    """Bind a prohibition to the dangerous predicate instead of any negation nearby."""
    if directly_negated(text, predicate_start):
        return True
    prefix = text[max(0, predicate_start - 120) : predicate_start].lower()
    suffix = text[predicate_end : min(len(text), predicate_end + 80)].lower()
    forbidden_prefix = re.compile(
        r"(?:\bwithout|\b(?:forbid|prohibit|disallow|reject|avoid)(?:s|ed|ing)?|"
        r"\beliminat(?:e|es|ed|ing) the need to|\bstop(?:s|ped|ping)?(?:\s+\w+){0,3})"
        r"(?:\s+[`'\"\w:/-]+){0,7}\s*$"
    )
    forbidden_suffix = re.compile(r"^\s*(?:is|are|must be)?\s*(?:forbidden|prohibited|disallowed|rejected)\b")
    return bool(forbidden_prefix.search(prefix) or forbidden_suffix.search(suffix))


def clause_span(text: str, object_start: int, object_end: int, window: int) -> tuple[int, int]:
    search_start = max(0, object_start - window)
    search_end = min(len(text), object_end + window)
    before = list(CLAUSE_BOUNDARY.finditer(text, search_start, object_start))
    after = CLAUSE_BOUNDARY.search(text, object_end, search_end)
    return (before[-1].end() if before else search_start, after.start() if after else search_end)


def statement_span(text: str, start: int, end: int, window: int = 240) -> tuple[int, int]:
    """Return the surrounding sentence so trailing safety qualifiers stay visible."""
    search_start = max(0, start - window)
    search_end = min(len(text), end + window)
    before = list(SENTENCE_BOUNDARY.finditer(text, search_start, start))
    after = SENTENCE_BOUNDARY.search(text, end, search_end)
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
    subject_risk_architecture = re.compile(
        r"\b(?:elevated|security|authentication|authorization|cryptography|privacy)\b"
        r"(?P<context>[^.\n]{0,130}?)"
        r"\b(?P<action>gets?|creates?|starts?|uses?|requires?)\b"
        r"[^.\n]{0,70}\b(?:separate )?(?:system )?architecture phase\b"
    )
    for match in subject_risk_architecture.finditer(lowered):
        clause = match.group(0)
        allowed_trigger = re.search(
            r"\b(?:cross[- ]client|cross[- ]service|unresolved shared contract|material rework risk|security[- ]policy fork)\b",
            clause,
        )
        if not allowed_trigger and not directly_negated(lowered, match.start("action")):
            errors.append(
                ValidationError(
                    "subject-risk-architecture",
                    f"line {line_number_at(text, match.start())}: subject risk alone cannot force an architecture phase",
                )
            )
    if re.search(r"\bminor findings?\b[^.\n]{0,50}\b(?:requires?|must|always)\b[^.\n]{0,50}\b(?:return|re-review|repair)\b", lowered):
        errors.append(ValidationError("minor-rereview", "minor findings cannot force another review"))

    subject_risk_approval = re.compile(
        r"\b(?:elevated|security|authentication|authorization|cryptography|privacy)\b"
        r"[^.\n]{0,130}?\b(?P<action>asks?|requires?|waits?|needs?|requests?|obtains?)\b"
        r"[^.\n]{0,80}\b(?:the\s+)?user(?:'s)?(?:\s+(?:approval|sign[- ]off|consent))?\b"
    )
    for match in subject_risk_approval.finditer(lowered):
        start, end = statement_span(lowered, match.start(), match.end())
        statement = lowered[start:end]
        legitimate_boundary = re.search(
            r"\b(?:product|security[- ]policy) fork\b|\b(?:new authority|new secret|irreversible|destructive|external side effect|purchase|deployment|release|platform approval card)\b",
            statement,
        )
        if not legitimate_boundary and not directly_negated(lowered, match.start("action")):
            errors.append(
                ValidationError(
                    "subject-risk-approval",
                    f"line {line_number_at(text, match.start())}: subject risk cannot create user approval",
                )
            )

    forced_user_replan = re.compile(
        r"\b(?:after|following) (?:two|the second) returns?\b[^.\n]{0,120}?"
        r"\b(?P<action>waits?|asks?|requests?|requires?|needs?|pauses?)\b[^.\n]{0,80}"
        r"(?:\b(?:the\s+)?user(?:'s)?(?:\s+(?:approval|sign[- ]off))?\b|"
        r"\b(?:the\s+)?user\s+approves?\b)"
    )
    for match in forced_user_replan.finditer(lowered):
        start, end = statement_span(lowered, match.start(), match.end())
        statement = lowered[start:end]
        boundary_exception = re.search(
            r"\bonly when\b[^.\n]{0,100}(?:"
            r"\b(?:cross(?:es|ed|ing)?|outside|beyond)\b[^.\n]{0,50}\b(?:authority|approval) boundary\b|"
            r"\b(?:needs?|requires?)\b[^.\n]{0,30}\bnew authority\b)",
            statement,
        )
        if not boundary_exception and not directly_negated(lowered, match.start("action")):
            errors.append(
                ValidationError(
                    "forced-user-replan",
                    f"line {line_number_at(text, match.start())}: unchanged authority cannot force user reapproval",
                )
            )

    stale_user_blocker = re.compile(
        r"\b(?P<action>carr(?:y|ies)|inherits?|reuses?|keeps?|preserves?|retains?|propagat(?:e|es|ed|ing))\b"
        r"[^.\n]{0,70}\bblocked_on_user\b[^.\n]{0,70}"
        r"\b(?:new|next|every|following|later)\b[^.\n]{0,35}\b(?:candidate|objective|scope(?: revisions?)?)\b"
    )
    for match in stale_user_blocker.finditer(lowered):
        start, end = statement_span(lowered, match.start(), match.end())
        statement = lowered[start:end]
        preserves_isolation = re.search(r"\bblocked_on_user\s+(?:isolation|separation)\b", statement)
        if not preserves_isolation and not directly_negated(lowered, match.start("action")):
            errors.append(
                ValidationError(
                    "stale-user-blocker",
                    f"line {line_number_at(text, match.start())}: user blocker cannot cross identity boundaries",
                )
            )

    controller_work_hoarding = re.compile(
        r"\bcontroller\b[^.\n]{0,55}?\b(?P<action>"
        r"writes?|implements?|modifies?|runs?|keeps?|handles?|owns?|performs?|authors?|executes?)\b"
        r"[^.\n]{0,110}\b(?:repository (?:plans?|designs?)|production code|source (?:edits?|changes?)|"
        r"test code|complex debugging|full[- ]suite validation|full test suite|long validation|broad validation)\b"
        r"|\bsplit\b[^.\n]{0,70}\b(?:multi-file implementation|executor work)\b"
        r"[^.\n]{0,70}\b(?:small|direct controller)\b"
    )
    for match in controller_work_hoarding.finditer(lowered):
        action_start = match.start("action") if match.groupdict().get("action") else match.start()
        start, end = statement_span(lowered, match.start(), match.end())
        statement = lowered[start:end]
        read_only_exception = re.search(r"\bread[- ]only (?:review|inspection|spot check)\b", statement)
        if not read_only_exception and not directly_negated(lowered, action_start):
            errors.append(
                ValidationError(
                    "controller-work-hoarding",
                    f"line {line_number_at(text, match.start())}: executor work cannot stay in the controller",
                )
            )

    full_history_hazard = re.compile(
        r"\bfork_turns\b\s*(?:(?::|=|\bto\b)\s*)?[`'\"]?all\b"
        r"|\b(?:create|spawn|dispatch|use|set|inherit|copy|send|give|preserve|retain)\w*\b"
        r"[^.]{0,90}\b(?:full|complete|entire|whole)\b[- ]?(?:controller[- ]?)?\b(?:context|history)\b"
        r"|\b(?:full|complete|entire|whole|unbounded)[- ]history(?: inheritance| fork)?\b"
    )
    independent_reviewer = re.compile(r"\bindependent\b[^.]{0,45}\breviewer\b")
    for hazard in full_history_hazard.finditer(lowered):
        start, end = statement_span(lowered, hazard.start(), hazard.end())
        statement = lowered[start:end]
        explicit_prohibition = re.search(
            r"\b(?:never|cannot|can not|do not|does not|must not)\s+"
            r"(?:use|set|inherit|copy|create|spawn|dispatch)\b[^.]{0,110}"
            r"(?:fork_turns\b[^.]{0,15}\ball\b|(?:full|complete|entire|whole|unbounded)[- ]history)",
            statement,
        )
        safe_rewrite = re.search(
            r"\breplace\s+fork_turns\s*(?::|=|\bto\b)?\s*[`'\"]?all\b[^.]{0,25}\bwith\s+none\b"
            r"|\bflags?\s+fork_turns\s*(?::|=|\bto\b)?\s*[`'\"]?all\b[^.]{0,25}\bas\s+unsafe\b",
            statement,
        )
        if not explicit_prohibition and not safe_rewrite and not action_is_forbidden(
            lowered, hazard.start(), hazard.end()
        ):
            errors.append(
                ValidationError(
                    "full-history-route",
                    f"line {line_number_at(text, hazard.start())}: task creation cannot use full-history inheritance",
                )
            )
            nearby = lowered[max(0, hazard.start() - 180) : min(len(lowered), hazard.end() + 180)]
            if independent_reviewer.search(nearby):
                errors.append(
                    ValidationError(
                        "full-history-review",
                        f"line {line_number_at(text, hazard.start())}: an independent reviewer cannot inherit full controller history",
                    )
                )

    capacity_patterns = (
        re.compile(
            r"\b(?:while|when)\b[^.]{0,55}\b(?:any|a)\b[^.]{0,20}\bspark\b[^.]{0,35}\bactive\b"
            r"[^.]{0,80}\b(?:block|stop|forbid|delay)\w*\b[^.]{0,70}"
            r"\b(?:all|every)\b[^.]{0,45}\bterra\b[^.]{0,65}\b(?:across the project|independent scopes?)\b"
        ),
        re.compile(
            r"\b(?:one|any|a)\b[^.]{0,30}\bactive spark task\b[^.]{0,45}"
            r"\b(?:freez|block|stop|forbid|delay)\w*\b[^.]{0,50}\bterra\b[^.]{0,45}"
            r"\b(?:throughout|across)\b[^.]{0,20}\bproject\b"
        ),
        re.compile(
            r"\bdo not\s+(?:launch|start|dispatch)\b[^.]{0,30}\bterra\b[^.]{0,55}"
            r"\b(?:unrelated|independent) scopes?\b[^.]{0,45}\buntil\b[^.]{0,25}\bspark\b"
        ),
    )
    seen_capacity: set[int] = set()
    for pattern in capacity_patterns:
        for match in pattern.finditer(lowered):
            if match.start() not in seen_capacity:
                seen_capacity.add(match.start())
                errors.append(
                    ValidationError(
                        "global-capacity-block",
                        f"line {line_number_at(text, match.start())}: a Spark fallback guard cannot block independent Terra scopes",
                    )
                )

    notice_context = re.compile(
        r"\broute notice\b|\b(?:tell|announce|notify)\w*\b[^.]{0,70}\b(?:model|effort)\b"
    )
    notice_gate = re.compile(
        r"\b(?P<action>wait|pause|hold|require|obtain|receive|need|request|ask|defer|delay)(?:s|ed|ing)?\b"
        r"[^.]{0,90}\b(?:approval|consent|sign[- ]?off|confirm(?:s|ed|ation)?|response|user repl(?:y|ies))\b"
        r"|\b(?P<after>only after)\b[^.]{0,35}\b(?:response|approval|consent|sign[- ]?off|confirmation|user repl(?:y|ies))\b"
        r"|\b(?P<negative>do not\s+dispatch)\b[^.]{0,45}\buntil\b[^.]{0,35}\buser approv\w*\b"
        r"|\b(?P<prerequisite>approval)\b[^.]{0,45}\bprerequisite\b[^.]{0,35}\bdispatch\b"
    )
    for gate in notice_gate.finditer(lowered):
        action_group = next(name for name in ("action", "after", "negative", "prerequisite") if gate.group(name))
        context = lowered[max(0, gate.start() - 260) : gate.end()]
        start, end = statement_span(lowered, gate.start(), gate.end())
        statement = lowered[start:end]
        explicit_no_gate = re.search(
            r"\b(?:does not|do not|never)\s+(?:wait|pause|hold|ask|request|require|obtain|receive)\b"
            r"|\bask\s+no\s+approval\b"
            r"|\beliminat(?:e|es|ed|ing) the need to\s+(?:wait|ask|obtain|receive)\b"
            r"|\bstop(?:s|ped|ping)? asking\b[^.]{0,55}\bdispatch(?:es|ed|ing)? immediately\b",
            statement,
        )
        legitimate_boundary = re.search(
            r"\bonly for\b[^.]{0,80}\b(?:external|production|deployment|release|purchase|destructive|irreversible)\b",
            statement,
        )
        inherently_negative_gate = action_group in {"negative", "prerequisite"}
        if (
            notice_context.search(context)
            and not explicit_no_gate
            and not legitimate_boundary
            and (inherently_negative_gate or not action_is_forbidden(lowered, gate.start(action_group), gate.end(action_group)))
        ):
            errors.append(
                ValidationError(
                    "dispatch-notice-approval",
                    f"line {line_number_at(text, gate.start())}: a route notice cannot delay dispatch for approval",
                )
            )

    followup_context = re.compile(r"\b(?:followup_task|follow[-_ ]?up)\b")
    switch_patterns = (
        re.compile(
            r"\b(?P<action>switch|change|move|override|set|promote|retarget|reassign)(?:s|ed|d|ing)?\b"
            r"[^.]{0,85}(?:\.\s*)?(?:the\s+)?"
            r"\b(?:model|reasoning effort|terra|spark|luna|sol|high|xhigh|ultra)\b"
        ),
        re.compile(
            r"\b(?P<action>continue)(?:s|d|ing)?\b[^.]{0,40}\bexisting\b[^.]{0,35}"
            r"\b(?:task|follow[- ]?up)\b[^.]{0,35}\bunder\b[^.]{0,20}"
            r"\b(?:terra|spark|luna|sol)(?:\s+(?:high|xhigh|ultra|medium))?\b"
        ),
        re.compile(
            r"\b(?:terra|spark|luna|sol)\b[^.]{0,20}\b(?P<action>replaces?)\b[^.]{0,30}"
            r"\b(?:terra|spark|luna|sol)\b[^.]{0,40}\b(?:same|existing) task\b"
        ),
    )
    seen_switch: set[int] = set()
    for pattern in switch_patterns:
        for match in pattern.finditer(lowered):
            if match.start() in seen_switch:
                continue
            context_start = max(0, match.start() - 180)
            context_end = min(len(lowered), match.end() + 130)
            context = lowered[context_start:context_end]
            start, end = statement_span(lowered, match.start(), match.end())
            statement = lowered[start:end]
            impossible_explanation = re.search(
                r"\bexplains? why\b[^.]{0,85}\b(?:impossible|requires?\s+(?:a\s+)?(?:successor|replacement|new) task)\b",
                statement,
            )
            handoff = re.search(
                r"\b(?P<action>creat(?:e|es|ed|ing)|start(?:s|ed|ing)?|dispatch(?:es|ed|ing)?|"
                r"hand[- ]?off|require(?:s|d)?)\b[^.]{0,50}\b(?:replacement|new|successor) task\b",
                statement,
            )
            positive_handoff = bool(
                handoff
                and not action_is_forbidden(
                    lowered,
                    start + handoff.start("action"),
                    start + handoff.end("action"),
                )
            )
            if (
                followup_context.search(context)
                and not impossible_explanation
                and not positive_handoff
                and not action_is_forbidden(lowered, match.start("action"), match.end("action"))
            ):
                seen_switch.add(match.start())
                errors.append(
                    ValidationError(
                        "inplace-route-switch",
                        f"line {line_number_at(text, match.start())}: a follow-up without route fields cannot switch route",
                    )
                )

    statement_pattern = re.compile(r"[^.!?。！？\n]+")
    for statement_match in statement_pattern.finditer(lowered):
        statement = statement_match.group(0)
        if "ultra" not in statement:
            continue
        action = re.search(
            r"\b(?P<action>(?:always\s+)?(?:use|uses|select|selects|choose|chooses|run|runs|set|sets|make|makes))\b"
            r"[^;]{0,95}\bultra\b"
            r"|\bultra\b[^;]{0,35}\b(?P<passive>shall|must|will)\s+be\s+used\b"
            r"|\bultra\b[^;]{0,25}\b(?P<copula>is|becomes|remains)\b[^;]{0,35}"
            r"\b(?:the\s+)?(?:default|standard|universal)\b",
            statement,
        )
        if not action:
            continue
        action_group = next(name for name in ("action", "passive", "copula") if action.group(name))
        action_start = statement_match.start() + action.start(action_group)
        explicitly_not_default = bool(
            action.group("copula")
            and re.search(
                r"\bultra\s+(?:is|becomes|remains)\s+not\b[^;]{0,25}\b(?:default|standard|universal)\b",
                action.group(0),
            )
        )
        bounded_ultra = all(
            re.search(pattern, statement)
            for pattern in (
                r"\bonly\b",
                r"\blarge\b",
                r"\bparallel(?:izable)?\b",
                r"\bindependent\b",
                r"\bno shared mutable files\b",
            )
        ) and not re.search(r"\bnot independent\b|\bshares? mutable files\b", statement)
        blanket_scope = re.search(
            r"\b(?:always|universally|every|all|each|default|standard|routine)\b"
            r"|\b(?:executor|child) (?:tasks?|objectives?|work)\b",
            statement,
        )
        if (
            blanket_scope
            and not explicitly_not_default
            and not bounded_ultra
            and not action_is_forbidden(lowered, action_start, action_start + len(action.group(action_group)))
        ):
            errors.append(
                ValidationError(
                    "blanket-ultra",
                    f"line {line_number_at(text, statement_match.start())}: Ultra cannot be the blanket executor default",
                )
            )

    route_assumption = re.compile(
        r"\b(?P<action>assume|guess|trust)(?:s|d|ing)?\b[^.]{0,85}\b(?:requested )?route\b"
        r"[^.]{0,55}\b(?:accepted|resolved|correct)\b[^.]{0,65}\b(?:substantive brief|substantive work|start work)\b"
    )
    early_route_work = re.compile(
        r"\b(?P<action>start|begin|send)(?:s|ning|ing|t)?\b[^.]{0,50}"
        r"\b(?:substantive work|substantive brief)\b[^.]{0,45}\bbefore\b[^.]{0,40}\broute metadata\b"
    )
    for pattern in (route_assumption, early_route_work):
        for match in pattern.finditer(lowered):
            if not action_is_forbidden(lowered, match.start("action"), match.end("action")):
                errors.append(
                    ValidationError(
                        "unverified-route-work",
                        f"line {line_number_at(text, match.start())}: substantive work cannot start before route verification",
                    )
                )

    unsafe_handshake = re.compile(
        r"\bhandshake[- ]only task\b[^.]{0,100}\b(?P<action>read|write|modify|call|use)(?:s|d|ing)?\b"
        r"[^.]{0,55}\b(?:repository|project|files?|tools?)\b"
    )
    for match in unsafe_handshake.finditer(lowered):
        start, end = statement_span(lowered, match.start(), match.end())
        statement = lowered[start:end]
        explicit_no_access = re.search(
            r"\bno project reads, writes, or tool calls\b"
            r"|\b(?:cannot|can not|do not|never)\s+(?:read|write|modify|call|use)\b",
            statement,
        )
        if not explicit_no_access and not action_is_forbidden(
            lowered, match.start("action"), match.end("action")
        ):
            errors.append(
                ValidationError(
                    "unsafe-routing-handshake",
                    f"line {line_number_at(text, match.start())}: a routing handshake cannot access the project or tools",
                )
            )

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

    fast_solicitation = re.compile(
        r"\b(?:ask|suggest|recommend|offer|propose)\b[^.\n]{0,100}"
        r"\b(?:fast(?: mode)?|priority service)\b"
    )
    for match in fast_solicitation.finditer(lowered):
        if not directly_negated(lowered, match.start()):
            errors.append(
                ValidationError(
                    "fast-solicitation",
                    f"line {line_number_at(text, match.start())}: controller cannot solicit Fast service",
                )
            )

    missing_speed_block = re.compile(
        r"\bmissing\b[^.\n]{0,50}\b(?:speed|service[- ]tier)\b[^.\n]{0,40}"
        r"\b(?:blocks?|stops?|waits?|asks?)\b"
    )
    for match in missing_speed_block.finditer(lowered):
        if not directly_negated(lowered, match.start()):
            errors.append(
                ValidationError(
                    "missing-speed-block",
                    f"line {line_number_at(text, match.start())}: missing speed field must use platform default",
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
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != EXPECTED_CORE_SHA256:
        errors.append(
            ValidationError(
                "core-digest",
                "core skill differs from the exact reviewed contract; review it and update the bound digest",
            )
        )
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
    if "No lane repeats the same incremental review loop after two returns" not in visible:
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
