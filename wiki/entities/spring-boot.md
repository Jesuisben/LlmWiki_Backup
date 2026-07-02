---
title: Spring Boot
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [spring-boot, spring, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# Spring Boot

## 무엇인가

Spring 기반 백엔드 애플리케이션을 빠르게 구성하고 API, 업무 로직, DB 접근 계층을 만드는 프레임워크다.

## 이 위키에서의 맥락

- [[summaries/2026-03-30-fullstack-environment-setup|2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환]]에서 초기 구성으로 등장했다.
- [[summaries/2026-03-31-spring-boot-controller-html|2026-03-31 Spring Boot Controller와 HTML 응답]]에서는 FruitHtmlController와 HTML 응답으로 Controller의 역할을 배웠다.
- 회원, 상품, 장바구니, 주문, 페이징 기능을 구현하며 백엔드 중심 기술이 됐다.

## 핵심 기능 / 특징

- Controller로 HTTP 요청 처리
- Service로 장바구니 저장·주문 처리·재고 검증 같은 업무 규칙 구현
- Repository/JPA로 DB 접근
- DTO/Entity 구분과 Pageable/Specification 검색 처리

## 헷갈리기 쉬운 점

Controller에 모든 코드를 넣으면 단기적으로는 편하지만 기능이 커질수록 유지보수가 어렵다.

## 관련 개념

- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]

## 학습 이력

이 페이지는 단순 정의가 아니라, 수업에서 이 기술이 처음 등장한 맥락과 이후 Java/Oracle/UI&UX/Spring/React 프로젝트 흐름으로 확장된 위치를 추적하기 위한 엔티티 페이지다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
