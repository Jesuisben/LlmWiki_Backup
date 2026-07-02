---
title: 2026-04-22 Linux 설치, SSH 접속, 기본 CLI
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/리눅스 실습하기.md
status: growing
confidence: high
---

# 2026-04-22 Linux 설치, SSH 접속, 기본 CLI

## 한 줄 요약

VirtualBox에 Ubuntu Server VM을 만들고 SSH/MobaXterm으로 접속한 뒤, Linux 프롬프트·경로·파일 시스템의 기본 감각을 배운 Linux 과정 첫날이다.

## 배운 내용

- `Linux 실습(MobaXterm, VirtualBox, 실습).pdf` 기준으로 Ubuntu Server ISO, VirtualBox, MobaXterm을 준비했다.
- `Broadcast`, `Librarian` 같은 VM을 만들고 사용자 계정과 암호를 설정했다.
- `openssh-server`를 설치하고 `systemctl start/status ssh`로 SSH 서비스를 켰다.
- VirtualBox 네트워크를 NAT/브리지/포트 포워딩 관점에서 확인했다. 수업 메모에서는 브리지 모드로 바꾼 뒤 `ip addr`의 `enp0s3` 항목에서 IPv4 주소를 확인했다.
- MobaXterm에서 SSH Session을 만들 때 `Remote host`, `Username`, `Port 22`를 입력했다.
- Linux 이론 교안의 Prompt 설명을 바탕으로 `사용자@호스트:현재경로$` 구조와 `$`/`#`의 차이를 봤다.
- 절대 경로(`/home/broadcast/...`)와 상대 경로(`./`, `../`, `~/`)를 문제풀이로 익혔다.

## 핵심 실습 / 예제

```bash
sudo apt install -y openssh-server
sudo systemctl start ssh
sudo systemctl status ssh
sudo poweroff
ip addr
pwd
```

`sudo`는 “관리자 권한으로 이번 명령을 실행한다”는 의미로 처음 등장했다. `systemctl`은 SSH 같은 백그라운드 서비스의 시작/중지/상태 확인에 쓰였다.

## 왜 이 흐름으로 배웠는가

Linux는 이후 Spring Boot `.jar` 실행, Apache/Nginx 웹서버, Docker, GitHub 협업 실습의 실행 환경이다. 그래서 첫날에는 먼저 “리눅스 서버에 접속할 수 있는 상태”를 만드는 것이 목표였다.

## 헷갈린 점 / 질문

- `localhost`는 내 컴퓨터 자신을 가리키고, VM의 브리지 IP는 같은 네트워크에서 접근 가능한 VM 주소다.
- NAT 포트 포워딩은 호스트 포트를 게스트 포트로 넘기는 방식이고, 브리지 모드는 VM이 네트워크에 별도 PC처럼 붙는 방식이다.
- `$`는 일반 사용자, `#`는 root/관리자 prompt로 이해하면 된다.
- 절대 경로는 `/`에서 시작하고, 상대 경로는 현재 위치를 기준으로 해석된다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[entities/linux|Linux]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — Ubuntu/VirtualBox/MobaXterm, NAT/bridge/port forwarding, 디렉터리 구조 실습
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — prompt, 절대/상대 경로, apt/systemctl 개념
- `raw/Study/5. Linux/교육 자료/리눅스 실습하기.md`
