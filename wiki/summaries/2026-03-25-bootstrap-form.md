---
title: 2026-03-25 Bootstrap과 HTML Form
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [bootstrap, html, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md
  - raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf
  - raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html
status: growing
confidence: high
---

# 2026-03-25 Bootstrap과 HTML Form

## 한 줄 요약

직접 CSS를 작성하던 `B.nobootstrap` 방식과 Bootstrap class를 붙이는 `C.yesbootstrap` 방식을 비교하며, CDN·grid·form·button·select를 배운 날이다.

## 배운 내용

- Bootstrap은 HTML/CSS/JS 기반 프론트엔드 프레임워크이며, 반응형·모바일 우선 UI 구성을 돕는다.
- CDN은 가까운 서버에서 CSS/JS 파일을 가져오게 하는 연결 방식이다. 설치가 아니라 외부 파일 참조다.
- Bootstrap은 `container`, `row`, `col`, `table`, `btn`, `form-control`, `form-select`, `card` 같은 class를 사용한다.
- Form은 사용자가 입력한 데이터를 모으는 양식이며, `input`, `select`, `button`, `placeholder`, `label`과 함께 쓴다. ^[raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf]

## 핵심 실습

### 장바구니 화면: 직접 CSS vs Bootstrap

`B.nobootstrap/CartList.html`은 `.container`, `.row`, `.btn`, `.text-end`, `input[type="number"]` 등을 직접 작성해 장바구니 테이블을 만든다. 반면 `C.yesbootstrap/CartList.html`은 `table table-striped table-bordered`, `text-center`, `align-middle`, `img-thumbnail`, `form-control`, `btn btn-danger btn-sm` 같은 Bootstrap class로 같은 목적을 더 짧게 표현한다. ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html] ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html]

### 상품 등록 Form

`ProductInsertForm.html`도 직접 CSS 버전과 Bootstrap 버전이 나뉜다.

- 직접 CSS 버전: `.row`, `.label`, `.input-area`, `.error`, `.btn`을 작성한다.
- Bootstrap 버전: `row mb-3`, `col-sm-2`, `col-sm-10`, `form-control`, `form-select`, `invalid-feedback`, `btn btn-primary btn-lg`를 사용한다.
- 두 버전 모두 `FormData`, `submit` 이벤트, `preventDefault()`, `FileReader`로 이미지 미리보기를 다룬다. ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html] ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html]

## 헷갈린 점 / 질문

- `button type="submit"`은 form 제출 동작이고, `class="btn btn-primary"`는 모양이다. 동작 속성과 Bootstrap 스타일 class를 구분해야 한다.
- Bootstrap을 쓰면 CSS를 안 배워도 되는 것이 아니다. Bootstrap class는 미리 작성된 CSS 규칙을 호출하는 방식이다.
- `col-sm-2`와 `col-sm-10`처럼 12칸 grid를 기준으로 공간을 배분한다.

## 관련 페이지

- [[concepts/bootstrap-basics|Bootstrap 기본]]
- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[comparisons/library-vs-framework|Library vs Framework]]
- [[entities/bootstrap|Bootstrap]]

## 출처

- `raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf` p.13~23, p.25~34
- `raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf` p.40
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html`
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/CartList.html`
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html`
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductInsertForm.html`
