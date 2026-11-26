#!/usr/bin/env python3
"""Reading packs (web/media/read/m{N}uUU.pdf) from the Maths lesson notes in web/content/stage1N-unitUU.json.
The PDF holds the same notes as the on-screen reader: key ideas, methods, worked examples, common mistakes, exam tips and the
check questions as "Try it". Printed with headless Chromium (Playwright). Afterwards run content/authoring/read_index.py.
Usage: python3 tools/build_read_packs.py 6 [units …]"""
import base64, glob, html, json, os, re, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
LOGO = "data:image/svg+xml;base64," + base64.b64encode(open(os.path.join(ROOT, "web", "camday_logo.svg"), "rb").read()).decode()
ICON = "data:image/svg+xml;base64," + base64.b64encode(open(os.path.join(ROOT, "web", "camday_icon.svg"), "rb").read()).decode()
KIND = {"idea": "", "method": "Method · ", "example": "Worked example · ", "mistake": "Common mistake · ", "tip": "Exam tip · ",
        "hook": "Start here · ", "recall": "Remember · ", "try": "Your turn · ", "error": "Spot the mistake · ", "summary": ""}
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
.b.hook { border-color: #5AA9F0; } .b.recall { border-color: #9AA6B8; background: #F6F7F9; } .b.try { border-color: #2FA37A; background: #F1FAF6; }
.b.error { border-color: #F08A3C; background: #FFF7EE; } .b.summary { border-color: #E0B400; background: #FFFBE6; }
dl { display: grid; grid-template-columns: max-content 1fr; gap: 1px 10px; margin: 4px 0; font-size: 10pt; } dt { font-weight: 700; } dd { margin: 0; }
.ans { font-size: 9.5pt; color: #333; border-top: 1px dotted #999; margin-top: 4px; padding-top: 3px; }
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


def steps_html(st):
    return "<ol>" + "".join(f"<li><code>{md(x[0])}</code>{(' – ' + md(x[1])) if len(x) > 1 and x[1] else ''}</li>" for x in st) + "</ol>"


def answer_text(q):
    if q.get("type") == "num": return str(q.get("answer"))
    if q.get("type") in ("mcq", "multi"): return "; ".join(o["t"] for o in q.get("options", []) if o.get("ok"))
    if q.get("type") == "table": return ", ".join(str(c["ans"]) for r in q.get("rows", []) for c in r if isinstance(c, dict))
    if q.get("type") == "short": return str((q.get("accept") or [""])[0])
    return q.get("model") or ""


def block(b):
    k = b.get("k", "idea"); out = [f'<div class="b {k}"><h3>{KIND.get(k, "")}{md(b["t"])}</h3>']
    if k == "summary": out.append("<ul>" + "".join(f"<li>{md(p)}</li>" for p in b.get("p", [])) + "</ul>")
    else: out += [f"<p>{md(p)}</p>" for p in b.get("p", [])]
    if b.get("table"):
        t = b["table"]; out.append("<table><tr>" + "".join(f"<th>{md(h)}</th>" for h in t["head"]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t["rows"]) + "</table>")
    out += [f"<p>{md(p)}</p>" for p in b.get("p2", [])]
    if b.get("q"): out.append(f'<p class="q">{"Problem" if k == "error" else "Question"}: {md(b["q"])}</p>')
    gf = [(n, b.get(f)) for n, f in (("What we know", "given"), ("What we need", "find"), ("Plan", "plan")) if b.get(f)]
    if gf: out.append("<dl>" + "".join(f"<dt>{n}</dt><dd>{md(v)}</dd>" for n, v in gf) + "</dl>")
    if b.get("steps"): out.append(steps_html(b["steps"]))
    if b.get("a"): out.append(f'<p><span class="a"><b>Answer:</b> {md(b["a"])}</span></p>')
    if b.get("check"): out.append(f'<p><b>Check:</b> {md(b["check"])}</p>')
    if k == "error" and b.get("lines"):
        out.append("<ol>" + "".join(f"<li><code>{md(l)}</code></li>" for l in b["lines"]) + "</ol><p>Which line is the first one that is wrong? Decide before you read on.</p>")
        out.append(f'<p class="ans"><b>Answer:</b> line {b["bad"] + 1}. {md(b.get("why", ""))}</p>' + (steps_html(b["fix"]) if b.get("fix") else ""))
    if b.get("qq"):
        q = b["qq"]; out.append(f'<p class="q">Try it: {md(q.get("prompt", ""))}</p><p class="ans"><b>Answer:</b> {md(answer_text(q))}. {md(q.get("reason", "") if q.get("type") != "explain" else "")}</p>')
    return "".join(out) + "</div>"


def page(d, stage):
    u = d["unit"]; secs = d["sections"]
    h = [f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='cover'><img src='{LOGO}' alt='Camday' style='height:34px;margin-bottom:14px'>",
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
            if not any(s.get("notes") in ("v3", "v4") for s in d["sections"]): continue
            pg.set_content(page(d, stage)); pg.wait_for_timeout(100)
            foot = (f"<div style='font-size:8px;width:100%;padding:0 15mm;display:flex;justify-content:space-between;color:#555;font-family:Arial'><span><img src='{ICON}' style='height:10px;vertical-align:middle'> "
                    f"<b>Camday</b> · Stage {stage} Mathematics · Unit {n} {html.escape(d['unit']['title'])}</span><span>page <span class='pageNumber'></span> of <span class='totalPages'></span></span></div>")
            out = os.path.join(ROOT, "web", "media", "read", f"m{stage}u{n:02d}.pdf")
            pg.pdf(path=out, format="A4", print_background=True, display_header_footer=True, header_template="<div></div>", footer_template=foot, margin={"top": "16mm", "bottom": "18mm", "left": "15mm", "right": "15mm"})
            print(os.path.basename(out))
        b.close()


if __name__ == "__main__":
    main(int(sys.argv[1]), [int(a) for a in sys.argv[2:]])
