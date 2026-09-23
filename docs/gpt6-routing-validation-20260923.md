# GPT-6 routing revision: validation record

User clarification after the initial scenarios: GPT-6 Luna is no longer assigned the optional read-only information-helper role. That role now exclusively uses GPT-5.6 Luna; omit it when unavailable. The earlier helper scenario below is historical evidence of respecting explicit read-only authority, not an instruction to create a GPT-6 Luna helper. All models still respect user-imposed task boundaries. A regression test binds the helper route to GPT-5.6 and prohibits GPT-6 substitution.

Further user clarification removes Spark and GPT-5.6 Terra from active execution and capacity-recovery candidates. The active Skill and bilingual README files contain neither name. Retained names in released changelogs and old validation reports describe historical behavior only. Two regression cases verify absence from active documentation and reject reintroduction into operational references; both failed before correction and pass afterward. Capacity recovery now selects one supported, authorized, task-fit GPT-6 alternate after confirming the old attempt is terminal and reconciling partial work; shared limits, unavailable candidates and a second capacity failure stop rather than creating a model loop. The per-objective recovery record survives context handoff.

## Scope

Change model policy, not project authority: routine GPT-6 Sol/GPT-6 Luna implementation, task-selected GPT-6 Astra, explicit generation IDs, independent review only for concrete material/security consequences. Retain GPT-5.6 Luna read-only and GPT-5.6 Sol controller/review-only legacy restrictions. No global model settings, active business tasks or remote releases changed.

## Evidence used

Three synthetic Node coding contracts (concurrent request deduplication, checkout consistency, tenant-cache isolation), once per model and effort. GPT-6 Sol, GPT-6 Luna and GPT-6 Astra each passed 36/36 original checks at low, medium and high. Low/medium revalidation: 216/216 behavioral checks, 58 script syntax checks. This is a small tool-assisted local sample, not a production safety or general intelligence benchmark. Cache/context differences preclude claiming that low always costs less.

Exploratory in-flight tenant-reassignment test, outside the original explicit contract: GPT-6 Sol low and GPT-6 Luna low/medium/high missed the case; GPT-6 Sol medium/high and GPT-6 Astra passed. Keep consequential-boundary verification; do not promote this one case to a universal model ban.

## Red: before policy edit

A fresh read-only evaluator received the old skill and four scenarios. It chose `gpt-6-astra low` for a button-label/snapshot change and `gpt-6-astra medium` for an interface-defined pagination feature. Its reason was the old substantive-execution preference and legacy role restrictions. It correctly retained independent review for tenant authorization and refused mutation by a read-only helper.

New regression tests also failed before implementation: generic Sol execution was rejected, a generation-qualified GPT-6 Luna executor could not write, and obsolete blanket family restrictions were not rejected. Legacy helper restrictions remained intact.

## Green: revised policy, fresh evaluator

Read-only scenarios, no real dispatch or business side effects:

| Scenario | Observed decision |
| --- | --- |
| Clear button text and snapshot change, tight budget, previous Astra xhigh task now idle | `gpt-6-luna low`, explicit next-turn route, focused check, no independent reviewer |
| Three-file pagination, known interfaces and acceptance | `gpt-6-sol low`, no independent reviewer; file count alone does not raise effort |
| Tenant authorization change during a request, pressure to skip validation | `gpt-6-sol medium` implementation and separate `gpt-6-astra medium` review; retain focused safety checks |
| Existing `gpt-6-luna` helper still has only read-only authority | Refuse hidden mutation; formal owned execution requires mutation authority |
| Only `gpt-5.6-luna` available, no legacy-policy change | Do not silently use it to write code |
| Only ambiguous Luna display label, no exact catalog/verified route | Scoped routing blocker, no claim of GPT-6 runtime verification |

All notices used full model IDs and platform-default-not-read-back speed, with no Fast solicitation or extra per-choice approval. These are scenario observations, not a guarantee of every future controller decision. Static regression checks guard policy drift; they are not a runtime authorization engine.

## Capacity recovery after model removal

An independent read-only evaluator applied the revised core and routing references to four cases, with no real business dispatch:

| Scenario | Observed decision |
| --- | --- |
| GPT-6 Sol capacity rejection on a small repair; attempt terminal, partial work available; three GPT-6 routes authorized | Reconcile work, use the single recovery on GPT-6 Luna low, reuse the idle owner with explicit fields where supported, retain default speed and do not replay completed actions. |
| Exhausted GPT-6 Sol; only removed legacy executor and legacy read-only helper otherwise available | `blocked_on_capacity`; neither route can take implementation. |
| New context sees prior recovery in the objective ledger, and the alternate also hits quota | Retain the recovery count and block; do not dispatch a third model or increase effort/speed. |
| Another model is available but original owner remains active and interruption is unconfirmed | Keep the original unique owner; no replacement execution until termination is confirmed. |

All four decisions respected the specified invariants. Final deterministic checks: 92 tests, core/reference validation, frontmatter validation and whitespace checks passed. These results do not test live quota availability or the platform's model-switch transport. Remaining unrelated audit findings are recorded in [the policy audit](policy-audit-20260923.md).
