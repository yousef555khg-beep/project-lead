# Task-based, cost-aware model routing

Read for the first model decision, then reuse within this turn; refresh after a route rejection or a changed tool catalog. Resolve combinations from the current target host's dispatch schema, not an old transcript. If the catalog is unavailable, keep only an already verified and authorized route on this surface; otherwise report the scoped `blocked_on_routing`.

## Exact generations and roles

This policy targets the GPT-6 generation. Family names are not dispatch IDs. Show the complete generation and pass the exact ID in every dispatch; do not silently substitute generations or invent aliases. An ambiguous display name is not runtime verification. Do not synthesize a 5.6-family Astra alias. This table is policy, not a guarantee of host availability.

| Generation and name | Exact model ID | Role under this policy |
| --- | --- | --- |
| GPT-6 Sol | `gpt-6-sol` | Preferred candidate for routine development, debugging and interacting requirements; may implement; may independently review when assigned separately |
| GPT-6 Luna | `gpt-6-luna` | Formal implementation of clear bounded edits, tests, straightforward fixes and document work with reliable checks |
| GPT-6 Astra | `gpt-6-astra` | Direct choice for difficult diagnosis, unresolved architecture or consequential reasoning where extra depth is worthwhile; may implement or independently review |
| GPT-5.6 Sol (legacy) | `gpt-5.6-sol` | Controller/review-only under retained legacy policy; this restriction does not apply to GPT-6 Sol |
| GPT-5.6 Luna (legacy) | `gpt-5.6-luna` | Read-only assistance in every role; this restriction does not apply to an authorized GPT-6 Luna executor |

Retain the user's controller model and effort; do not change global settings or active turns. New execution and capacity-recovery candidates are limited to supported, authorized GPT-6 Sol, GPT-6 Luna and GPT-6 Astra routes; do not restore older execution models from historical instructions or transcripts. For new executor work, prefer GPT-6 Sol or GPT-6 Luna when adequate. This is a preference, not a requirement: select from uncertainty, coupling, consequences, verification strength, modality, capacity and total delivery cost. Explicit user model constraints win. No compulsory model ladder or trial failure. Choose GPT-6 Astra directly when the task merits it; a security label alone is not enough. A capacity error is not proof of weak reasoning.

Only concrete material/security consequences or explicit user requests require independent review. Use a separate authorized GPT-6 Sol or GPT-6 Astra reviewer with task-selected effort. An explicit Astra-only requirement wins. Different model names neither establish nor guarantee independence; an author never certifies its own required review. GPT-6 Sol may implement important work with sufficient checks and the required review. Ordinary tasks have no extra review stage, and a model release does not reopen accepted reviews. If no capable authorized reviewer is available, report the scoped blocker rather than waiving the gate.

GPT-6 Luna is an execution candidate, not this skill's read-only information assistant. Reserve that legacy helper role for `gpt-5.6-luna`; if unavailable, omit the optional helper instead of assigning GPT-6 Luna to it. Assign implementation an explicit owned scope. All models obey user-requested read-only task boundaries; coding capability never authorizes unrequested changes. No executor accepts its own work. Do not infer authority from the bare word Luna.

## Effort: choose, do not inherit

These examples calibrate judgment; they are not an exhaustive effort allowlist or a mandatory floor. Select model and effort together for the next concrete task using supported combinations, not the parent's settings.

| Task characteristics | Effort to consider, not a fixed default |
| --- | --- |
| Explicit contract, bounded change, deterministic checks | low may suffice on GPT-6 Luna or GPT-6 Sol; GPT-6 Astra low is possible when specifically justified |
| Interacting conditions, several plausible causes, planning or less obvious edge cases | medium may be worthwhile; inspect missing evidence rather than automatically escalating |
| Difficult unresolved reasoning with material consequences or weak verification | high or above only where the task-specific benefit warrants the cost |

Before xhigh/max/ultra, apply the core's single silent lower-effort risk check: no extra agent, audit or comparison run. File count, long context, labels such as architecture or security, and a prior failure do not alone justify `xhigh`, `max`, or `ultra`. Higher effort does not guarantee correctness; lower effort does not guarantee lower total usage. When causes or scope narrow, re-evaluate and downgrade the next follow-up when the higher-effort risk no longer exists.

If a focused check fails, first distinguish an implementation mistake from missing requirements, environment/tool failure or a genuine reasoning gap. Reuse the owner for bounded repair where appropriate; reselect model/effort when justified, preserving review limits and one owner. Do not repeatedly retry a cheaper model solely to avoid upgrading. Once accepted, do not rerun work on a stronger model for reassurance.

Verify required tool/modality support for every model. Interpret max/ultra through the live interface description; do not infer parallelism or helper authorization from the name. Child speed remains Standard/default without objective-specific user Fast authorization.

## Evidence and cost limits

Local September 2026 tests used three small synthetic coding tasks, once per model/effort. GPT-6 Sol, GPT-6 Luna and GPT-6 Astra at low/medium/high each passed the original 36 checks. An extra in-flight tenant-reassignment probe was missed by GPT-6 Sol low and GPT-6 Luna low/medium/high; GPT-6 Sol medium/high and GPT-6 Astra passed. This was an exploratory boundary not explicit in the original contract, not a general security ranking. It supports focused consequential-boundary tests, not review on every task or a ban on GPT-6 Luna coding.

Compare total delivery time and verified outcome, plus execution, repair and necessary review usage. Separate noncached input, cached input and output; reasoning tokens may already be included in output. Public API/credit rates are not included subscription quota percentages. Cache and context overhead varied between runs; do not encode a fixed price ratio, guaranteed savings or universal effort optimum. Verify current prices only when needed for a cost claim, not on every dispatch. Keep missing usage unknown.

Learn from ordinary completed work without duplicate implementations, routine reviewers or new benchmark calls. A visible failure or repeated expensive rework can change the next route; one successful toy test cannot establish production readiness.
