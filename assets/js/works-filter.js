/* works-filter.js – Filter der Werkliste (works.html), ohne Bibliotheken.

   Die Liste steht vollständig im HTML. Dieses Skript lädt data/works.json,
   blendet Werke nach den gewählten Filtern aus, zählt die Treffer pro Option,
   sortiert und schreibt den Zustand in die Adresse, z. B.
     works.html?genre=article&lang=fra&from=1960&to=1970&sort=title
   Innerhalb eines Filters gilt «oder», zwischen den Filtern «und».
*/
(function () {
  'use strict';

  var script = document.currentScript;
  var FACETS = ['worktype', 'genre', 'lang', 'keywords'];

  var form = document.querySelector('[data-facets]');
  var list = document.querySelector('[data-list]');
  var sortSelect = document.querySelector('[data-sort]');
  var range = document.querySelector('[data-range]');
  var badges = document.querySelector('[data-badges]');
  var empty = document.querySelector('[data-empty]');
  if (!form || !list) return;

  var MIN = +range.dataset.min;
  var MAX = +range.dataset.max;
  var fromInput = range.querySelector('input[type=range][name=from]');
  var toInput = range.querySelector('input[type=range][name=to]');
  var fields = range.querySelectorAll('input[type=number]');

  // Kategorien ohne Bezeichnung in taxonomy.json (Entscheid 2026-10-14: Schlüssel zeigen)
  form.querySelectorAll('label[data-missing-label]').forEach(function (label) {
    console.warn('Werkliste: keine Bezeichnung in taxonomy.json für «' + label.htmlFor.replace(/^f-/, '') + '», Schlüssel wird angezeigt.');
  });

  var works = [];
  var items = {};
  list.querySelectorAll('li[data-id]').forEach(function (li) { items[li.dataset.id] = li; });

  function values(work, facet) {
    var v = work[facet];
    return Array.isArray(v) ? v : (v ? [v] : []);
  }

  function readState() {
    var params = new URLSearchParams(location.search);
    var state = { sel: {}, from: MIN, to: MAX, sort: 'year' };
    FACETS.forEach(function (f) {
      state.sel[f] = [];
      params.getAll(f).forEach(function (v) {
        v.split(',').forEach(function (k) { if (k && state.sel[f].indexOf(k) < 0) state.sel[f].push(k); });
      });
    });
    var from = parseInt(params.get('from'), 10);
    var to = parseInt(params.get('to'), 10);
    if (!isNaN(from)) state.from = Math.min(Math.max(from, MIN), MAX);
    if (!isNaN(to)) state.to = Math.min(Math.max(to, MIN), MAX);
    if (state.from > state.to) { var t = state.from; state.from = state.to; state.to = t; }
    if (['year', 'year-desc', 'title'].indexOf(params.get('sort')) >= 0) state.sort = params.get('sort');
    return state;
  }

  function stateFromForm() {
    var state = { sel: {}, from: +fromInput.value, to: +toInput.value, sort: sortSelect.value };
    FACETS.forEach(function (f) {
      state.sel[f] = Array.prototype.map.call(form.querySelectorAll('input[name="' + f + '"]:checked'), function (i) { return i.value; });
    });
    return state;
  }

  function applyToForm(state) {
    FACETS.forEach(function (f) {
      form.querySelectorAll('input[name="' + f + '"]').forEach(function (i) { i.checked = state.sel[f].indexOf(i.value) >= 0; });
    });
    fromInput.value = state.from;
    toInput.value = state.to;
    fields[0].value = state.from;
    fields[1].value = state.to;
    sortSelect.value = state.sort;
  }

  function writeUrl(state) {
    var params = new URLSearchParams();
    FACETS.forEach(function (f) { state.sel[f].forEach(function (v) { params.append(f, v); }); });
    if (state.from > MIN) params.set('from', state.from);
    if (state.to < MAX) params.set('to', state.to);
    if (state.sort !== 'year') params.set('sort', state.sort);
    var query = params.toString();
    history.replaceState(null, '', location.pathname + (query ? '?' + query : '') + location.hash);
  }

  // Passt ein Werk? `except` lässt einen Filter weg (für die Zahlen pro Option).
  function matches(work, state, except) {
    for (var i = 0; i < FACETS.length; i++) {
      var f = FACETS[i];
      if (f === except || !state.sel[f].length) continue;
      var v = values(work, f);
      if (!state.sel[f].some(function (k) { return v.indexOf(k) >= 0; })) return false;
    }
    var year = parseInt(work.year, 10);
    var rangeActive = state.from > MIN || state.to < MAX;
    if (isNaN(year)) return !rangeActive;
    return year >= state.from && year <= state.to;
  }

  function compare(sort) {
    var collator = new Intl.Collator('de', { sensitivity: 'base', ignorePunctuation: true });
    return function (a, b) {
      if (sort === 'title') return collator.compare(a.title, b.title);
      var d = (parseInt(a.year, 10) || 9999) - (parseInt(b.year, 10) || 9999);
      if (sort === 'year-desc') d = -d;
      return d || collator.compare(a.title, b.title);
    };
  }

  function labelFor(input) {
    var label = form.querySelector('label[for="' + input.id + '"]');
    return label ? label.firstChild.textContent.trim() : input.value;
  }

  function renderBadges(state) {
    badges.querySelectorAll('.facet-badge:not([data-reset])').forEach(function (b) { b.remove(); });
    var active = form.querySelectorAll('.facet-box:checked');
    var rangeActive = state.from > MIN || state.to < MAX;
    active.forEach(function (input) {
      var badge = document.createElement('span');
      badge.className = 'facet-badge';
      badge.textContent = labelFor(input) + ' ';
      var remove = document.createElement('button');
      remove.type = 'button';
      remove.className = 'facet-badge-remove';
      remove.setAttribute('aria-label', labelFor(input) + ' entfernen');
      remove.textContent = '×';
      remove.addEventListener('click', function () { input.checked = false; update(); });
      badge.appendChild(remove);
      badges.appendChild(badge);
    });
    if (rangeActive) {
      var b = document.createElement('span');
      b.className = 'facet-badge';
      b.textContent = state.from + '–' + state.to + ' ';
      var r = document.createElement('button');
      r.type = 'button';
      r.className = 'facet-badge-remove';
      r.setAttribute('aria-label', 'Zeitraum zurücksetzen');
      r.textContent = '×';
      r.addEventListener('click', function () { fromInput.value = MIN; toInput.value = MAX; update(); });
      b.appendChild(r);
      badges.appendChild(b);
    }
    badges.hidden = !active.length && !rangeActive;
  }

  function render(state) {
    var visible = works.filter(function (w) { return matches(w, state); });
    var order = works.slice().sort(compare(state.sort));
    order.forEach(function (w) {
      var li = items[w.id];
      if (!li) return;
      li.hidden = visible.indexOf(w) < 0;
      list.appendChild(li);
    });
    document.querySelectorAll('[data-count]').forEach(function (el) { el.textContent = visible.length; });
    empty.hidden = visible.length > 0;

    // Trefferzahl pro Option: alle anderen Filter angewendet, diese Option dazu
    FACETS.forEach(function (f) {
      var base = works.filter(function (w) { return matches(w, state, f); });
      form.querySelectorAll('input[name="' + f + '"]').forEach(function (input) {
        var n = base.filter(function (w) { return values(w, f).indexOf(input.value) >= 0; }).length;
        var li = input.closest('li');
        li.querySelector('[data-freq]').textContent = n;
        li.classList.toggle('is-empty', n === 0 && !input.checked);
      });
    });
    renderBadges(state);
  }

  function update() {
    if (+fromInput.value > +toInput.value) {
      // Regler nicht übereinander schieben lassen
      if (document.activeElement === fromInput) fromInput.value = toInput.value;
      else toInput.value = fromInput.value;
    }
    fields[0].value = fromInput.value;
    fields[1].value = toInput.value;
    var state = stateFromForm();
    render(state);
    writeUrl(state);
  }

  form.addEventListener('change', update);
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  fromInput.addEventListener('input', update);
  toInput.addEventListener('input', update);
  sortSelect.addEventListener('change', update);
  fields.forEach(function (field) {
    field.addEventListener('change', function () {
      var v = Math.min(Math.max(parseInt(field.value, 10) || MIN, MIN), MAX);
      (field.dataset.for === 'from' ? fromInput : toInput).value = v;
      update();
    });
  });
  badges.querySelector('[data-reset]').addEventListener('click', function () {
    form.querySelectorAll('.facet-box').forEach(function (i) { i.checked = false; });
    fromInput.value = MIN;
    toInput.value = MAX;
    update();
  });

  fetch(script.dataset.works)
    .then(function (r) {
      if (!r.ok) throw new Error(r.status + ' ' + r.statusText);
      return r.json();
    })
    .then(function (data) {
      works = data;
      var state = readState();
      applyToForm(state);
      render(state);
      document.documentElement.classList.add('filters-ready');
    })
    .catch(function (err) {
      // Liste bleibt vollständig sichtbar, nur die Filter fehlen
      console.error('Werkliste: works.json konnte nicht geladen werden', err);
    });
})();
