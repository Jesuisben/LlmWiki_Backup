---
title: 2026-04-23 Linux 파일·디렉터리와 vi 편집기
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# 2026-04-23 Linux 파일·디렉터리와 vi 편집기

## 한 줄 요약

Linux의 디렉터리 트리, 경로, 파일 생성·복사·이동·검색·삭제, `vi` 편집까지 서버 파일 시스템을 직접 다룬 날이다.

## 배운 내용

- `tree / -L 1`로 Linux 최상위 디렉터리 구조를 확인했다.
- `pwd`, `cd`, `mkdir`, `rmdir`, `touch`, `ls`, `cat`, `echo > 파일`로 파일과 폴더를 조작했다.
- 절대경로(`/home/...`)와 상대경로, 홈 디렉터리(`~`), tab 자동완성을 구분했다.
- `cp`, `mv`, `rm`, `rm -r`, `rm -rf`로 복사·이동·삭제를 실습했다.
- `head`, `tail`, `find`로 파일 일부나 파일 위치를 확인했다.
- `vi`의 명령 모드/입력 모드/저장 종료 흐름을 익혔다.

## 핵심 개념

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]: 서버에서 파일을 배치하고 확인하는 기본기.
- `>` redirection: 터미널 출력 방향을 파일로 바꾸는 기호.
- `.`/`..`: 현재 디렉터리와 상위 디렉터리.
- `vi`: 서버에 GUI 편집기가 없을 때 파일을 직접 수정하는 기본 편집기.

## 실습 / 예제

```bash
sudo apt install -y tree
tree / -L 1
pwd
cd
mkdir /home/broadcast/mbc
echo "This is a test" > kbs/1night_2days/hello.txt
cat kbs/1night_2days/hello.txt
touch mbc/infinite_challenge/everyone.txt
ls -al
cp java.txt java.bak
mv python.txt python.bak
find . -name "*.txt"
vi index.html
```

## 헷갈린 점 / 질문

- `mkdir`는 디렉터리 생성이고 `touch`는 빈 파일 생성이다.
- `cat`은 파일 내용을 보여 주는 명령이지 파일을 “여는 프로그램”은 아니다.
- `rm -rf`는 강력한 삭제 명령이므로 학습 예제에서도 대상 경로를 반드시 확인해야 한다.
- `vi`에서 글자를 입력하려면 먼저 `i`로 입력 모드에 들어가야 하고, 저장/종료는 `Esc` 후 `:wq`처럼 명령 모드에서 한다.

## 관련 페이지

- [[summaries/2026-04-24-linux-users-permissions|2026-04-24 Linux 사용자, 그룹, 권한]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[entities/linux|Linux]]

## 출처

- `raw/Study/5. Linux/2026.04.23(목)/2026.04.23(목).md`
