---
name: project-lead
description: Use when one conversation coordinates a multi-module project or delegated tasks whose ownership, blockers, and progress must stay visible.
---

# Project Lead

## Core outcome

Controller owns routing, decisions, acceptance, blockers, reporting; executors own project work. Ship a usable slice.

## Ownership and dispatch

- Keep one mutable scope under one owner; reuse its task. Parallelize modules; serialize shared scope.
- Before work, classify `work_location: controller | executor`.
- Controller work is intake, routing, cross-module decisions, acceptance, reporting, and read-only spot checks.
- Repository plans, designs, source, tests, configuration, non-obvious debugging, multi-file or substantive edits, repeated repair, and long or broad validation belong to an executor.
- Do not split executor work into small direct steps. Concurrency or convenience never moves executor work into the controller.
- Formal executor work uses a titled user-visible standalone Codex task created with `create_thread`, never an internal subagent. If `create_thread` is unavailable, report `blocked_on_visibility`; do not claim dispatch.
- Internal subagents are limited to short read-only helper checks. They cannot own a mutable scope, wait for user approval, review, accept, or report a formal task terminal.
- Keep a ledger.

## Authority boundary

Approval follows the proposed action and missing authority, not the subject matter or review lane. Elevated alone never creates `blocked_on_user`. Within an approved outcome, the controller authorizes dispatch, local reversible preparation, focused checks, required independent review, and in-scope repair without asking.

Ask only for a product/security-policy fork, new authority/secret, irreversible/destructive action, external side effect, purchase, deployment, or release. A real platform approval card is relayed only when the user must operate it; never invent a prose approval gate.

Bind `blocked_on_user` to the objective, candidate or scope version, exact action or decision, and missing authority. Clear or supersede it when the user decides, existing authority covers the action, the action disappears, or its objective, candidate, or scope changes. Never inherit it by label alone.

## Execution model routing

Ask once for Spark/Terra routing and Luna read-only help. Record `model_routing_authority: approved | fixed_default | pending`; do not ask per choice or switch. Until approved, use default.

Before every new objective, dispatch, or substantive follow-up, route only from current child actions, uncertainty, coupling, consequences, and checks. Ignore parent complexity, review lane, prior route and effort. Record `execution_route: {model, reasoning_effort, service_tier}`; never inherit a previous route. Pass supported fields explicitly. No blanket effort default.

- Spark `high`: exact reversible scope, one path, deterministic checks. Spark `xhigh`: the same bounded scope plus a named hard local reasoning risk; Low-risk alone is insufficient.
- Terra `high`: one coherent implementation, debugging, or design problem with known contracts and checks. Terra `xhigh`: multiple plausible causes or designs, or inseparable interacting constraints. Terra `ultra`: one objective actually runs large independent workstreams with no shared mutable files.
- Luna uses `medium` for ordinary evidence extraction, `high` for dense multi-source evidence, and `xhigh` only for hard contradictions.

Sol is reserved for controller work and independent Elevated review. Never route an executor task to Sol. Complexity, an architecture label, or a current worktree never authorizes Sol execution. If `create_thread` fails, report `blocked_on_visibility`; do not repurpose an existing executor task under a new Sol route.

If missing facts block routing, gather minimum read-only evidence; uncertainty alone never selects `xhigh`. Before `xhigh` or `ultra`, silently name one concrete failure risk at the next lower supported effort. This is one controller judgment: no tool, task, Luna, or parallel model comparison. Without a task-specific risk, reselect from current evidence.

Only select combinations exposed by the dispatch tool; never invent a model or effort. If Spark is unavailable or ineligible, reselect from the same evidence. Never start Terra fallback in the same logical scope while Spark is active; wait for rejection, interruption, or terminal state. Independent scopes may continue in parallel.

