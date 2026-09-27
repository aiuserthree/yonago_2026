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

  // 사진 갤러리 카운터
  document.querySelectorAll(".gallery").forEach(function (g) {
    var track = g.querySelector(".track");
    var count = g.querySelector(".count");
    var n = track.children.length;
    function update() {
      var i = Math.round(track.scrollLeft / track.clientWidth) + 1;
      count.textContent = Math.min(i, n) + " / " + n;
    }
    track.addEventListener("scroll", function () { window.requestAnimationFrame(update); }, { passive: true });
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
    var COMBOS = {
      tensui: { name: "텐스이", stay: 145707 },
      kikuman: { name: "기쿠만", stay: 173823 },
      fuga: { name: "후가", stay: 192248 }
    };
    var state = { combo: "kikuman" };
    try { state.combo = localStorage.getItem("yonago2026-combo") || "kikuman"; } catch (e) {}
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
      var c = COMBOS[state.combo];
      document.getElementById("stay-name").textContent = "숙소 2박 (유니버설 + " + c.name + ")";
      document.getElementById("stay-amt").textContent = fmt(c.stay);
      var flight = 203491;
      var total = flight + c.stay + yen * rate / 100;
      document.getElementById("yen-sum").textContent = "¥" + yen.toLocaleString("ja-JP") + " · " + fmt(yen * rate / 100);
      document.getElementById("total").textContent = fmt(total);
      document.getElementById("total-2").textContent = fmt(total * 2);
      budget.querySelectorAll(".seg button").forEach(function (b) {
        b.setAttribute("aria-pressed", b.getAttribute("data-combo") === state.combo ? "true" : "false");
      });
    }
    budget.querySelectorAll(".seg button").forEach(function (b) {
      b.addEventListener("click", function () {
        state.combo = b.getAttribute("data-combo");
        try { localStorage.setItem("yonago2026-combo", state.combo); } catch (e) {}
        render();
      });
    });
    rateInput.addEventListener("input", render);
    render();
  }
})();
