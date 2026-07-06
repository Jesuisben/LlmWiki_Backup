---
title: 2026-04-07 회원 API와 문자열/토큰 처리
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
status: growing
confidence: high
---

# 2026-04-07 회원 API와 문자열/토큰 처리

## 한 줄 요약

Java String 메서드로 Bearer 토큰 문자열을 다루고 JWT Filter와 SecurityContextHolder를 통해 인증 정보를 Spring Security에 저장하는 흐름을 학습했다.

## 배운 내용

- 주제: JWT 필터와 공통 인증 정보
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

로그인 후 모든 API 요청에서 토큰을 읽고 사용자 인증 상태를 복원해야 하므로 문자열 처리와 SecurityContext 구조가 실전 기능으로 연결됐다.

## 핵심 개념

`startsWith`, `substring`, `toLowerCase`, `contains` 같은 String 메서드로 Authorization Header의 Bearer 형식을 해석했다. JwtAuthenticationFilter는 토큰을 검증하고 Authentication 객체를 만들어 SecurityContextHolder에 넣는다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

Spring Security의 User는 UserDetails 구현체와 헷갈릴 수 있다. SecurityContextHolder는 현재 요청을 처리하는 동안 인증 정보를 꺼내 볼 수 있는 저장소로 이해하면 좋다.

## 관련 페이지

- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]], [[entities/jwt|JWT]], [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
