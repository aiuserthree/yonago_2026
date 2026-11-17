#!/usr/bin/env python3
"""요나고 2026 여행 사이트 정적 페이지 생성기.

python3 build.py 를 실행하면 루트에 *.html 파일을 다시 만든다.
내용(일정·숙소·요금)은 이 파일의 데이터만 고치면 된다.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent

FONTS = ("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@700"
         "&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans+KR:wght@400;500;600;700&display=swap")

BACK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg>')
CHEV = ('<svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>')


def page(filename, title, body, tab, back=None, header=None):
    top = ""
    if header is not None:
        left = (f'<a class="icon-btn" href="{back}" aria-label="뒤로">{BACK}</a>' if back
                else '<span class="icon-btn ghost"></span>')
        top = (f'<header class="topbar">{left}<div class="title">{escape(header)}</div>'
               '<span class="icon-btn ghost"></span></header>')
    html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#22406a">
<title>{escape(title)}</title>
<meta name="description" content="요나고 3박 4일 여행 일정 · 숙소 · 교통 · 예산 (2026.11.29–12.2)">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
</head>
<body>
<div class="app">
{top}
<main>
{body}
</main>
<footer class="foot">항공권·숙소 금액은 예약할 때 확인한 요금이에요. 실제 결제 금액은 예약 확인서를 보세요. 숙소 사진·평점 출처: Agoda.</footer>
</div>
<nav class="tabbar" data-active="{tab}" aria-label="주요 메뉴"></nav>
<script src="/assets/app.js"></script>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")


def won(n):
    return f"₩{n:,}"


# ---------------------------------------------------------------- 숙소 데이터
HOTELS = {
    "dormy": {
        "name": "도미인 익스프레스 마쓰에",
        "jp": "ドーミーインEXPRESS松江",
        "kind": "비즈니스 호텔 · 3.5성급",
        "night": "1·2박째 · 11/29(일)~12/1(화)",
        "price": 152272,  # 싱글룸 2실 1박 (1실 ₩76,136)
        "nights": 2,
        "occ": "1인 1실 × 2실",
        "room": "1인 1실 × 2실 · 싱글룸 (청소 서비스 없음, 금연) · 13㎡ · 욕조",
        "meal": "조식 포함",
        "booked": True,
        "cancel": "예약 완료 · 11/27까지 무료 취소 · 11/26 자동 결제 · 청소 없는 요금이라 2박 동안 객실 청소를 하지 않아요",
        "addr": "498-1 Asahimachi, Matsue (松江市朝日町498-1)",
        "access": "마쓰에역에서 도보 약 5분(350m) · 신오하시 상점가 바로 옆 · 이온 마쓰에점 약 850m",
        "score": 8.3, "reviews": 2479, "label": "우수",
        "bars": [("청결도", 8.7), ("서비스", 8.5), ("객실의 안락함", 8.3), ("위치", 8.2)],
        "pros": [
            "깨끗하고 생각보다 방이 넓으며 조식이 맛있다는 후기가 많아요. 조식에 가쓰카레도 나와요.",
            "밤에는 무료 라멘과 아이스크림, 아침에는 요구르트를 줘요.",
            "어메니티를 필요한 만큼 가져갈 수 있어요.",
            "마쓰에역이 가깝고 주변에 상점가와 편의시설이 모여 있어요.",
        ],
        "cons": [
            "청소 서비스 없는 요금이라 2박 동안 방 청소를 하지 않아요. 수건이나 어메니티가 더 필요하면 프런트에 말하세요.",
            "위치·편의시설 점수(8.2)는 청결도보다 조금 낮아요.",
        ],
        "photos": [
            "https://pix8.agoda.net/hotelImages/411661/0/f472edf63f0f5067817e9b9045af3222.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/411661/3279972/73231288827c5c118040a5ab65cf521c.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/411661/77851141/bb44d319d0d883e61c234b3e8eb8e6eb.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/411661/0/6b7b694f237b98a9dd07d39d83f8b0c5.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/411661/0/71553b9dfa66b0e61f9ea786da0b1143.jpeg?va=1&s=1024x",
        ],
        "agoda": "https://www.agoda.com/ko-kr/dormy-inn-express-matsue/hotel/matsue-jp.html?checkIn=2026-11-29&checkOut=2026-12-01&los=2&adults=2&rooms=2&children=0",
    },
    "washington": {
        "name": "요나고 워싱턴 호텔 플라자",
        "jp": "米子ワシントンホテルプラザ",
        "kind": "비즈니스 호텔 · 3.5성급",
        "night": "3박째 · 12/1(화)",
        "price": 108806,  # 스탠다드 싱글 2실 1박 (1실 ₩54,403)
        "nights": 1,
        "occ": "1인 1실 × 2실",
        "room": "1인 1실 × 2실 · 스탠다드 싱글 (금연) · 14㎡ · 세미더블 침대 · 욕조",
        "meal": "조식 포함",
        "booked": True,
        "cancel": "예약 완료 · 11/29까지 무료 취소 · 11/28 자동 결제",
        "addr": "125 Meiji-cho, Yonago (米子市明治町125)",
        "access": "요나고역에서 길 건너 도보 약 2분(170m) · 공항 연계버스 7번 승강장과 가까워요",
        "score": 8.1, "reviews": 3292, "label": "우수",
        "bars": [("위치", 8.9), ("서비스", 8.4), ("청결도", 8.2), ("객실의 안락함", 8.0)],
        "pros": [
            "요나고역 바로 앞이라 JR·버스 타기 편하다는 후기가 가장 많아요.",
            "수건과 침대 시트를 매일 갈아 주고, 객실과 침구가 깨끗하다는 평이 많아요.",
            "로비에서 클렌징오일·토너·로션 같은 어메니티를 챙길 수 있어요.",
            "체크인 전과 체크아웃 후에 짐을 맡아 줘요. 다이센산이 보이는 방도 있어요.",
        ],
        "cons": [
            "편의시설 점수(7.7)는 다른 항목보다 낮아요.",
        ],
        "photos": [
            "https://pix8.agoda.net/hotelImages/267440/0/3300945399aff75c170bba84c84e7adf.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/267440/3279806/871f5e3809f947e4a571459e1bdac669.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/267440/3279807/7d95953f482e6c7e815c742cfee1b28e.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/267440/0/c94d522d6361d76136180023740e7cf9.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/267440/0/ee549b859aee20a06ff8fd76d70a1352.jpeg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/267440/3279808/5aaf37640adfe383ef3daf34f7fd7f84.jpeg?va=1&ce=2&s=1024x",
        ],
        "agoda": "https://www.agoda.com/ko-kr/yonago-washington-hotel-plaza_4/hotel/yonago-jp.html?checkIn=2026-12-01&checkOut=2026-12-02&los=1&adults=2&rooms=2&children=0",
    },
}

PLAN = ("dormy", "washington")  # 1·2박째, 3박째 (예약 완료)


def stay_total(h):
    return h["price"] * h.get("nights", 1)


def img(src, alt, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<img data-photo{c} src="{escape(src)}" alt="{escape(alt)}" loading="lazy" '
            'referrerpolicy="no-referrer">')


def plan_card():
    n1, n2 = HOTELS[PLAN[0]], HOTELS[PLAN[1]]
    total = stay_total(n1) + stay_total(n2)
    return f"""
