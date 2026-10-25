#!/usr/bin/env python3
"""Original, stdlib-only scene contract checks. Does not certify art or authorization."""
import json, math, sys
from pathlib import Path

def validate(d):
    errors=[]
    def need(ok,msg):
        if not ok: errors.append(msg)
    def number(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
    need(d.get('version')==1,'version must equal 1')
    need(isinstance(d.get('seed'),int) and not isinstance(d.get('seed'),bool),'seed must be integer')
    need(bool(d.get('project')),'project required')
    need(d.get('delivery') in ('preview','publish'),'delivery must be preview or publish')
    music=d.get('music',{})
    mode=music.get('mode','external')
    need(mode in ('none','external','platform'),'invalid music mode')
    need(isinstance(music.get('embedded'),bool),'music.embedded must be boolean')
    if mode!='none': need(bool(music.get('selected_title')),'selected music identity required')
    if mode=='none': need(music.get('embedded') is False,'silent mode cannot embed music')
    if mode=='external' and music.get('embedded'):
        need(music.get('license_status')=='cleared' and bool(music.get('license_evidence')),'embedded external music requires clearance evidence')
    if d.get('delivery')=='publish':
        need(d.get('publish_authorized') is True and bool(d.get('authorization_scope')),'publication authorization and scope missing')
        need(d.get('qa_status')=='pass','actual QA must pass')
        need(d.get('reference_condition_met') is True,'reference prerequisite unmet')
        need(d.get('content_updated') is True,'content update prerequisite unmet')
        if mode=='platform':
            need(bool(music.get('platform_track_id')) and music.get('platform_terms_verified') is True,'platform track identity and applicable terms unverified')
    scenes=d.get('scenes',[])
    need(isinstance(scenes,list) and bool(scenes),'scenes must be a nonempty list')
    previous=set(); seen=set(); end=0
    for s in scenes:
        sid=s.get('id','?'); prefix=f'{sid}: '
        need(isinstance(s.get('id'),str) and bool(s.get('id','').strip()),prefix+'nonempty scene id required')
        need(sid not in seen,'duplicate scene id');seen.add(sid)
        for key in ('question','claim','source','visual_change','model_boundary'): need(isinstance(s.get(key),str) and bool(s[key].strip()),prefix+key+' required')
        start,duration=s.get('start'),s.get('duration')
        if not (number(start) and number(duration) and duration>0):
            errors.append(prefix+'invalid timing');continue
        need(abs(start-end)<1e-6,prefix+'timing must be continuous from previous scene')
        end=start+duration
        objs=s.get('objects',[]); ids={o.get('id') for o in objs}
        need(bool(ids) and all(isinstance(i,str) and bool(i.strip()) for i in ids) and len(ids)==len(objs),prefix+'object IDs must be nonempty and unique')
        persistent=set(s.get('persistent_ids',[]))
        need(persistent<=ids and persistent<=previous,prefix+'persistent_ids must exist in current and previous scenes')
        if previous: need(bool(persistent) or bool(s.get('transition_reason')),prefix+'explain break in object continuity')
        beats=s.get('beats',[]);need(bool(beats),prefix+'at least one causal beat required');last=-1
        for b in beats:
            at=b.get('at')
            if not number(at): errors.append(prefix+'beat.at must be finite');continue
            need(0<=at<duration and at>=last,prefix+'beat timing invalid');last=at
            need(b.get('object_id') in ids,prefix+'beat object unknown')
            need(bool(b.get('action')) and bool(b.get('reason')),prefix+'action and explanatory reason required')
        hold=s.get('hold_after_event')
        need(number(hold) and 0<hold<=duration,prefix+'positive hold_after_event required')
        if number(hold) and last>=0: need(last+hold<=duration,prefix+'final event has insufficient hold')
        previous=ids
    return errors

if __name__=='__main__':
    try:
        d=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        errors=validate(d)
    except (OSError,ValueError,IndexError,TypeError,AttributeError) as exc:
        print('Invalid scene contract:',exc);sys.exit(2)
    print(json.dumps({'valid':not errors,'errors':errors,'scope':'structure only; visual, factual, licensing and authorization review still required'},ensure_ascii=False,indent=2))
    sys.exit(bool(errors))
