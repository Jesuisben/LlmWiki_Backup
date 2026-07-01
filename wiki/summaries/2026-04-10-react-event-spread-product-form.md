---
title: 2026-04-10 React 이벤트 객체와 전개 연산자
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [react, typescript, javascript, frontend, spring-boot]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
status: growing
confidence: medium
---

# 2026-04-10 React 이벤트 객체와 전개 연산자

## 한 줄 요약

React에서 이벤트 객체와 전개 연산자를 사용해 상품 입력 폼 상태를 관리하는 방법을 학습했다.

## 배운 내용

- event.target
- 전개 연산자
- 구조 분해 할당
- 상품 입력 폼 상태
- React 상태 업데이트

## 원본에서 확인한 세부 주제

- Event Object (React 교안 PDF (P.73))
- 전개 연산자 (React 교안 PDF (P.41))
- 제05장-05. 상품 등록 (리액트) (05.상품.txt)
- 등록 페이지(ProductInsertForm.tsx) (리액트) (05.상품.txt) (작성중)
- 서비스(ProductService) (스프링) (05.상품.txt)
- 컨트롤러(ProductController) (스프링) (05.상품.txt)
- 제05장-06. 상품 수정 (리액트) (05.상품.txt)
- 상품 등록과의 공통점과 차이점 (리액트) (05.상품.txt)

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