<article class="card combo pick">
  <div class="combo-top">
    <div>
      <span class="chip good">예약 완료</span>
      <h3 style="margin-top:8px">마쓰에 2박 + 요나고역 앞 1박</h3>
      <p class="small muted">앞의 두 밤은 공항에서 먼 마쓰에, 마지막 밤은 공항버스 타는 요나고역 앞</p>
    </div>
  </div>
  <div class="nights">
    <a class="night" href="/stay-{PLAN[0]}">{img(n1['photos'][0], n1['name'])}
      <div><div class="when">2박 · 11/29~12/1 · {escape(n1['meal'])}</div><div class="nm">{escape(n1['name'])}</div></div>
      <div class="p">{won(stay_total(n1))}</div></a>
    <a class="night" href="/stay-{PLAN[1]}">{img(n2['photos'][0], n2['name'])}
      <div><div class="when">1박 · 12/1 화 · {escape(n2['meal'])}</div><div class="nm">{escape(n2['name'])}</div></div>
      <div class="p">{won(stay_total(n2))}</div></a>
  </div>
  <div class="total"><span class="small muted">3박 합계 · 금연 1인실 2개 · 세금 포함<br>1인당 {won(round(total / 2))}</span><span class="amt">{won(total)}</span></div>
</article>"""


def carousel(h, cls="", tag=""):
    """사진 여러 장을 넘겨보는 캐러셀 (스와이프 · 화살표 · 점)."""
    n = len(h["photos"])
    slides = "".join(img(p, f"{h['name']} 사진 {i + 1}/{n}") for i, p in enumerate(h["photos"]))
    dots = "".join(f'<button type="button" class="dot" aria-label="{i + 1}번째 사진"></button>' for i in range(n))
    tag_html = f'<span class="tag">{escape(tag)}</span>' if tag else ""
    return f"""<div class="carousel {cls}" aria-roledescription="carousel" aria-label="{escape(h['name'])} 사진">
  <div class="track" tabindex="0">{slides}</div>{tag_html}
  <button type="button" class="nav prev" aria-label="이전 사진"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg></button>
  <button type="button" class="nav next" aria-label="다음 사진"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></button>
  <span class="count num">1 / {n}</span>
  <div class="dots">{dots}</div>
</div>"""


def stay_card(key):
    h = HOTELS[key]
    return f"""
<article class="card stay-card">
  {carousel(h, "photo", h['night'])}
  <a class="card-body" href="/stay-{key}">
    <div class="row">
      <div>
        <div class="tiny">{escape(h['kind'])}</div>
        <h3>{escape(h['name'])}</h3>
      </div>
      {CHEV}
    </div>
    <div class="row">
      <span class="score"><b>{h['score']}</b>{h['label']} · 후기 {h['reviews']:,}건</span>
      <div class="price"><div class="amt">{won(stay_total(h))}</div><div class="per">{h.get('nights', 1)}박 · {h.get('occ', '2인 1실')} · {escape(h['meal'])}</div></div>
    </div>
  </a>
</article>"""


def booking_card():
    """항공권·숙소 예약 현황을 한곳에 모은 카드."""
    d, w = HOTELS["dormy"], HOTELS["washington"]
    rows = [
        ("항공권", "에어서울 RS471/472 · 11/29~12/2 · 성인 2명",
         "직항 · <b>위탁 수하물 미포함</b> · 왕복 2명 ₩421,884 (1인 ₩210,942)",
         "<b>발권 중</b> · e-티켓을 받으면 영문 이름이 여권과 같은지 확인", None, True),
        ("1·2박 · 11/29~12/1", d["name"],
         "<b>싱글룸 (청소 서비스 없음, 금연) 2실 · 조식 포함</b> · 2박 " + won(stay_total(d)) + " (1인 " + won(stay_total(d) // 2) + ")",
         "<b>11/27까지 무료 취소 · 11/26 자동 결제</b> · 결제 카드 한도 확인", d["agoda"], True),
        ("3박 · 12/1", w["name"],
         "<b>스탠다드 싱글 (금연) 2실 · 조식 포함</b> · 1박 " + won(stay_total(w)) + " (1인 " + won(stay_total(w) // 2) + ")",
         "<b>11/29까지 무료 취소 · 11/28 자동 결제</b> · 12/1 오전에 짐부터 맡기기", w["agoda"], True),
    ]
    def status(done):
        return '<span class="chip good">예약 완료</span>' if done else '<span class="chip warn">예약 필요</span>'
    def button(url, done):
        if not url:
            return ""
        cls, text = ("btn secondary", "Agoda 숙소 페이지") if done else ("btn", "Agoda에서 예약하기")
        return f'<a class="{cls}" href="{escape(url)}" target="_blank" rel="noopener">{text}</a>'
    items = "".join(f"""
    <li class="book-row">
      <div class="row"><span class="tiny">{label}</span>{status(done)}</div>
      <strong>{name}</strong>
      <p class="small muted">{pick}</p>
      <p class="tiny">{note}</p>
      {button(url, done)}
    </li>""" for label, name, pick, note, url, done in rows)
    return f"""<article class="card card-body" id="booking">
    <div class="row"><strong>예약 현황</strong><span class="chip accent">성인 2명</span></div>
    <ol class="book-list">{items}</ol>
    <div class="note"><span class="mk">!</span><span>금액은 예약할 때 Agoda에서 확인한 요금이에요. 실제 결제 금액과 취소 기한은 예약 확인서를 기준으로 보세요.</span></div>
  </article>"""


# ---------------------------------------------------------------- 홈
home = f"""
<section class="hero">
  <svg class="mount" viewBox="0 0 200 90" aria-hidden="true"><path fill="#fff" d="M0 90 L70 20 L84 30 L100 8 L118 28 L130 22 L200 90 Z"/><path fill="#22406a" d="M92 18 L100 8 L108 19 L103 24 L100 20 L96 25 Z" opacity=".4"/></svg>
  <div class="eyebrow">SAN'IN · TOTTORI</div>
  <h1>요나고 3박 4일</h1>
  <p class="dates">2026. 11. 29 (일) — 12. 2 (수)</p>
  <div class="dday"><b data-dday>D-</b><span>에어서울 RS471 · 13:20 인천 출발</span></div>
</section>

<div class="stats">
  <div class="stat"><span class="label">항공</span><span class="value">에어서울</span><span class="tiny">직항 1시간 30분</span></div>
  <div class="stat"><span class="label">1·2박</span><span class="value">마쓰에</span><span class="tiny">도미인 익스프레스</span></div>
  <div class="stat"><span class="label">3박</span><span class="value">요나고역 앞</span><span class="tiny">워싱턴 호텔 플라자</span></div>
</div>

<section class="section">
  <div class="section-head"><h2>일정</h2><a href="/day1">자세히</a></div>
  <div class="card">
    <a class="day-link" href="/day1"><div class="day-badge"><span class="d">DAY</span><span class="n">1</span></div>
      <div><h3>도착 · 마쓰에로</h3><p>11/29 일 · 14:50 도착, 요나고역 ATM, JR로 마쓰에 도미인</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day2"><div class="day-badge"><span class="d">DAY</span><span class="n">2</span></div>
      <div><h3>가이케 바닷가 · MEGA 돈키호테</h3><p>11/30 월 · 짐은 호텔에 두고 바닷가와 쇼핑, 규코쓰 라멘</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day3"><div class="day-badge"><span class="d">DAY</span><span class="n">3</span></div>
      <div><h3>사카이미나토 요괴 마을</h3><p>12/1 화 · 요나고 호텔에 짐 맡기고 미즈키 시게루 로드, 저녁 요괴 조명</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day4"><div class="day-badge"><span class="d">DAY</span><span class="n">4</span></div>
      <div><h3>요나고역 앞 · 귀국</h3><p>12/2 수 · 여유 있는 오전, 13:35 역 앞 버스, 15:50 출발</p></div>{CHEV}</a>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>숙소</h2><a href="/stay">자세히</a></div>
  {plan_card()}
