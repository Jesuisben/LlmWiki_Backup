---
title: 2026-04-14 장바구니 Service와 DTO
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png
status: growing
confidence: high
---
# 2026-04-14 장바구니 Service와 DTO

## 한 줄 요약

장바구니 기능을 시작하며 Cart, CartProduct, Product 사이의 관계와 DTO/Service/Controller 흐름을 만들었다.

## 커리큘럼 위치와 흐름

상품 도메인 다음 단계로, 사용자가 상품을 담는 장바구니 기능에 들어갔다. 장바구니는 단일 Entity 하나로 끝나지 않고 회원, 장바구니, 장바구니상품, 상품 사이의 관계를 이해해야 한다.

## 배운 내용

- 쇼핑 카트 데이터 구조 다이어그램은 Customer(Member) 1명당 Cart 1개, Cart 1개가 여러 CartProduct를 가지며, 각 CartProduct가 하나의 Product를 참조하는 구조를 보여준다.
- Cart-CartProduct-Product 이미지 2개는 실제 장바구니 안의 수량과 상품 진열대의 원본 상품 정보를 분리해서 이해하도록 돕는다.
- `CartProductService`, `CartService`, `CartController`, DTO 작성이 핵심이다.

## 핵심 실습 / 예제

- 장바구니에 “사과 3개”를 담는다는 것은 Product 자체를 3개 복제하는 것이 아니라, CartProduct가 Product를 참조하면서 quantity를 별도로 가진다는 뜻이다.
- 테스트 시나리오와 DB 확인으로 API가 의도대로 장바구니 데이터를 만드는지 검증했다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- Cart와 Product는 직접 다대다로 묶기보다 수량 같은 추가 속성을 담는 CartProduct 중간 Entity가 필요하다.
- DTO는 화면/API 입출력용이고 Entity는 DB/JPA 관계용이므로 필드가 비슷해도 책임이 다르다.
- Service는 Controller와 Repository 사이에서 중복 담기, 수량 증가, 사용자 장바구니 찾기 같은 업무 규칙을 담당한다.

## 관련 페이지

- [[concepts/shopping-cart-flow]]
- [[comparisons/entity-vs-dto]]
- [[comparisons/controller-service-repository]]
- [[concepts/product-domain-flow]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png`
