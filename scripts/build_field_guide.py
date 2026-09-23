#!/usr/bin/env python3
"""Build linked bilingual PDFs directly from the canonical Markdown chapters."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import re
from pathlib import Path
from urllib.parse import quote, unquote
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, PageBreak,
                               Spacer, Table, TableStyle, Flowable, CondPageBreak, KeepTogether, NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus import paragraph as paragraph_layout
from reportlab.lib import textsplit
from build_master_playbook import ROOT, settings, chapters, source_manifest
rl_config.invariant = 1
# ReportLab's Japanese kinsoku list omits these common Chinese closing marks.
# Extend only this renderer's in-process line-breaking tables.
for layout in (paragraph_layout, textsplit):
    layout.ALL_CANNOT_START += '，；：！？、。）》】〉」』”’'
INK=colors.HexColor('#172D36')
TEAL=colors.HexColor('#12665F')
MUTED=colors.HexColor('#61747A')
PALE=colors.HexColor('#EEF4F1')
LINE=colors.HexColor('#D2DFDB')
PAGE_W,PAGE_H=A4
MARGIN=52
WIDTH=PAGE_W-2*MARGIN
FIGURE_W,FIGURE_H=landscape(A4)
FIGURE_MARGIN=28

class DiagramPage(Flowable):
    """Keep the author's full diagram sharp on a dedicated landscape page."""
    def __init__(self,path,caption,style):
        Flowable.__init__(self)
        self.path=path
        self.caption=Paragraph(html.escape(caption),style)
        self.width=FIGURE_W-2*FIGURE_MARGIN
        self.height=FIGURE_H-88
    def wrap(self,available,height):
        return self.width,self.height
    def draw(self):
        _,caption_height=self.caption.wrap(self.width,50)
        picture=ImageReader(str(self.path))
        width,height=picture.getSize()
        scale=min(self.width/width,(self.height-caption_height-12)/height)
        draw_width,draw_height=width*scale,height*scale
        self.canv.drawImage(picture,(self.width-draw_width)/2,self.height-draw_height,
                            width=draw_width,height=draw_height,mask='auto')
        self.caption.drawOn(self.canv,0,0)

