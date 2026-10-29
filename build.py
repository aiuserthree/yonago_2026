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
<footer class="foot">요금은 2026년 10월 29일 Agoda 조회 기준이며 바뀔 수 있습니다. 숙소 사진·평점 출처: Agoda.</footer>
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
    "universal": {
        "name": "요나고 유니버설 호텔",
        "jp": "米子ユニバーサルホテル",
        "kind": "비즈니스 호텔 · 3성급",
        "night": "2·3박째 · 11/30(월)~12/2(수)",
        "price": 58451,
        "nights": 2,
        "room": "2인 1실 · 트윈룸 A (금연) · 17㎡ · 싱글베드 2개",
        "meal": "조식·석식 무료 플랜",
        "cancel": "11/28까지 무료 취소 · 결제일은 예약 화면에서 확인",
        "addr": "121 Mannōchō, Yonago (米子市万能町)",
        "access": "요나고역 북口에서 도보 약 4분(280m)",
        "score": 7.5, "reviews": 3417, "label": "좋음",
        "bars": [("가격 대비", 7.5), ("직원 태도", 7.4), ("청결도", 6.5), ("편의시설", 5.9)],
        "pros": [
            "조식 뷔페와 세트 석식이 요금에 포함돼 가성비가 좋다는 평이 많아요.",
            "요나고역 바로 앞이라 공항버스·JR 이동이 편하고, 근처에 이온몰과 편의점이 있어요.",
            "저렴한 가격 대비 식사와 객실 상태가 기대 이상이었다는 한국인 후기가 여럿 있어요.",
            "옥상 대욕장에서 시내 전망을 보며 씻을 수 있어요.",
        ],
        "cons": [
            "건물이 오래돼 청결도(6.5)와 편의시설(5.9) 점수는 낮은 편이에요.",
        ],
        "photos": [
            "https://pix8.agoda.net/hotelImages/58297545/0/3861720c181742eef90c88f058fdd2d0.jpg?va=1&ce=3&s=1024x",
            "https://pix8.agoda.net/property/58297545/879492545/3263008aa95b83eb41b99490b3e0f28c.jpeg?va=1&ce=2&s=1024x",
            "https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/742891531.jpg?k=781dae3efc475bf1a5aa6ebb4e596c02432f2e1ebe76e9fb97cc8793f56efa72&o=&s=600x",
            "https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/542563946.jpg?k=93562a2175cc21ec9c9c07466eafc252487f0519b7634f5f3f4fc6a31009976c&o=&s=600x",
            "https://pix8.agoda.net/hotelImages/58297545/0/29b60c1bf5d0dd0924beeaffea7e92a4.jpeg?va=1&ce=2&s=600x",
            "https://pix8.agoda.net/property/58297545/0/ad37b8493d11530c8c72a98cb8aaa240.jpeg?va=1&ce=3&s=600x",
            "https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/742891533.jpg?k=a322c2b424937dbe051be74d02071d00dd96e29ccfa0d91ecbf371bc71651381&o=&s=600x",
        ],
        "agoda": "https://www.agoda.com/ko-kr/yonago-universal-hotel-station-h11458945/hotel/yonago-jp.html?checkIn=2026-11-30&checkOut=2026-12-02&los=2&adults=2&rooms=1",
    },
    "kikuman": {
        "name": "이코이테이 기쿠만",
        "jp": "いこい亭 菊萬",
        "kind": "온천 료칸 · 4성급",
        "night": "1박째 · 11/29(일)",
        "price": 418130,
        "room": "2인 1실 · 일본식 룸 - 욕조 (Japanese-Style Room with Bath) · 15㎡ · 객실 샤워실 · 금연",
        "meal": "조식·석식 포함",
        "cancel": "11/22까지 무료 취소 (11/23 전 취소 시) · 11/21까지 결제 없음",
        "addr": "4-27-1 Kaike Onsen, Yonago (米子市皆生温泉4-27-1)",
        "access": "가이케 온천 관광센터 정류장에서 도보 약 3~5분(약 250m) · 체크인 15:00 · 체크아웃 10:00 · 전화 0859-38-3300",
        "score": 8.7, "reviews": 122, "label": "우수",
        "bars": [("직원 태도", 9.4), ("청결도", 8.9), ("가격 대비", 8.8), ("편의시설", 8.6)],
        "pros": [
            "체크인부터 프런트 직원이 친절했다는 후기가 가장 많아요 (직원 태도 9.4).",
            "조식과 석식이 맛있고, 서비스와 음식 모두 만족했다는 평이 이어져요.",
            "노천탕이 좋고, 눈 오는 겨울에 들어가면 분위기가 특히 좋다고 해요.",
            "다다미방에 객실마다 안마의자가 있어요.",
        ],
        "cons": [
            "후기 수(122건)가 다른 곳보다 적어요.",
        ],
        "photos": [
            "https://pix8.agoda.net/property/15635178/0/1bf4f720c5d3b078f9b022616d4106c8.jpeg?va=1&ce=3&s=600x",
            "https://pix8.agoda.net/property/15635178/0/f623f8e72f008082e28b225c0bc47035.jpeg?va=1&ce=3&s=600x",
            "https://pix8.agoda.net/property/15635178/0/c9ed54c59dcec8f6548425868777d998.jpeg?va=1&ce=3&s=600x",
            "https://pix8.agoda.net/property/15635178/0/69e83a1e734a2d41d86198e4a0ea974d.jpeg?va=1&ce=3&s=600x",
            "https://pix8.agoda.net/property/15635178/612954456/30b5ca46ebe16bfb5f52b100ef6922cf.jpeg?va=1&s=1024x",
            "https://pix8.agoda.net/property/15635178/884440437/2de3dd1d9ffc22768cb1a80031cbd5fe.jpeg?va=1&s=1024x",
        ],
        "agoda": "https://www.agoda.com/ko-kr/ikoitei-kikuman-h15635178/hotel/yonago-jp.html?checkIn=2026-11-29&checkOut=2026-11-30&los=1&adults=2&rooms=1",
    },
    "fuga": {
        "name": "가이케 후가",
        "jp": "皆生 風雅",
        "kind": "정원 료칸 · 3성급",
        "night": "다른 후보 · 11/29(일)",
        "price": 486093,
        "room": "2인 1실 · 스탠다드 트윈룸 (금연)",
        "meal": "조식·석식 포함",
        "cancel": "11/23까지 무료 취소",
        "addr": "3-16-1 Kaike Onsen, Yonago",
        "access": "가이케 온천 관광센터 정류장에서 도보 약 4~7분(약 500m) · 요나고역 남쪽 출구 무료 송영(사전 예약)",
        "score": 8.4, "reviews": 440, "label": "우수",
        "bars": [("직원 태도", 8.9), ("가격 대비", 8.7), ("청결도", 8.6), ("편의시설", 8.5)],
        "pros": [
            "밤 9시까지 사케와 음료가 무료이고, 유카타를 골라 입을 수 있어요.",
            "조식이 특히 맛있어서 더 머물고 싶었다는 후기가 있어요.",
            "노천탕이 있고, 가족탕(대절탕)은 따로 예약해 쓸 수 있어요.",
            "요나고역에서 무료 송영 차량을 운영해요 (사전 예약 필수).",
            "첫 입실 때 직원이 관내 시설을 함께 돌며 안내해 줘요.",
        ],
        "cons": [
            "석식 포함 요금이라 늦게 체크인하면 석식이 제공되지 않고 환불도 안 돼요. 도착 예정 시간(16:30 전후)을 미리 알려 두세요.",
            "흡연 가능 객실 정책이라 냄새에 민감하면 금연 요청을 남기는 게 좋아요.",
        ],
        "photos": [
            "https://pix8.agoda.net/hotelImages/4436879/0/00d6c0e2563b146f1f5fbf5ff9e5b3c0.jpeg?va=1&ce=3&s=1024x",
            "https://pix8.agoda.net/hotelImages/4436879/0/4da76435ad5227e4b382c6756a444ae8.jpeg?va=1&ce=3&s=600x",
            "https://pix8.agoda.net/hotelImages/10569725/806986537/5f81f588461cc242a0f8c79017457591.jpg?va=1&ce=3&s=1024x",
            "https://pix8.agoda.net/hotelImages/10569725/806986540/032978827c53b5f479fd819f27e77563.jpg?va=1&ce=3&s=1024x",
            "https://pix8.agoda.net/hotelImages/10569725/806986537/965d868338ca29240b73570f85b4a61d.jpg?va=1&ce=2&s=1024x",
            "https://pix8.agoda.net/hotelImages/10569725/806986540/4c6dacbe40aacbbbd0da4c5e30077d34.jpg?va=1&ce=3&s=1024x",
            "https://pix8.agoda.net/hotelImages/10569725/806986536/02726504d7c3b85b92447b7cb478ed60.jpg?va=1&ce=3&s=1024x",
        ],
        "agoda": "https://www.agoda.com/ko-kr/kaike-no-yado-yururi/hotel/yonago-jp.html?checkIn=2026-11-29&checkOut=2026-11-30&los=1&adults=2&rooms=1",
    },
}

