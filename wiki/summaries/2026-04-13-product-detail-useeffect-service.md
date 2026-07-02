---
title: 2026-04-13 상품 상세와 useEffect, 서비스 계층
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---
# 2026-04-13 상품 상세와 useEffect, 서비스 계층

## 한 줄 요약

상품 상세 조회를 위해 React `useEffect`와 Spring `ProductService`/`ProductController` 흐름을 연결했다.

## 커리큘럼 위치와 흐름

상품 등록/삭제 이후 상세 조회와 수정 흐름으로 확장했다. 프론트는 화면이 열릴 때 데이터를 가져와야 하고, 백엔드는 Controller-Service 계층으로 상품 데이터를 조회·수정해야 한다.

## 배운 내용

- React 교안 p.87은 `useEffect(<function>, <dependency>)` 구조와 props/state 의존성 개념을 설명한다.
- `ProductService`는 상품 조회/수정 업무 로직을 담당하고, Controller는 HTTP 요청을 받아 서비스로 위임한다.
- `put` 요청은 기존 상품 데이터를 수정하는 REST 흐름과 연결된다.

## 핵심 실습 / 예제

- 상품 상세 페이지가 mount되거나 URL 파라미터가 바뀔 때 `useEffect`로 API를 호출해 상세 데이터를 가져온다.
- Service 계층은 Controller를 가볍게 유지하고, Repository 호출과 예외 처리를 모으는 위치다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- `useEffect`의 dependency 배열을 비워둘지, 상품 ID를 넣을지에 따라 호출 시점이 달라진다.
- Controller에 모든 로직을 쓰면 작은 예제는 동작하지만 기능이 커질수록 유지보수가 어렵다.
- PUT/PATCH/POST의 역할 차이를 CRUD 관점에서 구분해야 한다.

## 관련 페이지

- [[concepts/react-useeffect-data-fetching]]
- [[concepts/product-domain-flow]]
- [[comparisons/controller-service-repository]]
- [[concepts/spring-boot-rest-api]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
