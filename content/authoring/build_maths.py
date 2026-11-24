# -*- coding: utf-8 -*-
"""Build content/src/stage1N-unitUU.json for Mathematics Stage N (3-8) from mathN/uUU.py + private/mathN_tx.py.
Usage: python3 build_maths.py 8 [1 2 …]   (no unit numbers: every unit that exists)
Unit Tests: 2026 format, assembled by math9/mtest.py. Written by the Atomic teaching team."""
import json, os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))


def main(st, ns):
    d = os.path.join(HERE, f"math{st}")
    sys.path[:0] = [d, os.path.join(HERE, "math9"), os.path.join(HERE, "..", "private")]
    import kit; kit.STAGE = st
    import mtest
    TITLES = importlib.import_module("titles").TITLES
    TX = importlib.import_module(f"math{st}_tx")
    ns = ns or [n for n in range(1, 30) if os.path.exists(os.path.join(d, f"u{n:02d}.py"))]
    for n in ns:
        U = importlib.import_module(f"u{n:02d}").U
        assert U.stage == st, (n, U.stage)
        U.texp(*TX.EXP[n])
        for sid, f in getattr(TX, "TPL", {}).get(n, []): U.ttpl(sid, f)
        data = U.export(mtest.assemble(U), TITLES)
        json.dump(data, open(os.path.join(HERE, "..", "src", f"stage{10 + st}-unit{n:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False)
        print(st, n, len(U.tpl), [(s["id"], len(s["req"]), len(s["prac"]), len(s["adv"]), len(s["stops"])) for s in data["sections"]])


if __name__ == "__main__":
    main(int(sys.argv[1]), [int(a) for a in sys.argv[2:]])
