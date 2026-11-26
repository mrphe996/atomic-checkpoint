"""Write supabase/migrations/20261128000200_esl_stages.sql from the built ESL units (course keys 22–29)."""
import json, glob, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
L = "(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29)"
src = open(os.path.join(ROOT, "supabase/migrations/20261128000100_young_stages.sql")).read()
old = "(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)"
head = src.split("insert into public.stage_units")[0].replace(old, L)
head = head.replace("-- Cambridge Primary Stages 1 and 2 (Camday picture courses for ages 5–7): Science course keys 1, 2; Mathematics course keys 11, 12.",
                    "-- Camday English as a Second Language, Stages 2–9: course keys 22–29.")
head = head.replace("case when p_stage >= 10 then 'You are enrolled in Stage ' || (p_stage - 10) || ' Mathematics'",
                    "case when p_stage >= 20 then 'You are enrolled in Stage ' || (p_stage - 20) || ' English (ESL)' when p_stage >= 10 then 'You are enrolled in Stage ' || (p_stage - 10) || ' Mathematics'")
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, "content/src/stage2[2-9]-unit*.json"))):
    u = json.load(open(f))["unit"]; k = u["stage"]; n = u["n"]
    rows.append(f" ({k}, 'stage{k}-unit{n:02d}', '{u['title'].replace(chr(39), chr(39) * 2)}', array['{n}.1'])")
keys = sorted({int(re.search(r'stage(\d+)-', r).group(1)) for r in rows})
out = head + "insert into public.stage_units (stage, unit, title, free_sections) values\n" + ",\n".join(rows) + "\non conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;\n\n"
out += "-- testers get the ESL courses too\ninsert into public.enrolments (learner_id, stage, method, amount)\nselect t.learner_id, s.stage, 'test', 'tester' from public.testers t cross join (values " + ", ".join(f"({k})" for k in keys) + ") s(stage)\non conflict (learner_id, stage) do nothing;\n"
open(os.path.join(ROOT, "supabase/migrations/20261128000200_esl_stages.sql"), "w").write(out); print(len(rows), "units", keys)
