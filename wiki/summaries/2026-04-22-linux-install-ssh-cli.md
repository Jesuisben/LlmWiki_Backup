---
title: 2026-04-22 Linux 설치, SSH 접속, 기본 CLI
date: 2026-04-22
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
status: growing
confidence: high
---

# 2026-04-22 Linux 설치, SSH 접속, 기본 CLI

## 한 줄 요약

Linux 과정 첫날로, VirtualBox에 Ubuntu를 설치하고 MobaXterm으로 SSH 접속한 뒤 파일·디렉터리·프롬프트·절대/상대 경로의 기본 감각을 잡았다.

## 커리큘럼 위치

[[summaries/2026-04-22-product-repository-pageable-search|Spring/React 상품 목록 검색]]까지 웹 애플리케이션 구현을 배운 뒤, 서버 운영과 배포를 이해하기 위해 [[entities/linux|Linux]] 환경으로 넘어간 시작점이다. 이후 [[concepts/linux-cli-files|Linux CLI와 파일 시스템]] 학습, Docker, GitHub 협업으로 이어진다.

## 배운 내용

- VirtualBox는 Windows 위에 별도 운영체제인 Ubuntu Linux를 올리는 가상머신 도구로 사용했다.
- MobaXterm은 Windows에서 Linux 서버에 SSH로 접속하는 터미널 역할을 했다.
- `sudo apt install openssh-server`, `sudo systemctl start ssh`, `sudo systemctl status ssh`로 SSH 서버를 설치·시작·확인했다.
- `ip addr`로 가상머신의 IP를 찾고, 브릿지 네트워크 설정 후 MobaXterm 접속 아이콘을 만들었다.
- Linux 프롬프트의 사용자명, 호스트명, 현재 위치, `$`/`#`의 의미를 확인했다.
- `/`, `/home`, 절대 경로, 상대 경로, 파일과 디렉터리의 계층 구조를 배웠다.

## 핵심 실습 흐름

```bash
sudo apt install -y openssh-server
sudo systemctl start ssh
sudo systemctl status ssh
ip addr
sudo ufw allow 22
```

이 흐름은 “가상머신을 설치한다 → SSH 서비스를 켠다 → IP를 확인한다 → 방화벽/접속 설정을 맞춘다 → 원격 터미널에서 명령어를 실행한다”는 서버 접속의 기본 절차다.

## 헷갈린 점 / 질문

- `apt install git`처럼 패키지를 설치하는 명령과, `git` 자체 명령은 역할이 다르다. 전자는 운영체제 패키지 관리자이고 후자는 버전 관리 도구다.
- `$` 프롬프트는 일반 사용자, `#` 프롬프트는 root/관리자 권한을 뜻한다. 명령어 예시에서 `#`를 주석처럼 볼 수도 있지만, Linux 프롬프트 문맥에서는 권한 상태 표시다.
- IP 주소는 Windows PC 주소가 아니라 가상머신 Ubuntu의 네트워크 주소를 찾아야 MobaXterm 접속이 된다.

## 관련 페이지

- [[entities/linux|Linux]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
