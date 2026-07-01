---
title: 2026-04-09 상품 삭제, 라우팅, JSX와 표
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [spring-boot, react, typescript, html, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
status: growing
confidence: medium
---

# 2026-04-09 상품 삭제, 라우팅, JSX와 표

## 한 줄 요약

상품 삭제 기능과 React 라우팅, JSX 내부 JavaScript 표현, HTML 표 병합 속성을 함께 다뤘다.

## 배운 내용

- JwtTokenProvider 수정
- 상품 삭제
- AppRouters.tsx 라우팅
- JSX 안의 JavaScript
- rowspan/colspan 표 병합

## 원본에서 확인한 세부 주제

- 제05장-04. 상품 삭제
- 라우팅 설정(AppRouters.tsx) (리액트) (05.상품.txt)
- 병합 관련 속성
- JSX안에서 JS관련
- 이벤트 버블링 방지
- 등록/수정/삭제 버튼 만들기 (리액트) (05.상품.txt)
- 서비스(ProductService) (스프링) (05.상품.txt)

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

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
