---
title: 2026-03-26 JavaScript DOM과 상품 목록/상세 페이지
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [javascript, bootstrap, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md
  - raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf
  - raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf
  - raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductDetail.html
status: growing
confidence: high
---

# 2026-03-26 JavaScript DOM과 상품 목록/상세 페이지

## 한 줄 요약

배열·객체 데이터를 JavaScript로 반복해 Bootstrap 상품 카드 목록을 만들고, 이벤트·URL 파라미터·GET/POST 개념으로 페이지 간 흐름을 배운 날이다.

## 배운 내용

- `products` 배열 안의 상품 객체를 `forEach`로 반복해 화면에 렌더링했다.
- `role: "ADMIN"` 같은 사용자 권한 데이터는 이름만으로 기능을 갖는 것이 아니라, 조건문 로직이 있어야 동작한다.
- `document.getElementById`, `createElement`, `className`, `innerHTML`, `appendChild`로 DOM 노드를 만들고 붙였다.
- `onclick`, `alert`, `confirm`, `event.stopPropagation()`으로 브라우저 이벤트를 처리했다.
- GET 방식은 URL query string에 데이터가 보이고, POST 방식은 HTTP body에 담겨 주소창에 직접 보이지 않는다. ^[raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf]

## 핵심 실습

### ProductList

`ProductList.html`은 다음 흐름을 가진다.

1. `const products = [...]`로 상품 dummy data를 만든다.
2. `const container = document.getElementById("productContainer")`로 목록 영역을 찾는다.
3. `products.forEach(item => { ... })`로 상품마다 `div`를 생성한다.
4. `col.className = "col-md-4 mb-4"`로 Bootstrap grid class를 붙인다.
5. `col.innerHTML = \`...\``로 카드 HTML을 만든다.
6. `container.appendChild(col)`로 부모 영역에 추가한다.
7. ADMIN이면 `admin-${item.id}` 영역에 수정/삭제 버튼을 넣는다. ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html]

### ProductDetail

`ProductDetail.html`은 `loadingView`, `errorView`, `successView`를 만들고, 버튼 클릭 시 `style.display`를 바꿔 로딩/데이터 없음/정상 화면을 전환한다. 이 구조는 이후 React에서 loading/error/success state로 화면을 나누는 사고방식과 연결된다. ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductDetail.html]

## 헷갈린 점 / 질문

- `const product = products.find(item => item.id === productId);`는 상품 배열에서 URL로 넘어온 id와 같은 상품 객체를 찾는 코드다.
- `params.get("id")`는 문자열일 수 있으므로 `Number()`로 숫자로 바꾼 뒤 `===` 비교를 해야 한다.
- `innerHTML`은 콘솔 출력이 아니라 실제 HTML 내부를 바꾸는 동작이다. 디버깅 출력은 `console.log()`다.
- `event.stopPropagation()`은 카드 클릭 이벤트와 버튼 클릭 이벤트가 겹칠 때, 버튼 클릭이 부모 카드 클릭으로 전파되지 않도록 막는다.

## 관련 페이지

- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[concepts/bootstrap-basics|Bootstrap 기본]]
- [[comparisons/get-vs-post|GET vs POST]]
- [[entities/javascript|JavaScript]]

## 출처

- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf` p.30~34
- `raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf` p.213~214, p.224~225
- `raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf` p.26~27
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html`
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductDetail.html`
