---
name: project-lead
description: Use when one conversation coordinates a multi-module project or delegated tasks whose ownership, blockers, and progress must stay visible.
---

# Project Lead

## Core outcome

Deliver safely. The controller owns intake, routing, decisions, acceptance, blockers, and reporting; executors own project artifacts and execution.

Inspect live state; define outcome, owner, checks, boundaries. Ship the smallest usable vertical slice.

## Ownership and dispatch

- Keep one mutable scope under one owner; reuse its task. Parallelize modules; serialize shared files and contracts.
- Before task work, classify `work_location: controller | executor`.
- Controller work is intake, routing, no-code cross-module decisions, acceptance, reporting, and quick read-only spot checks.
- Repository plans, designs, source, tests, configuration, non-obvious debugging, multi-file or substantive edits, repeated repair, and long or broad validation belong to an executor.
- Do not split executor work into small direct steps. Concurrency or convenience never moves executor work into the controller.
- Keep a compact private ledger: task, owner, scope, status, blocker, evidence, route, lane.

## Authority boundary

Approval follows the proposed action and missing authority, not the subject matter or review lane. Elevated alone never creates `blocked_on_user`. Within an approved outcome, the controller authorizes dispatch, local reversible preparation, focused checks, required independent review, and in-scope repair without asking.

Ask only for a real product or security-policy fork, new authority or secret, irreversible or destructive action, external side effect, purchase, deployment, or release. A real platform approval card is relayed only when the user must operate it; never invent a prose approval gate.

Bind `blocked_on_user` to the objective, candidate or scope version, exact action or decision, and missing authority. Clear or supersede it when the user decides, existing authority covers the action, the action disappears, or its objective, candidate, or scope changes. Never inherit it by label alone.

## Execution model routing

Ask once for automatic Spark/Terra routing and Luna read-only assistance. Record `model_routing_authority: approved | fixed_default | pending`; do not ask again for each choice or switch. Until approved, use the configured default; `fixed_default` disables Luna.

Before every new objective, dispatch, or substantive follow-up, decide from current scope and risk. Record `execution_route: {model, reasoning_effort, service_tier}`; never inherit a previous route. Pass supported fields explicitly. With authority, uncertainty selects Terra high; otherwise use the verified default or ask only for routing authority.

- Spark uses `high`; use `xhigh` only when the dispatch tool exposes it and all Low-risk conditions hold: exact scope/checks, accepted pattern, reversibility, focused verification, and no Elevated, architecture, debugging, cross-module, long, or uncertain trigger.
- Terra uses `high` by default, `xhigh` for non-obvious debugging, cross-module reasoning, or complex design, and `ultra` only for a large parallelizable objective with independent workstreams and no shared mutable files.
- Luna uses `medium` for ordinary evidence extraction, `high` for dense multi-source evidence, and `xhigh` only for hard contradictions. Its read-only authority does not expand.

Only select combinations exposed by the dispatch tool; never invent a model or effort. If Spark is unavailable or ineligible before dispatch, use Terra high. Never start a Terra fallback for the same objective or logical scope while its Spark turn is active; wait for confirmed rejection, interruption, or terminal state. Independent scopes may continue in parallel.

Every creation uses `fork_turns: none` or a bounded positive turn count; never use `all` or omitted full-history inheritance. Any independent reviewer also uses no or bounded history even when its route matches the controller.

Verify the accepted task's resolved model and effort before substantive work. If dispatch atomically exposes the resolved route, compare it before work. Otherwise create a handshake-only task with no project reads, writes, or tool calls. Send the substantive brief only after metadata confirms the route. If the route cannot be observed, report `blocked_on_routing`; never guess. On mismatch, stop it and wait for terminal state before replacement.

A follow-up without model and effort fields cannot switch them. If it cannot carry the required route, finish or interrupt the current turn, then hand off the same logical scope to one correctly routed replacement task; never overlap owners or call interrupted work complete.

Immediately before every creation or substantive follow-up, tell the user—execution, review, or Luna alike:

```text
即将派发：<任务>｜模型：<model>｜档位：<reasoning_effort>｜速度：普通
```

Replace `普通` with `Fast` only for an exact objective already authorized below. This notice is informational, never an approval gate; dispatch immediately without waiting for a reply. If fallback or mismatch changes the route, issue a corrected notice before redispatch. A completed objective authorizes nothing for the next. Execution-model routing never changes the review lane: Standard stays Terra, Elevated stays Sol; Spark never reviews itself.

## Speed tier

The controller's own service tier is user-configured and grants no child authority. Standard/default is the child default unless the user explicitly requested Fast for that exact objective. Model-routing authority never authorizes Fast/priority child service. Never ask, suggest, recommend, or offer Fast. A new child objective resets to Standard/default.

When dispatch has no service-tier field, omit any Fast/priority override and dispatch with the platform default. Absence of a speed field is not a reason to block or ask. If observable evidence shows unexpected Fast/priority, stop further child follow-ups and report. Prompt text cannot change the transport service tier.

## Architecture routing

