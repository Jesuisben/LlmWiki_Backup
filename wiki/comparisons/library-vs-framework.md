---
title: Library vs Framework
created: 2026-07-02
updated: 2026-07-06
type: comparison
tags: [javascript, bootstrap, jquery, frontend]
sources:
  - "raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/Study/3. UI&UX/교육 자료/library&framework.png"
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
| UI&UX 예 | jQuery | Bootstrap은 UI framework 성격이 강함 |
| 이후 예 | axios, lodash | Spring Boot, React 앱 구조, Bootstrap |

## 핵심 차이

라이브러리는 “도구 상자”에 가깝다. 내가 필요할 때 `$(...)`, `show()`, `hide()`처럼 꺼내 쓴다. 프레임워크는 “작업 틀”에 가깝다. Bootstrap을 쓰면 `container-row-col`, `btn`, `form-control` 같은 정해진 class 체계를 따라 화면을 만든다.

## 헷갈리기 쉬운 포인트

- Bootstrap은 JavaScript framework라기보다 CSS/UI framework로 이해하면 쉽다.
- jQuery는 `$()` 함수를 직접 호출하므로 라이브러리 감각이 강하다.
- React는 라이브러리라고 불리지만, 실제 앱 구조에서는 프레임워크처럼 프로젝트 규칙을 강하게 만든다.

## 관련 페이지

- [[entities/jquery]]
- [[entities/bootstrap]]
- [[concepts/jquery-basics]]
- [[concepts/bootstrap-basics]]
- [[summaries/2026-03-27-jquery-ui-interaction]]

## 출처

- `raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/Study/3. UI&UX/교육 자료/library&framework.png`
