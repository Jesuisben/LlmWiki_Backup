---
title: 2026-03-24 CSS 레이아웃과 JavaScript 입문
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [html, css, javascript, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md
  - raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf
  - raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html
status: growing
confidence: high
---

# 2026-03-24 CSS 레이아웃과 JavaScript 입문

## 한 줄 요약

HTML 요소를 block/inline과 Box Model로 이해하고, `position`, `display`, `float`, `font`를 다룬 뒤 JavaScript로 HTML을 조작하는 첫 실습까지 확장한 날이다.

## 배운 내용

- block element는 한 줄을 차지하고 width/height 제어가 쉽다. 예: `<p>`, `<div>`
- inline element는 콘텐츠 크기만큼 차지하고 옆으로 배치된다. 예: `<span>`
- Box Model은 `content → padding → border → margin` 구조로 요소의 크기와 여백을 이해하는 방식이다. ^[raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf]
- `position: relative`인 부모 안에서 `position: absolute` 자식의 `top`, `left`가 어떻게 계산되는지 실습했다.
- `overflow`, `display`, `z-index`, `float`, `list-style`, `font-family`, `line-height`, `font` 단축 속성을 다뤘다.
- 후반에는 `<script>` 태그에서 `document.getElementById`, `innerHTML`, `undefined`, `==`/`===`, 객체/배열을 맛봤다.

## 핵심 실습

### boxModelTest

`boxModelTest.html`에서는 `#mydiv`를 부모 컨테이너로 두고, `.test1`~`.test4`를 절대 위치로 배치했다.

- 부모 `#mydiv`: `position: relative`, `top: 10px`, `left: 10px`, `width: 300px`, `height: 300px`
- 자식 `div`: `position: absolute`, `top`, `left`, `bottom`으로 위치 지정
- 핵심은 자식의 좌표가 화면 전체가 아니라 기준이 되는 부모 박스에 의해 해석될 수 있다는 점이다. ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html]

### JavaScript 첫 DOM 조작

빈 `<div id="output"></div>`를 `document.getElementById("output")`로 가져오고, `innerHTML`에 문자열을 더해 화면에 표시했다. 이때 `output`은 문자열이 아니라 HTML 요소 객체다.

## 헷갈린 점 / 질문

- `padding: 10px 10px 5px 10px`은 위→오른쪽→아래→왼쪽, 즉 시계 방향 순서다.
- `em`은 부모/현재 폰트 크기를 기준으로 하고, `rem`은 HTML 기본 폰트 크기를 기준으로 한다.
- `==`는 암시적 형변환을 허용하지만, `===`는 값과 타입이 모두 같아야 한다.
- JavaScript에서 `{}`는 객체, `[]`는 배열이라는 감각은 이후 상품 데이터 배열로 이어진다.

## 관련 페이지

- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[comparisons/inline-style-vs-internal-css-vs-external-css|inline style vs internal CSS vs external CSS]]

## 출처

- `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf` p.68, p.86, p.102~103
- `raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf` p.8~12
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html`
