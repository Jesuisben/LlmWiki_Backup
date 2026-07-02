---
title: Linux 패키지·다운로드·압축
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
status: growing
confidence: high
---

# Linux 패키지·다운로드·압축

## 정의

Linux에서 서버 작업을 하려면 필요한 프로그램을 패키지 관리자로 설치하고, 외부 파일을 다운로드하고, 압축 파일을 풀거나 묶을 수 있어야 한다. Ubuntu 수업에서는 `apt`, `wget`, `curl`, `tar`, `zip`을 중심으로 배웠다.

## 수업에서 나온 도구

| 도구 | 역할 | 수업 맥락 |
|---|---|---|
| `apt` | Ubuntu 패키지 설치/관리 | SSH 서버, Git, zip, Maven 설치 |
| `wget` | URL에서 파일 다운로드 | Vim `.tar.gz` 파일 내려받기 |
| `curl` | URL 요청/다운로드 | 다른 방식으로 압축 파일 받기 |
| `tar` | `.tar.gz` 압축 해제/묶기 | Linux용 Java/Vim 파일 풀기 |
| `zip` | zip 압축/해제 | 실습 디렉터리 압축 |

## 핵심 예제

```bash
sudo apt install -y openssh-server
sudo apt install -y zip
mkdir -p ~/downloads/wgettest
cd ~/downloads/wgettest
wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf v9.1.0000.tar.gz
```

## 왜 중요한가

Linux 서버는 필요한 도구가 처음부터 모두 설치되어 있지 않다. Java, Maven, Docker, Git 같은 도구를 설치하고, 배포 파일을 내려받아 압축을 풀 수 있어야 서버 환경을 준비할 수 있다.

## 자주 헷갈리는 점

- `apt install`은 운영체제 패키지 설치이고, `wget`/`curl`은 파일 다운로드다.
- `.tar.gz`는 압축 파일 형식이고 실행 파일이 아니다. 압축 해제 후 내부 파일을 확인해야 한다.
- `rm -rf`는 편리하지만 매우 위험하다. 다운로드/압축 실습 중 임시 폴더를 지울 때 경로를 특히 조심해야 한다.

## 관련 수업

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]
- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27 Linux 압축, 다운로드, Java 실행 준비]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
