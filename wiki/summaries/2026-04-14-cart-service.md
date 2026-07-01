---
title: 2026-04-14 장바구니 Service와 DTO
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [spring-boot, backend, react, typescript, project]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
status: growing
confidence: medium
---

# 2026-04-14 장바구니 Service와 DTO

## 한 줄 요약

장바구니 기능 구현을 시작하며 CartProductService, CartService, CartProductDto 등 백엔드 계층을 작성했다.

## 배운 내용

- CartProductService
- CartService
- CartProductDto
- 장바구니 저장
- 서비스 계층 역할

## 원본에서 확인한 세부 주제

- 서비스(CartProductService) 신규 작성 (스프링) (06.장바구니.txt)
- 서비스(CartService) 신규 작성 (스프링) (06.장바구니.txt)
- 컨트롤러(CartController) 신규 작성 (스프링) (06.장바구니.txt)
- 테스트 시나리오 (스프링) (06.장바구니.txt)
- 데이터 베이스 확인 (MySQL) (06.장바구니.txt)
- 제06장-02. 내 장바구니 목록 보기
- 파일 : CartProduct.ts(신규 작성) (리액트) (06.장바구니.txt)
- 라우팅 설정 (리액트) (06.장바구니.txt)

## 핵심 개념

- 백엔드의 Controller/Service/Repository/DTO/Entity 역할을 나누어 생각한다.
- 프론트엔드는 React 컴포넌트, props, state, Hook, 라우팅으로 화면과 상태를 관리한다.
- 실습 기능은 단독 문법보다 로그인, 상품, 장바구니, 주문처럼 이어지는 업무 흐름 안에서 이해해야 한다.

## 헷갈린 점 / 질문

- 같은 데이터가 백엔드 Entity, DTO, 프론트 TypeScript 타입에서 각각 어떻게 표현되는지 구분할 필요가 있다.
- React 라우팅 주소와 Spring Boot API 주소는 역할이 다르므로 혼동하지 않아야 한다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
