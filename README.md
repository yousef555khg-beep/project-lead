# Project Lead

English | [简体中文](README.zh-CN.md)

A Codex project-control skill: Astra-first but task-selected execution, optional same-project task communication, and independent review only for material or security risk. The controller keeps ownership visible, selects useful supporting skills, and verifies usable results without routine review loops.

## Project Lead 1.0

Project Lead 1.0 turns a capable Codex conversation into a **real project-control layer**: it keeps ownership visible, routes execution by the current objective, limits review to real risk, and reports a usable result rather than a stream of agent activity.

It follows one operating principle: **use the least process that is safe for the actual risk**. The controller owns scope, task ownership, blockers, acceptance, and reporting; executors own project artifacts and substantive execution. Ordinary work moves through one clear owner without unnecessary review, while high-risk work retains independent gates.

Project Lead is a decision and coordination skill, not a replacement for missing Codex App features. A prompt-only workaround cannot register a platform handler, change an unavailable service tier, or make an idle controller wake itself. The sections below distinguish its verified behavior from those platform boundaries.

## What Project Lead controls

| Capability | Observable result |
| --- | --- |
| Visible ownership | Implementation, review, and long validation run in titled sidebar-visible tasks; Project Lead reuses one executor for the same objective. |
| Approval boundary | The controller approves normal in-scope work itself and asks only for a real authority or product-policy decision. |
| Objective-local routing | Astra is preferred, not mandatory for substantive execution; Terra/Spark remain direct choices. Effort is chosen per task, never inherited. |
| Capacity recovery | A terminal Spark quota or capacity failure hands the remaining objective once to Terra, with fresh effort selection and no model bounce. |
| Risk-proportionate review | Ordinary work has no extra review stage. Material/security consequences trigger one bounded independent review workflow. |
| Capability discovery | One installed supporting skill may be selected automatically; missing skills are only searched and recommended until the user approves installation. |
| Completion reliability | `wait_threads` relays terminal events while the client provides it; unavailable event waiting degrades honestly instead of pretending to monitor in the background. |
| Context rollover | Long controller, executor, and reviewer context moves to a fresh visible successor before reliability degrades. |

## Controller authority and execution boundary

Inside an approved project outcome, the controller authorizes normal dispatch, local reversible preparation, focused checks, required review, and in-scope repair. Elevated review does not itself require user approval: review risk determines review strength, while the proposed action and missing authority determine approval. The user is asked only for a real product or security-policy fork, new authority or secret, irreversible or destructive action, external side effect, purchase, deployment, or release. A genuine platform approval card is still relayed when only the user can operate it.

The controller remains the control plane: intake, routing, no-code cross-module decisions, acceptance, reporting, and quick read-only spot checks. Repository plans, designs, source, tests, complex debugging, and long validation belong to executor tasks. Executor work cannot be split into small steps and kept in the controller. Old approval blockers are bound to one objective, candidate, action, and authority gap; they expire when that identity or need changes.

Elevated risk strengthens the independent review lane; it does not automatically create a separate architecture phase. Architecture work begins only for a concrete cross-client or cross-service boundary, unresolved shared contract, or material rework risk.

## Visible executor tasks

Formal implementation, independent review, and long validation use a titled, user-visible standalone Codex task created with `create_thread`, not an internal subagent. This lets the user find it in the sidebar, inspect its history, and act on approval cards. If `create_thread` is unavailable, Project Lead reports `blocked_on_visibility` instead of claiming dispatch. Internal subagents are only short read-only helper checks; they cannot own mutable scope, wait for approval, review, accept, or close formal work.

## Context rollover for long tasks

At 80,000 observed tokens, a controller, executor, or reviewer reaches a soft threshold: it finishes the current bounded step but receives no new phase. At 100,000 observed tokens or 5 MB of task history, Project Lead retires it before the next phase. Pagination, compression, or truncated history are also hard triggers when numeric telemetry is unavailable. A running executor is not restarted merely because its controller rolls over.

Token thresholds mean current context input, not accumulated billed tokens. These are Project Lead handoff guardrails, not official model context limits. A controller successor preserves the user's selected Astra route and existing child owners; a larger model window alone does not prove the client relay is more reliable.

Project Lead creates a fresh titled, user-visible successor and sends a compact handoff containing only the remaining objective, owner and writable scope, source-of-truth paths or IDs, accepted evidence, blockers, next check, and route. It never copies the complete transcript, verifies live state before mutation, names the retired predecessor, and never overlaps mutable ownership. If a visible successor cannot be created, it reports `blocked_on_visibility` instead of reusing the overlong task.

An empty/null completion relay is treated as a transport problem, not task failure. Project Lead recovers the original terminal record before any rerun. It never repeats execution or review merely to reproduce missing text; if the record is unavailable, it reports `blocked_on_relay`.

