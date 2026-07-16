---
title: Bootstrap
created: 2026-07-02
updated: 2026-07-15
type: entity
tags: [bootstrap, frontend, css]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html"
status: growing
confidence: high
---

# Bootstrap

## 무엇인가

Bootstrap은 반응형 레이아웃, 버튼, 표, form, card 같은 UI 요소를 미리 정의된 class로 빠르게 구성하게 해주는 프론트엔드 프레임워크다.

## 이 위키에서의 맥락

UI&UX 수업에서는 직접 CSS로 만든 장바구니/상품 화면을 Bootstrap class 기반 화면으로 바꾸며 학습했다. 이후 React Bootstrap과 프로젝트 화면 구성으로 이어진다.

## 핵심 기능 / 특징

- CDN으로 CSS/JS를 불러와 빠르게 시작한다.
- `container`, `row`, `col-*`로 grid 레이아웃을 만든다.
- `btn`, `btn-primary`, `btn-danger`로 버튼 스타일을 적용한다.
- `form-control`, `col-form-label`로 form을 정돈한다.
- `card`, `img-fluid`, margin/padding utility class로 상품 목록 UI를 구성한다.

## 화면 구현 역할

2026-03-25에는 non-Bootstrap form/table을 먼저 만든 뒤 Bootstrap CDN과 class를 적용했다. 2026-03-26에는 `row`, `col-md-4`, `card`, 버튼 class를 JavaScript로 생성하는 상품 목록에 결합했다. 2026-03-27 교육자료에서는 form control과 image utility class가 jQuery 상호작용의 화면 모양을 담당했다.

## 프로젝트·면접 설명 관점

- 프로젝트: 레이아웃·spacing·button 상태를 utility/component class로 빠르게 통일하되, class가 생성하는 실제 CSS를 확인한다고 설명할 수 있다.
- 면접: Bootstrap은 HTML 자체를 대신하지 않는다. HTML `class` 속성에 미리 정의된 CSS/UI 규칙을 조합하는 프론트엔드 프레임워크다.
- 범위 경계: UI&UX에서는 CDN 기반 Bootstrap 5 HTML을 직접 사용했다. React Bootstrap component 사용은 후속 범위다.

## 관련 개념

- [[concepts/bootstrap-basics]]
- [[concepts/html-css-basics]]
- [[comparisons/library-vs-framework]]
- [[comparisons/custom-css-vs-bootstrap]]
- [[entities/css]]
- [[entities/javascript]]

## 학습 이력

- [[summaries/2026-03-25-bootstrap-form]] — Bootstrap CDN, grid, form, button
- [[summaries/2026-03-26-javascript-dom-product-pages]] — Bootstrap card/grid로 상품 목록·상세 화면 구성
- [[summaries/2026-03-27-jquery-ui-interaction]] — jQuery와 함께 이미지 UI 실습에 사용

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
