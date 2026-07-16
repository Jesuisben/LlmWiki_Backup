---
title: Linux 사용자·그룹·권한
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/AccessRights.png
  - raw/KoreaICT/5. Linux/교육 자료/OwnerShip.png
status: growing
confidence: high
---

# Linux 사용자·그룹·권한

## 이 Concept의 책임

Linux에서 **누가 명령을 실행하는지**, file/directory의 **owner와 group이 누구인지**, owner·group·others에게 **어떤 access rights가 있는지**를 분리해 권한 오류를 진단한다. `chmod`·`chown`·`chgrp`, `sudo`·root, 실행 권한 오류까지 같은 흐름에서 다룬다.

## 왜 필요한가

04-23에는 file을 자유롭게 만들고 수정했지만 04-24에는 같은 작업이 사용자·group·directory permission에 따라 성공하거나 `Permission denied`로 끝났다. 04-27에는 `sudo`로 만든 download directory 때문에 Windows drag-and-drop이 실패했다. 즉, “파일이 존재한다”와 “현재 사용자가 그 파일에 필요한 동작을 할 수 있다”는 다른 문제다.

## 사용자·group·ownership의 관계

- **user**: login하거나 process·command를 실행하는 주체다.
- **group**: 여러 user에게 공통 permission을 적용하기 위한 묶음이다.
- **owner**: file/directory에 연결된 소유 user다.
- **group owner**: 해당 artifact에 연결된 group이다.
- **others**: owner도 해당 group 기준도 아닌 나머지 사용자 범주다.

`OwnerShip.png`는 file 하나에 owner가 있고, family/team에 비유한 group, outside people에 비유한 others가 별도 범주임을 보여 준다. `AccessRights.png`는 permission의 세 기본 동작을 `r` read, `w` write, `x` execute로 표시하고 이 세 묶음을 owner·group·others에 적용한다. 이미지에는 `chmod`·`chown` 명령이나 숫자 4/2/1은 표시되어 있지 않으므로, 그 내용은 04-24 날짜 MD의 별도 근거로 설명한다.

## `ls -l`을 읽는 순서

`-rw-rw-r--` 같은 앞부분은 file type 1글자와 permission 9글자다.

| 부분 | 의미 |
|---|---|
| 첫 글자 `-` / `d` | 일반 file / directory |
| 첫 `rwx` 묶음 | owner permission |
| 둘째 `rwx` 묶음 | group permission |
| 셋째 `rwx` 묶음 | others permission |

그 뒤에는 link 수, owner 이름, group 이름, byte 크기, 수정 시각, 파일명이 이어졌다. owner와 group 이름이 같아 보여도 서로 다른 field다. 04-24에는 전날의 Java/Python 파일과 방송사 directory 출력으로 이 구조를 읽었다. ^[raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md]

## account file과 UID·GID·home·login shell

| 파일 | 수업에서 확인한 역할 |
|---|---|
| `/etc/passwd` | 사용자명, password 자리 `x`, UID, 기본 GID, comment, home directory, login shell |
| `/etc/shadow` | password hash와 계정 잠금·만료·변경 주기 같은 aging 정보. 실제 hash를 외부 문서에 옮기지 않는다. |
| `/etc/group` | group 이름, GID, member 정보를 확인하는 파일 |

UID와 GID는 표시 이름과 별개인 숫자 식별자다. `useradd -m`으로 사용자를 만들자 같은 이름의 기본 group과 home이 생성되었고, `/etc/skel`의 `.bashrc`, `.profile`, 실습용 welcome file이 새 home에 복사되었다. 요구사항 실습에서는 `-d`로 home, `-u`로 UID, `-s`로 login shell을 지정하고 `/etc/passwd`, `/etc/group`, home 목록으로 결과를 확인했다.

login shell은 login 뒤 명령을 해석하고 program·script·환경 변수·redirection을 다루는 interface다. `/bin/sh`, `/bin/bash`, 실습에서 바꿔 본 다른 shell path는 단순 설명 문자열이 아니라 account의 login 환경 field다.

## 기본 group과 보조 group

사용자 생성 시 기본(primary) group이 연결되었고, 별도 `groupadd`로 일반 group·지정 GID group·system group을 만들었다. 이후 한 사용자를 추가 group에 지정하고 `groups 사용자`와 `/etc/group`을 확인하자 **자기 이름의 기본 group과 업무용 보조 group 두 곳에 속한 결과**가 나타났다.

group 관련 명령은 실행 뒤 다음을 확인한다.

1. `/etc/group`에서 group과 GID가 생성되었는가.
2. `groups` 결과에서 사용자의 기본·보조 소속이 의도와 맞는가.
3. group owner와 group permission이 실제 대상 directory에 설정되어 있는가.