def register_fonts():
    folder=ROOT/'docs/assets/fonts'
    for name,filename in [('Text','PlugChugSans-Regular.ttf'),('Strong','PlugChugSans-Semibold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(folder/filename)))
    pdfmetrics.registerFontFamily('Text',normal='Text',bold='Strong',italic='Text',boldItalic='Strong')

def styles(language):
    base=ParagraphStyle('Body',fontName='Text',textColor=INK,fontSize=10.5,leading=16.4,
                        wordWrap='CJK' if language=='zh-CN' else None,splitLongWords=True,spaceAfter=8)
    return {
      'body':base,
      'h1':ParagraphStyle('Chapter',parent=base,fontName='Strong',fontSize=24,leading=31,spaceAfter=20,keepWithNext=True),
      'chapter':ParagraphStyle('ChapterStart',parent=base,fontName='Strong',fontSize=24,leading=31,spaceBefore=30,spaceAfter=20,keepWithNext=True),
      'h2':ParagraphStyle('Section',parent=base,fontName='Strong',fontSize=14,leading=20,textColor=TEAL,spaceBefore=15,spaceAfter=8,keepWithNext=True),
      'h3':ParagraphStyle('Subsection',parent=base,fontName='Strong',fontSize=11.5,leading=17,spaceBefore=10,spaceAfter=6,keepWithNext=True),
      'list':ParagraphStyle('List',parent=base,leftIndent=15,firstLineIndent=0,bulletIndent=0,spaceAfter=5),
      'quote':ParagraphStyle('Quote',parent=base,leftIndent=14,rightIndent=10,textColor=TEAL,spaceBefore=5,spaceAfter=10),
      'table':ParagraphStyle('Cell',parent=base,fontSize=9,leading=13,spaceAfter=0),
      'tablehead':ParagraphStyle('CellHead',parent=base,fontName='Strong',fontSize=9,leading=13,textColor=colors.white,spaceAfter=0),
      'small':ParagraphStyle('Small',parent=base,fontSize=8.5,leading=12.5,textColor=MUTED),
      'eyebrow':ParagraphStyle('Eyebrow',parent=base,fontName='Strong',fontSize=10,leading=15,textColor=TEAL,spaceAfter=12),
      'toc':ParagraphStyle('Contents',parent=base,fontSize=11.5,leading=18,spaceBefore=5,spaceAfter=8),
      'title':ParagraphStyle('Title',parent=base,fontName='Strong',fontSize=35,leading=46,spaceAfter=21),
      'subtitle':ParagraphStyle('Subtitle',parent=base,fontSize=15,leading=24,textColor=TEAL,spaceAfter=18),
    }

class CodeBlock(Flowable):
    """Wrap at glyph boundaries, keeping every code character on the page."""
    def __init__(self,text,lines=None):
        Flowable.__init__(self)
        self.text,self.lines=text,lines
        self.spaceBefore,self.spaceAfter=5,12
        self.font='Text' if re.search(r'[^\x00-\x7f]',text) else 'Courier'
        self.size,self.leading,self.pad=8.3,12.6,10
    def wrap(self,available,height):
        self.width=available
        if self.lines is None:
            self.lines=[]
            for raw in self.text.expandtabs(4).splitlines() or ['']:
                current=''
                for ch in raw:
                    if pdfmetrics.stringWidth(current+ch,self.font,self.size)>available-2*self.pad:
                        self.lines.append(current);current=ch
                    else: current+=ch
                self.lines.append(current)
        self.height=len(self.lines)*self.leading+2*self.pad
        return self.width,self.height
    def split(self,available,height):
        self.wrap(available,height)
        if len(self.lines)<=18: return []
        count=int((height-2*self.pad)/self.leading)
        if count<2: return []
        return [CodeBlock(self.text,self.lines[:count]),CodeBlock(self.text,self.lines[count:])]
    def draw(self):
        c=self.canv
        c.setFillColor(PALE);c.roundRect(0,0,self.width,self.height,3,fill=1,stroke=0)
        c.setFillColor(INK);c.setFont(self.font,self.size)
        for i,line in enumerate(self.lines):
            c.drawString(self.pad,self.height-self.pad-self.size-i*self.leading,line)

class WorkFlow(Flowable):
    def __init__(self,language):
        Flowable.__init__(self)
        self.language=language
        self.width,self.height=WIDTH,108
    def draw(self):
        labels=['A real task','Working files','Checked result','A next step']
        if self.language=='zh-CN': labels=['一项真实任务','整理工作材料','检查形成成果','留下下一步']
        c=self.canv;w=(self.width-42)/4
        for i,label in enumerate(labels):
            x=i*(w+14)
            c.setFillColor(PALE);c.roundRect(x,25,w,65,5,stroke=0,fill=1)
            c.setFillColor(TEAL);c.setFont('Strong',9);c.drawString(x+11,70,f'0{i+1}')
            c.setFillColor(INK);c.setFont('Text',10);c.drawString(x+11,44,label)
            if i<3:
                c.setStrokeColor(TEAL);c.line(x+w+3,56,x+w+11,56)
                c.line(x+w+8,59,x+w+11,56);c.line(x+w+8,53,x+w+11,56)

def destination(target,source,chapter_map):
    if target.startswith(('https://','http://','mailto:')): return target
    raw,_,fragment=target.partition('#')
    if not raw:
        return settings()['repository']+'/blob/main/'+source.relative_to(ROOT).as_posix()+('#'+fragment if fragment else '')
    resolved=(source.parent/unquote(raw)).resolve()
    if resolved in chapter_map and not fragment: return '#'+chapter_map[resolved]
    relative=resolved.relative_to(ROOT).as_posix()
    return settings()['repository']+'/blob/main/'+quote(relative,safe='/')+('#'+fragment if fragment else '')

def inline(text,source,chapter_map,refs):
    tokens={}
    def reserve(value):
        key=f'ZZINLINE{len(tokens)}ZZ';tokens[key]=value;return key
    def code(match):
        value=match[1];font='Text' if re.search(r'[^\x00-\x7f]',value) else 'Courier'
        return reserve(f'<font name="{font}" size="9">{html.escape(value)}</font>')
    text=re.sub(r'`([^`]+)`',code,text)
    def link(match):
        label,target=match[1],match[2]
        url=destination(target,source,chapter_map)
        plain_label=label
        for key,value in tokens.items():
            plain_label=plain_label.replace(key,html.unescape(re.sub(r'<[^>]+>','',value)))
        if not url.startswith('#') and (plain_label,url) not in refs: refs.append((plain_label,url))
        return reserve(f'<a href="{html.escape(url,quote=True)}" color="#12665F"><u>{html.escape(label)}</u></a>')
    text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)
    text=html.escape(text)
    text=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',text)
    text=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',text)
    for key,value in reversed(list(tokens.items())):text=text.replace(key,value)
    return text

def markdown(text,source,chapter_map,sty,refs):
    lines=text.splitlines();story=[];i=0
    fmt=lambda t:inline(t,source,chapter_map,refs)
    while i<len(lines):
        line=lines[i].strip()
        if not line or line=='---' or line.startswith('<!--'):i+=1;continue
        if line.startswith('!['):
            match=re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)',line)
            if not match:raise ValueError(f'Unsupported image block: {source}')
            path=(source.parent/unquote(match[2])).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():raise ValueError(f'Invalid diagram: {path}')
            story.extend([NextPageTemplate('figure'),PageBreak(),DiagramPage(path,match[1],sty['small']),
                          NextPageTemplate('reading'),PageBreak()]);i+=1;continue
        if line.startswith('```'):
            block=[];i+=1
            while i<len(lines) and not lines[i].startswith('```'):block.append(lines[i]);i+=1
            if story and isinstance(story[-1],Paragraph):story[-1].keepWithNext=True
            story.append(CodeBlock('\n'.join(block)));i+=1;continue
        if line.startswith('# '):i+=1;continue
        if re.match(r'#{2,6} ',line):
            level='h2' if line.startswith('## ') else 'h3'
            story.append(Paragraph(fmt(re.sub(r'^#+ ','',line)),sty[level]));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[v.strip() for v in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+',v) for v in row):rows.append(row)
                i+=1
            count=max(map(len,rows))
            for row in rows:row.extend(['']*(count-len(row)))
            weights=[max(6,min(24,max(len(row[col]) for row in rows))) for col in range(count)]
            # Reserve enough room for a complete header word before distributing
            # the remaining width by content length.
            minimums=[min(WIDTH/count,max(38,max(pdfmetrics.stringWidth(word,'Strong',9)
                       for word in (re.sub(r'[*`]', '',cell).split() or ['']))+18)) for cell in rows[0]]
            remaining=WIDTH-sum(minimums)
            widths=[minimum+remaining*weight/sum(weights) for minimum,weight in zip(minimums,weights)]
            cells=[[Paragraph(fmt(v),sty['tablehead' if r==0 else 'table']) for v in row] for r,row in enumerate(rows)]
            table=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT',spaceBefore=6,spaceAfter=15)
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),TEAL),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),
              ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
              ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,0),0.7,TEAL),
              ('LINEBELOW',(0,1),(-1,-1),0.35,LINE)]))
            if story and isinstance(story[-1],Paragraph):story[-1].keepWithNext=True
            story.append(KeepTogether([table]) if table.wrap(WIDTH,PAGE_H)[1]<350 else table);continue
        bullet=re.match(r'^(?:[-*] |(\d+)\. )(.*)$',line)
        if bullet:
            label=(bullet[1]+'.') if bullet[1] else '•'
            story.append(Paragraph(fmt(bullet[2]),sty['list'],bulletText=label));i+=1;continue
        if line.startswith('> '):story.append(Paragraph(fmt(line[2:]),sty['quote']));i+=1;continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#{1,6} |```|!\[|\||[-*] |\d+\. |> |---)',lines[i].strip()):
            para.append(lines[i].strip());i+=1
        story.append(Paragraph(fmt(' '.join(para)),sty['body']))
    return story

