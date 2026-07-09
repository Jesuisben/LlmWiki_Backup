---
title: Session vs Cookie vs JWT
created: 2026-07-02
updated: 2026-07-09
type: comparison
tags: [auth, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf
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


## 교육자료 대조 보강

Cookie는 브라우저/PC에 저장되는 값, Session은 서버가 상태를 보관하고 클라이언트가 식별자를 들고 다니는 방식, JWT는 서명된 토큰 형식이다. JWT 이론 자료의 SPA/MPA 비교를 반영해, React SPA에서는 서버가 HTML 페이지보다 API 데이터를 제공하고 인증 정보는 Bearer 토큰으로 전달되는 흐름을 함께 보아야 한다. 관련 비교는 [[comparisons/mpa-vs-spa]]로 분리했다.

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
