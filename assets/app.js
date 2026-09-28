(function () {
  var TABS = [
    { id: "home", href: "/", label: "홈", icon: '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>' },
    { id: "plan", href: "/day1", label: "일정", icon: '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>' },
    { id: "stay", href: "/stay", label: "숙소", icon: '<path d="M3 19V8m0 7h18v4M3 11h8a3 3 0 0 1 3 3v1M21 15v-2a4 4 0 0 0-4-4h-3"/><circle cx="7" cy="8.5" r="1.8"/>' },
    { id: "move", href: "/transport", label: "교통", icon: '<path d="M21 15.5 13.5 12V5.5a1.5 1.5 0 0 0-3 0V12L3 15.5V17l7.5-2v3.5L8.5 20v1.2l3.5-.9 3.5.9V20l-2-1.5V15l7.5 2z"/>' },
    { id: "money", href: "/budget", label: "예산", icon: '<rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M3 10h18M7 15h3"/>' }
  ];

  var nav = document.querySelector("nav.tabbar");
  if (nav) {
    var active = nav.getAttribute("data-active");
    nav.innerHTML = TABS.map(function (t) {
      return '<a href="' + t.href + '"' + (t.id === active ? ' aria-current="page"' : "") + '>' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + t.icon + "</svg>" +
        "<span>" + t.label + "</span></a>";
    }).join("");
  }

  // D-day (출발: 2026-11-30 13:20 KST)
  var dd = document.querySelectorAll("[data-dday]");
  if (dd.length) {
    var depart = new Date("2026-11-30T00:00:00+09:00");
    var now = new Date();
    var today = new Date(now.toLocaleDateString("en-CA", { timeZone: "Asia/Seoul" }) + "T00:00:00+09:00");
    var diff = Math.round((depart - today) / 86400000);
    var text = diff > 0 ? "D-" + diff : diff === 0 ? "D-DAY" : diff >= -2 ? "여행 중" : "다녀왔어요";
    dd.forEach(function (el) { el.textContent = text; });
  }

  // 사진 캐러셀: 스와이프, 화살표, 점, 키보드
  document.querySelectorAll(".carousel").forEach(function (c) {
    var track = c.querySelector(".track");
    var count = c.querySelector(".count");
    var prev = c.querySelector(".nav.prev");
    var next = c.querySelector(".nav.next");
    var dots = c.querySelectorAll(".dot");
    var n = track.children.length;
    function index() { return Math.round(track.scrollLeft / (track.clientWidth || 1)); }
    function go(i) {
      i = Math.max(0, Math.min(n - 1, i));
      track.scrollTo({ left: i * track.clientWidth, behavior: "smooth" });
    }
    function update() {
      var i = Math.min(index(), n - 1);
      if (count) count.textContent = (i + 1) + " / " + n;
      if (prev) prev.disabled = i === 0;
      if (next) next.disabled = i === n - 1;
      dots.forEach(function (d, k) { d.setAttribute("aria-current", k === i ? "true" : "false"); });
    }
    if (prev) prev.addEventListener("click", function () { go(index() - 1); });
    if (next) next.addEventListener("click", function () { go(index() + 1); });
    dots.forEach(function (d, k) { d.addEventListener("click", function () { go(k); }); });
    track.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); go(index() + 1); }
      if (e.key === "ArrowLeft") { e.preventDefault(); go(index() - 1); }
    });
    var ticking = false;
    track.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () { update(); ticking = false; });
    }, { passive: true });
    window.addEventListener("resize", update);
    update();
  });

  // 이미지 로딩 실패 시 빈 배경 유지
  document.querySelectorAll("img[data-photo]").forEach(function (img) {
    img.addEventListener("error", function () { img.style.visibility = "hidden"; });
  });

  // 체크리스트 (이 브라우저에만 저장)
  var KEY = "yonago2026-check";
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { saved = {}; }
  document.querySelectorAll(".check input[type=checkbox]").forEach(function (cb) {
    if (saved[cb.id]) cb.checked = true;
    cb.addEventListener("change", function () {
      saved[cb.id] = cb.checked;
      try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {}
      updateProgress();
    });
  });
  function updateProgress() {
    var el = document.getElementById("check-progress");
    if (!el) return;
    var all = document.querySelectorAll(".check input[type=checkbox]");
    var done = Array.prototype.filter.call(all, function (c) { return c.checked; }).length;
    el.textContent = done + " / " + all.length;
  }
  updateProgress();

  // 예산 계산기
  var budget = document.getElementById("budget");
  if (budget) {
    var rateInput = document.getElementById("rate");
    var fmt = function (n) { return "₩" + Math.round(n).toLocaleString("ko-KR"); };
    function render() {
      var rate = parseFloat(rateInput.value) || 0;
      var yen = 0;
      budget.querySelectorAll("[data-yen]").forEach(function (td) {
        var y = parseFloat(td.getAttribute("data-yen"));
        yen += y;
        td.textContent = "¥" + y.toLocaleString("ja-JP") + " · " + fmt(y * rate / 100);
      });
      var stayWon = parseFloat(document.getElementById("stay-amt").getAttribute("data-won")) || 0;
      var flight = 203491;
      var total = flight + stayWon + yen * rate / 100;
      document.getElementById("yen-sum").textContent = "¥" + yen.toLocaleString("ja-JP") + " · " + fmt(yen * rate / 100);
      document.getElementById("total").textContent = fmt(total);
      document.getElementById("total-2").textContent = fmt(total * 2);
    }
    var edited = false;
    rateInput.addEventListener("input", function () { edited = true; render(); });
    render();

    // 최신 엔화 환율 불러오기 (실패하면 기본값 유지)
    var src = document.getElementById("rate-src");
    fetch("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/jpy.json")
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var per100 = d && d.jpy && d.jpy.krw ? d.jpy.krw * 100 : 0;
        if (!per100 || edited) return;
        rateInput.value = per100.toFixed(1);
        if (src) src.textContent = d.date + " 기준 환율 (100엔 ≈ " + per100.toFixed(1) + "원) · 자동 반영";
        render();
      })
      .catch(function () {});
  }
})();
