---
title: MPA vs SPA
created: 2026-07-02
updated: 2026-07-09
type: comparison
tags: [frontend, react, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf
status: growing
confidence: high
---
# MPA vs SPA

## 비교 목적

JWT 이론 자료는 React 기반 SPA 구조를 설명하면서 MPA와 비교한다. 이 구분은 왜 React 프로젝트에서 서버가 HTML 페이지를 계속 내려주기보다 API와 JSON을 제공하고, 로그인 상태 전달에 JWT를 자주 쓰는지 이해하는 데 중요하다.

## 한눈에 보기

| 항목 | MPA | SPA |
|---|---|---|
| 화면 전환 | 서버가 새 HTML 페이지를 내려주는 방식 | 처음 받은 앱 안에서 React가 화면을 바꿈 |
| 대표 예 | JSP + Spring MVC | React, Vue, Angular |
| 서버 역할 | View와 데이터 처리 모두 담당하는 경우가 많음 | API/JSON 제공 역할이 커짐 |
| 인증 흐름 | 세션 기반 구성이 자연스러움 | JWT/Bearer 토큰 기반 API 인증을 많이 사용 |

## 언제 무엇을 쓰는가

- 전통적인 서버 렌더링 중심 서비스는 MPA 구조가 이해하기 쉽다.
- 사용자 경험이 앱처럼 이어지고, 프론트/백엔드가 분리된 프로젝트는 SPA 구조가 잘 맞는다.
- 이 수업의 쇼핑몰 프로젝트는 React 화면과 Spring Boot API가 분리되므로 SPA 관점으로 이해하는 것이 좋다.

## 헷갈리기 쉬운 포인트

- SPA라고 해서 서버가 없는 것이 아니다. 서버는 HTML 대신 API 데이터를 주로 제공한다.
- JWT는 SPA 전용은 아니지만, 분리된 API 서버와 함께 자주 쓰인다.
- React Router의 화면 전환은 서버 페이지 이동과 다르다.

## 관련 페이지

- [[summaries/2026-04-06-login-jwt-session-cookie]]
- [[concepts/jwt-session-cookie-auth]]
- [[comparisons/session-vs-cookie-vs-jwt]]
- [[concepts/frontend-backend-architecture]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf`
