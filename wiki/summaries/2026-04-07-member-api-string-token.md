---
title: 2026-04-07 회원 API와 문자열/토큰 처리
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [java, spring-boot, auth, backend, react]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
status: growing
confidence: medium
---

# 2026-04-07 회원 API와 문자열/토큰 처리

## 한 줄 요약

회원 기능 구현 과정에서 Java String 메서드, Bearer 토큰 처리, Spring Controller/DTO 흐름을 다뤘다.

## 배운 내용

- String 클래스 주요 메서드
- Bearer 토큰 문자열 처리
- 회원 DTO와 Controller
- 쿠키/토큰 인증 흐름
- React와 회원 API 연결

## 원본에서 확인한 세부 주제

- String 클래스 (04.회원.txt) (중요!!!!!!!!!!)
- JWT 필터 클래스 신규 작성 : JwtAuthenticationFilter(config 패키지) (04.회원.txt)
- 엔터티 공통 속성 공통화 - SecurityContextHolder (SpringBoot 교안 PDF (P.165))
- 엔터티 공통 속성 공통화 - Authentication 인터페이스 (SpringBoot 교안 PDF (P.164))
- WebConfig 클래스 (04.회원.txt)
- config\CorsConfig 클래스 신규 작성 (04.회원.txt)
- 로그인/로그 아웃 구현하기 (SpringBoot 교안 PDF (P.148~150))
- 사용자 상세 정보 서비스 (04.회원.txt)

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
