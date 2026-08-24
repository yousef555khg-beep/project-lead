# Project Lead

English | [简体中文](README.zh-CN.md)

A Codex skill for coordinating multi-module projects, automatically routing Spark or Terra execution, using Luna for bounded read-only information assistance, selecting useful supporting skills, and keeping ordinary work out of unnecessary review loops.

## Project Lead 1.0

Project Lead 1.0 turns a capable Codex conversation into a **real project-control layer**: it keeps ownership visible, routes execution by the current objective, limits review to real risk, and reports a usable result rather than a stream of agent activity.

It follows one operating principle: **use the least process that is safe for the actual risk**. The controller owns scope, task ownership, blockers, acceptance, and reporting; executors own project artifacts and substantive execution. Ordinary work moves through one clear owner without unnecessary review, while high-risk work retains independent gates.

Project Lead is a decision and coordination skill, not a replacement for missing Codex App features. A prompt-only workaround cannot register a platform handler, change an unavailable service tier, or make an idle controller wake itself. The sections below distinguish its verified behavior from those platform boundaries.

## What Project Lead controls

| Capability | Observable result |
| --- | --- |
| Visible ownership | Implementation, review, and long validation run in titled sidebar-visible tasks; one mutable scope has one owner. |
| Approval boundary | The controller approves normal in-scope work itself and asks only for a real authority or product-policy decision. |
| Objective-local routing | Every new objective receives a fresh Spark, Terra, or Luna route, effort, and ordinary-speed decision; prior routes cannot leak forward. |
| Capacity recovery | A terminal Spark quota or capacity failure hands the remaining objective once to Terra, with fresh effort selection and no model bounce. |
| Risk-proportionate review | Low-risk work has no independent review; Standard and Elevated work retain bounded independent gates. |
| Capability discovery | One installed supporting skill may be selected automatically; missing skills are only searched and recommended until the user approves installation. |
| Completion reliability | `wait_threads` relays terminal events while the client provides it; unavailable event waiting degrades honestly instead of pretending to monitor in the background. |
| Context rollover | Long executor or reviewer histories move to a fresh visible successor before relay reliability degrades. |

## Controller authority and execution boundary

Inside an approved project outcome, the controller authorizes normal dispatch, local reversible preparation, focused checks, required review, and in-scope repair. Elevated review does not itself require user approval: review risk determines review strength, while the proposed action and missing authority determine approval. The user is asked only for a real product or security-policy fork, new authority or secret, irreversible or destructive action, external side effect, purchase, deployment, or release. A genuine platform approval card is still relayed when only the user can operate it.

The controller remains the control plane: intake, routing, no-code cross-module decisions, acceptance, reporting, and quick read-only spot checks. Repository plans, designs, source, tests, complex debugging, and long validation belong to executor tasks. Executor work cannot be split into small steps and kept in the controller. Old approval blockers are bound to one objective, candidate, action, and authority gap; they expire when that identity or need changes.

Elevated risk strengthens the independent review lane; it does not automatically create a separate architecture phase. Architecture work begins only for a concrete cross-client or cross-service boundary, unresolved shared contract, or material rework risk.

## Visible executor tasks

Formal implementation, independent review, and long validation use a titled, user-visible standalone Codex task created with `create_thread`, not an internal subagent. This lets the user find it in the sidebar, inspect its history, and act on approval cards. If `create_thread` is unavailable, Project Lead reports `blocked_on_visibility` instead of claiming dispatch. Internal subagents are only short read-only helper checks; they cannot own mutable scope, wait for approval, review, accept, or close formal work.

## Context rollover for long tasks

At 80,000 observed tokens, an executor or reviewer task reaches a soft threshold: it finishes the current bounded step but receives no new phase. At 100,000 observed tokens or 5 MB of task history, Project Lead retires it before the next phase. The following are also hard triggers: pagination, compression, truncated history, or an empty/null completion relay, even when numeric telemetry is unavailable.

Project Lead creates a fresh titled, user-visible successor and sends a compact handoff containing only the remaining objective, owner and writable scope, source-of-truth paths or IDs, accepted evidence, blockers, next check, and route. It never copies the complete transcript, verifies live state before mutation, names the retired predecessor, and never overlaps mutable ownership. If a visible successor cannot be created, it reports `blocked_on_visibility` instead of reusing the overlong task.

## Automatic skill routing and discovery

**You describe the outcome, not the skill name.** At project intake and before each new phase, Project Lead:

- automatically selects and invokes at most one relevant installed skill when the work has a concrete trigger;
- selects no supporting skill for ordinary bounded work instead of loading tools “just in case”;
- performs one privacy-safe, read-only public search only when a required specialist acceptance method is genuinely missing; and
- recommends at most three candidates, explains their project value and risk, and asks before any installation.

