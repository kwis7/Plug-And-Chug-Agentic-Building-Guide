#!/usr/bin/env python3
"""Create redistributable static font subsets from a supplied official Noto VF."""
import argparse
import hashlib
import json
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools import subset
ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = 'f8d157532fbfaeda587e826d4cd5b21a49186f7c'
SOURCE_HASH = 'd68bafcb48a2707749396aa12bbbd833cb70401f3a9a689fd2902c7e0d295964'
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    args=parser.parse_args()
    if hashlib.sha256(args.source.read_bytes()).hexdigest() != SOURCE_HASH:
        raise SystemExit('Source font differs from the pinned upstream file. Review the source and update its provenance constants before changing fonts.')
    chars=set(range(32,0x250))|set(range(0x2000,0x2070))|set(range(0x2190,0x2200))|set(range(0x2500,0x2580))|set(range(0x3000,0x3040))|set(range(0xff00,0xfff0))
    for a in range(0xa1,0xf8):
        for b in range(0xa1,0xff):
            try: chars.update(map(ord,bytes([a,b]).decode('gb2312')))
            except UnicodeDecodeError: pass
    for path in (ROOT/'docs/handbook').rglob('*.md'):
        chars.update(map(ord,path.read_text(encoding='utf-8')))
    out=ROOT/'docs/assets/fonts'
    out.mkdir(parents=True,exist_ok=True)
    for weight,name in [(400,'Regular'),(600,'Semibold')]:
        font=TTFont(args.source,recalcTimestamp=False)
        font=instantiateVariableFont(font,{'wght':weight},inplace=True)
        options=subset.Options()
        options.recalc_timestamp=False
        options.name_IDs=['*']
        options.name_legacy=True
        options.name_languages=['*']
        sub=subset.Subsetter(options=options)
        sub.populate(unicodes=chars)
        sub.subset(font)
        names={1:'PlugChug Sans',2:name,3:'PlugChugSans-'+name,4:'PlugChug Sans '+name,6:'PlugChugSans-'+name,16:'PlugChug Sans',17:name}
        for record in font['name'].names:
            if record.nameID in names:
                record.string=names[record.nameID].encode(record.getEncoding())
        font.save(out/f'PlugChugSans-{name}.ttf')
    receipt={'source_repository':'https://github.com/notofonts/noto-cjk','source_commit':SOURCE_SHA,'source_path':'Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf','source_sha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),'license':'SIL Open Font License 1.1','derivation':'Static weights 400 and 600, GB2312 plus Latin, punctuation, arrows, box drawing and authored handbook characters; renamed PlugChug Sans.','outputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.glob('*.ttf'))}}
    (out/'provenance.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('Prepared embedded font subsets.')
if __name__=='__main__':main()
