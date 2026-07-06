---
title: JavaScript와 DOM
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [javascript, frontend]
sources:
  - "raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
status: growing
confidence: high
---

# JavaScript와 DOM

## 정의

JavaScript는 브라우저에서 HTML 문서를 동적으로 바꾸는 언어이고, DOM(Document Object Model)은 HTML 문서를 JavaScript가 조작할 수 있는 객체 트리로 표현한 것이다.

## 왜 중요한가

정적인 HTML만으로는 상품 목록, 상세 보기, 버튼 클릭, 입력값 처리 같은 상호작용을 만들기 어렵다. JavaScript와 DOM을 이해해야 이후 React에서 배열 렌더링, 이벤트, state 변경을 배울 때 “왜 화면이 바뀌는지”를 연결할 수 있다.

## 핵심 설명

### document는 HTML 문서 자체를 가리킨다

원본은 `document`를 HTML 문서 자체인 객체로 설명한다. `document.getElementById("output")`은 HTML에서 `id="output"`인 요소를 찾아 JavaScript 변수에 연결한다.

```javascript
let output = document.getElementById("output");
output.innerHTML += '타이틀 : 자바스크립트<br>';
```

### 객체와 배열은 화면 데이터가 된다

원본은 중괄호 `{}`를 객체, 대괄호 `[]`를 배열로 설명한 뒤, 상품 목록에서 배열 안에 상품 객체를 넣는다.

```javascript
const products = [
  { id: 1, name: '아메리카노', price: 4000 }
];
```

이 데이터는 이후 `forEach`로 반복되며 HTML card가 된다.

### forEach와 template string

`forEach`는 배열 요소를 하나씩 꺼내 처리한다. template string은 백틱과 `${}`를 사용해 HTML 문자열 안에 데이터를 넣는다.

```javascript
products.forEach((item) => {
  col.innerHTML = `<h5>${item.name}</h5>`;
});
```

### createElement와 appendChild

DOM 조작의 수업 핵심 흐름은 다음과 같다.

```javascript
const container = document.getElementById("productContainer");
const col = document.createElement("div");
col.className = "col-md-4 mb-4";
col.innerHTML = `<h5>상품명</h5>`;
container.appendChild(col);
```

이것은 HTML 파일에 태그를 직접 쓰지 않고, 실행 중에 JavaScript가 새 요소를 만들어 부모 안에 붙이는 방식이다.

### 이벤트는 브라우저에서 발생하는 사건이다

클릭, 로딩 완료, 키보드 입력, select 값 변경 등이 이벤트다. 이벤트 핸들러는 “그 사건이 발생하면 실행할 함수”다.

```html
<button onclick="register()">상품 등록</button>
```

### URLSearchParams와 상세 페이지

상품 목록에서 `ProductDetail.html?id=1`처럼 이동하고, 상세 페이지에서 `URLSearchParams`로 `id`를 꺼내는 흐름을 배웠다. 이는 GET query string과도 연결된다.

## 예시: 상품 목록 렌더링 흐름

1. 상품 배열을 준비한다.
2. `productContainer`를 DOM에서 찾는다.
3. 배열을 `forEach`로 돈다.
4. 상품마다 `div`를 만든다.
5. Bootstrap card HTML을 `innerHTML`로 넣는다.
6. `appendChild`로 화면에 추가한다.
7. 버튼 클릭 이벤트로 상세/수정/삭제 동작을 연결한다.

## 자주 헷갈리는 점

- `innerHTML`은 HTML 문자열을 넣는 속성이다. 단순 텍스트만 넣는 것이 아니다.
- `createElement`로 만든 객체는 아직 화면에 붙지 않았다. `appendChild`를 해야 보인다.
- `this`와 `event`는 이벤트가 발생했을 때의 대상/상황을 가리킨다.
- jQuery는 이 DOM 조작을 짧게 쓰게 해주는 라이브러리다. 비교는 [[comparisons/javascript-dom-vs-jquery]].

## 관련 개념

- [[entities/javascript]]
- [[concepts/jquery-basics]]
- [[concepts/bootstrap-basics]]
- [[comparisons/get-vs-post]]
- [[summaries/2026-03-26-javascript-dom-product-pages]]

## 출처

- `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
