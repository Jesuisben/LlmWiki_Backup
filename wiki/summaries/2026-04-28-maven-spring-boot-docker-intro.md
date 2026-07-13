---
title: 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문
created: 2026-07-06
updated: 2026-07-13
type: summary
tags: [linux, docker, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
status: growing
confidence: high
---

# 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문

## 한 줄 요약

GitHub에서 Spring Boot 프로젝트를 Linux로 가져와 Maven으로 jar를 만들고 `java -jar`로 실행한 뒤, Docker 설치와 기본 컨테이너 실행으로 넘어갔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

개발 PC에서 잘 되는 Spring Boot 앱도 서버에서는 빌드 산출물, 포트, 방화벽, 프로세스 관리가 맞아야 동작한다. Docker는 이 실행 환경을 이미지/컨테이너로 재현하기 위한 다음 단계다.

## 핵심 개념

- GitHub clone → Spring 포트 확인 → 방화벽/포트 포워딩 → Maven 설치 → jar 패키징 → `java -jar` 실행 흐름을 정리했다.
- Apache/Nginx 중지와 포트 충돌 확인을 실습했다.
- Docker 개요, 이미지 생성, 설치와 docker 그룹 권한 설정을 배웠다.
- httpd/nginx/MySQL 컨테이너 실행·중지·삭제와 기본 명령을 확인했다.

## 실습 / 예제

`mvn clean package -DskipTests`, `java -jar`, `docker run -d -p ...`, `docker ps/stop/rm`을 순서대로 써서 IDE 밖 실행과 컨테이너 실행을 비교했다.

## 헷갈린 점 / 질문

Maven은 jar를 만드는 빌드 도구이고, `java -jar`는 만들어진 jar 실행이다. Docker image는 템플릿, container는 실행 인스턴스다.

## 관련 페이지

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]], [[concepts/docker-image-container|Docker 이미지와 컨테이너]], [[entities/maven|Maven]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`
