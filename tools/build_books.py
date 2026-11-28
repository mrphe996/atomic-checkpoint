#!/usr/bin/env python3
"""Camday book pages – the 'Read the PDF' step of a Maths lesson.
For each unit whose sections carry a `book` (maths_notes_v4 BK(...)), prints Camday's own textbook-style pages
(key words, explanation, worked examples, exercise, 'Think like a mathematician', checklist; answers at the back),
then turns every page into an image for the on-site viewer:
  web/media/books/c{stage}u{NN}/p0001.webp …   web/media/books/c{stage}u{NN}.pdf   web/media/books/index.json
and writes each section's `pdf` reference (book, p0, p1, label, note, look) into web/content/stage1N-unitNN.json.
Run after tools/apply_notes_v3.py. Usage: python3 tools/build_books.py 7 [units …]
Science: python3 tools/build_books.py s7 [units …] takes each lesson's Read blocks and pages from content/authoring/science_read/s7_uNN.py
(READ[sid] = L(blocks…, book=BK(…))), writes them as the section's `read` and `pdf`, books s{stage}u{NN}."""
import glob, html, json, os, re, subprocess, sys, tempfile
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
WEB = os.path.join(ROOT, "web")
SCRIPTS = ["figures.js", "figures2.js", "figures3.js", "figures4.js", "figures5.js"]
import base64
LOGO = "data:image/svg+xml;base64," + base64.b64encode(open(os.path.join(WEB, "camday_logo.svg"), "rb").read()).decode()
ICON = "data:image/svg+xml;base64," + base64.b64encode(open(os.path.join(WEB, "camday_icon.svg"), "rb").read()).decode()
KIND = {"hook": "Start here", "recall": "Remember", "idea": "Key idea", "method": "Method", "example": "Worked example", "try": "Try it",
        "error": "Spot the mistake", "mistake": "Common mistake", "tip": "Exam tip", "summary": "Key points"}
