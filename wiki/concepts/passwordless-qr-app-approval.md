---
title: Passwordless QR/앱 승인 흐름
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [auth, frontend, backend, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless QR/앱 승인 흐름

## 정의

Passwordless QR/앱 승인 흐름은 사용자가 브라우저에 비밀번호를 입력하는 대신, 모바일 앱에서 등록 QR을 스캔하거나 로그인 승인 요청을 확인해 인증을 완료하는 절차다.

## 왜 중요한가

프론트엔드 입장에서는 단순히 “로그인 버튼 하나 추가”처럼 보일 수 있지만, 실제로는 QR 표시, 승인 대기, polling 또는 결과 확인, 성공/실패/해제 상태를 모두 UI로 표현해야 한다. 백엔드 입장에서는 X1280 인증 서버와 통신해 각 상태를 정확히 해석해야 한다.

## 핵심 설명

### 등록 흐름

```text
사용자 ID 입력
→ 등록 요청
→ 인증 서버가 등록용 QR/데이터 생성
→ React가 QR 표시
→ 사용자가 X1280 앱으로 QR 스캔
→ 앱에 서비스/계정 등록
→ 서버가 등록 완료 상태 확인
```

### 로그인 승인 흐름

```text
사용자 ID 입력
→ Passwordless 로그인 요청
→ 인증 서버가 앱 승인 요청 생성
→ 사용자가 모바일 앱에서 요청 출처/내용 확인
→ 승인 또는 거절
→ Spring Boot가 결과 확인
→ 성공 시 JWT/세션 등 기존 로그인 상태 생성
```

### 해제 흐름

등록 해제는 사용자 계정과 앱 인증기 연결을 끊는 작업이다. 실습에서는 Passwordless 등록 후 일반 비밀번호 로그인이 제한되는 사례가 있었기 때문에, 해제 흐름은 비밀번호 로그인 복귀나 재등록 테스트에 중요하다.

## 수업 예시

- 2026-05-15에는 WordPress plugin 실습에서 Passwordless Reg/Unreg, QR 코드 앱 등록, Passwordless 로그인 확인 흐름을 다뤘다.
- 2026-05-18에는 Spring 샘플 웹서비스에서 계정 생성, Passwordless 등록, Passwordless 로그인, 해제, 일반 로그인 복귀를 확인했다.
- 중간 프로젝트 적용 가이드에서는 React 로그인 페이지에 Passwordless 옵션, 등록/해제 UI, result polling을 붙이는 흐름으로 확장된다.

## 자주 헷갈리는 점

- QR은 “로그인 성공 표시”가 아니라 등록 또는 인증 요청을 앱으로 넘기기 위한 매개다.
- 앱 승인을 기다리는 동안 프론트는 대기 상태를 보여줘야 하고, 백엔드는 결과 확인 API 또는 callback 흐름을 처리해야 한다.
- 사용자가 앱에서 거절하거나 timeout이 나면 로그인 실패와 다른 상태로 구분해 안내하는 것이 좋다.

## 관련 개념

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
