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
<meta name="description" content="요나고 2박 3일 여행 일정 · 숙소 · 교통 · 예산 (2026.11.30–12.2)">
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
<footer class="foot">요금은 2026년 9월 27일 Agoda 조회 기준이며 바뀔 수 있습니다. 숙소 사진·평점 출처: Agoda.</footer>
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
        "night": "1박째 · 11/30(월)",
        "price": 35081,
        "room": "싱글룸 A (금연) · 15㎡ · 싱글베드 1개",
        "meal": "조식·석식 무료 플랜",
        "cancel": "11/30 전까지 무료 취소 (11/28 자동 결제)",
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
        "agoda": "https://www.agoda.com/ko-kr/yonago-universal-hotel-station-h11458945/hotel/yonago-jp.html?checkIn=2026-11-30&los=1&adults=1&rooms=1",
    },
    "tensui": {
        "name": "가이케 그랜드 호텔 텐스이",
        "jp": "皆生グランドホテル天水",
        "kind": "해변 온천 호텔 · 3.5성급",
        "night": "2박째 · 12/1(화)",
        "price": 110626,
        "room": "1인 이용 객실",
        "meal": "조식·석식 포함",
        "cancel": "무료 취소 가능 (기한은 예약 화면에서 확인)",
        "addr": "4-18-45 Kaike Onsen, Yonago",
        "access": "가이케 온천 해변 바로 앞 · 요나고역에서 버스 약 20분",
        "score": 7.8, "reviews": 593, "label": "매우 좋음",
        "bars": [("객실 안락함", 10.0), ("직원 태도", 8.0), ("청결도", 7.7), ("가격 대비", 7.7)],
        "pros": [
            "객실과 욕실이 넓고, 대욕장과 노천탕에서 관광 뒤 피로를 풀기 좋았다는 후기가 많아요.",
            "바다가 보이는 객실이 있고, 파도 소리를 들으며 온천을 할 수 있어요.",
            "실내 수영장과 라운지 등 부대시설이 많은 대형 호텔이에요.",
            "직원이 친절하다는 평이 꾸준해요.",
        ],
        "cons": [
            "전통 료칸이라기보다 대형 온천 호텔이라 아늑한 료칸 분위기를 원하면 아쉬울 수 있어요.",
        ],
        "photos": [
            "https://pix8.agoda.net/hotelImages/290145/0/ceb48743363e549944e524c1cd2682a3.jpeg?va=1&ce=3&s=1024x",
            "https://pix8.agoda.net/hotelImages/290145/0/e9e35e94349a29b39c4a527d8b9a7b52.jpeg?va=1&ce=0&s=600x",
            "https://pix8.agoda.net/hotelImages/290145/1024534661/fadb7e370217d9272fe5cf81ff189487.jpg?va=1&ce=0&s=1024x",
            "https://pix8.agoda.net/hotelImages/290145/0/abeaad59ae440e0c6ac19a79fdfb087e.jpeg?va=1&ce=0&s=600x",
            "https://pix8.agoda.net/hotelImages/9077665/796593522/c2b7957a8a6f58058d2432bb8400971d.jpg?va=1&ce=0&s=1024x",
            "https://pix8.agoda.net/hotelImages/9077665/796593610/942f51aa16b639c8df71e9abc1d0d1c7.jpg?va=1&ce=0&s=1024x",
        ],
        "agoda": "https://www.agoda.com/ko-kr/kaike-grand-hotel-tensui_3/hotel/yonago-jp.html?checkIn=2026-12-01&los=1&adults=1&rooms=1",
    },
    "kikuman": {
        "name": "이코이테이 기쿠만",
        "jp": "いこい亭 菊萬",
        "kind": "온천 료칸 · 4성급",
        "night": "2박째 · 12/1(화)",
        "price": 138742,
        "room": "일본식 다다미 객실 (금연)",
        "meal": "조식·석식 포함",
        "cancel": "11/27 전까지 무료 취소 (11/25 자동 결제)",
        "addr": "4-27-1 Kaike Onsen, Yonago",
        "access": "가이케 온천가 · 요나고역에서 버스 약 20분",
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
        "agoda": "https://www.agoda.com/ko-kr/ikoitei-kikuman-h15635178/hotel/yonago-jp.html?checkIn=2026-12-01&los=1&adults=1&rooms=1",
    },
    "fuga": {
        "name": "가이케 후가",
        "jp": "皆生 風雅",
        "kind": "정원 료칸 · 3성급",
        "night": "2박째 · 12/1(화)",
        "price": 157167,
        "room": "1인 이용 일본식 객실",
        "meal": "조식·석식 포함",
        "cancel": "무료 취소 가능 (기한은 예약 화면에서 확인)",
        "addr": "3-16-1 Kaike Onsen, Yonago",
        "access": "가이케 온천 신사 옆 · 요나고역 무료 송영(사전 예약)",
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
            "체크인이 늦으면 석식이 제공되지 않고 환불도 안 돼요. 도착 시간을 미리 알려야 해요.",
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
        "agoda": "https://www.agoda.com/ko-kr/kaike-no-yado-yururi/hotel/yonago-jp.html?checkIn=2026-12-01&los=1&adults=1&rooms=1",
    },
}

