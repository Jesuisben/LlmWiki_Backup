---
title: 2026-04-21 상품 목록 페이징과 필드 검색
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf
status: growing
confidence: high
---
# 2026-04-21 상품 목록 페이징과 필드 검색

## 한 줄 요약

React 상품 목록에서 페이지 번호와 검색 조건을 상태로 관리하고, Paging 컴포넌트와 검색 UI를 만들었다.

## 커리큘럼 위치와 흐름

상품/장바구니/주문 기능 이후 목록 데이터가 많아지는 상황을 다뤘다. 모든 상품을 한 번에 가져오지 않고 페이지 단위로 요청하며, 검색 조건을 URL/API 파라미터로 전달하는 구조로 확장했다.

## 배운 내용

- `ProductList.tsx`에서 `pageNumber`, 검색 필드, 검색어 상태를 관리했다.
- 필드 검색 기능 PDF는 `totalElements`, `pageSize`, `totalPages`, `pageNumber`, `pageCount`, `beginPage`, `endPage`, `pagingStatus` 같은 페이징 계산 요소를 제시한다.
- 검색 조건은 이름/설명/카테고리 등 필드에 따라 다르게 적용될 수 있다.

## 핵심 실습 / 예제

- React는 현재 페이지와 검색 조건을 state로 들고 있다가 API 요청 파라미터로 보낸다.
- Paging 컴포넌트는 전체 페이지 수와 현재 페이지를 기준으로 이동 가능한 버튼을 렌더링한다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- 프론트의 pageNumber와 백엔드 Pageable의 page index 기준이 0부터인지 1부터인지 확인해야 한다.
- 검색 버튼을 눌렀을 때는 보통 1페이지로 돌아가야 사용자가 결과를 자연스럽게 볼 수 있다.
- 검색 조건 state와 API 요청 파라미터 이름이 어긋나면 화면은 정상이어도 서버 검색이 되지 않는다.

## 관련 페이지

- [[concepts/pagination-search]]
- [[concepts/spring-product-search-flow]]
- [[concepts/spring-data-jpa-specification-pageable]]
- [[entities/react]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf`
