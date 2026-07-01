---
title: Spring Data JPA Repository
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [spring-boot, backend, java]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: medium
---

# Spring Data JPA Repository

## 정의

Spring Data JPA Repository는 Entity를 기준으로 DB 조회, 저장, 삭제 같은 작업을 추상화해 주는 계층이다.

## 왜 중요한가

직접 SQL을 매번 쓰지 않아도 상품 목록, 상세 조회, 페이징, 검색 조건 조회를 메서드 중심으로 구현할 수 있다.

## 핵심 설명

- Repository는 DB 접근 담당이다.
- Pageable을 받으면 페이지 번호, 크기, 정렬 조건을 함께 처리할 수 있다.
- 검색 조건에 따라 메서드나 Query를 분기할 수 있다.

## 예시

상품 목록에서 `pageNumber`, `searchMode`, `keyword`를 받아 Repository가 조건에 맞는 Page 결과를 반환한다.

## 자주 헷갈리는 점

- Pageable은 단순 페이지 번호가 아니라 크기와 정렬까지 담을 수 있다.
- Repository는 Controller에서 직접 호출하기보다 Service를 거치는 구조가 일반적이다.

## 관련 개념

- [[concepts/pagination-search|페이징과 검색]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
