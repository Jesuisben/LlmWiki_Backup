---
title: Linux 패키지·다운로드·압축
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# Linux 패키지·다운로드·압축

## 정의

Linux 서버 작업에서는 필요한 프로그램을 `apt`로 설치하고, 외부 파일을 `wget`/`curl`로 내려받고, `tar`/`zip`/`unzip`으로 압축 파일을 다룰 수 있어야 한다.

## 수업에서 나온 도구

| 도구 | 역할 | 수업 맥락 |
|---|---|---|
| `apt` | Ubuntu 패키지 설치/관리 | SSH, tree, zip, JDK, Maven, Docker 준비 패키지 설치 |
| `wget` | URL에서 파일 다운로드 | Vim `.tar.gz`, JDBC driver 다운로드 |
| `curl` | URL 요청/다운로드 | `-L -o`로 redirect 추적 및 파일명 지정 다운로드 |
| `tar` | `.tar.gz` 압축 해제 | Linux용 압축 파일 풀기 |
| `zip`/`unzip` | zip 압축/해제 | 실습 디렉터리 압축/해제 |
| `rm`/`rm -rf` | 파일/디렉터리 삭제 | 다운로드 실습 정리 |
| `alias` | 명령어 별칭 | `head3`, `tail5`, `.bashrc` 지속 설정 |

## 핵심 예제

```bash
sudo apt update
sudo apt install -y tree zip openjdk-17-jdk
mkdir -p ~/downloads/wgettest
cd ~/downloads/wgettest
wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf v9.1.0000.tar.gz
curl -L -o vim.tar.gz https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
zip -r morning_garden.zip .
unzip morning_garden.zip
rm -rf vim-9.1.0000/
alias head3='head -n 3 java.txt'
cat alias_test.sh >> .bashrc
```

## Windows에서 파일을 옮길 때의 권한 문제

수업에서는 `sudo mkdir -p ~/downloads/fromwindows`로 만든 디렉터리에 MobaXterm drag-and-drop이 실패했다. 원인은 디렉터리 owner가 root였기 때문이다.

```bash
sudo chown -R broadcast:broadcast /home/broadcast/downloads/fromwindows/
```

이후 일반 사용자 `broadcast`가 파일을 넣을 수 있게 되었다.

## 왜 중요한가

Linux 서버는 필요한 도구가 처음부터 모두 설치되어 있지 않다. 배포 파일, Docker 설치 스크립트, Java/JDBC/Maven 같은 도구를 준비하려면 패키지·다운로드·압축 흐름을 알아야 한다.

## 자주 헷갈리는 점

- `apt install`은 설치이고, `wget`/`curl`은 다운로드다.
- `.tar.gz`는 압축 파일이지 실행 파일이 아니다.
- `curl -L`은 redirect를 따라가고, `-o`는 저장할 파일 이름을 정한다.
- `rm -rf`는 매우 위험하다. 특히 `/`, `~`, 변수 경로와 함께 쓸 때는 경로를 확인해야 한다.
- alias는 현재 shell에만 유지된다. 새 접속에서도 쓰려면 `.bashrc`에 넣어야 한다.

## 관련 수업

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]
- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27 Linux 압축, 다운로드, Java 실행 준비]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — apt/systemctl/ufw 개념
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — p.153~170 다운로드/압축/alias/Java 실습
