# Model roles and migration

Read for the first model decision, then reuse within this turn; refresh after a route rejection or a changed tool catalog. Resolve combinations from the current target host's dispatch schema, not an old transcript or a guessed product name. `gpt-6-astra` is the Astra ID. Do not synthesize a 5.6-family Astra alias, rename Terra/Luna, or assume that API efforts and desktop modes are identical. If the catalog is unavailable, keep only a route already verified and authorized on this surface; otherwise report `blocked_on_routing` for that scope.

## Roles

- Controller: retain the user's selected model and effort. This migration supports Astra controllers without changing global settings or running tasks.
- Formal implementation: consider `gpt-6-astra` first for substantive implementation, repairs and multi-step work. This is a preference, not a requirement: the controller may choose `gpt-5.6-terra` or eligible `gpt-5.3-codex-spark` directly for better task fit, latency or capacity. Do not force a trial or failure on another model. Preserve explicit user model constraints; Sol remains controller/review-only under existing authorization.
- Independent review: only for a concrete major/security consequence or an explicit user request. For Astra-authored work, prefer `gpt-5.6-sol` when suitable, exposed and authorized; for other authors, consider Astra. An explicit Astra-only requirement wins. A separate fresh Astra reviewer is also independent: different model names alone neither establish nor guarantee independence. Never let the author certify its own required review. If no capable authorized reviewer is available, report the scoped blocker; do not waive the gate or silently change authorization.
- Ordinary tasks have no extra Standard/Terra review stage. Select reviewer effort separately from execution. A new model release does not reopen an accepted review or add a review round.
- Information assistance: `gpt-5.6-luna`, read-only and advisory under the Luna reference. Do not convert existing assistance permission into coding or acceptance authority.

## Effort and modality

These examples calibrate judgment; they are not an exhaustive effort allowlist or a mandatory floor. Choose any supported level justified by the actual task, including low or medium. Never copy the controller's effort or promote a whole project after one difficult task.

- Spark `high`: exact reversible scope, one path, deterministic checks. Spark `xhigh`: the same bounded scope plus a named hard local reasoning risk; Low-risk alone is insufficient. Spark is text-only: if the next task must inspect images, screenshots, visual UI state, or use image-dependent computer tools, choose a model with those capabilities, normally Terra. Higher Spark effort cannot supply a missing modality.
- Terra `high`: one coherent implementation, debugging, or design problem with known contracts and checks. Terra `xhigh`: multiple plausible causes or designs, or inseparable interacting constraints. Terra `ultra`: one objective actually runs large independent workstreams with no shared mutable files.
- Luna uses `medium` for ordinary evidence extraction, `high` for dense multi-source evidence, and `xhigh` only for hard contradictions. Simpler extraction may use a lower supported effort.
- Astra execution/review: low may fit a well-scoped task with clear checks; medium/high may fit additional planning and analysis; xhigh needs unresolved interacting risks. No level is a default or compulsory starting point. `max` needs a named single-problem depth requirement beyond the lower effort. Sol review effort follows the same task-based principle. These are judgments, not guaranteed performance equivalences between models.
- `ultra` is a desktop parallel-work mode, not an API reasoning-effort assumption. Use it only when the dispatch interface exposes it and the task has actual independent work suitable for permitted helpers. It never replaces required visible owners, independent review, or serial access to shared files.

Apply the core's no-extra-call risk check to execution, review, and assistance. Missing evidence calls for a bounded read, not an automatic effort increase. Reassess the next turn after a scope reduction. Keep child speed Standard/default; Astra migration grants no Fast permission.

File count, long context, labels such as architecture or security, and a prior failure do not alone justify `xhigh`, `max`, or `ultra`. When causes or scope narrow, re-evaluate and downgrade the next follow-up when the higher-effort risk no longer exists.

## Evidence for this migration

The Astra-first preference is provisional local operating policy, informed by a small real-task sample, not a universal benchmark or quota-saving claim. Assess normal completed work by total delivery time, confirmed defects, and execution plus repair/review usage. Separate input, cached input and output tokens when available; fewer tokens do not establish lower subscription usage. Keep unavailable usage unknown. Do not run duplicate tasks or add reviews just to collect samples; a ten-task checkpoint is a review point, not proof that safety review can be removed.

Checked 2026-09-06: [OpenAI model selection](https://learn.chatgpt.com/docs/models) identifies Astra, Terra, Luna, and text-only Spark and distinguishes Max from Ultra. [Astra API model details](https://developers.openai.com/api/docs/models/gpt-6-astra) list `low`, `medium`, `high`, `xhigh`, and `max`. The local Codex dispatch schema additionally exposes Astra `ultra`. Host availability remains authoritative for a dispatch; these sources do not prove any account-specific quota saving.
