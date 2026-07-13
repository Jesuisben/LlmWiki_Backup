---
title: Docker
created: 2026-07-02
updated: 2026-07-13
type: entity
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
  - raw/KoreaICT/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
status: growing
confidence: high
---

# Docker

## 무엇인가

Docker는 애플리케이션과 실행 환경을 이미지로 묶고, 그 이미지를 컨테이너로 실행하게 해 주는 컨테이너 플랫폼이다.

## 이 위키에서의 맥락

Linux에서 Spring Boot를 직접 빌드·실행한 뒤, 같은 실행 환경을 더 쉽게 재현하기 위해 Docker가 등장했다. 수업은 Apache/nginx/MySQL 같은 기성 이미지 실행에서 시작해 network, mount, 사용자 정의 이미지, Dockerfile, reverse proxy, Docker Compose까지 확장됐다.

## 핵심 기능 / 특징

- image/container 생명주기 관리.
- host와 container port mapping.
- `exec`/`cp`를 통한 컨테이너 내부 조작.
- network로 컨테이너 간 통신 구성.
- bind mount/volume으로 파일과 데이터 보존.
- Dockerfile로 재현 가능한 이미지 작성.
- Compose로 다중 컨테이너 실행 선언.

## 학습 이력

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]: Docker 입문과 기본 컨테이너 실행.
- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29]]: network, volume, `exec`, `cp`, `commit`.
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]]: Dockerfile, Spring Boot image, reverse proxy.
- [[summaries/2026-05-01-docker-compose|2026-05-01]]: Docker Compose.
- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11]]: GitHub Actions가 만든 Spring Boot image를 Docker Hub에 저장하고 EC2에서 pull/run하는 CI/CD 배포 단위로 확장.

## 관련 개념

- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]

## 최신 원본 대조

Docker의 학습 이력을 04-28 image/container/port mapping → 04-29 network·mount·commit → 04-30 Dockerfile·reverse proxy → 05-01 Compose → 05-11 Docker Hub registry·EC2 container 배포로 명시했다. 따라서 Docker는 단일 컨테이너 명령어가 아니라 실행 구성을 재현하고 배포하는 도구다.

## 출처

- `raw/KoreaICT/5. Linux` Docker 관련 날짜 MD와 교육자료 MD/PDF
