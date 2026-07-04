---
title: Passwordless 로그인 vs 비밀번호 로그인
created: 2026-07-03
updated: 2026-07-03
type: comparison
tags: [auth, project, spring-boot]
sources:
  - raw/Study/8. Passwordless/2026.05.14(목)/2026.05.14(목).md
  - raw/Study/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/Study/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/Study/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless 로그인 vs 비밀번호 로그인

## 비교 목적

중간 프로젝트에서 기존 아이디/비밀번호 로그인에 Passwordless X1280을 추가할 때, 두 방식의 책임·위험·프론트/백엔드 구현 포인트를 구분하기 위해 비교한다.

## 한눈에 보기

| 항목 | 비밀번호 로그인 | Passwordless X1280 로그인 |
|---|---|---|
| 사용자가 입력하는 것 | 아이디, 비밀번호 | 아이디, QR 등록 또는 앱 승인 |
| 주요 검증 위치 | 프로젝트 서버/DB의 비밀번호 검증 | X1280 인증 서버와 모바일 앱 승인 결과 |
| 공격 표면 | 피싱, 키로깅, 비밀번호 재사용 | 연동값 노출, 승인 상태 처리 오류, 앱/서버 연결 실패 |
| 프론트 상태 | 성공/실패 중심 | 등록 필요, QR 표시, 승인 대기, 승인 성공/거절/timeout, 해제 |
| 백엔드 관심사 | 비밀번호 hash 검증, 세션/JWT 발급 | REST client, DTO, serverKey 관리, 승인 결과 확인, 기존 로그인 상태 연결 |
| 사용자 경험 | 기억한 비밀번호 입력 | 모바일 앱에서 요청 확인 후 승인 |
| 프로젝트 연결 | 기존 회원 로그인 기본 흐름 | [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]으로 확장 |

## 언제 무엇을 쓰는가

- 비밀번호 로그인은 기본 회원 기능과 JWT/세션 흐름을 학습하기 좋다.
- Passwordless는 피싱 저항성, 앱 승인, 상호인증 관점을 추가할 때 사용한다.
- 실제 프로젝트에서는 Passwordless를 완전 대체 로그인으로 둘 수도 있고, 기존 로그인과 병행하거나 2차 인증처럼 설계할 수도 있다.

## 헷갈리기 쉬운 포인트

Passwordless라고 해서 인증이 사라지는 것이 아니다. “브라우저에 비밀번호를 입력하는 책임”이 줄어들고, 인증 서버·모바일 앱·Spring Boot 백엔드가 승인 결과를 확인하는 구조로 이동한다.

또한 QR 등록은 로그인 자체가 아니라 계정과 인증기를 묶는 과정이다. 등록 후 로그인에서는 앱 승인 요청을 확인하고, 성공 결과를 기존 JWT/세션 발급 흐름과 연결해야 한다.

## 관련 페이지

- [[entities/passwordless-x1280|Passwordless X1280]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]

## 출처

- `raw/Study/8. Passwordless/2026.05.14(목)/2026.05.14(목).md`
- `raw/Study/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/Study/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/Study/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
