---
title: 2026-03-27 jQuery와 UI 상호작용
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [javascript, jquery, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md
  - raw/Study/3. UI&UX/교육 자료/library&framework.png
  - raw/Study/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html
status: growing
confidence: high
---

# 2026-03-27 jQuery와 UI 상호작용

## 한 줄 요약

JavaScript DOM 조작을 jQuery의 `$()` 선택자와 이벤트 메서드로 더 짧게 작성하고, 이미지 토글·필터·썸네일·회전·스타일 변경 UI를 만든 날이다.

## 배운 내용

- jQuery는 JavaScript의 라이브러리다. CSS 선택자와 JavaScript DOM 조작을 결합해 짧은 문법으로 쓸 수 있게 해준다.
- Library는 필요할 때 개발자가 가져다 쓰는 도구이고, Framework는 정해진 틀 안에 개발자가 코드를 넣는 구조다. 수업 자료는 jQuery를 Library 예시, Spring Boot/Django/Angular/Bootstrap을 Framework 예시로 비교했다. ^[raw/Study/3. UI&UX/교육 자료/library&framework.png]
- `$(function(){ ... })`은 DOM을 다 읽은 뒤 코드를 실행하는 jQuery ready 패턴이다.
- `click`, `change`, `toggleClass`, `addClass`, `removeClass`, `show`, `hide`, `attr`, `append`, `prepend`를 실습했다.

## 핵심 실습

`jQueryImageTest.html`은 이미지 UI 상호작용을 7개 패턴으로 묶은 대표 실습이다.

1. `:hover`와 `transform: scale(1.1)`로 hover 확대
2. `#grayImg` 클릭 시 `toggleClass("gray")`로 흑백 전환
3. `.select-img` 클릭 시 기존 `.active` 제거 후 선택 이미지 강조
4. `#categorySelect`의 `change` 이벤트와 `data-category` 속성 선택자로 카테고리 필터
5. 썸네일 클릭 시 `attr("src")`로 큰 이미지 교체
6. `last()/first()`와 `prepend()/append()`로 이미지 순서 회전
7. radio 값에 따라 `removeClass().addClass()`로 이미지 스타일 변경 ^[raw/Study/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html]

## 헷갈린 점 / 질문

- jQuery는 JavaScript를 대체하는 언어가 아니다. JavaScript 위에서 DOM 선택과 이벤트 처리를 쉽게 해주는 라이브러리다.
- `$()` 안에는 CSS 선택자처럼 `"#id"`, `".class"`, `"input[name='imgStyle']"` 등을 넣는다.
- 체크박스·라디오·콤보박스는 “클릭했는가”보다 “값이 바뀌었는가”가 중요하므로 `change` 이벤트가 자연스러운 경우가 많다.
- Bootstrap 5는 과거 Bootstrap 버전과 달리 jQuery가 필수는 아니다. 수업 맥락에서는 함께 넣어 실습했지만, 실제 프로젝트에서는 버전을 확인해야 한다.

## 관련 페이지

- [[concepts/jquery-basics|jQuery 기본]]
- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[comparisons/library-vs-framework|Library vs Framework]]
- [[entities/jquery|jQuery]]

## 출처

- `raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/Study/3. UI&UX/교육 자료/library&framework.png`
- `raw/Study/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html`