## Automatic skill routing and discovery

**You describe the outcome, not the skill name.** At project intake and before each new phase, Project Lead:

- automatically selects and invokes at most one relevant installed skill when the work has a concrete trigger;
- selects no supporting skill for ordinary bounded work instead of loading tools “just in case”;
- performs one privacy-safe, read-only public search only when a required specialist acceptance method is genuinely missing; and
- recommends at most three candidates, explains their project value and risk, and asks before any installation.

For example, it may use `apple-design` for a gesture-driven Apple interface, `codebase-design` for real module-boundary friction, or `webapp-testing` for a runnable web acceptance path. Candidate instructions are treated as untrusted information during discovery and are never executed or installed automatically.

## Direct communication between tasks

For real dependencies, the controller passes verified same-project peer IDs, ownership and communication limits in the task brief. Executors may ask one focused clarification and share existing evidence directly when the task exposes the messaging tools; the user need not relay each message. They cannot reassign work, change another task's route, edit another owner's files or approve completion. Read completed results instead of waking a task for status. No broadcasts, acknowledgment loops or repeated status checks; unresolved conflicts go to the controller once. Messages may wake a task and consume usage. If tools are absent, the controller relays the question; the skill cannot create missing platform capabilities.

## Automatic execution-model routing

Astra's exact model ID is **`gpt-6-astra`**. This update preserves the tiered workflow instead of moving every child to the flagship. Existing project routing authorization survives the migration; neither controller effort nor Fast settings flow to child tasks.

| Role | Model policy |
| --- | --- |
| Controller | User-selected model and effort; Astra is supported. |
| Necessary independent reviewer | A separate authorized Astra or Sol; prefer suitable Sol for Astra-authored work. Explicit user model constraints win. |
| Implementation | Astra preferred for substantive work; Terra or eligible text-only Spark when better suited. No compulsory model trial or fixed effort. |
| Ordinary work | Executor checks and controller acceptance; no Standard/Terra reviewer stage. |
| Read-only information helper | Luna, with no implementation or acceptance authority. |

Read the current target host's model and effort options before selection; do not manufacture aliases or assume API and desktop mode names are interchangeable. [Model-routing details and official sources](skills/project-lead/references/model-routing.md).

The user authorizes automatic routing once per project. For every new objective, Project Lead chooses both the model and reasoning effort from the current bounded child objective: its actions, uncertainty, coupling, consequences, checks, and combinations exposed by the dispatch tool. It never inherits the previous objective's route and never inherits effort from the parent project, review lane, or previous task.

- Spark high handles an exact reversible path with deterministic checks. Spark xhigh additionally requires a named hard local reasoning risk; Low-risk classification alone is not enough. Spark is text-only; screenshot interpretation and image-dependent UI work go to a capable executor, normally Terra.
- Terra high handles one coherent implementation, debugging, or design problem with known contracts and checks. Terra xhigh requires multiple plausible causes or designs, or inseparable interacting constraints. Terra Ultra requires one objective that actually runs large independent workstreams with no shared mutable files.
- Luna defaults to medium for read-only extraction, may use high for dense multi-source evidence, and uses xhigh only for difficult contradictions. Its authority stays read-only at every effort.
- Independent review is reserved for concrete major/security consequences or an explicit user request. Changing the execution model does not add a review or reopen an accepted verdict.
- Astra is preferred, not mandatory. The controller retains judgment and may choose Terra or Spark directly, without first trying Astra. Sol remains reserved for control and independent review.

These effort examples are not mandatory floors. Low and medium are eligible when supported and sufficient. Reviewer effort is chosen separately; an Elevated label never forces xhigh. Max gives a single hard problem more reasoning, while desktop Ultra uses permitted parallel helpers and is not automatically a valid API effort.

Before xhigh, Max, or Ultra, Project Lead performs one silent controller judgment: it names a concrete failure risk at the next lower effort. This uses no tool call, extra task, Luna call, or parallel model comparison. File count, long context, architecture/security labels, and prior failure are not enough; when the cause or scope narrows, the next follow-up is downgraded unless the higher-effort risk remains.

Project Lead announces the task, model, effort, and actual speed immediately before dispatch, adds one short task-specific reason, and does not wait for approval. The notice is a rendered two-column Markdown table with task, task title, model, reasoning effort, speed and selection reason; simultaneous tasks can share one table with a row per task. It is not a code block or decision request. Speed is ordinary by default and shows Fast only after an explicit request for that exact objective. If capacity or route verification changes the choice, it sends a corrected notice before redispatch.

