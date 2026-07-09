---
title: 2026-05-14 Passwordless X1280 소개와 보안 배경
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [auth, backend, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf
status: growing
confidence: high
---

# 2026-05-14 Passwordless X1280 소개와 보안 배경

## 한 줄 요약

피싱·랜섬웨어·원격 코드 실행 같은 공격이 “사용자 입력값 탈취”와 “이미 침투한 환경”을 전제로 발전한다는 배경에서, ITU-T X.1280 Passwordless가 왜 비밀번호 입력을 없애고 상호 인증을 강조하는지 배운 날이다.

## 배운 내용

- 주요 사이버 공격을 피싱, 멀웨어/랜섬웨어, 소프트웨어 취약점/RCE, DDoS로 나눠 보았다.
- 기존 보안의 약점은 사용자가 ID/PW 같은 credential을 직접 입력한다는 점이다.
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]은 “사용자가 입력해서 증명하는 방식”을 줄이고, 온라인 시스템과 사용자 단말/앱이 서로 확인하는 구조로 바꾼다.
- 인증은 신원인증, 계정인증, 연합인증으로 나눠 볼 수 있고, X1280은 주로 계정 로그인 영역의 비밀번호 대체·강화 기술로 등장했다.
- FIDO/Passkey처럼 단말 내 센서를 쓰는 대역내 인증과 달리, 수업에서는 X1280을 스마트폰 앱 승인 기반의 대역외 인증으로 소개했다.

## 핵심 개념

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[entities/passwordless-x1280|Passwordless X1280]]

## 실습 / 예제

수업의 핵심 예시는 “아이디를 입력하면 서버/서비스가 사용자에게 인증번호나 승인 요청을 제시하고, 사용자는 모바일 앱에서 요청이 맞는지 확인한다”는 흐름이다. 즉 사용자가 비밀번호를 브라우저에 입력하는 대신, 스마트폰 앱에서 요청 출처와 인증 내용을 확인해 승인한다.

```text
기존 로그인: 사용자가 ID/PW 입력 → 서버가 값 검증
Passwordless: 사용자가 ID 입력 → 서버/인증 서버가 요청 생성 → 앱에서 요청 확인/승인 → 서버가 결과 검증
```

## 헷갈린 점 / 질문

- Passwordless는 “인증이 없는 것”이 아니라 “비밀번호 입력이 없는 인증”이다.
- OTP는 사용자가 일회용 값을 다시 입력하지만, X1280 수업 흐름에서는 앱 승인과 상호 인증으로 입력 탈취면을 줄이는 점이 강조됐다.
- Zero Trust 관점에서는 내 PC가 이미 악성코드에 감염되어 있을 수 있다고 가정하고, 입력값 탈취에 기대지 않는 인증 방식을 고민한다.

## 관련 페이지

- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 로그인, JWT, 세션과 쿠키]]
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf`
