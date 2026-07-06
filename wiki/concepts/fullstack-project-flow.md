---
title: 풀스택 프로젝트 흐름
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [spring-boot, react, frontend, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# 풀스택 프로젝트 흐름

## 정의

풀스택 프로젝트 흐름은 React 화면에서 사용자가 행동하면 Spring Boot API가 요청을 받고, Service/Repository가 업무 규칙과 DB 접근을 처리한 뒤, 응답 데이터를 다시 React state와 화면으로 연결하는 전체 순서다.

## 왜 중요한가

FrontEnd_BackEnd 19개 MD의 중심은 개별 문법보다 같은 흐름이 기능마다 반복된다는 점이다. Fruit 예제, 회원/JWT, 상품, 장바구니, 주문, 페이징/검색 모두 “화면 이벤트 → API 요청 → 백엔드 계층 → DB → 응답 렌더링”으로 설명할 수 있다.

## 핵심 흐름

1. React component가 사용자 입력, 클릭, 라우팅, `useEffect`로 API 요청을 만든다.
2. axios/customAxios가 Spring Boot API URL로 HTTP 요청을 보낸다.
3. Controller가 URL, method, request body/query/path variable을 받는다.
4. Service가 검증, 권한, 재고, 주문 상태 같은 업무 규칙을 처리한다.
5. Repository가 JPA를 통해 DB를 조회/저장한다.
6. DTO/Page/Entity 기반 응답이 React로 돌아오고, React state가 바뀌며 화면이 다시 그려진다.

## 수업에서의 전개

- 2026-03-30~04-01: 환경 세팅, Fruit Controller, React Router, TypeScript 타입.
- 2026-04-02~04-07: HomePage, Member, 로그인, JWT, SecurityContext.
- 2026-04-08~04-13: Product 도메인, 등록/삭제/상세/수정, `useEffect`.
- 2026-04-14~04-17: Cart/CartProduct, DTO, 수량 변경, 재고 검증.
- 2026-04-20~04-22: Order, JPQL, Pageable, Specification 검색.

## 자주 헷갈리는 점

React Router path와 Spring API URL은 같은 브라우저 주소처럼 보여도 책임이 다르다. React Router는 어떤 컴포넌트를 보여줄지, Spring API URL은 어떤 데이터를 처리할지 결정한다.

## 관련 개념

- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
