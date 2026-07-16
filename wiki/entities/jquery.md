---
title: jQuery
created: 2026-07-02
updated: 2026-07-15
type: entity
tags: [jquery, javascript, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html"
status: growing
confidence: high
---

# jQuery

## 무엇인가

jQuery는 JavaScript DOM 선택, 이벤트 처리, class/속성 조작을 간단한 문법으로 작성하게 해주는 JavaScript 라이브러리다.

## 이 위키에서의 맥락

UI&UX 마지막 날에 이미지 확대, 흑백 토글, 선택 표시, 카테고리 필터링, 썸네일 변경, 이미지 회전 같은 상호작용을 만들며 등장했다.

## 핵심 기능 / 특징

- `$()`로 CSS 선택자 기반 요소 선택
- `click`, `change`로 이벤트 연결
- `toggleClass`, `addClass`, `removeClass`로 class 조작
- `show`, `hide`로 표시 상태 조작
- `attr`로 HTML attribute 읽기/쓰기
- method chaining으로 여러 조작을 연속 작성

## 화면 구현 역할

2026-03-27에 처음 등장해 CSS 선택자 문법으로 요소를 고르고, 클릭·change 이벤트에 class/attribute/display 변경을 연결했다. `jQueryImageTest.html`에서는 흑백 토글, 단일 active 선택, category 필터, 큰 이미지 교체, 이전/다음 순서 이동, radio 기반 Bootstrap image class 변경을 구현했다.

## 프로젝트·면접 설명 관점

- 프로젝트: 레거시 화면에서 `$()` 선택자와 이벤트 메서드를 만나면 JavaScript DOM 작업을 감싼 코드로 해석할 수 있다.
- 면접: jQuery는 JavaScript의 대체 언어가 아니라 JavaScript 라이브러리이며, 제어 흐름은 필요한 시점에 개발자가 jQuery 함수를 호출하는 쪽에 있다.
- 범위 경계: UI&UX에서는 브라우저 DOM을 직접 변경했다. React에서는 state와 rendering 흐름을 우선하며 jQuery 직접 조작을 그대로 옮기지 않는다.

## 관련 개념

- [[concepts/jquery-basics]]
- [[concepts/javascript-dom]]
- [[comparisons/javascript-dom-vs-jquery]]
- [[comparisons/library-vs-framework]]
- [[comparisons/custom-css-vs-bootstrap]]
- [[entities/javascript]]

## 학습 이력

- [[summaries/2026-03-27-jquery-ui-interaction]] — 날짜 노트의 `jQueryImageTestNew` 흐름과 현재 보존 `jQueryImageTest.html`의 이미지 UI 상호작용 비교

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html`