COMBOS = [
    ("tensui", "가성비", "온천 호텔에서 바다 보며 쉬기", False),
    ("kikuman", "추천", "평점과 식사 만족도가 가장 높아요", True),
    ("fuga", "분위기", "사케·유카타·정원이 있는 료칸 경험", False),
]


def img(src, alt, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<img data-photo{c} src="{escape(src)}" alt="{escape(alt)}" loading="lazy" '
            'referrerpolicy="no-referrer">')


def combo_card(key, tag, desc, pick):
    u, h = HOTELS["universal"], HOTELS[key]
    total = u["price"] + h["price"]
    chip = "accent" if pick else "sea"
    return f"""
<article class="card combo{' pick' if pick else ''}">
  <div class="combo-top">
    <div>
      <span class="chip {chip}">{tag}</span>
      <h3 style="margin-top:8px">유니버설 + {escape(h['name'])}</h3>
      <p class="small muted">{escape(desc)}</p>
    </div>
  </div>
  <div class="nights">
    <a class="night" href="/stay-universal">{img(u['photos'][0], u['name'])}
      <div><div class="when">1박 · 11/30 월</div><div class="nm">{escape(u['name'])}</div></div>
      <div class="p">{won(u['price'])}</div></a>
    <a class="night" href="/stay-{key}">{img(h['photos'][0], h['name'])}
      <div><div class="when">2박 · 12/1 화</div><div class="nm">{escape(h['name'])}</div></div>
      <div class="p">{won(h['price'])}</div></a>
  </div>
  <div class="total"><span class="small muted">2박 합계 · 1인 · 세금 포함</span><span class="amt">{won(total)}</span></div>
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
      <div class="price"><div class="amt">{won(h['price'])}</div><div class="per">1박 · 1인 · {escape(h['meal'])}</div></div>
    </div>
  </a>
</article>"""


