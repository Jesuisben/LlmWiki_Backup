---
title: 2026-05-14 Passwordless X1280 소개와 보안 배경
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [auth, backend, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/QPM 기본 기능 및 사용법 안내서_교육용_251209.pdf
status: growing
confidence: high
---

# 2026-05-14 Passwordless X1280 소개와 보안 배경

## 한 줄 요약

피싱·랜섬웨어·원격 코드 실행(RCE)·DDoS에서 출발해, 이미 침투했을 가능성을 전제로 하는 Zero Trust와 비밀번호 입력면을 줄이는 X1280 Passwordless의 필요성을 배운 날이다.

## 왜 이 순서로 배웠는가

도구 설치보다 먼저 공격자가 무엇을 노리는지 살폈다. 피싱은 사용자를 속여 입력값을 빼앗고, 랜섬웨어는 침투한 환경의 데이터를 암호화하며, RCE는 로그인 절차 자체를 우회할 수 있다. 따라서 “비밀번호를 더 복잡하게 만든다”만으로는 부족하고, 사용자가 접속 대상과 요청을 별도 인증기에서 확인하는 구조가 필요하다는 문제의식으로 X1280을 소개했다.

## 배운 내용

- 피싱, 멀웨어·랜섬웨어, 소프트웨어 취약점·RCE, DDoS의 공격 지점이 서로 다르다는 점을 구분했다.
- Zero Trust는 내부 PC나 서버도 이미 공격받았을 수 있다고 가정하고 계속 검증하는 관점으로 배웠다.
- Passwordless는 인증을 없애는 것이 아니라 사용자가 브라우저에 비밀번호를 입력하는 단계를 줄이고 다른 인증 요소와 승인 절차로 신원을 확인하는 방식이다.
- 수업에서는 X1280을 스마트폰 앱에서 요청 출처와 내용을 확인하는 대역외(Out-of-Band) 인증 흐름으로 설명했다.
- 인증을 신원인증·계정인증·연합인증으로 나눴고, IDP·SSO·RADIUS·FIDO·Passkey·QR Password Manager는 인접 용어로 소개했다. 제품 일반 기능이나 상호 호환을 직접 실습한 날은 아니다.

## 수업 예시와 결과 경계

개념 예시는 사용자 ID 입력 → 서비스가 인증 요청 생성 → 모바일 인증기가 요청 출처와 내용을 표시 → 사용자가 승인 → 서비스가 결과를 확인하는 흐름이었다. 이 흐름은 [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]의 배경 설명이며, 이날 원본에는 X1280 서버 설치 명령·설정 파일·API 요청·응답·화면 성공 결과가 없다.

교육 PDF와 QPM 안내서는 제품 개념과 화면 절차를 보조하는 교육 입력자료다. 날짜 원본의 직접 실행 결과를 대신하지 않는다.

## 헷갈린 점 / 질문

- **Passwordless = 인증 없음:** 아니다. 비밀번호 입력 대신 인증기 소지·앱 승인·서버 검증이 남는다.
- **OTP와 앱 승인:** OTP는 사용자가 일회용 값을 다시 입력하는 방식이 일반적이고, 수업의 X1280 흐름은 앱에서 요청을 확인·승인하는 점을 강조했다.
- **Passwordless면 RCE·랜섬웨어도 해결:** 아니다. 계정 인증 공격면을 줄일 뿐, 서버 취약점과 저장 데이터 보호는 별도 계층이다. 05-20에는 이 경계를 [[concepts/nas-worm-storage-protection|NAS·WORM 저장소 보호]]로 확장한다.

## 이전·다음 연결

- 선행: [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 Cookie·Session·JWT 이론과 로그인 토큰 생성]]과 [[summaries/2026-04-07-member-api-string-token|2026-04-07 Bearer token과 Spring Security JWT 인증 흐름]]은 비밀번호 기반 로그인과 로그인 상태 전달을 구현했다.
- 다음: [[summaries/2026-05-15-passwordless-x1280-docker-service|2026-05-15 Passwordless X1280 Docker 통합 서버와 서비스 등록]]에서 서비스 등록과 서버 구성 절차로 이동한다.
- 후속: 중간 프로젝트 적용 설계는 단계 9의 [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]] 범위다.

## 관련 페이지

- [[entities/passwordless-x1280|Passwordless X1280]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[comparisons/authentication-vs-authorization|인증(Authentication) vs 인가(Authorization)]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/QPM 기본 기능 및 사용법 안내서_교육용_251209.pdf`