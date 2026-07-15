---
title: 직접 CSS 구현 vs Bootstrap
created: 2026-07-15
updated: 2026-07-15
type: comparison
tags: [css, bootstrap, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html"
status: growing
confidence: high
---

# 직접 CSS 구현 vs Bootstrap

## 비교 목적

UI&UX 수업은 같은 종류의 화면을 `B.nobootstrap`과 `C.yesbootstrap`에 나누어 보존했다. 이를 통해 직접 CSS 규칙을 작성하는 방식과 Bootstrap이 미리 정의한 class를 조합하는 방식을 비교할 수 있다.

## 한눈에 보기

| 항목 | 직접 CSS 구현 | Bootstrap |
|---|---|---|
| 스타일 출처 | 문서 내부 또는 external CSS에 직접 작성 | Bootstrap CSS CDN이 제공 |
| 화면 구성 | `.container`, `.row`, `.btn` 등의 규칙을 직접 정의 | `container`, `row`, `btn`, `form-control` 등을 조합 |
| 장점 | 세밀한 제어, 불필요한 규칙을 줄이기 쉬움 | 공통 UI를 빠르고 일관되게 구성 |
| 부담 | 배치·간격·색상·반응형 규칙을 직접 설계 | class 체계와 framework 규칙을 익혀야 함 |
| 수업 예 | `B.nobootstrap/CartList.html` | `C.yesbootstrap/CartList.html` |

## 실제 수업 비교

교육자료에는 파일명이 대응하는 non-Bootstrap/Bootstrap 화면 9쌍이 있다. 장바구니 화면에서 non-Bootstrap 버전은 `.container`, `.row`, `.col-4`, `.col-8`, `.btn` 등을 `<style>`에 직접 정의한다. Bootstrap 버전은 CSS CDN을 연결한 뒤 `table table-striped table-bordered`, `text-center`, `align-middle`, `form-control`, `btn btn-danger btn-sm` 같은 class를 사용한다.

상품 등록 화면도 구조적 목적은 같다. 두 버전 모두 `form`, `input`, `select`, `button`을 사용하지만, non-Bootstrap 버전은 `.label`, `.input-area`, `.error` 규칙을 직접 만들고 Bootstrap 버전은 `row mb-3`, `col-sm-*`, `form-control`, `form-select`, `invalid-feedback`을 조합한다.

## 언제 무엇을 쓰는가

### 상황 1: 빠르게 일관된 관리자 화면을 만든다

table, form, button, grid가 반복되는 화면에서는 Bootstrap class로 공통 모양과 간격을 빠르게 맞추기 좋다. 수업의 장바구니·상품 등록·상품 목록 화면이 이 경우다.

### 상황 2: 고유한 디자인과 세밀한 동작을 구현한다

Bootstrap class만으로 맞추기 어려운 고유 배치·색상·애니메이션이 필요하면 직접 CSS를 작성한다. 2026-03-27의 `transition`, hover, image class 변경처럼 상호작용에 맞춘 규칙도 직접 CSS가 필요하다.

## 함께 쓰는 관계

둘은 배타적이지 않다. Bootstrap을 기본 grid·form·button에 사용하면서, 프로젝트 고유 class와 CSS를 추가할 수 있다. 실제 교육자료도 Bootstrap class와 `style="..."` 및 별도 화면 규칙을 함께 사용한다.

## 헷갈리기 쉬운 포인트

- Bootstrap을 사용해도 HTML/CSS 지식은 필요하다. class가 어떤 display·spacing·grid 규칙을 적용하는지 이해해야 한다.
- 같은 class 이름도 정의 출처가 다를 수 있다. non-Bootstrap의 `.btn`은 수업 파일이 직접 정의하지만 Bootstrap의 `.btn`은 CDN CSS가 정의한다.
- Bootstrap을 쓰면 모든 디자인이 자동 완성되는 것이 아니다. 콘텐츠 구조, 접근성, 상태 흐름, 프로젝트 고유 스타일은 따로 설계해야 한다.
- 이 수업의 Bootstrap 실습은 CSS bundle 중심이다. modal/dropdown 같은 Bootstrap JavaScript component까지 직접 학습했다고 확대하지 않는다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[concepts/bootstrap-basics]]
- [[summaries/2026-03-25-bootstrap-form]]
- [[comparisons/library-vs-framework]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/KoreaICT/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html`
- `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html`
- `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html`
- `raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html`
