---
title: 2026-05-15 Passwordless X1280 Docker 통합 서버와 서비스 등록
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [auth, docker, backend, project, curriculum]
sources:
  - raw/Study/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/Study/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
  - raw/Study/8. Passwordless/교육 자료/Wordpress-Passwordless X1280 Plugin/PasswordlessX1280 - Wordpress plugin OVA install Test Guide.pdf
status: growing
confidence: high
---

# 2026-05-15 Passwordless X1280 Docker 통합 서버와 서비스 등록

## 한 줄 요약

Passwordless Members 사이트에서 서비스를 등록하고 `setting.ap` 라이선스 파일을 받은 뒤, Docker 통합 이미지로 Auth/User Connection/Push Request 서버를 띄워 웹 애플리케이션과 연결하는 전체 설치 흐름을 배운 날이다.

## 배운 내용

- 서비스 적용은 서비스 등록 → X1280 서버 설치 → 웹 애플리케이션 적용 순서로 진행된다.
- X1280 Docker 통합 이미지는 Auth Server, User Connection Server, Push Request Server를 함께 제공한다.
- 서비스 등록 시 서비스 도메인, 사설 IP, 유저 커넥션 서버 도메인을 입력하고, 일반 모드에서는 DNS TXT 검증을 거쳐 승인 상태가 된다.
- 테스트 모드는 도메인 검증 절차를 단순화해 수업 실습에 적합하다.
- Auth Server 관리자 페이지에는 `setting.ap`를 업로드하고, 서비스 서버 설정에서 서버 아이디와 서버키를 발급한다.
- 웹 애플리케이션 적용 방식은 UI 제공 방식과 RESTful API 제공 방식으로 나뉜다.

## 핵심 개념

- [[entities/passwordless-x1280|Passwordless X1280]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]

## 실습 / 예제

수업에서는 Docker Hub의 X1280 통합 이미지를 실행하고 여러 포트를 열어 서버 3종을 확인했다. 위키에는 원본의 실습 IP·서버키·관리자 비밀번호 같은 값은 보존하지 않고, 역할만 남긴다.

```text
Passwordless Members
→ 서비스 추가/승인
→ setting.ap 다운로드
→ X1280 Docker 서버 실행
→ Auth 관리자 페이지에서 setting.ap 업로드
→ 서버 아이디/서버키 발급
→ 웹 애플리케이션이 REST 또는 UI 방식으로 연동
```

## 헷갈린 점 / 질문

- `setting.ap`는 웹 앱 소스코드가 아니라 인증 서버 관리자 페이지에 올리는 라이선스/설정 파일이다.
- `DOMAIN`, Auth Server URL, User Connection URL, Push URL은 같은 “주소”처럼 보이지만 각 서버 역할이 다르다.
- Docker 컨테이너 포트와 host 방화벽 포트는 구분해야 한다. 원본에서는 host 방화벽 오픈과 Docker 포트 매핑을 별도로 다뤘다.

## 관련 페이지

- [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|2026-05-18 Passwordless 서버와 Spring 샘플 연동]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]

## 출처

- `raw/Study/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/Study/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`
- `raw/Study/8. Passwordless/교육 자료/Wordpress-Passwordless X1280 Plugin/PasswordlessX1280 - Wordpress plugin OVA install Test Guide.pdf`
