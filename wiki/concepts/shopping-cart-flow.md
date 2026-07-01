---
title: 장바구니 기능 흐름
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [project, spring-boot, react, typescript]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: medium
---

# 장바구니 기능 흐름

## 정의

장바구니 기능은 사용자가 상품을 담고, 수량을 조절하고, 선택한 품목을 주문으로 넘기기 전까지 관리하는 흐름이다.

## 왜 중요한가

장바구니는 프론트 상태 관리와 백엔드 검증이 동시에 필요한 대표 기능이다. 특히 재고 검증과 선택/전체 선택 로직이 함께 등장한다.

## 핵심 설명

1. 사용자가 상품을 장바구니에 담는다.
2. 백엔드는 Cart, CartProduct 같은 객체로 저장한다.
3. React는 CartList에서 목록을 보여준다.
4. 사용자는 전체 선택/개별 선택과 수량 변경을 한다.
5. 백엔드는 품목 존재 여부와 재고를 검증한다.
6. 선택된 품목이 주문 단계로 이어진다.

## 예시

`CartProductService`가 장바구니 품목을 찾지 못하면 오류를 반환하고, 재고가 부족하면 수량 변경을 막는다.

## 자주 헷갈리는 점

- 선택 상태는 화면 상태이고, 재고 검증은 백엔드 업무 규칙이다.
- 수량 변경은 단순 숫자 변경이 아니라 재고와 품목 존재 여부 확인이 필요하다.

## 관련 개념

- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
