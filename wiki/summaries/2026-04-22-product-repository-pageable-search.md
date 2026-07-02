---
title: 2026-04-22 ProductRepository와 Pageable 검색
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---
# 2026-04-22 ProductRepository와 Pageable 검색

## 한 줄 요약

Spring Data JPA Repository에서 Pageable과 검색 조건을 받아 상품 목록을 조회하는 백엔드 검색 흐름을 학습했다.

## 커리큘럼 위치와 흐름

전날 React 검색 UI를 만든 뒤, 백엔드에서 실제로 검색 조건과 페이징을 처리하는 단계다. 프론트 state가 Controller 파라미터가 되고, Service가 검색 조건을 조립하고, Repository가 DB 조회를 수행한다.

## 배운 내용

- `ProductRepository`에 검색/페이징 메서드를 작성했다.
- `ProductService`는 필드 검색 조건과 페이징 기본 정보를 사용해 상품 목록 조회 로직을 구성했다.
- `ProductController`는 pageNumber, 검색 필드, 검색어 같은 요청 파라미터를 받는다.
- SpringBoot 교안 p.89~90의 query method, JPQL, Pageable/Sort 개념과 연결된다.

## 핵심 실습 / 예제

- MySQL에서 상품 날짜를 변경해 필드 검색/정렬 테스트 데이터를 준비했다.
- 필드 검색 기능 PDF의 페이징 지표는 백엔드 응답 DTO 또는 프론트 Paging 계산 기준으로 반영된다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- Repository 메서드 이름만으로 해결되는 검색과 Specification/동적 조건이 필요한 검색을 구분해야 한다.
- Pageable은 “페이지 화면 컴포넌트”가 아니라 DB 조회 범위를 제한하는 백엔드 요청 객체다.
- 검색 조건이 없을 때 전체 목록 조회로 자연스럽게 fallback되는지 확인해야 한다.

## 관련 페이지

- [[concepts/spring-product-search-flow]]
- [[concepts/spring-data-jpa-specification-pageable]]
- [[concepts/pagination-search]]
- [[concepts/spring-data-jpa-repository]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
