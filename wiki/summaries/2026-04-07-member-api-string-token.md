---
title: 2026-04-07 회원 API와 문자열/토큰 처리
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
status: growing
confidence: high
---

# 2026-04-07 회원 API와 문자열/토큰 처리

## 한 줄 요약

Java String 메서드로 Bearer 토큰 문자열 처리를 익히고, JwtAuthenticationFilter·SecurityConfig·MemberController로 로그인 API 보안 흐름을 구성했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

JWT 인증은 “문자열 하나를 받는다”에서 끝나지 않고, Header 접두어 확인, 토큰 추출, 검증, SecurityContext 등록, Controller 응답까지 이어진다.

## 핵심 개념

- `startsWith`, `substring`, `replace`, `contains` 등 String 메서드를 Bearer 토큰 처리 예제로 복습했다.
- `JwtAuthenticationFilter`에서 Authorization Header를 읽고 토큰을 검증하는 흐름을 작성했다.
- SecurityContextHolder와 Authentication 인터페이스를 통해 인증 객체가 Spring Security 안에서 어떻게 쓰이는지 확인했다.
- WebConfig/CorsConfig/SecurityConfig/MemberController를 연결해 로그인 테스트를 수행했다.

## 실습 / 예제

`Bearer hello world` 같은 문자열로 접두어 제거와 토큰 추출을 실습한 뒤 실제 JWT Filter 코드에 같은 사고방식을 적용했다.

## 헷갈린 점 / 질문

Bearer는 토큰 자체가 아니라 Header 값 앞에 붙는 인증 방식 표기다. 문자열 처리 실수가 나면 토큰 검증 이전에 인증 흐름이 깨진다.

## 관련 페이지

- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]], [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]], [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
