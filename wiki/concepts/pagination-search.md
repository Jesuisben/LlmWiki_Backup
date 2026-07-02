---
title: 페이징과 검색
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# 페이징과 검색

## 정의

많은 데이터를 여러 페이지로 나누고, 사용자가 입력한 조건에 맞는 데이터만 조회하는 방식이다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- React ProductList는 pageNumber와 검색 상태를 관리한다.
- useEffect는 페이지 번호나 검색 조건이 바뀔 때 다시 목록을 가져온다.
- ProductController는 query parameter를 받아 Service로 넘긴다.
- Service/Repository는 Pageable, searchDateType, searchMode로 DB 조회를 수행한다.
- 응답에는 현재 페이지 데이터와 전체 페이지 수 같은 UI 정보가 필요하다.

## 수업 예시

- [[summaries/2026-04-21-product-pagination-search-react|2026-04-21 상품 목록 페이징과 필드 검색]] — ProductList.tsx, useEffect, Paging 컴포넌트
- [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22 ProductRepository와 Pageable 검색]] — ProductRepository, Pageable, searchDateType, searchMode, MySQL 테스트

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
