/* Coach Link landing: forms, live demo data, smooth scroll and scroll-driven motion.
   Everything degrades: without JS or with prefers-reduced-motion the page is a plain static layout. */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement;
  var lang = document.currentScript.dataset.lang;
  var calm = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = matchMedia("(hover:hover) and (pointer:fine)").matches;

  /* ---------- forms (unchanged behaviour) ---------- */
  var q = new URLSearchParams(location.search), meta = {};
  ["utm_source", "utm_medium", "utm_campaign", "ref"].forEach(function (k) { if (q.get(k)) meta[k] = q.get(k); });
  try { var s = sessionStorage.getItem("cl_meta"); if (s && !Object.keys(meta).length) meta = JSON.parse(s); else if (Object.keys(meta).length) sessionStorage.setItem("cl_meta", JSON.stringify(meta)); } catch (e) {}
  function send(form, done) {
    var data = {}; new FormData(form).forEach(function (v, k) { if (data[k] === undefined) data[k] = v; else data[k] = [].concat(data[k], v); });
    if (data.company) return;
    data.lang = lang; data.meta = meta; data.form = form.id;
    var url = form.dataset.endpoint;
    if (!url) { console.info("[demo mode] no FORM_ENDPOINT set, not sent:", data); return done(); }
    fetch(url, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw 0; done(); }).catch(function () { alert("Something went wrong. Please try again or email us."); });
  }
  var beta = $("#beta-form");
  if (beta) beta.addEventListener("submit", function (ev) {
    ev.preventDefault();
    if (!beta.checkValidity()) { beta.reportValidity(); return; }
    send(beta, function () { beta.classList.add("sent"); $("#thanks").scrollIntoView({ behavior: calm ? "auto" : "smooth", block: "center" }); });
  });
  var copy = $("#copy");
  if (copy) copy.addEventListener("click", function () {
    var link = location.origin + location.pathname + "?ref=" + encodeURIComponent(($("#f-email").value || "").split("@")[0]);
    (navigator.clipboard ? navigator.clipboard.writeText(link) : Promise.resolve()).then(function () { copy.textContent = copy.dataset.done; });
  });

  /* ---------- live heart-rate demo (decorative) ---------- */
  var MAXHR = 190, LIM = [[171, 5], [152, 4], [133, 3], [114, 2], [0, 1]];
  var zoneOf = function (hr) { for (var i = 0; i < LIM.length; i++) if (hr >= LIM[i][0]) return LIM[i][1]; return 1; };
  var live = $$("[data-live]").map(function (el) {
    return { el: el, base: +el.dataset.base, amp: +el.dataset.amp, ph: +el.dataset.phase, hr: $(".lc-hr", el), zn: $(".lc-zone", el), ring: $(".w-val", el), z: 0, last: 0, vis: false };
  });
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) { es.forEach(function (en) { live.forEach(function (l) { if (l.el === en.target) l.vis = en.isIntersecting; }); }); }, { threshold: 0.1 }) : null;
  live.forEach(function (l) { if (io) io.observe(l.el); else l.vis = true; });
  function tick(now) {
    var t = now / 1000;
    live.forEach(function (l) {
      if (!l.vis) return;
      var v = Math.round(l.base + Math.sin(t / 5.5 + l.ph) * l.amp + Math.sin(t * 1.7 + l.ph * 3) * 3);
      if (v === l.last) return; l.last = v;
      l.hr.textContent = v;
      var z = zoneOf(v);
      if (z !== l.z) { l.z = z; l.el.style.setProperty("--zc", "var(--z" + z + ")"); if (l.zn) l.zn.textContent = (l.zn.classList.contains("w-zone") ? "Z" : l.zn.textContent.replace(/\d+$/, "").trim() + " ") + z; }
      if (l.ring) l.ring.setAttribute("stroke-dashoffset", (100 - v / MAXHR * 100).toFixed(1));
    });
  }
  if (!calm) setInterval(function () { if (!document.hidden) tick(performance.now()); }, 1000);

  /* ---------- header + nav highlight (no libraries needed) ---------- */
  var bar = $("#bar");
  var onScroll = function () { if (bar) bar.classList.toggle("scrolled", (window.scrollY || 0) > 24); };
  addEventListener("scroll", onScroll, { passive: true }); onScroll();
  var navs = $$(".nl[data-nav]");
  if (navs.length && io) {
    var map = {}; navs.forEach(function (a) { var s = document.getElementById(a.dataset.nav); if (s) map[a.dataset.nav] = s; });
    var navIO = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) navs.forEach(function (a) { a.classList.toggle("active", map[a.dataset.nav] === en.target); }); });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(map).forEach(function (k) { navIO.observe(map[k]); });
    ["#top", "#apply"].forEach(function (id) { var x = $(id); if (x) navIO.observe(x); });
  }

  /* ---------- spotlight on cards (cheap: only sets two CSS vars) ---------- */
  if (fine) $$("[data-spot]").forEach(function (c) {
    c.addEventListener("pointermove", function (e) { var r = c.getBoundingClientRect(); c.style.setProperty("--mx", (e.clientX - r.left) + "px"); c.style.setProperty("--my", (e.clientY - r.top) + "px"); });
  });

  /* ---------- everything below needs motion + libraries ---------- */
  if (calm) return;
  function start() {
    if (!window.gsap || !window.ScrollTrigger) return false;
    var gsap = window.gsap, ST = window.ScrollTrigger;
    gsap.registerPlugin(ST);
    root.classList.add("js");

    /* smooth scroll */
    var lenis = null;
    if (window.Lenis && fine) {
      lenis = new window.Lenis({ duration: 1.1, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
      lenis.on("scroll", ST.update);
      gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
      gsap.ticker.lagSmoothing(0);
    }
    $$('a[href^="#"]').forEach(function (a) {
      a.addEventListener("click", function (e) {
        var id = a.getAttribute("href"); if (id.length < 2) return;
        var t = $(id); if (!t) return;
        e.preventDefault();
        if (lenis) lenis.scrollTo(t, { offset: id === "#story" ? 0 : -50 }); else t.scrollIntoView({ behavior: "smooth" });
        history.replaceState(null, "", id);
      });
    });

    /* reveal on enter */
    ST.batch("[data-reveal]", { start: "top 88%", once: true, onEnter: function (els) {
      els.forEach(function (el, i) { setTimeout(function () { el.classList.add("in"); }, i * 80); });
    } });

    /* counters */
    $$("[data-count]").forEach(function (el) {
      var end = +el.dataset.count; if (!end) return;
      var o = { v: 0 }; el.textContent = "0";
      ST.create({ trigger: el, start: "top 92%", once: true, onEnter: function () {
        gsap.to(o, { v: end, duration: 1.6, ease: "power3.out", onUpdate: function () { el.textContent = Math.round(o.v); } });
      } });
    });

    /* hero parallax: pointer + scroll, transform only */
    var stage = $("[data-parallax]");
    if (stage) {
      var layers = $$("[data-depth]", stage), hw = $(".hero-watch", stage);
      if (fine) {
        var xs = layers.concat(hw ? [hw] : []).map(function (l) { return { x: gsap.quickTo(l, "x", { duration: .9, ease: "power3" }), y: gsap.quickTo(l, "y", { duration: .9, ease: "power3" }), d: +(l.dataset.depth || 26) }; });
        $(".hero").addEventListener("pointermove", function (e) {
          var nx = e.clientX / innerWidth - .5, ny = e.clientY / innerHeight - .5;
          xs.forEach(function (o) { o.x(nx * o.d * -1); o.y(ny * o.d * -1); });
        });
      }
      gsap.to(stage, { yPercent: -8, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
    }

    /* how-it-works progress line */
    var steps = $(".steps");
    if (steps) {
      var line = $(".steps-line i", steps), items = $$(".step", steps), vertical = function () { return innerWidth <= 760; };
      ST.create({ trigger: steps, start: "top 75%", end: "bottom 60%", scrub: .4, onUpdate: function (s) {
        line.style.setProperty("--k", s.progress.toFixed(3));
        items.forEach(function (it, i) { it.classList.toggle("on", s.progress >= i / (items.length - 1) - .02); });
      } });
      items.forEach(function (it) { it.classList.remove("on"); });
    }

    /* pinned story */
    var story = $("[data-story]");
    if (story) buildStory(story, gsap, ST);

    ST.refresh();
    return true;
  }

  function buildStory(story, gsap, ST) {
    var pin = $(".story-pin", story), stage = $(".story-stage", story);
    var watchEl = $(".s-watch .watch", story), cards = $$(".s-card", story), caps = $$(".cap", story);
    var base = $(".sp-base", story), glow = $(".sp-glow", story), dots = $$(".sp-dots circle", story);
    var poke = $(".s-poke", story), phone = $(".s-phone", story), watchWrap = $(".s-watch", story);
    var tl, len = 0, pts = null;

    function layout() {
      var sr = stage.getBoundingClientRect(), wr = watchEl.getBoundingClientRect(), pr = phone.getBoundingClientRect();
      var vert = innerWidth <= 860;
      var x1 = vert ? wr.left - sr.left + wr.width / 2 : wr.right - sr.left, y1 = vert ? wr.bottom - sr.top : wr.top - sr.top + wr.height / 2;
      var x2 = vert ? pr.left - sr.left + pr.width / 2 : pr.left - sr.left, y2 = vert ? pr.top - sr.top : pr.top - sr.top + pr.height / 2;
      var d = vert ? "M" + x1 + " " + y1 + "C" + x1 + " " + (y1 + (y2 - y1) * .5) + " " + x2 + " " + (y1 + (y2 - y1) * .5) + " " + x2 + " " + y2
                   : "M" + x1 + " " + y1 + "C" + (x1 + (x2 - x1) * .5) + " " + y1 + " " + (x1 + (x2 - x1) * .5) + " " + y2 + " " + x2 + " " + y2;
      base.setAttribute("d", d); glow.setAttribute("d", d);
      len = glow.getTotalLength();
      glow.style.strokeDasharray = len; glow.style.strokeDashoffset = len;
    }
    var at = function (p) { return glow.getPointAtLength(len * p); };

    function build() {
      if (tl) { tl.scrollTrigger && tl.scrollTrigger.kill(); tl.kill(); }
      layout();
      var vert = innerWidth <= 860;
      var o = { p: 0, dots: 0 };
      gsap.set(cards, { opacity: 0, y: 24, scale: .96 });
      gsap.set(poke, { opacity: 0 });
      gsap.set(dots, { opacity: 0 });
      gsap.set(watchEl, { scale: .85, opacity: .5 });
      gsap.set(phone, { opacity: .35 });
      caps.forEach(function (c) { c.classList.remove("on"); });
      setCap(0);
      tl = gsap.timeline({ defaults: { ease: "none" }, scrollTrigger: {
        trigger: pin, start: "top top", end: "+=" + (vert ? 220 : 260) + "%", pin: true, scrub: .6, anticipatePin: 1, invalidateOnRefresh: true,
        onUpdate: function (s) { setCap(s.progress < .33 ? 0 : s.progress < .7 ? 1 : 2); $(".s-prog i", story) && ($(".s-prog i", story).style.transform = "scaleX(" + s.progress + ")"); },
        onRefresh: function () { layout(); }
      } });
      /* scene 1: client trains */
      tl.to(watchEl, { scale: 1, opacity: 1, duration: .25, ease: "power2.out" }, 0)
        .to(phone, { opacity: .6, duration: .25 }, 0);
      /* scene 2: data flies */
      tl.to(glow, { strokeDashoffset: 0, duration: .3 }, .3);
      tl.to(o, { dots: 1, duration: .4, onUpdate: function () {
        dots.forEach(function (d, i) {
          var k = (o.dots * 1.4 - i * .12); k = Math.max(0, Math.min(1, k));
          var pt = at(k); d.setAttribute("cx", pt.x); d.setAttribute("cy", pt.y);
          d.style.opacity = k > 0 && k < 1 ? 1 : 0;
        });
      } }, .32);
      /* scene 3: phone lights up, coach pokes, watch buzzes */
      tl.to(phone, { opacity: 1, duration: .15 }, .68)
        .to(cards, { opacity: 1, y: 0, scale: 1, duration: .12, stagger: .06, ease: "power2.out" }, .7)
        .to(poke, { opacity: 1, duration: .08 }, .84).to(poke, { scale: .9, duration: .04 }, .9).to(poke, { scale: 1.08, duration: .04 }, .94)
        .add(function () { if (tl.scrollTrigger.direction > 0) { watchEl.classList.remove("buzz"); void watchEl.offsetWidth; watchEl.classList.add("buzz"); } }, .94)
        .to({}, { duration: .06 }, .94);
    }
    var cur = -1;
    function setCap(i) { if (i === cur) return; cur = i; caps.forEach(function (c, k) { c.classList.toggle("on", k === i); }); }

    build();
    var rt; addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { var w = innerWidth; if (build.w !== w) { build.w = w; build(); ST.refresh(); } }, 200); });
    build.w = innerWidth;
  }

  var tries = 0;
  (function wait() { if (start()) return; if (++tries < 80) setTimeout(wait, 50); })();
})();
