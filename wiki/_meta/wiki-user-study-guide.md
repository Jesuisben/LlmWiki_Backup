---
title: LLM Wiki 사용자 학습 가이드
created: 2026-07-16
updated: 2026-07-22
type: meta
tags: [curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/_meta/llm-wiki-operating-model.md
  - wiki/_meta/llm-wiki-command-reference.md
status: stable
confidence: high
---

# LLM Wiki 사용자 학습 가이드

## 이 페이지부터 시작하기

이 Wiki에는 두 가지 읽기 방식이 있다. **과목 전체를 한 파일로 복습할 때는 `study-guides/`의 인간용 통합 교재를 읽고**, 특정 날짜·개념·근거를 자세히 찾을 때는 기존 Summary·Concept·Comparison·Raw를 사용한다.

가장 기본적인 학습 순서는 다음과 같다.

> 과목 전체 복습은 Study Guide 한 파일 → 세부 확인이 필요할 때만 Concept·Comparison·날짜 Summary → 실제 코드가 필요할 때 Raw

Study Guide가 있는 과목은 **해당 파일 하나만 읽어도 전체 기억을 복원할 수 있게 만드는 것**이 기준이다. 기존 Wiki 링크는 필수가 아니라 더 자세히 볼 때 사용하는 보조 경로다.

## 지금 무엇을 열어야 할까

| 공부 목적 | 가장 먼저 볼 페이지 | 다음에 볼 페이지 |
|---|---|---|
| 과목 전체 복습 | `study-guides/`의 과목별 인간용 통합 총정리 | 필요할 때만 핵심 Concept와 Comparison |
| 특정 수업일 복습 | 날짜별 Summary | 그날 연결된 Concept |
| 개념 하나 이해 | Concept | 관련 Summary와 Comparison |
| 비슷한 개념 구분 | Comparison | 양쪽 Concept |
| 기술의 전체 학습 이력 확인 | Entity | 날짜별 Summary와 Concept |
| 실제 수업 코드·교안 확인 | 연결된 `raw/` 출처 | 다시 Wiki 설명으로 돌아오기 |
| 공부 순서가 막힘 | 이 가이드 또는 AI에게 질문 | 추천받은 페이지 2~4개 |

## 가장 추천하는 시작점: 인간용 통합 총정리

과목을 다시 공부할 때는 `study-guides/`에 있는 파일 하나를 처음부터 끝까지 읽는다.

- [[study-guides/java-complete-review|Java 인간용 통합 총정리]]

아직 인간용 통합 총정리가 없는 과목은 다음 기존 과목 허브를 사용한다.

- [[summaries/2026-03-20-oracle-subject-review|Oracle 총정리]]
- [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]
- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]
- [[summaries/2026-05-08-aws-subject-review|AWS 총정리]]
- [[summaries/2026-07-08-python-subject-review|Python 총정리]]

Study Guide는 본문 자체에 학습 흐름·핵심 개념·간단한 예제·혼동 포인트·점검 질문을 포함한다. 더 깊이 확인하고 싶은 부분만 기존 Wiki 링크를 따라간다.

## 페이지 종류별 사용법

### Summary: 언제 무엇을 배웠는지 복원하기

`wiki/summaries/`에는 날짜별 수업 요약과 과목 총정리가 있다.

다음 상황에 사용한다.

- 오늘이나 특정 날짜에 무엇을 배웠는지 복습할 때
- 수업 진도를 시간순으로 다시 따라갈 때
- 개념이 실제 수업에서 어떤 순서로 등장했는지 확인할 때

날짜별 복습은 해당 Summary 한 개를 읽은 뒤, 그 페이지의 `관련 페이지`에서 Concept 1~2개만 선택하는 방식이 좋다.

### Concept: 한 가지 개념을 제대로 이해하기

`wiki/concepts/`에는 문법, 원리, 구현 흐름이 정리되어 있다.

예를 들면 다음과 같다.

- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]

Concept를 읽을 때는 다음 네 가지를 확인한다.

1. 왜 필요한가
2. 어떻게 동작하는가
3. 수업에서는 어디에 사용했는가
4. 무엇과 헷갈리는가

### Comparison: 차이를 설명할 수 있게 만들기

`wiki/comparisons/`는 비슷해 보이는 개념을 구분할 때 사용한다. 복습 문제나 면접 준비에 특히 유용하다.

- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]
- [[comparisons/props-vs-state|props vs state]]

읽은 뒤에는 표를 보지 않고 **“A는 언제 쓰고 B는 언제 쓰는지”** 직접 말해본다.

### Entity: 기술별 학습 지도로 사용하기

`wiki/entities/`는 Java, Spring Boot, React, Docker 같은 기술의 정의와 학습 이력을 모은 허브다.

Entity는 세부 문법을 외우는 페이지가 아니라 다음을 확인하는 지도다.

- 이 기술을 언제 처음 배웠는가
- 어떤 기능 구현에 사용했는가
- 관련 Concept와 Summary는 무엇인가
- 다음에 무엇을 공부해야 하는가

