---
title: 2026-04-22 Linux 설치, SSH 접속, 기본 CLI
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
status: growing
confidence: high
---

# 2026-04-22 Linux 설치, SSH 접속, 기본 CLI

## 한 줄 요약

Windows 개발 환경에서 벗어나 VirtualBox Ubuntu VM을 만들고, `openssh-server`와 MobaXterm으로 원격 접속하는 서버 학습의 출발점이다.

## 배운 내용

- Ubuntu ISO, VirtualBox, MobaXterm을 설치하고 `Broadcast`, `Librarian` 같은 가상 머신을 만들었다.
- VM 계정을 만들고 메모리/CPU/디스크를 지정한 뒤 Ubuntu Server를 설치했다.
- `sudo apt install openssh-server`, `systemctl start/status ssh`로 SSH 서버를 준비했다.
- VirtualBox 네트워크를 NAT에서 브리지 어댑터로 바꾸고 `ip addr`로 접속 IP를 확인했다.
- MobaXterm에서 SSH session을 만들 때 remote host, username, port 22를 지정했다.
- 프롬프트의 `$`는 일반 사용자, `#`는 root/관리자 상태라는 점을 구분했다.
- `apt`를 Ubuntu의 패키지 설치 도구로 이해하고, npm처럼 필요한 도구를 설치하는 역할로 연결했다.

## 핵심 개념

- [[entities/linux|Linux]]: 서버 운영체제 학습의 기반.
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]: 이후 명령어·경로·파일 조작으로 이어지는 출발점.
- SSH: 원격 서버에 안전하게 접속하는 프로토콜.
- `sudo`: 일반 사용자가 관리자 권한으로 명령을 실행하는 방식.

## 실습 / 예제

```bash
sudo apt install openssh-server
sudo systemctl start ssh
sudo systemctl status ssh
sudo poweroff
ip addr
```

수업에서는 `active (running)` 상태를 확인한 뒤 VM을 끄고 브리지 모드로 바꾸었다. 이 흐름은 이후 EC2 SSH 접속, Linux 서버 배포, Docker 서버 운영으로 그대로 이어진다.

## 헷갈린 점 / 질문

- `sudo`로 시작하는 명령은 “명령어 이름”이 아니라 관리자 권한으로 뒤 명령을 실행하겠다는 의미다.
- `apt install`은 프로그램을 “다운로드만” 하는 것이 아니라 Ubuntu 패키지 저장소에서 설치까지 수행한다.
- 브리지 모드는 VM이 같은 네트워크의 별도 컴퓨터처럼 IP를 받게 하므로 MobaXterm 접속 실습에 필요했다.
- `ip addr` 출력에서 `lo`는 localhost이고, 실제 접속 대상 IP는 보통 `enp0s3` 같은 네트워크 인터페이스의 `inet` 값이다.

## 관련 페이지

- [[summaries/2026-04-23-linux-files-vi|2026-04-23 Linux 파일·디렉터리와 vi 편집기]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[entities/linux|Linux]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf`
