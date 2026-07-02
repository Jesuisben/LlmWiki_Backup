---
title: 2026-04-23 Linux 파일·디렉터리와 vi 편집기
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
status: growing
confidence: high
---

# 2026-04-23 Linux 파일·디렉터리와 vi 편집기

## 한 줄 요약

Linux 파일 시스템을 `tree`, `mkdir`, `touch`, `cat`, `cp`, `mv`, `find`로 직접 다루고, 서버에서 파일을 수정하기 위한 `vi` 편집기의 기본 모드와 저장 흐름을 익혔다.

## 배운 내용

- `tree`로 디렉터리 구조를 눈으로 확인했다.
- `pwd`, `cd`, `mkdir`, `mkdir -p`, `touch`, `cat`, `ls -l`, `ls -al`, `ls -lR`를 사용했다.
- 방송국/프로그램 이름을 예시로 `kbs/1night_2days`, `mbc/infinite_challenge`, `sbs/morning_wide` 같은 계층형 디렉터리를 만들었다.
- `cp`, `mv`로 복사와 이동을 구분했다.
- `find`로 이름, 타입, 실행 권한 조건에 맞는 파일을 찾았다.
- `vi`에서 명령 모드와 입력 모드를 구분하고, `:wq`로 저장 후 종료하는 흐름을 배웠다.
- 리다이렉션으로 명령 결과를 파일에 기록하는 기초를 맛봤다.

## 핵심 실습 흐름

```bash
sudo apt install -y tree
mkdir -p /home/broadcast/sbs/morning_wide
touch mbc/infinite_challenge/everyone.txt
cat kbs/1night_2days/hello.txt
ls -al
vi myfile.txt
```

## 왜 중요한가

Spring Boot나 React 프로젝트를 서버에 올릴 때도 결국 서버 안에서는 파일을 만들고, 옮기고, 찾고, 설정 파일을 수정한다. IDE 없이 터미널에서 작업하는 감각은 이후 [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]과 Docker 실습의 바탕이 된다.

## 헷갈린 점 / 질문

- `mkdir a/b`는 중간 디렉터리 `a`가 없으면 실패하지만, `mkdir -p a/b`는 필요한 중간 경로를 함께 만든다.
- `touch`는 빈 파일 생성에도 쓰지만, 기존 파일의 수정 시각을 바꾸는 명령이기도 하다.
- `vi`에서 글자가 안 써지면 입력 모드가 아닐 수 있다. `i`로 입력 모드에 들어가고 `Esc`로 명령 모드로 나온다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치, SSH 접속, 기본 CLI]]

## 출처

- `raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md`
