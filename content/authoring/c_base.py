# -*- coding: utf-8 -*-
"""Helpers + unit meta for Camday Stage 7 Unit 3 (Cells)."""

def O(t, ok=False, fb=""):
    return {"t": t, "ok": ok, "fb": fb}

def q(id, type, prompt, diff, obj, skill, **kw):
    d = {"id": id, "type": type, "prompt": prompt, "diff": diff, "obj": obj, "skill": skill}
    d.update(kw)
    return d

def mcq(id, prompt, opts, diff, obj, skill="Knowledge", **kw):
    return q(id, "mcq", prompt, diff, obj, skill, options=opts, **kw)

def multi(id, prompt, opts, diff, obj, skill="Knowledge", **kw):
    return q(id, "multi", prompt, diff, obj, skill, options=opts, **kw)

def num(id, prompt, answer, unit, diff, obj, skill="Application", tol=0.0, units=None, errs=None, unitFb="", **kw):
    return q(id, "num", prompt, diff, obj, skill, answer=answer, unit=unit, tol=tol,
             units=units or [unit], errs=errs or [], unitFb=unitFb, **kw)

def label(id, prompt, fig, spots, diff, obj, skill="Figure", confuse=None, **kw):
    # spots: {anchorId: correctLabel}
    return q(id, "label", prompt, diff, obj, skill, fig=fig, spots=spots, confuse=confuse or {}, **kw)

def order(id, prompt, items, diff, obj, skill="Knowledge", **kw):
    return q(id, "order", prompt, diff, obj, skill, items=items, **kw)

def match(id, prompt, pairs, diff, obj, skill="Knowledge", **kw):
    # pairs: [(left, right)], right options shuffled in UI
    return q(id, "match", prompt, diff, obj, skill, pairs=[{"l": a, "r": b} for a, b in pairs], **kw)

