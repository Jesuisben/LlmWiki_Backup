---
title: 2026-05-19 인증 기본과 AAM/APE 통합 설치
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [auth, linux, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf
status: growing
confidence: high
---

# 2026-05-19 인증 기본과 AAM/APE 통합 설치

## 한 줄 요약

인증(Authentication), 인가(Authorization), IDP, SSO, 상호인증을 구분한 뒤 AAM/APE 서버와 클라이언트 설치 흐름을 통해 기업형 Passwordless 계정·인증기 관리 구조를 살펴본 날이다.

## 배운 내용

- 인증은 “당신이 정말 당신인지 확인”하는 과정이고, 인가는 “확인된 사용자가 무엇을 할 수 있는지”를 제한하는 과정이다.
- MFA는 아는 것, 가진 것, 나 자신이라는 인증 요소 중 2개 이상을 조합한다.
- SSO는 한 번의 로그인으로 여러 서비스 접근을 가능하게 하는 구조이며, IDP는 디지털 신분증을 발급·관리하는 역할로 이해했다.
- 상호인증은 서비스가 사용자만 확인하는 것이 아니라 사용자가 서비스의 신뢰성도 확인하는 구조다.
- AAM/APE 실습에서는 서버 설치, 라이선스 적용, 관리자 웹 설정, 사용자 생성, 앱 계정 추가 흐름을 다뤘다.

## 핵심 개념

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]

## 실습 / 예제

```text
Rocky Linux VM 준비
→ AAM/APE/DMZ 서버 패키지 설치
→ APE 관리자 웹에서 라이선스/연동 서비스 설정
→ AAM 콘솔/관리자 웹에서 인증 서버 설정과 사용자 생성
→ APE에서 사용자·인증기 정보 확인
→ 모바일 앱 또는 클라이언트에서 계정 추가/로그인 확인
```

## 헷갈린 점 / 질문

- 인증과 인가는 항상 같이 등장하지만 책임이 다르다. 로그인 성공은 인증이고, 관리자 기능 접근 가능 여부는 인가다.
- 상호인증은 단순히 MFA를 하나 더 붙이는 것이 아니라 “내가 접속한 서비스가 진짜인지”도 확인하는 관점이다.
- 원본에는 라이선스 키·관리자 토큰·비밀번호가 실습값으로 적혀 있지만, wiki에서는 보안상 역할 설명만 남긴다.

## 관련 페이지

- [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14 Passwordless X1280 소개와 보안 배경]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf`