# ---------------------------------------------------------------- 홈
home = f"""
<section class="hero">
  <svg class="mount" viewBox="0 0 200 90" aria-hidden="true"><path fill="#fff" d="M0 90 L70 20 L84 30 L100 8 L118 28 L130 22 L200 90 Z"/><path fill="#22406a" d="M92 18 L100 8 L108 19 L103 24 L100 20 L96 25 Z" opacity=".4"/></svg>
  <div class="eyebrow">SAN'IN · TOTTORI</div>
  <h1>요나고 2박 3일</h1>
  <p class="dates">2026. 11. 30 (월) — 12. 2 (수)</p>
  <div class="dday"><b data-dday>D-</b><span>에어서울 RS471 · 13:20 인천 출발</span></div>
</section>

<div class="stats">
  <div class="stat"><span class="label">항공</span><span class="value">에어서울</span><span class="tiny">직항 1시간 30분</span></div>
  <div class="stat"><span class="label">1박</span><span class="value">역 앞 호텔</span><span class="tiny">요나고 유니버설</span></div>
  <div class="stat"><span class="label">2박</span><span class="value">온천 료칸</span><span class="tiny">가이케 온천</span></div>
</div>

<section class="section">
  <div class="section-head"><h2>일정</h2><a href="/day1">자세히</a></div>
  <div class="card">
    <a class="day-link" href="/day1"><div class="day-badge"><span class="d">DAY</span><span class="n">1</span></div>
      <div><h3>도착 · 요나고역 앞</h3><p>11/30 월 · 14:50 도착, 호텔 석식, 규코쓰 라멘</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day2"><div class="day-badge"><span class="d">DAY</span><span class="n">2</span></div>
      <div><h3>아다치 미술관 · 가이케 온천</h3><p>12/1 화 · 일본 최고 정원, 료칸 가이세키</p></div>{CHEV}</a>
  </div>
  <div class="card">
    <a class="day-link" href="/day3"><div class="day-badge"><span class="d">DAY</span><span class="n">3</span></div>
      <div><h3>온천 아침 · 귀국</h3><p>12/2 수 · 해변 산책, 15:50 출발</p></div>{CHEV}</a>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>추천 숙소 조합</h2><a href="/stay">전체 보기</a></div>
  <div class="hscroll">
    {''.join(f'<div style="width:86%">{combo_card(*c)}</div>' for c in COMBOS)}
  </div>
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
</section>
"""
page("index.html", "요나고 2박 3일", home, "home")


# ---------------------------------------------------------------- 일정
def day_tabs(active):
    items = [("day1", "DAY 1 · 11/30"), ("day2", "DAY 2 · 12/1"), ("day3", "DAY 3 · 12/2")]
    cur = ' aria-current="page"'
    return '<nav class="day-tabs" aria-label="날짜 선택">' + "".join(
        f'<a href="/{k}"{cur if k == active else ""}>{v}</a>' for k, v in items) + "</nav>"


def tl(time, title, text="", kind=""):
    return (f'<li class="tl {kind}"><span class="t">{time}</span><span class="dot"></span>'
            f'<div class="c"><h3>{title}</h3>{f"<p>{text}</p>" if text else ""}</div></li>')


day1 = day_tabs("day1") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 1 · 11월 30일 월요일</div><h2 style="font-size:24px;margin-top:4px">도착하고, 역 앞에서 쉬기</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("11:00", "인천공항 제1터미널 도착", "에어서울 카운터에서 체크인. 여권 유효기간을 확인하세요.")}
    {tl("13:20", "RS471 인천 출발", "비행 1시간 30분", "key")}
    {tl("14:50", "요나고 기타로 공항 도착", "입국 심사 후 7번 승강장으로")}
    {tl("15:50", "서울편 연계버스 탑승", "공항 → 가이케 온천 → 요나고역 북口 16:35 · ¥640 · 현금", "move")}
    {tl("16:45", "요나고 유니버설 호텔 체크인", "역에서 도보 약 4분. 싱글룸 A (금연)", "key")}
    {tl("18:00", "호텔 석식", "무료 석식 플랜 포함. 옥상 대욕장은 식후에")}
    {tl("21:00", "야식: 규코쓰(소뼈) 라멘", "역 앞 라멘 야마토(ラーメン大和), 한 그릇 ¥550, 22:45까지")}
  </ol>
  </div>
  <div class="note info"><span class="mk">i</span><span>연계버스는 서울편(월·수·목·금·일) 도착에 맞춰 운행하고, 비행기가 늦으면 출발도 늦춰져요. 놓치면 JR 요나고공항역(터미널에서 도보 약 5분) 16:12 열차로 요나고역까지 약 30분(¥240), 택시는 약 30분·약 ¥5,500이에요.</span></div>
  <a class="card stay-card" href="/stay-universal" style="display:grid;grid-template-columns:96px 1fr;align-items:center">
    <div style="height:96px">{img(HOTELS['universal']['photos'][0], '요나고 유니버설 호텔', '')}</div>
    <div class="card-body"><div class="tiny">오늘 숙소</div><strong>요나고 유니버설 호텔</strong><span class="small muted">조식·석식 포함 · {won(35081)}</span></div>
  </a>
