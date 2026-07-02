---
title: 장바구니 기능 흐름
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [project, spring-boot, react]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png
status: growing
confidence: high
---

# 장바구니 기능 흐름

## 정의

사용자가 상품을 담고, 목록에서 선택·수량 변경·합계 계산을 하며 주문 전 상태를 관리하는 쇼핑몰 핵심 기능이다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- 로그인 사용자가 상품을 장바구니에 담는다.
- CartProductService/CartService가 저장 규칙과 중복 여부를 처리한다.
- CartController가 저장·목록·수량 변경 요청을 받는다.
- React CartList가 전체 선택/개별 선택/수량/합계를 반영한다.
- 재고 부족이나 잘못된 수량은 검증과 메시지로 처리한다.

## 수업 예시

- [[summaries/2026-04-14-cart-service|2026-04-14 장바구니 Service와 DTO]] — CartProductService, CartService, CartProductDto, CartController
- [[summaries/2026-04-15-cart-list-selection-typescript|2026-04-15 장바구니 목록과 TypeScript props]] — 전체 선택/개별 선택과 props 타입
- [[summaries/2026-04-16-cart-quantity-stock|2026-04-16 장바구니 수량 변경과 재고 검증]] — 수량 변경과 재고 검증
- [[summaries/2026-04-17-cart-total-array-some|2026-04-17 장바구니 합계와 Array some]] — 합계와 Array some

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/order-flow|주문 기능 흐름]]


## 교육자료 대조 보강

쇼핑 카트 데이터 구조 다이어그램은 `Customer(Member) 1 : 1 Cart`, `Cart 1 : N CartProduct`, `CartProduct N : 1 Product` 관계를 보여준다. CartProduct는 “사용자가 어떤 상품을 몇 개 담았는가”를 표현하는 중간 Entity이며, Product는 진열대의 원본 상품 정보처럼 여러 장바구니 항목에서 참조될 수 있다. 이 구분은 수량 변경과 재고 검증을 이해하는 핵심이다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
