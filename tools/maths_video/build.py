#!/usr/bin/env python3
"""Camday maths lesson videos (Phase 2): an animated, narrated video per lesson with pause questions and captions.

Each lesson's video is authored in content/authoring/maths_video/s{stage}_u{NN}.py as VIDEOS = {"1.1": [scene, ...]},
where a scene is {"kind", "title", "steps": [{"say": narration, "do": [actions], "pause": stop id (optional)}]}.
The narration is voiced with VoiceZuno (one text_to_speech call per lesson, split by paragraph), so the build has 3 steps:
  python3 tools/maths_video/build.py text   7 1 1.1   → /tmp/mv/7_1.1/narration.txt  (paste into text_to_speech, split=paragraph)
  python3 tools/maths_video/build.py audio  7 1 1.1 URL1 URL2 …   (the audio_url of each paragraph, in order)
  python3 tools/maths_video/build.py render 7 1 1.1   → web/media/mv/s7/1-1.mp4 (+ poster) and web/media/mv/index.json
Then tools/maths_video/apply.py 7 copies the index entry into each lesson's `lv` (rebuild_maths_v4.sh runs it)."""
import importlib, json, os, re, subprocess, sys, wave
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
WEB = os.path.join(ROOT, "web")
sys.path.insert(0, os.path.join(ROOT, "content", "authoring"))
RATE, FPS, GAP, PAUSE_GAP = 24000, 25, 0.55, 1.4
FIGS = ["figures.js", "figures2.js", "figures3.js", "figures4.js", "figures5.js"]


def work(stage, sec):
    d = f"/tmp/mv/{stage}_{sec}"; os.makedirs(d, exist_ok=True); return d


def lesson(stage, unit, sec):
    m = importlib.import_module(f"maths_video.s{stage}_u{unit:02d}")
    meta = json.load(open(os.path.join(WEB, "content", f"stage{10 + stage}-unit{unit:02d}.json")))
    s = next(x for x in meta["sections"] if x["id"] == sec)
    return m.VIDEOS[sec], s


def paragraphs(stage, unit, sec):
    scenes, s = lesson(stage, unit, sec)
    intro = f"Welcome to Camday. Stage {stage} Maths. Lesson {sec}: {s['title']}."
    outro = f"Great work! Now practise lesson {sec} on Camday."
    return [intro] + [st["say"] for sc in scenes for st in sc["steps"]] + [outro]


def cmd_text(stage, unit, sec):
    p = paragraphs(stage, unit, sec); d = work(stage, sec)
    open(os.path.join(d, "narration.txt"), "w").write("\n\n".join(p))
    print(f"{len(p)} paragraphs, {sum(map(len, p))} characters → {d}/narration.txt")


def pcm(path):
    """decode any audio file to mono 16-bit PCM at RATE"""
    return subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "s16le", "-ac", "1", "-ar", str(RATE), "-"], capture_output=True, check=True).stdout


def cmd_audio(stage, unit, sec, urls):
    p = paragraphs(stage, unit, sec); d = work(stage, sec)
    assert len(urls) == len(p), f"need {len(p)} audio links, got {len(urls)}"
    for i, u in enumerate(urls):
        subprocess.run(["curl", "-sS", "-f", "-o", os.path.join(d, f"p{i:03d}.mp3"), u], check=True)
    print("downloaded", len(urls), "files")


def timeline(stage, unit, sec):
    """seconds for every step from the real audio lengths; returns spec + the audio pieces in order"""
    scenes, s = lesson(stage, unit, sec); d = work(stage, sec)
    clips = [pcm(os.path.join(d, f"p{i:03d}.mp3")) for i in range(len(paragraphs(stage, unit, sec)))]
    dur = [len(c) / 2 / RATE for c in clips]
    pieces, t = [], 0.6
    def put(i, gap):
        nonlocal t
        pieces.append((t, clips[i])); start = t; t += dur[i] + gap; return start
    put(0, 0.2); intro_end = max(4.2, t + 0.3); t = intro_end + 0.3
    k, caps, stops, out = 1, [], {}, []
    for sc in scenes:
        steps = []
        for st in sc["steps"]:
            start = put(k, PAUSE_GAP if st.get("pause") else GAP)
            caps += split_caption(st["say"], start, dur[k])
            if st.get("pause"): stops[st["pause"]] = round(start + dur[k] + 0.35, 2)
            steps.append(dict(st, start=round(start, 3), dur=dur[k])); k += 1
        for a, b in zip(steps, steps[1:]): a["next"] = b["start"]
        out.append(dict(sc, steps=steps, start=steps[0]["start"] - 0.25, end=steps[-1]["start"] + steps[-1]["dur"] + GAP))
    for sc in out:   # thermometer moves are written as [step number in the scene, value]: turn them into seconds
        for st in sc["steps"]:
            for a in st.get("do", []):
                if a.get("a") == "therm":
                    t0 = st["start"] + a.get("at", 0.15)
                    a["seq"] = [[round(sc["steps"][j]["start"] + 0.2 - t0, 3) if j else 0, v] for j, v in a["seq"]]
    outro_start = t; put(k, 0.4); total = round(t + 1.2, 2)
    caps.append([round(outro_start, 2), paragraphs(stage, unit, sec)[-1]])
    spec = dict(stageLabel=f"Stage {stage} Mathematics", lessonId=sec, lessonTitle=s["title"], introEnd=intro_end, outroStart=outro_start - 0.3,
                total=total, scenes=out, logo="file://" + os.path.join(WEB, "camday_logo.svg"), icon="file://" + os.path.join(WEB, "camday_icon.svg"))
    return spec, pieces, caps, stops, s