CSS = """
@page { size: A4; margin: 12mm 11mm 18mm; }
body { font-family: 'Lexend', 'Inter', Arial, sans-serif; color: #1B1B1B; font-size: 12.5pt; line-height: 1.5; margin: 0; }
.top { display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid #222; padding-bottom: 6px; }
.top img { height: 26px; } .top span { font-size: 9pt; letter-spacing: .06em; font-weight: 700; color: #444; text-transform: uppercase; }
.title { margin: 12px 0 8px; } .title .chip { display: inline-block; background: #FFE555; font-weight: 800; padding: 2px 10px; border-radius: 6px; font-size: 11pt; }
.title h1 { font-size: 24pt; margin: 6px 0 0; line-height: 1.15; }
.goal { background: #F4F4F4; border-left: 5px solid #222; padding: 6px 12px; font-size: 10.5pt; margin: 8px 0 10px; } .goal p { margin: 2px 0; }
.keys { border: 2px solid #222; border-radius: 10px; padding: 6px 12px; font-size: 10pt; margin: 8px 0 12px; columns: 2; column-gap: 18px; }
.keys h3 { column-span: all; margin: 0 0 4px; font-size: 11pt; } .keys p { margin: 2px 0; break-inside: avoid; } .keys b { background: linear-gradient(transparent 60%, #FFE555 60%); }
.blk { border: 1.5px solid #D8D8D8; border-radius: 10px; margin: 10px 0; break-inside: avoid; overflow: hidden; }
.blk .k { font-size: 8.5pt; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; padding: 4px 12px; background: #F2F2F2; }
.blk .in { padding: 6px 12px 8px; } .blk h3 { margin: 2px 0 4px; font-size: 13pt; } .blk p { margin: 4px 0; }
.k-hook .k { background: #DDEEFF; } .k-example .k { background: #FFF1B8; } .k-method .k { background: #F1E6F7; } .k-try .k, .k-error .k { background: #DFF4EA; }
.k-mistake .k { background: #FDE2E2; } .k-tip .k { background: #E4F6E4; } .k-summary .k { background: #FFE555; } .k-summary { border-color: #222; }
table { border-collapse: collapse; margin: 6px 0; font-size: 10pt; } td, th { border: 1px solid #BDBDBD; padding: 3px 8px; text-align: left; } th { background: #F2F2F2; }
.steps { width: 100%; } .steps td { border: 0; border-top: 1px dotted #D8C77A; vertical-align: top; } .steps td:first-child { font-weight: 700; width: 50%; } .steps td:last-child { color: #555; }
dl { display: grid; grid-template-columns: max-content 1fr; gap: 1px 10px; margin: 4px 0; font-size: 10pt; } dt { font-weight: 700; } dd { margin: 0; }
.ans { background: #EEF8EE; border-radius: 6px; padding: 3px 8px; display: inline-block; font-weight: 600; } .chk { color: #1E6B35; font-size: 10pt; }
.lines { counter-reset: ln; padding: 0; list-style: none; } .lines li { counter-increment: ln; padding: 2px 0; } .lines li:before { content: 'Line ' counter(ln) '   '; font-weight: 700; color: #8A5A2B; }
.fig { margin: 6px 0; text-align: center; } .fig svg { width: 80%; max-height: 60mm; }
ul.sum { margin: 2px 0 2px 18px; padding: 0; }
.ex h2 { break-after: avoid; font-size: 15pt; border-bottom: 3px solid #222; margin: 16px 0 6px; padding-bottom: 2px; }
.qq { break-inside: avoid; margin: 8px 0; display: grid; grid-template-columns: 22px 1fr; gap: 4px; } .qq .n { font-weight: 800; }
.qq ol { list-style: lower-alpha; margin: 3px 0 0 16px; padding: 0; } .qq li { margin: 2px 0; }
.think { border: 2px dashed #222; border-radius: 8px; padding: 6px 8px; } .think .tag { font-weight: 800; font-size: 8.5pt; letter-spacing: .06em; background: #FFE555; padding: 1px 6px; border-radius: 4px; }
.tip { background: #F4F4F4; border-left: 4px solid #222; padding: 3px 8px; font-size: 9.5pt; margin-top: 4px; }
.check { border: 2px solid #222; border-radius: 10px; padding: 6px 12px; margin-top: 12px; break-inside: avoid; } .check h3 { margin: 0 0 4px; font-size: 12pt; } .check p:before { content: '☐  '; }
.anshead h2 { font-size: 15pt; } .anshead h3 { font-size: 11pt; margin: 10px 0 2px; } .anshead p { margin: 1px 0; font-size: 9.5pt; }
.cover { text-align: center; padding-top: 55mm; } .cover img { height: 46px; } .cover h1 { font-size: 30pt; margin: 18mm 0 4mm; } .cover .st { font-size: 12pt; letter-spacing: .1em; font-weight: 700; }
.cover ol { text-align: left; display: inline-block; font-size: 12pt; margin-top: 10mm; } .cover .bar { height: 10px; background: #FFE555; margin: 14mm 30mm 0; border-radius: 6px; }
"""


def md(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(str(t)))


def fig(f):
    return f"<div class='fig' data-fig='{html.escape(json.dumps(f))}'></div>"


def table(t):
    return "<table><tr>" + "".join(f"<th>{md(h)}</th>" for h in t["head"]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t["rows"]) + "</table>"


def qtext(q):
    if q.get("type") == "table":
        rows = [[("☐" if isinstance(c, dict) else c) for c in r] for r in q["rows"]]
        return md(q["prompt"]) + table({"head": q["head"], "rows": rows})
    if q.get("type") in ("mcq", "multi"):
        return md(q["prompt"]) + "<span style='display:block;margin:4px 0 0 10px;line-height:2.1'>" + "<br>".join(f"<b>{'ABCDEF'[i]}</b>  {md(o['t'])}" for i, o in enumerate(q["options"])) + "</span>"
    if q.get("type") == "grid":
        return md(q["prompt"]) + f" ({', '.join(md(c) for c in q['cols'])})<ol>" + "".join(f"<li>{md(r['l'])}</li>" for r in q["rows"]) + "</ol>"
    return md(q.get("prompt", ""))


