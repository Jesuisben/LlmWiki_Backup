---
title: JavaScript DOM vs jQuery
created: 2026-07-06
updated: 2026-07-06
type: comparison
tags: [javascript, jquery, frontend]
sources:
  - "raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
status: growing
confidence: high
---

# JavaScript DOM vs jQuery

## 비교 목적

2026-03-26에는 순수 JavaScript DOM 조작을 배우고, 2026-03-27에는 jQuery로 비슷한 일을 더 짧게 작성했다. 둘의 관계를 구분해야 jQuery가 JavaScript의 대체물이 아니라는 점을 이해할 수 있다.

## 한눈에 보기

| 항목 | JavaScript DOM | jQuery |
|---|---|---|
| 정체 | 브라우저 기본 API | JavaScript 라이브러리 |
| 선택 | `document.getElementById("id")` | `$("#id")` |
| 이벤트 | `addEventListener`, `onclick` | `.click()`, `.change()` |
| class 조작 | `classList.add/remove/toggle` | `addClass/removeClass/toggleClass` |
| 표시 조작 | `style.display = "none"` | `hide()`, `show()` |
| 수업 예 | ProductList/ProductDetail | jQueryImageTestNew |

## 핵심 차이

JavaScript DOM은 브라우저가 기본으로 제공하는 기능이다. jQuery는 그 기능을 더 짧고 일관된 문법으로 감싼 라이브러리다.

```javascript
// JavaScript DOM
const box = document.getElementById("grayImg");
box.style.display = "none";
```

```javascript
// jQuery
$("#grayImg").hide();
```

## 언제 무엇을 쓰는가

- 기본 원리 학습: JavaScript DOM을 먼저 이해한다.
- 오래된 프로젝트나 간단한 DOM 조작: jQuery를 만날 수 있다.
- React 프로젝트: 보통 jQuery로 DOM을 직접 만지지 않고 state/props로 화면을 바꾼다.

## 헷갈리기 쉬운 포인트

- `$("#id")`는 JavaScript 문법 위에서 jQuery 함수 `$`를 호출하는 것이다.
- jQuery 객체와 순수 DOM 객체는 사용할 수 있는 메서드가 다르다.
- 수업에서 `$(this)`는 이벤트가 발생한 DOM 요소를 jQuery 객체로 감싸는 패턴이다.

## 관련 페이지

- [[concepts/javascript-dom]]
- [[concepts/jquery-basics]]
- [[entities/javascript]]
- [[entities/jquery]]
- [[summaries/2026-03-27-jquery-ui-interaction]]

## 출처

- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
