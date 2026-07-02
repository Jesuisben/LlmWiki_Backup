---
title: Docker 설치와 권한 설정
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
status: growing
confidence: high
---

# Docker 설치와 권한 설정

## 정의

Docker 설치와 권한 설정은 Ubuntu VM에서 Docker Engine을 설치하고, 일반 사용자도 `docker` 명령을 실행할 수 있게 `docker` 그룹에 추가하는 준비 과정이다.

## 수업 흐름

1. 교육자료의 `docker_setup.sh.txt`를 Linux 홈 디렉터리로 옮겼다.
2. root 권한으로 `/root/docker_setup.sh`에 복사했다.
3. Windows에서 만든 스크립트의 CRLF 줄바꿈 문제를 `dos2unix`로 변환했다.
4. 실행 권한을 부여하고 설치 스크립트를 실행했다.
5. `systemctl status docker`로 Docker daemon 상태를 확인했다.
6. 일반 사용자를 `docker` 그룹에 추가했다.
7. `permission denied`가 보이면 logout/login 후 다시 확인했다.

## 핵심 명령어

```bash
sudo cp docker_setup.sh.txt /root/docker_setup.sh
sudo su -
apt update
apt install dos2unix -y
dos2unix docker_setup.sh
chmod +x docker_setup.sh
./docker_setup.sh
docker container --help
systemctl status docker
exit
sudo usermod -aG docker $USER
groups $USER
logout
docker version
```

## 왜 중요한가

Docker 명령은 Docker daemon과 통신한다. 일반 사용자가 권한 없이 실행하면 `permission denied`가 날 수 있다. 설치와 권한 설정이 안정적으로 끝나야 이후 Apache/nginx/MySQL/Spring Boot 컨테이너 실습을 진행할 수 있다.

## 자주 헷갈리는 점

- `dos2unix`는 Windows CRLF 줄바꿈 때문에 shell script가 깨지는 문제를 해결한다.
- `chmod +x`는 스크립트 실행 권한을 준다.
- `usermod -aG docker $USER` 후에는 현재 로그인 세션에 바로 반영되지 않을 수 있어 재로그인이 필요하다.
- root로 계속 작업하기보다, 설치 후에는 일반 사용자 + docker 그룹으로 작업하는 편이 안전하다.

## 관련 페이지

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — Docker 설치/권한 설정
- `raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
