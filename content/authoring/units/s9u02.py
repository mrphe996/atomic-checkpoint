# -*- coding: utf-8 -*-
"""Stage 9 Unit 2 – Excretion. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Biology"
BLURB = "Why the body must excrete waste, what urine contains, the parts of the excretory system and how the kidneys filter blood."
OBJECTIVES = {
    "O1": {"sec": "2.1", "code": "9Bs.02", "codeNote": "excretion", "t": "Explain what excretion is and name the lungs, skin and kidneys as excretory organs."},
    "O2": {"sec": "2.1", "code": "9Bs.02, 9TWSa.01", "codeNote": "urine", "t": "Describe what urine contains and how it changes with water intake."},
    "O3": {"sec": "2.1", "code": "9Bs.02", "codeNote": "", "t": "Identify the kidneys, ureters, bladder and urethra and describe the path of urine."},
    "O4": {"sec": "2.1", "code": "9Bs.02, 9SIC.03", "codeNote": "kidneys", "t": "Describe how the kidneys filter blood, and how dialysis and transplants help when kidneys fail."},
}
SECTIONS = [
    {"id": "2.1", "title": "How does the human excretory system work?", "objs": ["O1", "O2", "O3", "O4"]},
]
u = Unit(9, 2)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

u.sec("2.1", "O1")
u.gd("r", "Which organ excretes each waste?", "Organ", [("Carbon dioxide and water vapour, when breathing out", "Lungs"), ("Water, salts and a little urea in sweat", "Skin"), ("Excess water, salts and urea in urine", "Kidneys")])
u.tb("r", "The approximate make-up of urine. Complete the table.", ["Substance", "Percentage (%)"], [["Water", "95"], ["Urea", "2"], ["Salts and uric acid", B(3)]], o="O2")
u.od("r", "Order the path of urine.", ["Kidney", "Ureter", "Bladder", "Urethra"], o="O3")
u.ex("r", "Explain why urine is darker yellow when a person is dehydrated.", [("body conserves / saves water", ["conserv|save|keep"]), ("less water in urine", ["less water|less urine|concentrat"]), ("same waste in less water – darker", ["darker|concentrat|same waste"])],
     "When dehydrated, the body conserves water, so the kidneys make less urine. The waste is dissolved in less water, so the urine is more concentrated and darker.", o="O2")
u.mc("r", "Excretion is…", "removing waste products made by the body's chemical reactions", [("removing undigested food", "That is egestion."), ("taking in food", "No."), ("breathing in oxygen", "No.")])
u.mc("r", "Urea is made when the body breaks down…", "proteins", ["fats", "starch", "water"], o="O2")
u.mc("r", "Blood enters the kidney through the…", "renal artery", ["renal vein", "ureter", "urethra"], o="O4", d="H")
u.mc("r", "Why might a patient whose kidneys have failed need dialysis?", "A machine must remove urea and excess water from their blood", ["To add urea to the blood", "To pump blood round the body", "To digest proteins"], o="O4", d="VH")
mcs("p", [
    ("'To excrete' means to…", "get rid of", ["take in", "digest", "store"]),
    ("Metabolism is…", "all the chemical reactions in the body", ["breathing only", "eating food", "growing hair"]),
    ("Excretion stops … from building up.", "toxic substances", ["oxygen", "vitamins", "useful nutrients"]),
    ("The body is about … water.", "60%", ["10%", "95%", "30%"]),
    ("We can survive only about … without water.", "three days", ["three weeks", "three months", "three hours"]),
    ("Sweat is produced by the…", "skin", ["kidneys", "bladder", "lungs"]),
    ("Eating more protein than we need increases…", "the urea we excrete", ["the oxygen we breathe out", "our height", "the water in blood"], "O2"),
    ("Urine is about … water.", "95%", ["50%", "5%", "60%"], "O2"),
    ("Drinking lots of water makes urine…", "paler", ["darker", "thicker", "red"], "O2"),
    ("The kidneys are in the…", "lower back", ["chest", "head", "feet"], "O3"),
    ("Urine is stored in the…", "bladder", ["kidney", "ureter", "renal vein"], "O3"),
    ("Urine leaves the body through the…", "urethra", ["ureter", "renal artery", "bladder wall"], "O3"),
    ("Clean blood leaves the kidney through the…", "renal vein", ["renal artery", "urethra", "ureter"], "O4"),
    ("Healthy kidneys filter about … of fluid a day.", "180 litres", ["1.8 litres", "18 000 litres", "18 millilitres"], "O4"),
    ("A person can live healthily with…", "one kidney", ["no kidneys and no treatment", "no bladder or kidneys", "only a ureter"], "O4"),
])
u.ms("p", "Select ALL the substances removed by the kidneys.", ["Urea", "Excess water", "Excess salts"], ["Glucose the body needs", "Red blood cells"], o="O4")
u.mt("p", "Match the part to its job.", [("Ureter", "carries urine to the bladder"), ("Bladder", "stores urine"), ("Urethra", "carries urine out of the body")], o="O3")
u.gd("p", "Excretion or not?", "Answer", [("Breathing out carbon dioxide", "Excretion"), ("Sweating out salts", "Excretion"), ("Passing undigested food", "Not excretion")])
u.ex("a", "Wetlands are sometimes called 'the kidneys of the landscape'. Explain this comparison.", [("wetlands filter water", ["filter|clean"]), ("kidneys filter blood", ["kidney.*blood|blood"]), ("both remove waste / harmful substances", ["remov|waste|harmful"])],
     "Wetlands filter water and remove harmful substances, just as kidneys filter the blood and remove waste such as urea.")
u.nm("a", "A person makes 1.5 litres of urine a day. About 2% of it is urea. What volume is urea, in millilitres? (1 litre = 1000 ml)", 30, "ml", o="O2")
u.mc("a", "Why is a kidney transplant often better long-term than dialysis?", "The new kidney filters blood all the time, without hours on a machine", ["Dialysis adds urea", "Transplants need no matching", "Dialysis removes all water"], o="O4", skill="Reasoning")
u.mc("a", "On a hot day an athlete sweats a lot. What happens to their urine?", "Less urine is made and it is darker", ["More urine is made and it is paler", "Urine stops containing urea", "Urine becomes 100% water"], o="O2", skill="Reasoning")
u.stop("It stops toxic substances from building up", "Excretion removes waste made by…", "metabolism", ["digestion of fibre", "breathing in", "drinking"])
u.stop("in urine", "Which organ removes carbon dioxide?", "The lungs", ["The kidneys", "The bladder", "The skin"])
u.stop("These figures are only approximate", "Urine is mostly…", "water", ["urea", "salts", "protein"], o="O2")
u.stop("leaves through the urethra", "Urine is stored in the…", "bladder", ["ureter", "kidney", "urethra"], o="O3")
u.stop("leaves through the renal vein", "The kidneys filter…", "blood", ["air", "food", "sweat"], o="O4")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Excretion", "sec": None, "kids": [
    {"id": "ex", "t": "Excretion", "d": "Removes waste of metabolism • Stops toxins building up", "obj": "O1", "sec": "2.1"},
    {"id": "or", "t": "Organs", "d": "Lungs: carbon dioxide • Skin: sweat • Kidneys: urine", "obj": "O1", "sec": "2.1"},
    {"id": "ur", "t": "Urine", "d": "95% water • Urea from proteins • Darker when dehydrated", "obj": "O2", "sec": "2.1"},
    {"id": "sy", "t": "System", "d": "Kidneys → ureters → bladder → urethra", "obj": "O3", "sec": "2.1"},
    {"id": "kd", "t": "Kidneys", "d": "Renal artery in • Filter blood • Renal vein out • Dialysis and transplants", "obj": "O4", "sec": "2.1"},
]}
