---
title: UI&UX 총정리
type: summary
created: 2026-07-03
updated: 2026-07-03
tags: [html, css, javascript, bootstrap, frontend, curriculum, study-log]
sources:
  - raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md
status: growing
confidence: medium
---

# UI&UX 총정리

## 한 줄 요약

`UI&UX 총정리`는 HTML로 구조를 만들고, CSS/Bootstrap으로 화면을 꾸미며, JavaScript/jQuery로 동작을 붙이는 프론트엔드 입문 흐름을 한 문서에 모은 복습 노트다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-03-20-database-modeling-normalization-view-index|Oracle/DB 설계]]까지는 데이터를 저장하고 조회하는 쪽을 배웠다.
- 중심 기간: [[summaries/2026-03-23-html-css-intro|2026-03-23]] ~ [[summaries/2026-03-27-jquery-ui-interaction|2026-03-27]] UI&UX 수업 흐름
- 다음 흐름: React와 Spring Boot가 분리되는 [[summaries/2026-03-30-fullstack-environment-setup|FrontEnd/BackEnd 개발 환경과 커리큘럼 전환]]으로 연결
- 주의: 원본 첫 줄의 종료일이 `2026.00.00(00)`으로 되어 있어 날짜 범위는 실제 UI&UX 수업 요약 흐름에 맞춰 2026-03-23~2026-03-27로 해석했다.

## 배운 내용

### 1. HTML: 문서 구조와 태그

총정리는 HTML을 하이퍼텍스트와 마크업 개념으로 설명하고, tag/element/attribute/value 같은 기본 용어를 정리한다. 표(`table`), 이미지, 링크, 제목, `alt`, form 입력 요소는 이후 상품 목록/상세/장바구니 화면을 만드는 기본 재료가 된다.

### 2. CSS: 선택자, 색상, 박스 모델, 배치

CSS는 HTML 대상을 선택자(selector)로 지목하고 스타일을 적용하는 언어로 정리되어 있다. 태그 선택자, class 선택자, id 선택자, inline/internal/external style, 색상 코드, 박스 모델, margin/padding, `display`, `overflow`, `z-index`, FlexBox, pseudo-class가 핵심 복습 범위다.

### 3. JavaScript: 값, 객체, 배열, DOM 조작

JavaScript는 HTML 안의 `<script>`에서 시작해 객체, 배열, 함수, template string, arrow function, `forEach`, console, DOM 조작으로 확장된다. 총정리의 상품 배열 반복 예시는 이후 React에서 배열을 화면 컴포넌트로 렌더링하는 흐름의 전 단계다.

### 4. Bootstrap과 form UI

Bootstrap은 HTML/CSS/JS 기반 프레임워크로, 반응형(responsive), mobile-first, grid, form, button, card 같은 UI 구성을 빠르게 만든다. 총정리에서는 `form`, `select`, button, label/input-area 조합이 입력 양식의 중심으로 정리되어 있다.

### 5. jQuery와 상호작용

날짜별 UI&UX 학습에서는 jQuery로 선택자, 이벤트, class/속성 조작, show/hide 같은 상호작용을 다뤘다. 총정리에는 JavaScript 중심 내용이 더 많이 남아 있으므로, jQuery는 [[concepts/jquery-basics|jQuery 기본]]과 날짜별 요약을 함께 보는 것이 좋다.

## 헷갈린 점 / 질문

- HTML은 구조, CSS는 표현, JavaScript는 동작을 담당한다. Bootstrap은 이 중 특히 화면 구성과 반응형 UI를 빠르게 만드는 도구다.
- `<table>`은 표 데이터 구조에 적합하지만, 전체 화면 레이아웃 용도로 남용하면 유지보수가 어렵다.
- `class` 선택자는 여러 요소에 재사용할 수 있고, `id` 선택자는 한 문서에서 특정 요소를 가리키는 데 쓴다.
- JavaScript의 template string과 arrow function은 문법이 낯설지만, React/TypeScript 코드에서 계속 등장하므로 초반에 익숙해질 필요가 있다.

## 관련 페이지

- [[entities/html|HTML]]
- [[entities/css|CSS]]
- [[entities/javascript|JavaScript]]
- [[entities/bootstrap|Bootstrap]]
- [[entities/jquery|jQuery]]
- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[concepts/bootstrap-basics|Bootstrap 기본]]
- [[comparisons/inline-style-vs-internal-css-vs-external-css|inline style vs internal CSS vs external CSS]]
- [[comparisons/library-vs-framework|Library vs Framework]]

## 출처

- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
