---
title: Library vs Framework
created: 2026-07-02
updated: 2026-07-15
type: comparison
tags: [javascript, bootstrap, jquery, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/library&framework.png"
status: growing
confidence: high
---

# Library vs Framework

## 비교 목적

UI&UX 수업에서 jQuery와 Bootstrap을 함께 쓰면서 “라이브러리와 프레임워크가 뭐가 다른가”가 등장했다. 이 비교는 이후 React, Spring Boot를 배울 때도 계속 중요하다.

## 한눈에 보기

| 항목 | Library | Framework |
|---|---|---|
| 기본 느낌 | 필요한 기능을 내가 호출 | 정해진 구조 안에 내 코드를 끼워 넣음 |
| 제어 흐름 | 내 코드가 주도 | 프레임워크 규칙이 주도 |
| UI&UX 예 | jQuery | Bootstrap |
| 교육 이미지의 예 | NumPy, Pandas, jQuery | Spring Boot, Django, Angular/Bootstrap |

## 핵심 차이

라이브러리는 “도구 상자”에 가깝다. 내가 필요할 때 `$(...)`, `show()`, `hide()`처럼 꺼내 쓴다. 프레임워크는 “작업 틀”에 가깝다. Bootstrap을 쓰면 `container-row-col`, `btn`, `form-control` 같은 정해진 class 체계를 따라 화면을 만든다.

교육 이미지의 핵심 표현은 library는 “개발자가 직접 코드의 흐름을 제어하고 필요한 기능만 호출”, framework는 “전체 흐름을 제어하며 정해진 규칙에 코드를 끼워 넣는 구조”라는 것이다. 이미지에는 framework 예가 본문에서는 Spring Boot·Django·Angular, 하단 표에서는 Spring Boot·Django·Bootstrap으로 제시되어 있어, Bootstrap 분류는 UI framework라는 수업 맥락에서 사용한다.

## 언제 무엇을 쓰는가

- 상황 1 — 클릭한 이미지만 흑백 처리하거나 순서를 바꾸는 함수를 필요할 때 호출: jQuery library를 사용한다.
- 상황 2 — form·button·grid를 정해진 class 체계로 일관되게 구성: Bootstrap UI framework 규칙을 따른다.

둘은 함께 쓸 수 있다. 실제 `jQueryImageTest.html`은 Bootstrap이 화면 모양과 form class를 제공하고, jQuery가 click/change 이벤트와 class/attribute 변경을 담당한다.

## 헷갈리기 쉬운 포인트

- Bootstrap은 JavaScript framework라기보다 CSS/UI framework로 이해하면 쉽다.
- jQuery는 `$()` 함수를 직접 호출하므로 라이브러리 감각이 강하다.
- 라이브러리는 구조가 전혀 없고 프레임워크는 자유가 전혀 없다는 이분법은 과장이다. 비교의 핵심은 누가 전체 제어 흐름과 호출 시점을 주도하는가다.

## 관련 페이지

- [[entities/jquery]]
- [[entities/bootstrap]]
- [[concepts/jquery-basics]]
- [[concepts/bootstrap-basics]]
- [[summaries/2026-03-27-jquery-ui-interaction]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/KoreaICT/3. UI&UX/교육 자료/library&framework.png`
