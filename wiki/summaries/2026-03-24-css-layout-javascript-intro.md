---
title: 2026-03-24 CSS 레이아웃과 JavaScript 입문
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [html, css, javascript, frontend, curriculum]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf"
  - "raw/KoreaICT/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/listModelEx.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/spanEx.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/undefinedEx.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/CartList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/FruitList.html"
status: growing
confidence: high
---

# 2026-03-24 CSS 레이아웃과 JavaScript 입문

## 한 줄 요약

전날 배운 태그·선택자·표를 바탕으로 `div`, `position`, `display`, 글꼴 스타일을 다루고, 오후에는 [[concepts/javascript-dom|JavaScript가 HTML 문서를 조작하는 방식]]을 처음 실습한 날이다.

## 배운 내용

### 1. Element와 div 레이아웃

원본은 Element를 “태그를 열고 닫고의 합”으로 설명하며, `boxModelTest`에서 부모 `div#mydiv`와 자식 `div.test1~test4`를 배치한다. 핵심은 부모 요소가 큰 기준 영역이 되고, 자식 요소들이 그 안에서 좌표와 크기를 갖는다는 점이다.^[raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md]

### 2. position과 overflow/display

`position: relative`가 걸린 부모를 기준으로 자식의 위치가 계산되고, `position: absolute`는 기준점에 따라 위치를 직접 배치한다. 원본은 `overflow`의 `hidden`과 `display`도 함께 다룬다.

교육자료의 실제 `boxModelTest.html`은 부모를 기준으로 삼는 이유를 코드로 보여준다.

```css
div {
	width: 100px;
	height: 100px;
	position: absolute;
}

/* 부모 기준 설정 (핵심) */
#mydiv {
	position: relative;
	top: 10px;
	left: 10px;
	width: 300px;
	height: 300px;
	background: white;
	border: 1px solid red;
}
```

자식 `div`의 `top`·`left`·`bottom` 좌표가 부모 `#mydiv`를 기준으로 계산되므로, `relative`와 `absolute`는 서로 배타적인 선택지가 아니라 **부모 기준과 자식 배치를 함께 만드는 조합**이다.

- `overflow: hidden`: 영역을 벗어나는 내용을 감춘다.
- `display: block`: 한 줄 전체 폭을 차지하는 박스 흐름.
- `display: inline`: 글자처럼 흐르며 `width`, `height`가 잘 먹지 않는다.
- `display: inline-block`: 옆으로 나란히 배치하면서 크기 조절도 가능하다.

### 3. 글꼴·텍스트 스타일

`font-family`, `line-height`, `font-style`, `text-transform`, highlight 효과 등 텍스트 표현을 실습했다. 특히 `font-family: "Gulim", "굴림", serif;`처럼 여러 글꼴을 콤마로 연결하는 폰트 스택 개념을 다룬다.

`listModelEx.html`에서는 `float`, 목록 이미지, `list-style-position`으로 좌우 영역과 목록 표시를 만들었고, `spanEx.html`에서는 짧은 인라인 범위의 글꼴·강조·highlight를 바꿨다. `overflow`, `z-index`, padding의 시계 방향 순서, shorthand property까지 함께 다루며 CSS가 색상만이 아니라 **배치와 가시성**을 결정한다는 범위를 넓혔다.

### 4. JavaScript 첫 입문

오후에는 `<script>` 태그와 JavaScript 주석, 변수, 비교 연산, 객체/배열을 다룬다. 원본은 `document`를 “HTML 문서 자체인 객체”로 설명하고, `document.getElementById("output")`으로 HTML 요소를 가져와 `innerHTML`에 문자열을 누적한다.

```javascript
let output = document.getElementById("output");
let mytitle = '자바스크립트';
output.innerHTML += '타이틀 : ' + mytitle + '<br>';
```

여기서 `output`은 단순 문자열이 아니라 HTML 요소 객체이고, `innerHTML`은 그 요소 내부에 HTML 문자열을 넣는 속성이다.

### 5. `==`와 `===`, 객체와 배열

원본은 `num == str`과 `num === str` 비교를 통해 암시적 형변환과 엄격 비교의 차이를 보여준다. 또한 중괄호는 객체(Object), 대괄호는 배열(Array)이라는 식으로 처음 구분한다.

```javascript
/* 중괄호는 무조건 객체입니다. */
const hong = { name: '홍길동'};
output.innerHTML += '객체의 이름 : ' + hong.name + '<br>' ;
```

이 객체/배열 감각은 2026-03-25의 Bootstrap/Form 화면 준비를 거쳐, 2026-03-26 상품 데이터 배열과 `forEach` 렌더링으로 이어진다.

## 핵심 실습

### boxModelTest

부모 `div`와 자식 `div`를 만들고 `position`, `top`, `left`, `width`, `height`, `border`로 사각형 배치를 연습했다. 화면 배치가 “감”이 아니라 박스와 좌표의 조합이라는 점을 배운 실습이다.

### CartList 기초

`B.nobootstrap/CartList.html`에서는 `.container`, flex 기반 `.row`, `.col-4/.col-8`, 속성 선택자 `input[type="number"]`를 직접 정의했다. `FruitList.html`에서는 `tr:hover`로 마우스 상태에 따른 style 변경을 확인했다. 이 직접 CSS 화면이 다음 날 [[concepts/bootstrap-basics|Bootstrap 기본]]과 [[comparisons/custom-css-vs-bootstrap|직접 CSS 구현 vs Bootstrap]] 비교의 기준이 된다.

## 헷갈린 점 / 질문

- `position: relative`는 요소를 “조금 이동”시키기도 하지만, 더 중요한 역할은 자식 absolute 요소의 기준점을 제공하는 것이다.
- `innerHTML`은 화면에 보이는 글자만 넣는 것이 아니라 HTML 태그 문자열도 해석한다. 그래서 편하지만, 실제 프로젝트에서는 보안과 유지보수성을 조심해야 한다.
- JavaScript의 객체와 Java 객체는 이름은 같지만 쓰임과 문법이 다르다. 이 수업에서는 우선 “key-value 묶음”으로 이해하면 된다.
- 원본의 “중괄호는 무조건 객체, 대괄호는 무조건 배열”은 첫 구분을 위한 단순화다. `{}`는 block/function body 등에, `[]`는 property 접근 등에도 쓰일 수 있다.
- `table, th, td`에 border를 함께 준 것은 표와 각 cell 경계를 보이게 하기 위해서다. `tr`만 선택하면 cell 각각의 테두리를 같은 방식으로 만들지 못한다.
- `innerHTML` 보안 주의는 후속 일반 설명이다. 이 날 직접 확인한 범위는 HTML 문자열을 해석해 요소 내부에 넣는 동작이다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[concepts/javascript-dom]]
- [[comparisons/id-vs-class]]
- [[entities/css]]
- [[entities/javascript]]
- [[comparisons/custom-css-vs-bootstrap]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md`
