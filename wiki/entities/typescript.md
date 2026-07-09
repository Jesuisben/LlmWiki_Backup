---
title: TypeScript
created: 2026-07-02
updated: 2026-07-09
type: entity
tags: [typescript, react, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# TypeScript

## 무엇인가

JavaScript에 타입을 더해 변수, 객체, 함수 인자, 컴포넌트 props의 모양을 미리 적는 언어다.

## 이 위키에서의 맥락

- [[summaries/2026-04-01-react-router-spring-boot|2026-04-01 React 라우팅과 Spring Boot 연동 흐름]]에서 types 폴더와 Fruit.ts 인터페이스를 만들며 등장했다.
- [[summaries/2026-04-15-cart-list-selection-typescript|2026-04-15 장바구니 목록과 TypeScript props]]에서는 CartProduct.ts, AppProps, props 구조 분해와 연결됐다.
- 상품/장바구니/주문 화면의 API 데이터 구조를 표현하는 데 쓰였고, [[summaries/2026-04-21-product-pagination-search-react|2026-04-21 상품 목록 페이징과 필드 검색]]에서는 페이징 파라미터와 화면 상태 관리로 이어졌다.

## 핵심 기능 / 특징

- interface/type으로 데이터 구조 정의
- props 타입 지정으로 컴포넌트 사용 실수 감소
- API 응답 필드 자동완성·검사
- Java의 자료형 학습과 연결

## 헷갈리기 쉬운 점

TypeScript interface는 DB 테이블이 아니다. 프론트 코드에서 API 데이터 모양을 안전하게 쓰기 위한 약속이다.

## 관련 개념

- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[entities/react|React]]

## 학습 이력

이 페이지는 단순 정의가 아니라, 수업에서 이 기술이 처음 등장한 맥락과 이후 Java/Oracle/UI&UX/Spring/React 프로젝트 흐름으로 확장된 위치를 추적하기 위한 엔티티 페이지다.

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
