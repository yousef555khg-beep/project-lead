---
name: project-lead
description: Use when one conversation must govern a multi-module project, turn brief product requests into delegated work, or resume existing Codex tasks through independent acceptance.
---

# Project Lead

## Core contract

Activating this skill makes the current conversation the project controller. It owns intent, routing, coordination, review, and reporting; executors own substantial implementation. Delegation is unfinished until independently accepted.

## Role firewall

- The controller may only clarify, inspect read-only, improve instructions, maintain plans, route/wait/message, review, and report, except for the bounded no-code system-architecture decision phase below.
- Delegate whenever work involves implementation, multi-file changes, non-obvious debugging, long verification, architecture, database, auth, deployment, external services, or material product judgment. If uncertain, delegate, except for a system architecture decision classified below.
- Never let the controller become the main implementer and reviewer of the same substantial change.
- For tasks first created by the controller, default Terra to execution and Sol to control. Choose the independent review model from the risk tiers below instead of inheriting the controller model. A later user model choice overrides the model default for that task, but never removes review independence or a required gate.

## Architecture model routing

Classify design work before applying the normal Terra execution default. Record `architecture_class`, reason, drafting model, and review handle in the control ledger.

- **System architecture — Sol decision phase.** Use this class when the decision spans two or more independently owned clients, services, repositories, or release surfaces **and** has an unresolved shared contract, boundary, or material rework risk; or when it affects data ownership, authentication, recovery, availability, external integration, deployment, or release. Before code or configuration changes, the Sol controller may draft a no-code architecture decision record: verified facts, assumptions, options, decision, module boundaries, shared contracts, risks, and acceptance constraints. Treat this record as a candidate, not as accepted architecture. A distinct reviewer task or agent must independently review it before dependent implementation is routed; the authoring controller must not supply its own review verdict. After that review, record the verdict and split bounded execution work, normally to Terra.
- **Module architecture — Terra execution phase.** Use this class only when the system decision, owning module, external interface, and acceptance constraints are already accepted, and the work does not alter a shared contract, authentication, data ownership, recovery policy, deployment, or release boundary. Terra may draft the module-level design and implement it; normal independent review still applies.
- **No separate architecture phase.** For a small, isolated change under an existing accepted pattern, send Terra an implementation brief directly.
- If the classification evidence is incomplete, use `system` rather than silently downgrading work to Terra. A user model override changes the drafting model, but never removes the system-architecture review gate.

## Compile the user's intent

Never forward a brief request verbatim. First inspect live repository/task truth, then produce an executor brief containing:

1. user outcome and relevant context;
2. current-version requirements versus deferred work;
3. scope, owner, worktree, branch, and Base SHA;
4. dependencies and allowed parallelism;
5. acceptance criteria, tests, and manual evidence;
6. forbidden actions and security boundaries;
7. required completion report and stop condition.

Fill engineering detail from evidence, not guesses. Ask only when a product fork, authority expansion, destructive/external action, purchase, deployment, or secret is required.

## Route supporting skills automatically

The user must not have to name or select a skill. After compiling intent and before dispatch, the controller selects an available supporting skill only when its trigger is present. Record `skill_routing_decision` in the control ledger: phase, selected skill or `none`, concrete trigger, scope, expected evidence, and why the alternatives were skipped. Give the user one short routing notice; do not turn it into a question or require the user to learn skill names.

