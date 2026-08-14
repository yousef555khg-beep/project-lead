# Project Lead

English | [简体中文](README.zh-CN.md)

A Codex skill for coordinating multi-module projects, automatically routing Spark or Terra execution and useful supporting skills, and keeping ordinary work out of unnecessary review loops.

## What changed

Project Lead now follows one rule: **use the least process that is safe for the actual risk**. Progress is measured by usable outcomes, not by task count, review count, or long technical reports.

The controller still owns scope, task ownership, blockers, acceptance, and reporting. Executors own substantial implementation. Small work can move directly; high-risk work keeps independent gates.

## Automatic skill routing and discovery

**You describe the outcome, not the skill name.** At project intake and before each new phase, Project Lead:

- automatically selects and invokes at most one relevant installed skill when the work has a concrete trigger;
- selects no supporting skill for ordinary bounded work instead of loading tools “just in case”;
- performs one privacy-safe, read-only public search only when a required specialist acceptance method is genuinely missing; and
- recommends at most three candidates, explains their project value and risk, and asks before any installation.

For example, it may use `apple-design` for a gesture-driven Apple interface, `codebase-design` for real module-boundary friction, or `webapp-testing` for a runnable web acceptance path. Candidate instructions are treated as untrusted information during discovery and are never executed or installed automatically.

## Automatic execution-model routing

The user authorizes automatic routing once per project; Project Lead does not ask again for every switch. Every new objective is classified again from its current scope, evidence, and risk, and it never inherits the previous objective's model.

- Spark is used only for Fast work whose target, accepted pattern, reversibility, and focused verification are all clear.
- Terra is the conservative choice whenever a Spark condition is false or unknown, and for Standard or Elevated implementation, non-obvious debugging, cross-module effects, or expanded scope.
- Spark-to-Terra escalation reuses the same task and sends an explicit Terra override on the next turn. A running response is not switched mid-turn, and the interrupted work is not reported complete.
- Execution routing does not weaken review independence: Standard review remains Terra, Elevated review remains Sol, and Spark never reviews its own implementation.

Spark eligibility and Spark capacity are checked separately. If the research-preview quota is exhausted or the model is unavailable before dispatch, an authorized controller explicitly falls back to Terra for that objective. If a Spark turn is already accepted, running, or queued, Project Lead does not start concurrent Terra work; it waits for a confirmed rejection, interruption, or terminal state, then rechecks availability on the next objective.

## Risk-based review lanes

| Lane | Use when | Review behavior |
| --- | --- | --- |
| Fast — default | Copy, styling, tests, local fixes, small reversible behavior, isolated work under accepted interfaces | No independent reviewer. The controller verifies the real diff, worktree, and focused checks, then accepts. |
| Standard | Meaningful multi-file work inside one module or bounded integration under accepted contracts | One batched `gpt-5.6-terra high` review after the deliverable is stable. At most one incremental repair review. Minor findings never cause a return. |
| Elevated | Authentication, authorization, secrets, privacy or regulated personal data, cryptography or security compliance, payments, destructive actions, data loss or ownership, migration, concurrency or recovery, shared contracts, cross-module integration, deployment, release, or system architecture | One stable candidate receives an independent `gpt-5.6-sol xhigh` review. A necessary irreversible architecture decision may be reviewed once before implementation. |

No lane launches a third automatic review for the same objective. After two returns, the controller stops the loop and explains the root cause and choices to the user.

## How it works

1. Inspect the live repository and active tasks.
2. Separate the current usable outcome from optional later work.
3. Keep one owner per mutable scope and reuse that task for repair.
4. Choose Fast, Standard, or Elevated from concrete risk evidence.
5. Run only the checks required by the changed surface and repository policy.
6. Report progress in plain language.

The controller may handle a brief, isolated, reversible change directly when no executor owns the files. Delegated Fast work may use Spark only when every allowlist condition is proven; substantial implementation, non-obvious debugging, long verification, and parallel modules go to Terra.

Missing information does not automatically create a system-architecture phase. The controller first inspects or asks. System architecture is reserved for a real cross-client or cross-service boundary with an unresolved shared contract, material rework risk, or an Elevated trigger.

## Plain-language reporting

The default user update is deliberately short:

```text
已完成：<用户能理解的结果>
当前结果：<能否使用或验证>
阻塞：无 | <需要用户处理的唯一事项>
下一步：<一个最有价值的动作>
```

Internal fields such as Base/Head, SHA, model, review request, and ledger state stay hidden unless the user asks or they explain a real blocker.

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
- Approval requests are surfaced immediately with the task name, exact action, effect or risk, and where the user should act. Hidden approval-card contents are never guessed.
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