def qanswer(q):
    t = q.get("type")
    if t == "num": return str(q.get("answer")).replace("-", "−")
    if t in ("mcq", "multi"): return "; ".join(o["t"] for o in q["options"] if o.get("ok"))
    if t == "table": return ", ".join(str(c["ans"]).replace("-", "−") for r in q["rows"] for c in r if isinstance(c, dict))
    if t == "short": return str((q.get("accept") or [""])[0])
    if t == "expr": return q.get("show") or q.get("expr", "")
    return q.get("model") or q.get("reason") or ""


def block(b, tries):
    k = b.get("k", "idea"); h = [f"<div class='blk k-{k}'><div class='k'>{KIND.get(k, 'Key idea')}</div><div class='in'><h3>{md(b['t'])}</h3>"]
    if k == "summary": h.append("<ul class='sum'>" + "".join(f"<li>{md(p)}</li>" for p in b.get("p", [])) + "</ul>")
    else: h += [f"<p>{md(p)}</p>" for p in b.get("p", [])]
    if b.get("fig"): h.append(fig(b["fig"]))
    if b.get("table"): h.append(table(b["table"]))
    h += [f"<p>{md(p)}</p>" for p in b.get("p2", [])]
    if b.get("q"): h.append(f"<p><b>{'Problem' if k == 'error' else 'Question'}:</b> {md(b['q'])}</p>")
    gf = [(n, b.get(f)) for n, f in (("What we know", "given"), ("What we need", "find"), ("Plan", "plan")) if b.get(f)]
    if gf: h.append("<dl>" + "".join(f"<dt>{n}</dt><dd>{md(v)}</dd>" for n, v in gf) + "</dl>")
    if b.get("steps"): h.append("<table class='steps'>" + "".join(f"<tr><td>{md(x[0])}</td><td>{md(x[1]) if len(x) > 1 else ''}</td></tr>" for x in b["steps"]) + "</table>")
    if b.get("a"): h.append(f"<p><span class='ans'>Answer: {md(b['a'])}</span></p>")
    if b.get("check"): h.append(f"<p class='chk'><b>Check:</b> {md(b['check'])}</p>")
    if k == "error" and b.get("lines"):
        tries.append(("Spot the mistake: " + b["t"], f"Line {b['bad'] + 1} is the first wrong line. {b.get('why', '')} " + " ".join(f[0] for f in b.get("fix", []))))
        h.append("<ol class='lines'>" + "".join(f"<li>{md(l)}</li>" for l in b["lines"]) + "</ol><p><i>Which line is the first one that is wrong? Decide, then check the answers at the back.</i></p>")
    if b.get("qq"):
        tries.append((b["t"], qanswer(b["qq"]) + (". " + b["qq"]["reason"] if b["qq"].get("reason") and b["qq"].get("type") != "explain" else "")))
        h.append(f"<p><b>Try it ({len(tries)}):</b> {qtext(b['qq'])}</p>")
    return "".join(h) + "</div></div>"


def head(stage, unit_title, unit, s):
    return (f"<div class='top'><img src='{LOGO}' alt='Camday'><span>Stage {stage} {SUBJ} · Unit {unit} {md(unit_title)}</span></div>"
            f"<div class='title'><span class='chip'>Lesson {s['id']}</span><h1>{md(s['title'])}</h1></div>")


def section(stage, unit, s, d):
    b = s["book"]; tries = []
    goals = "".join(f"<p>• {md((d['objectives'].get(o) or {}).get('t', ''))}</p>" for o in s.get("objs", []))
    keys = "".join(f"<p><b>{md(k)}</b> – {md(v)}</p>" for k, v in b["keys"])
    body = "".join(block(x, tries) for x in s.get("lesson") or s.get("read") or [])
    qs = []
    for i, e in enumerate(b["exercise"], 1):
        parts = "".join(f"<li>{md(p['t'])}</li>" for p in e["parts"])
        q = f"{md(e['q'])}{fig(e['fig']) if e.get('fig') else ''}{'<ol>' + parts + '</ol>' if parts else ''}{'<div class=tip><b>Hint</b> ' + md(e['tip']) + '</div>' if e.get('tip') else ''}"
        if e.get("think"): q = f"<div class='think'><span class='tag'>REASON IT OUT</span><br>{q}</div>"
        qs.append(f"<div class='qq'><span class='n'>{i}</span><div>{q}</div></div>")
    check = "".join(f"<p>{md(c)}</p>" for c in b["check"])
    s["_tries"] = tries
    return (f"<div class='sec'>{head(stage, d['unit']['title'], unit, s)}<div class='goal'><b>In this lesson you will learn to</b>{goals}</div>"
            f"<div class='keys'><h3>Words to know</h3>{keys}</div>{body}"
            f"<div class='ex'><h2>Practice on paper · Lesson {s['id']}</h2>{''.join(qs)}</div><div class='check'><h3>Can I …?</h3>{check}</div></div>")


