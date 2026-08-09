# V2 Local Verification - 2026-08-09

This receipt records local verification before any commit, push, release, or pull request. The test fixture contains only public synthetic names and no credentials or private data.

## Evidence labels

- `verified_static`: repository files, validators, and deterministic tests passed.
- `verified_runtime_entrypoint`: a clean installed runtime reported the intended native entrypoint.
- `partial`: some requested runtime behaviour was blocked by the local installation or authentication state.
- `not_run`: no live inference/session claim is made.

## Static suite

Command:

```bash
python3 -m unittest discover -s tests -v
```

Result after the final rebuild: `20 tests passed` with the bundled document runtime, including the 47-page PDF assertion. The same suite passed under the system Python with only the PDF assertion skipped because that interpreter lacks `pypdf`.

Covered claims:

- generated Codex, Claude Code, and Gemini bridge entrypoints;
- rejection of unsupported `@import` syntax;
- generated-status staleness detection;
- memory and context budgets;
- resource-lock ownership and guarded release;
- completion-gate rejection without receipts and acceptance with valid receipts;
- adapter classification for all 19 named products/profiles;
- progressive Skill structure and routing evaluations;
- system-map assets, guide length, and PDF page count.

The bundled `skill-creator` `quick_validate.py` was also attempted, but the system interpreter lacks its optional PyYAML dependency. No dependency was installed for this audit. Equivalent frontmatter checks passed (`name`, allowed keys, hyphen-case, description length below the 1,024-character ceiling, and a `SKILL.md` below 500 lines), and the repository's stricter description validator passed with no trigger, negative-boundary, or collision issue.

## Generated-harness self-containment

The final generator created a 99-file synthetic harness with two generic domain agents. Validation was then run from the copied `.pas/bin/` scripts inside that generated root, without importing scripts from this source repository.

- full validator: pass, 0 errors and 0 warnings;
- memory/instruction/storage budgets: pass;
- routing descriptions: pass for two agents;
- generated `STATUS.md`: current;
- static Codex, Claude Code, and Gemini adapter probes: pass;
- static health: 100/100 with `runtime_verification: not_run`;
- invalid Codex-protocol completion claim: returned `decision: block`;
- valid synthetic closeout with output, receipt, current status, released locks, budgets, and handoff: common gate passed and the translator returned an empty allow response.

These direct translator calls prove the generated scripts and host response shapes, not that an installed runtime discovered, trusted, and executed the project hook.

## Runtime smoke matrix

| Runtime | Local version | Result | Evidence and limitation |
|---|---:|---|---|
| Codex CLI | 0.147.0-alpha.6.5 | `verified_runtime_entrypoint`, then `partial` | An ephemeral read-only session in a generated fixture reported `AGENTS.md` and reproduced its first three contract rules. The installed CLI then could not read additional task/identity files because `codex-code-mode-host` is missing. This is a local runtime-installation blocker, not evidence that the repository gate is runtime verified. |
| Claude Code | 2.1.222 | `not_run` | Non-interactive fixture smoke stopped before inference with `Not logged in`. No `CLAUDE.md` runtime-loading claim is made. |
| OpenClaw | 2026.4.15 | `not_run` | Official runtime semantics were reviewed, but this repository generates no OpenClaw integration. The installed CLI's existing user config is invalid for this version because it contains an unrecognised `mcpServers` key; the audit did not rewrite it or start a gateway. |
| Gemini CLI | not installed | `not_run` | Static adapter and generated `GEMINI.md` only. |
| Hermes Agent | not installed | `not_run` | Documented runtime guide only; no generated integration. |
| MiMo Code | not installed | `not_run` | Documented runtime guide only; no generated integration. |

## Adapter claim boundary

The repository does not collapse every named product into a native runtime claim:

- Codex, Claude Code, and Gemini CLI receive generated native entrypoint/gate adapters and require a real fresh-session smoke before promotion beyond static verification;
- OpenClaw, Hermes Agent, and MiMo Code are `documented_only`; a Markdown guide is not a generated integration;
- Claude Cowork, ChatGPT Projects, Custom GPTs, and generic workspace products are manual projections;
- MiMo Claw and Tencent WorkBuddy remain provisional where native loading semantics are not proved;
- CC Switch is a provider/configuration switchboard, not a second harness;
- DeepSeek, Qwen, MiniMax, GLM, Xiaomi MiMo API, and Tencent Hunyuan are provider profiles, not local harness runtimes;
- direct API is a `reference_pattern`; a real custom harness must supply and verify its own execution loop, permissions, receipts, and gates.

## PDF and visual QA

- Final guide: 47 pages after the last content build.
- All pages rendered to PNG and inspected as contact sheets.
- The two system maps, cover, redesigned one-page contents, representative textbook chapters, appendices, and final starter-prompt page were inspected at full or contact-sheet resolution.
- The contents page uses larger linked entries, expanded vertical spacing, section grouping, and right-aligned dot leaders; all section page references remained `7/12/19/25/32/42/44/47` after regeneration.
- No empty page, clipped table, missing image, or corrupted text extraction was observed in the final build.

Final artifact SHA-256 values:

- PDF: `4db166e52309f09c16bee5a0a4848fbfc718179b02668c0a69bee4b03f956cd6`
- DOCX: `609433ad05ff010150b4e02e981162985f68c4ac21c8b9610c242ea8f965769e`
- Harness concept map PNG: `96799cf0688e84c2d6cb160ee193513c8c16286a3bc2db6975933693ab189722`
- Anonymised example map PNG: `dfd13ecf5b210fb50ebc7c7e387626fd83aeb2746c17d18fc1ba15d503db35f2`
- Core `SKILL.md`: `4708b76471e2b58c01655279a5d29e3ca644425fc77d34c7cdb7d1e5fed5a188`

## Release status

Local review only. No files were staged or committed. Nothing was pushed, published, deployed, or sent externally. Runtime gate verification remains `partial` until an authenticated Claude Code smoke and a fully functional Codex tool host are available.
