#!/usr/bin/env python3
"""Camday book pages – the 'Read the PDF' step of a Maths lesson.
For each unit whose sections carry a `book` (maths_notes_v4 BK(...)), prints Camday's own textbook-style pages
(key words, explanation, worked examples, exercise, 'Think like a mathematician', checklist; answers at the back),
then turns every page into an image for the on-site viewer:
  web/media/books/c{stage}u{NN}/p0001.webp …   web/media/books/c{stage}u{NN}.pdf   web/media/books/index.json
and writes each section's `pdf` reference (book, p0, p1, label, note, look) into web/content/stage1N-unitNN.json.
Run after tools/apply_notes_v3.py. Usage: python3 tools/build_books.py 7 [units …]"""
import glob, html, json, os, re, subprocess, sys, tempfile
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
WEB = os.path.join(ROOT, "web")
SCRIPTS = ["figures.js", "figures2.js", "figures3.js", "figures4.js", "figures5.js"]
CSS = """
@page { size: A4; margin: 14mm 14mm 16mm; }
body { font-family: 'Lexend', 'Inter', Arial, sans-serif; color: #0B1730; font-size: 11.5pt; line-height: 1.5; margin: 0; }
.band { background: #0B2545; color: #fff; padding: 10px 14px; border-radius: 6px; display: flex; justify-content: space-between; align-items: baseline; }
.band b { font-size: 15pt; } .band span { font-size: 9pt; letter-spacing: .06em; }
h1 { font-size: 22pt; margin: 12px 0 4px; } .goal { background: #FFF4C2; padding: 6px 10px; border-radius: 4px; font-size: 10pt; margin: 6px 0 10px; }
.cols { display: grid; grid-template-columns: 1fr 52mm; gap: 12px; align-items: start; }
.keys { border: 2px solid #0149AF; border-radius: 8px; padding: 6px 10px; font-size: 9.5pt; } .keys h3 { margin: 0 0 4px; color: #0149AF; font-size: 10.5pt; }
.keys p { margin: 3px 0; } .keys b { color: #0B2545; }
p { margin: 5px 0; } .fig svg { width: 100%; max-height: 62mm; } .fig { margin: 6px 0; text-align: center; }
.we { border: 2px solid #E3B505; border-radius: 8px; margin: 10px 0; break-inside: avoid; }
.we h3 { background: #FFF1B8; margin: 0; padding: 5px 10px; font-size: 11pt; border-radius: 6px 6px 0 0; } .we .q { padding: 6px 10px 2px; font-weight: 600; }
.we table { width: 100%; border-collapse: collapse; font-size: 10pt; } .we td { padding: 4px 10px; vertical-align: top; border-top: 1px dotted #E3D18A; }
.we td:first-child { width: 52%; font-weight: 600; } .we td:last-child { color: #3B4A5E; }
.ex h2 { break-after: avoid; page-break-after: avoid; font-size: 14pt; border-bottom: 3px solid #0B2545; margin: 14px 0 6px; padding-bottom: 2px; }
.qq { break-inside: avoid; margin: 8px 0; display: grid; grid-template-columns: 22px 1fr; gap: 4px; } .qq .n { font-weight: 700; }
.qq ol { list-style: lower-alpha; margin: 3px 0 0 16px; padding: 0; } .qq li { margin: 2px 0; }
.think { border: 2px dashed #7A4BD1; border-radius: 8px; padding: 6px 8px; } .think .tag { color: #7A4BD1; font-weight: 700; font-size: 9pt; letter-spacing: .05em; }
.tip { background: #E9F7EC; border-left: 4px solid #1E8E4E; padding: 3px 8px; font-size: 9.5pt; margin-top: 4px; }
.check { border: 2px solid #1E8E4E; border-radius: 8px; padding: 6px 10px; margin-top: 12px; break-inside: avoid; } .check h3 { margin: 0 0 4px; color: #1E8E4E; font-size: 11pt; }
.check p:before { content: '☐  '; }
.sec { page-break-after: always; } .ans h2 { font-size: 14pt; } .ans h3 { font-size: 11pt; margin: 8px 0 2px; } .ans p { margin: 1px 0; font-size: 9.5pt; }
.cover { text-align: center; padding-top: 70mm; page-break-after: always; } .cover h1 { font-size: 30pt; } .cover p { color: #3B4A5E; }
"""


