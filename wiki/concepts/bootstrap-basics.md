---
title: Bootstrap 기본
created: 2026-06-30
updated: 2026-07-02
type: concept
tags: [bootstrap, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md
  - raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md
  - raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md
  - raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md
status: growing
confidence: high
---

# Bootstrap 기본

## 정의

Bootstrap은 HTML, CSS, JavaScript 기반의 프론트엔드 프레임워크다. 버튼, 테이블, 폼, 카드, 그리드 같은 UI 구성 요소와 반응형 레이아웃 규칙을 미리 제공해, 직접 CSS를 모두 작성하지 않아도 일관된 화면을 빠르게 만들 수 있게 한다.

## 이 수업에서의 맥락

UI&UX 수업 첫날부터 Bootstrap은 “UI 라이브러리”로 언급되었고, 2026-03-25에는 Bootstrap 5를 CDN으로 불러와 장바구니 목록, 상품 등록 폼, 상품 카드 화면을 만드는 방식으로 본격 실습했다. 이전날 CSS를 직접 작성해 `B_nobootstrap` 폴더에서 화면을 만들었다면, Bootstrap 실습에서는 `C_yesbootstrap` 폴더에서 같은 종류의 화면을 class 조합으로 빠르게 만들었다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md] ^[raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md]

## 핵심 설명

### Bootstrap은 반응형·모바일 우선 프레임워크다

수업에서는 Bootstrap의 핵심 특징을 responsive, 즉 장치 크기에 따라 화면이 다르게 보이는 것으로 정리했다. 예를 들어 화면 크기가 달라지면 메뉴 모양이 바뀌거나, 칸의 배치가 바뀔 수 있다. 또한 모바일 우선 프레임워크라는 점도 언급되었다. ^[raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md]

### CDN으로 CSS/JS 파일을 불러온다

CDN(Content Delivery Network)은 같은 소스코드 복제본을 여러 지역에 두고 가까운 곳에서 가져오게 하는 방식이다. 수업에서는 W3Schools의 Bootstrap 예제를 열어 CSS와 JS 주소를 확인하고, HTML의 `<head>`에 CSS 링크를 붙여 사용하는 흐름을 배웠다.

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
```

장점은 설치 없이 최신 파일을 쉽게 쓸 수 있다는 것이고, 단점은 인터넷이 안 되면 외부 CDN을 불러올 수 없다는 것이다. ^[raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md]

### Bootstrap class는 미리 만들어진 CSS 규칙을 가져다 쓰는 방식이다

수업에서 “부트스트랩이 대부분 class 선택자를 사용한다”는 메모가 있었다. 예를 들어 직접 `.btn-primary`의 배경색을 매번 작성하지 않고, HTML 요소에 class를 붙여 준비된 스타일을 적용한다.

```html
<button type="submit" class="btn btn-primary">Submit</button>
```

이 구조는 [[concepts/html-css-basics|HTML/CSS 기본]]에서 배운 class 선택자가 Bootstrap 사용의 기초임을 보여준다. ^[raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md]

### container, row, col은 레이아웃의 기본 단위다

Bootstrap의 행렬 구조는 `row`와 `col`로 설명되었다. 수업에서는 상품 이미지와 텍스트를 한 영역 안에서 나누기 위해 다음 구조를 다뤘다.

```html
<td>
    <div class="row">
        <div class="col-4">이미지</div>
        <div class="col-8">아메리카노</div>
    </div>
</td>
```

이후 Bootstrap grid system에서는 12컬럼을 기준으로 `col-sm-1`, `col-sm-9`처럼 공간을 나누는 방식도 배웠다. 설정하지 않은 나머지 컬럼은 빈 공간으로 남을 수 있다는 설명이 있었다. ^[raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md]

### Form과 버튼은 이후 백엔드 전송 흐름으로 연결된다

상품 등록 폼 실습에서는 `<form>`, `<label>`, `<input>`, `<select>`, `<button>`을 Bootstrap class와 함께 구성했다.

```html
<form id="productform">
    <div class="mb-3 mt-3">
        <label for="name">이름</label>
        <input type="text" class="form-control" id="name" placeholder="이름 입력" name="name">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

