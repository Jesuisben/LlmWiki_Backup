---
title: 2026-04-16 장바구니 수량 변경과 재고 검증
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png
status: growing
confidence: high
---
# 2026-04-16 장바구니 수량 변경과 재고 검증

## 한 줄 요약

장바구니 품목 수량 변경과 재고 검증을 구현하며 CartProduct와 Product의 책임 차이를 다뤘다.

## 커리큘럼 위치와 흐름

장바구니 목록을 보여준 뒤 사용자가 수량을 바꾸는 기능으로 넘어갔다. 이때 화면 state만 바꾸면 안 되고, 서버에서 상품 재고와 장바구니 품목을 함께 검증해야 한다.

## 배운 내용

- `CartProductService`와 `CartController`를 수정해 장바구니 품목 찾기, 수량 변경, 재고 부족 처리를 다뤘다.
- CartProduct는 사용자가 담은 수량을 가지며 Product는 원본 상품과 재고 정보를 가진다.
- CartProduct-Product 다이어그램은 여러 사용자의 장바구니 항목이 같은 Product를 참조할 수 있음을 보여준다.

## 핵심 실습 / 예제

- 수량 증가 요청 시 서버는 현재 CartProduct와 연결된 Product 재고를 확인한 뒤 변경을 허용해야 한다.
- 화면에서는 수량 버튼/입력값을 바꾸지만, 최종 검증은 백엔드 업무 로직에서 수행한다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- 프론트에서 버튼을 비활성화해도 백엔드 검증을 생략하면 직접 API 호출로 재고 초과가 가능하다.
- Product 재고와 CartProduct 수량은 서로 다른 값이다.
- CartProduct를 찾을 때 현재 로그인 사용자 Cart에 속한 항목인지 함께 확인해야 한다.

## 관련 페이지

- [[concepts/shopping-cart-flow]]
- [[concepts/product-domain-flow]]
- [[comparisons/controller-service-repository]]
- [[concepts/spring-boot-rest-api]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png`
