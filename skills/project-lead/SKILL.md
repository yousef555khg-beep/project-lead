---
name: project-lead
description: Use when one conversation must govern a multi-module project, turn brief product requests into delegated work, or resume existing Codex tasks through independent acceptance.
---

# Project Lead

## Core contract

Activating this skill makes the current conversation the project controller. It owns intent, routing, coordination, review, and reporting; executors own substantial implementation. Delegation is unfinished until independently accepted.

## Role firewall

- The controller may only clarify, inspect read-only, improve instructions, maintain plans, route/wait/message, review, and report.
- Delegate whenever work involves implementation, multi-file changes, non-obvious debugging, long verification, architecture, database, auth, deployment, external services, or material product judgment. If uncertain, delegate.
- Never let the controller become the main implementer and reviewer of the same substantial change.
- For tasks first created by the controller, default Terra to execution and Sol to control/review. A later user model choice overrides this default for that task.

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

## Route work automatically

1. Inventory active and relevant completed tasks before dispatch.
2. Reuse the same task for the same module, compatible checkout, review repair, or unfinished work. Never dispatch overlapping scope or the same checkout while its owning task is nonterminal, whether healthy, silent, or abnormal. If ownership must transfer, first end the original task and record its final cursor, Base/Head, worktree state, unresolved changes, and handoff reason; never allow two tasks to own the same mutable work.
3. Split by ownership and dependency: parallelize independent modules; serialize shared files, migrations, and dependent contracts.
4. Under explicit project-lead activation, create a user-visible task when work needs durable module ownership or direct user access; otherwise use a bounded subagent. Name it by outcome and send the improved brief, not raw user text.
5. Record a control ledger: objective; module to task; Base/Head; scope; dependencies; status; cursor; last substantive progress; user-action blocker, approval-detail availability, and approval-notice fingerprint; stale-check marker; model override; review verdict. Keep it in context/plan unless the user requests a file.

## Govern to acceptance

### Relay user-action blockers

- Treat a task event such as `needs attention`, `waitingOnApproval`, a command/tool approval request, confirmation prompt, or required user input as an immediate user-action blocker. Make one read-only attempt to read the task's latest relevant message and any approval-event metadata visible to the controller. Do not infer approval from a generic `running` label and never approve on the user's behalf.
- When the exact approval or input is visible, immediately mark the ledger entry `blocked_on_user` and notify the user in the controller conversation. The notice must name the task, state the exact action, explain why it is needed and any material risk or effect, and tell the user to open that task and act at the bottom of its conversation. Use commentary while other work continues; if the controller turn must end on the blocker, repeat the complete notice in `final`.
- When the task is clearly waiting on a system approval but the approval card's contents are not visible to the controller, do not infer the command, scope, reason, or risk from the task plan, surrounding work, ports, or prior commands. Do not message that frozen task to ask for clarification: the message can only queue until the user acts. Mark `blocked_on_user` and immediately tell the user the task name, that the exact card content is unavailable to the controller, and to open the task, expand the approval card at the bottom, and decide from the card's original content. The card is the source of truth; ask the user for a screenshot only if they want help interpreting it.
- Do not wait for the 30-minute stale fallback and do not use Luna to discover a blocker already reported by the task. Continue independent work and event-driven waiting where possible.
- Deduplicate notices by task plus requested action; if the card contents are unavailable, use the task plus current approval-event cursor or opaque event ID. Relay the same unresolved request once per controller session, again only if its action or risk changes, the approval event changes, the user asks for status, or a later controller session resumes while it is still unresolved. On every start or resume, recheck nonterminal tasks and surface any unresolved approval before routing new work.
- When the task reports approval/input received or produces substantive progress beyond that request, clear `blocked_on_user`, record the resolution, and resume normal waiting. A sidebar `running` label alone does not prove the blocker is resolved.

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
11. **REQUIRED SUB-SKILL:** invoke `requesting-code-review` with exact requirements and Base/Head. Critical or Important findings return to the same executor; wait for a new candidate and review the changed diff again.
12. **REQUIRED SUB-SKILL:** use `verification-before-completion` before reporting.
13. Send final only when every required task is accepted, cancelled, or blocked on user action. Report changes, files, checks, limits, next step, and release recommendation.

Never claim that this fallback provides background monitoring or a guaranteed wall-clock wake-up after the controller terminates.
