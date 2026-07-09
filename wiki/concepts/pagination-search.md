---
title: 페이징과 검색
created: 2026-07-06
updated: 2026-07-09
type: concept
tags: [spring-boot, react, frontend, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# 페이징과 검색

## 정의

페이징과 검색은 상품 목록을 한 번에 모두 가져오지 않고 page/size/searchMode/searchKeyword 같은 조건으로 나누어 조회하는 방식이다.

## 왜 중요한가

데이터가 많아질수록 전체 목록을 매번 가져오는 방식은 느리고 비효율적이다. React 화면은 현재 페이지와 검색어를 state로 가지고, Spring Boot는 Pageable과 Specification으로 DB 조회를 제한한다.

## 핵심 설명

- React: pageNumber, pageSize, 검색 mode/keyword를 state로 관리한다.
- API 요청: query parameter로 page, size, search 조건을 보낸다.
- Spring Controller: 요청 parameter를 받아 Service에 전달한다.
- Service/Repository: Specification으로 검색 조건을 만들고 Pageable로 정렬·페이지 크기를 적용한다.
- 응답: Page 객체의 `content`, `number`, `size`, `totalPages` 등을 React가 화면에 반영한다.

## 수업 예시

2026-04-21에는 ProductList에서 `response.data.content`, `pageable?.pageNumber ?? 0` 같은 프론트 처리와 Paging 컴포넌트를 다뤘다. 2026-04-22에는 ProductRepository의 `findAll(Specification<Product> spec, Pageable pageable)`와 Service 검색 조건 생성을 배웠다.

## 자주 헷갈리는 점

`pageable?.pageNumber ?? 0`에서 `?.`는 값이 없을 때 안전하게 접근하는 문법이고, `??`는 null/undefined일 때 기본값을 쓰는 문법이다. 검색 조건 비교에서는 `"name".equals(searchMode)`처럼 쓰면 null에 더 안전하다.

## 관련 개념

- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