HOTELS = {k: HOTELS[k] for k in ("kikuman", "universal", "fuga")}
PLAN = ("kikuman", "universal")  # 1박째, 2·3박째 (확정)
ALTS = ("fuga",)  # 1박째 다른 후보


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
      <span class="chip accent">확정</span>
      <h3 style="margin-top:8px">료칸 1박 + 역 앞 호텔 2박</h3>
      <p class="small muted">첫날은 온천 료칸에서 쉬고, 나머지 이틀은 역 앞에서 편하게</p>
    </div>
  </div>
  <div class="nights">
    <a class="night" href="/stay-{PLAN[0]}">{img(n1['photos'][0], n1['name'])}
      <div><div class="when">1박 · 11/29 일 · {escape(n1['meal'])}</div><div class="nm">{escape(n1['name'])}</div></div>
      <div class="p">{won(stay_total(n1))}</div></a>
    <a class="night" href="/stay-{PLAN[1]}">{img(n2['photos'][0], n2['name'])}
      <div><div class="when">2박 · 11/30~12/2 · {escape(n2['meal'])}</div><div class="nm">{escape(n2['name'])}</div></div>
      <div class="p">{won(stay_total(n2))}</div></a>
  </div>
  <div class="total"><span class="small muted">3박 합계 · 2인 1실 · 세금 포함<br>1인당 약 {won(round(total / 2))}</span><span class="amt">{won(total)}</span></div>
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
      <div class="price"><div class="amt">{won(stay_total(h))}</div><div class="per">{h.get('nights', 1)}박 · 2인 1실 · {escape(h['meal'])}</div></div>
    </div>
  </a>
