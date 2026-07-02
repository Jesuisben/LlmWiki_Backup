---
title: Linux
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [linux]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# Linux

## 무엇인가

Linux는 서버 운영체제로 많이 쓰이는 Unix 계열 운영체제다. 이 위키에서는 Spring/React로 만든 웹 애플리케이션을 실제 서버 환경에서 실행·배포하기 위해 배우는 운영체제 단계로 등장했다.

## 이 위키에서의 맥락

Java와 Spring Boot에서는 코드를 작성하고 실행하는 개발자 관점이 중심이었다. Linux 과정부터는 서버에 접속하고, 파일을 배치하고, 권한을 관리하고, 포트를 열고, 배포 산출물을 실행하는 운영 관점이 추가된다. 이후 Docker, GitHub 협업, AWS, CI/CD로 이어지는 기반이다.

## 학습 이력

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22]]: VirtualBox Ubuntu 설치, SSH 서버, MobaXterm 접속, 프롬프트와 경로.
- [[summaries/2026-04-23-linux-files-vi|2026-04-23]]: 파일/디렉터리 명령어, `vi`, 복사·이동·검색, redirection, `grep`, `diff`.
- [[summaries/2026-04-24-linux-users-permissions|2026-04-24]]: 사용자, 그룹, 권한, `/etc/passwd`, `/etc/shadow`, `/etc/group`, `chmod`, `chown`, `chgrp`.
- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27]]: 다운로드, 압축, 삭제, alias, Java 실행 준비, Apache/Nginx 웹서버.
- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]: Maven 설치, Spring Boot `.jar` 빌드/실행, Docker 입문.
- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29]]: Docker 네트워크, mount, 사용자 정의 이미지, Docker Hub.
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]]: Dockerfile, Spring Boot 컨테이너, reverse proxy/load balancing.
- [[summaries/2026-05-01-docker-compose|2026-05-01]]: Docker Compose, Docker Desktop/WSL2, 다중 컨테이너 구성.

## 핵심 기능 / 특징

- CLI 중심 작업: `cd`, `ls`, `mkdir`, `touch`, `cat`, `find`, `vi`.
- 사용자/권한 관리: owner/group/others, root, sudo, useradd, chmod/chown/chgrp.
- 서버 프로세스 관리: `systemctl`, UFW, 포트.
- 웹서버 운영: Apache/Nginx, `/var/www/html/`, reverse proxy.
- 배포 준비: Maven, Java, Docker, Git과 연결된다.

## 프로젝트/면접 관점

Linux를 “명령어 몇 개”로만 외우기보다, 웹 서비스를 서버에 올리기 위한 운영 환경으로 설명하면 좋다. 예를 들어 “Spring Boot jar를 Linux 서버에서 실행하고, 포트/방화벽/권한을 확인하며, Docker 컨테이너로 실행 환경을 재현할 수 있다”가 실무적인 설명이다.

## 관련 개념

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md`
- `raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/2026.04.29(수)/2026.04.29(수).md`
- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf`
