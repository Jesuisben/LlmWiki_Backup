---
title: 2026-04-13 상품 상세와 useEffect, 서비스 계층
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [spring-boot, react, typescript, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
status: growing
confidence: medium
---

# 2026-04-13 상품 상세와 useEffect, 서비스 계층

## 한 줄 요약

상품 상세 조회를 위해 Spring ProductService와 React useEffect Hook을 연결하는 흐름을 학습했다.

## 배운 내용

- ProductService
- getProductById
- useEffect Hook
- 상품 상세 조회
- MVC/JDBC/Web 복습 권장

## 원본에서 확인한 세부 주제

- JSP 웹 프로그래밍과 스프링 프레임워크 책 공부 한번해보기
- 서비스(ProductService) (05.상품.txt)
- useEffect Hook React 교안 PDF (P.87)
- 컨트롤러(ProductController) (05.상품.txt)
- 컨트롤러(put 요청) (05.상품.txt)
- 테스트 시나리오(get 요청) (05.상품.txt)
- 테스트 시나리오(put 요청) (05.상품.txt)
- 제05장-07. 상세 보기 (05.상품.txt)

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
