---
title: Passwordless X1280
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [auth, backend, project]
sources:
  - raw/Study/8. Passwordless/2026.05.14(목)/2026.05.14(목).md
  - raw/Study/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/Study/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/Study/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/Study/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/Study/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless X1280

## 무엇인가

Passwordless X1280은 비밀번호 입력 대신 인증 서버와 모바일 앱 승인 흐름을 이용해 계정 로그인을 처리하는 패스워드리스 인증 기술이다. 수업에서는 ITU-T X.1280 기반 자동패스워드/Passwordless 인증 SW로 소개되었다.

## 이 위키에서의 맥락

이 위키에서 Passwordless X1280은 [[entities/aws|AWS]], [[entities/docker|Docker]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]]를 배운 뒤 중간 프로젝트 인증을 고도화하는 단계에서 등장한다. 앞선 수업에서 배운 JWT/세션/쿠키는 “로그인 상태 유지”를 다뤘고, X1280은 “사용자를 어떻게 비밀번호 없이 인증할 것인가”를 다룬다.

## 핵심 기능 / 특징

- Passwordless Members 사이트에서 서비스 등록과 라이선스 파일(`setting.ap`) 발급을 수행한다.
- Docker 통합 이미지로 Auth Server, User Connection Server, Push Request Server를 구성할 수 있다.
- Auth Server 관리자 페이지에서 서비스 서버 ID/key와 API 사용 종류를 설정한다.
- REST API 방식으로 Spring Boot 백엔드와 연동할 수 있다.
- QR 등록, 앱 승인, 등록 해제, 사용자 등록 여부 확인 같은 흐름을 제공한다.

## 학습 이력

- [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14]]: 보안 위협과 X1280 개념 소개.
- [[summaries/2026-05-15-passwordless-x1280-docker-service|2026-05-15]]: Docker 통합 서버, 서비스 등록, `setting.ap`, 관리자 페이지.
- [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|2026-05-18]]: Spring 샘플 앱과 MariaDB를 이용한 등록/로그인/해제 확인.
- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19]]: 인증/인가/SSO/상호인증과 AAM/APE 제품군 흐름.
- [[summaries/2026-05-21-passwordless-x1280-rest-api|2026-05-21]]: Postman으로 REST API 응답 구조 확인.
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]: 중간 프로젝트 Spring Boot/React 로그인에 X1280을 붙이는 적용 흐름.

## 관련 개념

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]

## 출처

- `raw/Study/8. Passwordless/2026.05.14(목)/2026.05.14(목).md`
- `raw/Study/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/Study/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/Study/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
- `raw/Study/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/Study/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
