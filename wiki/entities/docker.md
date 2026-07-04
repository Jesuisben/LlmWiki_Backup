---
title: Docker
created: 2026-07-02
updated: 2026-07-03
type: entity
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
  - raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
  - raw/Study/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Docker

## 무엇인가

Docker는 애플리케이션과 실행 환경을 이미지로 묶고, 그 이미지를 컨테이너로 실행하게 해 주는 컨테이너 플랫폼이다.

## 이 위키에서의 맥락

Linux에서 Spring Boot를 빌드·실행한 뒤, 같은 실행 환경을 더 쉽게 재현하기 위해 Docker가 등장했다. 수업은 Apache/nginx/MySQL 같은 기성 이미지 실행에서 시작해, 네트워크, mount, 사용자 정의 이미지, Dockerfile, reverse proxy, Docker Compose까지 확장됐다.

## 학습 이력

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]: Docker 이미지/컨테이너 개념, 설치, Apache/nginx/MySQL 컨테이너 실습.
- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29]]: WordPress+MySQL, Redmine+MariaDB, host↔container 파일 복사, bind/volume mount, Docker Hub push/pull.
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]]: Dockerfile, Spring Boot + MySQL 컨테이너, nginx reverse proxy/load balancing.
- [[summaries/2026-05-01-docker-compose|2026-05-01]]: Docker Compose, Docker Desktop/WSL2, MySQL+Spring Boot/WordPress manifest.
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]: Docker를 Linux 배포 학습의 후반 핵심 축으로 묶어 image/container, network, volume, Dockerfile, Compose를 복습.

## 핵심 기능 / 특징

- 이미지와 컨테이너 분리.
- 포트 매핑으로 호스트와 컨테이너 연결.
- 네트워크로 컨테이너 간 통신.
- `exec`/`cp`로 컨테이너 내부 작업과 파일 이동.
- bind mount/volume으로 데이터와 파일 유지.
- `commit` 또는 Dockerfile로 사용자 정의 이미지 생성.
- Docker Hub로 이미지 push/pull.
- Compose로 여러 서비스를 한 번에 실행.

## 프로젝트/면접 관점

Docker는 “배포 환경을 코드처럼 고정하는 도구”라고 설명할 수 있다. Spring Boot + MySQL 서비스를 Dockerfile과 Compose로 구성하면 팀원이 같은 DB/서버 구성을 반복해서 띄울 수 있고, 이후 CI/CD와 클라우드 배포로 이어진다.

## 관련 개념

- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf`
- `raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md`
- `raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
- `raw/Study/5. Linux/Linux 총정리/Linux 총정리.md`