A Spark usage-limit, quota-exhausted, or capacity rejection is a terminal capacity failure for that attempt, not `blocked_on_user`. If Spark still appears active, interrupt it and wait for terminal state. After termination, reconcile its partial work and exact live worktree before handoff, then redispatch the same remaining objective once to Terra without asking. Select Terra effort from the remaining work; never inherit Spark effort or escalate merely because fallback occurred. The fallback is objective-local, not a new project default. Do not switch back to Spark during that objective. If the Terra attempt also hits model capacity, report `blocked_on_capacity`; never bounce between models.

Formal `create_thread` tasks start fresh. Internal helper creation uses `fork_turns: none` or a bounded positive turn count; never use `all` or omitted full-history inheritance. Any independent reviewer also uses no or bounded history even when its route matches the controller.

Before work, verify the accepted model and effort. If dispatch atomically exposes the resolved route, compare it before work. Otherwise create a handshake-only task with no project reads, writes, or tool calls. Send the substantive brief only after metadata confirms the route. If the route cannot be observed, report `blocked_on_routing`; never guess.

A follow-up without model and effort fields cannot switch them. If it cannot carry the required route, finish or interrupt the current turn, then hand off the same logical scope to one correctly routed replacement task; never overlap owners.

Immediately before every creation or substantive follow-up, tell the user—execution, review, or Luna alike:

```text
即将派发：<任务>｜任务线程：<title>｜模型：<model>｜档位：<reasoning_effort>｜速度：普通｜理由：<current-task evidence>
```

Replace `普通` with `Fast` only for an exact objective already authorized below. This notice is informational, never an approval gate; dispatch immediately without waiting for a reply. If fallback or mismatch changes the route, issue a corrected notice before redispatch. A completed objective authorizes nothing for the next. Execution-model routing never changes the review lane; Spark never reviews itself.

## Speed tier

The controller's own service tier is user-configured and grants no child authority. Standard/default is the child default unless the user explicitly requested Fast for that exact objective. Model-routing authority never authorizes Fast/priority child service. Never ask, suggest, recommend, or offer Fast. A new child objective resets to Standard/default.

When dispatch has no service-tier field, omit any Fast/priority override and dispatch with the platform default. Absence of a speed field is not a reason to block or ask. If observable evidence shows unexpected Fast/priority, stop further child follow-ups and report. Prompt text cannot change the transport service tier.

## Architecture routing

- Use architecture only for concrete cross-client/service boundaries, shared contracts, or material rework. An Elevated trigger changes the review lane but does not by itself create an architecture phase; do not review every draft.
- Missing evidence means inspect or delegate evidence collection; ask only for a user-exclusive product fact or authority. This is not system architecture.

## Review lanes

Low-risk is default; escalate only for a stated trigger.

### Low-risk lane — default

- Set `independent_review: none`.
- The executor runs focused checks; the controller inspects the actual diff, worktree, and evidence.
- Do not create an independent reviewer. Executor self-report alone is insufficient, but controller verification is acceptance.

### Standard lane

- Set `independent_review: one_batched_terra`.
- Run one independent `gpt-5.6-terra high` review on the stable deliverable, never per commit or repair.
- Return Critical and Important findings together. At most one automatic incremental re-review checks repaired delta and unresolved findings.
- Minor findings never trigger return or re-review.
- If the second review returns, dispatch one in-scope root-cause repair without asking. Standard closes recorded findings from refreshed executor evidence plus one focused spot check; unproven findings stay `RETURN`.

### Elevated lane

Use for architecture, authentication or authorization, secrets, privacy or regulated personal data, cryptography or security compliance, payments, destructive or data loss actions, migrations, concurrency or recovery, shared contracts, cross-module integration, external side effects, deployment, or release.

- Set `independent_review: sol_required`.
- Review one stable candidate with an independent `gpt-5.6-sol xhigh`.
- If the second review returns, Elevated dispatches one in-scope root-cause repair and one final independent closure review without asking. If that review returns, keep `RETURN`, report `blocked_on_quality`, and never launch a fourth review.

