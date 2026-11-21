/* Atomic Education — light maths typesetting for the Mathematics courses.
   Turns plain-text fractions (3/8, 2 1/10) into stacked fractions and recurring-decimal dots (0.45̇) into proper dots,
   on any text that appears inside the main area. Answers typed by learners are never changed. */
(function () {
  const FR = /(^|[^\w./⁄])(\d+(?:\.\d+)?)\/(\d+(?:\.\d+)?)(?![\w/]|\.\d)/g;   // 3/8, 0.5/2 – not dates, units or 1/x
  const REC = /(\d)̇/g;                                                     // digit + combining dot above
  const SKIP = 'input,textarea,select,svg,script,style,.mf,.notex,.mathprev,.mathin,.chip,.tag';
  const OK = '.qp,.qctx,.qbody,.opt,.fb,.reason,.hint,.rubric,.match,.order,.grid,.tablewrap,.lblock,.lcheck,.lans,.solx';
  const needs = t => /\d\/\d/.test(t) || /̇/.test(t);
  function typesetText(node) {
    const t = node.nodeValue; if (!t || !needs(t)) return;
    const p = node.parentElement; if (!p || p.closest(SKIP) || !p.closest(OK)) return;
    const frag = document.createDocumentFragment(); let last = 0; const parts = [];
    t.replace(FR, (m, pre, n, d, off) => { parts.push({ s: off + pre.length, e: off + m.length, kind: 'f', n, d }); return m; });
    t.replace(REC, (m, d, off) => { parts.push({ s: off, e: off + m.length, kind: 'r', d }); return m; });
    if (!parts.length) return;
    parts.sort((a, b) => a.s - b.s);
    parts.forEach(x => {
      if (x.s < last) return;
      if (x.s > last) frag.append(t.slice(last, x.s));
      if (x.kind === 'f') { const f = document.createElement('span'); f.className = 'mf'; f.setAttribute('aria-label', `${x.n} over ${x.d}`);
        const a = document.createElement('span'); a.className = 'n'; a.textContent = x.n; const b = document.createElement('span'); b.className = 'd'; b.textContent = x.d; f.append(a, b); frag.append(f); }
      else { const r = document.createElement('span'); r.className = 'rd'; r.textContent = x.d; frag.append(r); }
      last = x.e;
    });
    if (last < t.length) frag.append(t.slice(last));
    node.replaceWith(frag);
  }
  function typeset(root) {
    if (!root || !(window.Core && Core.IS_MATHS)) return;
    if (root.nodeType === 3) { typesetText(root); return; }
    if (root.nodeType !== 1 || root.closest && root.closest(SKIP)) return;
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); const list = []; let n;
    while ((n = w.nextNode())) if (needs(n.nodeValue)) list.push(n);
    list.forEach(typesetText);
  }
  const obs = new MutationObserver(ms => { if (!(window.Core && Core.IS_MATHS)) return; ms.forEach(m => m.addedNodes.forEach(typeset)); });
  function start() { const m = document.body; obs.observe(m, { childList: true, subtree: true }); typeset(m); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  window.AtomicMath = { typeset };
})();
