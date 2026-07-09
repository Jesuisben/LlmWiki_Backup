---
title: 2026-04-17 장바구니 합계와 Array some
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: high
---

# 2026-04-17 장바구니 합계와 Array some

## 한 줄 요약

JavaScript Array `some()`과 CartList 수정으로 장바구니 선택/재고/합계 처리를 보강하고, 주문하기와 주문 목록 조회 기능으로 넘어갔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

주문 버튼은 아무 품목이나 보내는 것이 아니라 선택 여부, 재고, 수량, 로그인 사용자 조건을 검증한 뒤 동작해야 한다.

## 핵심 개념

- W3Schools로 JavaScript Array `some()` 메서드를 확인했다.
- CartList, CartController, OrderService, ProductService, CartProductService를 함께 수정했다.
- React에서 주문하기 함수를 구현하고 테스트 시나리오를 확인했다.
- OrderList, OrderDetailDto, OrderRepository, OrderService, OrderController로 주문 내역 조회를 시작했다.

## 실습 / 예제

선택된 장바구니 품목 중 조건을 만족하는 항목이 있는지 `some()`으로 확인하고, 주문 생성 후 장바구니/상품 재고 상태를 갱신하는 흐름을 실습했다.

## 헷갈린 점 / 질문

`map()`은 목록을 변환/렌더링할 때, `some()`은 조건을 만족하는 항목이 하나라도 있는지 확인할 때 쓴다. 둘 다 배열 메서드지만 목적이 다르다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[concepts/react-form-state-event|React 폼 상태와 이벤트]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
