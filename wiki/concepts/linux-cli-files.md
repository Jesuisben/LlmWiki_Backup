---
title: Linux CLI와 파일 시스템
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux]
sources:
  - raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
status: growing
confidence: high
---

# Linux CLI와 파일 시스템

## 정의

Linux CLI(Command Line Interface)는 마우스 대신 명령어로 파일, 디렉터리, 프로세스, 네트워크, 패키지를 다루는 작업 방식이다. 파일 시스템은 `/` 루트에서 시작해 `/home`, `/etc`, 프로젝트 디렉터리처럼 계층적으로 구성된다.

## 왜 중요한가

Spring Boot나 React를 서버에 배포하면 IDE 화면이 아니라 터미널에서 파일을 만들고, 로그를 보고, 설정 파일을 수정해야 한다. 이 위키에서 Linux는 “서버 배포를 위한 운영체제 감각”을 익히는 단계다.

## 수업에서 배운 순서

1. VirtualBox에 Ubuntu를 설치했다.
2. SSH 서버를 켜고 MobaXterm으로 접속했다.
3. `pwd`, `cd`, `ls`로 현재 위치와 목록을 확인했다.
4. `mkdir`, `touch`, `cat`으로 디렉터리와 파일을 만들고 확인했다.
5. `cp`, `mv`, `find`로 복사·이동·검색을 실습했다.
6. `vi`로 서버 안에서 파일을 직접 편집했다.

## 핵심 명령어

```bash
pwd
cd /home/broadcast
ls -al
mkdir -p sbs/morning_wide
touch mbc/infinite_challenge/everyone.txt
cat kbs/1night_2days/hello.txt
cp source.txt target.txt
mv old.txt new.txt
find . -name "*.txt"
vi myfile.txt
```

## 자주 헷갈리는 점

- 절대 경로는 `/home/broadcast/...`처럼 `/`에서 시작한다. 상대 경로는 현재 위치를 기준으로 해석된다.
- `mkdir a/b`는 `a`가 없으면 실패하지만 `mkdir -p a/b`는 중간 디렉터리까지 만든다.
- `vi`는 입력 모드와 명령 모드가 나뉜다. 글 입력은 `i`, 저장 후 종료는 `Esc` → `:wq`다.
- `ls -al`에서 숨김 파일은 `.`으로 시작하는 파일이다. Git의 `.git`도 이 규칙을 따른다.

## 이후 학습과 연결

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]을 알아야 파일 수정/실행 오류를 해석할 수 있다.
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]은 서버에 필요한 도구와 파일을 준비하는 단계다.
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]도 결국 Linux 파일 시스템과 명령어 위에서 실행된다.

## 관련 수업

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]
- [[summaries/2026-04-23-linux-files-vi|2026-04-23 Linux 파일·디렉터리와 vi 편집기]]

## 출처

- `raw/Study/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`
- `raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md`
