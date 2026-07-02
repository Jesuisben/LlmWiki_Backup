---
title: React와 TypeScript 기본
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [react, typescript, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png
status: growing
confidence: high
---

# React와 TypeScript 기본

## 정의

React는 UI를 컴포넌트로 만들고, TypeScript는 데이터와 props의 타입을 명확히 적게 해준다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- 컴포넌트는 화면 조각을 함수처럼 분리한다.
- props는 부모가 자식에게 넘기는 입력값이다.
- state는 화면 안에서 바뀌는 값이다.
- useEffect는 렌더링 시점/API 호출 같은 부수효과를 다룬다.
- interface/type은 Fruit, CartProduct, AppProps 같은 데이터 구조를 정의한다.

## 수업 예시

- [[summaries/2026-04-01-react-router-spring-boot|2026-04-01 React 라우팅과 Spring Boot 연동 흐름]] — App.tsx, MenuItems.tsx, types/Fruit.ts
- [[summaries/2026-04-02-react-bootstrap-homepage|2026-04-02 React Bootstrap과 HomePage 구성]] — Carousel, Card, HomePage 구성
- [[summaries/2026-04-03-spring-member-seed-react-comments|2026-04-03 Member 데이터 준비와 React JSX 기초]] — JSX 주석과 편집 흐름
- [[summaries/2026-04-09-product-delete-routing-jsx-table|2026-04-09 상품 삭제, 라우팅, JSX와 표]] — 라우팅과 JSX 내부 JavaScript 표현
- [[summaries/2026-04-10-react-event-spread-product-form|2026-04-10 React 이벤트 객체와 전개 연산자]] — 이벤트 객체와 전개 연산자를 이용한 상품 입력 폼
- [[summaries/2026-04-15-cart-list-selection-typescript|2026-04-15 장바구니 목록과 TypeScript props]] — 장바구니 목록의 props 구조 분해와 AppProps
- [[summaries/2026-04-21-product-pagination-search-react|2026-04-21 상품 목록 페이징과 필드 검색]] — useEffect 의존성과 페이징 파라미터

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[entities/react|React]]
- [[entities/typescript|TypeScript]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]


## 교육자료 대조 보강

React 교안 p.41, p.72~73, p.87을 대조해 전개 연산자, 이벤트 객체, `useEffect`를 각각 폼 상태 관리·이벤트 처리·API 데이터 요청의 핵심 도구로 연결했다. 라우터 설명 이미지는 React Router가 사용자를 알맞은 화면 컴포넌트로 안내하는 역할임을 보여주며, 이는 [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]와 직접 연결된다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
