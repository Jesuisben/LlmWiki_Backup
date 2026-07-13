---
title: 중간 프로젝트 CI/CD·배포·Passwordless 가이드
created: 2026-07-03
updated: 2026-07-14
type: summary
tags: [project, ci-cd, aws, auth, spring-boot, react]
sources:
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md
status: growing
confidence: medium
---

# 중간 프로젝트 CI/CD·배포·Passwordless 가이드

## 한 줄 요약

중간 프로젝트를 AWS EC2/RDS 환경에 배포하고, GitHub Actions/Secrets 기반 CI/CD와 Passwordless X1280 인증을 붙이는 실전 가이드 묶음이다.

## 배운 내용

- Spring Boot 백엔드와 React 프론트엔드 프로젝트를 배포 가능한 산출물로 준비한다.
- GitHub Secrets에는 Docker Hub 인증, 배포 대상 image, EC2 접속, DB 접속, JWT 공개/개인키, S3 접근 항목처럼 역할별 설정을 넣고 workflow에서 참조한다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md]
- CI/CD 파이프라인은 코드 변경 → GitHub Actions 실행 → CI의 Docker Hub image push → CD의 EC2 컨테이너 갱신 → 서비스 확인의 흐름으로 이해한다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md]
- Passwordless 적용 가이드는 기존 로그인 흐름에 외부 인증 서버, QR 등록, 앱 승인 대기/결과 흐름을 연결하는 방식으로 읽는다. 2026-05-14~05-21 Passwordless 날짜별 수업은 이 가이드의 배경 지식과 실습 기반이다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md]
- 실습 원본에는 IP, endpoint, password, secret 예시가 섞일 수 있으므로 위키에서는 구조만 남기고 값은 일반화한다.

## 핵심 개념

- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/jwt-rs256-key-flow|JWT RS256 키 흐름]]

## 실습 / 예제

1. GitHub 저장소에 프로젝트 코드를 올린다.
2. Repository Secrets에 서버/DB/인증 관련 설정값을 등록한다.
3. GitHub Actions workflow가 빌드·전송·재시작을 수행한다.
4. AWS 서버에서 Spring Boot/React 또는 Nginx 연동 상태를 확인한다.
5. Passwordless 설정 화면에서 사용자 등록, QR 승인, 앱 승인 대기/성공/실패 상태를 확인한다.

## 헷갈린 점 / 질문

- Secret 이름과 실제 값은 다르다. 위키에는 이름과 역할만 남기고 실제 값은 남기지 않는다.
- JWT `HS256`과 `RS256`은 키 구조가 다르다. RS256은 개인키로 서명하고 공개키로 검증하는 흐름이다. ^[raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md]
- Passwordless는 “비밀번호가 없는 로그인 UI”만이 아니라 외부 인증 서버와 앱 승인 상태까지 포함하는 인증 흐름이다.

## 관련 페이지

- [[entities/aws|AWS]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/react|React]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14 Passwordless X1280 소개와 보안 배경]]
- [[summaries/2026-05-21-passwordless-x1280-rest-api|2026-05-21 Passwordless X1280 REST API와 Postman]]

## 출처

- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md`
