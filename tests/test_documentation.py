"""Documentation contract tests: source drift, links, exercise facts and export."""
import json
import re
from urllib.parse import unquote
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import build_master_playbook as book
import check_docs

class DocumentationTests(unittest.TestCase):
    def test_reading_copies_are_generated_from_current_sources(self):
        for path,expected in book.generated_files().items():
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(path.read_text(encoding='utf-8'),expected)

    def test_document_links_resolve(self):
        self.assertEqual(check_docs.check_links(),[])

    def test_homepages_preserve_functional_entrypoints(self):
        # Reader-facing capabilities must remain discoverable during editorial changes.
        required = {
            'skills/portable-agentic-system/SKILL.md',
            'skills/portable-agentic-system/pas/references/friend-starter-prompt.md',
            'skills/portable-agentic-system/pas/references/intake-questions.md',
            'skills/portable-agentic-system/pas/references/filesystem-contract.md',
            'skills/portable-agentic-system/pas/references/master-build-playbook.md',
            'skills/portable-agentic-system/scripts/create_agentic_system.py',
            'docs/reference/task-lifecycle.md', 'docs/reference/compatibility.md',
            'docs/downloads/Agentic-System-Building-Guide.pdf',
        }
        for language, name, suffix in [('en','README.md',''),('zh-CN','README.zh-CN.md','.zh-CN')]:
            text=(ROOT/name).read_text(encoding='utf-8')
            targets={target.partition('#')[0] for target in check_docs.LINK.findall(text)}
            self.assertTrue(required.issubset(targets), f'{name}: missing {required-targets}')
            for stem in ['harness-concept-map','anonymised-agent-system-map']:
                self.assertIn(f'docs/assets/{stem}{suffix}.png',targets)
                self.assertIn(f'docs/assets/{stem}{suffix}.svg',targets)
            for target in check_docs.LINK.findall(text):
                if target.startswith(('http:', 'https:', 'mailto:')) or '#' not in target:
                    continue
                path,_,fragment=target.partition('#')
                destination=ROOT/path if path else ROOT/name
                content=destination.read_text(encoding='utf-8')
                anchors=set(re.findall(r'<a id="([^"]+)"',content))
                for heading in re.findall(r'^#+ (.+)$',content,re.M):
                    slug=re.sub(r'[^\w\s-]','',heading.lower()).replace(' ','-')
                    anchors.add(slug)
                self.assertIn(unquote(fragment),anchors,f'{name} -> {target}')

    def test_skill_markdown_is_self_contained(self):
        for path in book.SKILL.rglob('*.md'):
            text=path.read_text(encoding='utf-8')
            for target in check_docs.LINK.findall(text):
                if target.startswith(('http://','https://','mailto:','#')):continue
                resolved=(path.parent/target.partition('#')[0]).resolve()
                with self.subTest(path=path,target=target):
                    self.assertTrue(resolved.is_relative_to(book.SKILL))
                    self.assertTrue(resolved.exists())

    def test_rebased_links_keep_destinations(self):
        source=ROOT/'docs/handbook/en/01-first-task.md'
        target=ROOT/'docs/agentic-systems-field-guide.md'
        text=book.rebase_links('[Example](../../../examples/first-project/README.md)',source,target)
        self.assertEqual(text,'[Example](../examples/first-project/README.md)')
        self.assertEqual(book.rebase_links('[Site](https://example.com/a?q=1#b)',source,target),'[Site](https://example.com/a?q=1#b)')
        packaged=book.SKILL/'pas/references/master-build-playbook.md'
        image=book.rebase_links('![Company](../../assets/harness-concept-map.png)',ROOT/'docs/handbook/en/00-foundations.md',packaged)
        self.assertEqual(image,'![Company](https://raw.githubusercontent.com/kwis7/Plug-And-Chug-Agentic-Building-Guide/main/docs/assets/harness-concept-map.png)')

    def test_fictional_sources_keep_accessibility_unknown(self):
        folder=ROOT/'examples/first-project/sources'
        facts={p.stem:p.read_text(encoding='utf-8') for p in folder.glob('*.md')}
        self.assertIn('18',facts['cedar'])
        self.assertIn('24',facts['willow'])
        self.assertIn('20',facts['maple'])
        self.assertIn('18:00',facts['cedar'])
        self.assertIn('17:00',facts['willow'])
        self.assertRegex(facts['maple'].lower(),r'unspecified|not specified|not recorded')
        expected=(ROOT/'examples/first-project/expected/comparison.md').read_text().lower()
        self.assertIn('unknown',expected)
        self.assertIn('synthetic',expected)

    def test_pdf_sources_fonts_and_links(self):
        try:
            import pypdf
            import reportlab
        except ImportError:
            self.skipTest('Install requirements-docs.txt for PDF checks')
        self.assertEqual(check_docs.check_glyphs(),[])
        self.assertEqual(check_docs.validate_pdfs(),[])

    def test_company_diagrams_are_tracked_and_rendered_on_landscape_pages(self):
        try:
            from pypdf import PdfReader
        except ImportError:
            self.skipTest('Install requirements-docs.txt for PDF checks')
        sources={p.name for p in book.image_sources()}
        self.assertEqual(sources,{'harness-concept-map.png','harness-concept-map.zh-CN.png'})
        for meta in book.settings()['languages'].values():
            reader=PdfReader(ROOT/'docs/downloads'/meta['pdf'])
            landscape=[i for i,p in enumerate(reader.pages) if p.mediabox.width>p.mediabox.height]
            self.assertEqual(len(landscape),1)
            index=landscape[0]
            self.assertTrue(reader.pages[index].images)
            following=reader.pages[index+1]
            self.assertLess(following.mediabox.width,following.mediabox.height)

    def test_inline_code_in_link_does_not_leak_parser_tokens(self):
        try:
            import build_field_guide as pdf
        except ImportError:
            self.skipTest('Install requirements-docs.txt for exporter tests')
        refs=[]
        rendered=pdf.inline('[`README.md`](../../../README.md)',ROOT/'docs/handbook/en/00-introduction.md',{},refs)
        self.assertNotIn('ZZINLINE',rendered)
        self.assertNotIn('ZZINLINE',str(refs))
        self.assertIn('https://github.com/',rendered)

if __name__=='__main__':unittest.main()