For example, it may use `apple-design` for a gesture-driven Apple interface, `codebase-design` for real module-boundary friction, or `webapp-testing` for a runnable web acceptance path. Candidate instructions are treated as untrusted information during discovery and are never executed or installed automatically.

## Automatic execution-model routing

The user authorizes automatic routing once per project. For every new objective, Project Lead chooses both the model and reasoning effort from the current bounded child objective: its actions, uncertainty, coupling, consequences, checks, and combinations exposed by the dispatch tool. It never inherits the previous objective's route and never inherits effort from the parent project, review lane, or previous task.

- Spark high handles an exact reversible path with deterministic checks. Spark xhigh additionally requires a named hard local reasoning risk; Low-risk classification alone is not enough.
- Terra high handles one coherent implementation, debugging, or design problem with known contracts and checks. Terra xhigh requires multiple plausible causes or designs, or inseparable interacting constraints. Terra Ultra requires one objective that actually runs large independent workstreams with no shared mutable files.
- Luna defaults to medium for read-only extraction, may use high for dense multi-source evidence, and uses xhigh only for difficult contradictions. Its authority stays read-only at every effort.
- Standard review remains independent Terra; Elevated review remains independent Sol. Execution routing never weakens review gates.
- Sol never executes delegated project work; it is reserved for controller decisions and independent Elevated review.

Before xhigh or Ultra, Project Lead performs one silent controller judgment: it names a concrete failure risk at the next lower effort. This uses no tool call, extra task, Luna call, or parallel model comparison. Without a task-specific risk, it reselects from current evidence, so uncertainty or the parent project's complexity cannot silently force xhigh.

Project Lead announces the task, model, effort, and actual speed immediately before dispatch, adds one short task-specific reason, and does not wait for approval. This is a notice, not a decision request. Speed is ordinary by default and shows Fast only after an explicit request for that exact objective. If capacity or route verification changes the choice, it sends a corrected notice before redispatch.

Formal `create_thread` executor tasks start fresh. Internal helper and reviewer tasks receive no or bounded history; full-history inheritance is never used. If dispatch exposes the resolved route atomically, Project Lead verifies it before work. Otherwise it starts a handshake-only task with no project reads, writes, or tool calls, verifies the metadata, and only then sends the substantive brief. An unobservable route is reported as `blocked_on_routing`, never guessed.

A follow-up API without route fields cannot switch an existing task in place; after the current turn ends or is interrupted, the logical scope is handed to one correctly routed task without overlapping owners. A Spark-to-Terra fallback waits only for the active Spark turn on the same objective or logical scope; independent scopes may continue in parallel.

If a Spark attempt hits a usage, quota, or capacity limit, Project Lead first makes that attempt terminal, reconciles any partial work in the live worktree, and redispatches the remaining objective once to Terra without asking. Terra effort is selected from the remaining work instead of inherited from Spark. This objective-local fallback does not become the project default and will not bounce back to Spark during the same objective. If Terra also hits model capacity, Project Lead reports `blocked_on_capacity` instead of bouncing between models.

## Child tasks use Standard speed by default

Fast speed is not the Low-risk lane. The controller may keep its user-configured speed, but that setting grants no speed authority to delegated work. By default, every new child task starts at Standard/default, including follow-ups, and Project Lead never asks whether to use Fast. Fast is used only when the user explicitly requests Fast for that exact child objective; the permission expires with the objective.

When the dispatch API has no speed field, Project Lead omits any Fast/priority override and uses the platform Standard/default. The missing field does not block ordinary dispatch. If runtime evidence later shows unexpected Fast/priority, the controller stops further follow-ups and reports it.

## Luna as a read-only information assistant

When large or repetitive evidence would materially expand controller context or cost, Project Lead keeps one logical project-scoped `gpt-5.6-luna` assistant scope, normally at medium. If effort must change, it uses the same no-overlap handoff rule as other routes. Luna summarizes long task reports, logs, and test output; extracts progress, blockers, approvals, and terminal state; deduplicates repeated status; and drafts the plain-language update.

Luna is not used for a few lines or routine updates. Its result remains advisory and source-bound, so the controller verifies primary evidence before acting. Luna never writes code, selects models, reviews, accepts, or marks work complete, and it never replaces required verification.

## Event-driven completion relay

After delegated work is accepted, Project Lead keeps the controller turn open with `wait_threads` until every promised target finishes or needs attention. A timeout only renews the event wait; it does not trigger status polling, repeated reads, or Luna. When one target finishes, the controller relays it in commentary and continues waiting for the others.

The controller ends early only for required user input, an explicit user stop, or an unavailable event-wait tool. When `wait_threads` is unavailable, it gives one concise degraded-mode notice: automatic completion relay is unavailable in this client, but the accepted or running task is unchanged. It does not retry the interface, poll, call Luna, or repeat the warning in that controller turn. It ends after the current report; the user can later say `continue` or `follow up` for one fresh read. Luna and the 30-minute rule cannot wake an idle controller.

