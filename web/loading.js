/* Loading feedback: a thin progress bar while anything is fetched, an overlay for big switches (another stage),
   skeleton placeholders for slow pages and a spinner inside busy buttons. Respects "reduce motion". */
(function () {
  'use strict';
  const doc = document;
  let active = 0, shown = false, showT = null, doneT = null, w = 0, creep = null;
  const bar = () => {
    let b = doc.getElementById('routebar');
    if (!b) { b = doc.createElement('div'); b.id = 'routebar'; b.setAttribute('aria-hidden', 'true'); b.innerHTML = '<i></i>'; doc.body.appendChild(b); }
    return b;
  };
  function setW(v) { w = v; const i = bar().firstChild; if (i) i.style.width = v + '%'; }
  function start() {
    active++;
    if (active > 1 || shown) return;
    clearTimeout(doneT); clearTimeout(showT);
    showT = setTimeout(() => {   // only show for waits a person would notice
      if (!active) return; shown = true; const b = bar(); b.className = 'on'; setW(8);
      clearInterval(creep); creep = setInterval(() => { if (w < 90) setW(w + (90 - w) * 0.08); }, 160);
    }, 90);
  }
  function stop() {
    active = Math.max(0, active - 1);
    if (active) return;
    clearTimeout(showT); clearInterval(creep);
    if (!shown) return;
    setW(100); doneT = setTimeout(() => { const b = bar(); b.className = 'off'; shown = false; doneT = setTimeout(() => { if (!shown) setW(0); }, 260); }, 220);
  }
  function track(p) { start(); return Promise.resolve(p).finally(stop); }

  // every request the app makes moves the bar (course content, the account, marking)
  const realFetch = window.fetch && window.fetch.bind(window);
  if (realFetch) window.fetch = function () { return track(realFetch.apply(null, arguments)); };

  // a full-page panel for switches that replace the whole course on screen
  function overlay(text, p) {
    const o = doc.createElement('div'); o.className = 'loadover'; o.setAttribute('role', 'status'); o.setAttribute('aria-live', 'polite');
    o.innerHTML = `<div class="lo-box">${atom(64)}<b></b><span class="lo-dots"><i></i><i></i><i></i></span></div>`;
    o.querySelector('b').textContent = text || 'Loading';
    const t = setTimeout(() => { doc.body.appendChild(o); requestAnimationFrame(() => o.classList.add('in')); }, 120);
    return Promise.resolve(p).finally(() => { clearTimeout(t); o.classList.remove('in'); setTimeout(() => o.remove(), 220); });
  }
  // the Atomic atom: three orbits and an electron on each
  function atom(size) {
    return `<svg class="atomspin" width="${size}" height="${size}" viewBox="0 0 64 64" aria-hidden="true">
      <circle cx="32" cy="32" r="5" fill="#F3BF69"/>
      <g class="orb o1"><ellipse cx="32" cy="32" rx="27" ry="10" fill="none" stroke="#0149AF" stroke-width="2.4"/><circle cx="59" cy="32" r="3.4" fill="#0149AF"/></g>
      <g class="orb o2"><ellipse cx="32" cy="32" rx="27" ry="10" fill="none" stroke="#2F6FD6" stroke-width="2.4" transform="rotate(60 32 32)"/><circle cx="45.5" cy="55.4" r="3.4" fill="#2F6FD6"/></g>
      <g class="orb o3"><ellipse cx="32" cy="32" rx="27" ry="10" fill="none" stroke="#A9C6F2" stroke-width="2.4" transform="rotate(120 32 32)"/><circle cx="18.5" cy="55.4" r="3.4" fill="#C48A2C"/></g></svg>`;
  }
  // grey placeholder blocks in the shape of the page that is coming
  function skeleton(kind) {
    const s = doc.createElement('div'); s.className = 'skel'; s.setAttribute('aria-busy', 'true'); s.setAttribute('aria-label', 'Loading');
    const line = (wd, h) => `<i class="sk" style="width:${wd};height:${h || 14}px"></i>`;
    const card = inner => `<div class="skcard">${inner}</div>`;
    if (kind === 'rows') s.innerHTML = card(Array.from({ length: 6 }, () => `<div class="skrow"><i class="sk sq"></i><span>${line('62%', 15)}${line('38%', 11)}</span>${line('80px', 22)}</div>`).join(''));
    else if (kind === 'lines') s.innerHTML = `<div class="skinline">${line('70%')}${line('92%')}${line('54%')}</div>`;
    else s.innerHTML = `<div class="skgrid">${Array.from({ length: 3 }, () => card(`<i class="sk sq"></i>${line('70%', 18)}${line('92%')}${line('60%')}`)).join('')}</div>` + card(`${line('30%', 18)}${line('96%')}${line('88%')}${line('72%')}`);
    return s;
  }
  // a spinner inside a button until the work behind it ends
  function busy(btn, p) {
    if (!btn) return Promise.resolve(p);
    btn.classList.add('busy'); btn.setAttribute('aria-busy', 'true'); const was = btn.disabled; btn.disabled = true;
    return Promise.resolve(p).finally(() => { btn.classList.remove('busy'); btn.removeAttribute('aria-busy'); btn.disabled = was; });
  }
  function hideSplash() {
    const s = doc.getElementById('splash'); if (!s) return;
    s.classList.add('out'); setTimeout(() => s.remove(), 450);
  }
  window.Loading = { track, start, stop, overlay, skeleton, busy, atom, hideSplash };
})();