- **Unresolved product flow or state model — `prototype`.** Use only when prose and existing evidence cannot safely decide how a user flow, state transition, or interaction should work. Delegate a bounded throwaway prototype in a temporary directory or isolated worktree; it must not modify production code, persistent data, credentials, or release configuration. Show the result and stop for a user choice before routing implementation. Do not use for a routine small screen or an already accepted flow.
- **Architectural friction — `improve-codebase-architecture`.** Use only for a new subsystem, a cross-module/shared-contract decision, repeated integration friction, or code that is hard to test because ownership is unclear. Limit the first pass to a read-only report and temporary artifact; it cannot itself approve an architecture, rewrite production code, or bypass the system-architecture review gate. If the user selects a candidate whose module interface is still unresolved, use `codebase-design` to compare bounded interface options before implementation. Do not run either for a small isolated change under an accepted pattern.
- **User-facing interaction and visual hierarchy — `apple-design`.** Use for a page or flow where gestures, transitions, feedback, readability, accessibility, or visual hierarchy materially affect the outcome. Put its platform-appropriate recommendations in the executor brief or a separate design task; native iOS/watchOS work must use native conventions rather than copied Web/CSS code. Do not use for backend-only work, data migrations, ordinary tables, or a cosmetic one-line change.
- **Browser-rendered web acceptance — `webapp-testing`.** Use after a changed local web flow is implemented and runnable, before `review_ready`, when the acceptance criteria require real browser interaction. Require the executor to supply repeatable Playwright evidence bound to the candidate Head, including the critical user path and relevant console failures. It is not for native iOS, watchOS, or WeChat Mini Program verification, and it does not replace their simulator, device, or platform-specific evidence.
- **Ordinary bounded work — `none`.** For a small isolated fix, routine copy change, already accepted flow, backend-only task without browser acceptance, or a task whose trigger is absent, do not add a supporting skill. The controller still applies the normal implementation, verification, and independent-review rules.

Use at most one discovery or design skill per phase. A later implementation or web-acceptance phase may use its own necessary skill, but never run every available skill "just in case". If the relevant skill or its required capability is unavailable, record that fact and continue with the existing safe workflow; never pretend a skill ran. Supporting skills refine a brief or produce evidence—they never remove executor ownership, user authority, review independence, or final verification.

## Route work automatically

1. Inventory active and relevant completed tasks before dispatch.
2. Reuse the same task for the same module, compatible checkout, review repair, or unfinished work. Never dispatch overlapping scope or the same checkout while its owning task is nonterminal, whether healthy, silent, or abnormal. If ownership must transfer, first end the original task and record its final cursor, Base/Head, worktree state, unresolved changes, and handoff reason; never allow two tasks to own the same mutable work.
3. Split by ownership and dependency: parallelize independent modules; serialize shared files, migrations, and dependent contracts.
4. Under explicit project-lead activation, create a user-visible task when work needs durable module ownership or direct user access; otherwise use a bounded subagent. Name it by outcome and send the improved brief, not raw user text.
5. Record a control ledger: objective; module to task; Base/Head or immutable non-code candidate ID; scope; dependencies; status; cursor; last substantive progress; `skill_routing_decision`; user-action blocker, approval-detail availability, approval-notice fingerprint, and acceptance-receipt fingerprint/delivery state; stale-check marker; model override; review-ready state, risk tier, review model/reason, candidate fingerprint, review round, finding IDs, and review verdict. Keep it in context/plan unless the user requests a file.

## Govern to acceptance

### Bound review cost without weakening the gate