</section>

<section class="section">
  <div class="section-head"><h2>날씨와 옷차림</h2></div>
  <div class="card card-body">
    <div class="row"><span class="muted small">11/29~12/2 평년</span><span class="num">최고 14° / 최저 5~6°</span></div>
    <div class="row"><span class="muted small">하늘</span><span class="small">흐린 날이 많고 하루 해 약 3시간</span></div>
    <div class="row"><span class="muted small">1개월 예보 (10/29)</span><span class="small">평년보다 따뜻할 확률 60% · 11월 말 흐리거나 비 오는 날 많음</span></div>
    <p class="small muted">아침저녁은 5°까지 내려가고 바닷가인 가이케·사카이미나토는 바람이 차요. 겹쳐 입고, 우산과 방수 겉옷은 매일 들고 다니세요. 11/22쯤부터 주간 예보를 확인하세요. (기상청 요나고 일별 평년값 1991~2020 · 중국지방 1개월 예보)</p>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>바로가기</h2></div>
  <div class="btn-row">
    <a class="btn secondary" href="/checklist">준비물 체크</a>
    <a class="btn secondary" href="/food">먹거리</a>
  </div>
  <a class="btn" href="/stay#booking">예약 현황 보기</a>
  <a class="btn secondary" href="/budget#cash">현금 · ATM 안내</a>
