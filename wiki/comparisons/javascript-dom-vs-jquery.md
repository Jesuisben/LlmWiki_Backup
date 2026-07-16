---
title: JavaScript DOM vs jQuery
created: 2026-07-06
updated: 2026-07-15
type: comparison
tags: [javascript, jquery, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductList.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/C.yesbootstrap/ProductDetail.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html"
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
| 수업 예 | ProductList/ProductDetail | 날짜 노트의 jQueryImageTestNew, 현재 artifact의 jQueryImageTest |

## 핵심 차이

JavaScript DOM은 브라우저가 기본으로 제공하는 기능이다. jQuery는 그 기능을 더 짧고 일관된 문법으로 감싼 라이브러리다.

```javascript
document.getElementById("insertBtn").style.display = "none";
```

```javascript
$("#grayImg").click(function () {
    $(this).toggleClass("gray");
});
```

## 언제 무엇을 쓰는가

- 상황 1 — 외부 라이브러리 없이 관리자 버튼 하나를 숨길 때: 브라우저 기본 DOM API와 `style.display`만으로 충분하다.
- 상황 2 — 여러 이미지에 동일한 click/change 이벤트와 class 토글을 연속 적용할 때: 수업의 jQuery 선택자·메서드가 반복 코드를 줄였다.
- 후속 React 프로젝트: 보통 둘 중 하나로 DOM을 직접 고치기보다 state/props로 화면을 다시 렌더링한다.

둘은 함께 존재할 수 있으며 배타적이지 않다. jQuery가 선택한 대상은 결국 브라우저 DOM 요소이며, `$(this)`는 이벤트 대상 DOM 객체를 jQuery 객체로 감싸 라이브러리 메서드를 쓰는 패턴이다.

## 헷갈리기 쉬운 포인트

- `$("#id")`는 JavaScript 문법 위에서 jQuery 함수 `$`를 호출하는 것이다.
- jQuery 객체와 순수 DOM 객체는 사용할 수 있는 메서드가 다르다.
- 수업에서 `$(this)`는 이벤트가 발생한 DOM 요소를 jQuery 객체로 감싸는 패턴이다.
- jQuery 문법이 짧다고 DOM 원리를 건너뛰는 것은 아니다. 선택·이벤트·class/attribute/display 변경이라는 실행 흐름은 같다.

## 관련 페이지

- [[concepts/javascript-dom]]
- [[concepts/jquery-basics]]
- [[entities/javascript]]
- [[entities/jquery]]
- [[summaries/2026-03-27-jquery-ui-interaction]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