수업의 UID/GID 범위는 해당 Ubuntu 환경의 조회 기준이다. 배포판 설정에 따라 system/general account 경계가 달라질 수 있으므로 숫자 하나를 모든 Linux의 절대 규칙으로 외우지 않는다.

## `r`, `w`, `x`: file과 directory에서 다시 읽기

| permission | file | directory |
|---|---|---|
| `r` | 내용 읽기 | entry 이름 목록을 읽는 데 관련 |
| `w` | 내용 수정 | 내부 entry 생성·삭제·이름 변경에 관련 |
| `x` | file 실행 | directory를 통과해 내부 entry에 접근하는 데 관련 |

directory의 `x`는 “directory 실행”이 아니라 **경로 통과(search/traverse)**다. 04-24에는 쓰기 없는 directory에서 `touch`가 `Permission denied`로 실패했고, owner만 읽는 `400` 상태의 directory에 file 복사가 실패한 뒤 `775`로 바꾸자 성공했다. directory 작업은 대상 file permission만 보지 말고 경로를 이루는 directory의 `x`와 목적지 directory의 `w`를 함께 본다.

## 숫자 mode: 전체 permission 상태를 한 번에 지정

날짜 MD에서는 `r=4`, `w=2`, `x=1`을 더해 owner/group/others 세 자리를 만들었다.

| 값 | permission | 수업의 선택 상황 |
|---:|---|---|
| `644` | `rw-r--r--` | owner만 수정하고 모두 읽게 함 |
| `444` | `r--r--r--` | 모두 읽기 전용으로 만들어 vi 저장 오류를 확인 |
| `600` | `rw-------` | owner만 읽고 쓰는 설정 파일 |
| `555` | `r-xr-xr-x` | 모두 읽고 통과/실행할 수 있지만 쓰기는 막음 |
| `700` | `rwx------` | owner만 모든 권한 |
| `777` | `rwxrwxrwx` | 모두 모든 권한. 편하지만 기본 해결책으로 사용하지 않음 |

숫자 mode는 원하는 **최종 상태 전체가 명확할 때** 편하다. 04-24에는 `chmod 644`, `444`, `600`, `555`, `700`, `777` 전후를 `ls -l`로 확인했다.

## 기호 mode: 기존 상태의 일부만 조정

기호 mode는 `u` owner, `g` group, `o` others, `a` all과 `+` 추가, `-` 제거, `=` 정확히 설정을 조합한다.

- owner에게 실행만 추가: `u+x`
- group에서 실행이나 쓰기만 제거: `g-x`, `g-w`
- others를 읽기만 가능하게 설정: `o=r`
- 모두에게 쓰기 제거: `a-w`

기호 mode는 기존 permission을 유지하면서 **한 대상의 한 권한만 바꿀 때** 읽기 쉽다. 숫자 mode와 경쟁하는 방식이 아니라 변경 목적에 따라 고른다.

## `chmod`, `chown`, `chgrp`의 책임 차이

| 명령 | 바꾸는 것 | 바꾸지 않는 것 |
|---|---|---|
| `chmod` | owner/group/others의 access rights | owner 이름 자체 |
| `chown` | owner, 또는 `owner:group` 형태의 ownership | permission bit 자체 |
| `chgrp` | group owner | user owner와 permission bit 자체 |

04-24에는 `sudo mkdir`로 만든 `ytn` directory의 owner/group이 root여서 일반 사용자 `touch`가 실패했다. `chown -R`로 ownership을 넘긴 뒤 같은 위치에 file이 생성되었다. 다른 방송사 tree에는 `chgrp -R`로 group owner를 바꾸고, group write permission을 제거·복원해 `cp` 실패와 성공을 확인했다.

이 사례에서 `chmod 777`은 필수 해법이 아니었다. **실행 주체 → owner/group → directory permission → 필요한 최소 변경** 순서로 보면 ownership을 바로잡을지 permission만 조정할지 선택할 수 있다.

## `sudo`와 root 계정은 같은 상태가 아니다

- `sudo 명령`: 현재 일반 사용자 session에서 특정 명령만 관리자 권한으로 실행한다.
- `sudo su -`: 수업에서는 root login shell로 전환해 prompt가 `#`로 바뀌고 root 환경에서 여러 명령을 연속 실행했다.
- root account/session: 시스템 전체를 관리할 수 있지만, 이 session에서 만든 artifact가 root owner가 되어 이후 일반 사용자 작업을 막을 수 있다.

사용자 생성은 “반드시 root prompt에서만 가능한 명령”이라기보다 **관리자 권한이 필요한 작업**이다. 수업은 root session에서 `useradd`, `passwd`, `groupadd`를 수행했지만, root로 계속 작업하는 것과 필요한 명령에 관리자 권한을 주는 것은 범위가 다르다.

## 실제 오류 해결 1: root 소유 directory