def answers(stage, d, secs):
    out = [f"<div class='top'><img src='{LOGO}' alt='Camday'><span>Stage {stage} {SUBJ} · Unit {d['unit']['n']} {md(d['unit']['title'])}</span></div><div class='anshead'><h2>Answers</h2>"]
    letters = "abcdefghij"
    for s in secs:
        out.append(f"<h3>Lesson {s['id']} {md(s['title'])} – Try it</h3>")
        out += [f"<p><b>{i}</b> {md(t)}: {md(a)}</p>" for i, (t, a) in enumerate(s.get("_tries", []), 1)]
        out.append(f"<h3>Lesson {s['id']} – Practice on paper</h3>")
        for i, e in enumerate(s["book"]["exercise"], 1):
            a = "; ".join(f"({letters[k]}) {md(p['a'])}" for k, p in enumerate(e["parts"]) if p.get("a"))
            if e.get("a"): a = (a + " " if a else "") + md(e["a"])
            out.append(f"<p><b>{i}</b> {a}</p>")
    return "".join(out) + "</div>"


def page_html(body):
    scripts = "".join(f"<script src='file://{os.path.join(WEB, x)}'></script>" for x in SCRIPTS)
    kx = os.path.join(WEB, "vendor/katex")
    # maths is typeset exactly as in the app (KaTeX via mathtype.js): fractions, powers, equations
    return (f"<!DOCTYPE html><html><head><meta charset='utf-8'><link rel='stylesheet' href='file://{kx}/katex.min.css'><style>{CSS}"
            f" .lblock .katex{{font-size:1.08em}} .lblock .katex .mfrac{{font-size:1.06em}}</style></head><body><div class='lblock'>{body}</div>"
            f"<script>window.AtomicTheme=null;window.Core={{IS_MATHS:true}};</script>{scripts}<script src='file://{kx}/katex.min.js'></script>"
            f"<script src='file://{os.path.join(WEB, 'mathtype.js')}'></script>"
            f"<script>document.querySelectorAll('[data-fig]').forEach(d=>{{const f=JSON.parse(d.dataset.fig);"
            f"const g=window.AtomicFig&&window.AtomicFig.get(f.kind,f);if(g)d.innerHTML=g.svg;}});"
            f"{'try{AtomicMath.typeset(document.body)}catch(e){}' if SUBJ == 'Mathematics' else ''}</script></body></html>")


SUBJ = "Mathematics"


