---
title: 2026-04-14 장바구니 Service와 DTO
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
status: growing
confidence: high
---

# 2026-04-14 장바구니 Service와 DTO

## 한 줄 요약

장바구니 기능 구현을 시작하며 CartProductService, CartService, CartController, CartProductDto를 만들고 로그인 사용자 기준 장바구니 데이터를 조회했다.

## 배운 내용

- 주제: 장바구니 백엔드 시작
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

상품 도메인 다음 단계는 사용자가 상품을 담는 상태를 저장하는 장바구니다. 단순 상품 목록과 달리 회원, 카트, 상품, 수량이 함께 연결된다.

## 핵심 개념

CartProductService는 장바구니 품목을 저장하고 CartService는 회원의 Cart를 찾거나 생성한다. Controller는 로그인 사용자 id와 상품 id/수량을 받아 장바구니에 담고 React CartList는 user id가 있을 때만 목록을 요청한다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

Entity를 그대로 화면에 보내기보다 DTO를 쓰면 필요한 필드만 전달하고 순환 참조나 과한 데이터 노출을 줄일 수 있다. CartProduct는 Product와 Cart 사이에서 수량 같은 추가 정보를 담는 중간 Entity다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[comparisons/entity-vs-dto|Entity vs DTO]], [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