Formal `create_thread` executor tasks start fresh. Internal helper and reviewer tasks receive no or bounded history; full-history inheritance is never used. If dispatch exposes the resolved route atomically, Project Lead verifies it. Routine accepted dispatches do not create handshake-only tasks when explicit supported model and effort were sent and no mismatch evidence exists; this includes Elevated review. Request acceptance is recorded separately from runtime verification. Concrete mismatches must be resolved before more work; otherwise report `blocked_on_routing`. A model's self-report cannot verify the route.

A follow-up API without route fields cannot switch an existing task in place; after the current turn ends or is interrupted, the logical scope is handed to one correctly routed task without overlapping owners. A Spark-to-Terra fallback waits only for the active Spark turn on the same objective or logical scope; independent scopes may continue in parallel.

When an existing task is idle and `send_message_to_thread` supports `model` and `thinking`, explicitly pass both for the next turn and reuse it. This applies to executor and Luna effort changes. Never change an active turn's route or create a replacement solely because an idle task needs a supported route change.

If a Spark attempt hits a usage, quota, or capacity limit, Project Lead first makes that attempt terminal, reconciles any partial work in the live worktree, and redispatches the remaining objective once to Terra without asking. Terra effort is selected from the remaining work instead of inherited from Spark. This objective-local fallback does not become the project default and will not bounce back to Spark during the same objective. If Terra also hits model capacity, Project Lead reports `blocked_on_capacity` instead of bouncing between models.

## Child tasks use Standard speed by default

Fast speed is not the Low-risk lane. The controller may keep its user-configured speed, but that setting grants no speed authority to delegated work. By default, every new child task starts at Standard/default, including follow-ups, and Project Lead never asks whether to use Fast. Fast is used only when the user explicitly requests Fast for that exact child objective; the permission expires with the objective.

When the dispatch API has no speed field, Project Lead omits any Fast/priority override and uses the platform Standard/default. The missing field does not block ordinary dispatch. If runtime evidence later shows unexpected Fast/priority, the controller stops further follow-ups and reports it.

Without service-tier readback, the notice says `平台默认（未回读）` (platform default, not read back); it does not claim the actual service tier has been verified.

## Luna as a read-only information assistant

When large or repetitive evidence would materially expand controller context or cost, Project Lead keeps one logical project-scoped `gpt-5.6-luna` assistant scope, normally at medium. An idle helper receives a new effort through supported explicit route fields; replacement is only needed when the interface or context boundary requires it. Luna summarizes long task reports, logs, and test output; extracts progress, blockers, approvals, and terminal state; deduplicates repeated status; and drafts the plain-language update.

Luna is not used for a few lines or routine updates. Its result remains advisory and source-bound, so the controller verifies primary evidence before acting. Luna never writes code, selects models, reviews, accepts, or marks work complete, and it never replaces required verification.

## Event-driven completion relay

After delegated work is accepted, Project Lead keeps the controller turn open with `wait_threads` until every promised target finishes or needs attention. A timeout only renews the event wait; it does not trigger status polling, repeated reads, or Luna. When one target finishes, the controller relays it in commentary and continues waiting for the others.

The controller ends early only for required user input, an explicit user stop, or an unavailable event-wait tool. When `wait_threads` is unavailable, it gives one concise degraded-mode notice: automatic completion relay is unavailable in this client, but the accepted or running task is unchanged. It does not retry the interface, poll, call Luna, or repeat the warning in that controller turn. It ends after the current report; the user can later say `continue` or `follow up` for one fresh read. Luna and the 30-minute rule cannot wake an idle controller.

## Risk-based review lanes

| Lane | Use when | Review behavior |
| --- | --- | --- |
| Low-risk — default | Copy, styling, tests, local fixes, small reversible behavior, isolated work under accepted interfaces | No independent reviewer. The controller verifies the real diff, worktree, and focused checks, then accepts. |
| Elevated | Actual risk to money, authentication/authorization, secrets/privacy, data integrity or major production availability, including unsafe migrations and consequential releases | One separate authorized Astra/Sol reviewer on a stable candidate, with task-selected effort. Module names, file count, and a routine integration alone do not trigger it. |

No lane repeats the same incremental review loop after two returns. Necessary reviews reuse valid exact-candidate evidence and return reproducible Critical/Important findings together. Minor issues do not trigger repair/re-review. After a second return, dispatch one root-cause repair and one final independent closure review. Never launch a fourth review; unresolved material findings remain `RETURN` / `blocked_on_quality`.

## How it works

1. Inspect the live repository and active tasks.
2. Separate the current usable outcome from optional later work.
3. Keep one owner per mutable scope and reuse that task for repair.
4. Choose ordinary acceptance or Elevated review from concrete failure consequences.
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

Receipts are deduplicated by task and accepted candidate. A message may wake the task, but creates no new work or promised wait target; its acknowledgment never triggers another receipt.

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
- `requesting-code-review` is used only for necessary or explicitly requested independent review.
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