</article>"""


FLIGHT_URL = "https://www.agoda.com/ko-kr/flights/results?departureFrom=ICN&departureFromType=1&arrivalTo=YGJ&arrivalToType=1&departDate=2026-11-29&returnDate=2026-12-02&searchType=2&cabinType=Economy&adults=2&children=0&infants=0&sort=8"


def booking_card():
    """항공권·숙소 예약 링크를 한곳에 모은 카드."""
    k, u = HOTELS["kikuman"], HOTELS["universal"]
    rows = [
        ("항공권", "에어서울 RS471/472 · 11/29~12/2 · 성인 2명",
         "직항 · <b>위탁 수하물 미포함</b> 요금 · 1인 ₩210,942 (10/29)", "탑승객 영문 이름은 여권과 똑같이", FLIGHT_URL),
        ("1박 · 11/29", k["name"],
         "<b>일본식 룸 - 욕조 (Japanese-Style Room with Bath)</b> · 조식·석식 · " + won(k["price"]),
         "11/22까지 무료 취소 · 11/21까지 결제 없음 · 요청란에 도착 16:20 적기", k["agoda"]),
        ("2·3박 · 11/30~12/2", u["name"],
         "<b>트윈룸 A (금연) · Free Breakfast and Dinner Plan</b> · 2박 " + won(stay_total(u)),
         "11/28까지 무료 취소", u["agoda"]),
    ]
    items = "".join(f"""
    <li class="book-row">
      <div class="tiny">{label}</div>
      <strong>{name}</strong>
      <p class="small muted">{pick}</p>
      <p class="tiny">{note}</p>
      <a class="btn" href="{escape(url)}" target="_blank" rel="noopener">Agoda에서 예약하기</a>
    </li>""" for label, name, pick, note, url in rows)
    return f"""<article class="card card-body" id="booking">
    <div class="row"><strong>예약하기</strong><span class="chip accent">성인 2명</span></div>
    <ol class="book-list">{items}</ol>
    <div class="note"><span class="mk">!</span><span>요금은 10/29 조회 기준이라 바뀔 수 있어요. Agoda에 로그인했는지, 결제 화면의 최종 금액과 자동 결제일을 꼭 확인하세요. 예약은 직접 진행해요.</span></div>
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
  <div class="stat"><span class="label">1박</span><span class="value">온천 료칸</span><span class="tiny">이코이테이 기쿠만</span></div>
  <div class="stat"><span class="label">2·3박</span><span class="value">역 앞 호텔</span><span class="tiny">요나고 유니버설</span></div>
</div>

<section class="section">
  <div class="section-head"><h2>일정</h2><a href="/day1">자세히</a></div>
  <div class="card">
    <a class="day-link" href="/day1"><div class="day-badge"><span class="d">DAY</span><span class="n">1</span></div>
      <div><h3>도착 · 가이케 온천 료칸</h3><p>11/29 일 · 14:50 도착, 해변 일몰, 료칸 석식</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day2"><div class="day-badge"><span class="d">DAY</span><span class="n">2</span></div>
      <div><h3>아다치 미술관 · 돈키호테</h3><p>11/30 월 · 일본 최고 정원, 호텔 석식, 돈키호테 쇼핑, 규코쓰 라멘</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day3"><div class="day-badge"><span class="d">DAY</span><span class="n">3</span></div>
      <div><h3>사카이미나토 요괴 거리</h3><p>12/1 화 · 미즈키 시게루 로드, 기념관, 항구 점심</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day4"><div class="day-badge"><span class="d">DAY</span><span class="n">4</span></div>
      <div><h3>마쓰에성 · 귀국</h3><p>12/2 수 · 오전 마쓰에성, 13:35 역 앞 버스, 15:50 출발</p></div>{CHEV}</a>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>숙소</h2><a href="/stay">자세히</a></div>
  {plan_card()}
</section>

<section class="section">
  <div class="section-head"><h2>날씨와 옷차림</h2></div>
  <div class="card card-body">
    <div class="row"><span class="muted small">11월 말 평년</span><span class="num">최고 15° / 최저 6°</span></div>
    <div class="row"><span class="muted small">12월 초 평년</span><span class="num">최고 13° / 최저 5°</span></div>
    <p class="small muted">비나 진눈깨비가 잦은 시기예요. 방풍 겉옷과 접이식 우산을 챙기세요. (기상청 요나고 평년값)</p>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>바로가기</h2></div>
  <div class="btn-row">
    <a class="btn secondary" href="/checklist">준비물 체크</a>
    <a class="btn secondary" href="/food">먹거리</a>
  </div>
  <a class="btn" href="/stay#booking">항공권 · 숙소 예약 링크</a>
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
    "airport-guide", "공항 → 이코이테이 기쿠만 가는 길", "11/29",
    [
        ("14:50", "입국 심사 · 짐 찾기", "끝나면 1층 도착 로비로 나가요."),
        ("~15:40", "버스 승강장 7번 찾기", "터미널 밖 버스 승강장에서 7번을 찾아요. 모르겠으면 안내 데스크에 아래 문장을 보여 주세요.",
         ("ソウル便の連絡バスはどこですか？", "서울편 연계버스는 어디서 타나요?")),
        ("15:50", "인천 노선 연계버스 승차", "기사에게 아래 문장을 보여 주고, 요금 ¥500은 현금으로 내요. 일요일에도 다니고, 비행기가 늦으면 버스도 기다려요.",
         ("皆生温泉で降ります。いこい亭菊萬に行きたいです。", "가이케 온천에서 내려요. 이코이테이 기쿠만에 가고 싶어요."), True),
        ("16:15", "가이케 온천에서 하차", "가이케 온천 관광센터(皆生温泉観光センター) 정류장일 가능성이 높아요. 공식 자료에는 정류장 이름이 없어서, 내릴 때 기사에게 한 번 더 확인하세요.", None, True),
        ("16:20", "기쿠만까지 걷기", "도보 약 3~5분(약 250m). 길을 모르겠으면 아래 문장을 보여 주세요.",
         ("いこい亭菊萬はどこですか？", "이코이테이 기쿠만은 어디인가요?")),
    ],
    "버스는 서울편이 결항하면 운행하지 않고, 만차면 못 탈 수 있어요. 놓치면 공항에서 택시로 약 20분 · 약 ¥4,500. 료칸 전화 0859-38-3300 (9:00–18:00)",
    "요나고 공항 서울편 연계버스 시간표(2026.03 게시), 기쿠만 공식 교통 안내(관광센터 정류장 도보 약 5분), 지도 경로 계산.",
)

