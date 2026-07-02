---
title: Library vs Framework
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [javascript, bootstrap, spring, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md
  - raw/Study/3. UI&UX/교육 자료/library&framework.png
status: growing
confidence: high
---

# Library vs Framework

## 비교 목적

UI&UX 수업에서는 jQuery를 배우며 Library와 Framework의 차이를 함께 다뤘다. 이후 Bootstrap, Spring Boot, React를 배울 때 “내가 도구를 호출하는가, 정해진 틀 안에 코드를 넣는가”를 구분하는 기준이 된다.

## 한눈에 보기

| 항목 | Library | Framework |
|---|---|---|
| 제어 흐름 | 개발자가 제어 | 프레임워크가 전체 흐름 제어 |
| 사용 방식 | 필요할 때 호출 | 정해진 구조 안에 코드를 채움 |
| 자유도 | 높음 | 상대적으로 낮음 |
| 구조 | 자유 | 이미 정해진 구조가 있음 |
| 수업 예시 | jQuery | Bootstrap, Spring Boot |

## 핵심 차이

Library는 “필요할 때 내가 가져다 쓰는 도구 모음”이다. 예를 들어 jQuery에서 `$("#grayImg").click(...)`은 개발자가 원하는 순간 원하는 기능을 호출하는 방식이다.

Framework는 “이미 만들어진 틀 안에서 내가 코드를 채워 넣는 구조”다. Bootstrap은 정해진 class 체계에 맞춰 UI를 만들고, Spring Boot는 Controller/Service/Repository 같은 구조 안에서 백엔드 코드를 작성한다. ^[raw/Study/3. UI&UX/교육 자료/library&framework.png]

## 헷갈리기 쉬운 포인트

- Bootstrap은 CSS class를 가져다 쓰는 느낌도 있지만, 수업 자료에서는 Framework 예시로 다뤘다.
- jQuery는 JavaScript 언어 자체가 아니라 JavaScript로 만든 Library다.
- Framework라고 해서 무조건 나쁘거나 답답한 것이 아니다. 팀 프로젝트에서는 구조가 정해져 있어야 협업과 유지보수가 쉬워진다.

## 관련 페이지

- [[summaries/2026-03-27-jquery-ui-interaction|2026-03-27 jQuery와 UI 상호작용]]
- [[concepts/jquery-basics|jQuery 기본]]
- [[concepts/bootstrap-basics|Bootstrap 기본]]
- [[entities/spring-boot|Spring Boot]]

## 출처

- `raw/Study/3. UI&UX/2026.03.27(금)/2026.03.27(금).md`
- `raw/Study/3. UI&UX/교육 자료/library&framework.png`
