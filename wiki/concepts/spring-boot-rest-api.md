---
title: Spring Boot REST API
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

# Spring Boot REST API

## 정의

Spring Boot REST API는 브라우저나 React 앱의 요청을 받아 JSON 같은 데이터 응답을 제공하는 백엔드 인터페이스다.

## 왜 중요한가

React와 Spring Boot를 분리해서 개발할 때 프론트엔드는 화면을 담당하고, 백엔드는 데이터와 업무 규칙을 API로 제공한다.

## 핵심 설명

- Controller: 요청 주소와 HTTP 메서드를 받는다.
- DTO: 요청/응답에 필요한 데이터 모양을 정한다.
- Service: 실제 업무 규칙을 처리한다.
- Repository: DB 접근을 담당한다.
- Entity: DB 테이블과 가까운 객체 모델이다.

## 예시

상품 상세 조회에서는 React가 상품 id로 요청하고, Spring Boot는 Controller → ProductService → ProductRepository 순서로 데이터를 찾아 응답한다.

## 자주 헷갈리는 점

- Controller는 입구이지 모든 일을 하는 장소가 아니다.
- Entity를 그대로 화면에 노출하기보다 DTO로 필요한 데이터만 전달하는 편이 안전하다.
- GET/POST/PUT/DELETE는 기능 이름이 아니라 HTTP 요청 의도에 맞게 선택한다.

## 관련 개념

- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
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
