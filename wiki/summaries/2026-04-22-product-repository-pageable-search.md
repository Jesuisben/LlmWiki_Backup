---
title: 2026-04-22 ProductRepository와 Pageable 검색
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# 2026-04-22 ProductRepository와 Pageable 검색

## 한 줄 요약

Spring Data JPA Repository에서 Specification과 Pageable을 받아 상품 목록을 검색하고 정렬/페이징하는 백엔드 흐름을 마무리했다.

## 배운 내용

- 주제: 백엔드 페이징/검색
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

전날 React가 검색·페이지 요청을 보내는 구조를 만들었다면 이날은 Spring Repository와 Service가 그 요청을 실제 DB 조회로 바꾸는 역할을 배웠다.

## 핵심 개념

ProductRepository는 `Page<Product> findAll(Specification<Product> spec, Pageable pageable)` 형태로 검색 조건과 페이징 객체를 함께 받는다. Service에서는 searchMode에 따라 Specification 조건을 만들고 Controller는 page/size/search parameter를 받아 Page 응답을 반환한다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

Java 기본 자료형은 `==` 비교가 가능하지만 String 같은 참조 자료형은 보통 `equals()`로 값 비교를 한다. `"name".equals(searchMode)`처럼 쓰면 null 안전성도 좋아진다.

## 관련 페이지

- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]], [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]], [[concepts/pagination-search|페이징과 검색]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