def build(stage, units, sci=False):
    global SUBJ
    SUBJ = "Science" if sci else "Mathematics"
    out_dir = os.path.join(WEB, "media", "books"); os.makedirs(out_dir, exist_ok=True)
    idx_path = os.path.join(out_dir, "index.json")
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
    files = sorted(glob.glob(os.path.join(WEB, "content", f"stage{stage if sci else 10 + stage}-unit[0-9][0-9].json")))
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for f in files:
            d = json.load(open(f, encoding="utf-8")); n = d["unit"]["n"]
            if units and n not in units: continue
            if sci:
                rd = os.path.join(ROOT, "content", "authoring", "science_read", f"s{stage}_u{n:02d}.py")
                if not os.path.exists(rd): continue
                sys.path.insert(0, os.path.join(ROOT, "content", "authoring")); import importlib
                READ = importlib.import_module(f"science_read.s{stage}_u{n:02d}").READ
                for s in d["sections"]:
                    if s["id"] in READ: s["read"] = READ[s["id"]]["blocks"]; s["book"] = READ[s["id"]]["book"]
            secs = [s for s in d["sections"] if s.get("book")]
            if not secs: continue
            key = f"{'s' if sci else 'c'}{stage}u{n:02d}"; tmp = tempfile.mkdtemp(); parts = []
            title = f"Camday {'Science' if sci else 'Maths'} Stage {stage} · Unit {n}: {d['unit']['title']}"
            cover = (f"<div class='cover'><img src='{LOGO}' alt='Camday'><p class='st'>STAGE {stage} {SUBJ.upper()}</p><h1>Unit {n}<br>{md(d['unit']['title'])}</h1>"
                     f"<p>Lesson notes and practice on paper</p><ol>" + "".join(f"<li>Lesson {s['id']} · {md(s['title'])}</li>" for s in secs) + "</ol><div class='bar'></div></div>")
            chunks = [("cover", cover, title)] + [(s["id"], section(stage, n, s, d), f"Lesson {s['id']} · {s['title']}") for s in secs]
            chunks.append(("answers", answers(stage, d, secs), "Answers"))
            for name, body, label in chunks:
                hp = os.path.join(tmp, f"{len(parts):02d}.html"); open(hp, "w", encoding="utf-8").write(page_html(body))
                pg.goto("file://" + hp); pg.wait_for_timeout(350)
                pp = os.path.join(tmp, f"{len(parts):02d}.pdf")
                pg.pdf(path=pp, format="A4", print_background=True, display_header_footer=True, header_template="<span></span>",
                       footer_template=(f"<div style='font-size:8px;width:100%;padding:0 10mm;display:flex;justify-content:space-between;align-items:center;color:#555;font-family:Arial'>"
                                        f"<span><img src='{ICON}' style='height:10px;vertical-align:middle'> <b>Camday</b> · Stage {stage} {SUBJ} · {html.escape(label)}</span>"
                                        f"<span>page <span class='pageNumber'></span></span></div>"),
                       margin={"top": "12mm", "bottom": "16mm", "left": "10mm", "right": "10mm"})
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
                # on screen, a half-empty A4 page wastes space: cut the blank area between the content and the footer
                body = im.crop((0, 0, W_, int(H_ * 0.92))); gray = body.convert("L").point(lambda v: 0 if v > 245 else 255)
                box = gray.getbbox()
                if box and box[3] < int(H_ * 0.85):   # keep the branded footer: content + a small gap + footer strip
                    foot = im.crop((0, int(H_ * 0.92), W_, H_)); top = im.crop((0, 0, W_, box[3] + int(W_ * 0.04)))
                    im = Image.new("RGB", (W_, top.size[1] + foot.size[1]), "white"); im.paste(top, (0, 0)); im.paste(foot, (0, top.size[1]))
                # on screen the A4 side margins only make the text smaller: keep a thin margin round the content
                g2 = im.convert("L").point(lambda v: 0 if v > 245 else 255).getbbox()
                if g2:
                    pad = int(im.size[0] * 0.025); im = im.crop((max(0, g2[0] - pad), 0, min(im.size[0], g2[2] + pad), im.size[1]))
                im.save(os.path.join(img_dir, f"p{i:04d}.webp"), "WEBP", quality=90)
            import hashlib
            ver = hashlib.sha1(open(pdf_out, "rb").read()).hexdigest()[:10]
            idx[key] = {"title": title, "pages": len(pngs), "dir": f"media/books/{key}/", "ext": "webp", "pdf": f"media/books/{key}.pdf?v={ver}", "v": ver,
                        "secs": {k: list(v) for k, v in pages.items() if k not in ("cover",)}}
            for s in secs:
                a, b = pages[s["id"]]; bk = s.pop("book")
                s.pop("_tries", None)
                s["pdf"] = [{"book": key, "p0": a, "p1": b, "label": f"pages {a}–{b}" if b > a else f"page {a}", "title": f"Lesson {s['id']} notes · {s['title']}",
                             "note": bk.get("note") or "", "look": bk.get("look") or []}]
            json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False)
            print(key, len(pngs), "pages", {k: v for k, v in pages.items()})
        br.close()
    json.dump(idx, open(idx_path, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    a = sys.argv[1]
    build(int(a.lstrip("s")), [int(x) for x in sys.argv[2:]], sci=a.startswith("s"))
