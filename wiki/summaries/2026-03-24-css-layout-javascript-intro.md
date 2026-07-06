---
title: 2026-03-24 CSS 레이아웃과 JavaScript 입문
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [html, css, javascript, frontend, curriculum]
sources:
  - "raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/속성들.md"
  - "raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf"
  - "raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf"
status: growing
confidence: high
---

# 2026-03-24 CSS 레이아웃과 JavaScript 입문

## 한 줄 요약

전날 배운 태그·선택자·표를 바탕으로 `div`, `position`, `display`, 글꼴 스타일을 다루고, 오후에는 [[concepts/javascript-dom|JavaScript가 HTML 문서를 조작하는 방식]]을 처음 실습한 날이다.

## 배운 내용

### 1. Element와 div 레이아웃

원본은 Element를 “태그를 열고 닫고의 합”으로 설명하며, `boxModelTest`에서 부모 `div#mydiv`와 자식 `div.test1~test4`를 배치한다. 핵심은 부모 요소가 큰 기준 영역이 되고, 자식 요소들이 그 안에서 좌표와 크기를 갖는다는 점이다.^[raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md]

### 2. position과 overflow/display

`position: relative`가 걸린 부모를 기준으로 자식의 위치가 계산되고, `position: absolute`는 기준점에 따라 위치를 직접 배치한다. 원본은 `overflow`의 `hidden`과 `display`도 함께 다룬다.

- `overflow: hidden`: 영역을 벗어나는 내용을 감춘다.
- `display: block`: 한 줄 전체 폭을 차지하는 박스 흐름.
- `display: inline`: 글자처럼 흐르며 `width`, `height`가 잘 먹지 않는다.
- `display: inline-block`: 옆으로 나란히 배치하면서 크기 조절도 가능하다.

### 3. 글꼴·텍스트 스타일

`font-family`, `line-height`, `font-style`, `text-transform`, highlight 효과 등 텍스트 표현을 실습했다. 특히 `font-family: "Gulim", "굴림", serif;`처럼 여러 글꼴을 콤마로 연결하는 폰트 스택 개념을 다룬다.

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
const hong = { name: '홍길동' };
const members = ['김철수', '이영희'];
```

이 객체/배열 감각은 다음 날 상품 데이터 배열과 `forEach` 렌더링으로 이어진다.

## 핵심 실습

### boxModelTest

부모 `div`와 자식 `div`를 만들고 `position`, `top`, `left`, `width`, `height`, `border`로 사각형 배치를 연습했다. 화면 배치가 “감”이 아니라 박스와 좌표의 조합이라는 점을 배운 실습이다.

### CartList 기초

`B_nobootstrap/CartList.html`, `C_yesbootstrap` 디렉터리를 만들며 Bootstrap 이전/이후 화면 구성을 준비했다. 이 흐름은 다음 날 [[concepts/bootstrap-basics|Bootstrap 기본]]으로 연결된다.

## 헷갈린 점 / 질문

- `position: relative`는 요소를 “조금 이동”시키기도 하지만, 더 중요한 역할은 자식 absolute 요소의 기준점을 제공하는 것이다.
- `innerHTML`은 화면에 보이는 글자만 넣는 것이 아니라 HTML 태그 문자열도 해석한다. 그래서 편하지만, 실제 프로젝트에서는 보안과 유지보수성을 조심해야 한다.
- JavaScript의 객체와 Java 객체는 이름은 같지만 쓰임과 문법이 다르다. 이 수업에서는 우선 “key-value 묶음”으로 이해하면 된다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[concepts/javascript-dom]]
- [[comparisons/id-vs-class]]
- [[entities/css]]
- [[entities/javascript]]

## 출처

- `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/속성들.md`
