---
title: Spring Boot Passwordless 인증 연동
created: 2026-07-03
updated: 2026-07-13
type: concept
tags: [spring-boot, auth, backend, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Spring Boot Passwordless 인증 연동

## 정의

Spring Boot Passwordless 인증 연동은 Spring 기반 웹 애플리케이션이 X1280 인증 서버 REST API와 통신하고, 등록·로그인·해제 결과를 서비스 로그인 흐름과 연결하는 구조다. React·JWT·SecurityConfig를 포함한 전체 프로젝트 설계는 별도 중간 프로젝트 가이드의 확장 범위다.

## 왜 중요한가

중간 프로젝트의 기존 로그인은 보통 회원 DB, 비밀번호 검증, JWT 발급처럼 프로젝트 내부 로직 중심이다. Passwordless를 붙이면 외부 인증 서버의 등록/승인 상태를 함께 해석해야 하므로 Controller, Service, DTO, REST client, SecurityConfig가 모두 영향을 받는다.

## 핵심 설명

### 백엔드 구성 요소

- **설정값**: 인증 서버 REST URL, corpId/serverId, serverKey, Push/User Connection URL 등. 실제 값은 환경변수나 secret으로 분리한다.
- **REST client**: X1280 인증 서버 API를 호출한다.
- **공통 응답 DTO**: `result`, `code`, `msg`, `data` 같은 API 응답 구조를 받는다.
- **기능별 DTO·Service·Controller·SecurityConfig·Member 상태**: 중간 프로젝트 가이드에서 제안한 프로젝트 적용 구조다. 05-18·05-21 날짜 원본은 이 전체 구현을 직접 작성한 근거가 아니라, 샘플 설정과 API 계약을 확인한 근거다.

### 요청 흐름

```text
웹 애플리케이션 요청
→ 프로젝트의 연동 계층
→ X1280 REST client
→ X1280 Auth Server
→ 앱 승인/QR 등록
→ 결과 해석
→ 서비스 로그인 처리 또는 실패 안내
```

## 수업 예시

- 2026-05-18 샘플 프로젝트에서는 `config.properties`에 인증 서버 URL, corpId/serverId, serverKey, REST check URL, Push connector URL을 넣고 Spring 기반 샘플 앱을 실행했다. 뒤쪽 실습에서는 MariaDB `userinfo`와 WAR/Tomcat 배포도 확인했다.
- 2026-05-21 Postman 실습에서는 `isAP` 같은 API 응답 구조를 직접 확인했다. 이 경험이 Spring Boot REST client/DTO 설계의 기준이 된다.
- 중간 프로젝트 적용 가이드는 `application.properties`, Member 등록 여부 컬럼, REST client, DTO, Service, Controller, SecurityConfig, React 화면 연결을 순서대로 제시한다. 이 설계는 날짜 수업에 없는 구현 세부사항을 보완하는 후속 출처다.

## 자주 헷갈리는 점

- X1280 serverKey는 application source에 하드코딩하지 않고 환경변수, GitHub Secrets, 서버 설정으로 분리해야 한다.
- Postman에서 API 호출이 되는 것과 프로젝트 로그인 완료는 다르다. 승인 결과를 기존 회원 로그인 상태와 연결해야 사용자가 실제로 로그인된다.
- Passwordless endpoint를 모두 막아두면 로그인 시작 자체가 안 되고, 모두 열어두면 결과 확인/해제 API가 위험해질 수 있다. SecurityConfig에서 공개/보호 범위를 구분해야 한다.

## 관련 개념

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
