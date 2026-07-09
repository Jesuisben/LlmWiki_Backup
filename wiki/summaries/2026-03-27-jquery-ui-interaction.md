---
title: 2026-03-27 jQuery와 UI 상호작용
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [javascript, jquery, bootstrap, frontend, curriculum]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/library&framework.png"
  - "raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html"
status: growing
confidence: high
---

# 2026-03-27 jQuery와 UI 상호작용

## 한 줄 요약

[[entities/jquery|jQuery]]를 CDN으로 불러와 `$()` 선택자, `click`, `toggleClass`, `addClass/removeClass`, `show/hide`, `attr`, method chaining으로 이미지 UI 상호작용을 구현한 날이다.

## 배운 내용

### 1. jQuery의 위치

원본은 “jQuery의 상위 개념은 JavaScript”라고 설명한다. 정확히는 jQuery가 JavaScript로 만들어진 라이브러리다. 기존 CSS 선택자 감각과 JavaScript DOM 조작을 묶어, 더 짧은 문법으로 요소를 선택하고 이벤트를 붙이게 해준다.^[raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md]

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
```

### 2. Library와 Framework

이날 라이브러리와 프레임워크의 차이도 함께 다룬다. jQuery는 필요한 기능을 내가 호출하는 라이브러리이고, Bootstrap은 정해진 class와 컴포넌트 규칙을 따라 화면을 구성하게 해주는 프레임워크 성격이 강하다. 자세한 비교는 [[comparisons/library-vs-framework]]에 있다.

### 3. `$()`와 DOM ready

원본은 표준 JavaScript의 `document.addEventListener("DOMContentLoaded", ...)`와 jQuery 방식을 비교한다.

```javascript
$(function() {
  // DOM 준비 후 실행
});
```

`$`는 jQuery를 호출하는 기호이고, `$()` 안에는 CSS 선택자처럼 `"#grayImg"`, `".select-img"` 등을 넣는다.

### 4. toggleClass, addClass, removeClass

이미지를 클릭하면 흑백 처리 class를 붙였다 떼거나, 선택된 이미지에 `active` class를 붙인다.

```javascript
$("#grayImg").click(function() {
  $(this).toggleClass("gray");
});
```

`this`는 이벤트가 발생한 바로 그 요소를 가리킨다.

### 5. 필터링, show/hide, attr

콤보박스에서 카테고리를 고르면 `data-category` 속성을 기준으로 이미지를 필터링한다.

- `show()`: 선택한 요소를 보여준다.
- `hide()`: 선택한 요소를 숨긴다.
- `attr()`: HTML attribute 값을 읽거나 바꾼다.
- `.menu-img[data-category='bread']`: 속성 선택자로 특정 카테고리 이미지만 고른다.

### 6. method chaining

원본 마지막에는 method chaining이 등장한다. jQuery 객체에 `.addClass(...).attr(...).show()`처럼 메서드를 이어 붙여 같은 대상에 여러 작업을 연속 적용하는 방식이다.

## 핵심 실습

### jQueryImageTestNew

이미지 확대 hover, 흑백 토글, active 선택 표시, 콤보박스 카테고리 필터링, 썸네일 → 큰 이미지 교체, 이미지 회전, 스타일 변경을 하나의 HTML 파일에서 실습했다.

이 실습은 “화면의 특정 요소를 선택하고 → 이벤트를 붙이고 → class/속성/display를 바꾼다”는 프론트엔드 상호작용의 기본 패턴을 압축해서 보여준다.

## 헷갈린 점 / 질문

- jQuery가 JavaScript를 대체하는 언어는 아니다. JavaScript DOM 조작을 쉽게 쓰게 해주는 라이브러리다.
- `$()` 안에는 문자열 선택자가 많이 들어가지만, `$(this)`처럼 이미 존재하는 DOM 객체를 감싸는 경우도 있다.
- Bootstrap 5는 예전 Bootstrap과 달리 jQuery 의존성이 줄었지만, 이 수업에서는 Bootstrap과 jQuery를 함께 쓰는 UI 흐름을 학습했다.

## 관련 페이지

- [[concepts/jquery-basics]]
- [[concepts/javascript-dom]]
- [[comparisons/javascript-dom-vs-jquery]]
- [[comparisons/library-vs-framework]]
- [[entities/jquery]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html`