def md(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(str(t)))


def fig(f):
    return f"<div class='fig' data-fig='{html.escape(json.dumps(f))}'></div>"


def section(stage, unit, s, objectives):
    b = s["book"]
    goals = "".join(f"<p>• {md((objectives.get(o) or {}).get('t', ''))}</p>" for o in s.get("objs", []))
    keys = "".join(f"<p><b>{md(k)}</b> – {md(v)}</p>" for k, v in b["keys"])
    intro = "".join(fig(p["fig"]) if isinstance(p, dict) and p.get("fig") else f"<p>{md(p)}</p>" for p in b["intro"])
    ex = []
    for e in b["examples"]:
        rows = "".join(f"<tr><td>{md(r[0])}</td><td>{md(r[1]) if len(r) > 1 else ''}</td></tr>" for r in e["rows"])
        ex.append(f"<div class='we'><h3>{md(e['t'])}</h3><p class='q'>{md(e['q'])}</p><table><tr><td><i>Working</i></td><td><i>Reason</i></td></tr>{rows}</table></div>")
    qs = []
    for i, e in enumerate(b["exercise"], 1):
        parts = "".join(f"<li>{md(p['t'])}</li>" for p in e["parts"])
        body = f"{md(e['q'])}{fig(e['fig']) if e.get('fig') else ''}{'<ol>' + parts + '</ol>' if parts else ''}{'<div class=tip><b>Hint</b> ' + md(e['tip']) + '</div>' if e.get('tip') else ''}"
        if e.get("think"): body = f"<div class='think'><div class='tag'>REASON IT OUT</div>{body}</div>"
        qs.append(f"<div class='qq'><span class='n'>{i}</span><div>{body}</div></div>")
    check = "".join(f"<p>{md(c)}</p>" for c in b["check"])
    return (f"<div class='sec' data-sid='{s['id']}'><div class='band'><b>{s['id']} {md(s['title'])}</b><span>CAMDAY MATHS · STAGE {stage} · UNIT {unit}</span></div>"
            f"<div class='goal'><b>By the end of these pages you can …</b>{goals}</div>"
            f"<div class='cols'><div>{intro}</div><div class='keys'><h3>Words to know</h3>{keys}</div></div>{''.join(ex)}"
            f"<div class='ex'><h2>Practice on paper {s['id']}</h2>{''.join(qs)}</div><div class='check'><h3>Can I …?</h3>{check}</div></div>")


def answers(secs):
    out = ["<div class='ans'><h2>Answers</h2>"]
    for s in secs:
        out.append(f"<h3>Practice on paper {s['id']}</h3>")
        for i, e in enumerate(s["book"]["exercise"], 1):
            letters = "abcdefghij"
            a = "; ".join(f"({letters[k]}) {md(p['a'])}" for k, p in enumerate(e["parts"]) if p.get("a"))
            if e.get("a"): a = (a + " " if a else "") + md(e["a"])
            out.append(f"<p><b>{i}</b> {a}</p>")
    return "".join(out) + "</div>"


def page_html(body):
    scripts = "".join(f"<script src='file://{os.path.join(WEB, x)}'></script>" for x in SCRIPTS)
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}"
            f"<script>window.AtomicTheme=null;</script>{scripts}<script>document.querySelectorAll('[data-fig]').forEach(d=>{{const f=JSON.parse(d.dataset.fig);"
            f"const g=window.AtomicFig&&window.AtomicFig.get(f.kind,f);if(g)d.innerHTML=g.svg;}});</script></body></html>")