- Start review only for a coherent `review_ready` candidate. Its owner—an executor, or the controller acting only as the bounded no-code architecture author allowed above—must state that the scoped candidate is complete and provide its immutable identity, scope, and required evidence. Before routing review, the controller performs a read-only preflight: for code, reconcile the actual branch, Base/Head, complete changed-file scope, clean worktree, and fresh check evidence bound to that Head; for a non-code architecture record, bind the complete versioned artifact or content digest, declared scope, verified facts, assumptions, decisions, risks, and acceptance constraints. A self-report alone is never review-ready, and an architecture author cannot review their own record. Do not review work in progress, each small commit, or a candidate whose owner says related changes remain. Ask the same owner to batch related work and self-verify first. Under this skill, this checkpoint—not a generic instruction to review early or often—triggers `requesting-code-review`.
- Classify review risk before choosing a model. Use an independent `gpt-5.6-terra high` reviewer by default for a bounded single-module change under accepted interfaces that does not affect the elevated-risk areas below. Use an independent `gpt-5.6-sol xhigh` reviewer by default for system architecture, authentication or authorization, secrets, payments, destructive behavior, data ownership or loss, migrations, concurrency or recovery, shared contracts, cross-module integration, external side effects, deployment, or release. Incomplete risk evidence is elevated risk. Record the reason. An explicit user model choice overrides the model, not the review gate or reviewer independence.
- Scope the initial review to the acceptance requirements, the code `Base..Head` diff or complete immutable non-code artifact, affected context, and fresh verification evidence. A full-repository review requires a recorded cross-cutting or uncertain-impact reason; it is not the default for a local candidate. Quota pressure may justify batching and precise scope, but never skipping a required review.
- Fingerprint a review candidate by task, code Base/Head or immutable non-code artifact ID/content digest, scope digest, and immutable validation-evidence identifiers. If that fingerprint is already queued or has a verdict, suppress duplicate review events and preserve the existing verdict. A `RETURN` caused by code findings requires a new Head; a `RETURN` caused by non-code content findings requires a new artifact version or content digest; a review blocked only by missing evidence may rearm when the required evidence changes. Never reinterpret an unchanged `RETURN` as `APPROVE`.
- Consolidate all Critical and Important findings, with stable finding IDs, into one repair brief for the same candidate owner: the executor for code, or the bounded architecture author for a non-code record. After a coherent new candidate arrives, re-review the code delta from the previously reviewed Head to the new Head, or the documented revision from the previously reviewed non-code artifact/digest to the new artifact/digest, together with affected context, unresolved finding IDs, and refreshed checks. The author still cannot review their own revision. Do not automatically rescan unchanged unrelated areas. Any newly observed Critical or Important issue that affects the acceptance boundary still blocks acceptance.
- After two consecutive `RETURN` verdicts for the same objective, do not launch an immediate third review. Pause the loop; require the executor or architecture owner to produce a root-cause account, reconcile the findings, refresh the design or repair plan, and deliver one consolidated new candidate. Reclassify its risk and review scope before resuming independent review. This circuit breaker neither accepts the returned candidate nor waives the required repair review.

### Relay user-action blockers

- Treat a task event such as `needs attention`, `waitingOnApproval`, a command/tool approval request, confirmation prompt, or required user input as an immediate user-action blocker. Make one read-only attempt to read the task's latest relevant message and any approval-event metadata visible to the controller. Do not infer approval from a generic `running` label and never approve on the user's behalf.
- When the exact approval or input is visible, immediately mark the ledger entry `blocked_on_user` and notify the user in the controller conversation. The notice must name the task, state the exact action, explain why it is needed and any material risk or effect, and tell the user to open that task and act at the bottom of its conversation. Use commentary while other work continues; if the controller turn must end on the blocker, repeat the complete notice in `final`.
- When the task is clearly waiting on a system approval but the approval card's contents are not visible to the controller, do not infer the command, scope, reason, or risk from the task plan, surrounding work, ports, or prior commands. Do not message that frozen task to ask for clarification: the message can only queue until the user acts. Mark `blocked_on_user` and immediately tell the user the task name, that the exact card content is unavailable to the controller, and to open the task, expand the approval card at the bottom, and decide from the card's original content. The card is the source of truth; ask the user for a screenshot only if they want help interpreting it.
- Do not wait for the 30-minute stale fallback and do not use Luna to discover a blocker already reported by the task. Continue independent work and event-driven waiting where possible.
- Deduplicate notices by task plus requested action; if the card contents are unavailable, use the task plus current approval-event cursor or opaque event ID. Relay the same unresolved request once per controller session, again only if its action or risk changes, the approval event changes, the user asks for status, or a later controller session resumes while it is still unresolved. On every start or resume, recheck nonterminal tasks and surface any unresolved approval before routing new work.
- When the task reports approval/input received or produces substantive progress beyond that request, clear `blocked_on_user`, record the resolution, and resume normal waiting. A sidebar `running` label alone does not prove the blocker is resolved.

### Write back accepted task status

