# When a step does not work

## The agent cannot see a file

Check the selected working directory, the exact path and the tool's read permissions. Name the required files explicitly. A chat-only interface may require you to paste the synthetic example notes and save the results manually. Do not describe that as automatic filesystem access.

## The generator says a file already exists

Keep the existing work. For a first trial, select a new empty target and rerun `--dry-run`. The generator refuses collisions by default. `--force` authorizes overwriting; it should not be a routine response to an unexplained error.

## The configuration is rejected

Use the bundled [starter config](../../skills/portable-agentic-system/pas/examples/starter-config.json) to identify the expected fields. Each agent needs a meaningful routing description, exclusions and positive/negative examples. Copy it to your own working file before changing it. The current generator creates a standard scaffold; it has no minimal-profile switch.

## Status is out of date

In a standard scaffold, edit the task records first and regenerate `STATUS.md` with `generate_status.py`. `--check` reports whether the view is current; it does not update it. A small tutorial handoff is not a standard task manifest.

## A check passes but the runtime does not behave as expected

Separate configuration inspection from an actual fresh-session test. Follow only the selected adapter, verify the installed version and hook trust requirements, and retain the failure. Do not solve uncertainty by marking the runtime verified.

## A PDF is stale or has missing text

Follow [Contributing](../../CONTRIBUTING.md) to rebuild the reading copies and both PDFs. `check_docs.py` checks source hashes, navigation, external link annotations and fonts. If a new character is outside the font subset, extend it using the documented font preparation process. Render every page after the repair.

## A source is missing

Name the missing input and narrow the conclusion. In the example, Maple Studio's step-free entry is unspecified; that remains unknown. If an external action times out, read back its state before retrying when duplication would matter.
