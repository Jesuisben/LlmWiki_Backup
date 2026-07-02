---
title: Linux 사용자·그룹·권한
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux]
sources:
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/AccessRights.png
  - raw/Study/5. Linux/교육 자료/OwnerShip.png
status: growing
confidence: high
---

# Linux 사용자·그룹·권한

## 정의

Linux는 여러 사용자가 함께 쓰는 운영체제이므로 파일마다 소유자(owner), 그룹(group), 그 외 사용자(others)를 구분하고, 각 범주에 읽기(`r`), 쓰기(`w`), 실행(`x`) 권한을 따로 부여한다.

## 왜 중요한가

서버에서 “파일은 있는데 실행이 안 됨”, “설정 파일 저장이 안 됨”, “Docker mount 경로에 파일을 못 씀” 같은 문제는 권한과 소유권 때문에 자주 발생한다.

## `ls -l` 읽는 법

```bash
-rw-r--r-- 1 broadcast broadcast 80 Apr 23 03:53 java.txt
```

- 첫 글자 `-`: 일반 파일이다. 디렉터리는 `d`로 시작한다.
- `rw-`: owner 권한이다. 읽기/쓰기 가능, 실행 불가.
- `r--`: group 권한이다. 읽기만 가능.
- `r--`: others 권한이다. 읽기만 가능.
- 첫 번째 `broadcast`: 파일 owner.
- 두 번째 `broadcast`: 파일 group.
- `80`: 파일 크기(bytes).

`AccessRights.png`는 read/write/execute를 각각 `cat file.txt`, `echo "hello" > file.txt`, `./script.sh` 예시로 설명한다. `OwnerShip.png`는 owner를 집 주인, group을 가족/팀, others를 외부인으로 비유한다.

## 사용자와 그룹 파일

| 파일 | 역할 |
|---|---|
| `/etc/passwd` | 계정명, UID, GID, 홈 디렉터리, shell 정보 |
| `/etc/shadow` | 암호 해시와 password aging 정보 |
| `/etc/group` | 그룹명, GID, 그룹 구성원 |
| `/etc/skel` | 새 사용자 홈 디렉터리에 복사될 템플릿 파일 |
| `/etc/default/useradd` | `useradd` 기본값 |

## 핵심 명령어

```bash
sudo su -
useradd -m skywalker
passwd skywalker
tail /etc/passwd | grep skyw
useradd -m -d /home/sunnyday -u 7000 -s /bin/bash sunnyday
useradd -D
groupadd -g 7777 journalist
usermod -G journalist sunnyday
groups sunnyday
chmod 644 hello.txt
chmod u+x script.sh
chmod -R a-w /home/broadcast/kbs
sudo chown -R broadcast:broadcast ytn
sudo chgrp -R journalist kbs
```

## 숫자 권한

| 숫자 | 의미 |
|---|---|
| 4 | read |
| 2 | write |
| 1 | execute |
| 7 | read + write + execute |
| 6 | read + write |
| 5 | read + execute |
| 0 | 권한 없음 |

예를 들어 `chmod 644 file.txt`는 owner에게 `rw-`, group과 others에게 `r--`를 준다.

## 자주 헷갈리는 점

- `sudo`로 만든 파일/디렉터리는 owner가 root가 될 수 있다.
- `chown user:group path`는 owner와 group을 함께 바꾼다.
- `chgrp group path`는 group만 바꾼다.
- `.sh` 파일은 내용이 맞아도 실행 권한이 없으면 `Permission denied`가 난다.
- `chmod 777`은 편하지만 모든 사용자에게 쓰기 권한까지 주므로 실무에서는 신중해야 한다.

## 관련 수업

- [[summaries/2026-04-24-linux-users-permissions|2026-04-24 Linux 사용자, 그룹, 권한]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]

## 출처

- `raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf` — 사용자 계정 파일, 권한/chmod/chown/chgrp
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — 사용자·그룹·권한 실습
- `raw/Study/5. Linux/교육 자료/AccessRights.png`
- `raw/Study/5. Linux/교육 자료/OwnerShip.png`
