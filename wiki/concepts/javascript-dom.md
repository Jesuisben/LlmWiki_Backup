---
title: JavaScript와 DOM
created: 2026-06-30
updated: 2026-07-02
type: concept
tags: [javascript, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md
  - raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md
  - raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md
status: growing
confidence: high
---

# JavaScript와 DOM

## 정의

JavaScript와 DOM(Document Object Model)은 HTML 문서를 JavaScript에서 객체처럼 읽고 바꾸는 방식이다. 수업에서는 빈 `<div>`에 값을 넣는 작은 예제에서 시작해, 상품 배열을 반복하며 상품 목록 카드를 동적으로 만들고, 버튼·URL 파라미터·상세 페이지 전환까지 연결했다.

## 이 수업에서의 위치

2026-03-24에는 JavaScript 맛보기로 `document.getElementById`, `innerHTML`, `undefined`, `==`와 `===`, 객체와 배열을 배웠다. 2026-03-26에는 이 기초를 바탕으로 ProductList와 ProductDetail 화면을 만들며 DOM 조작이 실제 웹 페이지 기능으로 확장되었다. ^[raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md] ^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

## 핵심 설명

### document는 HTML 문서 자체를 가리키는 기본 객체다

수업에서는 `document`를 HTML 문서 자체로 설명했다. HTML에 빈 상자를 만들고 JavaScript로 가져오면, 그 상자 안에 내용을 넣을 수 있다.

```html
<body>
    <div id="output"></div>
    <script>
        let output = document.getElementById("output");
        let mytitle = '자바스크립트';
        output.innerHTML += '타이틀 : ' + mytitle;
    </script>
</body>
```

여기서 `output`은 문자열이 아니라 HTML 요소를 가리키는 객체다. `innerHTML`에 값을 넣으면 실제 화면의 `<div id="output"></div>` 안에 내용이 들어간다. ^[raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md]

### JavaScript는 top-down 흐름을 따른다

값을 할당하기 전에 출력하면 `undefined`가 나온다.

```javascript
let myname;
output.innerHTML += '이름 : ' + myname;
```

수업에서는 `if (myname == undefined)`로 값이 아직 없는 상태를 확인하고, 나중에 `myname = "김철수"`를 할당하면 그 이후 출력만 값이 생기는 것을 확인했다. HTML과 JavaScript 모두 위에서 아래로 실행된다는 감각이 중요하다. ^[raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md]

### `==`와 `===`는 타입 비교에서 차이가 난다

```javascript
let num = 1;
let str = "1";
output.innerHTML += '== 비교 : ' + (num == str) + '<br>';
output.innerHTML += '=== 비교 : ' + (num === str) + '<br>';
```

수업 출력은 `== 비교 : true`, `=== 비교 : false`였다. `==`는 암시적 형변환을 허용하고, `===`는 값과 타입이 모두 같아야 한다. 이후 상품 id처럼 URL에서 문자열로 넘어온 값을 숫자로 바꿔 비교할 때 이 차이가 중요해진다. ^[raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md]

### JavaScript 객체와 배열은 상품 데이터의 형태가 된다

수업에서는 중괄호는 객체, 대괄호는 배열이라고 정리했다.

```javascript
const hong = { name: '홍길동' };
const members = ['김철수', '이규철', '박진섭'];
```

상품 목록 수업에서는 이 구조가 바로 상품 데이터로 확장되었다.

```javascript
const products = [
    { id: 1, name: '아메리카노', price: 4000, image: '/images/americano01.png' }
];

const user = {
    role: 'ADMIN'
};
```

`role`은 특별한 내장 기능이 아니라, 개발자가 “사용자의 권한”을 나타내기 위해 정한 속성 이름이다. 로직이 있어야 ADMIN일 때만 버튼을 보이게 만들 수 있다. ^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

### DOM 요소의 style을 바꿔 화면 표시를 제어한다

관리자가 아니면 상품 등록 버튼을 숨기는 실습은 DOM 조작의 대표 예다.

```javascript
if (user.role !== 'ADMIN') {
    document.getElementById("insertBtn").style.display = "none";
}
```

`display = "none"`은 요소를 화면에서 보이지 않게 하고, 공간도 차지하지 않게 한다. 이 로직은 이후 React에서 조건부 렌더링을 배울 때 같은 사고방식으로 이어진다. ^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

### 배열을 반복해 HTML을 동적으로 만든다

상품 목록은 `products.forEach`로 배열 원소를 하나씩 꺼내면서 만들었다.

```javascript
const container = document.getElementById("productContainer");

products.forEach(item => {
    const col = document.createElement("div");
    col.className = "col-md-4 mb-4";
    col.innerHTML = `${item.name}`;
    container.appendChild(col);
});
```

- `createElement("div")`: 메모리상에 새 태그 노드를 만든다.
- `className`: Bootstrap class를 부여한다.
- `innerHTML`: 태그 안에 표시할 HTML을 넣는다.
- `appendChild`: 부모 요소의 마지막 자식으로 추가한다.

수업 노트에서는 `append`를 “무리 제일 뒤쪽에 하나 추가하는 행위”로 설명했다. ^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

### 이벤트는 브라우저에서 발생하는 사건이다

수업에서는 이벤트를 키보드 누르기, 마우스 클릭, 스크롤, 페이지 전환처럼 브라우저에서 발생하는 사건으로 정리했다. `onclick="register()"`처럼 이벤트 속성에 함수를 연결하면, 클릭 시 함수가 실행된다.

```javascript
function register() {
    alert('상품 등록 완료');
}
```

상품 목록에서는 `register`, `goDetail`, `edit`, `remove` 같은 함수를 버튼에 연결했다. ^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

### URL 파라미터는 페이지 간 데이터 전달의 첫 경험이다

상품 상세 페이지로 이동할 때는 URL에 id를 붙였다.

```javascript
function goDetail(id) {
    location.href = `ProductDetailNew.html?id=${id}`;
}
```

상세 페이지에서는 `URLSearchParams`로 `?id=...` 값을 읽고, `Number(params.get("id"))`로 숫자로 바꾼 뒤 상품 배열에서 해당 상품을 찾았다.

```javascript
const product = products.find(item => item.id === productId);
```

원본 노트의 `???` 표시는 이 줄이 헷갈렸던 지점으로 보인다. 의미는 “상품 목록 중에서 `item.id`가 URL로 넘어온 `productId`와 같은 첫 번째 상품 객체를 찾아라”이다. 이때 `===`를 쓰므로 `productId`를 숫자로 바꾸는 `Number()`가 중요하다. ^[raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md]

### DOMContentLoaded는 HTML을 다 읽은 뒤 실행하게 한다

HTML은 기본적으로 위에서 아래로 읽힌다. 아직 만들어지지 않은 요소를 JavaScript가 먼저 찾으면 실패할 수 있다. 수업에서는 `DOMContentLoaded`를 “HTML문서가 다 읽혀지고 나서 동작하라는 구문”으로 정리했다. 이 개념은 이후 jQuery의 `$(function(){ ... })`와도 연결된다.

## 자주 헷갈리는 점

### DOM에서 태그는 “노드/객체”로 다뤄진다

눈에는 `<div>`나 `<h1>` 같은 태그로 보이지만, JavaScript 입장에서는 조작 가능한 객체이므로 노드(Node)라고 부른다. 태그뿐 아니라 글자, 주석도 넓은 의미의 노드에 포함된다.

### `innerHTML`은 문자열 출력이 아니라 HTML 내부 변경이다

`output.innerHTML += ...`은 콘솔에 출력하는 것이 아니라, 실제 HTML 요소 안의 내용을 바꾼다. 디버깅용 출력은 `console.log()`이고, 화면 표시 변경은 DOM 조작이다.

### URL에서 넘어온 값은 문자열로 다루는 경우가 많다

`params.get("id")`는 보통 문자열을 반환한다. 상품의 `id`가 숫자라면 `Number()`로 바꿔야 `===` 비교가 의도대로 동작한다.

## 이전/이후 학습과의 연결

- 이전: [[concepts/html-css-basics|HTML/CSS 기본]]의 id, class, 태그 구조를 JavaScript가 선택하고 조작한다.
- 같은 흐름: [[concepts/bootstrap-basics|Bootstrap 기본]] class를 동적으로 붙여 상품 카드를 만든다.
- 이후: [[concepts/jquery-basics|jQuery 기본]]은 DOM 선택과 이벤트 처리를 더 짧은 문법으로 작성하게 해준다.
- 이후 React: 배열을 반복해 UI를 만든다는 발상은 React의 `map` 렌더링과 직접 연결된다.

## 관련 개념

- [[entities/javascript|JavaScript]]
- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[concepts/bootstrap-basics|Bootstrap 기본]]
- [[concepts/jquery-basics|jQuery 기본]]
- [[summaries/2026-03-24-css-layout-javascript-intro|2026-03-24 CSS 레이아웃과 JavaScript 입문]]
- [[summaries/2026-03-26-javascript-dom-product-pages|2026-03-26 JavaScript DOM과 상품 목록/상세 페이지]]

## 출처

- `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/Study/3. UI&UX/2026.03.25(수)/2026.03.25(수).md`
- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
