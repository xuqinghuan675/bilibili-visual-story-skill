#!/usr/bin/env python3
"""Read-only SVG caption ink-bounds checker using installed Inkscape.
Input manifest: samples[{id,svg,text,lines:[exact rendered text],safe_rect:[x,y,w,h]}].
Never wraps or rewrites text. A pass is geometric only, not reading/visual/release QA.
"""
import argparse, hashlib, json, math, re, subprocess, tempfile
from pathlib import Path
import xml.etree.ElementTree as ET
NS='{http://www.w3.org/2000/svg}'
FONT_CACHE={}
def font_evidence(e):
    family=e.get('font-family'); weight=e.get('font-weight','400')
    if not family or ',' in family: raise ValueError('explicit single font family required for verified match')
    key=(family,weight)
    if key not in FONT_CACHE:
        style='Bold' if weight in ('bold','700','800','900') else 'Regular'
        q=subprocess.run(['fc-match','-f','%{family}|%{style}|%{file}',family+':style='+style],capture_output=True,text=True,timeout=10)
        fields=q.stdout.split('|')
        if q.returncode or len(fields)!=3 or family not in fields[0].split(','): raise ValueError('requested font unresolved or substituted')
        fp=Path(fields[2]);FONT_CACHE[key]={'requested_family':family,'requested_weight':weight,'resolved_family':fields[0],'resolved_style':fields[1],'file':str(fp),'sha256':hashlib.sha256(fp.read_bytes()).hexdigest()}
    return FONT_CACHE[key]

def numeric_box(box):
    return isinstance(box,list) and len(box)==4 and all(isinstance(x,(float,int)) and not isinstance(x,bool) and math.isfinite(x) for x in box) and box[2]>0 and box[3]>0

def outside_edges(box, safe):
    if not numeric_box(box) or not numeric_box(safe): raise ValueError('finite positive-size rectangles required')
    x,y,w,h=box; X,Y,W,H=safe; eps=1e-4
    return [side for side,bad in [('left',x<X-eps),('top',y<Y-eps),('right',x+w>X+W+eps),('bottom',y+h>Y+H+eps)] if bad]

def inspect_svg(sample):
    safe=sample['safe_rect']; lines=sample['lines']; full=sample['text']
    if not numeric_box(safe): raise ValueError('invalid safe_rect')
    if not isinstance(lines,list) or not lines or not all(isinstance(x,str) and x for x in lines): raise ValueError('nonempty exact rendered lines required')
    if ''.join(lines)!=full: raise ValueError('rendered lines do not reconstruct original caption; no silent token splitting')
    path=Path(sample['svg']); raw=path.read_bytes()
    if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper(): raise ValueError('DTD/entities forbidden')
    root=ET.fromstring(raw)
    if root.tag!=NS+'svg': raise ValueError('SVG root required')
    for e in root.iter():
        if e.tag.rsplit('}',1)[-1] in ('script','foreignObject','image','use'): raise ValueError('external/active SVG elements unsupported')
        for k,v in e.attrib.items():
            if k.rsplit('}',1)[-1].lower().startswith('on') or k.endswith('href') or re.search(r'url\(\s*["\x27]?(?!#)',v): raise ValueError('external/active SVG attribute unsupported')
    picked=[]
    for i,line in enumerate(lines):
        hits=[e for e in root.iter(NS+'text') if ''.join(e.itertext())==line]
        if len(hits)!=1: raise ValueError(f'exact line must identify one text element: {line!r}, found {len(hits)}')
        e=hits[0]; font_evidence(e); e.set('id',f'caption-check-{i}'); picked.append((e,line))
    with tempfile.TemporaryDirectory(prefix='caption-ink-') as tmp:
        clone=Path(tmp)/'measured.svg'; clone.write_bytes(ET.tostring(root))
        proc=subprocess.run(['inkscape',str(clone),'--query-all'],text=True,capture_output=True,timeout=45)
        if proc.returncode: raise RuntimeError(f'Inkscape exit {proc.returncode}: {proc.stderr[-1000:]}')
    boxes={}
    for line in proc.stdout.splitlines():
        parts=line.split(',')
        if len(parts)==5:
            try: boxes[parts[0]]=list(map(float,parts[1:]))
            except ValueError: pass
    checks=[]
    for i,(e,line) in enumerate(picked):
        box=boxes.get(f'caption-check-{i}')
        if not numeric_box(box): raise ValueError('missing/invalid ink bbox')
        checks.append({'text':line,'ink_bbox':box,'outside_edges':outside_edges(box,safe),'declared_font_family':e.get('font-family'),'declared_font_size':e.get('font-size'),'declared_font_weight':e.get('font-weight'),'resolved_font':font_evidence(e)})
    return {'id':sample['id'],'svg':str(path),'svg_sha256':hashlib.sha256(raw).hexdigest(),'safe_rect':safe,'lines':checks,'geometry_status':'FAIL' if any(x['outside_edges'] for x in checks) else 'PASS'}

def unverified(error, sample_id=None):
    return {'id':sample_id,'geometry_status':'UNVERIFIED','error':str(error)}

def run(samples):
    results=[]
    if not isinstance(samples,list) or not samples:
        results.append(unverified('samples must be a nonempty list of objects'))
    else:
        for s in samples:
            if not isinstance(s,dict):
                results.append(unverified('each sample must be an object')); continue
            try: results.append(inspect_svg(s))
            except (ValueError,TypeError,KeyError,OSError,RuntimeError,ET.ParseError,subprocess.TimeoutExpired) as e:
                results.append(unverified(e,s.get('id')))
    engine=None
    try: engine=subprocess.check_output(['inkscape','--version'],text=True,stderr=subprocess.PIPE,timeout=10).strip()
    except (OSError,subprocess.SubprocessError) as e: results.append(unverified('Inkscape version unavailable: '+str(e)))
    return {'engine':engine,'scope':'Actual installed Inkscape ink bounding boxes of supplied SVG caption lines. No automatic wrapping, no playback, readability or release authorization.', 'release_authorized':None,'samples':results,'counts':{s:sum(r['geometry_status']==s for r in results) for s in ('PASS','FAIL','UNVERIFIED')}}

def run_manifest(manifest):
    return run(manifest.get('samples') if isinstance(manifest,dict) else None)

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('manifest');a.add_argument('--output',required=True);args=a.parse_args()
    try: result=run_manifest(json.loads(Path(args.manifest).read_text()))
    except (OSError,ValueError) as e:
        result=run(None);result['samples'][0]['error']='Cannot read manifest: '+str(e)
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result['counts']))
    raise SystemExit(0 if result['counts']['PASS'] and not result['counts']['FAIL'] and not result['counts']['UNVERIFIED'] else 1)
