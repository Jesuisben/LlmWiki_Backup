---
title: 2026-04-16 장바구니 수량 변경과 재고 검증
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
status: growing
confidence: high
---

# 2026-04-16 장바구니 수량 변경과 재고 검증

## 한 줄 요약

CartProductService/Controller를 수정해 장바구니 품목 찾기, 수량 변경, 삭제, 재고 검증을 다루고 주문 기능의 OrderStatus·영속성 전이로 넘어갔다.

## 배운 내용

- 주제: 수량 변경과 주문 전환
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

장바구니 수량은 사용자가 자주 바꾸는 값이고 상품 재고보다 많이 주문하지 못하게 검증해야 실제 쇼핑몰 흐름이 된다.

## 핵심 개념

CartProductService는 cartProductId로 품목을 찾고 Product stock과 비교해 수량을 조정한다. React는 수량 input이 바뀔 때 API를 호출하고 삭제 전 confirm을 띄운다. 후반에는 주문 Entity, OrderStatus enum, JPA cascade/영속성 전이를 확인했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

재고 검증은 프론트에서만 하면 안 된다. 사용자가 API를 직접 호출할 수 있으므로 Service 계층에서 다시 검증해야 한다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