</section>
"""
page("day1.html", "요나고 DAY 1", day1, "plan", back="/", header="일정")

day2 = day_tabs("day2") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 2 · 12월 1일 화요일</div><h2 style="font-size:24px;margin-top:4px">정원 한 폭, 그리고 온천</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:30", "호텔 조식 뷔페", "")}
    {tl("09:00", "체크아웃 · 짐 맡기기", "호텔 수하물 보관 서비스 이용")}
    {tl("09:30", "JR 요나고 → 야스기", "산인본선 보통열차 약 8분 · ¥200", "move")}
    {tl("10:15", "야스기역 무료 셔틀", "미술관까지 약 20분 · 선착순 25명", "move")}
    {tl("10:40", "아다치 미술관", "미국 정원 전문지 선정 일본 정원 1위를 이어온 곳. 12월 초는 늦단풍이 남아 있을 수 있어요. 성인 ¥2,500, 여권 제시 시 ¥2,400", "key")}
    {tl("13:00", "셔틀 → 야스기역 → 요나고", "미술관 발 13:00 / 13:30 셔틀", "move")}
    {tl("13:45", "점심: 규코쓰 라멘", "니쿠곳초 요나고역 앞점(肉ごっつお, 15:00까지) 또는 라멘 야마토")}
    {tl("15:00", "짐 찾고 가이케 온천으로", "요나고역 → 가이케선 버스 약 20분 · 약 ¥300 (1,000엔권까지 환전)", "move")}
    {tl("15:30", "료칸 체크인", "석식 시간을 미리 정해 두세요", "key")}
    {tl("16:30", "가이케 해변 일몰 산책", "12월 초 일몰은 오후 5시 전후")}
    {tl("18:00", "료칸 석식 · 온천", "대게(마쓰바가니) 시즌이 11/6부터 시작돼요")}
  </ol>
  </div>
  <div class="section-head"><h2>다른 코스로 바꾸려면</h2></div>
  <div class="list">
    <div class="card card-body">
      <div class="row"><strong>마쓰에성</strong><span class="chip">JR 약 30분 · ¥510</span></div>
      <p class="small muted">현존 천수각 중 하나인 국보 성. 마쓰에역에서 레이크라인 버스 약 10분(¥250). 천수각 8:30–17:00, 성인 ¥1,200.</p>
    </div>
    <div class="card card-body">
      <div class="row"><strong>미즈키 시게루 로드</strong><span class="chip">JR 약 45분 · ¥330</span></div>
      <p class="small muted">요괴 동상이 늘어선 사카이미나토 거리. 기타로 래핑 열차가 다녀요. 기념관 9:30–17:00, ¥1,000.</p>
    </div>
  </div>
</section>
"""
page("day2.html", "요나고 DAY 2", day2, "plan", back="/", header="일정")

day3 = day_tabs("day3") + f"""
<section class="section">
  <div><div class="eyebrow">DAY 3 · 12월 2일 수요일</div><h2 style="font-size:24px;margin-top:4px">온천 아침, 천천히 공항으로</h2></div>
  <div class="card card-body">
  <ol class="timeline">
    {tl("07:00", "아침 온천", "체크아웃 전 한 번 더")}
    {tl("08:00", "료칸 조식", "")}
    {tl("10:00", "체크아웃", "짐은 프런트에 맡기기", "key")}
    {tl("10:30", "가이케 온천가 산책", "해변 산책로, 가이케 온천 신사, 도코엔(東光園) 정원")}
    {tl("12:00", "점심", "온천가 근처에서 가볍게")}
    {tl("13:55", "서울편 연계버스 탑승", "가이케 온천 → 공항 14:20 · ¥500 · 현금. 택시는 약 20분, 약 ¥4,500", "move")}
    {tl("14:20", "요나고 공항 도착", "출국 수속, 기념품")}
    {tl("15:50", "RS472 요나고 출발", "", "key")}
    {tl("17:40", "인천 도착", "")}
  </ol>
  </div>
  <div class="note"><span class="mk">!</span><span>연계버스는 만차면 못 탈 수 있고, 결항 시 운행하지 않아요. 짐이 많거나 여유 있게 가려면 료칸에 택시를 불러 달라고 하세요.</span></div>
</section>
"""
page("day3.html", "요나고 DAY 3", day3, "plan", back="/", header="일정")


