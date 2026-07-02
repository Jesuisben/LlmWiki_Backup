---
title: JWT
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [auth, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
status: growing
confidence: high
---

# JWT

## 무엇인가

로그인한 사용자의 인증 정보를 서명된 토큰 형태로 전달하는 방식이다.

## 이 위키에서의 맥락

- 2026-04-06 로그인 수업에서 쿠키, 세션, SPA/MPA 비교와 함께 등장했다.
- 2026-04-07에는 문자열 처리와 Bearer 토큰 처리 흐름으로 이어졌다.

## 핵심 기능 / 특징

- 로그인 성공 후 서버가 토큰 발급
- 프론트가 토큰을 저장했다가 API 요청에 첨부
- Authorization: Bearer ... 형태로 전달
- 서버는 토큰을 검증해 사용자를 식별

## 헷갈리기 쉬운 점

JWT는 쿠키나 세션과 같은 저장소가 아니라 인증 정보를 담는 토큰 형식이다.

## 관련 개념

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 학습 이력

이 페이지는 단순 정의가 아니라, 수업에서 이 기술이 처음 등장한 맥락과 이후 Java/Oracle/UI&UX/Spring/React 프로젝트 흐름으로 확장된 위치를 추적하기 위한 엔티티 페이지다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
