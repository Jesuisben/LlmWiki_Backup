---
title: 2026-04-27 Linux 압축, 다운로드, Java 실행 준비
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, java, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
status: growing
confidence: high
---

# 2026-04-27 Linux 압축, 다운로드, Java 실행 준비

## 한 줄 요약

Linux에서 `wget`, `curl`, `tar`, `zip`, `rm`, `alias`를 사용해 외부 파일을 내려받고 압축을 풀며, Java 실행 파일과 서버 작업을 준비하는 흐름을 배웠다.

## 배운 내용

- Linux에서 Java 설치 파일은 보통 `.tar.gz` 같은 압축 파일로 제공될 수 있음을 확인했다.
- `wget`과 `curl`은 설치가 아니라 외부 URL의 파일을 내려받는 도구다.
- `tar -xzvf`로 `.tar.gz` 파일을 압축 해제했다.
- Windows에서 받은 파일을 Linux로 옮긴 뒤 권한과 소유권을 확인했다.
- `zip` 패키지를 설치하고 디렉터리를 압축·해제하는 흐름을 실습했다.
- `rm`, `rm -rf`로 파일/디렉터리를 삭제할 때의 위험성을 배웠다.
- 자주 쓰는 긴 명령을 `alias`로 줄이고, `.sh` 파일로 관리하는 방식을 배웠다.
- Java 테스트를 통해 Linux 서버에서 Java 프로그램 실행으로 이어질 준비를 했다.

## 핵심 실습 흐름

```bash
mkdir -p ~/downloads/wgettest
cd ~/downloads/wgettest
wget https://github.com/vim/vim/archive/refs/tags/v9.1.0000.tar.gz
tar -xzvf v9.1.0000.tar.gz
sudo apt install -y zip
```

## 왜 중요한가

서버 배포에서는 Git clone 외에도 릴리스 파일, 압축 파일, JDK, 설정 파일을 내려받아 배치하는 일이 많다. 이 날 배운 다운로드·압축·삭제·별칭은 이후 [[concepts/linux-spring-boot-server-deploy|Spring Boot 서버 실행]]과 [[concepts/docker-image-container|Docker 이미지와 컨테이너]] 실습으로 이어진다.

## 헷갈린 점 / 질문

- `wget`/`curl`은 패키지를 “설치”하는 명령이 아니라 URL에서 파일을 “가져오는” 명령이다.
- `rm -rf`는 확인 없이 재귀 삭제할 수 있어 실수하면 복구가 어렵다. 실습에서는 경로를 반드시 확인해야 한다.
- alias는 현재 셸에서만 살아 있을 수 있으므로, 재접속 후에도 쓰려면 설정 파일에 넣어야 한다.

## 관련 페이지

- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[entities/java|Java]]

## 출처

- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