GUIDE_DAY2 = guide_card(
    "ryokan-guide", "기쿠만 → 요나고역 · 호텔 가는 길", "11/30",
    [
        ("10:00", "체크아웃", "체크아웃은 10:00이에요."),
        ("10:05", "관광센터 정류장까지 걷기", "도보 약 3~5분(약 250m). 아래 문장으로 정류장을 물어보세요.",
         ("米子駅行きのバス停はどこですか？", "요나고역 가는 버스 정류장은 어디인가요?")),
        ("10:15", "요나고역행 노선버스", "가이케 온천 관광센터 → 요나고역 약 20분 · 약 ¥300 · 시간당 2~3대. 차내에서는 1,000엔권까지만 바꿀 수 있어요.", None, True),
        ("10:35", "요나고역 도착 → 이온 ATM → 호텔", "역 앞 이온 요나고에키마에점 1층 ATM에서 현금을 뽑고(도보 약 4분), 유니버설 호텔로 가요(이온에서 약 8분)."),
        ("10:50", "유니버설 호텔에 짐 맡기기", "체크인 전이라 프런트에 짐만 맡겨요.",
         ("チェックインまで荷物を預かってください。", "체크인 전까지 짐을 맡아 주세요."), True),
    ],
    "짐이 많으면 료칸에 택시를 불러 달라고 하세요 (요나고역까지 약 15분 · 약 ¥1,800~2,200). 기쿠만이 근처 정류장까지 송영해 준다는 안내도 있으니 체크인 때 물어보세요.",
    "기쿠만 공식 교통 안내, 요나고역↔가이케 온천 버스·택시 안내, 요나고시·JR 서일본 가이나 로드 안내.",
)

