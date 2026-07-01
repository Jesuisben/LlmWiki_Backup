---
title: 2026-04-15 장바구니 목록과 TypeScript props
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [react, typescript, frontend, spring-boot, project]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
status: growing
confidence: medium
---

# 2026-04-15 장바구니 목록과 TypeScript props

## 한 줄 요약

React 장바구니 목록에서 전체 선택, props 구조 분해, 타입 지정, 로그인 사용자 조건 처리를 학습했다.

## 배운 내용

- CartList 전체 선택
- props 구조 분해 할당
- AppProps 타입
- user 조건 검사
- 장바구니 목록 UI

## 원본에서 확인한 세부 주제

- 카트 목록(전체 선택 기능) (리액트) (06.장바구니.txt)
- MenuItems.tsx에 코드 추가
- 카트 목록(개별 선택 기능) (리액트) (06.장바구니.txt)
- 테스트 시나리오 (리액트) (06.장바구니.txt)
- 제06장-03. 카트 상품 수량 변경하기
- 카트 내 수량 변경 (리액트) (06.장바구니.txt)
- 서비스(CartProductService) (스프링) (06.장바구니.txt)
- 컨트롤러(CartController) (스프링) (06.장바구니.txt)

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
