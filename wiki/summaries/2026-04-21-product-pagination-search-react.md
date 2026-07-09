---
title: 2026-04-21 상품 목록 페이징과 필드 검색
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: high
---

# 2026-04-21 상품 목록 페이징과 필드 검색

## 한 줄 요약

ProductList에서 pageNumber/pageSize와 검색 조건 state를 추가하고, Spring Pageable 응답의 `content`와 page 정보를 React Paging/FieldSearch 컴포넌트와 연결했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

상품 수가 많아지면 모든 데이터를 한 번에 내려받기 어렵다. 프론트는 페이지/검색 조건을 보내고 백엔드는 조건에 맞는 일부 데이터와 페이지 정보를 반환해야 한다.

## 핵심 개념

- ProductList의 `useEffect` 의존성에 paging.pageNumber를 포함해 페이지 변경 시 API를 다시 호출했다.
- 응답 구조를 `response.data`에서 `response.data.content` 중심으로 바꿔 Page 응답을 처리했다.
- SearchCondition.ts와 FieldSearch.tsx로 검색 조건 타입과 입력 컴포넌트를 분리했다.
- Querydsl 관련 API와 CSR/SSR 개념을 함께 언급하며 화면 렌더링 방식을 비교했다.

## 실습 / 예제

React에서 page/search parameter를 요청으로 보내고, Spring이 Page 결과를 돌려주면 `products`와 `paging` state를 함께 갱신하는 흐름을 실습했다.

## 헷갈린 점 / 질문

`?` optional chaining과 `??` nullish coalescing은 모두 안전한 기본값 처리에 쓰이지만 역할이 다르다. 페이징 값이 없을 때 화면이 깨지지 않게 하는 데 중요하다.

## 관련 페이지

- [[concepts/pagination-search|페이징과 검색]], [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]], [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
