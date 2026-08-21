#!/usr/bin/env python3
"""Behavior-contract tests for Project Lead's risk-based operating modes."""

from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "project-lead" / "SKILL.md"
README_EN = ROOT / "README.md"
README_ZH = ROOT / "README.zh-CN.md"
INSTALL_REFERENCE = (
    ROOT / "skills" / "project-lead" / "references" / "skill-installation-safety.md"
)


def section(text: str, heading: str) -> str:
    lines = text.splitlines()
    start = lines.index(heading)
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if line.startswith("#"):
            next_level = len(line) - len(line.lstrip("#"))
            if next_level <= level:
                end = index
                break
    return "\n".join(lines[start:end])


class ProjectLeadModeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")

    def test_core_skill_stays_within_context_budget(self) -> None:
        self.assertLessEqual(len(self.skill.split()), 1800)

    def test_low_risk_lane_is_default_and_skips_independent_review(self) -> None:
        low_risk = section(self.skill, "### Low-risk lane — default")
        self.assertIn("`independent_review: none`", low_risk)
        self.assertIn("Do not create an independent reviewer", low_risk)
        self.assertIn("controller verification is acceptance", low_risk)

    def test_approval_depends_on_action_and_missing_authority(self) -> None:
        for phrase in (
            "Approval follows the proposed action and missing authority, not the subject matter or review lane",
            "Elevated alone never creates `blocked_on_user`",
            "the controller authorizes dispatch, local reversible preparation, focused checks, required independent review, and in-scope repair",
            "A real platform approval card is relayed only when the user must operate it",
            "never invent a prose approval gate",
        ):
            self.assertIn(phrase, self.skill)

    def test_user_blockers_are_scoped_and_expire(self) -> None:
        for phrase in (
            "Bind `blocked_on_user` to the objective, candidate or scope version, exact action or decision, and missing authority",
            "Clear or supersede it when the user decides, existing authority covers the action, the action disappears, or its objective, candidate, or scope changes",
            "Never inherit it by label alone",
            "dispatch one in-scope root-cause repair without asking",
        ):
            self.assertIn(phrase, self.skill)

    def test_controller_delegates_project_artifacts_and_long_validation(self) -> None:
        for phrase in (
            "classify `work_location: controller | executor`",
            "Controller work is intake, routing, no-code cross-module decisions, acceptance, reporting, and quick read-only spot checks",
            "Repository plans, designs, source, tests, configuration, non-obvious debugging, multi-file or substantive edits, repeated repair, and long or broad validation belong to an executor",
            "Do not split executor work into small direct steps",
            "Concurrency or convenience never moves executor work into the controller",
            "Acceptance reconciles executor evidence and at most one focused spot check; it does not require the controller to rerun full suites or long manual validation",
        ):
            self.assertIn(phrase, self.skill)

    def test_standard_lane_batches_one_review_and_one_repair_review(self) -> None:
        standard = section(self.skill, "### Standard lane")
        self.assertIn("`independent_review: one_batched_terra`", standard)
        self.assertIn("At most one automatic incremental re-review", standard)
        self.assertIn("Minor findings never trigger return or re-review", standard)

    def test_elevated_lane_keeps_sol_gate_for_concrete_risk(self) -> None:
        elevated = section(self.skill, "### Elevated lane")
        self.assertIn("`independent_review: sol_required`", elevated)
        for risk in (
            "authentication",
            "payments",
            "data loss",
            "privacy",
            "cryptography",
            "security compliance",
            "migration",
            "shared contract",
            "deployment",
            "release",
            "destructive",
        ):
            self.assertIn(risk, elevated.lower())

    def test_missing_evidence_does_not_automatically_create_architecture_work(self) -> None:
        self.assertIn(
            "Missing evidence means inspect or delegate evidence collection; ask only for a user-exclusive product fact or authority.",
            self.skill,
        )
        self.assertIn(
            "An Elevated trigger changes the review lane but does not by itself create an architecture phase.",
            self.skill,
        )
        self.assertNotIn(
            "If the classification evidence is incomplete, use `system`",
            self.skill,
        )
        self.assertNotIn("or Elevated area", self.skill)

    def test_review_loop_has_a_hard_automatic_cap(self) -> None:
        self.assertIn("No lane repeats the same incremental review loop after two returns", self.skill)
        for phrase in (
            "dispatch one in-scope root-cause repair without asking",
            "Standard closes recorded findings from refreshed executor evidence plus one focused spot check",
            "unproven findings stay `RETURN`",
            "Elevated dispatches one in-scope root-cause repair and one final independent closure review without asking",
            "If that review returns, keep `RETURN`, report `blocked_on_quality`, and never launch a fourth review",
        ):
            self.assertIn(phrase, self.skill)

    def test_model_routing_asks_once_per_project_then_stops_reprompting(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Ask once", routing)
        self.assertIn("`model_routing_authority: approved | fixed_default | pending`", routing)
        self.assertIn("do not ask again for each choice or switch", routing)
        self.assertIn("Until approved", routing)

    def test_every_objective_gets_a_fresh_explicit_model_decision(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Before every new objective, dispatch, or substantive follow-up", routing)
        self.assertIn("`execution_route: {model, reasoning_effort, service_tier}`", routing)
        self.assertIn("never inherit a previous route", routing)
        self.assertIn("Pass supported fields explicitly", routing)
        self.assertIn("A completed objective authorizes nothing for the next", routing)

    def test_spark_is_an_all_conditions_allowlist_with_terra_fallback(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Spark uses `high`; use `xhigh` only when the dispatch tool exposes it", routing)
        for phrase in (
            "Low-risk conditions",
            "exact scope/checks",
            "accepted pattern",
            "reversibility",
            "focused verification",
            "no Elevated",
            "non-obvious debugging",
            "cross-module",
        ):
            self.assertIn(phrase, routing)
        self.assertIn("If Spark is unavailable or ineligible before dispatch, use Terra high", routing)

    def test_complex_follow_up_uses_a_verified_route_without_duplicate_ownership(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("A follow-up without model and effort fields cannot switch them", routing)
        self.assertIn("finish or interrupt the current turn", routing)
        self.assertIn("hand off the same logical scope to one correctly routed replacement task", routing)
        self.assertIn("never overlap owners", routing)
        self.assertIn("never use `all` or omitted full-history inheritance", routing)

    def test_unavailable_spark_capacity_falls_back_explicitly_to_terra(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("If Spark is unavailable or ineligible before dispatch, use Terra high", routing)
        self.assertIn("Never start a Terra fallback for the same objective or logical scope while its Spark turn is active", routing)
        self.assertIn("Independent scopes may continue in parallel", routing)
        self.assertIn("confirmed rejection, interruption, or terminal state", routing)

    def test_execution_and_review_model_choices_are_independent(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Execution-model routing never changes the review lane", routing)
        self.assertIn("Spark never reviews itself", routing)

    def test_controller_selects_a_supported_reasoning_effort_per_dispatch(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        for phrase in (
            "`execution_route: {model, reasoning_effort, service_tier}`",
            "Terra uses `high` by default, `xhigh` for non-obvious debugging, cross-module reasoning, or complex design",
            "`ultra` only for a large parallelizable objective with independent workstreams",
            "Spark uses `high`; use `xhigh` only when the dispatch tool exposes it",
            "Luna uses `medium` for ordinary evidence extraction, `high` for dense multi-source evidence, and `xhigh` only for hard contradictions",
            "Only select combinations exposed by the dispatch tool; never invent a model or effort",
        ):
            self.assertIn(phrase, routing)

    def test_cross_model_dispatch_avoids_full_history_inheritance_and_verifies_route(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        for phrase in (
            "`fork_turns: none` or a bounded positive turn count",
            "never use `all` or omitted full-history inheritance",
            "Any independent reviewer also uses no or bounded history even when its route matches the controller",
            "Verify the accepted task's resolved model and effort before substantive work",
            "If dispatch atomically exposes the resolved route, compare it before work",
            "Otherwise create a handshake-only task with no project reads, writes, or tool calls",
            "Send the substantive brief only after metadata confirms the route",
            "If the route cannot be observed, report `blocked_on_routing`",
            "A follow-up without model and effort fields cannot switch them",
            "hand off the same logical scope to one correctly routed replacement task",
            "never overlap owners",
        ):
            self.assertIn(phrase, routing)

    def test_every_dispatch_announces_route_without_waiting_for_approval(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        for phrase in (
            "Immediately before every creation or substantive follow-up, tell the user",
            "即将派发：<任务>｜模型：<model>｜档位：<reasoning_effort>｜速度：普通",
            "informational, never an approval gate",
            "dispatch immediately without waiting for a reply",
            "issue a corrected notice before redispatch",
            "Replace `普通` with `Fast` only for an exact objective already authorized below",
        ):
            self.assertIn(phrase, routing)

    def test_child_speed_defaults_to_standard_without_fast_prompt(self) -> None:
        speed = section(self.skill, "## Speed tier")
        for phrase in (
            "Standard/default is the child default unless the user explicitly requested Fast for that exact objective",
            "The controller's own service tier is user-configured and grants no child authority",
            "Model-routing authority never authorizes Fast/priority child service",
            "Never ask, suggest, recommend, or offer Fast",
            "When dispatch has no service-tier field, omit any Fast/priority override and dispatch with the platform default",
            "Absence of a speed field is not a reason to block or ask",
            "A new child objective resets to Standard/default",
            "observable evidence shows unexpected Fast/priority, stop further child follow-ups and report",
            "Prompt text cannot change the transport service tier",
        ):
            self.assertIn(phrase, speed)

    def test_luna_is_a_bounded_read_only_information_assistant(self) -> None:
        monitoring = section(self.skill, "## Monitoring and blockers")
        for phrase in (
            "`gpt-5.6-luna medium`",
            "one project-scoped read-only Luna assistant scope",
            "large or repetitive enough to materially reduce controller context or cost",
            "summarize long task reports, logs, and test output",
            "extract progress, evidence, blockers, pending approvals, and terminal state",
            "deduplicate repeated status and draft the four-line user update",
            "A Luna result is advisory",
            "verify the primary evidence before acting",
            "Do not use Luna for a few lines, routine updates, or to appear busy",
            "cannot write or modify code, choose execution models or review lanes, make architecture decisions, review, accept, or mark work complete",
            "Deduplicate by phase plus evidence",
            "apply the route handoff rule when effort changes",
        ):
            self.assertIn(phrase, monitoring)

    def test_controller_keeps_event_wait_open_until_relay_is_safe(self) -> None:
        monitoring = section(self.skill, "## Monitoring and blockers")
        for phrase in (
            "immediately enter `wait_threads`",
            "Do not send a final answer while any promised target is accepted, queued, or running",
            "A timeout is not a state change; reuse the returned cursor",
            "do not read tasks, call Luna, or report unchanged status",
            "relay it in commentary and keep waiting for the rest",
            "End the turn only when all promised targets are terminal",
            "automatic relay cannot be guaranteed",
            "an idle controller, the 30-minute rule, or Luna can wake itself",
        ):
            self.assertIn(phrase, monitoring)

    def test_public_docs_explain_the_luna_information_assistant(self) -> None:
        readme_en = README_EN.read_text(encoding="utf-8")
        for phrase in (
            "## Luna as a read-only information assistant",
            "large or repetitive evidence",
            "never writes code, selects models, reviews, accepts, or marks work complete",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## Luna 只读信息助理",
            "大量或重复的证据",
            "不会写代码、选择模型、审查、验收或宣布完成",
        ):
            self.assertIn(phrase, readme_zh)

    def test_public_docs_explain_event_driven_completion_relay(self) -> None:
        readme_en = README_EN.read_text(encoding="utf-8")
        for phrase in (
            "## Event-driven completion relay",
            "keeps the controller turn open with `wait_threads`",
            "Luna and the 30-minute rule cannot wake an idle controller",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## 事件驱动的完成回传",
            "使用 `wait_threads` 保持总控回合",
            "Luna 和 30 分钟规则都不能唤醒空闲总控",
        ):
            self.assertIn(phrase, readme_zh)

    def test_public_docs_explain_safe_automatic_model_routing(self) -> None:
        readme_en = README_EN.read_text(encoding="utf-8")
        for phrase in (
            "## Automatic execution-model routing",
            "authorizes automatic routing once per project",
            "For every new objective",
            "never inherits the previous objective's route",
            "chooses both the model and reasoning effort",
            "announces the task, model, effort, and actual speed immediately before dispatch",
            "does not wait for approval",
            "full-history inheritance is never used",
            "handshake-only task with no project reads, writes, or tool calls",
            "`blocked_on_routing`",
            "independent scopes may continue in parallel",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## 自动选择执行模型",
            "每个项目只授权一次自动路由",
            "每个新目标都会根据",
            "绝不继承上一个目标的路由",
            "同时选择模型和推理档位",
            "派发前会告知任务、模型、档位和实际速度",
            "不会等待批准",
            "不能继承完整历史",
            "禁止读取、修改项目或调用工具的握手任务",
            "`blocked_on_routing`",
            "无关范围仍可并行推进",
        ):
            self.assertIn(phrase, readme_zh)

    def test_public_docs_separate_child_speed_from_controller_speed(self) -> None:
        readme_en = README_EN.read_text(encoding="utf-8")
        for phrase in (
            "## Child tasks use Standard speed by default",
            "Fast speed is not the Low-risk lane",
            "The controller may keep its user-configured speed",
            "every new child task starts at Standard/default",
            "never asks whether to use Fast",
            "explicitly requests Fast",
            "omits any Fast/priority override and uses the platform Standard/default",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## 下发任务默认使用普通速度",
            "Fast 速度不等于低风险通道",
            "总控本身可以保留用户当前设置的速度",
            "每个新执行任务默认使用 Standard/普通速度",
            "不会主动询问是否使用 Fast",
            "用户主动明确要求",
            "不传入任何 Fast/priority 覆盖",
        ):
            self.assertIn(phrase, readme_zh)

    def test_public_docs_explain_controller_authority_and_delegation(self) -> None:
        readme_en = README_EN.read_text(encoding="utf-8")
        for phrase in (
            "## Controller authority and execution boundary",
            "Elevated review does not itself require user approval",
            "plans, designs, source, tests, complex debugging, and long validation belong to executor tasks",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## 总控审批权与执行边界",
            "Elevated 审查本身不需要用户批准",
            "计划、设计、源码、测试、复杂调试和长验证都属于执行任务",
        ):
            self.assertIn(phrase, readme_zh)
        self.assertNotIn("or an Elevated trigger", readme_en)
        self.assertNotIn("或高风险触发项", readme_zh)

    def test_user_feedback_is_plain_and_progress_first(self) -> None:
        for line in (
            "已完成：<用户能理解的结果>",
            "当前结果：<能否使用或验证>",
            "阻塞：无 | <需要用户处理的唯一事项>",
            "下一步：<一个最有价值的动作>",
        ):
            self.assertIn(line, self.skill)
        self.assertIn(
            "Outside the required route notice, do not expose ledger fields, SHA values, model names, review IDs, or other routing",
            self.skill,
        )
        self.assertIn("Ship the smallest usable vertical slice", self.skill)

    def test_installation_detail_is_progressively_disclosed(self) -> None:
        self.assertTrue(INSTALL_REFERENCE.is_file())
        self.assertIn(
            "Read `references/skill-installation-safety.md` only after the user approves an exact candidate",
            self.skill,
        )
        self.assertIn("## Fail-closed installation transaction", INSTALL_REFERENCE.read_text(encoding="utf-8"))

    def test_skill_selection_is_automatic_but_installation_requires_approval(self) -> None:
        supporting = section(self.skill, "## Supporting skills and capability discovery")
        self.assertIn("automatically decide whether an installed supporting skill is needed", supporting)
        self.assertIn("select and invoke one without asking the user to remember its name", supporting)
        self.assertIn("Ordinary bounded work selects `none`", supporting)

        readme_en = README_EN.read_text(encoding="utf-8")
        for phrase in (
            "## Automatic skill routing and discovery",
            "You describe the outcome, not the skill name",
            "automatically selects and invokes",
            "asks before any installation",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## 自动选择与搜索 Skill",
            "你只需要描述目标，不需要记住 Skill 名称",
            "自动选择并调用",
            "任何安装前都会先征得你的同意",
        ):
            self.assertIn(phrase, readme_zh)


if __name__ == "__main__":
    unittest.main()
