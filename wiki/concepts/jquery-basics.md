---
title: jQuery 기본
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [jquery, javascript, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html"
status: growing
confidence: high
---

# jQuery 기본

## 정의

jQuery는 JavaScript로 만든 라이브러리로, DOM 선택, 이벤트 연결, class/속성 조작, show/hide 같은 작업을 짧은 문법으로 작성하게 해준다.

## 이 수업에서의 맥락

2026-03-26에 순수 JavaScript로 `document.getElementById`, `createElement`, `appendChild`를 배운 뒤, 2026-03-27에는 jQuery로 이미지 UI를 빠르게 조작했다. 즉 jQuery는 JavaScript의 대체 언어가 아니라 JavaScript DOM 조작을 편하게 하는 도구다.

## 핵심 설명

### `$`는 jQuery를 호출하는 기호다

```javascript
$("#grayImg")
```

CSS 선택자처럼 `#id`, `.class`, `태그명`, `[속성=값]`을 넣어 요소를 고른다.

### DOM ready

```javascript
// $(function(){여기에할일작성});
$(function (){
    // 흑백 토글
    $("#grayImg").click(function(){
        $(this).toggleClass("gray");
    });
});
```

표준 JavaScript의 `DOMContentLoaded`와 비슷하게, 문서 준비 후 코드를 실행하게 한다.

### 이벤트 연결

```javascript
$("#grayImg").click(function() {
  $(this).toggleClass("gray");
});
```

선택한 요소가 클릭되면 함수를 실행한다. `this`는 클릭된 바로 그 요소다.

### class 조작

- `toggleClass("gray")`: class가 없으면 붙이고, 있으면 제거한다.
- `addClass("active")`: class를 붙인다.
- `removeClass("active")`: class를 제거한다.

### 표시/숨김과 속성 조작

- `show()`, `hide()`: 요소 표시 상태를 바꾼다.
- `attr("src")`, `attr("src", 새값)`: HTML attribute를 읽거나 바꾼다.

### 속성 선택자와 필터링

원본은 `data-category`를 이용해 카테고리별 이미지를 필터링한다.

```javascript
const selected = $(this).val();

if (selected === "all") {
    $(".menu-img").show();
} else {
    $(".menu-img").hide();
    $(".menu-img[data-category='" + selected + "']").show();
}
```

이 교육자료 코드는 `select`의 현재 값을 읽고, 전체 보기면 모두 표시하며, 특정 category면 먼저 모두 숨긴 다음 일치하는 `data-category`만 다시 보여준다.

### 노드를 이동하는 `prepend`와 `append`

```javascript
const last = $("#rotateBox img").last();
$("#rotateBox").prepend(last);
```

기존 마지막 이미지를 선택해 컨테이너 앞으로 이동한다. 문자열을 추가하는 예가 아니라 기존 DOM 노드의 순서를 바꾸는 수업 예다.

## 예시: 이미지 UI 패턴

1. 이미지를 class로 묶는다.
2. 클릭 이벤트를 붙인다.
3. 기존 active class를 모두 제거한다.
4. 클릭한 이미지에만 active class를 붙인다.
5. 필요하면 큰 이미지의 `src` 속성을 바꾼다.

## 자주 헷갈리는 점

- `$("#id")`와 `document.getElementById("id")`는 비슷한 대상을 잡지만 반환 객체와 사용 메서드가 다르다.
- `$()` 안에는 보통 문자열 선택자를 넣지만 `$(this)`처럼 DOM 객체를 jQuery 객체로 감싸는 경우도 있다.
- `attr`은 HTML attribute 조작이고, `css`는 CSS style 조작이다.
- jQuery는 오래된 웹 프로젝트에서 많이 보지만, React에서는 보통 직접 함께 쓰지 않는다. 개념 비교는 [[comparisons/javascript-dom-vs-jquery]].
- `show()/hide()`는 요소의 표시 상태를 바꾸지만 데이터를 삭제하지 않는다. 반대로 DOM에서 노드를 제거하는 작업과는 다르다.
- jQuery 예제의 결과는 브라우저 안 UI 변경까지다. 서버 저장이나 React state 변경이 일어난 것으로 해석하지 않는다.

## 관련 개념

- [[entities/jquery]]
- [[concepts/javascript-dom]]
- [[comparisons/library-vs-framework]]
- [[comparisons/javascript-dom-vs-jquery]]
- [[summaries/2026-03-27-jquery-ui-interaction]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html`
