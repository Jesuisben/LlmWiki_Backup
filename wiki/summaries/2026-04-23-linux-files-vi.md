---
title: 2026-04-23 Linux 파일·디렉터리와 vi 편집기
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
status: growing
confidence: high
---

# 2026-04-23 Linux 파일·디렉터리와 vi 편집기

## 한 줄 요약

최상위 파일 시스템을 `tree`로 확인한 뒤 방송사 directory 구조에서 생성·복사·이동·검색을 반복하고, vi 3모드와 redirection·`grep`·`more`·`diff`로 텍스트 파일을 편집·조합·검증했다.

## 왜 이 흐름으로 배웠는가

04-22에는 VM에 접속하고 경로를 읽는 방법을 배웠다. 서버에서 설정·배포 파일을 다루려면 다음으로 **구조를 보고 → 대상을 만들고 → 복사·이동·검색하고 → 내용까지 편집·비교**할 수 있어야 한다. 그래서 이날은 한 번 만든 방송사 tree를 하루 종일 같은 artifact로 재사용하며 명령 하나가 파일 시스템 상태를 어떻게 바꾸는지 추적했다.

## 교시별 학습 전개

### 1교시: 최상위 구조와 방송사 directory tree

`tree` utility를 설치하고 `tree / -L 1`로 `/` 바로 아래의 `bin`, `boot`, `dev`, `etc`, `home`, `root`, `tmp`, `usr`, `var` 등을 확인했다. `bin`, `lib`, `sbin` 일부가 `usr` 아래를 가리키는 link로 표시되는 실제 출력도 보았다.

이어서 `pwd`, `cd`, `mkdir`, `rmdir`, Tab completion을 사용해 사용자 home 아래에 방송사와 프로그램을 본뜬 계층을 만들었다. `mkdir`는 한 directory를 만들고, 중간 부모가 없을 때는 `mkdir -p`가 부모까지 함께 만든다는 차이를 오류와 성공으로 확인했다.

### 2교시: 파일 생성과 목록 확인

- `echo`의 문자열을 `>`로 보내 내용이 있는 파일을 만들었다.
- `touch`로 크기 0인 빈 파일을 만들었다.
- `cat`으로 파일 내용을 확인했다.
- `ls`, `ls -l`, `ls -al`, `ls -lR`로 일반 목록·상세 정보·숨김 파일·재귀 구조를 단계적으로 확인했다.

`ls -al`에서는 `.bashrc`, `.profile`, `.ssh`처럼 `.`으로 시작하는 hidden entry와 owner/group이 표시되었다. 이 출력은 다음 날 권한 문자열을 해석하는 직접 선행 artifact가 된다.

### 3교시: 복사·이동·이름 변경·검색

방송사 tree의 실제 파일을 대상으로 다음 상태 변화를 만들었다.

- `cp`와 wildcard로 한 directory의 여러 파일을 다른 프로그램 directory에 복사했다.
- `cp`의 목적지 이름을 바꿔 접두사가 붙은 복사본을 만들었다.
- `mv`로 파일을 다른 directory로 옮겼다.
- 같은 directory 안에서 `mv`의 목적지 이름을 바꿔 rename 효과를 확인했다.
- `find`의 `-name`, `-iname`, wildcard, `-type d`로 경로·대소문자·이름 pattern·자료형 조건을 달리해 검색 결과를 확인했다.

`find`는 반드시 `/`로 `cd`한 뒤에만 전체 검색이 가능한 것이 아니라, 첫 검색 경로를 어디로 지정하느냐가 범위를 결정한다. 날짜 노트에서는 `/home/...`를 명시해 home subtree를 검색했다.

### 3~4교시: vi 3모드와 파일 생성·수정

vi를 단순 메모장처럼 보지 않고 mode가 바뀌는 editor로 배웠다.

| 모드 | 들어가는 방법·역할 | 빠져나오는 기준 |
|---|---|---|
| 명령 모드 | 기본 모드, cursor 이동·삭제·복사·붙여넣기 | 다른 모드의 기준점 |
| 입력 모드 | `a`, `i`, `o`로 text 입력 | `Esc`로 명령 모드 복귀 |
| 마지막 행/실행 모드 | `:`, `/`, `?`로 저장·종료·검색·치환·외부 명령 | `Esc` 또는 명령 실행 후 복귀 |

vi로 Java·Python keyword 목록 파일을 각각 만들고 `Esc` 후 `:wq`로 저장했다. 원본을 보존하기 위해 `.bak` 복사본을 만든 뒤 `dd`, `3dd`, `u`, `yy`, `3yy`, `p`로 삭제·undo·복사·붙여넣기를 연습했다.

### 4교시: redirection으로 파일 조합

백업본을 원래 파일로 복원한 뒤 `cat`과 redirection으로 `total.txt`를 만들었다.

