---
title: 주문 기능 흐름
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [project, spring-boot, react]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: high
---

# 주문 기능 흐름

## 정의

장바구니에 담긴 상품을 주문으로 확정하고 주문 목록과 상태를 관리하는 과정이다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- 장바구니에서 주문할 상품을 선택한다.
- Order와 OrderProduct 같은 주문 Entity를 만든다.
- Service가 주문 생성, 상태 변경, 사용자 조건을 처리한다.
- Repository가 최신 주문 우선 조회 같은 DB 조회를 담당한다.
- React OrderList가 주문 상태와 관리자/일반 사용자 버튼을 보여준다.

## 수업 예시

- [[summaries/2026-04-16-cart-quantity-stock|2026-04-16 장바구니 수량 변경과 재고 검증]] — OrderStatus, 연관 관계 매핑, 영속성 전이, Order/OrderProduct
- [[summaries/2026-04-20-order-list-scenario|2026-04-20 주문 목록과 테스트 시나리오]] — OrderList.tsx, 주문 상태 표시, 테스트 시나리오

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