def split_caption(text, start, dur):
    """one caption per sentence, timed by its share of the characters"""
    parts = [p for p in re.split(r"(?<=[.!?])\s+", text.strip()) if p]
    tot, out, t = sum(map(len, parts)), [], start
    for p in parts:
        out.append([round(t, 2), p]); t += dur * len(p) / tot
    return out


def page(spec):
    kx = os.path.join(WEB, "vendor", "katex"); here = os.path.dirname(os.path.abspath(__file__))
    return (f"<!DOCTYPE html><html><head><meta charset='utf-8'><link rel='stylesheet' href='file://{kx}/katex.min.css'>"
            f"<link rel='stylesheet' href='file://{here}/engine.css'></head><body><div id='stage'></div>"
            f"<script>window.AtomicTheme=null;window.Core={{IS_MATHS:true}};</script>"
            + "".join(f"<script src='file://{os.path.join(WEB, f)}'></script>" for f in FIGS)
            + f"<script src='file://{kx}/katex.min.js'></script><script src='file://{here}/engine.js'></script>"
            f"<script>window.N=buildVideo({json.dumps(spec)});</script></body></html>")


def cmd_render(stage, unit, sec, preview=None):
    from playwright.sync_api import sync_playwright
    spec, pieces, caps, stops, s = timeline(stage, unit, sec); d = work(stage, sec)
    missing = [x["id"] for x in s["stops"] if x["id"] not in stops]
    assert not missing, f"every check question needs a pause step: {missing}"
    # audio: every clip at its exact start, silence between
    n = int(spec["total"] * RATE); buf = bytearray(n * 2)
    for t, c in pieces:
        o = int(t * RATE) * 2; buf[o:o + len(c)] = c[:len(buf) - o]
    with wave.open(os.path.join(d, "audio.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(buf))
    hp = os.path.join(d, "page.html"); open(hp, "w").write(page(spec))
    out_dir = os.path.join(WEB, "media", "mv", f"s{stage}"); os.makedirs(out_dir, exist_ok=True)
    base = sec.replace(".", "-"); mp4 = os.path.join(out_dir, base + ".mp4") if not preview else os.path.join(d, "preview.mp4")
    frames = int(spec["total"] * FPS) if not preview else int(preview * FPS)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1.5)   # 1920×1080 frames
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto("file://" + hp); pg.wait_for_timeout(800)
        assert not errs, errs
        ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-", "-i", os.path.join(d, "audio.wav"),
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k",
                               "-shortest", "-movflags", "+faststart", mp4], stdin=subprocess.PIPE)
        stage_el = pg.query_selector("#stage")
        for i in range(frames):
            pg.evaluate(f"seek({i / FPS})")
            ff.stdin.write(stage_el.screenshot(type="jpeg", quality=97))
        pg.evaluate(f"seek({spec['introEnd'] + 6})"); poster = os.path.join(out_dir, base + "_poster.jpg")
        stage_el.screenshot(path=poster, type="jpeg", quality=85)
        ff.stdin.close(); ff.wait(); br.close()
        assert not errs, errs
    if preview: print("preview", mp4); return
    real = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp4], capture_output=True, text=True).stdout)
    srt = os.path.join(out_dir, base + ".srt"); fmt = lambda x: "%02d:%02d:%02d,%03d" % (x // 3600, x % 3600 // 60, x % 60, round(x % 1 * 1000) % 1000)
    open(srt, "w").write("\n".join(f"{i + 1}\n{fmt(c[0])} --> {fmt((caps[i + 1][0] if i + 1 < len(caps) else real) - 0.05)}\n{c[1]}\n" for i, c in enumerate(caps)))
    idx_p = os.path.join(WEB, "media", "mv", "index.json"); idx = json.load(open(idx_p)) if os.path.exists(idx_p) else {}
    idx.setdefault(str(stage), {})[sec] = {"src": f"media/mv/s{stage}/{base}.mp4", "poster": f"media/mv/s{stage}/{base}_poster.jpg", "srt": f"media/mv/s{stage}/{base}.srt",
                                         "dur": round(real, 2), "captions": caps, "times": stops}
    json.dump(idx, open(idx_p, "w"), ensure_ascii=False, indent=1)
    print(f"{mp4}: {real:.1f}s, {len(caps)} captions, pauses {stops}")


if __name__ == "__main__":
    c, st, un, sec = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    if c == "text": cmd_text(st, un, sec)
    elif c == "audio": cmd_audio(st, un, sec, sys.argv[5:])
    elif c == "render": cmd_render(st, un, sec, float(sys.argv[5]) if len(sys.argv) > 5 else None)
