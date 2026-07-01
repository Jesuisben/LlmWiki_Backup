---
title: 2026-04-21 상품 목록 페이징과 필드 검색
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [react, typescript, spring-boot, frontend, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: medium
---

# 2026-04-21 상품 목록 페이징과 필드 검색

## 한 줄 요약

React 상품 목록에서 pageNumber 등 페이징 파라미터를 추가하고 Paging 컴포넌트와 검색 상태를 다뤘다.

## 배운 내용

- ProductList.tsx
- useEffect 의존성
- 페이징 parameters
- Paging 컴포넌트
- 필드 검색 준비

## 원본에서 확인한 세부 주제

- 상품 목록(ProductList.tsx) (리액트) (08.페이징과 필드 검색.txt)
- useEffect Hook (React 교안 PDF (P.88))
- 서비스(ProductService) (스프링) (08.페이징과 필드 검색.txt)
- 컨트롤러(ProductController) (스프링) (08.페이징과 필드 검색.txt)
- 페이징(ProductList.tsx) (리액트) (08.페이징과 필드 검색.txt)
- 테스트하기 (MySQL) (08.페이징과 필드 검색.txt)
- Querydsl 관련 API (SpringBoot 교안 PDF (P.119))
- 제08장-02. 필드 검색 (08.페이징과 필드 검색.txt)

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
- [[concepts/pagination-search|페이징과 검색]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