수업에서는 `button type="submit"`은 나중에 form 데이터를 제출할 곳을 지정하면 그곳으로 데이터가 날아가는 버튼이고, `type="button"`은 일반 버튼, `type="reset"`은 입력값을 초기화하는 버튼이라고 구분했다. ^[raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md]

### Bootstrap은 JavaScript DOM 실습의 화면 뼈대가 되었다

2026-03-26 상품 목록 실습에서는 Bootstrap의 `container`, `my-4`, `d-flex`, `justify-content-start`, `btn`, `btn-primary`, `col-md-4`, `mb-4` 같은 class를 사용해 상품 목록 페이지를 만들었다. JavaScript는 상품 배열을 반복하면서 DOM 요소를 만들고, Bootstrap class를 붙여 카드 형태로 화면에 배치했다. ^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

## 자주 헷갈리는 점

### Bootstrap을 쓰면 CSS를 몰라도 되는 것은 아니다

Bootstrap class는 결국 CSS 규칙의 묶음이다. class 선택자, 박스 모델, flex, grid 감각을 모르면 왜 화면이 그렇게 배치되는지 이해하기 어렵다. 그래서 3월 23~24일의 HTML/CSS 수업이 Bootstrap 실습의 기반이 된다.

### CDN은 설치가 아니라 외부 파일 연결이다

CDN 링크를 붙였다고 내 프로젝트 안에 Bootstrap 파일이 생긴 것은 아니다. 브라우저가 실행될 때 외부 주소에서 CSS/JS를 가져오는 방식이다.

### `submit`, `button`, `reset`은 버튼 모양이 아니라 동작 차이다

Bootstrap의 `btn btn-primary`는 모양이고, `<button type="submit">`의 `type`은 form 안에서의 동작이다. 모양 class와 HTML 동작 속성을 구분해야 한다.

## 이전/이후 학습과의 연결

- 이전: [[concepts/html-css-basics|HTML/CSS 기본]]에서 class 선택자, 박스 모델, 레이아웃을 배웠다.
- 같은 흐름: [[concepts/javascript-dom|JavaScript와 DOM]]에서 Bootstrap class가 붙은 요소를 JavaScript로 만들고 조작했다.
- 이후: React Bootstrap 수업에서는 Bootstrap 컴포넌트 사용 방식이 React 컴포넌트 구조로 확장된다.
- 프로젝트: 상품 목록, 상품 등록 폼, 상세 화면, 장바구니 목록 같은 쇼핑몰 UI의 기본 재료가 된다.

## 관련 개념

- [[entities/bootstrap|Bootstrap]]
- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[summaries/2026-03-25-bootstrap-form|2026-03-25 Bootstrap과 HTML Form]]
- [[summaries/2026-03-26-javascript-dom-product-pages|2026-03-26 JavaScript DOM과 상품 목록/상세 페이지]]

## 교육자료·소스코드 대조 보강 (2026-07-02)

이번 백필에서는 `B.nobootstrap`와 `C.yesbootstrap` 소스코드를 비교했다. `B.nobootstrap/CartList.html`은 `.container`, `.row`, `.btn`, `input[type="number"]` 등을 직접 CSS로 작성하는 반면, `C.yesbootstrap/CartList.html`은 `table table-striped table-bordered`, `img-thumbnail`, `form-control`, `btn btn-danger btn-sm` 같은 Bootstrap class로 같은 목적을 표현한다.

상품 등록 폼도 직접 CSS 버전과 Bootstrap 버전이 함께 있어, Bootstrap이 HTML/CSS를 없애는 도구가 아니라 반복 UI 규칙을 class로 표준화하는 도구임을 보여 준다. Library/Framework 관점은 [[comparisons/library-vs-framework|Library vs Framework]]에 따로 보존했다.

## 출처

- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
