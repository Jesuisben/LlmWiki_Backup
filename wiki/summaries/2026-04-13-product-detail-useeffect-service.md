---
title: 2026-04-13 상품 상세와 useEffect, 서비스 계층
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
status: growing
confidence: high
---

# 2026-04-13 상품 상세와 useEffect, 서비스 계층

## 한 줄 요약

상품 수정/상세 조회를 마무리하고, useEffect로 상세 데이터를 불러온 뒤 장바구니 Entity 관계 매핑으로 넘어갔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

목록에서 상세 페이지로 이동하면 URL의 id를 기준으로 백엔드에서 단건 데이터를 조회해야 한다. 이 패턴은 이후 장바구니와 주문 상세에도 반복된다.

## 핵심 개념

- ProductService와 ProductController의 GET/PUT 요청 처리와 테스트 시나리오를 확인했다.
- ProductDetail.tsx에서 상품 id를 기준으로 상세 데이터를 요청하고 화면에 표시했다.
- 장바구니 zip을 받아 Cart/CartProduct 구조로 넘어가며 JPA 연관관계 매핑을 시작했다.
- Cart와 Product 사이의 다대다 관계를 직접 두지 않고 CartProduct 중간 Entity로 풀어내는 구조를 배웠다.

## 실습 / 예제

React `useEffect`에서 상세 API를 호출하고, Spring Controller가 id 기반으로 Product를 조회해 DTO/응답으로 돌려주는 흐름을 실습했다.

## 헷갈린 점 / 질문

다대다 관계를 그대로 매핑하면 수량·선택 여부 같은 중간 속성을 넣기 어렵다. 장바구니에서는 CartProduct 같은 연결 Entity가 필요하다.

## 관련 페이지

- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]], [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]], [[concepts/shopping-cart-flow|장바구니 기능 흐름]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
