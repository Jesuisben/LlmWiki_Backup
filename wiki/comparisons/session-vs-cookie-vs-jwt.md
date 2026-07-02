---
title: Session vs Cookie vs JWT
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [auth, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
status: growing
confidence: high
---

# Session vs Cookie vs JWT

## 비교 목적

로그인 상태 유지에서 쿠키, 세션, JWT가 각각 어떤 층위인지 구분한다.

## 한눈에 보기

| 항목 | Cookie | Session | JWT |
|---|---|---|---|
| 정체 | 브라우저 저장/전송 수단 | 서버가 로그인 상태를 저장하는 방식 | 서명된 토큰 형식 |
| 저장 위치 | 브라우저 | 서버 | 보통 클라이언트 저장 후 요청 첨부 |
| 서버 역할 | 쿠키 값을 읽음 | 세션 저장소 조회 | 토큰 검증 |

## 언제 무엇을 쓰는가

수업 예제에서 실제 기능을 추적할 때는 먼저 '어느 계층의 문제인가'를 본다. 화면 상태인지, 서버 인증인지, DB 저장인지에 따라 선택지가 달라진다.

## 헷갈리기 쉬운 포인트

쿠키는 저장/전송 수단, 세션은 서버 저장 방식, JWT는 토큰 형식이다. JWT를 쿠키에 저장할 수도 있으므로 단순 대립으로 외우면 안 된다.

## 관련 페이지

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[entities/jwt|JWT]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
