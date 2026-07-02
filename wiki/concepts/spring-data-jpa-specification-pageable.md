---
title: Spring Data JPA Specification과 Pageable
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [spring-boot, backend, java]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---
# Spring Data JPA Specification과 Pageable

## `Specification` 이해하기

`Specification<Product>`는 상품 검색 조건을 객체처럼 조립하기 위한 도구다.

수업 코드에서는 다음 조건들이 등장했다.

| 조건 | 역할 |
|---|---|
| `hasDateRange(searchDateType)` | 기간 조건 |
| `hasCategory(categoryEnum)` | 카테고리 조건 |
| `hasNameLike(searchKeyword)` | 상품명 검색 |
| `hasDescriptionLike(searchKeyword)` | 상품 설명 검색 |

핵심은 검색 조건을 문자열 SQL로 직접 이어붙이는 것이 아니라, 조건 객체를 하나씩 `and`로 결합한다는 점이다.

```java
spec = spec.and(ProductSpecification.hasCategory(categoryEnum));
```

이 구조는 Oracle 수업에서 배운 `WHERE`, `AND`, 조건 조합의 Spring Boot 버전처럼 볼 수 있다.

## `Pageable` 이해하기

`Pageable`은 단순히 페이지 번호만 담는 객체가 아니다. 다음 정보를 함께 담는다.

- 페이지 번호: `pageNumber`
- 페이지 크기: `pageSize`
- 정렬 조건: `sort`

```java
Sort sort = Sort.by(Sort.Order.desc("id"));
Pageable pageable = PageRequest.of(pageNumber, pageSize, sort);
```

위 코드는 “`pageNumber`번째 페이지를 `pageSize`개씩 가져오되, `id` 내림차순으로 정렬하라”는 뜻이다.

`Page<Product>` 결과에는 단순 상품 목록뿐 아니라 다음 정보도 들어간다.

- 전체 상품 개수
- 전체 페이지 수
- 현재 페이지 번호
- 현재 페이지의 상품 목록

원본 Controller 코드에서도 이를 확인하기 위해 다음 값을 출력했다.

```java
System.out.println("총 상품 갯수 : " + productPage.getTotalElements());
System.out.println("총 페이지 번호 : " + productPage.getTotalPages());
System.out.println("현재 페이지 번호 : " + productPage.getNumber());
```

## 관련 페이지

- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/pagination-search|페이징과 검색]]


## 교육자료 대조 보강

필드 검색 기능 PDF의 페이징 지표는 프론트가 보여줄 페이지 버튼 계산에 쓰이고, Spring Data JPA의 `Pageable`/`Sort`는 DB 조회 범위를 제한하는 백엔드 객체다. Specification은 검색 필드가 동적으로 바뀔 때 조건을 조립하는 도구로 이해하면 좋다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
