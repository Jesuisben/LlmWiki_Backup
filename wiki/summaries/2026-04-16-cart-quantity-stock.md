---
title: 2026-04-16 장바구니 수량 변경과 주문 Entity
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
status: growing
confidence: high
---

# 2026-04-16 장바구니 수량 변경과 주문 Entity

## 한 줄 요약

Cart 수량 변경 보정 후 OrderStatus, Order, OrderProduct, OrderDto를 만들며 장바구니에서 주문으로 도메인 흐름을 확장했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

장바구니는 주문 전 임시 상태이고, 주문은 구매 이력으로 남는 별도 도메인이다. 수량/재고/회원/상품 관계를 명확히 나눠야 한다.

## 핵심 개념

- CartProductService/CartController와 CartList.tsx를 수정해 수량 변경 흐름을 보강했다.
- 정규화 개념을 다시 언급하며 주문 데이터 구조가 왜 여러 테이블로 나뉘는지 연결했다.
- OrderStatus enum, Order Entity, OrderProduct Entity, OrderProductDto, OrderDto를 작성했다.
- OrderRepository, OrderService, OrderController로 주문 생성 API의 기반을 만들었다.

## 실습 / 예제

CartList에서 선택한 장바구니 품목을 주문 DTO로 보내고, Spring Service가 Order/OrderProduct를 생성하는 흐름을 준비했다.

## 헷갈린 점 / 질문

CartProduct와 OrderProduct는 모두 “상품과 수량”을 담지만 의미가 다르다. CartProduct는 주문 전 장바구니 상태, OrderProduct는 주문 확정 후 이력이다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