# ---------------------------------------------------------------- 숙소 목록
stay = f"""
<section class="section">
  <div><div class="eyebrow">1박은 역 앞, 1박은 온천</div><h2 style="font-size:24px;margin-top:4px">추천 숙소 조합</h2>
  <p class="small muted" style="margin-top:6px">1인 1실 · 세금 포함 · 2026년 9월 27일 Agoda 요금</p></div>
  <div class="list">{''.join(combo_card(*c) for c in COMBOS)}</div>
</section>
<section class="section">
  <div class="section-head"><h2>숙소 한눈에 보기</h2></div>
  <div class="list">{''.join(stay_card(k) for k in HOTELS)}</div>
</section>
<section class="section">
  <div class="note info"><span class="mk">i</span><span>APA 제휴 호텔(요나고 시티가든즈 호텔)도 이 날짜에 빈방이 있어요. 싱글 기준 11/30 ¥13,500 · 12/1 ¥5,500이며 식사는 없어요. APA 공식 사이트에서 예약할 수 있어요.</span></div>
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
      <div><div class="tiny">1박 · 1인 · 세금 포함</div><div class="num" style="font-size:26px;font-weight:600">{won(h['price'])}</div></div>
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
    <div class="tiny">가는 편 · 11/30 월 · RS471</div>
    <div class="boarding">
      <div><div class="code">ICN</div><div class="time">13:20</div><div class="city">인천 제1터미널</div></div>
      <div class="mid"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 15.5 13.5 12V5.5a1.5 1.5 0 0 0-3 0V12L3 15.5V17l7.5-2v3.5L8.5 20v1.2l3.5-.9 3.5.9V20l-2-1.5V15l7.5 2z" transform="rotate(90 12 12)"/></svg><span>1시간 30분</span></div>
      <div class="end"><div class="code">YGJ</div><div class="time">14:50</div><div class="city">요나고 기타로</div></div>
    </div>
    <div class="perf"></div>
    <div class="tiny">오는 편 · 12/2 수 · RS472</div>
    <div class="boarding">
      <div><div class="code">YGJ</div><div class="time">15:50</div><div class="city">요나고 기타로</div></div>
      <div class="mid"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 15.5 13.5 12V5.5a1.5 1.5 0 0 0-3 0V12L3 15.5V17l7.5-2v3.5L8.5 20v1.2l3.5-.9 3.5.9V20l-2-1.5V15l7.5 2z" transform="rotate(90 12 12)"/></svg><span>1시간 50분</span></div>
      <div class="end"><div class="code">ICN</div><div class="time">17:40</div><div class="city">인천 제1터미널</div></div>
    </div>
    <div class="perf"></div>
    <div class="row"><span class="small muted">Agoda 왕복 · 1인 · 세금 포함</span><span class="num" style="font-size:20px;font-weight:600">₩203,491</span></div>
    <p class="tiny">위탁 수하물 포함 여부는 예약 전에 확인하세요.</p>
  </div>
</section>

<section class="section">
  <div class="section-head"><h2>공항 ↔ 시내</h2></div>
  <div class="card card-body">
    <div class="row"><strong>서울편 연계버스</strong><span class="chip accent">추천</span></div>
    <dl class="kv">
      <dt>도착일</dt><dd>공항 7번 15:50 → 가이케 온천 16:15 → 요나고역 북口 16:35</dd>
      <dt>귀국일</dt><dd>요나고역 13:35 → 가이케 온천 13:55 → 공항 14:20</dd>
      <dt>요금</dt><dd>요나고역 ¥640 · 가이케 온천 ¥500 · 현금</dd>
    </dl>
    <p class="tiny">요나고 공항 공식 시간표 기준. 서울편이 결항하면 운행하지 않고, 만차면 못 탈 수 있어요.</p>
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
  <div><div class="eyebrow">1인 기준</div><h2 style="font-size:24px;margin-top:4px">여행 예산</h2></div>
  <div class="card card-body">
    <div class="tiny">2박째 숙소</div>
    <div class="seg" role="group" aria-label="2박째 숙소 선택">
      <button type="button" data-combo="tensui" aria-pressed="false">텐스이</button>
      <button type="button" data-combo="kikuman" aria-pressed="true">기쿠만</button>
      <button type="button" data-combo="fuga" aria-pressed="false">후가</button>
    </div>
    <label class="row small" for="rate" style="margin-top:4px"><span class="muted">환율 (100엔당 원)</span>
      <input id="rate" type="number" inputmode="decimal" value="861" min="500" max="2000" step="0.1"
        style="width:96px;height:36px;border-radius:10px;border:1px solid var(--line);background:var(--surface-2);color:var(--ink);padding:0 10px;font:600 15px var(--num);text-align:right"></label>
    <p class="tiny" id="rate-src">2026-09-27 기준 환율 (100엔 ≈ 861원)</p>
  </div>
  <div class="card">
    <div class="table-wrap" style="padding:4px 16px">
    <table class="money">
      <tr><td>항공권 왕복 (에어서울)</td><td>₩203,491</td></tr>
      <tr><td id="stay-name">숙소 2박</td><td id="stay-amt">-</td></tr>
      <tr><td>공항 연계버스 (도착 ¥640 + 귀국 ¥500)</td><td data-yen="1140">-</td></tr>
      <tr><td>JR 요나고↔야스기 왕복</td><td data-yen="400">-</td></tr>
      <tr><td>가이케선 버스</td><td data-yen="300">-</td></tr>
      <tr><td>아다치 미술관 (여권 할인)</td><td data-yen="2400">-</td></tr>
      <tr><td>점심 2번 · 간식 · 라멘</td><td data-yen="5000">-</td></tr>
      <tr><td class="muted">현지 지출 합계</td><td id="yen-sum" class="muted">-</td></tr>
      <tr class="sum"><td>1인 합계</td><td id="total">-</td></tr>
      <tr><td class="muted">2명 (각자 1실 기준)</td><td id="total-2" class="muted">-</td></tr>
    </table>
    </div>
  </div>
  <p class="tiny">석식·조식은 두 숙소 모두 포함이라 따로 넣지 않았어요. 환율은 페이지를 열 때 최신값으로 바뀌고, 직접 고쳐 넣을 수도 있어요.</p>
</section>
"""
page("budget.html", "요나고 예산", budget, "money", header="예산")


# ---------------------------------------------------------------- 먹거리
food = """
<section class="section">
  <div><div class="eyebrow">요나고에서 먹을 것</div><h2 style="font-size:24px;margin-top:4px">규코쓰 라멘과 대게</h2></div>
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
  <div class="note info"><span class="mk">i</span><span>마쓰바가니(대게) 시즌은 2026년 11월 6일부터 2027년 3월 20일까지예요.</span></div>
</section>
"""
page("food.html", "요나고 먹거리", food, "home", back="/", header="먹거리")


# ---------------------------------------------------------------- 체크리스트
ITEMS = [
    ("여권 (유효기간 6개월 이상 권장)", "p1"), ("항공권 e-티켓", "p2"), ("숙소 예약 확인서 2곳", "p3"),
    ("Visit Japan Web 입국 정보 등록", "p4"), ("엔화 현금 · 동전 (버스는 현금)", "p5"),
    ("해외 결제 카드", "p6"), ("eSIM 또는 로밍", "p7"), ("110V 돼지코 어댑터", "p8"),
    ("방풍 겉옷 · 접이식 우산", "p9"), ("료칸 석식 시간 · 도착 시간 알리기", "p10"),
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