GUIDE_DAY4 = guide_card(
    "airport-return-guide", "요나고역 → 공항 가는 길", "12/2",
    [
        ("13:20", "호텔에서 짐 찾기", "아침에 맡겨 둔 짐을 찾아요."),
        ("13:25", "요나고역 북쪽 출구 7번 승강장", "호텔에서 도보 약 4분. 버스 승강장 7번에서 기다려요. 못 찾겠으면 아래 문장을 보여 주세요.",
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
    <div class="card-body"><div class="tiny">{label}</div><strong>{escape(h['name'])}</strong><span class="small muted">{escape(h['meal'])} · {h.get('nights', 1)}박 {won(stay_total(h))}</span></div>
  </a>"""


day1 = day_tabs("day1") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 1 · 11월 29일 일요일</div><h2 style="font-size:24px;margin-top:4px">도착해서 곧장 온천 마을로</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("11:00", "인천공항 제2터미널 도착", "에어서울은 2025년 9월부터 제2터미널이에요. E1~E10 카운터에서 체크인. 여권 유효기간을 확인하세요.")}
    {tl("13:20", "RS471 인천 출발", "비행 1시간 30분", "key")}
    {tl("14:50", "요나고 기타로 공항 도착", "입국 심사 후 7번 승강장으로. 버스비는 한국에서 바꿔 온 엔화 현금으로")}
    {tl("15:50", "인천 노선 연계버스 탑승", "현지 이름: ソウル便連絡バス · 공항 7번 승강장 → 가이케 온천 16:15 하차 · ¥500 · 현금", "move")}
    {tl("16:20", "이코이테이 기쿠만 체크인", "관광센터 정류장에서 도보 약 3~5분(약 250m). 체크인 때 석식 시간을 정해요.", "key")}
    {tl("16:45", "가이케 해변 일몰 산책", "11월 말 일몰은 오후 5시 전후. 료칸에서 해변까지 가까워요")}
    {tl("18:00", "료칸 석식", "조식·석식 포함 요금. 대게(마쓰바가니) 시즌이에요", "key")}
    {tl("20:00", "노천탕 · 객실 안마의자", "대욕장과 노천탕에서 온천을 즐기고, 방 샤워실도 쓸 수 있어요")}
  </ol>
  </div>
  {GUIDE_DAY1}
  {today_stay("kikuman", "오늘 숙소 · 2인 1실")}
</section>
"""
page("day1.html", "요나고 DAY 1", day1, "plan", back="/", header="일정")

day2 = day_tabs("day2") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 2 · 11월 30일 월요일</div><h2 style="font-size:24px;margin-top:4px">정원 한 폭, 그리고 역 앞 호텔</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:00", "아침 온천", "체크아웃 전 노천탕 한 번 더")}
    {tl("08:00", "료칸 조식", "")}
    {tl("10:00", "체크아웃 · 버스로 요나고역", "관광센터 정류장 → 요나고역 약 20분 · 약 ¥300. 아래 길 안내 참고", "move")}
    {tl("10:35", "이온 ATM에서 현금 인출", "요나고역 앞 이온 1층 ATM 코너(도보 약 4분, 9:00–23:00). 남은 일정 현금 약 ¥29,000", "key")}
    {tl("10:50", "유니버설 호텔에 짐 맡기기", "이온에서 도보 약 8분. 체크인 전 수하물 보관")}
    {tl("11:10", "JR 요나고 → 야스기", "산인본선 보통열차 약 8분 · ¥200. 열차 시간은 전날 확인하세요", "move")}
    {tl("11:30", "야스기역 무료 셔틀", "미술관까지 약 20분 · 선착순 25명 (다음 편 11:55)", "move")}
    {tl("11:50", "아다치 미술관", "미국 정원 전문지 선정 일본 정원 1위를 이어온 곳. 12월 초는 늦단풍이 남아 있을 수 있어요. 성인 ¥2,500, 여권 제시 시 ¥2,400", "key")}
    {tl("14:00", "셔틀 → 야스기역 → 요나고", "미술관 발 14:00 / 14:30 셔틀", "move")}
    {tl("15:00", "늦은 점심 · 역 앞 구경", "니쿠곳초(肉ごっつお, 15:00까지)는 빠듯하니 역 주변 카페나 이온몰도 좋아요")}
    {tl("16:00", "요나고 유니버설 호텔 체크인", "트윈룸 A (금연) · 2박", "key")}
    {tl("18:00", "호텔 석식", "무료 석식 플랜 포함")}
    {tl("19:29", "JR 요나고 → 고토", "사카이선 1정거장, 6분 · ¥150", "move")}
    {tl("19:35", "MEGA 돈키호테 요나고점", "고토역 바로 옆. 9:00–24:00, 연중무휴. 면세 가능하니 여권을 챙기세요", "key")}
    {tl("20:59", "JR 고토 → 요나고", "놓치면 다음 열차 22:10. 택시는 약 10분, 걸어서 약 28분(2.1km)", "move")}
    {tl("21:15", "야식: 규코쓰(소뼈) 라멘", "역 앞 라멘 야마토(ラーメン大和), 한 그릇 ¥550, 22:45까지 (월요일 영업)")}
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
      <dt>가는 법</dt><dd>요나고역에서 JR 사카이선 6분 ¥150 · 택시 약 10분 · 도보 약 28분</dd>
    </dl>
    <p class="tiny">저녁 사카이선은 한 시간에 한 대꼴이에요. 요나고 발 18:03·19:29·20:25 / 고토 발 19:57·20:59·22:10 (평일)</p>
  </div>
  {today_stay("universal", "오늘부터 2박 · 2인 1실")}
</section>
"""
page("day2.html", "요나고 DAY 2", day2, "plan", back="/", header="일정")

day3 = day_tabs("day3") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 3 · 12월 1일 화요일</div><h2 style="font-size:24px;margin-top:4px">요괴 거리와 항구 마을</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:30", "호텔 조식 뷔페", "")}
    {tl("09:00", "JR 요나고 → 사카이미나토", "사카이선 약 45분 · ¥330. 기타로 래핑 열차가 다녀요. 열차 시간은 전날 확인하세요", "move")}
    {tl("10:00", "미즈키 시게루 로드", "요괴 동상이 늘어선 역 앞 거리. 천천히 걸으며 사진 찍기", "key")}
    {tl("11:00", "미즈키 시게루 기념관", "9:30–17:00 (입장 16:30까지), 일반 ¥1,000. 역에서 도보 약 10분")}
    {tl("12:30", "항구 근처 해산물 점심", "사카이미나토는 대게와 해산물 항구 도시예요")}
    {tl("14:00", "JR 사카이미나토 → 요나고", "약 45분", "move")}
    {tl("15:00", "호텔에서 쉬기 · 역 주변 산책", "옥상 대욕장, 이온몰 구경")}
    {tl("18:00", "호텔 석식", "무료 석식 플랜 포함")}
    {tl("20:00", "자유 시간", "역 앞 이자카야에서 대게 한 접시도 좋아요 (먹거리 페이지 참고)")}
  </ol>
  </div>
  {today_stay("universal", "오늘 숙소 · 2박째")}
</section>
"""
page("day3.html", "요나고 DAY 3", day3, "plan", back="/", header="일정")

day4 = day_tabs("day4") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 4 · 12월 2일 수요일</div><h2 style="font-size:24px;margin-top:4px">마쓰에성 한 바퀴, 역 앞에서 공항으로</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:30", "호텔 조식 뷔페", "")}
    {tl("08:30", "체크아웃 · 짐 맡기기", "호텔 수하물 보관 서비스 이용", "key")}
    {tl("09:00", "JR 요나고 → 마쓰에", "산인본선 보통열차 약 30분 · ¥510. 열차 시간은 전날 확인하세요", "move")}
    {tl("09:40", "레이크라인 버스 → 마쓰에성", "마쓰에역 7번 승강장, 약 10분 · ¥250", "move")}
    {tl("10:00", "마쓰에성 천수각", "현존 천수각 중 하나인 국보 성. 8:30–17:00, 성인 ¥1,200")}
    {tl("11:30", "마쓰에 → 요나고", "버스 + JR, 약 50분", "move")}
    {tl("12:30", "점심: 규코쓰 라멘", "라멘 야마토 또는 니쿠곳초 요나고역 앞점 (둘 다 수요일 영업)")}
    {tl("13:20", "호텔에서 짐 찾기", "")}
    {tl("13:35", "인천 노선 연계버스 탑승", "현지 이름: ソウル便連絡バス · 요나고역 북口 7번 → 공항 14:20 · ¥640 · 현금", "move")}
    {tl("14:20", "요나고 공항 도착", "출국 수속, 기념품")}
    {tl("15:50", "RS472 요나고 출발", "", "key")}
    {tl("17:40", "인천 제2터미널 도착", "")}
  </ol>
  </div>
  {GUIDE_DAY4}
  <div class="note info"><span class="mk">i</span><span>마쓰에에서 늦어질 것 같으면 성 관람을 줄이세요. 13:35 버스를 놓쳐도 13:38 JR 열차가 있어요.</span></div>
</section>
"""
page("day4.html", "요나고 DAY 4", day4, "plan", back="/", header="일정")


# ---------------------------------------------------------------- 숙소 목록
stay = f"""
{booking_card()}
<section class="section">
  <div><div class="eyebrow">1박은 온천 료칸, 2박은 역 앞</div><h2 style="font-size:24px;margin-top:4px">확정한 숙소</h2>
  <p class="small muted" style="margin-top:6px">성인 2명 · 2인 1실 · 세금 포함 · 2026년 10월 29일 Agoda 요금</p></div>
  {plan_card()}
  <div class="list">{''.join(stay_card(k) for k in PLAN)}</div>
</section>
<section class="section">
  <div class="section-head"><h2>11/29 다른 료칸 후보</h2></div>
  <p class="small muted">2인 1실 조식·석식 포함 기준이에요. 후가는 11/29 일요일 밤 요금이 11/30보다 훨씬 비싸요.</p>
  <div class="list">{''.join(stay_card(k) for k in ALTS)}</div>
</section>
<section class="section">
  <div class="note info"><span class="mk">i</span><span>APA 제휴 호텔(요나고 시티가든즈 호텔)도 APA 공식 사이트에서 예약할 수 있어요. 식사는 포함되지 않아요.</span></div>
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
      <div><div class="tiny">{h.get('nights', 1)}박 · 2인 1실 · 세금 포함</div><div class="num" style="font-size:26px;font-weight:600">{won(stay_total(h))}</div><div class="tiny">{'1박 ' + won(h['price']) + ' · ' if h.get('nights', 1) > 1 else ''}1인당 약 {won(round(stay_total(h) / 2))}</div></div>
      <span class="chip good">{escape(h['meal'])}</span>
    </div>
    <dl class="kv">
      <dt>객실</dt><dd>{escape(h['room'])}</dd>
      <dt>취소</dt><dd>{escape(h['cancel'])}</dd>
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
<a class="btn" href="{escape(h['agoda'])}" target="_blank" rel="noopener">Agoda에서 요금 보기</a>
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
    <div class="row"><span class="small muted">Agoda 왕복 · 2명 · 세금 포함<br>1인 ₩210,942 (10/29 조회)</span><span class="num" style="font-size:20px;font-weight:600">₩421,884</span></div>
    <a class="btn" href="/stay#booking">예약 링크 보기</a>
    <p class="tiny"><b>위탁 수하물 미포함 요금</b>으로 정했어요(기내 수하물만). 위탁 수하물 포함 요금은 1인 ₩222,744예요(10/29 조회). 기내 수하물 무게·크기 규정은 에어서울에서 확인하세요.</p>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>공항 ↔ 시내</h2></div>
  <a class="card card-body" href="/day1#airport-guide" style="text-decoration:none">
    <div class="row"><strong>공항 → 이코이테이 기쿠만 가는 길</strong><svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></div>
    <p class="small muted">7번 승강장 찾기부터 료칸까지 단계별 안내와 보여 주기용 일본어 문장</p>
  </a>
  <a class="card card-body" href="/day2#ryokan-guide" style="text-decoration:none">
    <div class="row"><strong>기쿠만 → 요나고역 · 호텔 가는 길</strong><svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></div>
    <p class="small muted">관광센터 정류장에서 버스로 요나고역, 호텔에 짐 맡기기까지</p>
  </a>
  <a class="card card-body" href="/day4#airport-return-guide" style="text-decoration:none">
    <div class="row"><strong>요나고역 → 공항 가는 길</strong><svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></div>
    <p class="small muted">북쪽 출구 7번 승강장 13:35 연계버스, 놓쳤을 때 JR 13:38</p>
  </a>
  <div class="card card-body">
    <div class="row"><strong>인천 노선 연계버스</strong><span class="chip accent">추천</span></div>
    <p class="small muted">현지 정식 이름은 국제선(서울편) 연락버스(国際線 ソウル便連絡バス)예요. 에어서울 인천↔요나고 편 시간에 맞춰 히노마루 버스가 운행해요. 정류장 안내판에서는 「ソウル便」을 찾으세요.</p>
    <dl class="kv">
      <dt>도착일</dt><dd>공항 7번 15:50 → <b>가이케 온천 16:15 하차</b> → 요나고역 북口 16:35</dd>
      <dt>귀국일</dt><dd><b>요나고역 북口 7번 13:35 승차</b> → 가이케 온천 13:55 → 공항 14:20</dd>
      <dt>요금</dt><dd>우리 일정은 도착일 ¥500 + 귀국일 ¥640 · 현금</dd>
    </dl>
    <p class="tiny">요나고 공항 공식 시간표 기준. 인천 노선 항공편이 결항하면 운행하지 않고, 만차면 못 탈 수 있어요.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>JR 사카이선 열차</strong><span class="chip">약 30분 · ¥240</span></div>
    <p class="small muted">터미널에서 JR 요나고공항역까지 도보 약 5분. 도착일 오후 요나고행은 14:53, 16:12, 17:03, 17:52 (평일). 14:53은 입국 심사 때문에 타기 어려워요.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>택시</strong><span class="chip">대략</span></div>
    <p class="small muted">공항 → 요나고역 약 30분 · 약 ¥5,500 (공항 공식 안내)<br>가이케 온천 → 공항 약 20분 · 약 ¥4,500<br>가이케 온천 → 요나고역 약 15분 · 약 ¥2,200<br>공항 택시는 대수가 적어 미리 예약을 권해요. 日ノ丸ハイヤー 0859-22-3231</p>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>시내 이동</h2></div>
  <div class="card">
    <div class="table-wrap" style="padding:4px 16px">
    <table class="money">
      <tr><td>요나고역 → 가이케 온천 (가이케선 버스)<div class="tiny">약 20분 · 평일 시간당 2–4편 · 막차 20:45</div></td><td>약 ¥300</td></tr>
      <tr><td>요나고 → 야스기 (JR 보통)<div class="tiny">약 8분 · 아다치 미술관 셔틀 연결</div></td><td>¥200</td></tr>
      <tr><td>야스기역 → 아다치 미술관 셔틀<div class="tiny">약 20분 · 선착순 25명</div></td><td>무료</td></tr>
      <tr><td>요나고 → 마쓰에 (JR 보통)<div class="tiny">약 30분</div></td><td>¥510</td></tr>
      <tr><td>요나고 → 사카이미나토 (JR 사카이선)<div class="tiny">약 45분 · 기타로 열차</div></td><td>¥330</td></tr>
    </table>
    </div>
  </div>
  <div class="note info"><span class="mk">i</span><span>버스는 현금 위주예요. 차내에서는 1,000엔권까지만 바꿀 수 있으니 동전과 천 엔짜리를 넉넉히 준비하세요.</span></div>
</section>

<section class="section">
  <div class="section-head"><h2>아다치 미술관 셔틀 시간</h2></div>
  <div class="card card-body">
    <div class="tiny">야스기역 → 미술관</div>
    <p class="num small">8:50 9:20 9:50 10:15 10:45 11:05 11:30 11:55 12:30 13:00 13:30 14:00 14:30 15:05 15:30 15:55 16:25</p>
    <div class="tiny" style="margin-top:6px">미술관 → 야스기역</div>
    <p class="num small">9:15 9:50 10:15 10:35 11:05 11:30 12:00 12:30 12:55 13:30 14:00 14:30 15:00 15:30 15:55 16:30 17:10</p>
  </div>
</section>
"""
page("transport.html", "요나고 교통", transport, "move", header="교통")


# ---------------------------------------------------------------- 예산
budget = """
<section class="section" id="budget">
  <div><div class="eyebrow">성인 2명 기준</div><h2 style="font-size:24px;margin-top:4px">여행 예산</h2></div>
  <div class="card card-body">
    <label class="row small" for="rate"><span class="muted">환율 (100엔당 원)</span>
      <input id="rate" type="number" inputmode="decimal" value="861" min="500" max="2000" step="0.1"
        style="width:96px;height:36px;border-radius:10px;border:1px solid var(--line);background:var(--surface-2);color:var(--ink);padding:0 10px;font:600 15px var(--num);text-align:right"></label>
    <p class="tiny" id="rate-src">2026-09-27 기준 환율 (100엔 ≈ 861원)</p>
  </div>
  <div class="card">
    <div class="table-wrap" style="padding:4px 16px">
    <table class="money">
      <tr><td>항공권 왕복 2명 (에어서울 · 위탁 수하물 미포함)</td><td id="flight-amt" data-won="421884">₩421,884</td></tr>
      <tr><td>숙소 3박 2인 1실 (기쿠만 2식 + 유니버설 2식 2박)</td><td id="stay-amt" data-won="535032">₩535,032</td></tr>
      <tr><td>공항 연계버스 2명 (도착 ¥500 + 귀국 ¥640)</td><td data-yen="2280">-</td></tr>
      <tr><td>JR 요나고↔야스기 왕복 2명</td><td data-yen="800">-</td></tr>
      <tr><td>JR 요나고↔고토 왕복 2명 (돈키호테)</td><td data-yen="600">-</td></tr>
      <tr><td>가이케 온천 → 요나고역 버스 2명</td><td data-yen="600">-</td></tr>
      <tr><td>마쓰에 왕복 2명 (JR + 레이크라인 버스)</td><td data-yen="3040">-</td></tr>
      <tr><td>마쓰에성 천수각 2명</td><td data-yen="2400">-</td></tr>
      <tr><td>아다치 미술관 2명 (여권 할인)</td><td data-yen="4800">-</td></tr>
      <tr><td>사카이미나토 JR 왕복 2명</td><td data-yen="1320">-</td></tr>
      <tr><td>미즈키 시게루 기념관 2명</td><td data-yen="2000">-</td></tr>
      <tr><td>점심 3번 · 간식 · 라멘 2명</td><td data-yen="15000">-</td></tr>
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
      <tr><td><b>꼭 현금</b><div class="tiny">인천 노선 연계버스 (도착 ¥500 + 귀국 ¥640) · 공항 시간표에 "기본 현금"</div></td><td>¥2,280</td></tr>
      <tr><td><b>현금 또는 ICOCA</b><div class="tiny">JR(야스기·고토·사카이미나토·마쓰에), 레이크라인 버스, 가이케↔요나고역 노선버스 · 트래블월렛 카드로는 못 내요</div></td><td>¥6,360</td></tr>
      <tr><td><b>카드 확인 못 함 → 현금 준비</b><div class="tiny">아다치 미술관, 마쓰에성, 미즈키 시게루 기념관 입장료</div></td><td>¥9,200</td></tr>
      <tr><td><b>일부 현금</b><div class="tiny">점심 · 라멘 · 간식 (작은 식당은 현금만 받는 곳이 많아요)</div></td><td>약 ¥15,000</td></tr>
      <tr class="sum"><td>준비할 현금</td><td>약 ¥30,000</td></tr>
    </table>
    </div>
  </div>
  <div class="card card-body">
    <strong>카드로 내도 되는 곳</strong>
    <p class="small muted">MEGA 돈키호테(신용카드·은련), 편의점, 이온. 숙소는 Agoda에서 미리 결제해요. 료칸 음료 같은 현장 요금이 있을 수 있으니 소액 현금은 들고 다니세요.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>이온은행 ATM (트래블월렛)</strong><span class="chip good">해외 카드 가능</span></div>
    <dl class="kv">
      <dt>추천</dt><dd><b>이온 요나고에키마에점 1층 ATM 코너</b> (米子市末広町311)</dd>
      <dt>시간</dt><dd>9:00–23:00</dd>
      <dt>거리</dt><dd>요나고역에서 도보 약 4분(280m) · 유니버설 호텔에서 약 8분(600m)</dd>
      <dt>다른 곳</dt><dd>JU 요나고 다카시마야(米子市角盤町1-30, 호텔에서 약 14분) · 이온 마쓰에점(9:00–22:00)</dd>
    </dl>
    <p class="tiny">공항과 가이케 온천에는 이온은행 ATM이 없어요. 공항 1층 세븐일레븐에 세븐은행 ATM이 있지만 수수료가 붙을 수 있어요. 트래블월렛 수수료는 출발 전에 앱에서 확인하세요.</p>
  </div>
  <div class="card card-body">
    <strong>인출 계획</strong>
    <ol class="timeline">
      <li class="tl key"><span class="t">출발 전</span><span class="dot"></span><div class="c"><h3>한국에서 엔화 ¥5,000 환전</h3><p>첫날 공항 연계버스(¥1,000)와 비상금. 공항·가이케에는 이온 ATM이 없어요.</p></div></li>
      <li class="tl key"><span class="t">11/30</span><span class="dot"></span><div class="c"><h3>10:35 이온 요나고에키마에점 ATM</h3><p>버스로 요나고역에 내리면 바로 들러서 약 ¥29,000 인출. 천 엔 단위로 뽑으면 1,000엔권이 섞여 나와 버스 요금 내기 편해요.</p></div></li>
      <li class="tl"><span class="t">이후</span><span class="dot"></span><div class="c"><h3>부족하면 같은 ATM</h3><p>DAY 3·4에도 9:00–23:00에 쓸 수 있어요. 1만 엔권은 돈키호테·편의점에서 깨 두세요.</p></div></li>
    </ol>
  </div>
  <div class="note info"><span class="mk">i</span><span>ICOCA: 요나고 일대 JR과 노선버스(2026년 3월부터)에서 쓸 수 있고 운임은 현금과 같아요. 사려면 요나고역에서 현금으로 사요(보통 ¥2,000, 보증금 ¥500 포함). 이번 일정은 현금만으로도 충분해요.</span></div>
</section>
  <p class="tiny">세 밤 모두 조식·석식이 포함이라 저녁 식비는 넣지 않았어요. 항공권은 10/29 조회 요금(1인 ₩210,942)이에요. 환율은 페이지를 열 때 최신값으로 바뀌고, 직접 고쳐 넣을 수도 있어요.</p>
</section>
"""
page("budget.html", "요나고 예산", budget, "money", header="예산")


# ---------------------------------------------------------------- 먹거리
food = """
<section class="section">
  <div><div class="eyebrow">요나고에서 먹을 것</div><h2 style="font-size:24px;margin-top:4px">규코쓰 라멘과 대게</h2></div>
  <div class="section-head" style="margin-top:4px"><h2>요나고역 앞 (둘째 날 ~ 넷째 날)</h2></div>
  <div class="card card-body">
    <div class="row"><strong>라멘 야마토</strong><span class="chip">ラーメン大和</span></div>
    <p class="small muted">요나고의 명물 규코쓰(소뼈) 라멘. 역 앞 야요이초. 한 그릇 ¥550, 11:00–22:45, 일요일 휴무라 월요일 밤에 가기 좋아요.</p>
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
    <p class="small muted">역 도보 3분 이자카야(太平記). 마쓰바가니 5품 코스 ¥9,800, 일반 코스 ¥3,300부터. 17:00–24:00, 연중무휴.</p>
  </div>
  <div class="section-head" style="margin-top:8px"><h2>가이케 온천가 (산책·한잔)</h2></div>
  <p class="small muted">첫날 저녁은 료칸 석식이에요. 11/29는 일요일이라 쇼쿠사이 슈와 야키토리 아오이야는 쉬어요. 영업 정보는 바뀔 수 있어요.</p>
  <div class="card card-body">
    <div class="row"><strong>이자카야 엔야</strong><span class="chip">エンヤ</span></div>
    <p class="small muted">현지인에게도 인기 있는 이자카야. 메뉴가 많고 가격이 부담 없어요. 17:00–23:00, 베이사이드 스퀘어 가이케 호텔 안.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>쇼쿠사이 슈</strong><span class="chip accent">대게</span></div>
    <p class="small muted">食彩 シュウ. 매일 들여오는 해산물 창작 일식, 겨울엔 게 요리. 17:00–23:00, 일요일·첫째·셋째 월요일 휴무.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>야키토리 아오이야</strong><span class="chip">やきとり葵屋</span></div>
    <p class="small muted">닭꼬치에 반찬 5가지와 음료 2잔 세트 ¥1,500. 일요일 휴무.</p>
  </div>
  <div class="card card-body">
    <div class="row"><strong>오션 레스토랑</strong><span class="chip">연중무휴</span></div>
    <p class="small muted">당일치기 온천 시설 안 식당. 10:00–24:00, 산인 지역 식재료 요리.</p>
  </div>
  <div class="note info"><span class="mk">i</span><span>마쓰바가니(대게) 시즌은 2026년 11월 6일부터 2027년 3월 20일까지예요.</span></div>
</section>
"""
page("food.html", "요나고 먹거리", food, "home", back="/", header="먹거리")


# ---------------------------------------------------------------- 체크리스트
ITEMS = [
    ("여권 (유효기간 6개월 이상 권장)", "p1"), ("항공권 e-티켓 · 인천 제2터미널", "p2"), ("숙소 예약 확인서 2곳", "p3"),
    ("Visit Japan Web 입국 정보 등록", "p4"), ("한국에서 엔화 ¥5,000 환전 (첫날 버스·비상금)", "p5"), ("트래블월렛 이온은행 ATM 수수료 확인", "p16"),
    ("해외 결제 카드", "p6"), ("돈키호테 쇼핑 목록 · 면세용 여권", "p13"), ("기내 수하물 규정 확인 (위탁 수하물 없음)", "p14"), ("eSIM 또는 로밍", "p7"), ("110V 돼지코 어댑터", "p8"),
    ("방풍 겉옷 · 접이식 우산", "p9"), ("료칸 석식 시간 · 도착 시간 알리기", "p10"), ("기쿠만에 도착 시간(16:20쯤)과 석식 시간 알리기", "p15"),
    ("연계버스 동계 시간표 확인", "p11"), ("여행자 보험", "p12"),
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
