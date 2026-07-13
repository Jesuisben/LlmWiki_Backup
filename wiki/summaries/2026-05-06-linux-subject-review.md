---
title: Linux 총정리
created: 2026-07-06
updated: 2026-07-14
type: summary
tags: [linux, docker, github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
status: growing
confidence: high
---

# Linux 총정리

## 한 줄 요약

5과목은 Ubuntu VM/SSH/CLI에서 시작해 권한·파일·Java/Spring Boot 서버 실행을 익히고, Docker/Compose로 실행 환경을 재현한 뒤 Git/GitHub/PR 협업으로 마무리하는 운영·협업 과정이다.

## 전체 흐름

1. [[summaries/2026-04-22-linux-install-ssh-cli|04-22]]: Ubuntu VM, VirtualBox, MobaXterm, SSH, apt, prompt, 디렉터리 구조.
2. [[summaries/2026-04-23-linux-files-vi|04-23]]: 파일/디렉터리 조작, tree, cp/mv/find, vi, redirection.
3. [[summaries/2026-04-24-linux-users-permissions|04-24]]: 사용자·그룹·권한, `/etc/passwd`, `/etc/shadow`, `/etc/group`.
4. [[summaries/2026-04-27-linux-archive-java-alias|04-27]]: wget/curl/tar/zip, alias, JDK/JDBC, Java 실행.
5. [[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]]: GitHub clone, Maven package, `java -jar`, Docker 입문.
6. [[summaries/2026-04-29-docker-network-volume-image|04-29]]: Docker network, MariaDB/Redmine, bind mount/volume, commit.
7. [[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30]]: Dockerfile, Spring Boot container, nginx reverse proxy/load balancing.
8. [[summaries/2026-05-01-docker-compose|05-01]]: Docker Compose manifest, Docker Desktop, 다중 컨테이너 실행.
9. [[summaries/2026-05-04-git-github-sourcetree|05-04]] ~ [[summaries/2026-05-06-github-branch-pr-conflict|05-06]]: Git Bash, SourceTree, clone/pull/push, branch, PR, merge, conflict.

## 기능 흐름으로 다시 보기

- **서버에 들어간다:** VirtualBox의 Ubuntu VM에 SSH 서버를 설치하고 MobaXterm으로 접속했다. 브리지 네트워크, VM IP, SSH 서비스와 UFW 22번 허용은 “어디에 접속하는가”를 분리해 이해하는 출발점이다.
- **서버의 파일을 다룬다:** `tree`, `mkdir -p`, `cp`, `mv`, `find`, `vi`, `>`/`>>`를 방송사 디렉터리와 텍스트 파일 실습에 적용했다. 이후 배포 파일, 설정 파일, 로그를 CLI에서 다루는 기반이다.
- **누가 실행·수정할 수 있는지 결정한다:** `ls -l`의 owner/group/others, `/etc/passwd`·`/etc/shadow`·`/etc/group`, `chmod 644/600`, `chown`, `chgrp`을 실습했다. `Permission denied`는 코드보다 파일·디렉터리 권한이 원인일 수 있음을 확인했다.
- **앱을 직접 실행한다:** GitHub clone → 포트 확인/허용 → Maven package → `java -jar`로 Spring Boot jar를 VM에서 실행했다. 80→9000 전환과 UFW는 앱 포트와 외부 진입 포트를 구별하게 한다.
- **실행 환경을 재현한다:** MariaDB+Redmine, Spring Boot+MySQL까지 image/container/network/mount를 확장했다. `docker exec/cp`는 일회성 조작, bind mount/volume은 지속성, Dockerfile/Compose는 재현성을 담당한다.
- **변경을 협업한다:** `status → add → commit → push/pull`을 먼저 확인하고 branch → PR → merge → 로컬 최신화 → conflict/rebase를 실습했다. SourceTree와 IntelliJ UI도 같은 Git 상태 전이를 보여 주는 도구다.

## 헷갈리기 쉬운 연결

- VM, SSH 클라이언트, Linux OS, Docker container는 모두 다른 층위다.
- `>`는 기존 파일을 덮어쓰고 `>>`는 이어 쓴다. `docker cp`도 연결이 아니라 한 번 복사다.
- 파일 권한 문제와 VM/UFW/iptables/Docker 포트 문제는 코드 오류처럼 보일 수 있지만 운영 환경 문제다.
- Dockerfile은 이미지 생성, Compose는 여러 컨테이너 실행 구성을 담당한다.
- clone/pull/fetch는 모두 원격과 관련 있지만 결과가 다르다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]], [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]], [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]] — 정적 응답과 reverse proxy 역할을 Spring Boot·Docker 배포 흐름에 연결
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]], [[concepts/docker-network-volume|Docker 네트워크와 볼륨]], [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]], [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]], [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]

## 출처

- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux` 날짜별 MD 10개
