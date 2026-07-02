---
title: 2026-04-17 장바구니 합계와 Array some
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
status: growing
confidence: high
---
# 2026-04-17 장바구니 합계와 Array some

## 한 줄 요약

장바구니 화면에서 선택 상품 합계와 재고 상태를 계산하고 JavaScript `Array.some()`을 활용했다.

## 커리큘럼 위치와 흐름

수량 변경 기능 이후, 장바구니 화면을 사용자 친화적으로 만들기 위해 합계 계산과 주문 가능 여부 판단을 보강했다. JavaScript 배열 메서드가 실제 UI 상태 판단에 쓰이는 예다.

## 배운 내용

- 선택된 CartProduct의 가격×수량을 합산해 총액을 계산했다.
- W3Schools 등을 통해 `Array.some()`이 배열 중 하나라도 조건을 만족하면 true를 반환한다는 점을 확인했다.
- 재고 부족 상품이 하나라도 있으면 주문 버튼을 막는 식의 조건에 연결할 수 있다.

## 핵심 실습 / 예제

- `cartProducts.some(item => item.quantity > item.stock)` 같은 형태로 하나라도 재고 초과인지 판단할 수 있다.
- 합계 계산은 선택 상태, 수량, 가격을 모두 반영해야 한다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- `some`, `every`, `filter`, `map`, `reduce`는 비슷해 보여도 반환값과 목적이 다르다.
- 화면 합계는 사용자 편의 표시이고, 실제 결제/주문 검증은 서버에서도 다시 해야 한다.
- 선택 상태와 수량 상태가 어긋나면 합계가 틀어질 수 있다.

## 관련 페이지

- [[concepts/shopping-cart-flow]]
- [[concepts/react-typescript-basics]]
- [[comparisons/props-vs-state]]
- [[entities/javascript]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
