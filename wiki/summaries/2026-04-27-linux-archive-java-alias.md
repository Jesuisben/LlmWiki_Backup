---
title: 2026-04-27 Linux 압축, 다운로드, Java 실행 준비
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# 2026-04-27 Linux 압축, 다운로드, Java 실행 준비

## 한 줄 요약

`wget`, `curl`, `tar`, `zip`, `chown`, `alias`를 사용해 Linux 서버에 파일을 가져오고 압축을 다루며 Java 실행 환경으로 이어진 날이다.

## 배운 내용

- `wget`과 `curl -L -o`로 외부 URL의 tar.gz 파일을 다운로드했다.
- `tar -xzvf`로 `.tar.gz` 압축을 풀고, `zip`/`unzip`으로 zip 파일을 다뤘다.
- Windows에서 드래그 앤 드롭한 파일이 권한 문제로 복사되지 않을 수 있음을 확인했다.
- `sudo chown -R 사용자:그룹 경로`로 폴더 소유권을 바꾸어 일반 사용자가 파일을 넣을 수 있게 했다.
- `rm`, `rm -r`, `rm -rf`와 alias를 학습하며 위험한 명령을 더 안전하게 쓰는 감각을 배웠다.
- Java 설치 파일이 보통 tar.gz 형태로 제공된다는 점을 서버 설치 흐름과 연결했다.

## 핵심 개념

- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- `wget`: URL에서 파일을 내려받는 명령.
- `curl`: 요청/다운로드를 더 유연하게 제어하는 명령.
- `tar`: Linux에서 자주 쓰는 묶음/압축 해제 도구.

## 실습 / 예제

```bash
mkdir -p ~/downloads/wgettest
cd ~/downloads/wgettest
wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf v9.1.0000.tar.gz

mkdir -p ~/downloads/curltest
cd ~/downloads/curltest
curl -L -o vim.tar.gz https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf vim.tar.gz

sudo chown -R broadcast:broadcast /home/broadcast/downloads/fromwindows/
alias rm='rm -i'
```

## 헷갈린 점 / 질문

- `wget`은 파일명을 서버가 주는 이름으로 저장하는 경우가 많고, `curl -o`는 저장 파일명을 직접 지정한다.
- `tar -xzvf`는 옵션 네 글자의 조합이다. `x`는 풀기, `z`는 gzip, `v`는 과정 출력, `f`는 파일 지정이다.
- 권한이 없어서 파일 복사가 안 되는 문제는 “명령어가 틀림”이 아니라 owner/group/permission 문제일 수 있다.

## 관련 페이지

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문]]
- [[entities/maven|Maven]]
- [[entities/linux|Linux]]

## 출처

- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
