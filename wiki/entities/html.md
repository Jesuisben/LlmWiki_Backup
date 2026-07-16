---
title: HTML
created: 2026-07-02
updated: 2026-07-15
type: entity
tags: [html, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html"
status: growing
confidence: high
---

# HTML

## 무엇인가

HTML(Hyper Text Markup Language)은 브라우저가 해석하는 웹 문서의 구조를 만드는 마크업 언어다.

## 이 위키에서의 맥락

UI&UX 과목 첫날인 2026-03-23에 Java/Oracle 이후 화면 개발의 출발점으로 등장했다. 이 수업에서는 HTML을 태그 암기가 아니라 `table`, `form`, `img`, `a`, `div`, `span` 등 화면 구조의 역할로 배웠다.

## 핵심 기능 / 특징

- 문서 구조: `html`, `head`, `body`, `title`
- 텍스트: `h1~h6`, `p`, `span`
- 목록: `ol`, `ul`, `li`
- 표: `table`, `thead`, `tbody`, `tr`, `th`, `td`
- 입력: `form`, `input`, `select`, `button`
- 링크/이미지: `a`, `img`, `alt`, `src`

`alt`는 태그가 아니라 `img`의 속성이다. `태그들.md`의 `<alt>` 표기는 날짜별 원본과 실제 `tableExam.html`에 맞춰 이 페이지에서는 속성으로 정정한다.

## 화면 구현 역할

HTML은 “무엇을 보여 줄지”와 “입력받을 구조가 무엇인지”를 정한다. 수업의 table은 데이터를 행·열로 표시했고, form/input/select/button은 상품 등록 입력 구조를 만들었다. CSS·Bootstrap이 모양을 바꾸고 JavaScript·jQuery가 동작을 붙여도, 조작 대상 자체는 HTML 요소다.

## 프로젝트·면접 설명 관점

- 프로젝트: 상품 목록은 반복 가능한 card/table 구조, 상품 등록은 label과 form control 구조로 먼저 설계한다고 설명할 수 있다.
- 면접: HTML을 프로그래밍 언어가 아니라 문서의 구조와 의미를 표현하는 markup language라고 설명하고, tag·attribute·element를 구분한다.
- 범위 경계: UI&UX 과목은 정적 문서와 브라우저 내 더미 데이터 화면까지 구현했다. 서버 렌더링·React component는 후속 확장이다.

## 관련 개념

- [[concepts/html-css-basics]]
- [[comparisons/html-tag-vs-attribute]]
- [[comparisons/id-vs-class]]
- [[concepts/html-form-controls-submission]]
- [[entities/css]]
- [[entities/javascript]]

## 학습 이력

- [[summaries/2026-03-23-html-css-intro]] — HTML 태그, 속성, table, 이미지, CSS 선택자 입문
- [[summaries/2026-03-24-css-layout-javascript-intro]] — div 영역을 CSS 좌표 배치와 JavaScript 선택 대상으로 사용
- [[summaries/2026-03-25-bootstrap-form]] — form/input/select/button으로 상품 등록 양식 구성
- [[summaries/2026-03-26-javascript-dom-product-pages]] — JavaScript가 HTML 요소를 찾아 동적으로 변경

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
