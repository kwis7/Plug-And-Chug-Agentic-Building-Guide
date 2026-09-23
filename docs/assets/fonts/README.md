# Fonts for the bilingual handbook

`PlugChugSans-Regular.ttf` and `PlugChugSans-Semibold.ttf` are renamed static subsets of Noto Sans SC, weights 400 and 600. They include GB2312 characters, Latin, punctuation, arrows, box drawing and additional authored handbook characters. Both PDFs embed the glyphs they use.

The fonts remain under [SIL OFL 1.1](OFL.txt). [provenance.json](provenance.json) records the exact upstream commit, source hash and output hashes. This keeps normal PDF builds offline and independent of system fonts.

To extend the character coverage, obtain the exact official source described in the provenance file, install the optional `requirements-fonts.txt` dependencies in an isolated environment, and run from the repository root:

```bash
python3 scripts/prepare_fonts.py /path/to/NotoSansSC-VF.ttf
```

This command performs no download. It regenerates both bundled subsets and their provenance. Review the license, output diff and PDF render again when updating fonts. A missing glyph is an error to fix, not a reason to suppress a check.
