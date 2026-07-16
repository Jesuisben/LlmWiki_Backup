---
title: JavaScript
created: 2026-07-02
updated: 2026-07-15
type: entity
tags: [javascript, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductDetail.html"
status: growing
confidence: high
---

# JavaScript

## 무엇인가

JavaScript는 브라우저에서 실행되어 HTML 문서를 동적으로 바꾸고 사용자 이벤트에 반응하는 프로그래밍 언어다.

## 이 위키에서의 맥락

UI&UX 과정에서는 `<script>` 태그, `document`, `getElementById`, `innerHTML`, 객체/배열, `forEach`, template string, arrow function, `createElement`, `appendChild`, 이벤트를 상품 목록/상세 페이지로 배웠다.

## 핵심 기능 / 특징

- HTML 문서를 `document` 객체로 다룬다.
- 객체 `{}`와 배열 `[]`로 화면 데이터를 표현한다.
- `forEach`로 배열을 반복해 화면 요소를 만든다.
- `innerHTML`, `createElement`, `appendChild`로 DOM을 조작한다.
- `onclick`, `DOMContentLoaded`, `URLSearchParams`로 이벤트와 URL 정보를 처리한다.

## 화면 구현 역할

2026-03-24에는 `document.getElementById`와 `innerHTML`로 기존 요소를 바꾸는 첫 조작을 했고, 2026-03-26에는 객체 배열을 `forEach`로 순회해 상품 card를 만들었다. 목록에서 id를 query string으로 넘기고 상세 문서에서 `URLSearchParams → Number → find`로 상품을 고르는 흐름까지 이어졌다.

## 프로젝트·면접 설명 관점

- 프로젝트: “데이터 배열 → 반복 → DOM 요소 생성 → 이벤트 연결”의 흐름으로 상품 목록 화면을 설명할 수 있다.
- 면접: JavaScript는 언어이고 DOM은 브라우저가 제공하는 문서 객체 모델이다. jQuery는 이 DOM API를 감싼 라이브러리다.
- 범위 경계: 수업 데이터는 HTML 안의 더미 배열이며 API 응답이 아니다. React state/props와 fetch 기반 서버 통신은 후속 과정에서 확장된다.

## 관련 개념

- [[concepts/javascript-dom]]
- [[concepts/jquery-basics]]
- [[comparisons/javascript-dom-vs-jquery]]
- [[comparisons/get-vs-post]]
- [[concepts/html-form-controls-submission]]
- [[entities/jquery]]

## 학습 이력

- [[summaries/2026-03-24-css-layout-javascript-intro]] — 변수, 비교, 객체/배열, `innerHTML` 입문
- [[summaries/2026-03-26-javascript-dom-product-pages]] — 상품 목록/상세 페이지 DOM 렌더링
- [[summaries/2026-03-27-jquery-ui-interaction]] — jQuery가 JavaScript 라이브러리임을 확인

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
