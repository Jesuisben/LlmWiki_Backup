---
title: Linux 총정리
type: summary
created: 2026-07-03
updated: 2026-07-03
tags: [linux, docker, ci-cd, curriculum, study-log]
sources:
  - raw/Study/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux 총정리

## 한 줄 요약

`Linux 총정리`는 2026-04-22부터 2026-05-06까지 배운 서버 운영 기초를 “Linux CLI와 권한 → Spring Boot 서버 실행 → Docker/Compose → GitHub 협업” 순서로 다시 묶는 복습 허브다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]부터 [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결]]까지의 날짜별 Linux/Docker/GitHub 수업 노트
- 이전 흐름: [[entities/spring-boot|Spring Boot]]와 [[entities/react|React]]로 만든 웹서비스를 개발 PC 밖의 서버 환경에서 실행하는 단계로 넘어감
- 다음 흐름: [[entities/aws|AWS]]에서 EC2/RDS/Route 53/Load Balancer 같은 클라우드 인프라에 배포하고, 이후 CI/CD 자동화로 연결
- 역할: 날짜별 수업 요약을 대체하는 새 진도 페이지가 아니라, Linux 서버 운영·Docker·협업 흐름을 다시 찾기 위한 복습 허브

## 배운 내용

### 1. Linux 서버 접속과 파일 시스템

초반부는 VirtualBox Ubuntu 설치, SSH 서버, MobaXterm 접속, 프롬프트, 경로, `pwd`, `cd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `find`, `vi` 같은 기본 명령으로 서버 파일 시스템을 다루는 흐름이다. 개발자가 만든 파일을 서버 어디에 두고 어떻게 확인하는지의 출발점이며, [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]으로 이어진다.

### 2. 사용자, 그룹, 권한

Linux에서는 파일을 “누가 읽고/쓰고/실행할 수 있는가”가 중요하다. `owner/group/others`, `rwx`, `sudo`, 사용자·그룹 생성, `/etc/passwd`, `/etc/shadow`, `/etc/group` 이해는 서버에서 권한 오류를 해석하는 기준이 된다. 이 내용은 [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]과 직접 연결된다.

### 3. 서버 도구 설치와 Spring Boot 실행

`wget`, `curl`, `tar`, `zip`, `apt`, alias, Java 실행 준비를 거쳐 Maven으로 Spring Boot `.jar`를 만들고 Linux에서 실행하는 흐름이 등장한다. 여기서부터 Linux는 단순 명령어 연습이 아니라 [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]을 위한 배포 환경이 된다.

### 4. Docker 이미지, 컨테이너, 네트워크, 볼륨

후반부의 핵심은 [[entities/docker|Docker]]다. image/container의 차이, `docker exec`, `docker cp`, port mapping, Docker network, bind mount, volume, Docker Hub push/pull을 통해 실행 환경을 재현 가능하게 만드는 법을 배운다. 특히 `docker cp`로 한 번 복사하는 것과 bind mount/volume으로 연결·보존하는 것은 생명주기가 다르다.

### 5. Dockerfile, reverse proxy, Compose, GitHub 협업

`docker commit`은 컨테이너 상태를 임시 스냅샷처럼 이미지화하는 방식이고, Dockerfile은 같은 이미지를 반복해서 만들 수 있는 레시피다. nginx upstream/reverse proxy/load balancing을 거쳐 Docker Compose manifest로 MySQL+Spring Boot 같은 다중 컨테이너 구성을 선언한다. 마지막 GitHub/SourceTree/branch/PR/conflict 학습은 이후 CI/CD에서 자동 배포의 입력이 되는 협업 흐름이다.

## 헷갈린 점 / 질문

- Linux 명령어는 각각 따로 외우기보다 “서버에 접속 → 파일 배치 → 권한 확인 → 프로세스 실행 → 포트/방화벽 확인”의 배포 흐름 안에서 묶어야 한다.
- `docker commit`은 빠른 실습에는 편하지만 재현성이 약하고, Dockerfile은 팀원이 같은 이미지를 다시 만들 수 있게 하는 기록이다. 비교는 [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]] 참고.
- `docker cp`, bind mount, volume은 모두 파일과 관련되지만, 복사/연결/보존의 책임이 다르다. 비교는 [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]] 참고.
- `git fetch`, `pull`, `clone`은 모두 원격 저장소와 관련되지만, 언제 로컬 작업 디렉터리에 반영되는지가 다르다. 비교는 [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]] 참고.

## 관련 페이지

- [[entities/linux|Linux]]
- [[entities/docker|Docker]]
- [[entities/maven|Maven]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]

## 출처

- `raw/Study/5. Linux/Linux 총정리/Linux 총정리.md`