1. **입력**: 일반 사용자 home에서 `sudo mkdir`로 만든 directory와 그 안에 만들 file.
2. **오류**: owner/group이 root인 상태에서 일반 사용자 `touch`가 `Permission denied`로 실패.
3. **진단**: `ls -l`로 실행 주체와 directory ownership을 비교.
4. **처리**: `chown -R`로 owner/group을 일반 사용자에게 넘김.
5. **결과**: 같은 `touch`가 성공하고 file 목록이 확인됨.

04-27의 MobaXterm drag-and-drop 실패도 같은 class의 문제였다. root 소유 download directory를 확인하고 ownership을 넘긴 뒤 file transfer와 archive 해제가 이어졌다. ^[raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md]

## 실제 오류 해결 2: script 실행 권한

`print_tree.sh`에는 `ls`, `echo`, `tree`가 들어 있었지만 처음 permission은 실행 가능한 상태가 아니었다.

1. `ls -l`로 `x`가 없음을 확인했다.
2. `./print_tree.sh`가 `Permission denied`로 실패했다.
3. `chmod 744`로 owner에게 실행 권한을 부여했다.
4. 다시 실행하자 현재 directory의 script 안에 적은 세 명령 결과가 출력되었다.

여기서 `./`는 현재 directory의 file을 지목하고, `x`는 그 file을 program/script로 실행할 수 있게 한다. 단순히 `.sh` 확장자가 있다는 사실만으로 실행 권한이 생기지 않는다.

## 자주 헷갈리는 점과 선택 기준

1. **owner와 같은 이름의 group**: 자동 생성될 수 있지만 user와 group은 별도 식별자·field다.
2. **`/etc/passwd`의 `x`**: 실행 permission이 아니라 password 정보가 `/etc/shadow`에 분리되었다는 자리다.
3. **UID/GID**: 표시 이름과 별개인 숫자 식별자다. 기본 GID와 보조 group membership도 구분한다.
4. **directory `x`**: 내부 path 통과·접근과 관련된다. `r`이나 `w` 하나만 보고 directory 동작을 단정하지 않는다.
5. **숫자 vs 기호 mode**: 전체 상태를 정하면 숫자, 기존 상태의 일부만 조정하면 기호가 읽기 쉽다.
6. **`chmod` vs `chown` vs `chgrp`**: permission, owner, group이라는 서로 다른 field를 바꾼다.
7. **`sudo` vs root**: 한 명령의 privilege 상승과 지속적인 관리자 shell은 범위·환경·생성 artifact owner가 다르다.
8. **group 삭제 예시**: 04-24 말미의 기존 group 전체 삭제는 원본에 “하지는 않음”으로 적혀 있어 실제 실행 결과로 취급하지 않는다.

## 직접 수업과 후속 활용 경계

- Linux 직접: account file·UID/GID·home/shell, 사용자·group 생성, 기본/보조 group 확인, chmod 숫자·기호 mode, chown/chgrp, permission 오류와 script 실행.
- Docker group 후속: 일반 사용자가 Docker daemon socket을 쓰도록 group에 넣고 재로그인하는 문제는 04-28 이후 Docker setup에서 직접 다룬다. 이 페이지는 그 선행 원리만 제공한다.
- AWS EC2 후속: EC2 login user와 SSH private key permission은 cloud VM 접속에서 적용되며, VirtualBox 사용자 실습과 동일한 artifact가 아니다.
- CI/CD 후속: deploy user와 자동화 process의 file 접근은 pipeline 과목에서 다룬다. 04-24에는 workflow나 운영 배포 계정을 만들지 않았다.

## 선행·후속 연결

- 선행: [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]에서 만든 방송사 tree와 `ls -l` 출력이 permission 실습 대상이 되었다.
- 직접 수업: [[summaries/2026-04-24-linux-users-permissions|04-24 사용자·그룹·권한]]에서 계정 생성부터 오류 해결까지 실행했다.
- 다음: [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]에서 root 소유 download directory와 archive 이동 문제에 ownership을 적용했다.
- 후속: [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]에서 Docker group과 재로그인으로 확장한다.

## 관련 페이지

- [[summaries/2026-04-23-linux-files-vi|04-23 파일·vi]]
- [[summaries/2026-04-27-linux-archive-java-alias|04-27 압축·Java·웹서버]]
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]
- [[entities/linux|Linux]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md` — account·group·permission·ownership·오류·script 실행의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` — root 소유 download directory와 archive 반입 실패·해결의 확장 사례
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — 권한과 후속 Docker·server 흐름의 연결 보조
- `raw/KoreaICT/5. Linux/교육 자료/AccessRights.png` — 화면에 표시된 `r/w/x`와 owner/group/others 적용 구조
- `raw/KoreaICT/5. Linux/교육 자료/OwnerShip.png` — 화면에 표시된 owner·family/team group·outside people others 비유