class Guide(BaseDocTemplate):
    def __init__(self,filename,language):
        super().__init__(filename,pagesize=A4,leftMargin=MARGIN,rightMargin=MARGIN,topMargin=57,bottomMargin=53,
                         title=settings()['languages'][language]['title'],author='@kwis7',
                         subject='Plug & Chug | Personal AI workspace handbook',pageCompression=1)
        self.language=language
        frame=Frame(MARGIN,53,WIDTH,PAGE_H-110,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        figure=Frame(FIGURE_MARGIN,44,FIGURE_W-2*FIGURE_MARGIN,FIGURE_H-88,
                     leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates([PageTemplate(id='reading',frames=[frame],onPage=self.draw_page,pagesize=A4),
                               PageTemplate(id='figure',frames=[figure],onPage=self.draw_page,pagesize=landscape(A4))])
    def draw_page(self,canvas,doc):
        canvas.saveState()
        if doc.page>1:
            width,height=canvas._pagesize
            margin=FIGURE_MARGIN if width>height else MARGIN
            canvas.setFont('Text',8);canvas.setFillColor(MUTED)
            canvas.drawString(margin,height-31,'PLUG & CHUG')
            canvas.drawRightString(width-margin,height-31,settings()['edition'])
            canvas.drawString(margin,28,'@kwis7  /  '+settings()['date'])
            canvas.drawRightString(width-margin,28,str(doc.page))
        canvas.restoreState()
    def afterFlowable(self,flowable):
        if isinstance(flowable,Paragraph) and hasattr(flowable,'bookmark'):
            key=flowable.bookmark;text=flowable.getPlainText()
            self.canv.bookmarkPage(key);self.canv.addOutlineEntry(text,key,0,False)
            self.notify('TOCEntry',(0,text,self.page,key))

def build_pdf(language,output):
    register_fonts();config=settings();meta=config['languages'][language];sty=styles(language)
    sources=chapters(language);chapter_map={p.resolve():f'chapter-{i}' for i,p in enumerate(sources)}
    cover_title=html.escape(meta['title'])
    if language=='zh-CN':cover_title=cover_title.replace('，','，<br/>',1)
    story=[Spacer(1,66),Paragraph('PLUG &amp; CHUG',sty['eyebrow']),Paragraph(cover_title,sty['title']),
      Paragraph(meta['subtitle'],sty['subtitle']),Spacer(1,19),WorkFlow(language),Spacer(1,32),
      Paragraph('@kwis7',sty['h3']),Paragraph(config['edition']+' / '+config['date'],sty['small']),
      Paragraph(f'<a href="{config["repository"]}" color="#12665F">github.com/kwis7/Plug-And-Chug-Agentic-Building-Guide</a>',sty['small']),
      PageBreak(),Paragraph(meta['contents'],sty['h1'])]
    intro='Start with the first task. Return to the reference when your work needs more structure.'
    if language=='zh-CN':intro='从第一个任务开始。遇到具体问题时，再回到相应章节和技术参考。'
    story.extend([Paragraph(intro,sty['body']),Spacer(1,10)])
    toc=TableOfContents();toc.levelStyles=[sty['toc']];toc.dotsMinLevel=0;story.append(toc)
    refs=[]
    for index,source in enumerate(sources):
        text=source.read_text(encoding='utf-8')
        first=next(line[2:] for line in text.splitlines() if line.startswith('# '))
        story.append(PageBreak() if index==0 else CondPageBreak(320))
        heading=Paragraph(html.escape(first),sty['chapter'])
        heading.bookmark=chapter_map[source.resolve()];story.append(heading)
        story.extend(markdown(text,source,chapter_map,sty,refs))
    story.append(CondPageBreak(320));title=Paragraph(meta['links'],sty['chapter']);title.bookmark='further-reading';story.append(title)
    explanation='Links lead to this repository and its technical references. Product guidance carries its own evidence date; a link does not establish a new runtime verification.'
    if language=='zh-CN':explanation='本版链接指向仓库及相关技术参考。产品接入说明有各自的证据日期；保留链接不代表本次已重新验证运行行为。'
    story.append(Paragraph(explanation,sty['body']));seen=set()
    for label,url in refs:
        if url in seen:continue
        seen.add(url);story.append(CondPageBreak(50));story.append(Paragraph(html.escape(label),sty['h3']))
        story.append(Paragraph(f'<a href="{html.escape(url,quote=True)}" color="#12665F">{html.escape(unquote(url))}</a>',sty['small']))
    output.parent.mkdir(parents=True,exist_ok=True)
    Guide(str(output),language).multiBuild(story)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--language',choices=['all','en','zh-CN'],default='all')
    parser.add_argument('--output-dir',type=Path,default=ROOT/'docs/downloads')
    args=parser.parse_args();languages=settings()['languages'] if args.language=='all' else [args.language]
    for language in languages:
        path=args.output_dir/settings()['languages'][language]['pdf'];build_pdf(language,path);print(path)
    if args.language=='all':
        artifacts={settings()['languages'][lang]['pdf']:hashlib.sha256((args.output_dir/settings()['languages'][lang]['pdf']).read_bytes()).hexdigest() for lang in languages}
        manifest={**source_manifest(),'pdf_sha256':artifacts,'builder_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'fonts_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'docs/assets/fonts').glob('*.ttf'))}}
        (args.output_dir/'pdf-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':main()