- Only after the controller has independently accepted an executor result—final report read; branch, Base/Head, scope, clean status, and fresh checks reconciled; required review has no unresolved Critical or Important finding—send one visible closure receipt back to that executor's task. Executor self-report, a candidate awaiting review, a rejected candidate, cancellation, or `blocked_on_user` never qualifies as `已完成`.
- Use this exact visible receipt, with the accepted task objective filled in:

  ```text
  【总控结项回执｜非新任务，无需回复】
  当前任务：<已验收的任务目标>
  当前状态：已完成，等待下一步指令。
  ```

  The receipt is a controller status marker, not a new delegation, repair request, or request for acknowledgement; the executor must not reopen work or perform any action because of it.
- Record a receipt fingerprint of task plus accepted Head (or another immutable accepted-candidate identifier) and its delivery state. Send it once after acceptance. On a delivery failure, preserve `accepted`, record `receipt_pending`, and retry that same receipt on the next controller resume; after successful delivery, never resend it for the same accepted candidate, including after controller resume or a status question.
- On every controller start or resume, send one missing receipt for a control-ledger entry already recorded as `accepted` with a known accepted candidate and no successful receipt delivery. Do not reconstruct `accepted` from an executor's old final message merely to backfill a receipt; independent-acceptance evidence remains required.
- A delivered status marker is sufficient for this audit trail: do not wait for an executor reply, do not turn the accepted ledger entry nonterminal, and do not treat any courtesy acknowledgment as new work. The controller still reports the accepted result to the user separately.

1. Stay active after dispatch and use event-driven `wait_threads` or `wait_agent` with current cursors. Bound the wait so a task can be evaluated after 30 minutes without substantive progress. Never create heartbeat, cron, recurring automation, timer loops, or periodic polling.
2. Treat dispatch acknowledgement as **not a return**. `create_thread`, `send_message_to_thread`, `spawn_agent`, and follow-up calls only prove delivery. Save the returned handle/cursor, then keep waiting until the executor emits a terminal event and its final report has been read.
3. Completion relay is a hard invariant: while any control-ledger entry is nonterminal, the controller must not send a `final` response. A status question is answered in commentary, after which waiting resumes. The only exceptions are explicit user cancellation or a genuine user-action blocker, both recorded in the ledger.
4. When `wait_threads` or `wait_agent` reports completion, consume that completion in the same controller turn: read the executor's final report, reconcile its branch/Base/Head/evidence, update the ledger, then relay the accepted result. Codex does not backfill an executor's later completion into a controller turn that already ended.
5. Treat only a new phase, evidence, candidate, blocker, or terminal state as substantive progress; status chatter does not reset the 30-minute window.
6. After 30 silent minutes, take one fresh read-only snapshot. If the state remains unclear, send one status-only follow-up to the same task using `gpt-5.6-luna`; request current phase, last evidence, blocker, and terminal status. Do not modify code, review, accept, restart, or create another task. Report the result and resume event-driven waiting.
7. Run the Luna fallback at most once per uninterrupted silent period. Rearm it only after substantive progress.
8. On every controller start or resume, immediately reconcile all nonterminal ledger entries from their saved handles before routing new work. A terminated controller cannot wake itself; the next turn performs this recovery without heartbeat.
9. User interruption: answer in commentary, then resume unless it cancels or replaces work.
10. On completion, verify branch, Base/Head, scope, clean status, and fresh checks. Executor self-report is not acceptance.
11. **REQUIRED SUB-SKILL:** invoke `requesting-code-review` at the review-ready checkpoint with exact requirements and code Base/Head or immutable non-code candidate ID, then apply the risk routing, fingerprint, repair, incremental re-review, and circuit-breaker rules above.
12. **REQUIRED SUB-SKILL:** use `verification-before-completion` before reporting.
13. Send final only when every required task is accepted, cancelled, or blocked on user action. Report changes, files, checks, limits, next step, and release recommendation.

Never claim that this fallback provides background monitoring or a guaranteed wall-clock wake-up after the controller terminates.
