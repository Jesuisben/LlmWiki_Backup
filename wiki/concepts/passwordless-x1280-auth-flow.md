---
title: Passwordless X1280 인증 흐름
created: 2026-07-03
updated: 2026-07-13
type: concept
tags: [auth, project, backend, frontend, spring-boot]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless X1280 인증 흐름

## 정의

Passwordless X1280 인증 흐름은 비밀번호를 사용자가 직접 입력하지 않고, 외부 X1280 인증 서버와 모바일 앱 승인 결과를 이용해 사용자를 확인하는 로그인 구조다. 수업에서는 ITU-T X.1280 기반 자동패스워드/패스워드리스 기술로 소개되었다.

## 왜 중요한가

기존 ID/PW 방식은 사용자가 credential을 입력하므로 피싱·파밍·키로깅·중간자 공격의 표적이 된다. X1280 흐름은 사용자의 입력 책임을 줄이고, 서비스/인증 서버/모바일 앱 사이의 승인 결과를 확인해 계정 탈취 위험을 낮추는 방향으로 설계된다.

중간 프로젝트에서는 이 흐름이 단순 이론이 아니라 [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]의 실제 로그인 기능 확장으로 이어진다.

## 핵심 설명

### 1. 구성 요소

- **사용자/브라우저**: 아이디 입력, 등록/로그인/해제 요청을 시작한다.
- **웹 애플리케이션**: 등록·로그인·해제 UI를 제공하고, X1280 인증 결과를 서비스 로그인 흐름과 연결한다.
- **Spring 샘플/프로젝트 백엔드**: X1280 인증 서버 REST API를 호출하고 결과를 해석한다.
- **Passwordless X1280 Auth Server**: 서비스 등록 정보, 서버 아이디/서버키, 사용자 등록/승인 상태를 관리한다.
- **User Connection / Push Request Server**: 앱과 연결하고 승인 요청/결과 흐름을 전달한다.
- **모바일 앱**: QR 등록 또는 로그인 승인 요청을 사용자가 확인하고 승인하는 장소다.

### 2. 전체 흐름

```text
아이디 입력
→ 웹 애플리케이션이 X1280 연동 요청
→ Spring 샘플 또는 프로젝트 백엔드가 X1280 인증 서버 REST API 호출
→ 등록 전이면 QR/등록 흐름 생성
→ 등록 후이면 앱 승인 요청 생성
→ 사용자가 모바일 앱에서 요청 확인/승인
→ 애플리케이션이 REST 결과를 확인
→ 서비스의 로그인 상태 처리와 연결
```

### 3. 등록과 로그인의 차이

- **등록**: 특정 사용자 계정과 모바일 앱/인증기를 연결하는 단계다. 원본 실습에서는 QR 코드로 앱에 사이트/계정을 등록하는 흐름이 반복 등장한다.
- **로그인**: 이미 등록된 계정에 대해 앱 승인 요청을 보내고, 승인 결과가 성공이면 서비스 로그인 상태를 만든다.
- **해제**: 계정과 Passwordless 인증기 연결을 끊어 일반 로그인 또는 재등록 가능 상태로 되돌린다.

## 수업 예시

- [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14]]: 피싱/랜섬웨어/RCE와 Zero Trust 배경, X1280의 개념과 OTP/FIDO/Passkey와의 차이.
- [[summaries/2026-05-15-passwordless-x1280-docker-service|2026-05-15]]: Members 사이트 서비스 등록, `setting.ap`, Docker 통합 서버, Auth 관리자 페이지, REST/UI 제공 방식.
- [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|2026-05-18]]: MariaDB와 Spring 샘플 앱에서 등록/로그인/해제 흐름 확인.
- [[summaries/2026-05-21-passwordless-x1280-rest-api|2026-05-21]]: Postman collection으로 사용자 등록 여부 확인 API 같은 REST 응답 구조 확인.

### 날짜 원본과 프로젝트 적용 가이드의 경계

2026-05-15·05-18·05-21 날짜 원본은 서비스 등록, X1280 서버, 샘플 애플리케이션, Postman API 확인을 직접 다룬다. React의 polling, callback 처리, JWT/세션 발급, Member 상태 컬럼, `SecurityConfig`의 공개 endpoint 설계는 [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]에서 확장한 프로젝트 적용 설계다. 이를 날짜 수업의 직접 구현 사실로 섞지 않는다.

## 자주 헷갈리는 점

- Passwordless는 “인증이 사라지는 것”이 아니라 “비밀번호 입력이 앱 승인/외부 인증 서버 검증으로 이동하는 것”이다.
- QR은 주로 등록 단계에서 계정과 앱을 묶기 위한 수단이고, 앱 승인은 로그인 요청이 진짜인지 확인하는 수단이다.
- X1280 서버의 serverId/serverKey는 사용자 비밀번호가 아니라 서비스 서버가 인증 서버와 통신하기 위한 연동 credential이다.
- Postman에서 API가 성공해도 프로젝트 로그인 처리가 완성된 것은 아니다. Spring Boot에서 DTO, REST client, Service, Controller, Security 설정까지 연결해야 한다.

## 관련 개념

- [[entities/passwordless-x1280|Passwordless X1280]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
