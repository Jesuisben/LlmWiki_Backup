---
title: 페이징과 검색
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [spring-boot, react, typescript, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md
status: growing
confidence: medium
---

# 페이징과 검색

## 정의

페이징은 많은 데이터를 일정한 크기의 페이지로 나누어 조회하는 방식이고, 검색은 조건에 맞는 데이터만 걸러 조회하는 방식이다.

## 왜 중요한가

상품 목록처럼 데이터가 많아지는 화면에서는 모든 데이터를 한 번에 가져오면 느리고 불편하다. 페이지 번호, 정렬, 검색 조건을 함께 다뤄야 한다.

## 핵심 설명

- React는 현재 페이지 번호와 검색 조건을 state로 관리한다.
- `useEffect`는 페이지나 검색 조건이 바뀔 때 API를 다시 호출한다.
- Spring Boot는 Pageable과 검색 파라미터를 받아 Repository 조회에 반영한다.
- 응답에는 목록뿐 아니라 전체 페이지 수 같은 페이징 정보도 필요하다.

## 예시

`ProductList.tsx`가 `pageNumber`를 요청 파라미터로 보내고, 백엔드는 `Pageable` 객체를 통해 정렬과 페이지 크기를 처리한다.

## 자주 헷갈리는 점

- 페이지 번호는 보통 화면 표시용 1부터 시작할 수 있지만, 내부 API/Pageable은 0부터 시작할 수 있다.
- 검색 조건이 바뀌면 현재 페이지를 첫 페이지로 되돌리는 처리가 필요할 수 있다.

## 관련 개념

- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
- `raw/Study/10. Python/2026.07.01(수)/2026.07.01(수).md`
