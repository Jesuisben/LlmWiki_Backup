---
title: DTO, Entity, Service, Controller
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [spring-boot, backend, java]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: medium
---

# DTO, Entity, Service, Controller

## 정의

Spring Boot 백엔드에서 역할을 나누기 위한 대표 계층/객체들이다. Entity는 DB 모델, DTO는 전달 데이터, Service는 업무 규칙, Controller는 요청 입구에 가깝다.

## 왜 중요한가

상품, 장바구니, 주문 기능이 커질수록 모든 코드를 한 파일에 넣으면 이해하기 어렵다. 역할을 나누면 수정 위치를 찾기 쉬워진다.

## 핵심 설명

| 요소 | 역할 |
|---|---|
| Controller | HTTP 요청을 받고 응답을 반환 |
| Service | 업무 규칙과 처리 흐름 담당 |
| Repository | DB 접근 담당 |
| Entity | DB 테이블과 가까운 객체 |
| DTO | 요청/응답 전달용 객체 |

## 예시

장바구니 품목 수량 변경은 Controller가 요청을 받고, Service가 품목 존재 여부와 재고를 확인한 뒤, Repository를 통해 저장한다.

## 자주 헷갈리는 점

- DTO와 Entity가 비슷해 보여도 목적이 다르다.
- Controller가 DB를 직접 다루기 시작하면 코드가 빨리 복잡해진다.
- Service는 단순 저장뿐 아니라 검증과 업무 규칙을 담는다.

## 관련 개념

- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