def explain(id, prompt, rubric, model, diff, obj, skill="Reasoning", need=None, **kw):
    # rubric: [(point text, [keyword regex alternatives])]
    return q(id, "explain", prompt, diff, obj, skill,
             rubric=[{"pt": p, "kw": k} for p, k in rubric], model=model,
             need=need if need is not None else max(1, (len(rubric) + 1) // 2), **kw)

def grid(id, prompt, cols, rows, diff, obj, skill="Data", **kw):
    # rows: [(rowLabel, [answers per col])]; each cell chosen from cols' choices
    return q(id, "grid", prompt, diff, obj, skill, cols=cols, rows=[{"l": a, "a": b} for a, b in rows], **kw)

def table(id, prompt, head, rows, diff, obj, skill="Data", **kw):
    # rows: list of lists; a dict {"ans": x, "tol": t} marks a blank to fill
    return q(id, "table", prompt, diff, obj, skill, head=head, rows=rows, **kw)

def graph(id, prompt, x, y, pts, diff, obj, skill="Data", follow=None, **kw):
    # x/y: {label,min,max,step}; pts: [[x,y]] the student must plot; follow: an mcq about trend
    return q(id, "graph", prompt, diff, obj, skill, x=x, y=y, pts=pts, follow=follow, **kw)

def scale(id, prompt, fig, answer, unit, diff, obj, skill="Measurement", tol=0.0, units=None, errs=None, unitFb="", **kw):
    return q(id, "scale", prompt, diff, obj, skill, fig=fig, answer=answer, unit=unit, tol=tol,
             units=units or [unit], errs=errs or [], unitFb=unitFb, **kw)

def B(x):
    return {"ans": x}


OBJECTIVES = {
    "O1": {"sec": "3.1", "code": "7Bs.01", "codeNote": "", "t": "Understand that living things are made up of cells.", "vi": "Understand that living things are made up of cells."},
    "O2": {"sec": "3.1", "code": "7Bs.01", "codeNote": "", "t": "Understand that microorganisms are usually only a single cell.", "vi": "Understand that microorganisms are usually only a single cell."},
    "O3": {"sec": "3.1", "code": "7SIC.01", "codeNote": "", "t": "Describe how scientific knowledge develops over time (cell theory).", "vi": "Describe how scientific knowledge develops over time (cell theory)."},
    "O4": {"sec": "3.1", "code": "7TWSc.02, 7TWSc.04", "codeNote": "no Stage 7 statement names microscopes; choosing/using equipment (02) and accurate measurement (04)", "t": "Use a light microscope and calculate total magnification.", "vi": "Use a light microscope and calculate total magnification."},
    "O5": {"sec": "3.2", "code": "7Bs.02", "codeNote": "", "t": "Identify the parts of typical plant and animal cells and describe their functions.", "vi": "Identify the parts of plant and animal cells and describe what they do."},
    "O6": {"sec": "3.2", "code": "7Bs.04", "codeNote": "", "t": "Compare plant cells and animal cells.", "vi": "Compare plant cells and animal cells."},
    "O7": {"sec": "3.2", "code": "7TWSm.01", "codeNote": "", "t": "Evaluate a model by describing its strengths and limitations.", "vi": "Evaluate a model: its strengths and limitations."},
    "O8": {"sec": "3.3", "code": "7Bs.03", "codeNote": "", "t": "Relate the structures of specialised cells to their functions.", "vi": "Relate the structures of specialised cells to their functions."},
    "O9": {"sec": "3.4", "code": "7Bs.05", "codeNote": "", "t": "Understand how cells are grouped into tissues, organs and organ systems.", "vi": "Understand how cells are grouped into tissues, organs and organ systems."},
}

SECTIONS = [
    {"id": "3.1", "title": "Cells: the building blocks of life", "objs": ["O1", "O2", "O3", "O4"],
     "video": {"src": "media/u3_s1.mp4", "offset": 0.0, "dur": 330.456, "range": "00:00–05:30"}},
    {"id": "3.2", "title": "Inside plant and animal cells", "objs": ["O5", "O6", "O7"],
     "video": {"src": "media/u3_s2.mp4", "offset": 330.456, "dur": 148.632, "range": "05:30–07:59"}},
    {"id": "3.3", "title": "Cells with special jobs", "objs": ["O8"],
     "video": {"src": "media/u3_s3.mp4", "offset": 479.088, "dur": 87.659, "range": "07:59–09:26"}},
    {"id": "3.4", "title": "From cells to organisms", "objs": ["O9"],
     "video": {"src": "media/u3_s4.mp4", "offset": 566.747, "dur": 140.576, "range": "09:26–11:47"}},
]

# segments of the full lesson video, given as times inside each section clip (seconds)
SEGMENTS = {
    "O1": ("3.1", 30.5, 85.3, "Cells & organisms"),
    "O2": ("3.1", 52.2, 85.3, "Unicellular / multicellular"),
    "O3": ("3.1", 85.3, 171.3, "How cell theory developed"),
    "O4": ("3.1", 171.3, 330.4, "Microscope & magnification"),
    "O5": ("3.2", 0.0, 104.6, "Plant cell & animal cell parts"),
    "O6": ("3.2", 104.6, 148.6, "Plant vs animal cells"),
    "O7": ("3.2", 0.0, 6.2, "Cell diagrams are models"),
    "O8": ("3.3", 0.0, 87.6, "Specialised cells"),
    "O9": ("3.4", 0.0, 140.5, "Tissues → organs → organ systems"),
}

SOURCES = [
    {"id": "SRC1", "name": "Genetic Science Learning Center, University of Utah — 'Cell Size and Scale' (listed by NIH Office of Science Education)",
     "url": "https://science.education.nih.gov/resource-materials/11", "objs": ["O2", "O4"],
     "use": "Idea for comparing sizes of cells, bacteria and viruses (advanced 3.1)."},
    {"id": "SRC2", "name": "NIH NIGMS Biomedical Beat — 'Through the Looking Glass: Microscopic Structures in Many Sizes'",
     "url": "https://www.nigms.nih.gov/node/145536", "objs": ["O4"],
     "use": "Context: the largest things viewed through microscopes are about 1 mm; scale reasoning."},
    {"id": "SRC3", "name": "UC Museum of Paleontology (Berkeley) — Robert Hooke (1635–1703)",
     "url": "https://ucmp.berkeley.edu/history/hooke.html", "objs": ["O3"],
     "use": "Hooke saw cell walls of dead cork; in 1678 the Royal Society asked him to check Leeuwenhoek's 'little animals'."},
    {"id": "SRC4", "name": "Royal Museums Greenwich — 'The most ingenious book…': Pepys and Micrographia",
     "url": "https://rmg.co.uk/stories/blog/most-ingenious-book-ever-i-read-my-life-pepys-micrographia", "objs": ["O3", "O7"],
     "use": "Hooke used the cork 'cells' to explain why cork floats and can be squashed — an early model built from evidence."},
    {"id": "SRC5", "name": "Preproom.org (school science technicians) — Practical 'Observing Plant Cells (onion cells)'",
     "url": "https://www.preproom.org/practicals/pr.aspx?prID=1034", "objs": ["O5", "O6"],
     "use": "Onion epidermis cells are large but contain no chloroplasts — basis for an 'unexpected result' question."},
    {"id": "SRC6", "name": "University of Southern Queensland open textbook (Pressbooks) — 'Anatomy', 5.3 Erythrocytes",
     "url": "https://usq.pressbooks.pub/anatomy/chapter/5-3-erythrocytes/", "objs": ["O8"],
     "use": "Red blood cells lose their nucleus as they mature; biconcave shape gives more surface area than a sphere."},
 {"id": "SRC7", "name": "University of Hawaiʻi OER (Pressbooks) — Concepts of Biology, ch. 15 'Flatworms, Nematodes and Arthropods'",
     "url": "https://pressbooks-dev.oer.hawaii.edu/lccbiology/chapter/flatworms-nematodes-and-arthropods", "objs": ["O9"],
     "use": "Cestodes (tapeworms) have no digestive system; they absorb nutrients across the body wall but do have an excretory system."},
]
