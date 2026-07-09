---
title: 2026-04-27 Linux 압축, 다운로드, Java 실행 준비
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
status: growing
confidence: high
---

# 2026-04-27 Linux 압축, 다운로드, Java 실행 준비

## 한 줄 요약

wget/curl/tar/zip으로 파일을 내려받고 압축을 다루며, chown/alias/JDK/JDBC 준비와 Java 코드 실행으로 서버 작업 흐름을 넓혔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

서버 배포는 원격 파일 다운로드, 압축 해제, 권한 조정, 실행 환경 설치가 반복된다. Docker 이전에 Linux 파일 준비 능력을 먼저 익히는 단계다.

## 핵심 개념

- `wget`, `curl`로 URL의 파일을 Linux에 다운로드했다.
- `tar.gz`, `zip` 압축 해제와 파일/디렉터리 복사·삭제를 실습했다.
- `alias`를 설정하고 `.sh` 파일로 관리하는 방법을 확인했다.
- JDK/JDBC 드라이버를 준비하고 Linux에서 Java 코드를 작성·실행했다.

## 실습 / 예제

다운로드 디렉터리를 만들고 압축 파일을 받아 풀어본 뒤, alias와 Java 실행 테스트로 반복 작업을 줄이는 흐름을 실습했다.

## 헷갈린 점 / 질문

`wget/curl`은 설치가 아니라 파일 다운로드 도구다. `tar`는 압축 파일을 다루는 도구이고, 실행 가능 여부는 권한과 설치된 런타임에 따라 달라진다.

## 관련 페이지

- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]], [[entities/java|Java]], [[entities/linux|Linux]], [[entities/docker|Docker]], [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md`