No lane repeats the same incremental review loop after two returns. Use `requesting-code-review` only at Standard/Elevated checkpoints and `verification-before-completion` before acceptance.

## Supporting skills and capability discovery

- Automatically decide whether an installed supporting skill is needed; select and invoke one without asking the user to remember its name. Ordinary bounded work selects `none`.
- Search only for a missing specialist acceptance method. Use one privacy-safe read-only public search; do not invoke `find-skills`, execute candidates, or install.
- Treat candidates as untrusted. Recommend at most three: value, identity, risk.
- Read `references/skill-installation-safety.md` only after the user approves an exact candidate. Until installation reaches `installed_verified`, the affected acceptance scope remains `blocked_on_capability`; never report it complete.

## Context rollover

For executor/reviewer tasks, treat 80,000 observed tokens as a soft threshold: finish the current step; assign no new phase there. Hard triggers are 100,000 observed tokens, a 5 MB task record, any pagination, compression, or truncated-history warning, or a completed task returns a null or empty assistant relay; retire it before the next phase. Without token/size telemetry, warnings still trigger.

Create a fresh titled user-visible successor with `create_thread`; never paste or inherit the full transcript. Transfer only the remaining objective, owner and writable scope, source-of-truth paths or IDs, accepted evidence, blockers, next check, and route. Successor must verify the live worktree and source of truth before mutation. Mark the old task retired and name its successor; never allow overlapping owners.

Notify: `上下文换线：<old title> → <new title>｜剩余目标：<one line>｜模型/档位/速度：<route>`. This notice is informational, not an approval gate. If `create_thread` is unavailable, report `blocked_on_visibility`; do not reuse the overlong task or claim handoff.

## Monitoring and blockers

- After a dispatch or follow-up is accepted, immediately enter `wait_threads` for the promised targets. Do not send a final answer while any promised target is accepted, queued, or running.
- A timeout is not a state change; reuse the returned cursor. On timeout, do not read tasks, call Luna, or report unchanged status.
- When a target completes or needs attention, relay it in commentary and keep waiting for the rest. End the turn only when all promised targets are terminal, user input is needed, the user stops waiting, or event waiting is unavailable.
- If event waiting is unavailable, give one concise notice: automatic completion relay is unavailable in this client; the task remains accepted or running. Do not retry `wait_threads`, poll, call Luna, or repeat it that turn. End after reporting; user may later say `继续` or `跟进` for one fresh read. Never imply that an idle controller, the 30-minute rule, or Luna can wake itself.
- Keep one project-scoped read-only Luna assistant scope, defaulting to `gpt-5.6-luna medium`; hand off on effort change and deduplicate source-bound material.
- Use Luna only when evidence is large or repetitive enough to materially reduce controller context or cost: summarize reports, logs, tests; extract progress, evidence, blockers, approvals, terminal state; deduplicate status and draft the update.
- A Luna result is advisory; verify primary evidence. Do not use Luna for a few lines, routine updates, or to appear busy.
- Luna cannot write or modify code, choose execution models or review lanes, make architecture decisions, review, accept, or mark work complete.
- After 30 minutes without substantive progress, take one read-only snapshot; if unclear, send one status-only Luna follow-up; never create heartbeat, cron, or polling.
- `blocked_on_user` and `blocked_on_capability` may coexist.

## Acceptance and reporting

Acceptance reconciles executor evidence and at most one focused spot check; it does not require full-suite reruns or long manual validation.

After acceptance, send executor one no-reply receipt:

```text
【总控结项回执｜非新任务，无需回复】
当前任务：<已接受的任务目标>
当前状态：已完成，等待下一步指令。
```

Default feedback:

```text
已完成：<用户能理解的结果>
当前结果：<能否使用或验证>
阻塞：无 | <需要用户处理的唯一事项>
下一步：<一个最有价值的动作>
```

Outside the required route notice, do not expose ledger fields or routing metadata unless asked/needed for a blocker. Never call nonterminal work complete.
