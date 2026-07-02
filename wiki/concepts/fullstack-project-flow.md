---
title: 풀스택 프로젝트 흐름
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [project, frontend, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---

# 풀스택 프로젝트 흐름

## 정의

React 화면, Spring Boot API, Service/Repository, DB 테이블이 기능 단위로 이어지는 흐름이다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- 사용자가 React 화면에서 입력/클릭한다.
- React가 상태와 입력값을 모아 API를 호출한다.
- Controller가 요청을 받고 Service를 호출한다.
- Service가 업무 규칙을 처리한다.
- Repository가 DB를 조회/저장한다.
- 응답이 React로 돌아와 화면이 다시 렌더링된다.

## 수업 예시

- [[summaries/2026-03-30-fullstack-environment-setup|2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환]] — [[entities/mysql|MySQL]], [[entities/node-js|Node.js]], [[entities/visual-studio-code|Visual Studio Code]], Spring Boot, React 준비
- [[summaries/2026-03-31-spring-boot-controller-html|2026-03-31 Spring Boot Controller와 HTML 응답]] — Fruit Controller와 HTML 응답
- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 로그인, JWT, 세션과 쿠키]] ~ [[summaries/2026-04-07-member-api-string-token|2026-04-07 회원 API와 문자열/토큰 처리]] — 로그인/JWT/Bearer 토큰
- [[summaries/2026-04-08-product-domain-oci|2026-04-08 상품 도메인과 OCI 소개]] ~ [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13 상품 상세와 useEffect, 서비스 계층]] — 상품 도메인, 삭제, 입력 폼, 상세 조회
- [[summaries/2026-04-14-cart-service|2026-04-14 장바구니 Service와 DTO]] ~ [[summaries/2026-04-17-cart-total-array-some|2026-04-17 장바구니 합계와 Array some]] — 장바구니 저장·목록·수량·재고
- [[summaries/2026-04-20-order-list-scenario|2026-04-20 주문 목록과 테스트 시나리오]] 이후 — 주문·페이징·검색

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]


## 교육자료 대조 보강

SpringBoot 교안 p.55~60의 구성도는 `Controller → Service → Repository → Database` 흐름과 `Entity`, `application.properties`, `pom.xml`의 위치를 한 장으로 보여준다. 이번 백필에서는 이 그림을 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]와 연결해, React 화면이 View 역할의 상당 부분을 맡고 Spring Boot가 REST API와 업무 로직을 담당하는 흐름으로 정리했다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
