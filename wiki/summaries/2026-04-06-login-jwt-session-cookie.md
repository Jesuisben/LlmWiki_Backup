---
title: 2026-04-06 로그인, JWT, 세션과 쿠키
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [auth, spring-boot, react, typescript, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
status: growing
confidence: medium
---

# 2026-04-06 로그인, JWT, 세션과 쿠키

## 한 줄 요약

로그인 구현을 시작하며 JWT 토큰, 세션, 쿠키, DTO, React 로그인 흐름의 차이를 학습했다.

## 배운 내용

- 로그인 보안 개념
- JWT 토큰
- 세션과 쿠키
- DTO 사용
- React 로그인 상태 관리

## 원본에서 확인한 세부 주제

- 프로젝트 정보
- 새로운 파일 다운 받기
- 로그인 관련 개념
- 쿠키(Cookie) (IT 관련 용어.pdf (P.48))
- 세션(Session) (IT 관련 용어.pdf (P.49))
- 쿠키 / 세션 정리
- JWT - SPA구조 - MPA와 SPA 비교 (JWT(이론)(P.2))
- JWT - SPA구조 (JWT(이론)(P.2))

## 핵심 개념

- 백엔드의 Controller/Service/Repository/DTO/Entity 역할을 나누어 생각한다.
- 프론트엔드는 React 컴포넌트, props, state, Hook, 라우팅으로 화면과 상태를 관리한다.
- 실습 기능은 단독 문법보다 로그인, 상품, 장바구니, 주문처럼 이어지는 업무 흐름 안에서 이해해야 한다.

## 헷갈린 점 / 질문

- 같은 데이터가 백엔드 Entity, DTO, 프론트 TypeScript 타입에서 각각 어떻게 표현되는지 구분할 필요가 있다.
- React 라우팅 주소와 Spring Boot API 주소는 역할이 다르므로 혼동하지 않아야 한다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
