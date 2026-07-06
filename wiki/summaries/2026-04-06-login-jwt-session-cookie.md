---
title: 2026-04-06 로그인, JWT, 세션과 쿠키
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, auth]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
status: growing
confidence: high
---

# 2026-04-06 로그인, JWT, 세션과 쿠키

## 한 줄 요약

로그인 구현을 시작하며 쿠키·세션·JWT의 역할 차이를 배우고 React axios 401 처리와 사용자 role 기반 화면 분기를 다뤘다.

## 배운 내용

- 주제: 인증 방식 전환
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

서버 렌더링 중심에서는 세션을 많이 쓰지만 React SPA와 API 서버 구조에서는 JWT Bearer 토큰을 요청마다 보내는 방식이 중요해졌다.

## 핵심 개념

쿠키는 브라우저가 보관하는 작은 데이터, 세션은 서버가 로그인 상태를 기억하는 구조, JWT는 서명된 토큰을 클라이언트가 보관하고 API 요청 Header에 담아 보내는 구조로 정리했다. React에서는 401 응답 시 토큰을 삭제하고 로그인 화면으로 보내는 axios interceptor 흐름을 확인했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

JWT는 암호화 자체가 아니라 서명으로 위변조를 검증하는 토큰이다. 쿠키/세션/JWT는 저장 위치와 상태 유지 방식이 다른 층위다.

## 관련 페이지

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]], [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]], [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
