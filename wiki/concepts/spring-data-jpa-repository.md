---
title: Spring Data JPA Repository
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [spring-boot, backend, java]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---
# Spring Data JPA Repository

## 정의

Spring Data JPA Repository는 Spring Boot에서 **Entity를 기준으로 DB 조회·저장·삭제를 담당하는 계층**이다. SQL을 직접 매번 작성하지 않고 Repository 인터페이스와 Spring Data JPA 기능으로 DB 작업을 처리한다.

## 왜 중요한가

상품 목록 페이지는 전체 상품 조회뿐 아니라 페이징, 정렬, 기간 검색, 카테고리 검색, 상품명/설명 검색을 필요로 한다. Repository는 이 흐름에서 DB 접근의 마지막 관문이다.

## 핵심 흐름

1. Controller: 프론트엔드 요청 파라미터를 받는다.
2. DTO: 검색 조건을 묶는다.
3. Service: 검색 조건을 조립하고 비즈니스 로직을 처리한다.
4. Repository: 실제 DB 조회를 담당한다.
5. Entity: DB 테이블과 연결되는 객체다.

## 대표 메서드

```java
Page<Product> findAll(Specification<Product> spec, Pageable pageable);
```

- `Specification<Product> spec`: 검색 조건
- `Pageable pageable`: 페이지 번호, 페이지 크기, 정렬 조건
- `Page<Product>`: 페이징 결과와 전체 개수/페이지 수를 담은 결과

## 분리된 하위 주제

- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]] — 동적 검색 조건과 페이징 객체
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]] — Controller/Service/Repository/React 테스트 흐름

## 자주 헷갈리는 점

- Repository는 DB 접근, Service는 업무 로직과 조건 조립을 맡는다.
- `Pageable`은 요청 조건이고 `Page`는 조회 결과다.
- `Specification`은 DB 조건식이고 `SearchDto`는 요청 데이터를 담는 객체다.
- React Router 주소와 Spring API 주소는 역할이 다르다.

## 관련 페이지

- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/pagination-search|페이징과 검색]]
- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