## Risk-based review lanes

| Lane | Use when | Review behavior |
| --- | --- | --- |
| Low-risk — default | Copy, styling, tests, local fixes, small reversible behavior, isolated work under accepted interfaces | No independent reviewer. The controller verifies the real diff, worktree, and focused checks, then accepts. |
| Standard | Meaningful multi-file work inside one module or bounded integration under accepted contracts | One batched `gpt-5.6-terra high` review after the deliverable is stable. At most one incremental repair review. Minor findings never cause a return. |
| Elevated | Authentication, authorization, secrets, privacy or regulated personal data, cryptography or security compliance, payments, destructive actions, data loss or ownership, migration, concurrency or recovery, shared contracts, cross-module integration, deployment, release, or system architecture | One stable candidate receives an independent `gpt-5.6-sol xhigh` review. A necessary irreversible architecture decision may be reviewed once before implementation. |

No lane repeats the same incremental review loop after two returns. After a second Standard return, the controller dispatches one in-scope root-cause repair and closes each recorded finding from fresh executor evidence plus one focused spot check; anything unproven stays `RETURN`. After a second Elevated return, the controller automatically dispatches one in-scope root-cause repair and one final independent closure review. It never launches a fourth review; another `RETURN` remains `blocked_on_quality` and unfinished.

## How it works

1. Inspect the live repository and active tasks.
2. Separate the current usable outcome from optional later work.
3. Keep one owner per mutable scope and reuse that task for repair.
4. Choose Low-risk, Standard, or Elevated from concrete risk evidence.
5. Run only the checks required by the changed surface and repository policy.
6. Report progress in plain language.

Delegated Low-risk work may use Spark only when every allowlist condition is proven; substantive project work, non-obvious debugging, and long validation stay in executor tasks.

Missing information does not automatically create a system-architecture phase or a user question. The controller first inspects or delegates evidence collection; it asks only for a user-exclusive product fact or authority. System architecture is reserved for a real cross-client or cross-service boundary with an unresolved shared contract or material rework risk.

## Plain-language reporting

The default user update is deliberately short:

```text
已完成：<用户能理解的结果>
当前结果：<能否使用或验证>
阻塞：无 | <需要用户处理的唯一事项>
下一步：<一个最有价值的动作>
```

Outside the required pre-dispatch route notice, internal fields such as Base/Head, SHA, review request, and ledger state stay hidden unless the user asks or they explain a real blocker.

After an accepted delegated task, the controller leaves one receipt in its original task:

```text
【总控结项回执｜非新任务，无需回复】
当前任务：<已接受的任务目标>
当前状态：已完成，等待下一步指令。
```

## Coordination and approvals

- One checkout or mutable scope has one owner.
- Independent modules may run in parallel; shared files, migrations, and contracts are serialized.
- Dispatch acknowledgement is not completion. The controller reads the terminal report and verifies evidence.
- Only genuine approval-boundary crossings are surfaced with the task, exact action, risk, and where the user should act. Hidden platform-card contents are never guessed; ordinary review or local work is never repackaged as a prose approval request.
- After 30 minutes without substantive progress, the controller may take one read-only snapshot and one status-only Luna follow-up. It never creates heartbeat, cron, or polling.

## Supporting skills and discovery

Project Lead selects at most one supporting design or discovery skill per phase, and only when a concrete trigger exists. Ordinary work selects none.

Its missing-skill lookup is built in and read-only. It does not call `find-skills`. A search happens only for a genuinely unavailable specialist acceptance method, uses a privacy-safe public query, treats candidate content as untrusted, and recommends at most three options. Discovery never installs anything or blocks unrelated work.

Detailed candidate binding and fail-closed installation rules live in [the installation safety reference](skills/project-lead/references/skill-installation-safety.md) and are loaded only after the user approves an exact candidate. Moving this detail out of the core keeps normal project work fast without weakening installation safety.

## Installation

Install globally for Codex:

```bash
npx skills add yousef555khg-beep/project-lead@project-lead -g -a codex
```

Then start a controller conversation with:

```text
Use project-lead to govern this project.
```

## Companion skills

- `verification-before-completion` is used before accepting every lane.
- `requesting-code-review` is used only at Standard and Elevated review checkpoints.
- Optional supporting skills include `prototype`, `codebase-design`, `apple-design`, and `webapp-testing` when their concrete trigger is present.

## Evidence and community

- [Sanitized use cases](docs/USE-CASES.md)
- [Behavior validation](docs/VALIDATION.md)
- [Changelog](CHANGELOG.md)
- [Contributing guide](CONTRIBUTING.md)
- [Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [Security policy](.github/SECURITY.md)

## License

[MIT](LICENSE)