1. `>`로 Java 파일 내용을 새 결과 파일에 덮어썼다.
2. 다시 다른 파일을 `>`로 보내 기존 내용이 사라지는 것을 확인했다.
3. Java 내용을 복원한 뒤 `>>`로 Python 내용과 추가 문자열을 뒤에 누적했다.
4. `head -n`과 `tail -n`으로 결과 파일의 앞·뒤 일부를 확인했다.

### 5~6교시: Librarian 별도 session 복습

전날 만든 두 번째 VM의 Librarian session에서 별도 실습 교안의 directory 문제를 수행했다. 날짜 노트에는 page 범위만 기록되어 있으므로, 세부 결과를 첫 VM 실습과 합쳐 새 성공 결과로 만들지 않는다.

### 7교시: vi 검색·치환, `grep`, `more`

- `:set nu`와 `:set nonu`로 line number 표시를 전환했다.
- `/단어`, 단일 line 치환, 전체 `%s/.../.../g`, 범위 치환과 확인 `gc`를 사용했다.
- 교안의 잘못된 치환 표기를 `:%s/for/hello/g` 형태로 바로잡아 실행했다.
- `:11r! ls -al ...`처럼 외부 명령 결과를 편집 중인 파일에 읽어 들였다.
- `grep`에 `-i`, `-n`, `-w`를 조합해 대소문자·line number·whole word 조건을 비교했다.
- `more`와 pipe를 사용해 긴 파일을 화면·줄 단위로 넘겨 보았다.

### 8교시: `diff`로 두 파일 비교

원본 파일을 다른 확장자 파일로 복사하고 vi에서 두 keyword를 치환했다. `diff --brief`는 두 파일이 다른지만 알렸고, 일반 `diff`는 `6c6`, `11c11`과 `<`, `>` 표시로 왼쪽·오른쪽 파일의 실제 차이를 보여 주었다. 즉, “수정했다”는 기억이 아니라 비교 결과로 변경 위치를 검증했다.

## 대표 실습: 방송사 tree에서 `total.txt`와 diff까지

**입력**은 방송사·프로그램 directory 구조, Java/Python keyword 목록, `echo`·`touch`로 만든 파일이다. **처리**는 `cp`·`mv`·`find`로 위치를 바꾸고 찾은 뒤 vi로 편집하고, `>`·`>>`로 내용을 조합하며, `grep`·`more`·`diff`로 확인하는 과정이다. **결과**로 파일 tree와 `total.txt`, backup, 수정 비교본이 남았고 각 명령이 경로·내용·이름 중 무엇을 바꾸는지 구분할 수 있게 되었다. ^[raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md]

## 대표 artifact와 확인 결과

- 방송사/프로그램 형태의 directory tree
- 내용이 있는 text file과 `touch`로 만든 0-byte file
- Java/Python keyword 파일과 `.bak` backup
- redirection으로 조합한 `total.txt`
- `find`의 실제 경로 결과
- `diff --brief`의 다름 판정과 일반 `diff`의 line별 차이
- Librarian VM의 별도 복습 session

## 헷갈리기 쉬운 지점

1. **`>`와 `>>`는 모두 파일에 쓰지만 결과가 반대다.** `>`는 기존 내용을 대체하고 `>>`는 끝에 추가한다.
2. **`mv`는 이동과 rename을 모두 담당한다.** 같은 directory에서만 rename 가능한 것이 아니라 목적지 path와 이름에 따라 결과가 정해진다.
3. **`mkdir` 실패 뒤 `mkdir -p`가 성공한 이유는 부모 생성 여부다.** 이름 오타와 구분해야 한다.
4. **vi에서 글자를 입력한 상태와 저장 명령을 받는 상태가 다르다.** `Esc`로 명령 모드에 돌아온 뒤 `:wq` 또는 `:q!`를 사용한다.
5. **`grep`와 `find`의 검색 대상이 다르다.** `find`는 파일 시스템 entry를 찾고, `grep`은 파일 내용의 pattern을 찾는다.
6. **`more`는 파일을 바꾸지 않는다.** 긴 출력을 나누어 읽는 viewer이고, `diff`는 두 파일의 차이를 판정한다.

## 이전·다음 수업 연결

- 이전: [[summaries/2026-04-22-linux-install-ssh-cli|04-22]]의 prompt·home·절대/상대 경로를 실제 tree 조작에 적용했다.
- 다음: [[summaries/2026-04-24-linux-users-permissions|04-24]]에는 이날 `ls -l`에서 본 `-rw-rw-r--`, owner, group을 읽고 실제 `chmod`·`chown`·`chgrp`로 바꾼다.
- 후속 활용: vi·redirection·검색·비교는 Docker 설정, 배포 파일, 로그를 다룰 때 재사용되지만 이날은 Linux 파일 작업 자체를 직접 학습한 날이다. AWS EC2나 CI/CD 실행 결과를 이날로 소급하지 않는다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[entities/linux|Linux]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md` — 실제 교시·명령 순서·방송사/Librarian·vi·redirection·diff 결과의 최우선 근거