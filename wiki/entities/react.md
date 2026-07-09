---
title: React
created: 2026-07-02
updated: 2026-07-09
type: entity
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: high
---

# React

## 무엇인가

화면을 컴포넌트 단위로 나누고 state/props 변화에 따라 UI를 다시 그리는 프론트엔드 라이브러리다.

## 이 위키에서의 맥락

- [[summaries/2026-04-01-react-router-spring-boot|2026-04-01 React 라우팅과 Spring Boot 연동 흐름]]에서 App.tsx, MenuItems, Router, TypeScript 인터페이스로 시작했다.
- [[summaries/2026-04-02-react-bootstrap-homepage|2026-04-02 React Bootstrap과 HomePage 구성]]에서는 React Bootstrap으로 홈 화면을 구성했다.
- 이후 로그인, 상품, 장바구니, 주문, 페이징 화면을 만들며 Spring Boot API와 연결됐다.

## 핵심 기능 / 특징

- 컴포넌트 기반 화면 분리
- props/state를 통한 데이터 전달·상태 관리
- useEffect로 API 호출 시점 관리
- Router로 화면 주소 관리

## 헷갈리기 쉬운 점

React Router 주소와 Spring API 주소는 모두 URL처럼 보이지만 역할이 다르다.

## 관련 개념

- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[entities/typescript|TypeScript]]

## 학습 이력

이 페이지는 단순 정의가 아니라, 수업에서 이 기술이 처음 등장한 맥락과 이후 Java/Oracle/UI&UX/Spring/React 프로젝트 흐름으로 확장된 위치를 추적하기 위한 엔티티 페이지다.

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
