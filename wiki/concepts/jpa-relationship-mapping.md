---
title: JPA 연관관계 매핑
created: 2026-07-06
updated: 2026-07-09
type: concept
tags: [spring, spring-boot, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# JPA 연관관계 매핑

## 정의

JPA 연관관계 매핑은 Java Entity 사이의 관계를 DB의 외래키 관계와 연결하는 방법이다. 수업에서는 상품, 장바구니, 장바구니 상품, 주문 흐름에서 `@ManyToOne`, `@OneToMany`, `@OneToOne`, `@JoinColumn`, 영속성 전이(cascade)가 반복해서 등장했다.

## 왜 중요한가

쇼핑몰 기능은 단일 테이블 하나로 끝나지 않는다. 회원은 장바구니를 가지고, 장바구니는 여러 CartProduct를 가지며, CartProduct는 원본 Product를 참조한다. 이 관계를 Entity에 표현해야 Service 계층에서 회원의 장바구니 찾기, 상품 수량 변경, 주문 생성 같은 로직을 자연스럽게 작성할 수 있다.

## 핵심 설명

- `@ManyToOne`: 여러 자식이 하나의 부모를 참조한다. 예: 여러 CartProduct가 하나의 Product를 참조한다.
- `@OneToMany`: 부모가 여러 자식을 컬렉션으로 가진다. 예: Cart가 여러 CartProduct를 가진다.
- `@JoinColumn`: 외래키 컬럼을 가진 쪽에 두는 경우가 많다. 수업 질문처럼 “왜 여기는 JoinColumn을 쓰고 저기는 안 쓰는가”는 실제 FK를 어느 테이블이 들고 있는지를 보면 풀린다.
- cascade/영속성 전이: 부모 Entity를 저장·삭제할 때 연결된 자식 Entity 작업도 함께 전파할지 정하는 설정이다.

## 예시

CartProduct는 단순 연결 테이블이 아니라 quantity 같은 업무 데이터를 가지므로 Entity로 다루는 것이 자연스럽다. 이것이 장바구니-상품 관계를 다대다 그대로 두지 않고 중간 Entity로 푸는 이유다.

## 자주 헷갈리는 점

- 일대다/다대일 이름보다 외래키를 실제로 들고 있는 쪽이 어디인지가 먼저다.
- Entity를 그대로 JSON으로 노출하면 순환 참조나 과한 데이터 노출이 생길 수 있어 DTO와 함께 설계해야 한다.

## 관련 개념

- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
