---
title: Linux 총정리
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, docker, github, backend, study-log]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/Study/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/Study/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md
  - raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
status: growing
confidence: high
---

# Linux 총정리

## 한 줄 요약

Linux 총정리는 “서버에 접속해 파일을 다루고, Spring Boot를 실행하고, Docker로 실행 환경을 고정하며, GitHub 협업으로 배포 흐름을 이어 가는” 5과목 전체 복습 허브다.

## 배운 내용

1. 서버 접속 기반
   - VirtualBox Ubuntu VM 생성, SSH 서버 설치, MobaXterm 접속.
   - `sudo`, `$`/`#`, `apt`, `systemctl`, `ip addr`의 의미.
2. 파일 시스템과 편집
   - `pwd`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm`, `find`, `vi`.
   - 절대경로/상대경로, 홈 디렉터리, redirection.
3. 사용자·그룹·권한
   - `ls -l` 권한 문자열, owner/group/others, `/etc/passwd`, `/etc/shadow`, `/etc/group`.
   - `useradd`, `passwd`, `groupadd`, `usermod`, `chown`.
4. 서버 실행과 배포 기초
   - `wget`, `curl`, `tar`, `zip`, Maven package, `java -jar`, 방화벽/포트 확인.
5. Docker
   - image/container, `exec`, `cp`, network, bind mount, volume, commit, Dockerfile, reverse proxy, Compose.
6. GitHub 협업
   - Git Bash/SourceTree, branch, PR, merge, pull, conflict.

## 핵심 개념

- [[entities/linux|Linux]]
- [[entities/docker|Docker]]
- [[entities/git|Git]], [[entities/github|GitHub]], [[entities/source-tree|SourceTree]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]

## 실습 / 예제

Linux 과정의 실습 흐름은 단순 명령 암기가 아니라 다음 배포 시나리오로 이어진다.

```text
Windows/IntelliJ에서 만든 Spring Boot 프로젝트
  → GitHub에 push
  → Linux 서버에서 clone
  → Maven으로 jar 패키징
  → java -jar 또는 Docker container로 실행
  → nginx/reverse proxy/Compose로 다중 컨테이너 운영
  → GitHub branch/PR로 팀 협업
```

## 헷갈린 점 / 질문

- Linux 명령은 “서버의 파일/프로세스/권한을 직접 조작한다”는 점에서 IDE 안의 실행 버튼보다 책임 범위가 넓다.
- Docker는 Linux를 대체하는 것이 아니라 Linux 위에서 실행 환경을 컨테이너 단위로 격리·재현하는 도구다.
- GitHub 협업은 Linux와 별개처럼 보이지만, 실제 배포에서는 서버가 GitHub에서 코드를 가져오거나 CI/CD가 GitHub push를 트리거로 실행된다.
- 실습용 비밀번호, IP, token은 wiki에 그대로 보존하지 않고 `{PASSWORD}`, `{IP}`처럼 역할 중심으로 일반화한다.

## 관련 페이지

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]
- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문]]
- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose와 다중 컨테이너 실행]]
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결]]

## 출처

- `raw/Study/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/Study/5. Linux` 날짜별 MD 10개
