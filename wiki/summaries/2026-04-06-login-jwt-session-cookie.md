---
title: 2026-04-06 로그인, JWT, 세션과 쿠키
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
status: growing
confidence: high
---

# 2026-04-06 로그인, JWT, 세션과 쿠키

## 한 줄 요약

로그인 구현을 시작하며 쿠키·세션·JWT·SPA/MPA·Stateful/Stateless를 비교하고 React axiosInstance/localStorage 기반 토큰 처리로 넘어갔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

React SPA는 화면 전환마다 서버가 HTML을 새로 만들어 주는 구조가 아니므로, 로그인 상태를 API 요청 Header의 토큰으로 전달하는 방식이 중요해진다.

## 핵심 개념

- 쿠키는 브라우저 저장소, 세션은 서버의 로그인 상태 저장, JWT는 서명된 토큰 기반 인증 방식으로 구분했다.
- MPA와 SPA, Session 인증 방식과 JWT 인증 방식, Stateful과 Stateless를 JWT 이론 자료 기준으로 비교했다.
- React `axiosInstance.tsx`, `User.ts`, localStorage 확인 흐름을 통해 토큰 저장과 API 요청 준비를 했다.
- MIME type과 HTTP 전송 데이터 형식을 함께 확인해 API 통신의 배경을 보강했다.

## 실습 / 예제

로그인 요청 후 받은 JWT를 localStorage에 저장하고, 이후 axiosInstance가 Authorization Header에 Bearer 토큰을 붙이는 흐름을 준비했다.

## 헷갈린 점 / 질문

JWT는 암호화된 비밀 상자가 아니라 서명으로 위변조를 확인하는 토큰이다. 쿠키는 저장/전송 수단이고, 세션/JWT는 로그인 상태 유지 전략이다.

## 관련 페이지

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]], [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]], [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]], [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
