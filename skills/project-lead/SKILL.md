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
2. Reuse the same task for the same module, compatible checkout, review repair, or unfinished work. Never duplicate healthy work.
3. Split by ownership and dependency: parallelize independent modules; serialize shared files, migrations, and dependent contracts.
4. Under explicit project-lead activation, create a user-visible task when work needs durable module ownership or direct user access; otherwise use a bounded subagent. Name it by outcome and send the improved brief, not raw user text.
5. Record a control ledger: objective; module to task; Base/Head; scope; dependencies; status; cursor; last substantive progress; stale-check marker; model override; review verdict. Keep it in context/plan unless the user requests a file.

## Govern to acceptance

1. Stay active after dispatch and use event-driven `wait_threads` or `wait_agent` with current cursors. Bound the wait so a task can be evaluated after 30 minutes without substantive progress. Never create heartbeat, cron, recurring automation, timer loops, or periodic polling.
2. Treat only a new phase, evidence, candidate, blocker, or terminal state as substantive progress; status chatter does not reset the 30-minute window.
3. After 30 silent minutes, take one fresh read-only snapshot. If the state remains unclear, send one status-only follow-up to the same task using `gpt-5.6-luna`; request current phase, last evidence, blocker, and terminal status. Do not modify code, review, accept, restart, or create another task. Report the result and resume event-driven waiting.
4. Run the Luna fallback at most once per uninterrupted silent period. Rearm it only after substantive progress.
5. On every controller start or resume, immediately reconcile all nonterminal ledger entries from their saved handles before routing new work. A terminated controller cannot wake itself; the next turn performs this recovery without heartbeat.
6. User interruption: answer in commentary, then resume unless it cancels or replaces work.
7. On completion, verify branch, Base/Head, scope, clean status, and fresh checks. Executor self-report is not acceptance.
8. **REQUIRED SUB-SKILL:** invoke `requesting-code-review` with exact requirements and Base/Head. Critical or Important findings return to the same executor; wait for a new candidate and review the changed diff again.
9. **REQUIRED SUB-SKILL:** use `verification-before-completion` before reporting.
10. Send final only when every required task is accepted, cancelled, or blocked on user action. Report changes, files, checks, limits, next step, and release recommendation.

Never claim that this fallback provides background monitoring or a guaranteed wall-clock wake-up after the controller terminates.
