---
title: Linux 사용자·그룹·권한
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux]
sources:
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
status: growing
confidence: high
---

# Linux 사용자·그룹·권한

## 정의

Linux는 파일마다 소유자(owner), 그룹(group), 그 외 사용자(others)에 대해 읽기(`r`), 쓰기(`w`), 실행(`x`) 권한을 따로 관리한다. 사용자는 계정이고, 그룹은 여러 사용자를 묶어 권한을 관리하는 단위다.

## 왜 중요한가

서버에서 “파일이 있는데 실행이 안 됨”, “설정 파일 저장이 안 됨”, “Docker volume에 접근이 안 됨” 같은 문제는 대부분 권한과 관련된다. 이 개념은 배포·보안·운영 오류 해결의 기본이다.

## `ls -l` 읽는 법

예를 들어 다음과 같은 출력이 있다고 하자.

```bash
-rwxr-xr-- 1 owner group 1234 Apr 24 app.sh
```

- 첫 글자 `-`: 일반 파일이다. 디렉터리는 `d`로 시작한다.
- `rwx`: owner 권한이다. 읽기·쓰기·실행 가능.
- `r-x`: group 권한이다. 읽기·실행 가능, 쓰기 불가.
- `r--`: others 권한이다. 읽기만 가능.

## 수업 예제

```bash
sudo su -
cd /etc/skel
useradd -m skywalker
ls -al /home/skywalker
useradd -m -d /home/sunnyday -u 7000 -s /bin/bash sunnyday
cat /etc/passwd
cat /etc/shadow
cat /etc/group
```

수업에서는 `/etc/skel`이 새 사용자 홈 디렉터리에 복사되는 템플릿이라는 점과, `/etc/shadow`의 password aging 정보가 보안 강화를 위해 쓰인다는 점을 확인했다.

## 자주 헷갈리는 점

- `sudo`는 한 명령만 관리자 권한으로 실행하고, `sudo su -`는 root 셸로 들어가는 느낌이다.
- root 권한은 강력하지만 실수도 크게 만든다. 삭제·권한 변경 명령은 경로를 반드시 확인해야 한다.
- `useradd` 옵션을 빼면 홈 디렉터리나 셸이 기대와 다를 수 있다. 수업에서는 `-m`, `-d`, `-u`, `-s` 옵션을 함께 봤다.

## 관련 수업

- [[summaries/2026-04-24-linux-users-permissions|2026-04-24 Linux 사용자, 그룹, 권한]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]

## 출처

- `raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
