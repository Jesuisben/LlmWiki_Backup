---
title: 2026-04-22 ProductRepository와 Pageable 검색
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, backend, frontend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# 2026-04-22 ProductRepository와 Pageable 검색

## 한 줄 요약

ProductRepository의 `Specification<Product>` + `Pageable` 검색 메서드, ProductService/Controller 검색 처리, MySQL 테스트 시나리오를 정리하며 4과목 기능 구현 흐름을 마무리했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

검색/페이징은 프론트 state만으로 끝나지 않는다. Repository가 검색 조건과 정렬/페이지 정보를 함께 받아 DB 조회를 수행해야 한다.

## 핵심 개념

- `Page<Product> findAll(Specification<Product> spec, Pageable pageable)` 형태로 조건 검색과 페이징을 결합했다.
- Java 기본 자료형/참조 자료형 비교를 다시 언급하며 Entity/객체/배열이 참조 자료형이라는 점을 복습했다.
- ProductService와 ProductController에서 검색 DTO와 Pageable 요청을 받아 Repository 호출로 연결했다.
- MySQL 데이터 날짜를 조정하고 테스트 시나리오로 검색 결과를 확인했다.

## 실습 / 예제

검색 조건 객체와 Pageable을 Controller → Service → Repository로 전달하고, Page 결과를 React에서 사용할 수 있는 응답 구조로 반환하는 흐름을 확인했다.

## 헷갈린 점 / 질문

Pageable은 단순 페이지 번호만 담는 객체가 아니라 page, size, sort 정보를 함께 담는다. Specification은 동적 WHERE 조건을 조립하는 역할이다.

## 관련 페이지

- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]], [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]], [[concepts/pagination-search|페이징과 검색]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
