---
title: 2026-04-17 장바구니 합계와 Array some
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [react, typescript, javascript, frontend, project]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: medium
---

# 2026-04-17 장바구니 합계와 Array some

## 한 줄 요약

장바구니 화면에서 재고/합계 계산을 보강하고 JavaScript Array some 메서드를 학습했다.

## 배운 내용

- stock 필드 추가
- CartList.tsx 수정
- 구조 분해와 타입 지정
- Array some()
- 장바구니 합계/선택 로직

## 원본에서 확인한 세부 주제

- 여러가지 수정하기
- JS Array some() 메소드 W3Schools에서 공부
- CartList.tsx 코드 수정 (리액트)
- CartController 코드 추가 (스프링)
- OrderService 코드 추가 (스프링)
- ProductService 코드 전체 수정 (스프링)
- CartProductService (스프링) 수정
- 주문 하기(함수 구현) (리액트) (07.주문.txt)

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
