---
title: Docker 설치와 권한 설정
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [linux, docker, backend]
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

Docker 설치와 권한 설정은 Ubuntu 서버에 Docker Engine을 설치하고 일반 사용자도 `docker` 명령을 실행할 수 있게 준비하는 과정이다.

## 왜 중요한가

Docker는 Linux 배포 실습의 핵심 도구지만, daemon과 socket 권한을 사용하므로 설치 직후 일반 사용자에게 `permission denied`가 날 수 있다. 권한 문제를 해결해야 컨테이너 실행·Compose 실습이 가능하다.

## 핵심 설명

- 교육자료의 설치 스크립트를 Linux 서버로 옮겼다.
- Windows에서 작성된 스크립트는 CRLF 줄바꿈 때문에 바로 실행이 안 될 수 있어 `dos2unix`를 사용했다.
- `chmod +x`로 실행 권한을 부여하고 root 권한으로 설치했다.
- Docker daemon 상태를 `systemctl status docker`로 확인했다.
- 일반 사용자를 `docker` 그룹에 추가한 뒤 재로그인해 권한을 반영했다.

## 예시

```bash
sudo cp docker_setup.sh.txt /root/docker_setup.sh
sudo su -
apt update
apt install -y dos2unix
dos2unix docker_setup.sh
chmod +x docker_setup.sh
./docker_setup.sh
systemctl status docker
usermod -aG docker broadcast
```

## 자주 헷갈리는 점

- `docker` 명령 권한은 단순 파일 실행 권한이 아니라 Docker socket 접근 권한과 관련된다.
- 그룹 추가 후 현재 shell에 바로 반영되지 않을 수 있으므로 logout/login이 필요하다.
- Docker를 root로만 쓰면 당장은 편하지만, 학습/운영에서는 권한 구조를 이해하는 것이 중요하다.

## 관련 개념

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/docker|Docker]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
