---
title: 2026-03-26 JavaScript DOM과 상품 목록/상세 페이지
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [javascript, bootstrap, frontend, curriculum]
sources:
  - "raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf"
  - "raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf"
  - "raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf"
status: growing
confidence: high
---

# 2026-03-26 JavaScript DOM과 상품 목록/상세 페이지

## 한 줄 요약

상품 배열을 만들고 `forEach`, template string, `createElement`, `appendChild`, 이벤트, URL parameter를 이용해 상품 목록과 상세 페이지를 동적으로 구성한 날이다.

## 배운 내용

### 1. 상품 데이터를 배열과 객체로 표현

원본은 `products` 배열에 상품 객체를 넣어 `id`, `name`, `price`, `image` 같은 속성을 갖게 한다. 전날 배운 “중괄호는 객체, 대괄호는 배열”이 실제 화면 데이터로 연결된 것이다.^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

```javascript
const products = [
  { id: 1, name: '아메리카노', price: 4000, image: '/images/americano01.png' }
];
```

### 2. forEach와 template string

`forEach`는 배열 요소를 하나씩 꺼내 반복 처리한다. 원본은 Java의 확장 for와 비슷하다고 연결한다.

Template string은 백틱(``)과 `${}`를 써서 문자열 안에 변수나 표현식을 넣는 방식이다. 상품 카드 HTML을 만들 때 문자열 연결보다 읽기 쉽다.

### 3. DOM 동적 생성

이날의 핵심은 HTML을 미리 다 써두는 것이 아니라 JavaScript로 태그를 만드는 흐름이다.

1. `document.getElementById("productContainer")`로 부모 영역을 가져온다.
2. `document.createElement("div")`로 새 `div`를 만든다.
3. `col.className = "col-md-4 mb-4"`처럼 class를 붙인다.
4. `col.innerHTML = ...`로 내용을 채운다.
5. `container.appendChild(col)`로 부모 안에 자식 요소를 추가한다.

이 과정이 곧 [[concepts/javascript-dom|DOM 조작]]이다.

### 4. 이벤트와 이벤트 핸들러

원본은 이벤트를 “브라우저에서 발생하는 사건”으로 설명한다. `onclick="register()"`, `onload`, `DOMContentLoaded`, `click`, `mousedown`, `mouseup` 등이 등장한다.

이벤트 핸들러는 “어떤 이벤트가 발생하면 이 함수를 실행하라”는 연결이다. 상품 등록 버튼, 수정/삭제 버튼, 상세 페이지 이동이 모두 이 패턴으로 이어진다.

### 5. 상품 상세 페이지와 URL parameter

`goDetail(id)`는 상품 목록에서 상세 페이지로 이동할 때 `?id=...` 형태의 query string을 붙인다. 상세 페이지에서는 `URLSearchParams`로 id를 꺼내 더미 데이터에서 해당 상품을 찾는다.

이 흐름은 이후 React Router와 Spring API URL을 구분하는 기초가 된다. 관련 비교는 [[comparisons/react-router-vs-spring-api-url]]에 이어진다.

### 6. GET과 POST

원본은 웹 페이지 주소 형식과 전송 방식에서 GET/POST를 다룬다.

- GET: parameter가 URL에 붙어서 보인다.
- POST: parameter가 HTTP body에 실려 주소창에 직접 보이지 않는다.

자세한 비교는 [[comparisons/get-vs-post]]에 정리했다.

## 핵심 실습

### ProductList

Bootstrap card/grid 형태로 상품 목록을 만들고, 관리자일 때만 수정·삭제 버튼을 보이게 했다. `user.role === 'ADMIN'` 같은 조건과 `style.display = 'none'`이 화면 제어로 연결된다.

### ProductDetail

상세 페이지는 `loadingView`, `errorView`, `successView`를 만들고 `display: none/block`으로 상태별 화면을 전환했다. 이후 React의 조건부 렌더링과 `useEffect` 학습의 전 단계로 볼 수 있다.

## 헷갈린 점 / 질문

- `innerHTML`은 HTML 문자열을 넣는 방식이고, `createElement/appendChild`는 DOM 노드를 직접 만드는 방식이다. 둘을 섞어 쓸 수 있지만 구조를 이해해야 한다.
- `event.stopPropagation()`은 버튼 클릭이 부모 카드 클릭까지 전파되는 것을 막을 때 사용한다.
- query string의 `?id=1`은 화면 이동용 정보이고, 나중에 백엔드 API의 parameter와 연결된다.

## 관련 페이지

- [[concepts/javascript-dom]]
- [[concepts/bootstrap-basics]]
- [[entities/javascript]]
- [[comparisons/get-vs-post]]
- [[comparisons/javascript-dom-vs-jquery]]

## 출처

- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
