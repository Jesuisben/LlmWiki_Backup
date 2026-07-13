---
title: 가상 머신(VM) vs Docker 컨테이너
created: 2026-07-13
updated: 2026-07-13
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# 가상 머신(VM) vs Docker 컨테이너

## 비교 목적

5과목은 VirtualBox의 Ubuntu VM에 SSH로 접속하는 실습으로 시작하고, 그 Linux 안에서 Docker 컨테이너를 실행하는 단계로 확장된다. 둘 다 격리된 실행 환경처럼 보이지만, VM은 운영체제 단위이고 컨테이너는 호스트 Linux 커널을 공유하는 프로세스 단위다.

## 한눈에 보기

| 항목 | VM | Docker 컨테이너 |
|---|---|---|
| 수업의 예 | VirtualBox에 설치한 Ubuntu | `httpd`, `nginx`, MySQL, Spring Boot 컨테이너 |
| 격리 기준 | 가상 하드웨어와 guest OS | 프로세스와 파일 시스템/네트워크 namespace |
| 시작점 | ISO로 Ubuntu 설치 | image를 `docker run`으로 실행 |
| 접속 방식 | VM IP에 SSH/MobaXterm 접속 | `docker exec`로 실행 중 컨테이너 명령 실행 |
| 주 용도 | 서버 OS 자체를 실습·운영 | 앱과 의존 환경을 반복 가능하게 실행 |

## 수업 흐름에서의 관계

`VirtualBox VM → Ubuntu → SSH/MobaXterm → Docker Engine → image → container` 순서다. 즉 Docker는 VM의 대체물이 아니라, 수업에서는 Ubuntu 서버 위에서 웹·DB·Spring Boot 실행 환경을 더 잘게 나누고 재현하는 도구로 등장했다.

## 헷갈리기 쉬운 포인트

- MobaXterm은 VM이나 Docker가 아니라 VM에 SSH로 접속하는 클라이언트다.
- `docker exec -it 컨테이너 /bin/bash`는 컨테이너 안에서 shell을 실행하는 것이며, VM에 새로 SSH 접속하는 것과 다르다.
- VM의 네트워크/방화벽과 Docker의 `-p host:container` 포트 매핑은 별도 층위다. 접속 실패 시 둘을 함께 점검해야 한다.

## 관련 페이지

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
