/* Camday design sample v4 — secure print-only worksheet viewer (demo data, no backend). */
(function () {
  'use strict';
  var DOC = { id: 'S7-U03-W32', unit: 'Unit 3 · Cells', sec: '3.2 Inside plant and animal cells', mins: 25, marks: 16, pages: 3 };
  var LEARNER = { id: 'L-7F3K-29', email: 'an.nguyen@example.com' };
  var serial = 118;

  // ---------- helpers ----------
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fnv(s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  var B32 = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';
  function code(s) { var a = fnv(s), b = fnv(s + '#'), o = ''; for (var i = 0; i < 8; i++) { var v = i < 4 ? a : b; o += B32[(v >>> (i % 4 * 7)) % B32.length]; } return 'AE-' + o.slice(0, 4) + '-' + o.slice(4); }
  function stamp(d) { var p = function (n) { return (n < 10 ? '0' : '') + n; }; return p(d.getDate()) + '/' + p(d.getMonth() + 1) + '/' + d.getFullYear() + ' ' + p(d.getHours()) + ':' + p(d.getMinutes()); }

  // ---------- security graphics ----------
  function micro(cls) { return '<div class="micro ' + cls + '">' + new Array(70).join('ATOMICEDUCATION·VERIFIED·') + '</div>'; }

  function watermark(info, big) {
    var line = esc(info.name + '  ·  ' + LEARNER.id + '  ·  ' + info.when + '  ·  Copy #' + info.serial);
    return '<div class="wm"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 297" preserveAspectRatio="none"><defs>' +
      '<pattern id="wp' + info.k + '" width="105" height="44" patternUnits="userSpaceOnUse" patternTransform="rotate(-32)">' +
      '<text x="0" y="12" font-family="Figtree,Arial" font-size="3.4" font-weight="700" fill="#0149AF" fill-opacity=".11">' + line + '</text>' +
      '<text x="52" y="34" font-family="Figtree,Arial" font-size="3.4" font-weight="700" fill="#0149AF" fill-opacity=".11">' + line + '</text></pattern></defs>' +
      '<rect width="210" height="297" fill="url(#wp' + info.k + ')"/>' +
      // faint "CAMDAY" on every page, cover included
      '<text x="105" y="160" text-anchor="middle" transform="rotate(-38 105 150)" font-family="Outfit,Arial" font-weight="800" font-size="15" fill="#0E1B3D" fill-opacity=".05" letter-spacing="2">CAMDAY</text>' +
      '</svg></div>';
  }

  // guilloche rosette, unique to each verification code
  function seal(c) {
    var h = fnv(c), paths = '', cols = ['#0149AF', '#0E1B3D', '#B9842B', '#0149AF'];
    for (var k = 0; k < 4; k++) {
      var n = 14 + ((h >>> (k * 6)) % 13), a = 30 + k * 4, b = 4 + ((h >>> (k * 4 + 2)) % 5), ph = (h >>> (k * 3)) % 7, pts = [];
      for (var t = 0; t <= Math.PI * 2 + .01; t += 0.01) {
        var r = a + b * Math.cos(n * t + ph) + 1.5 * Math.sin((n * 2 + 1) * t);
        pts.push((50 + r * Math.cos(t)).toFixed(2) + ',' + (50 + r * Math.sin(t)).toFixed(2));
      }
      paths += '<polyline points="' + pts.join(' ') + '" fill="none" stroke="' + cols[k] + '" stroke-width=".4" stroke-opacity=".85"/>';
    }
    return '<svg class="seal" viewBox="0 0 100 100">' + paths + '<circle cx="50" cy="50" r="22" fill="#fff" stroke="#0E1B3D" stroke-width=".5"/><text x="50" y="49" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="9" fill="#0E1B3D">CAMDAY</text><text x="50" y="58" text-anchor="middle" font-family="Figtree" font-weight="700" font-size="5.5" fill="#0149AF">VERIFIED</text></svg>';
  }

  function waves() {
    var s = '';
    for (var i = 0; i < 9; i++) {
      var p = '';
      for (var x = 0; x <= 178; x += 2) p += (x ? ' L' : 'M') + x + ',' + (6 + Math.sin(x / (7 + i * .6) + i) * 3.2 + Math.cos(x / 13) * 1.2).toFixed(2);
      s += '<path d="' + p + '" fill="none" stroke="' + (i % 2 ? '#0149AF' : '#B9842B') + '" stroke-width=".18" stroke-opacity=".7"/>';
    }
    return '<svg viewBox="0 0 178 12" preserveAspectRatio="none" style="width:100%;height:5mm;display:block;margin-top:1.5mm">' + s + '</svg>';
  }

  // ---------- page parts ----------
  function boxes(txt, n) { var o = '<span class="boxes">'; for (var i = 0; i < n; i++) o += '<i>' + esc(txt[i] || '') + '</i>'; return o + '</span>'; }
  function foot(info, n, last) {
    return '<div class="pfoot"><div>© Camday 2026 · ' + DOC.id + ' · Copy #' + info.serial + ' · ' + esc(info.code) + '<br>Printed for ' + esc(info.name) + ' (' + LEARNER.id + ') on ' + info.when + '. Not for sharing or resale.</div>' +
      '<div class="to">' + (last ? 'End of worksheet' : '[Turn over') + '</div></div>';
  }
  function head(info, n) { return '<div class="qhead"><span><b>Cambridge</b> Stage 7 Science · ' + DOC.unit + ' · ' + DOC.sec + '</span><b>' + n + '</b></div>'; }
  function page(info, n, inner) {
    return '<div class="a4">' + micro('t') + micro('b') + micro('l') + micro('r') + watermark(info, n === 1) + '<div class="pad"><div class="content">' + inner + '</div></div></div>';
  }

  function cover(info) {
    var d = info.date, dd = ('0' + d.getDate()).slice(-2) + ('0' + (d.getMonth() + 1)).slice(-2) + d.getFullYear();
    return page(info, 1,
      '<div class="cv-h"><img src="../camday_logo.png" alt="" style="height:17mm"><div><div class="nm">CAMDAY</div><div class="tg"><b>Cambridge</b> Lower Secondary Science · Checkpoint preparation</div></div></div>' + waves() +
      '<div class="cv-meta">Written by the Camday teaching team · Videos, practice and Unit Tests online at Camday<br>Learner account: ' + esc(LEARNER.email) + '</div>' +
      '<div class="cv-ttl"><span>PRACTICE WORKSHEET</span><span class="sc">SCORE: ______ / ' + DOC.marks + '</span></div>' +
      '<table class="grid"><tr><td class="k">LEARNER NAME</td><td colspan="3" class="pre">' + esc(info.name) + '</td></tr>' +
      '<tr><td class="k">LEARNER ID</td><td>' + boxes(LEARNER.id.replace(/-/g, ''), 7) + '</td><td class="k" style="width:22mm">DATE</td><td>' + boxes(dd, 8) + '</td></tr></table>' +
      '<div class="subj"><div class="ico"><svg width="56" height="56" viewBox="0 0 56 56"><rect x="6" y="10" width="44" height="36" rx="10" fill="none" stroke="#0E1B3D" stroke-width="3"/><ellipse cx="28" cy="28" rx="13" ry="9" fill="#DCE8FA" stroke="#0149AF" stroke-width="2"/><circle cx="33" cy="27" r="4" fill="#0E1B3D"/><circle cx="13" cy="18" r="2.6" fill="#1F9D5C"/><circle cx="43" cy="38" r="2.6" fill="#1F9D5C"/><circle cx="15" cy="39" r="2.6" fill="#1F9D5C"/></svg></div>' +
      '<div><div class="camline"><b>CAMBRIDGE</b> STAGE 7 · SCIENCE</div><div style="font-size:11pt;margin-top:1mm">' + DOC.unit + '<br>' + DOC.sec + '</div></div>' +
      '<div><div class="code">' + DOC.id + '</div><div style="margin-top:1mm">' + DOC.mins + ' minutes</div><div style="font-size:9pt;color:#3E4558">' + DOC.marks + ' marks</div></div></div>' +
      '<p style="margin:5mm 0 0">You must answer on this worksheet.</p>' +
      '<div class="sec">YOU WILL NEED</div><ul><li>A pen and a ruler. No other materials are needed.</li></ul>' +
      '<div class="sec">INSTRUCTIONS</div><ul><li>Answer <b>all</b> questions.</li><li>Use a black or dark blue pen. You may use an HB pencil for diagrams.</li><li>Write your answer to each question in the space provided.</li><li>When you finish, open Unit 3 on Camday and check your answers with the worked solutions.</li></ul>' +
      '<div class="sec">INFORMATION</div><ul><li>The total mark for this worksheet is <b>' + DOC.marks + '</b>.</li><li>The number of marks for each question or part question is shown in brackets [ ].</li></ul>' +
      '<div class="verify">' + seal(info.code) + '<div>Verification code<br><b>' + info.code + '</b><br>Check this copy at <b style="font-size:9pt;letter-spacing:0">atomic › Verify a document</b>. The code is tied to this learner, this worksheet and copy #' + info.serial + '. A copy whose code does not match was not printed by Camday.</div></div>' +
      '<p style="text-align:center;font-size:9pt;margin:3mm 0 0">This worksheet has <b>' + DOC.pages + '</b> pages.</p>' + foot(info, 1));
  }

  var CELL = '<svg width="230" height="210" viewBox="0 0 230 210" font-family="Figtree,Arial" font-size="13" font-weight="700">' +
    '<rect x="60" y="15" width="100" height="180" rx="16" fill="none" stroke="#111" stroke-width="3"/>' +
    '<rect x="66" y="21" width="88" height="168" rx="12" fill="#F4F6F2" stroke="#111" stroke-width="1"/>' +
    '<path d="M84 40 Q110 30 136 42 Q146 100 134 166 Q108 176 84 166 Q74 100 84 40Z" fill="#fff" stroke="#111" stroke-width="1.2"/>' +
    '<ellipse cx="141" cy="105" rx="7" ry="10" fill="#333"/>' +
    '<g fill="#B8D8B0" stroke="#111" stroke-width=".9"><ellipse cx="76" cy="40" rx="6" ry="4"/><ellipse cx="146" cy="46" rx="6" ry="4"/><ellipse cx="74" cy="110" rx="4" ry="6"/><ellipse cx="78" cy="176" rx="6" ry="4"/><ellipse cx="144" cy="172" rx="6" ry="4"/><ellipse cx="110" cy="182" rx="6" ry="4"/></g>' +
    '<g stroke="#111" stroke-width="1"><line x1="160" y1="30" x2="196" y2="30"/><line x1="154" y1="62" x2="196" y2="62"/><line x1="146" y1="105" x2="196" y2="105"/><line x1="40" y1="110" x2="70" y2="110"/><line x1="40" y1="70" x2="110" y2="70"/><line x1="40" y1="150" x2="67" y2="150"/></g>' +
    '<text x="200" y="35">A</text><text x="200" y="67">B</text><text x="200" y="110">C</text><text x="26" y="115">D</text><text x="26" y="75">E</text><text x="26" y="155">F</text></svg>';

  function mcq(opts) { return '<div class="opts">' + opts.map(function (o) { return '<span>' + o + '</span>'; }).join('') + '</div>'; }
  function lines(n) { var s = ''; for (var i = 0; i < n; i++) s += '<div class="dots"></div>'; return s; }

  function p2(info) {
    return page(info, 2, head(info, 2) +
      '<div class="q"><div class="n">1</div><div><p>The diagram shows a cell from a leaf.</p><div class="cellfig">' + CELL + '</div>' +
      '<div class="part"><span class="l">(a)</span><div>Circle the letter that labels the cell wall.<div style="display:flex;justify-content:space-around;font-weight:800;margin:2mm 10mm"><span>A</span><span>B</span><span>C</span><span>D</span><span>E</span><span>F</span></div><span class="mk">[1]</span></div></div>' +
      '<div class="part"><span class="l">(b)</span><div>Name the part labelled <b>D</b>.<div class="ansrow"><div class="dots"></div><b>[1]</b></div></div></div>' +
      '<div class="part"><span class="l">(c)</span><div>Name <b>two</b> parts of this cell that you would <b>not</b> find in an animal cell.<div class="ansrow"><span>1</span><div class="dots"></div></div><div class="ansrow"><span>2</span><div class="dots"></div><b>[2]</b></div></div></div></div></div>' +
      '<div class="q"><div class="n">2</div><div><p>Which statement about the cell wall is <b>false</b>? Tick (✓) <b>one</b> box.</p>' +
      mcq(['It is made of cellulose.', 'It controls exactly which substances enter the cell.', 'It supports the cell and gives it a regular shape.', 'Animal cells do not have one.']) + '<span class="mk">[1]</span></div></div>' +
      '<div class="q"><div class="n">3</div><div><p>Why is iodine solution added to onion cells on a microscope slide? Tick (✓) <b>one</b> box.</p>' +
      mcq(['To kill any bacteria on the slide', 'To stain parts of the cells so they are easier to see', 'To remove the cell walls', 'To make the cells grow bigger']) + '<span class="mk">[1]</span></div></div>' +
      foot(info, 2));
  }

  function p3(info) {
    return page(info, 3, head(info, 3) +
      '<div class="q"><div class="n">4</div><div><p>Draw <b>one</b> straight line from each cell part to its job.</p>' +
      '<table class="mtab"><tr><td>nucleus</td><td class="mid"></td><td>keeps the cell firm by taking in water</td></tr><tr><td>cell membrane</td><td class="mid"></td><td>releases energy from food</td></tr><tr><td>mitochondrion</td><td class="mid"></td><td>controls what the cell does</td></tr><tr><td>sap vacuole</td><td class="mid"></td><td>controls what goes into and out of the cell</td></tr></table><span class="mk">[4]</span></div></div>' +
      '<div class="q"><div class="n">5</div><div><p>A student drew an onion bulb cell and added chloroplasts. The teacher marked the drawing wrong.</p><p>Explain why.</p>' + lines(1) + '<div class="ansrow"><div class="dots"></div><b>[2]</b></div></div></div>' +
      '<div class="q"><div class="n">6</div><div><p>Cheek cells on a slide are spread out and have irregular shapes. Suggest <b>two</b> reasons.</p>' + lines(1) + '<div class="ansrow"><div class="dots"></div><b>[2]</b></div></div></div>' +
      '<div class="q"><div class="n">7</div><div><p>Dodder is a plant with <b>no</b> green parts. It grows wrapped around other plants.</p><p>State which cell part dodder cells are missing, and how dodder gets its food.</p>' + lines(1) + '<div class="ansrow"><div class="dots"></div><b>[2]</b></div></div></div>' +
      '<div class="end">— End of worksheet · total ' + DOC.marks + ' marks —</div>' +
      '<div style="margin-top:auto"></div>' + foot(info, 3, true));
  }

  function build(name, printing) {
    var d = new Date(), s = printing ? ++serial : serial;
    var info = { name: name || 'Learner', date: d, when: stamp(d), serial: String(s).padStart(6, '0'), k: printing ? 'p' : 's' };
    info.code = code(DOC.id + '|' + LEARNER.id + '|' + info.serial + '|' + info.when);
    return cover(info) + p2(info) + p3(info);
  }

  // ---------- wire up ----------
  var who = document.getElementById('who'), pages = document.getElementById('pages'), pr = document.getElementById('printRoot');
  function render() { pages.innerHTML = build(who.value.trim()); }
  function doPrint() {
    pr.innerHTML = build(who.value.trim(), true);   // fresh copy number + time for every print (logged on the server in the real app)
    setTimeout(function () { window.print(); }, 60);
  }
  who.addEventListener('input', render);
  document.getElementById('printBtn').addEventListener('click', doPrint);
  window.addEventListener('afterprint', function () { pr.innerHTML = ''; render(); });

  // deterrents (screen only)
  ['contextmenu', 'copy', 'cut', 'dragstart', 'selectstart'].forEach(function (ev) {
    pages.addEventListener(ev, function (e) { e.preventDefault(); });
  });
  document.addEventListener('keydown', function (e) {
    var k = (e.key || '').toLowerCase();
    if ((e.ctrlKey || e.metaKey) && (k === 's' || k === 'p')) { e.preventDefault(); if (k === 'p') doPrint(); }
  });
  document.addEventListener('visibilitychange', function () { document.body.classList.toggle('blurred', document.hidden); });

  render();
})();