</section>
"""
page("index.html", "요나고 3박 4일", home, "home")


# ---------------------------------------------------------------- 일정
def day_tabs(active):
    items = [("day1", "1 · 11/29"), ("day2", "2 · 11/30"), ("day3", "3 · 12/1"), ("day4", "4 · 12/2")]
    cur = ' aria-current="page"'
    return '<nav class="day-tabs" aria-label="날짜 선택">' + "".join(
        f'<a href="/{k}"{cur if k == active else ""}>{v}</a>' for k, v in items) + "</nav>"


def tl(time, title, text="", kind=""):
    return (f'<li class="tl {kind}"><span class="t">{time}</span><span class="dot"></span>'
            f'<div class="c"><h3>{title}</h3>{f"<p>{text}</p>" if text else ""}</div></li>')


def guide_card(gid, title, chip, steps, note, source):
    """길 안내 카드. steps: (시간, 제목, 설명[, (일본어, 뜻)], [강조])"""
    items = ""
    for st in steps:
        t, head, text = st[0], st[1], st[2]
        ph = ""
        if len(st) > 3 and st[3]:
            jp, ko = st[3]
            ph = f'<div class="phrase"><span class="jp" lang="ja">{jp}</span><span class="ko">{ko}</span></div>'
        key = " key" if len(st) > 4 and st[4] else ""
        items += (f'<li class="tl{key}"><span class="t">{t}</span><span class="dot"></span>'
                  f'<div class="c"><h3>{head}</h3><p>{text}</p>{ph}</div></li>')
    return f"""<article class="card card-body guide" id="{gid}">
    <div class="row"><strong>{title}</strong><span class="chip accent">{chip}</span></div>
    <ol class="timeline">{items}</ol>
    <div class="note"><span class="mk">!</span><span>{note}</span></div>
    <p class="tiny">근거: {source} 일본어 문장은 화면을 그대로 보여 주면 돼요.</p>
  </article>"""


GUIDE_DAY1 = guide_card(
    "airport-guide", "공항 → 요나고역 → 도미인 마쓰에 가는 길", "11/29",
    [
        ("14:50", "입국 심사 · 세관", "위탁 수하물이 없어서 짐 찾는 곳은 그냥 지나가요. 끝나면 1층 도착 로비로 나가요."),
        ("~15:40", "버스 승강장 7번 찾기", "터미널 밖 버스 승강장에서 7번을 찾아요. 모르겠으면 안내 데스크에 아래 문장을 보여 주세요.",
         ("ソウル便の連絡バスはどこですか？", "서울편 연계버스는 어디서 타나요?")),
        ("15:50", "인천 노선 연계버스 승차", "가이케 온천을 거쳐 요나고역까지 약 45분 · ¥640 현금. 일요일에도 다니고, 비행기가 늦으면 버스도 기다려요.",
         ("米子駅で降ります。", "요나고역에서 내려요."), True),
        ("16:35", "요나고역 북口 하차 → 이온 ATM", "역 앞 이온 요나고에키마에점 1층 ATM(도보 약 4분, 9:00–23:00)에서 현금 약 ¥30,000을 뽑아요."),
        ("17:00", "JR 요나고 → 마쓰에", "산인본선 마쓰에 방면 보통열차 약 30분 · ¥510. 승강장을 모르면 역무원에게 아래 문장을 보여 주세요.",
         ("松江に行く電車は何番線ですか？", "마쓰에 가는 열차는 몇 번 승강장인가요?"), True),
        ("17:40", "마쓰에역 → 도미인 걷기", "도보 약 5분(350m). 신오하시 상점가 바로 옆이에요. 길을 모르겠으면 아래 문장을 보여 주세요.",
         ("ドーミーインEXPRESS松江はどこですか？", "도미인 익스프레스 마쓰에는 어디인가요?")),
    ],
    "버스는 서울편이 결항하면 운행하지 않고, 만차면 못 탈 수 있어요. 놓치면 JR 사카이선(요나고공항역 16:12·17:03, 약 30분 · ¥240)이나 택시(약 30분 · 약 ¥5,500)로 요나고역까지 가요. 요나고→마쓰에 특급(약 20분)은 요금이 더 들어요.",
    "요나고 공항 서울편 연계버스 시간표(2026.03 게시), JR 사카이선 평일 시간표, Agoda 숙소 위치 정보(마쓰에역 350m).",
)

GUIDE_DAY2 = guide_card(
    "beach-guide", "마쓰에 → 가이케 바닷가 → 돈키호테 → 마쓰에", "11/30",
    [
        ("09:00", "JR 마쓰에 → 요나고", "산인본선 요나고 방면 약 30분 · ¥510. 짐은 도미인 방에 두고 가벼운 가방만 들고 가요.",
         ("米子に行く電車は何番線ですか？", "요나고 가는 열차는 몇 번 승강장인가요?")),
        ("09:40", "요나고역 → 가이케 온천 노선버스", "요나고역 버스 승강장에서 가이케 온천행 · 약 20분 · 약 ¥300 · 시간당 2~4편. 차내에서는 1,000엔권까지만 바꿀 수 있어요.",
         ("皆生温泉に行きますか？", "가이케 온천에 가나요?"), True),
        ("10:00", "가이케 온천 관광센터 하차 → 해변", "정류장에서 바닷가까지 걸어서 몇 분이에요. 바람이 차니 겉옷을 챙기세요."),
        ("13:30", "택시로 MEGA 돈키호테", "가이케 온천에서 약 10~15분 · 약 ¥2,000. 택시 기사에게 아래 문장을 보여 주세요.",
         ("MEGAドン・キホーテ米子店までお願いします。", "MEGA 돈키호테 요나고점으로 가 주세요."), True),
        ("16:30", "고토역 → 요나고 → 마쓰에", "돈키호테 바로 옆 JR 고토역에서 요나고까지 6분 · ¥150, 요나고에서 마쓰에까지 약 30분 · ¥510. 쇼핑 짐이 많으면 택시로 요나고역(약 10분)까지 가도 돼요."),
    ],
    "가이케선 버스 막차는 20:45쯤이에요. 사카이선(고토역)은 한 시간에 한 대꼴이니 열차 시간을 미리 확인하세요. 저녁 고토 발 요나고행: 19:57 · 20:59 · 22:10 (평일)",
    "요나고역↔가이케 온천 버스 안내, JR 사카이선 평일 시간표, MEGA 돈키호테 요나고점 안내.",
)

GUIDE_DAY3 = guide_card(
    "yokai-guide", "도미인 → 워싱턴 호텔(짐) → 사카이미나토", "12/1",
    [
        ("10:30", "JR 마쓰에 → 요나고", "체크아웃하고 캐리어를 들고 요나고로 가요. 약 30분 · ¥510."),
        ("11:05", "워싱턴 호텔에 짐 맡기기", "요나고역에서 길 건너 도보 약 2분. 체크인 전이라 프런트에 짐만 맡겨요.",
         ("チェックインまで荷物を預かってください。", "체크인 전까지 짐을 맡아 주세요."), True),
        ("11:34", "JR 사카이선 (0번 승강장)", "요나고역 0번 승강장에서 사카이미나토행 · 약 50분 · ¥330. 요괴 그림 열차가 다녀요.",
         ("境港行きはどこから乗りますか？", "사카이미나토행은 어디서 타나요?"), True),
        ("12:23", "사카이미나토역 도착", "역 앞부터 미즈키 시게루 로드가 시작돼요."),
        ("저녁", "사카이미나토 → 요나고", "약 50분 · ¥330. 열차는 한 시간에 1~2대라 역에서 시간을 먼저 확인하세요."),
    ],
    "11:34를 놓치면 다음 열차는 12:37(→13:25)이에요. 사카이미나토 수산물 직판센터는 화요일 휴무예요.",
    "JR 서일본 사카이선 평일 시간표, Agoda 숙소 위치 정보(요나고역 170m), 돗토리현 수산물 직판센터 안내.",
)

GUIDE_DAY4 = guide_card(
    "airport-return-guide", "요나고역 → 공항 가는 길", "12/2",
    [
        ("13:20", "호텔에서 짐 찾기", "체크아웃 때 맡겨 둔 짐을 찾아요."),
        ("13:25", "요나고역 북쪽 출구 7번 승강장", "호텔에서 도보 약 2분. 버스 승강장 7번에서 기다려요. 못 찾겠으면 아래 문장을 보여 주세요.",
         ("ソウル便の連絡バスの乗り場はどこですか？", "서울편 연계버스 타는 곳이 어디인가요?")),
        ("13:35", "인천 노선 연계버스 승차", "가이케 온천을 거쳐 공항까지 약 45분 · ¥640 현금. 탈 때 아래 문장으로 확인하세요.",
         ("米子空港まで行きますか？", "요나고 공항까지 가나요?"), True),
        ("14:20", "요나고 공항 도착", "에어서울 카운터에서 체크인하고 출국 수속을 해요. 남은 엔화는 공항 매점·면세점에서 써요.", None, True),
        ("15:50", "RS472 요나고 출발", "17:40 인천 제2터미널 도착"),
    ],
    "버스를 놓치면 JR 사카이선 요나고역 13:38 열차로 요나고공항역까지 약 30분(¥240), 역에서 터미널까지 도보 약 5분이에요. 택시는 약 30분 · 약 ¥5,500.",
    "요나고 공항 서울편 연계버스 시간표(2026.03 게시), JR 사카이선 평일 시간표, 요나고 공항 택시·열차 안내.",
)


def today_stay(key, label):
    h = HOTELS[key]
    return f"""<a class="card stay-card" href="/stay-{key}" style="display:grid;grid-template-columns:96px 1fr;align-items:center">
    <div style="height:96px">{img(h['photos'][0], h['name'])}</div>
    <div class="card-body"><div class="tiny">{label}</div><strong>{escape(h['name'])}</strong><span class="small muted">{escape(h['meal'])} · {h.get('nights', 1)}박 {won(stay_total(h))} (1인 {won(stay_total(h) // 2)})</span></div>
  </a>"""


day1 = day_tabs("day1") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 1 · 11월 29일 일요일</div><h2 style="font-size:24px;margin-top:4px">도착해서 마쓰에로</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("11:00", "인천공항 제2터미널 도착", "에어서울은 2025년 9월부터 제2터미널이에요. E1~E10 카운터에서 체크인. 여권 유효기간을 확인하세요.")}
    {tl("13:20", "RS471 인천 출발", "비행 1시간 30분", "key")}
    {tl("14:50", "요나고 기타로 공항 도착", "입국 심사 후 7번 승강장으로. 버스비는 한국에서 바꿔 온 엔화 현금으로")}
    {tl("15:50", "인천 노선 연계버스 탑승", "현지 이름: ソウル便連絡バス · 공항 7번 승강장 → 요나고역 북口 16:35 · ¥640 · 현금", "move")}
    {tl("16:40", "이온 ATM에서 현금 인출", "요나고역 앞 이온 1층 ATM 코너(도보 약 4분, 9:00–23:00). 남은 일정 현금 약 ¥30,000", "key")}
    {tl("17:00", "JR 요나고 → 마쓰에", "산인본선 보통열차 약 30분 · ¥510", "move")}
    {tl("17:40", "도미인 익스프레스 마쓰에 체크인", "마쓰에역에서 도보 약 5분. 싱글룸 2실 · 2박 · 조식 포함", "key")}
    {tl("18:30", "마쓰에역 주변 저녁", "신오하시 상점가와 역 주변 식당. 시마네 명물 이즈모 소바도 좋아요")}
    {tl("21:30", "도미인 무료 야식 라멘", "밤에 무료 라멘과 아이스크림을 줘요. 시간은 체크인 때 확인하세요")}
  </ol>
  </div>
  {GUIDE_DAY1}
  {today_stay("dormy", "오늘부터 2박 · 싱글룸 2실")}
</section>
"""
page("day1.html", "요나고 DAY 1", day1, "plan", back="/", header="일정")

day2 = day_tabs("day2") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 2 · 11월 30일 월요일</div><h2 style="font-size:24px;margin-top:4px">가이케 바닷가와 MEGA 돈키호테</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:30", "도미인 조식", "가쓰카레도 나와요")}
    {tl("09:00", "JR 마쓰에 → 요나고", "약 30분 · ¥510. 캐리어는 호텔 방에 두고 가요", "move")}
    {tl("09:40", "요나고역 → 가이케 온천 버스", "노선버스 약 20분 · 약 ¥300", "move")}
    {tl("10:00", "가이케 해변 산책", "온천 마을 바로 앞 바닷가. 맑으면 다이센산이 보여요", "key")}
    {tl("12:00", "가이케에서 점심", "오션 레스토랑(10:00–24:00, 연중무휴) 등. 먹거리 페이지 참고")}
    {tl("13:30", "택시 → MEGA 돈키호테", "약 10~15분 · 약 ¥2,000", "move")}
    {tl("14:00", "MEGA 돈키호테 요나고점", "9:00–24:00, 연중무휴. 면세 가능하니 여권을 챙기세요", "key")}
    {tl("16:30", "JR 고토 → 요나고", "사카이선 6분 · ¥150. 짐이 많으면 택시 약 10분", "move")}
    {tl("17:00", "저녁: 규코쓰(소뼈) 라멘", "역 앞 라멘 야마토(ラーメン大和), 한 그릇 ¥550 (월요일 영업)")}
    {tl("18:00", "JR 요나고 → 마쓰에", "약 30분 · ¥510", "move")}
    {tl("19:00", "도미인에서 쉬기", "쇼핑한 짐 정리. 밤에는 무료 야식 라멘")}
  </ol>
  </div>
  {GUIDE_DAY2}
  <div class="card card-body">
    <div class="row"><strong>MEGA 돈키호테 요나고점</strong><span class="chip accent">쇼핑</span></div>
    <dl class="kv">
      <dt>위치</dt><dd>米子市米原2丁目1-1 · JR 고토(後藤)역 바로 옆</dd>
      <dt>영업</dt><dd>9:00–24:00 · 연중무휴</dd>
      <dt>면세</dt><dd>가능 (여권 필요)</dd>
      <dt>결제</dt><dd>신용카드, 은련, ICOCA·Suica 등 교통카드</dd>
      <dt>가는 법</dt><dd>가이케 온천에서 택시 약 10~15분 · 요나고역에서 JR 사카이선 6분 ¥150</dd>
    </dl>
    <p class="tiny">사카이선은 한 시간에 한 대꼴이에요. 저녁 고토 발 요나고행 19:57·20:59·22:10 (평일)</p>
  </div>
  {today_stay("dormy", "오늘 숙소 · 2박째")}
</section>
"""
page("day2.html", "요나고 DAY 2", day2, "plan", back="/", header="일정")

day3 = day_tabs("day3") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 3 · 12월 1일 화요일</div><h2 style="font-size:24px;margin-top:4px">요괴 마을 사카이미나토</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:30", "도미인 조식", "")}
    {tl("10:00", "체크아웃", "캐리어를 들고 마쓰에역으로 (도보 약 5분)")}
    {tl("10:30", "JR 마쓰에 → 요나고", "약 30분 · ¥510", "move")}
    {tl("11:05", "워싱턴 호텔에 짐 맡기기", "요나고역에서 길 건너 도보 약 2분", "key")}
    {tl("11:34", "JR 요나고 → 사카이미나토", "0번 승강장 · 12:23 도착 · ¥330. 요괴 그림 열차", "move")}
    {tl("12:30", "항구 마을 점심", "해산물 덮밥 · 회전초밥. 수산물 직판센터는 화요일 휴무")}
    {tl("13:30", "미즈키 시게루 로드", "요괴 동상 170여 개가 늘어선 역 앞 거리. 천천히 걸으며 사진 찍기", "key")}
    {tl("14:30", "미즈키 시게루 기념관", "9:30–17:00 (입장 16:30까지), 일반 ¥1,000")}
    {tl("16:50", "해 질 녘 요괴 거리", "해가 지면 길바닥에 요괴 그림자 조명이 켜져요", "key")}
    {tl("17:30", "JR 사카이미나토 → 요나고", "약 50분 · ¥330. 열차 시간은 역에서 확인", "move")}
    {tl("18:30", "워싱턴 호텔 체크인", "스탠다드 싱글 2실 · 조식 포함", "key")}
    {tl("19:00", "역 앞 저녁", "대게 이자카야 다이헤이키나 라멘. 먹거리 페이지 참고")}
  </ol>
  </div>
  {GUIDE_DAY3}
  {today_stay("washington", "오늘 숙소 · 1박 · 싱글룸 2실")}
</section>
"""
page("day3.html", "요나고 DAY 3", day3, "plan", back="/", header="일정")

day4 = day_tabs("day4") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 4 · 12월 2일 수요일</div><h2 style="font-size:24px;margin-top:4px">요나고역 앞에서 여유 있게, 공항으로</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:30", "워싱턴 호텔 조식", "")}
    {tl("09:00", "자유 시간", "역 앞 이온 구경, 또는 JR 6분 거리 MEGA 돈키호테 한 번 더")}
    {tl("11:00", "체크아웃 · 짐 맡기기", "체크아웃하고 프런트에 짐을 맡겨요", "key")}
    {tl("12:00", "점심: 규코쓰 라멘", "라멘 야마토 또는 니쿠곳초 요나고역 앞점 (둘 다 수요일 영업)")}
    {tl("13:20", "호텔에서 짐 찾기", "")}
    {tl("13:35", "인천 노선 연계버스 탑승", "현지 이름: ソウル便連絡バス · 요나고역 북口 7번 → 공항 14:20 · ¥640 · 현금", "move")}
    {tl("14:20", "요나고 공항 도착", "출국 수속, 기념품")}
    {tl("15:50", "RS472 요나고 출발", "", "key")}
    {tl("17:40", "인천 제2터미널 도착", "")}
  </ol>
  </div>
  {GUIDE_DAY4}
  <div class="note info"><span class="mk">i</span><span>13:35 버스를 놓쳐도 13:38 JR 열차가 있어요. 체크아웃 시간은 체크인 때 확인하세요.</span></div>
</section>
"""
page("day4.html", "요나고 DAY 4", day4, "plan", back="/", header="일정")


# ---------------------------------------------------------------- 숙소 목록
stay = f"""
{booking_card()}
<section class="section">
  <div><div class="eyebrow">숙소 예약 완료 · 마쓰에 2박 + 요나고역 앞 1박</div><h2 style="font-size:24px;margin-top:4px">예약한 숙소</h2>
  <p class="small muted" style="margin-top:6px">성인 2명 · 두 곳 모두 금연 1인실 2개 · 조식 포함 · 세금 포함 · 실제 금액은 예약 확인서 기준</p></div>
  {plan_card()}
  <div class="list">{''.join(stay_card(k) for k in PLAN)}</div>
</section>
"""
page("stay.html", "요나고 숙소", stay, "stay", header="숙소")


def hotel_page(key):
    h = HOTELS[key]
    bars = "".join(
        f'<div class="bar"><span>{n}</span><span class="track"><span class="fill" style="width:{v * 10:.0f}%;display:block"></span></span><span class="v">{v:.1f}</span></div>'
        for n, v in h["bars"])
    pros = "".join(f'<li class="plus"><span class="mk">+</span><span>{escape(p)}</span></li>' for p in h["pros"])
    cons = "".join(f'<li class="minus"><span class="mk">−</span><span>{escape(p)}</span></li>' for p in h["cons"])
    body = f"""
<div>
  {carousel(h, "gallery")}
  <p class="credit">사진: <a href="{escape(h['agoda'])}" target="_blank" rel="noopener">Agoda 숙소 페이지</a></p>
</div>
<section class="section">
  <div>
    <div class="chips"><span class="chip sea">{escape(h['night'])}</span><span class="chip">{escape(h['kind'])}</span></div>
    <h2 style="font-size:24px;margin-top:10px">{escape(h['name'])}</h2>
    <p class="small muted">{escape(h['jp'])}</p>
  </div>
  <div class="card card-body">
    <div class="row">
      <div><div class="tiny">{h.get('nights', 1)}박 · {h.get('occ', '2인 1실')} · 세금 포함</div><div class="num" style="font-size:26px;font-weight:600">{won(stay_total(h))}</div><div class="tiny">{'1박 ' + won(h['price']) + (' (2실)' if h.get('occ') else '') + ' · ' if h.get('nights', 1) > 1 else ''}1인당 약 {won(round(stay_total(h) / 2))}</div></div>
      <span class="chip good">{escape(h['meal'])}</span>
    </div>
    <dl class="kv">
      <dt>객실</dt><dd>{escape(h['room'])}</dd>
      <dt>{"예약" if h.get("booked") else "취소"}</dt><dd>{escape(h['cancel'])}</dd>
      <dt>위치</dt><dd>{escape(h['access'])}</dd>
      <dt>주소</dt><dd>{escape(h['addr'])}</dd>
    </dl>
  </div>
</section>
<section class="section">
  <div class="section-head"><h2>이용 후기</h2><span class="tiny">Agoda {h['reviews']:,}건</span></div>
  <div class="card card-body" style="gap:16px">
    <div class="big-score"><span class="s">{h['score']}</span><div><strong>{h['label']}</strong><p class="small muted">10점 만점 · 투숙객 평점</p></div></div>
    <div class="bars">{bars}</div>
  </div>
  <div class="card card-body">
    <strong>투숙객들이 말하는 장점</strong>
    <ul class="pros">{pros}</ul>
    <strong style="margin-top:6px">알아둘 점</strong>
    <ul class="pros">{cons}</ul>
    <p class="tiny">한국인 투숙객 후기를 요약한 내용이에요.</p>
  </div>
</section>
<a class="btn" href="{escape(h['agoda'])}" target="_blank" rel="noopener">{"Agoda 숙소 페이지" if h.get("booked") else "Agoda에서 요금 보기"}</a>
"""
    page(f"stay-{key}.html", h["name"], body, "stay", back="/stay", header="숙소 상세")


for k in HOTELS:
    hotel_page(k)


# ---------------------------------------------------------------- 교통
transport = """
<section class="section">
  <div class="section-head"><h2>항공권</h2><span class="chip sea">에어서울 · 월수목금일 운항</span></div>
  <div class="card card-body" style="gap:14px">
    <div class="tiny">가는 편 · 11/29 일 · RS471</div>
    <div class="boarding">
      <div><div class="code">ICN</div><div class="time">13:20</div><div class="city">인천 제2터미널</div></div>
      <div class="mid"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 15.5 13.5 12V5.5a1.5 1.5 0 0 0-3 0V12L3 15.5V17l7.5-2v3.5L8.5 20v1.2l3.5-.9 3.5.9V20l-2-1.5V15l7.5 2z" transform="rotate(90 12 12)"/></svg><span>1시간 30분</span></div>
      <div class="end"><div class="code">YGJ</div><div class="time">14:50</div><div class="city">요나고 기타로</div></div>
    </div>
    <div class="perf"></div>
    <div class="tiny">오는 편 · 12/2 수 · RS472</div>
    <div class="boarding">
      <div><div class="code">YGJ</div><div class="time">15:50</div><div class="city">요나고 기타로</div></div>
      <div class="mid"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 15.5 13.5 12V5.5a1.5 1.5 0 0 0-3 0V12L3 15.5V17l7.5-2v3.5L8.5 20v1.2l3.5-.9 3.5.9V20l-2-1.5V15l7.5 2z" transform="rotate(90 12 12)"/></svg><span>1시간 50분</span></div>
      <div class="end"><div class="code">ICN</div><div class="time">17:40</div><div class="city">인천 제2터미널</div></div>
    </div>
    <div class="perf"></div>
    <div class="row"><span class="small muted"><b>예약 완료 · 발권 중</b> · 왕복 2명 · 세금 포함<br>1인 ₩210,942 (예약 전 조회 요금)</span><span class="num" style="font-size:20px;font-weight:600">₩421,884</span></div>
    <a class="btn secondary" href="/stay#booking">예약 현황 보기</a>
    <p class="tiny"><b>위탁 수하물 미포함 요금</b>으로 예약했어요(기내 수하물만). 기내 수하물 무게·크기 규정은 에어서울에서 확인하세요.</p>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>공항 ↔ 시내</h2></div>
  <a class="card card-body" href="/day1#airport-guide" style="text-decoration:none">
    <div class="row"><strong>공항 → 요나고역 → 도미인 마쓰에</strong><svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></div>
    <p class="small muted">7번 승강장 연계버스, 요나고역 ATM, JR 마쓰에까지 단계별 안내와 보여 주기용 일본어 문장</p>
  </a>
  <a class="card card-body" href="/day2#beach-guide" style="text-decoration:none">
    <div class="row"><strong>마쓰에 → 가이케 바닷가 → 돈키호테</strong><svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></div>
    <p class="small muted">JR로 요나고, 버스로 가이케, 택시로 돈키호테, 다시 마쓰에까지</p>
  </a>
  <a class="card card-body" href="/day3#yokai-guide" style="text-decoration:none">
    <div class="row"><strong>도미인 → 워싱턴 호텔(짐) → 사카이미나토</strong><svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></div>
    <p class="small muted">요나고 호텔에 짐 맡기고 11:34 사카이선 0번 승강장</p>
  </a>
  <a class="card card-body" href="/day4#airport-return-guide" style="text-decoration:none">
    <div class="row"><strong>요나고역 → 공항 가는 길</strong><svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></div>
    <p class="small muted">북쪽 출구 7번 승강장 13:35 연계버스, 놓쳤을 때 JR 13:38</p>
  </a>
  <div class="card card-body">
    <div class="row"><strong>인천 노선 연계버스</strong><span class="chip accent">추천</span></div>
    <p class="small muted">현지 정식 이름은 국제선(서울편) 연락버스(国際線 ソウル便連絡バス)예요. 에어서울 인천↔요나고 편 시간에 맞춰 히노마루 버스가 운행해요. 정류장 안내판에서는 「ソウル便」을 찾으세요.</p>
    <dl class="kv">
      <dt>도착일</dt><dd>공항 7번 15:50 → 가이케 온천 16:15 → <b>요나고역 북口 16:35 하차</b></dd>
      <dt>귀국일</dt><dd><b>요나고역 북口 7번 13:35 승차</b> → 가이케 온천 13:55 → 공항 14:20</dd>
      <dt>요금</dt><dd>요나고역 ↔ 공항 ¥640 · 현금 (도착일 ¥640 + 귀국일 ¥640)</dd>
    </dl>
    <p class="tiny">요나고 공항 공식 시간표 기준. 인천 노선 항공편이 결항하면 운행하지 않고, 만차면 못 탈 수 있어요.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>JR 사카이선 열차</strong><span class="chip">약 30분 · ¥240</span></div>
    <p class="small muted">터미널에서 JR 요나고공항역까지 도보 약 5분. 도착일 오후 요나고행은 14:53, 16:12, 17:03, 17:52 (평일). 14:53은 입국 심사 때문에 타기 어려워요.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>택시</strong><span class="chip">대략</span></div>
    <p class="small muted">공항 → 요나고역 약 30분 · 약 ¥5,500 (공항 공식 안내)<br>가이케 온천 → MEGA 돈키호테 약 10~15분 · 약 ¥2,000<br>돈키호테 → 요나고역 약 10분<br>공항 택시는 대수가 적어 미리 예약을 권해요. 日ノ丸ハイヤー 0859-22-3231</p>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>시내 이동</h2></div>
  <div class="card">
    <div class="table-wrap" style="padding:4px 16px">
    <table class="money">
      <tr><td>요나고 ↔ 마쓰에 (JR 산인본선 보통)<div class="tiny">약 30분 · 11/29, 11/30 왕복, 12/1</div></td><td>¥510</td></tr>
      <tr><td>요나고역 → 가이케 온천 (가이케선 버스)<div class="tiny">약 20분 · 평일 시간당 2–4편 · 막차 20:45</div></td><td>약 ¥300</td></tr>
      <tr><td>가이케 온천 → MEGA 돈키호테 (택시)<div class="tiny">약 10~15분</div></td><td>약 ¥2,000</td></tr>
      <tr><td>고토 → 요나고 (JR 사카이선)<div class="tiny">6분 · 돈키호테 바로 옆 역</div></td><td>¥150</td></tr>
      <tr><td>요나고 ↔ 사카이미나토 (JR 사카이선)<div class="tiny">약 50분 · 요괴 그림 열차 · 0번 승강장</div></td><td>¥330</td></tr>
    </table>
    </div>
  </div>
  <div class="note info"><span class="mk">i</span><span>버스는 현금 위주예요. 차내에서는 1,000엔권까지만 바꿀 수 있으니 동전과 천 엔짜리를 넉넉히 준비하세요.</span></div>
</section>
"""
page("transport.html", "요나고 교통", transport, "move", header="교통")


# ---------------------------------------------------------------- 예산
budget = """
<section class="section" id="budget">
  <div><div class="eyebrow">성인 2명 기준</div><h2 style="font-size:24px;margin-top:4px">여행 예산</h2></div>
  <div class="card card-body">
    <label class="row small" for="rate"><span class="muted">환율 (100엔당 원)</span>
      <input id="rate" type="number" inputmode="decimal" value="854.4" min="500" max="2000" step="0.1"
        style="width:96px;height:36px;border-radius:10px;border:1px solid var(--line);background:var(--surface-2);color:var(--ink);padding:0 10px;font:600 15px var(--num);text-align:right"></label>
    <p class="tiny" id="rate-src">2026-11-09 기준 환율 (100엔 ≈ 854.4원)</p>
  </div>
  <div class="card">
    <div class="table-wrap" style="padding:4px 16px">
    <table class="money">
      <tr><td>항공권 왕복 2명 · 예약 완료 (에어서울 · 위탁 수하물 미포함)</td><td id="flight-amt" data-won="421884">₩421,884</td></tr>
      <tr><td>숙소 3박 · 예약 완료 (도미인 마쓰에 싱글룸 2실 2박 ₩304,544 + 워싱턴 스탠다드 싱글 2실 1박 ₩108,806 · 모두 조식 포함)<div class="tiny">1인 ₩206,675 (도미인 ₩152,272 + 워싱턴 ₩54,403)</div></td><td id="stay-amt" data-won="413350">₩413,350</td></tr>
      <tr><td class="muted">예약 소계 (항공권 + 숙소)<div class="tiny">1인 ₩417,617 · 남은 결제: 11/26 도미인 ₩304,544 · 11/28 워싱턴 ₩108,806 자동 결제</div></td><td class="muted">₩835,234</td></tr>
      <tr><td>공항 연계버스 2명 (도착 ¥640 + 귀국 ¥640)</td><td data-yen="2560">-</td></tr>
      <tr><td>JR 요나고 → 마쓰에 2명 (11/29)</td><td data-yen="1020">-</td></tr>
      <tr><td>JR 마쓰에 ↔ 요나고 왕복 2명 (11/30)</td><td data-yen="2040">-</td></tr>
      <tr><td>요나고역 → 가이케 온천 버스 2명</td><td data-yen="600">-</td></tr>
      <tr><td>가이케 → MEGA 돈키호테 택시 (약)</td><td data-yen="2000">-</td></tr>
      <tr><td>JR 고토 → 요나고 2명</td><td data-yen="300">-</td></tr>
      <tr><td>JR 마쓰에 → 요나고 2명 (12/1)</td><td data-yen="1020">-</td></tr>
      <tr><td>사카이미나토 JR 왕복 2명</td><td data-yen="1320">-</td></tr>
      <tr><td>미즈키 시게루 기념관 2명</td><td data-yen="2000">-</td></tr>
      <tr><td>저녁 3번 2명 (1인 1끼 약 ¥3,000)</td><td data-yen="18000">-</td></tr>
      <tr><td>점심 3번 · 간식 2명 (1인 1끼 약 ¥1,500)</td><td data-yen="14000">-</td></tr>
      <tr><td class="muted">현지 지출 합계</td><td id="yen-sum" class="muted">-</td></tr>
      <tr class="sum"><td>2명 합계</td><td id="total">-</td></tr>
      <tr><td class="muted">1인당</td><td id="total-2" class="muted">-</td></tr>
    </table>
    </div>
  </div>

<section class="section" id="cash">
  <div class="section-head"><h2>현금 · ATM</h2><span class="chip sea">2명 기준</span></div>
  <div class="card">
    <div class="table-wrap" style="padding:4px 16px">
    <table class="money">
      <tr><td><b>꼭 현금</b><div class="tiny">인천 노선 연계버스 (도착 ¥640 + 귀국 ¥640) · 공항 시간표에 "기본 현금"</div></td><td data-cash-yen="2560">¥2,560 · ₩21,873</td></tr>
      <tr><td><b>현금 또는 ICOCA</b><div class="tiny">JR(마쓰에·고토·사카이미나토), 가이케 노선버스 · 트래블월렛 카드로는 못 내요</div></td><td data-cash-yen="6300">¥6,300 · ₩53,827</td></tr>
      <tr><td><b>카드 확인 못 함 → 현금 준비</b><div class="tiny">미즈키 시게루 기념관 입장료 · 가이케 → 돈키호테 택시</div></td><td data-cash-yen="4000">¥4,000 · ₩34,176</td></tr>
      <tr><td><b>일부 현금</b><div class="tiny">점심 · 저녁 · 라멘 · 간식 (작은 식당은 현금만 받는 곳이 많아요)</div></td><td data-cash-yen="20000" data-approx="1">약 ¥20,000 · ₩170,880</td></tr>
      <tr class="sum"><td>준비할 현금<div class="tiny">필요 ¥32,860(<span data-won-of="32860">약 ₩280,756</span>) + 여유 · 한국 환전 ¥5,000 + ATM 인출 ¥30,000</div></td><td data-cash-yen="35000">¥35,000 · ₩299,040</td></tr>
    </table>
    </div>
    <p class="tiny" style="padding:0 16px 12px">원화는 위 예산의 환율로 계산해요. 환율을 바꾸면 같이 바뀌어요.</p>
  </div>
  <div class="card card-body">
    <strong>카드로 내도 되는 곳</strong>
    <p class="small muted">MEGA 돈키호테(신용카드·은련), 편의점, 이온. 숙소는 Agoda에서 자동 결제돼요(도미인 11/26, 워싱턴 11/28). 체인 식당은 카드가 되는 곳이 많지만 소액 현금은 들고 다니세요.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>이온은행 ATM (트래블월렛)</strong><span class="chip good">해외 카드 가능</span></div>
    <dl class="kv">
      <dt>추천</dt><dd><b>이온 요나고에키마에점 1층 ATM 코너</b> (米子市末広町311)</dd>
      <dt>시간</dt><dd>9:00–23:00</dd>
      <dt>거리</dt><dd>요나고역에서 도보 약 4분(280m) · 첫날 버스에서 내리자마자 들러요</dd>
      <dt>다른 곳</dt><dd>이온 마쓰에점(9:00–22:00, 도미인에서 약 850m) · JU 요나고 다카시마야(米子市角盤町1-30)</dd>
    </dl>
    <p class="tiny">공항과 가이케 온천에는 이온은행 ATM이 없어요. 공항 1층 세븐일레븐에 세븐은행 ATM이 있지만 수수료가 붙을 수 있어요. 트래블월렛 수수료는 출발 전에 앱에서 확인하세요.</p>
  </div>
  <div class="card card-body">
    <strong>인출 계획</strong>
    <ol class="timeline">
      <li class="tl key"><span class="t">출발 전</span><span class="dot"></span><div class="c"><h3>한국에서 엔화 ¥5,000 환전 (<span data-won-of="5000">약 ₩42,720</span>)</h3><p>첫날 공항 연계버스(2명 ¥1,280)와 비상금. 공항에는 이온 ATM이 없어요.</p></div></li>
      <li class="tl key"><span class="t">11/29</span><span class="dot"></span><div class="c"><h3>16:40 이온 요나고에키마에점 ATM</h3><p>연계버스로 요나고역에 내리면 바로 들러서 약 ¥30,000(<span data-won-of="30000">약 ₩256,320</span>) 인출. 일요일에도 열어요. 천 엔 단위로 뽑으면 1,000엔권이 섞여 나와 버스 요금 내기 편해요.</p></div></li>
      <li class="tl"><span class="t">이후</span><span class="dot"></span><div class="c"><h3>부족하면 이온 마쓰에점 · 요나고 같은 ATM</h3><p>마쓰에에서는 도미인 근처 이온 마쓰에점, 12/1 이후에는 요나고역 앞 이온. 1만 엔권은 돈키호테·편의점에서 깨 두세요.</p></div></li>
    </ol>
  </div>
  <div class="note info"><span class="mk">i</span><span>ICOCA: 요나고 일대 JR과 노선버스(2026년 3월부터)에서 쓸 수 있고 운임은 현금과 같아요. 사려면 요나고역에서 현금으로 사요(보통 ¥2,000, 보증금 ¥500 포함). 이번 일정은 현금만으로도 충분해요.</span></div>
</section>
  <p class="tiny">숙소는 조식만 포함이라 점심·저녁 식비를 넣었어요. 대게 코스처럼 비싼 식사를 하면 더 들어요. 항공권·숙소는 예약할 때 확인한 요금이라 실제 결제 금액과 조금 다를 수 있어요. 환율은 페이지를 열 때 최신값으로 바뀌고, 직접 고쳐 넣을 수도 있어요.</p>
</section>
"""
page("budget.html", "요나고 예산", budget, "money", header="예산")


# ---------------------------------------------------------------- 먹거리
food = """
<section class="section">
  <div><div class="eyebrow">요나고·마쓰에에서 먹을 것</div><h2 style="font-size:24px;margin-top:4px">규코쓰 라멘과 대게</h2></div>
  <div class="section-head" style="margin-top:4px"><h2>마쓰에 (첫째·둘째 날 밤)</h2></div>
  <div class="card card-body">
    <div class="row"><strong>도미인 무료 야식 라멘</strong><span class="chip good">무료</span></div>
    <p class="small muted">도미인에서 밤에 라멘과 아이스크림을 무료로 줘요. 시간은 체크인 때 확인하세요. 저녁은 신오하시 상점가와 마쓰에역 주변 식당에서 먹어요.</p>
  </div>
  <div class="section-head" style="margin-top:8px"><h2>요나고역 앞 (둘째 날 저녁 ~ 넷째 날)</h2></div>
  <div class="card card-body">
    <div class="row"><strong>라멘 야마토</strong><span class="chip">ラーメン大和</span></div>
    <p class="small muted">요나고의 명물 규코쓰(소뼈) 라멘. 역 앞 야요이초. 한 그릇 ¥550, 11:00–22:45, 일요일 휴무라 11/30(월) 저녁이나 12/2(수) 점심에 가기 좋아요.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>라멘 반라이</strong><span class="chip">ラーメンばんらい</span></div>
    <p class="small muted">요나고역 도보 2분. 간장·소금 규코쓰 라멘 약 ¥650 (가격 변동 가능).</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>니쿠곳초 요나고역앞점</strong><span class="chip">肉ごっつお</span></div>
    <p class="small muted">규코쓰 라멘(하루 100그릇 한정)과 스테이크 덮밥. 11:00–15:00, 17:00–22:00, 일요일 휴무.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>다이헤이키</strong><span class="chip accent">대게</span></div>
    <p class="small muted">역 도보 3분 이자카야(太平記). 마쓰바가니 5품 코스 ¥9,800, 일반 코스 ¥3,300부터. 17:00–24:00, 연중무휴. 12/1(화) 저녁에 좋아요.</p>
  </div>
  <div class="section-head" style="margin-top:8px"><h2>가이케 온천가 (둘째 날 점심)</h2></div>
  <p class="small muted">11/30(월) 낮에 들러요. 아래 이자카야들은 저녁 영업이라 점심은 오션 레스토랑이 편해요. 영업 정보는 바뀔 수 있어요.</p>
  <div class="card card-body">
    <div class="row"><strong>오션 레스토랑</strong><span class="chip">연중무휴</span></div>
    <p class="small muted">당일치기 온천 시설 안 식당. 10:00–24:00, 산인 지역 식재료 요리.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>이자카야 엔야</strong><span class="chip">エンヤ</span></div>
    <p class="small muted">현지인에게도 인기 있는 이자카야. 메뉴가 많고 가격이 부담 없어요. 17:00–23:00, 베이사이드 스퀘어 가이케 호텔 안.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>쇼쿠사이 슈</strong><span class="chip accent">대게</span></div>
    <p class="small muted">食彩 シュウ. 매일 들여오는 해산물 창작 일식, 겨울엔 게 요리. 17:00–23:00, 일요일·첫째·셋째 월요일 휴무.</p>
  </div>
  <div class="section-head" style="margin-top:8px"><h2>사카이미나토 (셋째 날 점심)</h2></div>
  <p class="small muted">항구 마을이라 해산물 덮밥과 회전초밥 집이 많아요. 수산물 직판센터는 화요일 휴무라 12/1에는 쉬어요.</p>
  <div class="note info"><span class="mk">i</span><span>마쓰바가니(대게) 시즌은 2026년 11월 6일부터 2027년 3월 20일까지예요.</span></div>
</section>
"""
page("food.html", "요나고 먹거리", food, "home", back="/", header="먹거리")


# ---------------------------------------------------------------- 체크리스트
ITEMS = [
    ("여권 (유효기간 6개월 이상 권장)", "p1"), ("항공권 e-티켓 발권 확인 · 인천 제2터미널", "p2"), ("숙소 예약 확인서 2곳 (도미인 · 워싱턴)", "p3"),
    ("도미인 11/26 자동 결제 · 11/27까지 무료 취소", "p22"), ("워싱턴 11/28 자동 결제 · 결제 카드 한도 확인", "p23"),
    ("Visit Japan Web 입국 정보 등록", "p4"), ("한국에서 엔화 ¥5,000 환전 (첫날 버스·비상금)", "p5"), ("트래블월렛 이온은행 ATM 수수료 확인", "p16"),
    ("해외 결제 카드", "p6"), ("돈키호테 쇼핑 목록 · 면세용 여권", "p13"), ("기내 수하물 규정 확인 (위탁 수하물 없음)", "p14"), ("eSIM 또는 로밍", "p7"), ("110V 돼지코 어댑터", "p8"),
    ("방수 되는 겉옷 (바람막이·얇은 패딩) · 접이식 우산", "p9"), ("겹쳐 입을 니트·긴팔 (아침 5°, 낮 14°)", "p19"), ("젖어도 되는 편한 신발 · 여벌 양말", "p20"),
    ("도미인은 청소 없는 요금 · 수건·어메니티는 프런트에 요청", "p24"),
    ("연계버스 동계 시간표 확인", "p11"), ("11/22쯤부터 요나고 주간 예보 확인", "p21"), ("여행자 보험", "p12"),
]
checklist = f"""
<section class="section">
  <div class="row"><div><div class="eyebrow">출발 전</div><h2 style="font-size:24px;margin-top:4px">준비물 체크</h2></div>
  <span class="chip sea num" id="check-progress">0 / {len(ITEMS)}</span></div>
  <div class="card check">
    {''.join(f'<label for="{i}"><input type="checkbox" id="{i}"><span>{escape(t)}</span></label>' for t, i in ITEMS)}
  </div>
  <p class="tiny">체크 상태는 이 기기의 브라우저에만 저장돼요.</p>
</section>
"""
page("checklist.html", "요나고 준비물", checklist, "home", back="/", header="준비물")

print("built:", sorted(p.name for p in ROOT.glob("*.html")))
