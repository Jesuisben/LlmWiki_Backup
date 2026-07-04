---
title: Spring Boot REST API
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [spring-boot, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf
status: growing
confidence: high
---

# Spring Boot REST API

## 정의

React 같은 클라이언트가 HTTP 요청으로 데이터를 주고받는 Spring Boot 백엔드 입구다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- Controller는 URL/HTTP 메서드에 맞는 요청을 받는다.
- DTO, path variable, query parameter로 요청 데이터를 해석한다.
- Service는 업무 규칙을 처리한다.
- Repository는 DB 접근을 담당한다.
- 응답은 HTML 문자열에서 객체/목록/페이지 데이터로 확장된다.

## 수업 예시

- [[summaries/2026-03-31-spring-boot-controller-html|2026-03-31 Spring Boot Controller와 HTML 응답]] — FruitHtmlController의 HTML 응답
- [[summaries/2026-04-07-member-api-string-token|2026-04-07 회원 API와 문자열/토큰 처리]] — 회원 API와 Bearer 토큰 처리
- [[summaries/2026-04-08-product-domain-oci|2026-04-08 상품 도메인과 OCI 소개]] — Category, Product 도메인과 상품 API 흐름
- [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13 상품 상세와 useEffect, 서비스 계층]] — ProductService와 상품 상세 조회
- [[summaries/2026-04-14-cart-service|2026-04-14 장바구니 Service와 DTO]] ~ [[summaries/2026-04-16-cart-quantity-stock|2026-04-16 장바구니 수량 변경과 재고 검증]] — CartController의 저장/목록/수량 변경
- [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22 ProductRepository와 Pageable 검색]] — ProductController의 페이징·검색 조건 처리

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]


## 교육자료 대조 보강

IT 관련 용어 교안 p.35~36은 REST를 URL(Resource)과 HTTP Method(GET/POST/PUT/DELETE) 중심으로 설명한다. SpringBoot 교안 p.57~60은 `@Controller`, `@RestController`, `@GetMapping`, `@PathVariable`의 차이를 보여준다. 따라서 이 페이지의 REST API 설명은 단순 “JSON 응답”이 아니라 HTTP Method와 Resource URL, Controller 매핑의 조합으로 읽어야 한다.

## Passwordless 연동으로 확장

2026-05-18~05-21 Passwordless 수업에서는 Spring Boot가 단순 CRUD API를 넘어 외부 인증 서버 REST API를 호출하는 client 역할도 맡았다. 이때 Controller는 React의 등록/로그인/해제 요청을 받고, Service는 X1280 API 호출과 응답 해석을 조립하며, DTO는 인증 서버 응답과 프론트 응답을 분리한다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
