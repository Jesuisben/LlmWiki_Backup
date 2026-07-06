---
title: Bootstrap 기본
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [bootstrap, css, frontend]
sources:
  - "raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md"
  - "raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
status: growing
confidence: high
---

# Bootstrap 기본

## 정의

Bootstrap은 미리 만들어진 CSS/JavaScript UI 규칙을 class 이름으로 가져다 쓰게 해주는 프론트엔드 프레임워크다. 수업에서는 CDN으로 연결해 table, button, grid, form, card를 빠르게 구성했다.

## 이 수업에서의 맥락

UI&UX 수업은 먼저 직접 CSS로 table과 box를 만들고, 그 다음 Bootstrap을 사용했다. 그래서 Bootstrap은 “CSS를 몰라도 되는 마법”이 아니라, 이미 배운 CSS 선택자와 class 개념을 바탕으로 남이 만들어 둔 class를 조합하는 도구로 이해해야 한다.

## 핵심 설명

### CDN으로 불러온다

HTML 문서의 `head` 등에 Bootstrap CSS CDN을 연결하면, `btn`, `container`, `row`, `col-*`, `form-control` 같은 class가 의미를 갖는다.

### class 조합으로 스타일을 적용한다

```html
<button class="btn btn-primary">Submit</button>
```

이 버튼은 HTML의 class 속성에 Bootstrap이 정의한 class 이름을 여러 개 넣은 것이다. 사용자가 직접 `.btn`을 작성한 것이 아니라 Bootstrap CSS 파일에 이미 있다.

### Grid system은 12칸 기준이다

수업에서는 `container`, `row`, `col-sm-1`, `col-sm-9`를 사용해 label과 input의 공간을 나눴다.

- `container`: 전체 영역
- `row`: 한 줄
- `col-*`: 열의 폭

### Form class는 입력 양식을 정돈한다

`form-control`, `mb-3`, `mt-3`, `col-form-label`, `btn`, `btn-primary`를 사용해 `ProductInsertForm`을 만들었다.

### Card와 상품 목록

상품 목록에서는 Bootstrap card/grid를 이용해 상품 이미지를 포함한 목록 화면을 만든다. 이후 2026-03-26 JavaScript DOM 실습에서 배열 데이터를 반복해 card를 생성한다.

## 예시

```html
<div class="container my-4">
  <div class="row">
    <div class="col-md-4 mb-4">상품 카드</div>
  </div>
</div>
```

## 자주 헷갈리는 점

- Bootstrap class도 결국 HTML의 `class` 속성이다. 다만 CSS 정의를 내가 쓰지 않고 Bootstrap이 제공한다.
- Bootstrap을 쓰면 빨라지지만, class 이름의 의미와 grid 구조를 모르면 화면이 왜 그렇게 배치되는지 알기 어렵다.
- jQuery와 Bootstrap은 모두 프론트엔드 도구지만 역할이 다르다. Bootstrap은 UI 모양/컴포넌트, jQuery는 DOM 선택/이벤트 조작에 가깝다.

## 관련 개념

- [[entities/bootstrap]]
- [[concepts/html-css-basics]]
- [[concepts/javascript-dom]]
- [[comparisons/library-vs-framework]]
- [[summaries/2026-03-25-bootstrap-form]]

## 출처

- `raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
