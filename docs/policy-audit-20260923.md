# Project Lead policy audit — 2026-09-23

Scope: current local core, operational references, bilingual descriptions and validation scripts. No business task was created, restarted, modified or messaged; no GitHub publication. Existing unrelated uncommitted work was preserved.

## Corrected during the audit at the user's request

Spark and GPT-5.6 Terra were still active compatibility/recovery candidates. Both are now removed from active Skill files and README files. New execution and execution-capacity recovery use only supported, authorized GPT-6 Sol/Luna/Astra. Existing GPT-5.6 Luna information-helper and GPT-5.6 Sol controller/review restrictions remain generation-specific, not execution fallbacks.

Capacity recovery no longer hard-codes an old model. It requires the original attempt to end, reconciles partial work, chooses one eligible alternate with fresh effort, preserves scope/default speed/unique ownership and persists the recovery count across handoff. Shared quota failures, no eligible candidate or a second capacity failure stop automatic recovery. Historical release/test evidence remains explicitly historical.

## Remaining findings — not changed in this turn

### P2: Model-policy checks have both missed conflicts and false alarms

`scripts/validate_skill_routing.py` checks a limited set of phrases and patterns in operational references; the core digest does not protect reference bytes. In-memory additions to `model-routing.md` still return no validation errors for these conflicting instructions:

```text
Use gpt-5.6-luna to implement a source-code patch.
Use gpt-6-luna as the optional read-only information assistant when the legacy route is unavailable.
Use GPT-6 Sol medium for every task.
Astra must only be used after GPT-6 Sol fails.
```

Conversely, the legitimate one-task choice `Use GPT-6 Luna for a routine bounded edit with explicit ownership and deterministic tests.` returns `luna-overuse`. That check confuses an executor's routine edit with mandatory information-helper use. These are demonstrated validator gaps, not evidence of actual unauthorized task execution.

Minimum correction: cover the demonstrated imperative/generation/role cases, narrow helper-only checks to helper roles, and require representative legal reference additions to produce no errors. Do not claim that more regexes constitute a semantic authorization engine.

### P2: Ordinary pagination can force an unnecessary new task

The core Context and relay health section treats `any pagination` as a hard rollover signal. Normal `read_thread` pagination on a short conversation is not evidence that the controller lost its own context. A controller could create another task solely because the source has more than one page, and the successor would encounter the same condition.

Minimum correction: distinguish normal API pagination from actual current-conversation compression, missing history or verified context-size thresholds. Do not add more polling or status calls.

### P2: Installation checks are loaded after the approval they are meant to inform

Core Skill discovery loads `skill-installation-safety.md` only after exact-candidate approval; that reference requires full inspection and an approval-bound manifest before recommending installation. This ordering is contradictory and can cause missing preapproval evidence or a second approval loop.

Minimum correction: load the read-only candidate-inspection rules before recommendation, while keeping every install/update/enable action behind exact user approval. The separate loader-quiescence/startup-gate requirements also need capability verification before promising installation; no installer/runtime integration was tested in this audit.

### Compatibility risk: Mandatory sidebar creation exceeds the current tool contract for ordinary delegation

The core requires `create_thread` for formal execution and context successors, and treats in-scope dispatch as controller-authorized. The current host tool contract permits creating a new user-owned task only on an explicit user request; ordinary delegated subtasks use internal collaboration tools. A generic request to repair a project is therefore not sufficient in every host environment for this prescribed sidebar workflow.

Minimum correction: make dispatch depend on both exposed capability and applicable creation authorization, while respecting the user's visible-task preference. A Skill cannot broaden a higher-priority tool contract. This is a static compatibility finding, not a newly reproduced client failure.

## Verification and limits

- 92 deterministic regression tests passed after the model-removal changes; the two new removal tests failed on the previous policy first.
- Core/reference checks, skill frontmatter validation and `git diff --check` passed.
- Four independent read-only capacity-recovery scenarios respected unique ownership, generation restrictions and the objective-local recovery bound.
- Installed Skill and repository Skill trees matched after synchronization.
- No App build, deployment or static typecheck target applies to this Markdown policy/Python validator change; no live model-switch or quota experiment was performed.
- Passing structural tests does not resolve the remaining demonstrated gaps above. Recommended next step: targeted fixes for those gaps, then rerun focused cases before publishing the broader unpublished revision.
