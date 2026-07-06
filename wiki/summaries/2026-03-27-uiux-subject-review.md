---
title: UI&UX 총정리
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [html, css, javascript, bootstrap, jquery, frontend, curriculum, study-log]
sources:
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/속성들.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/태그들.md"
  - "raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
status: growing
confidence: high
---

# UI&UX 총정리

## 한 줄 요약

UI&UX 과목은 HTML 문서 구조 → CSS 선택자/박스 모델/레이아웃 → Bootstrap form/grid → JavaScript DOM 상품 페이지 → jQuery 상호작용으로 이어지는, 이후 [[entities/react|React]]와 [[entities/spring-boot|Spring Boot]] 웹서비스 구현의 화면 기초 과정이다.

## 이 자료의 위치

`UI&UX 총정리.md`, `속성들.md`, `태그들.md`는 날짜별 수업을 대체하는 파일이 아니라, 2026-03-23~03-27에 흩어진 HTML/CSS/JavaScript/Bootstrap/jQuery 문법을 다시 찾기 쉽게 묶은 복습 허브다. 이번 재ingest에서는 사용자가 다시 변환한 현재 MD들을 기준으로 기존 wiki를 전면 재작성했다.

## 큰 흐름

### 1. HTML: 문서의 뼈대

HTML은 브라우저가 읽는 문서 구조다. 총정리 원본은 `html`, `head`, `body`, `title`, `h1~h6`, `p`, `span`, `div`, `ol`, `ul`, `li`, `table`, `thead`, `tbody`, `tr`, `th`, `td`, `img`, `a`, `form`, `input`, `select`, `button` 등을 묶어 정리한다.

핵심은 태그를 외우는 것보다 “이 태그가 문서에서 어떤 역할을 하는가”다. 예를 들어 `table`은 행/열 데이터, `form`은 입력 양식, `div`는 영역 분할, `span`은 짧은 인라인 범위다.

### 2. CSS: 선택하고 꾸민다

CSS는 선택자로 대상을 고른 뒤 속성과 값을 준다.

```css
.myyellow {
  color: yellow;
  background-color: black;
}
```

총정리 원본은 태그 선택자, class 선택자, id 선택자, 그룹 선택자, 속성 선택자, pseudo-class, inline/internal/external CSS, Box Model, `position`, `overflow`, `display`, `z-index`, `font-family`, `line-height`, `text-decoration`, 단위(px, %)를 다룬다.

### 3. Bootstrap: class로 빠르게 화면 구성

Bootstrap은 미리 정의된 class를 사용해 table, button, form, grid, card를 빠르게 만든다. `container`, `row`, `col-*`, `btn`, `btn-primary`, `form-control`, `table` 같은 class가 반복된다.

이 수업에서는 직접 CSS로 만든 화면과 Bootstrap으로 만든 화면을 나란히 경험하면서 “내가 CSS를 직접 작성하는 경우”와 “프레임워크 class를 조합하는 경우”를 비교했다.

### 4. JavaScript: HTML을 동적으로 바꾼다

JavaScript는 `document` 객체를 통해 HTML 문서를 조작한다. 총정리 원본은 `getElementById`, `innerHTML`, 객체/배열, `forEach`, template string, arrow function, `createElement`, `appendChild`, 이벤트, `URLSearchParams`를 상품 목록/상세 페이지 예제로 묶는다.

이 단계에서 HTML은 고정 문서가 아니라 데이터에 따라 바뀌는 화면이 된다.

### 5. jQuery: 선택자+이벤트를 짧게 쓴다

jQuery는 JavaScript 라이브러리다. `$()`로 요소를 선택하고, `click`, `change`, `toggleClass`, `addClass`, `removeClass`, `show`, `hide`, `attr` 등을 사용해 이미지 UI를 조작한다.

## 태그/속성 복습 포인트

### 태그

`태그들.md`는 자주 쓰는 HTML 태그를 짧게 모은다. 복습할 때는 다음처럼 기능별로 묶는 것이 좋다.

| 범주 | 대표 태그 | 수업상 쓰임 |
|---|---|---|
| 문서 구조 | `html`, `head`, `body`, `title` | 문서 전체 틀 |
| 텍스트 | `h1~h6`, `p`, `span` | 제목·문단·짧은 범위 |
| 목록 | `ol`, `ul`, `li` | 순서/비순서 목록 |
| 표 | `table`, `thead`, `tbody`, `tr`, `th`, `td` | 장바구니/상품 목록 표 |
| 이미지/링크 | `img`, `a` | 이미지 표시, 이동 |
| 입력 | `form`, `input`, `select`, `button` | 상품 등록 양식 |

### 속성

`속성들.md`는 CSS 속성을 중심으로 정리한다. `width`, `border`, `position`, `overflow`, `display`, `list-style-position`, `vertical-align`, `font-family`, `font-style`, `line-height`가 날짜별 실습과 연결된다.

복습할 때는 속성을 단독 암기하지 말고 다음 질문으로 묶어 보는 것이 좋다.

- 크기: `width`, `height`
- 테두리: `border`, `border-top`, `border-left`
- 배치: `position`, `top`, `left`, `z-index`
- 넘침/표시: `overflow`, `display`
- 목록: `list-style-type`, `list-style-position`
- 텍스트: `font-family`, `font-style`, `line-height`, `text-decoration`

## 날짜별 복습 경로

1. [[summaries/2026-03-23-html-css-intro|2026-03-23]] — 웹 흐름, HTML 태그/속성, CSS 선택자, table, Box Model 기초
2. [[summaries/2026-03-24-css-layout-javascript-intro|2026-03-24]] — div 레이아웃, position/display, JavaScript `document`와 `innerHTML`
3. [[summaries/2026-03-25-bootstrap-form|2026-03-25]] — Bootstrap CDN/grid/form/button, 상품 등록 폼
4. [[summaries/2026-03-26-javascript-dom-product-pages|2026-03-26]] — 상품 배열, DOM 생성, 이벤트, 상세 페이지, GET/POST
5. [[summaries/2026-03-27-jquery-ui-interaction|2026-03-27]] — jQuery 선택자, class/속성 조작, show/hide, 이미지 UI

## 이후 과정과의 연결

- [[entities/react|React]]에서는 JavaScript로 DOM을 직접 만지기보다 state/props로 화면을 선언적으로 바꾼다. 그러나 DOM, 이벤트, 배열 렌더링 감각은 그대로 이어진다.
- [[entities/spring-boot|Spring Boot]]와 연결될 때 form, GET/POST, URL parameter 개념이 Controller/API 요청 이해의 기반이 된다.
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]에서 UI&UX 과목은 프론트엔드 화면 층의 가장 낮은 기초다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[concepts/javascript-dom]]
- [[concepts/bootstrap-basics]]
- [[concepts/jquery-basics]]
- [[comparisons/html-tag-vs-attribute]]
- [[comparisons/id-vs-class]]
- [[comparisons/javascript-dom-vs-jquery]]

## 출처

- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/속성들.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/태그들.md`
- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md` ~ `raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
