---
title: Linux 총정리
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [linux, docker, github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
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

- 서버 접속: VM IP, SSH, MobaXterm, prompt를 이해해야 원격 서버 작업이 가능하다.
- 파일 준비: `wget/curl`, 압축 해제, vi, 권한 조정은 배포 파일을 서버에 올리는 기본기다.
- 앱 실행: Maven으로 jar를 만들고 Linux에서 `java -jar`로 실행하며 포트/방화벽을 확인한다.
- 컨테이너화: Docker image/container로 실행 환경을 재현하고 network/volume으로 DB·파일 지속성을 다룬다.
- 협업: GitHub branch/PR/merge/conflict로 팀 프로젝트 변경을 안전하게 합친다.

## 헷갈리기 쉬운 연결

- VM, SSH 클라이언트, Linux OS, Docker container는 모두 다른 층위다.
- 파일 권한 문제와 포트/방화벽 문제는 코드 오류처럼 보일 수 있지만 운영 환경 문제다.
- Dockerfile은 이미지 생성, Compose는 여러 컨테이너 실행 구성을 담당한다.
- clone/pull/fetch는 모두 원격과 관련 있지만 결과가 다르다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]], [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]], [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]], [[concepts/docker-network-volume|Docker 네트워크와 볼륨]], [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]], [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]

## 출처

- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux` 날짜별 MD 10개
