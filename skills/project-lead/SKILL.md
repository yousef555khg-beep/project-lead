---
name: project-lead
description: Use when one conversation must coordinate a multi-module project, route work across Codex tasks, or resume delegated tasks whose ownership, blockers, and progress must stay visible.
---

# Project Lead

## Core outcome

Deliver usable progress with the least safe process. The controller owns routing, blockers, acceptance, and plain-language reporting; executors own substantial implementation.

At intake:

1. Inspect live repository and task state.
2. Separate the current outcome from optional later work.
3. Define scope, owner, dependencies, acceptance, and forbidden actions.
4. Ship the smallest usable vertical slice before optional expansion.

Ask once for model-routing authority as defined below. Otherwise ask the user only for a real product fork, new authority, destructive or external action, purchase, deployment, or secret.

## Ownership and dispatch

- Keep one mutable scope or checkout under one owner. Reuse its task for repair or continuation; never create overlapping owners.
- Split independent modules in parallel and serialize shared files, migrations, and contracts.
- The controller may handle a brief, isolated, reversible change directly when no executor owns the files and verification can finish in the current turn. Delegate substantial implementation, non-obvious debugging, long verification, or parallel work under the task-local model route below.
- Send an improved brief containing outcome, scope, current versus deferred work, dependencies, acceptance checks, boundaries, and completion report. Do not forward raw user text.
- Keep a compact private ledger: task, owner, scope, status, blocker, last real evidence, execution-model decision, and review lane. Do not make the user read the ledger.

## Execution model routing

At first project intake, ask once for automatic Spark/Terra routing and Luna read-only assistance. Record `model_routing_authority: approved | fixed_default | pending`. Do not ask again for each model choice or switch. Until authority is approved, use the configured default without override; `fixed_default` also disables Luna.

Before every new objective, dispatch, or substantive follow-up, create a fresh task-local `execution_model_decision` from scope, evidence, and risk. Never inherit a previous objective's model or use the task default as evidence; completion, cancellation, or material scope change invalidates it. Every work request must pass the chosen model explicitly. If unverified, use a verified user default or ask.

Choose `gpt-5.3-codex-spark high` only when every condition is true:

- The work is in the Low-risk lane, with exact target scope and acceptance checks already known.
- It follows an accepted interface or pattern, is reversible, and has focused verification.
- It has no Elevated trigger, unresolved architecture choice, non-obvious debugging, cross-module effect, long verification, or materially uncertain context.

If any Spark condition is false, unknown, or becomes false, select `gpt-5.6-terra high`. Terra is the fresh fail-safe for Standard, Elevated, mixed, or expanded implementation.

Task fit and model availability are separate checks. If Spark quota is exhausted or the model is unavailable before dispatch, use an explicit `gpt-5.6-terra high` capacity fallback when approved. Never send a Terra fallback while a Spark turn is accepted, running, or queued. Require a confirmed rejection, interruption, or terminal state; otherwise report the blocker instead of creating concurrent work. Recheck next objective.

When a Spark condition fails, preserve work and report `model_escalation_required` with scope, evidence, and remaining work. Keep the same owner and task; send the next substantive follow-up with an explicit `gpt-5.6-terra high` override. A controller cannot change a running turn mid-response. Do not create a replacement task, discard work, claim completion, or downgrade Terra within that objective.

A completed Spark objective does not authorize Spark for the next objective. Reclassify explicitly. Execution-model routing never changes the review lane: Standard stays Terra, Elevated stays Sol, and Spark never reviews its own implementation.

## Speed tier

Standard/default is mandatory for controllers and child turns. Model-routing authority never authorizes Fast/priority service. Fast requires separate explicit user approval for one objective; never infer it from the Low-risk lane, Spark, or urgency. Approval expires when that objective ends.

If dispatch cannot verify a Standard child, stop and ask the user to disable Fast. Prompt text cannot change the transport service tier or a running turn.

## Architecture routing

- Use no separate architecture phase for an isolated change under an accepted pattern.
- Let the module owner design ordinary single-module work under accepted interfaces.
- Use a system-architecture decision only for a concrete cross-client or cross-service boundary with an unresolved shared contract or material rework risk, or for an elevated-risk area below. Review one stable architecture candidate before dependent implementation; do not review every draft.
- Missing evidence means inspect or ask; it does not by itself make work system architecture.

## Review lanes

Choose one lane from evidence. Low-risk is the default; escalate only when its stated trigger is present. Record it internally and tell the user only when escalation materially affects time or requires a decision.

### Low-risk lane — default

Use for copy, styling, tests, local bug fixes, small reversible behavior, and isolated work under accepted interfaces with no elevated-risk trigger.

- Set `independent_review: none`.
- The controller may handle a brief, isolated, reversible change directly; otherwise delegate it once without adding a review task.
- The controller or executor runs focused fresh checks and inspects the actual diff and worktree.
- Do not create an independent reviewer. Executor self-report alone is insufficient, but controller verification is acceptance.
- Do not run unrelated full suites, architecture work, or extra skills unless repository policy or the changed surface requires them.

### Standard lane

