---
title: 장바구니 기능 흐름
created: 2026-07-06
updated: 2026-07-09
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: high
---

# 장바구니 기능 흐름

## 정의

장바구니 기능 흐름은 로그인한 회원이 상품을 장바구니에 담고, 목록에서 선택·수량 변경·삭제·총액 계산·재고 검증을 거쳐 주문으로 넘어가는 과정이다.

## 왜 중요한가

장바구니는 Product, Member, Cart, CartProduct, Order가 연결되는 첫 복합 도메인이다. 단순 CRUD보다 Entity 관계, DTO, 화면 state, Service 검증이 함께 필요하다.

## 핵심 설명

- `CartService`: 회원의 장바구니를 찾거나 없으면 생성한다.
- `CartProductService`: 장바구니 품목 저장, 수량 변경, 삭제, stock 검증을 처리한다.
- `CartProductDto`: 화면에 필요한 상품명, 가격, 이미지, 수량, stock 등을 전달한다.
- React `CartList`: 전체 선택/개별 선택, 총 주문 금액, 수량 input, 삭제 confirm, 주문 버튼을 관리한다.

## 수업 예시

2026-04-14에는 장바구니 Service/Controller/DTO, 04-15에는 전체 선택과 개별 선택, 04-16에는 수량 변경과 재고 검증, [[summaries/2026-04-17-cart-total-array-some|2026-04-17]]에는 `Array.some()`을 이용한 재고 부족 여부 판단과 주문 생성 흐름을 다뤘다.

## 자주 헷갈리는 점

CartProduct는 Cart와 Product를 단순히 연결만 하는 것이 아니라 quantity 같은 업무 데이터를 가진다. 그래서 다대다를 그대로 쓰기보다 중간 Entity로 풀어내는 사고가 중요하다.

## 관련 개념

- [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/props-vs-state|props vs state]]

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
