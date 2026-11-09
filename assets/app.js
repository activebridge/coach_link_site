// Tiny glue: UTM/ref capture, form submit, referral link copy. No dependencies, no cookies.
(function () {
  var q = new URLSearchParams(location.search), meta = {};
  ["utm_source", "utm_medium", "utm_campaign", "ref"].forEach(function (k) { if (q.get(k)) meta[k] = q.get(k); });
  try { var s = sessionStorage.getItem("cl_meta"); if (s && !Object.keys(meta).length) meta = JSON.parse(s); else if (Object.keys(meta).length) sessionStorage.setItem("cl_meta", JSON.stringify(meta)); } catch (e) {}
  var lang = document.currentScript.dataset.lang;
  function send(form, done) {
    var data = {}; new FormData(form).forEach(function (v, k) { if (data[k] === undefined) data[k] = v; else data[k] = [].concat(data[k], v); });
    if (data.company) return; // honeypot
    data.lang = lang; data.meta = meta; data.form = form.id;
    var url = form.dataset.endpoint;
    if (!url) { console.info("[demo mode] no FORM_ENDPOINT set, not sent:", data); return done(); }
    fetch(url, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw 0; done(); }).catch(function () { alert("Something went wrong. Please try again or email us."); });
  }
  var beta = document.getElementById("beta-form");
  if (beta) beta.addEventListener("submit", function (ev) {
    ev.preventDefault();
    send(beta, function () { beta.classList.add("sent"); document.getElementById("thanks").scrollIntoView({ behavior: "smooth", block: "center" }); });
  });
  var evf = document.getElementById("event-form");
  if (evf) evf.addEventListener("submit", function (ev) {
    ev.preventDefault();
    send(evf, function () { evf.innerHTML = "<strong>✓</strong>"; });
  });
  var copy = document.getElementById("copy");
  if (copy) copy.addEventListener("click", function () {
    var link = location.origin + location.pathname + "?ref=" + encodeURIComponent((document.querySelector("[name=email]").value || "").split("@")[0]);
    (navigator.clipboard ? navigator.clipboard.writeText(link) : Promise.resolve()).then(function () { copy.textContent = copy.dataset.done; });
  });
})();
