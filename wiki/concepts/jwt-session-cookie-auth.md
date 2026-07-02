---
title: JWT, 세션, 쿠키 인증
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [auth, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---

# JWT, 세션, 쿠키 인증

## 정의

로그인한 사용자가 누구인지 확인하고 그 상태를 요청 사이에서 유지하는 방식들이다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- 쿠키는 브라우저가 저장하고 요청 때 서버로 보낼 수 있는 작은 데이터다.
- 세션은 서버가 로그인 상태를 저장하고 클라이언트는 보통 세션 ID만 들고 있는 방식이다.
- JWT는 인증 정보를 담은 서명 토큰이다.
- Bearer 토큰은 Authorization 헤더에 토큰을 실어 보내는 관례다.

## 수업 예시

- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 로그인, JWT, 세션과 쿠키]] — 쿠키/세션/JWT와 SPA/MPA 비교
- [[summaries/2026-04-07-member-api-string-token|2026-04-07 회원 API와 문자열/토큰 처리]] — 문자열 처리와 Bearer 토큰 처리

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[entities/jwt|JWT]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]


## 교육자료 대조 보강

IT 관련 용어 교안 p.48~49는 Cookie와 Session을, JWT 이론 p.2~4는 React SPA 구조와 JWT 사용 맥락을 설명한다. SpringBoot 교안 p.164~165의 `Authentication`/`SecurityContextHolder` 설명은 토큰 검증 후 서버 내부에서 현재 사용자를 어떻게 보관하는지 이해하는 근거가 된다. 자세한 필터 흐름은 [[concepts/spring-security-jwt-filter]]에 분리했다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