def build(stage, units):
    out_dir = os.path.join(WEB, "media", "books"); os.makedirs(out_dir, exist_ok=True)
    idx_path = os.path.join(out_dir, "index.json")
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
    files = sorted(glob.glob(os.path.join(WEB, "content", f"stage{10 + stage}-unit[0-9][0-9].json")))
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for f in files:
            d = json.load(open(f, encoding="utf-8")); n = d["unit"]["n"]
            if units and n not in units: continue
            secs = [s for s in d["sections"] if s.get("book")]
            if not secs: continue
            key = f"c{stage}u{n:02d}"; tmp = tempfile.mkdtemp(); parts = []
            title = f"Camday Maths Stage {stage} · Unit {n}: {d['unit']['title']}"
            chunks = [("cover", f"<div class='cover'><p>CAMDAY MATHS · STAGE {stage}</p><h1>Unit {n}<br>{md(d['unit']['title'])}</h1><p>Camday's own pages: read them after the lesson, then try the exercise on paper.</p></div>")]
            chunks += [(s["id"], section(stage, n, s, d["objectives"])) for s in secs] + [("answers", answers(secs))]
            for name, body in chunks:
                hp = os.path.join(tmp, f"{len(parts):02d}.html"); open(hp, "w", encoding="utf-8").write(page_html(body))
                pg.goto("file://" + hp); pg.wait_for_timeout(150)
                pp = os.path.join(tmp, f"{len(parts):02d}.pdf")
                pg.pdf(path=pp, format="A4", print_background=True, display_header_footer=True, header_template="<span></span>",
                       footer_template=f"<div style='font-size:8px;width:100%;text-align:center;color:#666'>{html.escape(title)}</div>",
                       margin={"top": "14mm", "bottom": "16mm", "left": "14mm", "right": "14mm"})
                parts.append((name, pp))
            w = PdfWriter(); pages = {}; at = 1
            for name, pp in parts:
                r = PdfReader(pp); k = len(r.pages); pages[name] = (at, at + k - 1); at += k
                for pgx in r.pages: w.add_page(pgx)
            pdf_out = os.path.join(out_dir, key + ".pdf"); w.write(pdf_out)
            img_dir = os.path.join(out_dir, key); os.makedirs(img_dir, exist_ok=True)
            for old in glob.glob(os.path.join(img_dir, "*")): os.remove(old)
            subprocess.run(["pdftoppm", "-r", "220", "-png", pdf_out, os.path.join(tmp, "pg")], check=True)
            pngs = sorted(glob.glob(os.path.join(tmp, "pg-*.png")))
            for i, png in enumerate(pngs, 1):
                im = Image.open(png).convert("RGB"); W_, H_ = im.size
                # on screen, a half-empty A4 page wastes space: cut the blank area below the content (the running footer is dropped)
                body = im.crop((0, 0, W_, int(H_ * 0.93))); gray = body.convert("L").point(lambda v: 0 if v > 245 else 255)
                box = gray.getbbox()
                if box: im = im.crop((0, 0, W_, min(H_, box[3] + int(W_ * 0.06))))
                im.save(os.path.join(img_dir, f"p{i:04d}.webp"), "WEBP", quality=90)
            idx[key] = {"title": title, "pages": len(pngs), "dir": f"media/books/{key}/", "ext": "webp", "pdf": f"media/books/{key}.pdf",
                        "secs": {k: list(v) for k, v in pages.items() if k not in ("cover",)}}
            for s in secs:
                a, b = pages[s["id"]]; bk = s.pop("book")
                s["pdf"] = [{"book": key, "p0": a, "p1": b, "label": f"pages {a}–{b}" if b > a else f"page {a}", "title": f"Camday Maths {stage} · Unit {n}",
                             "note": bk.get("note") or "", "look": bk.get("look") or []}]
            json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False)
            print(key, len(pngs), "pages", {k: v for k, v in pages.items()})
        br.close()
    json.dump(idx, open(idx_path, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    build(int(sys.argv[1]), [int(x) for x in sys.argv[2:]])
