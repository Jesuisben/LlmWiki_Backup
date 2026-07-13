---
title: 2026-05-01 Docker Compose와 다중 컨테이너 실행
created: 2026-07-06
updated: 2026-07-13
type: summary
tags: [linux, docker, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
status: growing
confidence: high
---

# 2026-05-01 Docker Compose와 다중 컨테이너 실행

## 한 줄 요약

Docker Compose manifest로 MySQL/WordPress 같은 다중 컨테이너 구성을 선언하고, Docker Desktop과 Compose 실습으로 컨테이너 묶음 실행을 익혔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

여러 `docker run` 명령을 매번 직접 입력하면 네트워크, 볼륨, 환경 변수, 포트 설정이 누락되기 쉽다. Compose는 실행 구성을 파일로 남기는 방식이다.

## 핵심 개념

- Compose manifest가 컨테이너, 이미지, 포트, 볼륨, 네트워크, 환경 변수를 선언하는 문서임을 배웠다.
- `services`, `networks`, `volumes`, `environment`, `depends_on` 같은 YAML 항목을 확인했다.
- Docker Desktop 설치와 GUI 확인 흐름을 다뤘다.
- Permission denied가 보이면 docker 그룹 권한 반영을 위해 로그아웃/재접속이 필요하다는 점을 확인했다.

## 실습 / 예제

Compose 파일을 작성해 DB와 앱 컨테이너를 한 번에 올리고, `docker compose up/down/ps/logs` 흐름으로 상태를 확인했다.

## 헷갈린 점 / 질문

Compose는 이미지를 만드는 도구라기보다 여러 컨테이너 실행 구성을 묶어 실행하는 도구다. 이미지 생성은 Dockerfile/build 단계와 연결된다.

## 관련 페이지

- [[concepts/docker-compose-manifest|Docker Compose manifest]], [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]], [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]

## 출처

- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md`
