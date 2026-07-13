---
title: 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱
created: 2026-07-06
updated: 2026-07-13
type: summary
tags: [linux, docker, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
status: growing
confidence: high
---

# 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱

## 한 줄 요약

docker commit과 Dockerfile을 비교하고, Spring Boot 컨테이너와 MySQL 접속, nginx upstream/proxy_pass 기반 로드 밸런싱을 실습했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

컨테이너 상태를 즉석 저장하는 방식보다 Dockerfile로 이미지 생성 과정을 문서화해야 재현 가능한 배포가 가능하다. 로드 밸런싱은 여러 서버/컨테이너로 트래픽을 나누는 배포 개념이다.

## 핵심 개념

- 컨테이너를 이미지로 만드는 방법으로 `commit`과 Dockerfile을 비교했다.
- Dockerfile에서 base image, copy, build context 개념을 확인했다.
- Spring Boot 컨테이너 생성과 MySQL 컨테이너 접속 명령을 실습했다.
- nginx.conf의 `upstream`, `server`, `proxy_pass`로 Apache/Nginx 컨테이너에 요청을 분산했다.

## 실습 / 예제

Dockerfile로 커스텀 웹 이미지를 만들고, nginx 설정 파일에서 `/apache`, `/nginx` 같은 경로별 proxy를 구성해 로드 밸런싱 테스트를 했다.

## 헷갈린 점 / 질문

Dockerfile은 이미지 생성 레시피이고 Docker Compose는 여러 컨테이너 실행 manifest다. `upstream`은 서버 그룹 이름이며 실제 요청 전달은 `proxy_pass`가 담당한다.

## 관련 페이지

- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]], [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]], [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md`
