---
title: 주문 기능 흐름
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: high
---

# 주문 기능 흐름

## 정의

주문 기능 흐름은 선택된 장바구니 품목을 주문으로 생성하고, 주문 목록에서 상태를 확인·변경하는 과정이다.

## 왜 중요한가

주문은 쇼핑몰에서 장바구니 이후 실제 거래 상태로 넘어가는 지점이다. 재고 검증, 주문 상품 생성, 주문 상태 변경, 관리자/사용자 화면 차이가 함께 들어간다.

## 핵심 설명

- 장바구니에서 선택된 CartProduct를 기준으로 주문을 생성한다.
- OrderStatus enum으로 주문 상태를 제한하고, 상태 변경 API로 완료 처리 등을 수행한다.
- React OrderList는 orders 배열을 `map()`으로 렌더링하고 role에 따라 버튼을 다르게 보여준다.
- Spring에서는 JPQL/Repository/Service를 이용해 상태 변경과 목록 조회를 처리한다.

## 수업 예시

2026-04-16에는 OrderStatus와 영속성 전이, 04-17에는 OrderService와 ProductService를 수정한 주문 생성·재고 차감 흐름, [[summaries/2026-04-20-order-list-scenario|2026-04-20]]에는 주문 목록 화면과 상태 변경 테스트 시나리오를 정리했다.

## 관련 개념

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[comparisons/jpql-vs-sql|JPQL vs SQL]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