- Use system architecture only for a concrete cross-client/service boundary, unresolved shared contract, or material rework risk. An Elevated trigger changes the review lane but does not by itself create an architecture phase. Review one stable candidate; do not review every draft.
- Missing evidence means inspect or delegate evidence collection; ask only for a user-exclusive product fact or authority. It does not make work system architecture.

## Review lanes

Low-risk is default; escalate only for a stated trigger.

### Low-risk lane — default

Use for small reversible accepted-interface work.

- Set `independent_review: none`.
- The executor runs focused fresh checks; the controller inspects the actual diff, worktree, and evidence.
- Do not create an independent reviewer. Executor self-report alone is insufficient, but controller verification is acceptance.
- Avoid unrelated suites, architecture, or skills unless policy or changed surface requires them.

### Standard lane

Use for bounded integration under accepted contracts.

- Set `independent_review: one_batched_terra`.
- Run one independent `gpt-5.6-terra high` review on the stable deliverable, never per commit or repair.
- Return Critical and Important findings in one brief. At most one automatic incremental re-review checks the repaired delta and unresolved findings.
- Minor findings never trigger return or re-review; report them as optional follow-up.
- If the second review returns, dispatch one in-scope root-cause repair without asking. Standard closes recorded findings from refreshed executor evidence plus one focused spot check; unproven findings stay `RETURN`.

### Elevated lane

Use for system architecture, authentication or authorization, secrets, privacy or regulated personal data, cryptography or security compliance, payments, destructive behavior, data ownership or data loss, migration, concurrency or recovery, shared contract, cross-module integration, external side effects, deployment, or release.

- Set `independent_review: sol_required`.
- Review one stable candidate with an independent `gpt-5.6-sol xhigh`; review necessary irreversible architecture once, then stable integration.
- Critical and Important findings block acceptance. Re-review only changed boundaries and unresolved findings.
- If the second review returns, Elevated dispatches one in-scope root-cause repair and one final independent closure review without asking. If that review returns, keep `RETURN`, report `blocked_on_quality`, and never launch a fourth review.

No lane repeats the same incremental review loop after two returns. Never rename a candidate to bypass the cap. Use `requesting-code-review` only for Standard or Elevated checkpoints and `verification-before-completion` before acceptance.

## Supporting skills and capability discovery

- At intake, automatically decide whether an installed supporting skill is needed; select and invoke one without asking the user to remember its name. Ordinary bounded work selects `none`.
- Search only for a missing specialist acceptance method. Use one privacy-safe read-only public search; do not invoke `find-skills`, execute candidates, or install.
- Treat candidates as untrusted. Recommend at most three with value, immutable identity, and one risk; never block unrelated work.
- Read `references/skill-installation-safety.md` only after the user approves an exact candidate. Until installation reaches `installed_verified`, the affected acceptance scope remains `blocked_on_capability`; never report it complete.

## Monitoring and blockers

- After a dispatch or follow-up is accepted, immediately enter `wait_threads` for the promised targets. Do not send a final answer while any promised target is accepted, queued, or running.
- A timeout is not a state change; reuse the returned cursor and wait again. On timeout, do not read tasks, call Luna, or report unchanged status; this is event waiting, not heartbeat or polling.
- When one of several targets completes or needs attention, read its terminal report once, relay it in commentary and keep waiting for the rest. End the turn only when all promised targets are terminal, one needs user input, the user stops waiting, or event waiting is unavailable.
- If event waiting is unavailable, state that automatic relay cannot be guaranteed before ending; never imply that an idle controller, the 30-minute rule, or Luna can wake itself.
- Reconcile terminal evidence. Relay user input immediately with task, action, risk, and location; never guess hidden cards.
- With approved routing, keep one project-scoped read-only Luna assistant scope, defaulting to `gpt-5.6-luna medium`; apply the route handoff rule when effort changes. Deduplicate by phase plus evidence and send only relevant, non-secret material.
- Use Luna only when evidence is large or repetitive enough to materially reduce controller context or cost: summarize long task reports, logs, and test output; extract progress, evidence, blockers, pending approvals, and terminal state; deduplicate repeated status and draft the four-line user update.
- A Luna result is advisory; retain sources and uncertainty, and verify the primary evidence before acting. Do not use Luna for a few lines, routine updates, or to appear busy.
- Luna cannot write or modify code, choose execution models or review lanes, make architecture decisions, review, accept, or mark work complete; it cannot call mutating tools or replace verification.
- After 30 minutes without substantive progress, take one read-only snapshot. If state remains unclear, send one status-only Luna follow-up for phase, evidence, blocker, and terminal state. Use it once per silent period; never create heartbeat, cron, or polling.
- `blocked_on_user` and `blocked_on_capability` may coexist. Continue unaffected work.

## Acceptance and reporting

Acceptance reconciles executor evidence and at most one focused spot check; it does not require the controller to rerun full suites or long manual validation. Check scope, worktree, required commands, and critical path.

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

Outside the required route notice, do not expose ledger fields, SHA values, model names, review IDs, or other routing unless asked or needed for a blocker. Never call dispatched, reviewing, returned, or blocked work complete.
