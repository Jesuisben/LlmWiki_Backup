---
title: FrontEnd_BackEnd 총정리
created: 2026-07-03
updated: 2026-07-09
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# FrontEnd_BackEnd 총정리

## 한 줄 요약

4과목은 개발 환경 세팅에서 시작해 Spring Boot REST API와 React/TypeScript 화면을 연결하고, JWT 로그인·상품·장바구니·주문·페이징/검색까지 쇼핑몰 기능 흐름을 완성하는 과정이다.

## 전체 흐름

1. [[summaries/2026-03-30-fullstack-environment-setup|03-30]]: Spring Boot, React, Node.js, VS Code, MySQL 준비.
2. [[summaries/2026-03-31-spring-boot-controller-html|03-31]] ~ [[summaries/2026-04-01-react-router-spring-boot|04-01]]: Controller/REST API/JSON, React Router, axios, CORS.
3. [[summaries/2026-04-02-react-bootstrap-homepage|04-02]] ~ [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]]: HomePage, Member/JPA, Signup, Repository.
4. [[summaries/2026-04-06-login-jwt-session-cookie|04-06]] ~ [[summaries/2026-04-07-member-api-string-token|04-07]]: 쿠키·세션·JWT, Bearer 토큰, Spring Security Filter.
5. [[summaries/2026-04-08-product-domain-oci|04-08]] ~ [[summaries/2026-04-13-product-detail-useeffect-service|04-13]]: Category/Product, 상품 등록·삭제·수정·상세, useEffect.
6. [[summaries/2026-04-14-cart-service|04-14]] ~ [[summaries/2026-04-17-cart-total-array-some|04-17]]: Cart/CartProduct, DTO, 선택/수량/삭제, 주문 생성.
7. [[summaries/2026-04-20-order-list-scenario|04-20]] ~ [[summaries/2026-04-22-product-repository-pageable-search|04-22]]: 주문 상태 변경, 대표 상품, Pageable/Specification 검색.

## 기능 흐름으로 다시 보기

- 화면: React page/component, Router, MenuItems, Bootstrap, state/props/useEffect.
- API: Spring Controller가 URL과 HTTP method를 받고 Service로 업무 로직을 넘긴다.
- 데이터: Entity/Repository/JPA/MySQL이 실제 저장과 조회를 담당한다.
- 인증: JWT Bearer 토큰을 React localStorage/axiosInstance와 Spring Security Filter가 함께 처리한다.
- 도메인: Product가 중심이고 CartProduct와 OrderProduct가 상품을 참조하며 장바구니·주문으로 확장된다.

## 특히 헷갈리기 쉬운 연결

- React Router 주소와 Spring API 주소는 다르다. 화면 이동은 Router, 데이터 요청은 axios/API URL이다.
- Entity는 DB와 가까운 객체이고 DTO는 화면/API 전달용 모양이다.
- 장바구니의 CartProduct와 주문의 OrderProduct는 비슷해 보이지만 생명주기가 다르다.
- Pageable 검색은 React state, API parameter, Spring Pageable/Specification, Repository 조회가 모두 맞아야 동작한다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[concepts/pagination-search|페이징과 검색]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]], [[comparisons/entity-vs-dto|Entity vs DTO]], [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개