예: [[entities/spring-boot|Spring Boot]], [[entities/react|React]], [[entities/docker|Docker]]

### Raw: Wiki로 부족할 때만 원본 확인하기

`raw/`는 사용자가 작성한 원본 수업 노트와 교안이다. 평소 복습의 첫 시작점으로 삼기보다 다음 상황에서 확인한다.

- 실제 수업 코드 전체가 필요할 때
- 강사의 표현이나 수업 진행 순서를 그대로 확인할 때
- Wiki 설명의 출처를 직접 대조할 때

원본을 읽다가 흐름을 잃으면 다시 Summary나 Concept로 돌아온다.

## 상황별 추천 공부법

### 오늘 배운 내용 복습

1. 오늘 날짜의 Summary를 읽는다.
2. `한 줄 요약`과 `배운 내용`을 자신의 말로 다시 설명한다.
3. 관련 Concept 1~2개를 읽는다.
4. 예제 코드나 SQL을 보지 않고 핵심 구조를 다시 작성해본다.
5. 막힌 부분만 `raw/` 원본에서 확인한다.

### 과목 전체 복습

1. 해당 과목의 Study Guide 한 파일을 처음부터 끝까지 읽는다.
2. 예제를 보지 않고 핵심 문법이나 흐름을 다시 써 본다.
3. 마지막 체크리스트에 직접 답한다.
4. 틀리거나 막힌 항목만 Concept·Comparison에서 자세히 확인한다.
5. 실제 수업 코드가 필요할 때만 날짜 Summary와 Raw로 돌아간다.

### 프로젝트 구현 복습

기능 단위 Concept를 먼저 사용한다.

- 전체 구조 → [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- 회원·인증 → [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- 상품 → [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- 장바구니 → [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- 주문 → [[concepts/order-flow|주문 기능 흐름]]
- 페이징·검색 → [[concepts/pagination-search|페이징과 검색]]

각 페이지에서 **사용자 입력 → Frontend 처리 → API 요청 → Backend 처리 → DB → 응답 화면** 순서로 직접 그려본다.

### 시험·면접 대비

1. Comparison 페이지 하나를 고른다.
2. 표를 가리고 차이를 설명한다.
3. 실제 수업이나 프로젝트 사례를 하나 붙인다.
4. Concept에서 정확한 용어를 확인한다.
5. 모르는 내용을 질문 형태로 남기거나 AI에게 확인한다.

## 한 번에 얼마나 읽어야 할까

한 학습 단위는 다음 정도가 적당하다.

- 과목 Study Guide 또는 날짜 Summary 1개
- 핵심 Concept 1~2개
- 필요한 Comparison 0~1개
- 마지막에 자신의 말로 설명하거나 작은 예제 작성

링크를 계속 따라가며 페이지를 많이 여는 것보다, **하나를 읽고 설명하거나 직접 실행하는 것**이 더 중요하다.

## 평소에는 읽지 않아도 되는 파일

- `wiki/index.md`: 전체 페이지를 찾기 위한 카탈로그
- `wiki/log.md`: AI가 언제 무엇을 정리했는지 남기는 작업 기록
- `wiki/_meta/`의 감사·계획 문서: Wiki 유지보수용 자료
- `AGENTS.md`: AI Agent가 따라야 하는 운영 규칙

이 파일들은 공부 교재가 아니다. 단, 현재 보고 있는 사용자 학습 가이드는 `_meta`에 있어도 사용자가 직접 읽기 위한 예외적인 시작 페이지다.

## AI에게 이렇게 요청하기

파일을 직접 고르기 어려우면 자연어로 목적만 말하면 된다.

- `Java를 처음부터 복습하려는데 오늘 볼 위키 3개만 골라줘.`
- `SQL JOIN을 공부할 건데 읽는 순서와 복습 문제를 만들어줘.`
- `장바구니부터 주문까지 관련 페이지를 순서대로 안내해줘.`
- `2026-04-07에 배운 내용을 복습시켜줘.`
- `이번 주에 하루 30분씩 공부할 위키 계획을 만들어줘.`
- `이 개념을 내가 이해했는지 질문으로 확인해줘.`
- `이 답변이 나중에도 유용하면 위키에 보존해줘.`

AI는 `wiki/index.md`에서 관련 페이지를 찾고, Wiki 내용이 부족할 때만 `raw/` 원본을 확인한다.

## 길을 잃었을 때의 기준

무엇을 열어야 할지 모르겠다면 다음 한 줄만 기억한다.

> **과목 전체는 Study Guide 한 파일, 특정 날짜는 Summary, 깊은 이해는 Concept, 차이는 Comparison, 실제 원문은 Raw에서 확인한다.**

## 관련 페이지

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/llm-wiki-command-reference|LLM Wiki 명령어 참고]]
- [[concepts/markdown-basic-syntax|Markdown 기본 문법]]
- [[index|Wiki Index]]
