---
title: 2026-05-18 Passwordless 서버 설치와 Spring 샘플 연동
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [auth, spring-boot, docker, backend, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
status: growing
confidence: high
---

# 2026-05-18 Passwordless 서버 설치와 Spring 샘플 연동

## 한 줄 요약

X1280 Docker 서버를 VM에 설치하고, MariaDB와 Spring 기반 샘플 웹서비스를 준비해 Passwordless 등록·로그인·해제 흐름을 실제 웹 애플리케이션에서 확인한 날이다.

## 배운 내용

- VM/네트워크/IP를 준비하고 Passwordless Members에서 테스트 서비스를 등록했다.
- Docker network와 X1280 통합 컨테이너를 만들고, host 방화벽과 서버 프로세스 상태를 확인했다.
- Auth Server 관리자 페이지에서 `setting.ap`를 업로드하고 서버 아이디/서버키를 발급한 뒤 API 사용 종류를 REST로 설정했다.
- 로컬 Windows 개발 환경에는 MariaDB, JDK, STS/Eclipse, Maven 프로젝트를 준비했다.
- 샘플 프로젝트의 설정 파일에는 인증 서버 주소, corpId/serverId, serverKey, REST check URL, Push connector URL 같은 연동값이 들어간다.
- Spring 샘플 앱에서 회원 생성 → Passwordless 등록 → Passwordless 로그인 → 등록 해제 → 비밀번호 로그인 복귀 흐름을 확인했다.

## 핵심 개념

- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 실습 / 예제

원본에는 실제 VM IP, 서버 아이디, 서버키, DB 비밀번호가 포함되어 있으나 wiki에는 재노출하지 않는다. 구조만 정리하면 다음과 같다.

```text
VM에 X1280 Docker 서버 실행
→ Auth 관리자 페이지에서 setting.ap 업로드
→ 서버 아이디/서버키 발급 및 REST 설정
→ 로컬 MariaDB userinfo 테이블 준비
→ Spring 샘플 프로젝트 설정 파일에 X1280 서버 정보 입력
→ Spring Boot App 실행
→ 계정 생성/등록/로그인/해제 테스트
```

수업에서 특히 중요한 관찰은 Passwordless 등록 후 일반 비밀번호 로그인 동작이 달라진다는 점이다. 샘플에서는 Passwordless 로그인 사용 시 비밀번호가 임의 값으로 바뀌어, 이후 일반 비밀번호 로그인을 하려면 Passwordless 등록 해제가 필요했다.

## 헷갈린 점 / 질문

- Passwordless 등록과 로그인은 같은 버튼처럼 보여도 서버 입장에서는 다른 API 흐름이다.
- serverId/corpId/serverKey는 외부 인증 서버 연동용 설정값이지, 사용자 비밀번호가 아니다.
- 로컬 개발환경의 DB와 인증 서버 컨테이너 내부 DB는 역할이 다르므로 “어느 DB에 무엇이 저장되는지”를 구분해야 한다.

## 관련 페이지

- [[summaries/2026-05-15-passwordless-x1280-docker-service|2026-05-15 Passwordless X1280 Docker 통합 서버와 서비스 등록]]
- [[summaries/2026-05-21-passwordless-x1280-rest-api|2026-05-21 Passwordless X1280 REST API와 Postman]]
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`
