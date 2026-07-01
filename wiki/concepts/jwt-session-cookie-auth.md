---
title: JWT, 세션, 쿠키 인증
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [auth, backend, frontend, spring-boot, react]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
status: growing
confidence: medium
---

# JWT, 세션, 쿠키 인증

## 정의

인증은 사용자가 누구인지 확인하고 이후 요청에서도 그 상태를 유지하는 방식이다. 수업에서는 JWT, 세션, 쿠키를 로그인 구현 맥락에서 비교했다.

## 왜 중요한가

상품, 장바구니, 주문 기능은 사용자에 따라 결과가 달라진다. 따라서 로그인 상태를 프론트와 백엔드가 일관되게 다뤄야 한다.

## 핵심 설명

- 쿠키: 브라우저가 저장하고 요청 때 함께 보낼 수 있는 작은 데이터다.
- 세션: 서버가 로그인 상태를 저장하고 클라이언트는 세션 식별자를 주고받는 방식이다.
- JWT: 사용자 정보/권한 일부를 서명된 토큰으로 만들어 클라이언트가 보관하고 요청 때 전달하는 방식이다.
- Bearer 토큰: `Authorization: Bearer ...` 형태로 토큰을 전달하는 관례다.

## 예시

React가 로그인 성공 후 토큰을 저장하고, 이후 상품/장바구니 API 요청에 토큰을 붙이면 Spring Boot의 토큰 검증 로직이 사용자를 확인한다.

## 자주 헷갈리는 점

- JWT는 암호화가 아니라 서명 기반 검증이 핵심이다. 민감 정보를 그대로 넣으면 안 된다.
- 쿠키는 저장 위치이고, 세션/JWT는 인증 상태를 표현하는 방식이다.
- 프론트의 로그인 상태 표시와 백엔드의 인증 검증은 둘 다 필요하다.

## 관련 개념

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[entities/jwt|JWT]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
