---
title: Linux 패키지·다운로드·압축
created: 2026-07-02
updated: 2026-07-13
type: concept
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux 패키지·다운로드·압축

## 정의

Linux에서 패키지 설치, 파일 다운로드, 압축 해제는 서버에 필요한 도구와 실행 파일을 준비하는 기본 작업이다.

## 왜 중요한가

Spring Boot jar 실행, Maven 설치, Docker 설치, Java tar.gz 배치처럼 서버 배포는 “필요한 것을 서버에 가져오고 풀고 실행 가능하게 만드는” 과정이다.

## 핵심 설명

- `apt`: Ubuntu의 패키지 관리 도구.
- `wget`: URL에서 파일 다운로드.
- `curl -L -o`: redirect를 따라가며 지정한 이름으로 다운로드.
- `tar -xzvf`: gzip으로 압축된 tar 파일 해제.
- `zip`/`unzip`: zip 파일 압축/해제.
- `chown`: 파일/디렉터리 소유권 변경.

## 예시

```bash
sudo apt install -y tree
sudo apt install -y openssh-server

mkdir -p ~/downloads/wgettest
cd ~/downloads/wgettest
wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf v9.1.0000.tar.gz

mkdir -p ~/downloads/curltest
cd ~/downloads/curltest
curl -L -o vim.tar.gz https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf vim.tar.gz
```

## 자주 헷갈리는 점

- `wget`/`curl`은 파일을 가져오는 도구이고, `apt install`은 패키지 설치 도구다.
- `tar.gz`는 “묶기 + gzip 압축”으로 이해하면 된다.
- Windows에서 가져온 파일이 Linux에서 실행되지 않으면 권한 문제뿐 아니라 줄바꿈(CRLF/LF) 문제도 의심해야 한다.

## 관련 개념

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[entities/maven|Maven]]

## 최신 원본 대조

2026-04-27의 `wget`/`curl` 다운로드, `tar -xzvf`, `zip -r`, alias와 `.bashrc` 실습을 기준으로 보강했다. 다운로드 도구와 설치 도구를 혼동하지 않고, alias는 shell 종료 후 사라져 `source` 또는 `.bashrc` 반영이 필요함을 남긴다.

## 출처

- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md`