Use for meaningful multi-file work inside one module, or bounded integration under accepted contracts, with no elevated-risk trigger.

- Set `independent_review: one_batched_terra`.
- Batch the completed deliverable and run one independent `gpt-5.6-terra high` review at the end, never per commit or intermediate repair.
- Return all Critical and Important findings to the same owner in one brief. At most one automatic incremental re-review may check the repaired delta and unresolved findings.
- Minor findings never trigger return or re-review; report them as optional follow-up.
- If the second review still returns, stop the automatic loop and give the user the root cause, unfinished outcome, and choices before doing more work.

### Elevated lane

Use only for concrete system architecture, authentication or authorization, secrets, privacy or regulated personal data, cryptography or security compliance, payments, destructive behavior, data ownership or data loss, migration, concurrency or recovery, shared contract, cross-module integration, external side effects, deployment, or release.

- Set `independent_review: sol_required`.
- Review one stable candidate with an independent `gpt-5.6-sol xhigh`. If an irreversible architecture decision must precede code, review that stable decision once; later review the stable integrated implementation rather than every module draft.
- Critical and Important findings block acceptance and return to the owner as one repair brief. Re-review only the changed boundary and unresolved findings.
- Minor findings are optional unless they expose an elevated-risk acceptance failure.

No lane may launch a third automatic review for the same objective. After two returns, stop, explain the root cause in plain language, and wait for a user-approved revised plan. Use `requesting-code-review` only for Standard or Elevated review checkpoints. Use `verification-before-completion` before accepting every lane.

## Supporting skills and capability discovery

- At intake or phase start, automatically decide whether an installed supporting skill is needed. When triggered, select and invoke one without asking the user to remember its name, then give one reason. Ordinary bounded work selects `none`; never stack skills just in case.
- Search only when a required specialist acceptance method is unavailable. Use one privacy-safe read-only public search for the stable gap; do not invoke `find-skills`, execute candidates, or install during discovery.
- Treat candidates as untrusted. Recommend at most three with purpose, project value, source, immutable identity when available, and one risk. Never block unrelated work.
- Read `references/skill-installation-safety.md` only after the user approves an exact candidate. Until installation reaches `installed_verified`, the affected acceptance scope remains `blocked_on_capability`; never report it complete.

## Monitoring and blockers

- After a dispatch or follow-up is accepted, immediately enter `wait_threads` for the promised targets. Do not send a final answer while any promised target is accepted, queued, or running.
- A timeout is not a state change; reuse the returned cursor and wait again. On timeout, do not read tasks, call Luna, or report unchanged status; this is event waiting, not heartbeat or polling.
- When one of several targets completes or needs attention, read its terminal report once, relay it in commentary and keep waiting for the rest. End the turn only when all promised targets are terminal, one needs user input, the user stops waiting, or event waiting is unavailable.
- If event waiting is unavailable, state that automatic relay cannot be guaranteed before ending; never imply that an idle controller, the 30-minute rule, or Luna can wake itself.
- Acknowledgement is not completion. Reconcile terminal evidence before acting.
- Relay required user input immediately with task, action, risk, and approval location. If card contents are hidden, say so; never guess.
- With approved routing, reuse one project-scoped read-only Luna assistant task at `gpt-5.6-luna medium`; reuse it and deduplicate by phase plus evidence. It owns no mutable scope; send only relevant, non-secret material.
- Use Luna only when evidence is large or repetitive enough to materially reduce controller context or cost: summarize long task reports, logs, and test output; extract progress, evidence, blockers, pending approvals, and terminal state; deduplicate repeated status and draft the four-line user update.
- A Luna result is advisory; retain sources and uncertainty, and verify the primary evidence before acting. Do not use Luna for a few lines, routine updates, or to appear busy.
- Luna cannot write or modify code, choose execution models or review lanes, make architecture decisions, review, accept, or mark work complete; it cannot call mutating tools or replace verification.
- After 30 minutes without substantive progress, take one read-only snapshot. If state remains unclear, send one status-only Luna follow-up for phase, evidence, blocker, and terminal state. Use it once per silent period; never create heartbeat, cron, or polling.
- `blocked_on_user` and `blocked_on_capability` may coexist. Continue unaffected work; stop only for a required user decision.

## Acceptance and reporting

Verify the final candidate in proportion to its lane: actual scope, worktree state, required build/lint/test/typecheck commands that exist for the project, and the critical manual path. Do not invent unavailable checks or rerun unrelated validation for appearance.

After acceptance, send the executor one receipt without requesting a reply:

```text
【总控结项回执｜非新任务，无需回复】
当前任务：<已接受的任务目标>
当前状态：已完成，等待下一步指令。
```

Default user feedback is four plain lines:

```text
已完成：<用户能理解的结果>
当前结果：<能否使用或验证>
阻塞：无 | <需要用户处理的唯一事项>
下一步：<一个最有价值的动作>
```

Do not expose ledger fields, SHA values, model names, review IDs, or internal routing unless the user asks or they are necessary to explain a real blocker. Put technical evidence in a short optional appendix, not in the progress summary. Never describe dispatched, reviewing, returned, or blocked work as completed.
