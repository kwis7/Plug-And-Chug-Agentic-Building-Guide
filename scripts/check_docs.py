#!/usr/bin/env python3
"""Check documentation navigation, generated sources and PDF provenance."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote
from build_master_playbook import ROOT, settings, chapters, generated_files, source_manifest
LINK=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
EXCLUDED={'.git','.venv','__pycache__','build'}
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def markdown_paths():
    return [p for p in ROOT.rglob('*.md') if not EXCLUDED.intersection(p.relative_to(ROOT).parts)]
def check_links():
    errors=[]
    for source in markdown_paths():
        text=re.sub(r'```.*?```','',source.read_text(encoding='utf-8'),flags=re.S)
        for target in LINK.findall(text):
            if target.startswith(('http://','https://','mailto:','#')):continue
            path=target.partition('#')[0].strip('<>')
            resolved=(source.parent/unquote(path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f'{source.relative_to(ROOT)} -> {target}')
    return errors

def validate_pdfs():
    from pypdf import PdfReader
    errors=[]
    manifest_path=ROOT/'docs/downloads/pdf-manifest.json'
    if not manifest_path.exists():return ['PDF manifest is missing; rebuild both editions.']
    manifest=json.loads(manifest_path.read_text())
    if manifest.get('sources')!=source_manifest()['sources']:errors.append('PDF sources are stale.')
    if manifest.get('builder_sha256')!=sha(ROOT/'scripts/build_field_guide.py'):errors.append('PDF builder changed after export.')
    fonts={p.name:sha(p) for p in sorted((ROOT/'docs/assets/fonts').glob('*.ttf'))}
    if manifest.get('fonts_sha256')!=fonts:errors.append('PDF fonts changed after export.')
    for language,meta in settings()['languages'].items():
        path=ROOT/'docs/downloads'/meta['pdf']
        if not path.exists():errors.append(f'Missing PDF: {path.name}');continue
        if manifest.get('pdf_sha256',{}).get(path.name)!=sha(path):errors.append(f'PDF hash differs: {path.name}')
        reader=PdfReader(path)
        text='\n'.join(p.extract_text() or '' for p in reader.pages)
        if not reader.outline:errors.append(f'No PDF bookmarks: {path.name}')
        external=internal=0
        for page in reader.pages:
            for ref in page.get('/Annots',[]):
                a=ref.get_object()
                if a.get('/Subtype')!='/Link':continue
                if a.get('/A',{}).get('/URI'):external+=1
                if a.get('/Dest') or a.get('/A',{}).get('/S')=='/GoTo':internal+=1
        if not external or not internal:errors.append(f'Missing external or internal links: {path.name}')
        if 'ZZINLINE' in text or '\ufffd' in text:errors.append(f'Unresolved inline token or replacement glyph: {path.name}')
        if 'Cedar' not in text or 'Maple' not in text:errors.append(f'Missing worked example: {path.name}')
        if '@kwis7' not in str(reader.metadata):errors.append(f'Missing author metadata: {path.name}')
        print(f'{path.name}: {len(reader.pages)} pages; {external} external links; {internal} internal links')
    return errors

def check_glyphs():
    from reportlab.pdfbase.ttfonts import TTFont
    font=TTFont('DocGlyphAudit',str(ROOT/'docs/assets/fonts/PlugChugSans-Regular.ttf'))
    chars=set()
    for language in settings()['languages']:
        for path in chapters(language):chars.update(path.read_text(encoding='utf-8'))
    chars.update(json.dumps(settings(),ensure_ascii=False))
    missing=sorted(c for c in chars if not c.isspace() and ord(c) not in font.face.charToGlyph)
    return [f'Font missing characters: {"".join(missing)}'] if missing else []

def run(include_pdf=True):
    errors=check_links()
    for path,content in generated_files().items():
        if not path.exists() or path.read_text(encoding='utf-8')!=content:errors.append(f'Stale generated file: {path.relative_to(ROOT)}')
    if list((ROOT/'docs/downloads').glob('*.docx')):errors.append('The retired DOCX edition is still present.')
    if include_pdf:errors.extend(check_glyphs());errors.extend(validate_pdfs())
    return errors

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-pdf',action='store_true',help='Only navigation and generated Markdown; not PDF QA')
    args=parser.parse_args()
    errors=run(not args.skip_pdf)
    if errors:raise SystemExit('\n'.join(errors))
    print('Documentation checks passed. Visual inspection and runtime smoke remain separate checks.')
if __name__=='__main__':main()
