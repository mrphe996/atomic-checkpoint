#!/usr/bin/env python3
"""Reading packs (web/media/read/m{N}uUU.pdf) from the Maths lesson notes in web/content/stage1N-unitUU.json.
The PDF holds the same notes as the on-screen reader: key ideas, methods, worked examples, common mistakes, exam tips and the
check questions as "Try it". Printed with headless Chromium (Playwright). Afterwards run content/authoring/read_index.py.
Usage: python3 tools/build_read_packs.py 6 [units …]"""
import glob, html, json, os, re, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KIND = {"idea": "", "method": "Method · ", "example": "Worked example · ", "mistake": "Common mistake · ", "tip": "Exam tip · "}
CSS = """
@page { size: A4; margin: 16mm 15mm 18mm; }
body { font-family: 'Lexend', 'Inter', Arial, sans-serif; color: #111; font-size: 11pt; line-height: 1.45; }
.cover { page-break-after: always; }
.eyebrow { font-size: 9pt; letter-spacing: .08em; font-weight: 700; color: #333; }
h1 { font-size: 26pt; margin: 6px 0 8px; } h2 { font-size: 16pt; margin: 0 0 8px; padding-top: 4px; border-bottom: 3px solid #111; }
.sec { page-break-before: always; } .sec:first-of-type { page-break-before: auto; }
.b { border-left: 5px solid #3B6FD8; background: #F6F8FD; padding: 8px 12px; margin: 10px 0; break-inside: avoid; border-radius: 4px; }
.b.method { border-color: #7A4BD1; background: #F8F3FC; } .b.example { border-color: #E3B505; background: #FFFBEA; }
.b.mistake { border-color: #E14E4E; background: #FFF4F4; } .b.tip { border-color: #1E8E4E; background: #F0FAF3; }
.b h3 { margin: 0 0 4px; font-size: 11.5pt; } .b p { margin: 3px 0; }
table { border-collapse: collapse; margin: 6px 0; font-size: 9.5pt; } td, th { border: 1px solid #bbb; padding: 3px 7px; text-align: left; } th { background: #eee; }
ol { margin: 4px 0 4px 18px; padding: 0; } code { font-family: inherit; font-weight: 600; }
.q { font-weight: 600; } .a { background: #E9F7EC; padding: 3px 8px; border-radius: 3px; display: inline-block; }
.try { border: 2px dashed #111; padding: 6px 10px; margin: 10px 0; break-inside: avoid; } .try b { letter-spacing: .06em; }
ul { margin: 4px 0 8px 18px; padding: 0; }
"""


def md(t):
    t = html.escape(str(t))
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)


def block(b):
    k = b.get("k", "idea"); out = [f'<div class="b {k}"><h3>{KIND.get(k, "")}{md(b["t"])}</h3>']
    out += [f"<p>{md(p)}</p>" for p in b.get("p", [])]
    if b.get("table"):
        t = b["table"]; out.append("<table><tr>" + "".join(f"<th>{md(h)}</th>" for h in t["head"]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t["rows"]) + "</table>")
    if b.get("q"): out.append(f'<p class="q">Question: {md(b["q"])}</p>')
    if b.get("steps"): out.append("<ol>" + "".join(f"<li><code>{md(w)}</code>{(' – ' + md(y)) if y else ''}</li>" for w, y in b["steps"]) + "</ol>")
    if b.get("a"): out.append(f'<p><span class="a"><b>Answer:</b> {md(b["a"])}</span></p>')
    return "".join(out) + "</div>"


def page(d, stage):
    u = d["unit"]; secs = d["sections"]
    h = [f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='cover'>",
         f"<p class='eyebrow'>STAGE {stage} MATHEMATICS · UNIT {u['n']} · READ BEFORE THE LESSON</p><h1>{md(u['title'])}</h1>",
         f"<p>{md(u.get('blurb', ''))}</p><h2>What you will learn</h2><ul>"]
    seen = []
    for s in secs:
        for o in s["objs"]:
            t = (d["objectives"].get(o) or {}).get("t")
            if t and t not in seen: seen.append(t); h.append(f"<li>{md(t)}</li>")
    h.append("</ul><h2>Sections</h2><ol>" + "".join(f"<li>{s['id']} {md(s['title'])}</li>" for s in secs) + "</ol>")
    h.append("<p>How to use this pack: read each section, try the <b>Try it</b> questions without looking back, then check your answers in the lesson on Camday.</p></div>")
    for s in secs:
        h.append(f"<div class='sec'><h2>{s['id']} {md(s['title'])}</h2>")
        for x in s.get("stops") or []:
            if x.get("after") == -1: h.append(f"<div class='try'><b>TRY IT</b><br>{md(x['q'].get('prompt', ''))}</div>")
        for i, b in enumerate(s.get("lesson") or []):
            h.append(block(b))
            for x in s.get("stops") or []:
                if x.get("after") == i: h.append(f"<div class='try'><b>TRY IT</b><br>{md(x['q'].get('prompt', ''))}</div>")
        h.append("</div>")
    return "".join(h) + "</body></html>"


def main(stage, units):
    files = sorted(glob.glob(os.path.join(ROOT, "web", "content", f"stage{10 + stage}-unit[0-9][0-9].json")))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for f in files:
            d = json.load(open(f, encoding="utf-8")); n = d["unit"]["n"]
            if units and n not in units: continue
            if not any(s.get("notes") == "v3" for s in d["sections"]): continue
            pg.set_content(page(d, stage)); pg.wait_for_timeout(100)
            foot = f"<div style='font-size:8px;width:100%;text-align:center;color:#555'>Camday · Stage {stage} Mathematics Unit {n} · page <span class='pageNumber'></span> of <span class='totalPages'></span></div>"
            out = os.path.join(ROOT, "web", "media", "read", f"m{stage}u{n:02d}.pdf")
            pg.pdf(path=out, format="A4", print_background=True, display_header_footer=True, header_template="<div></div>", footer_template=foot, margin={"top": "16mm", "bottom": "18mm", "left": "15mm", "right": "15mm"})
            print(os.path.basename(out))
        b.close()


if __name__ == "__main__":
    main(int(sys.argv[1]), [int(a) for a in sys.argv[2:]])
