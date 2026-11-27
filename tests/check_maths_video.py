"""Maths lesson videos, checked from the files: every lesson with a video has its poster and captions file, a pause
time for each of its check questions inside a gap in the narration, and (where the mp4 is on this machine - they are
not in git) the declared length. `STAGE=7 python3 tests/check_maths_video.py`."""
import os, json, glob, subprocess
WEB = os.path.join(os.path.dirname(__file__), '..', 'web'); bad = []; n = 0
for f in sorted(glob.glob(f"{WEB}/content/stage1{os.environ.get('STAGE', '7')}-unit*.json")):
    for s in json.load(open(f))['sections']:
        lv = s.get('lv')
        if not lv: continue
        n += 1; tag = s['id']; p = os.path.join(WEB, lv['src'])
        for k in ('poster', 'srt'):
            if not os.path.exists(os.path.join(WEB, lv[k])): bad.append(f'{tag} no {k}')
        if [x['id'] for x in s['stops'] if x['id'] not in lv['times']]: bad.append(f'{tag} a check question has no pause time')
        if not os.path.exists(p): continue
        r = subprocess.run(['ffmpeg', '-i', p, '-vn', '-af', 'silencedetect=n=-38dB:d=0.3', '-f', 'null', '-'], capture_output=True, text=True).stderr
        a = [float(l.split('silence_start: ')[1]) for l in r.splitlines() if 'silence_start' in l]
        e = [float(l.split('silence_end: ')[1].split()[0]) for l in r.splitlines() if 'silence_end' in l]
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
        if abs(dur - lv['dur']) > 1: bad.append(f"{tag} length {dur:.1f}s, declared {lv['dur']}")
        for x in s['stops']:
            t = lv['times'].get(x['id'], -1)
            if not any(u - 0.05 <= t <= v + 0.05 for u, v in zip(a, e)): bad.append(f"{tag} pause {x['id']} at {t}s is not in a gap")
print('\n'.join(bad)); print(f'{n} video lessons, {len(bad)} problems'); assert not bad
