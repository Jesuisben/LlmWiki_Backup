---
title: 2026-04-14 장바구니 Service와 DTO
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
status: growing
confidence: high
---

# 2026-04-14 장바구니 Service와 DTO

## 한 줄 요약

CartProductService, CartService, CartController를 만들고 React CartList와 CartProduct 타입, CartItemDto로 장바구니 목록 조회 흐름을 구성했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

장바구니는 단순히 상품 id만 저장하는 기능이 아니라 회원별 Cart, CartProduct, 수량, 상품 정보 DTO가 함께 움직이는 기능이다.

## 핵심 개념

- CartProductService에서 장바구니 품목 저장/조회 로직을 작성했다.
- CartService와 CartController로 내 장바구니 목록 API를 구성했다.
- React `CartProduct.ts` 타입과 CartList 라우팅/폼을 만들었다.
- CartItemDto로 Entity를 화면 표시용 데이터 구조로 변환했다.

## 실습 / 예제

Spring API가 CartItemDto 목록을 반환하고 React CartList가 이를 table/list 형태로 표시하는 흐름을 맞췄다.

## 헷갈린 점 / 질문

Entity를 그대로 화면에 보내면 관계 객체가 너무 깊어지거나 불필요한 정보가 노출될 수 있다. 장바구니 목록에는 DTO가 특히 중요하다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[comparisons/entity-vs-dto|Entity vs DTO]], [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
