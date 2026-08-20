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
        self.assertIn(
            "controller may handle a brief, isolated, reversible change directly",
            low_risk,
        )

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
            "Missing evidence means inspect or ask; it does not by itself make work system architecture.",
            self.skill,
        )
        self.assertNotIn(
            "If the classification evidence is incomplete, use `system`",
            self.skill,
        )

    def test_review_loop_has_a_hard_automatic_cap(self) -> None:
        self.assertIn("No lane may launch a third automatic review", self.skill)

    def test_model_routing_asks_once_per_project_then_stops_reprompting(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("ask once", routing)
        self.assertIn("`model_routing_authority: approved | fixed_default | pending`", routing)
        self.assertIn("Do not ask again for each model choice or switch", routing)
        self.assertIn("Until authority is approved", routing)

    def test_every_objective_gets_a_fresh_explicit_model_decision(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Before every new objective, dispatch, or substantive follow-up", routing)
        self.assertIn("`execution_model_decision`", routing)
        self.assertIn("Never inherit a previous objective's model", routing)
        self.assertIn("pass the chosen model explicitly", routing)
        self.assertIn("A completed Spark objective does not authorize Spark for the next objective", routing)

    def test_spark_is_an_all_conditions_allowlist_with_terra_fallback(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Choose `gpt-5.3-codex-spark high` only when every condition is true", routing)
        for phrase in (
            "Low-risk lane",
            "exact target scope",
            "accepted interface or pattern",
            "reversible",
            "focused verification",
            "no Elevated trigger",
            "non-obvious debugging",
            "cross-module",
        ):
            self.assertIn(phrase, routing)
        self.assertIn(
            "If any Spark condition is false, unknown, or becomes false, select `gpt-5.6-terra high`",
            routing,
        )

    def test_complex_follow_up_overrides_spark_on_the_same_task(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("`model_escalation_required`", routing)
        self.assertIn("same owner and task", routing)
        self.assertIn("next substantive follow-up", routing)
        self.assertIn("explicit `gpt-5.6-terra high` override", routing)
        self.assertIn("cannot change a running turn mid-response", routing)
        self.assertIn("Do not create a replacement task", routing)

    def test_unavailable_spark_capacity_falls_back_explicitly_to_terra(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Task fit and model availability are separate checks", routing)
        self.assertIn("Spark quota is exhausted or the model is unavailable before dispatch", routing)
        self.assertIn("explicit `gpt-5.6-terra high` capacity fallback", routing)
        self.assertIn("Never send a Terra fallback while a Spark turn is accepted, running, or queued", routing)
        self.assertIn("confirmed rejection, interruption, or terminal state", routing)
        self.assertIn("report the blocker instead of creating concurrent work", routing)

    def test_execution_and_review_model_choices_are_independent(self) -> None:
        routing = section(self.skill, "## Execution model routing")
        self.assertIn("Execution-model routing never changes the review lane", routing)
        self.assertIn("Spark never reviews its own implementation", routing)

    def test_standard_speed_is_default_and_fast_needs_separate_authority(self) -> None:
        speed = section(self.skill, "## Speed tier")
        for phrase in (
            "Standard/default is mandatory for controllers and child turns",
            "Model-routing authority never authorizes Fast/priority service",
            "Fast requires separate explicit user approval for one objective",
            "never infer it from the Low-risk lane, Spark, or urgency",
            "dispatch cannot verify a Standard child, stop and ask the user to disable Fast",
            "Prompt text cannot change the transport service tier",
        ):
            self.assertIn(phrase, speed)

    def test_luna_is_a_bounded_read_only_information_assistant(self) -> None:
        monitoring = section(self.skill, "## Monitoring and blockers")
        for phrase in (
            "`gpt-5.6-luna medium`",
            "one project-scoped read-only Luna assistant task",
            "large or repetitive enough to materially reduce controller context or cost",
            "summarize long task reports, logs, and test output",
            "extract progress, evidence, blockers, pending approvals, and terminal state",
            "deduplicate repeated status and draft the four-line user update",
            "A Luna result is advisory",
            "verify the primary evidence before acting",
            "Do not use Luna for a few lines, routine updates, or to appear busy",
            "cannot write or modify code, choose execution models or review lanes, make architecture decisions, review, accept, or mark work complete",
            "deduplicate by phase plus evidence",
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
            "Every new objective is classified again",
            "never inherits the previous objective's model",
            "Spark-to-Terra escalation reuses the same task",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## 自动选择执行模型",
            "每个项目只授权一次自动路由",
            "每个新目标都会重新判断",
            "绝不继承上一个目标的模型",
            "Spark 升级到 Terra 时复用同一个任务",
        ):
            self.assertIn(phrase, readme_zh)

    def test_public_docs_separate_low_risk_work_from_fast_speed(self) -> None:
        readme_en = README_EN.read_text(encoding="utf-8")
        for phrase in (
            "## Standard speed by default",
            "Fast speed is not the Low-risk lane",
            "separate explicit approval",
        ):
            self.assertIn(phrase, readme_en)

        readme_zh = README_ZH.read_text(encoding="utf-8")
        for phrase in (
            "## 默认使用普通速度",
            "Fast 速度不等于低风险通道",
            "单独明确授权",
        ):
            self.assertIn(phrase, readme_zh)

    def test_user_feedback_is_plain_and_progress_first(self) -> None:
        for line in (
            "已完成：<用户能理解的结果>",
            "当前结果：<能否使用或验证>",
            "阻塞：无 | <需要用户处理的唯一事项>",
            "下一步：<一个最有价值的动作>",
        ):
            self.assertIn(line, self.skill)
        self.assertIn(
            "Do not expose ledger fields, SHA values, model names, review IDs, or internal routing",
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
