---
title: UI&UX 총정리
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [html, css, javascript, bootstrap, jquery, frontend, curriculum, study-log]
sources:
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md"
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductDetail.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html"
status: growing
confidence: high
---

# UI&UX 총정리

## 한 줄 요약

UI&UX 과목은 HTML 문서 구조 → CSS 선택자/박스 모델/레이아웃 → Bootstrap form/grid → JavaScript DOM 상품 페이지 → jQuery 상호작용으로 이어지는, 이후 [[entities/react|React]]와 [[entities/spring-boot|Spring Boot]] 웹서비스 구현의 화면 기초 과정이다.

## 이 자료의 위치

`UI&UX 총정리.md`, `속성들.md`, `태그들.md`는 날짜별 수업을 대체하는 파일이 아니라, 2026-03-23~03-27에 흩어진 HTML/CSS/JavaScript/Bootstrap/jQuery 문법을 다시 찾기 쉽게 묶은 복습 허브다. 날짜 귀속과 실제 구현 순서는 날짜별 원본을 우선하고, 총정리는 빠른 회상과 용어 확인에 사용한다.

## 큰 흐름

이 순서는 임의의 기술 나열이 아니다. **구조를 만들 수 있어야(HTML) 대상을 선택해 배치할 수 있고(CSS), 정적 화면을 이해해야 미리 정의된 class를 조합할 수 있으며(Bootstrap), 화면 요소와 데이터를 연결한 다음에야(JavaScript/DOM) 같은 조작을 더 짧게 표현하는 라이브러리(jQuery)를 비교할 수 있다.**

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

> [!NOTE] 원본 정정
> `태그들.md`에는 `<alt>`가 목록에 들어 있지만, 실제 HTML에서 `alt`는 독립 태그가 아니라 `img` 등에 쓰는 속성이다. 날짜별 원본과 `tableExam.html`의 `<img src="..." alt="...">`를 기준으로 아래 표에서는 속성으로 정리한다.

| 범주 | 대표 태그 | 수업상 쓰임 |
|---|---|---|
| 문서 구조 | `html`, `head`, `body`, `title` | 문서 전체 틀 |
| 텍스트 | `h1~h6`, `p`, `span` | 제목·문단·짧은 범위 |
| 목록 | `ol`, `ul`, `li` | 순서/비순서 목록 |
| 표 | `table`, `thead`, `tbody`, `tr`, `th`, `td` | 장바구니/상품 목록 표 |
| 이미지/링크 | `img`, `a` | 이미지 표시, 이동 |
| 입력 | `form`, `input`, `select`, `button` | 상품 등록 양식 |

### 속성

`속성들.md`는 이름과 달리 CSS property만 모은 파일이 아니다. `bgcolor`, `text`, `style`, `src`, `href`, `value`, `min`, `alt` 같은 HTML attribute와 `width`, `border`, `position`, `overflow`, `display`, `font-family` 같은 CSS property가 함께 있다. 복습할 때는 어느 태그에 붙는 attribute인지, CSS 선언의 property인지 먼저 분류해야 한다.

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

## 대표 실습과 출처 차이

| 날짜 | 대표 artifact | 복원해야 할 흐름 |
|---|---|---|
| 03-23 | `tableExam.html` | HTML 표·이미지·링크와 CSS 테두리 연결 |
| 03-24 | `boxModelTest.html`, `undefinedEx.html`, non-Bootstrap `CartList.html` | 좌표 배치 → JavaScript 객체/배열 → 직접 CSS 화면 |
| 03-25 | non-Bootstrap/Bootstrap `CartList`, `ProductInsertForm` | 같은 구조를 직접 CSS와 framework class로 비교 |
| 03-26 | `ProductList.html`, `ProductDetail.html`, 날짜 노트의 `ProductDetailNew` | DOM 목록, 상태별 상세 UI, query string 상세 선택을 구분 |
| 03-27 | `jQueryImageTest.html` | 흑백·active·filter·thumbnail·순서 이동·style 변경 |

날짜 노트와 현재 교육 artifact는 항상 동일 버전이 아니다. 다음 차이는 오류를 조용히 통일하지 않고 provenance 차이로 남긴다.

| 날짜/총정리 표기 | 현재 artifact 또는 정확한 판단 |
|---|---|
| `<alt>` 태그 | `img`의 `alt` attribute |
| “중괄호/대괄호는 무조건 객체/배열” | 입문용 단순화이며 다른 JavaScript 문맥도 존재 |
| parameter 수 “구분자 - 1” | 총정리는 “+ 1”로 교정; 실제 key-value를 파싱해야 함 |
| `productform`, `col-sm-1/9`, `invalid-check` | 현재 HTML은 `productForm`, `col-sm-2/10`, `invalid-feedback` |
| `ProductDetailNew.html` query 흐름 | 현재 보존 `ProductDetail.html`은 loading/error/success 상태 전환 artifact |
| `.combo-image`, `.thumb-image`, `jQueryImageTestNew` | 현재 artifact는 `.menu-img`, `.thumb-img`, `jQueryImageTest.html` |

## 헷갈린 점 / 질문

- `<alt>`라는 독립 태그가 있는 것이 아니라 `alt`는 `img`에 붙는 속성이다.
- Bootstrap의 `btn`, `row`, `col-*`도 HTML `class` 속성에 쓰지만, 스타일 정의는 연결한 Bootstrap CSS가 제공한다.
- `innerHTML`은 문자열을 요소 내부 HTML로 해석하고, `createElement`·`appendChild`는 DOM 노드를 만들어 트리에 붙인다.
- POST parameter가 주소창에 직접 보이지 않는다는 사실만으로 안전한 요청이 되지는 않는다. HTTPS와 서버 검증이 별도로 필요하다.
- UI&UX에서 구현한 더미 배열·DOM 화면을 이후 React state·Spring API·DB 구현 결과와 섞어 말하지 않는다.

## 이후 과정과의 연결

### UI&UX에서 직접 구현한 범위

- 정적 HTML 문서, CSS 선택자·박스·좌표 배치
- Bootstrap CDN/class를 이용한 table·grid·form·card
- 더미 배열을 이용한 상품 목록/상세 화면과 query string
- jQuery 이벤트, class/속성 변경, 표시/숨김, 이미지 순서 변경

### 후속 과정에서 확장된 범위

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
- [[comparisons/ui-vs-ux]]
- [[comparisons/custom-css-vs-bootstrap]]
- [[concepts/html-form-controls-submission]]

## 출처

- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md`
- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md` ~ `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
