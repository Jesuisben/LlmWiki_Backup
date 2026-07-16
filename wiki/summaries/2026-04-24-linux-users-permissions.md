---
title: 2026-04-24 Linux 사용자, 그룹, 권한
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/교육 자료/AccessRights.png
  - raw/KoreaICT/5. Linux/교육 자료/OwnerShip.png
status: growing
confidence: high
---

# 2026-04-24 Linux 사용자, 그룹, 권한

## 한 줄 요약

`ls -l`의 owner/group/others와 `rwx`를 해석한 뒤 사용자·그룹·account file을 만들고 조회했으며, `chmod`·`chown`·`chgrp`와 실행 권한을 실제 성공·`Permission denied` 결과로 검증했다.

## 왜 이 흐름으로 배웠는가

04-23에는 파일을 만들고 옮기고 편집했지만, 다중 사용자 운영체제에서는 “파일이 존재하는가”만큼 “누가 무엇을 할 수 있는가”가 중요하다. 그래서 전날의 `ls -l` 출력부터 출발해 **권한 문자열 읽기 → 사용자와 그룹의 정체 확인 → 계정 생성 → 권한과 소유권 변경 → 실패·성공 검증** 순서로 확장했다.

이 흐름은 다음 수업에서 `sudo`로 만든 directory를 일반 사용자가 drag-and-drop하지 못하는 오류를 해결하고, 04-28 Docker의 `docker` group 권한을 이해하는 직접 선행이 된다.

## 교시별 학습 전개

### 1교시: `ls -l`, ownership, access rights

전날 만든 Java/Python 파일과 방송사 directory의 `ls -l` 결과를 실제로 읽었다.

- 첫 글자 `-`는 일반 파일, `d`는 directory를 뜻한다.
- 뒤의 9글자는 owner·group·others의 세 묶음이며 각 묶음은 `r`·`w`·`x`를 가진다.
- `r`은 읽기, `w`는 쓰기, `x`는 실행 권한이다.
- 이후에는 link 수, owner 이름, group 이름, byte 크기, 수정 시각, 파일명이 이어진다.

`AccessRights.png`도 같은 구조를 `r=read`, `w=write`, `x=execute`와 owner/group/others 세 범주로 보여 준다. `OwnerShip.png`는 모든 파일에 owner가 있고, family/team에 해당하는 group과 그 밖의 others가 별도 범주라는 점을 비유로 설명한다.

### 1교시 후반: root session과 `/etc/skel`

`sudo su -`로 root login shell에 들어가 prompt가 `#`로 바뀌는 것을 확인했다. `/etc/skel`에는 새 사용자 home에 복사될 `.bashrc`, `.profile` 같은 template이 있었고, 여기에 welcome page를 넣은 뒤 신규 사용자를 생성해 home에 복사되었는지 확인했다.

사용자 생성은 반드시 root prompt로 전환해야만 가능한 것이 아니라 root 권한이 필요한 작업이다. 수업에서는 root session에서 `useradd`와 `passwd`를 실행했지만, 개별 명령에 `sudo`를 사용하는 방식과 권한 요구를 구분해야 한다.

### 2교시: account file, UID/GID, shell

신규 사용자로 SSH session을 만들고 `pwd`, `ls`, `ls -al`로 home과 template 파일을 확인했다. 관리자는 `/etc/passwd`의 해당 행을 조회해 colon으로 나뉜 필드를 읽었다.

| 항목 | 의미 |
|---|---|
| 사용자명 | login account 식별자 |
| `x` | password 정보가 `/etc/shadow`에 분리되어 있음을 나타내는 자리 |
| UID / GID | 사용자와 기본 group의 숫자 식별자 |
| home | login 후 기본 작업 directory |
| shell | 명령을 해석하는 program 경로 |

`/etc/shadow`는 password hash와 만료·변경 주기 같은 aging 정보를, `/etc/group`은 group 정보를 보관한다. shell은 명령 해석·program/script 실행·환경 변수·redirection·process 관리의 사용자 interface라는 역할로 정리했다.

### 2~3교시: 요구사항 기반 사용자 생성과 기본값

`useradd` option으로 home, UID, shell, comment, 만료일을 요구사항에 맞게 지정하고 `/etc/passwd`, `/etc/group`, home directory를 다시 조회했다. 실제 계정명과 password 값은 이 Summary에서 일반화한다.

`useradd -D`와 `/etc/default/useradd`에서는 기본 home base, shell, skeleton directory를 확인·변경했다. 별도 skeleton directory와 shell 기본값을 준비한 뒤 새 사용자를 만들어 실제 home과 shell 필드가 바뀌었는지 확인하고, 실습 사용자를 삭제할 때 home이나 mail spool이 없어 경고가 나는 경우도 보았다.

### 3~4교시: group과 기본·보조 소속

- `groupadd`로 일반 group과 지정 GID group을 만들었다.
- `groupadd -r`로 system 관리용 group을 만들었다.
- `/etc/passwd`의 UID와 `/etc/group`의 GID를 `awk -F:` 조건으로 필터링했다.
- `usermod -G`로 사용자를 추가 group에 넣고 `groups`와 `/etc/group` 결과로 기본 group과 보조 group 소속을 확인했다.

이날의 기준에서는 system account와 일반 account를 UID 범위로 나누어 조회했지만, 정확한 범위는 배포판 설정에 따라 달라질 수 있으므로 “1000 이상이면 언제나 일반 사용자”라는 절대 규칙으로 외우지 않는다.

### 4~5교시: `chmod` 숫자 모드와 기호 모드

권한 값을 `r=4`, `w=2`, `x=1`로 합산해 owner/group/others 세 자리로 설정했다.

- `644`: owner는 읽기+쓰기, group/others는 읽기
- `444`: 모두 읽기 전용
- `600`: owner만 읽기+쓰기
- `555`: 모두 읽기+실행, 쓰기 없음
- `700`: owner만 모든 권한
- `777`: 모두 모든 권한

읽기 전용 파일을 vi로 저장하려 하자 `readonly` 오류가 나타났고, 쓰기 권한이 없는 directory에 `touch`를 실행하자 `Permission denied`가 발생했다. 이어 `u+x`, `g-x`, `a-w` 같은 기호 모드로 특정 대상·연산·권한만 추가하거나 제거했다.

### 5~6교시: `chown`, `chgrp`, directory 권한

일반 사용자 home에서 `sudo mkdir`로 directory를 만들자 owner/group이 root가 되었고, 일반 사용자의 파일 생성은 `Permission denied`로 실패했다. 관리자가 `chown -R`로 owner/group을 일반 사용자에게 넘긴 뒤 같은 `touch`가 성공했다. ^[raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md]

다른 파일들에는 owner와 group을 함께 또는 owner만 바꾸고, `chgrp -R`로 방송사 tree 전체 group을 변경했다. 특정 directory의 group을 바꾼 뒤 쓰기 권한을 제거했을 때 복사가 실패하고, 적절한 권한을 다시 부여한 뒤 복사가 성공하는 과정도 확인했다.

### 6교시 후반: 실행 권한과 process 기초

`ls`, `echo`, `tree`를 순서대로 적은 `print_tree.sh`를 만들었다. 처음에는 실행 권한이 없어 `./print_tree.sh`가 `Permission denied`로 실패했고, `chmod 744` 후에는 현재 directory의 script가 실행되어 세 명령의 결과를 냈다.

교안의 제목에는 `ps`, `kill` process monitoring도 있었지만 날짜 노트에 실제 실행 과정은 남아 있지 않다. 따라서 이날 직접 확인한 process artifact는 shell script 실행까지로 제한한다.

### 수업하지 않은 구간과 7~8교시

6교시 말미의 기존 group 전체 삭제 예시는 날짜 노트에 **“하지는 않음”**으로 표시되어 있다. 이를 실제 삭제 결과로 기록하지 않는다. 7~8교시는 Librarian 실습 교안의 지정 page를 이용한 복습으로만 기록되어 있어 세부 성공 결과를 추가하지 않는다.

## 대표 실습: root 소유 directory의 권한 오류 해결

**입력**은 일반 사용자 home에서 `sudo`로 만든 directory와 그 안에 만들려는 파일이었다. **처리** 과정에서 `ls -l`로 owner/group이 root임을 확인하고, 일반 사용자 `touch`의 `Permission denied`를 재현한 뒤 `chown -R`로 소유권을 넘겼다. **결과**로 같은 일반 사용자가 파일을 만들 수 있었고, 권한 오류가 명령 자체의 문제가 아니라 owner와 directory write permission 문제임을 확인했다.

## 대표 artifact와 확인 결과

- `ls -l`의 file type·owner/group/others·`rwx` 구조
- `/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/skel`, `/etc/default/useradd`
- 요구사항에 맞춘 사용자·group과 home/shell 확인 결과
- `chmod` 숫자·기호 mode 전후의 권한 문자열
- 읽기 전용 오류와 directory `Permission denied`
- `chown`·`chgrp` 전후의 owner/group 변화
- 실행 권한 전후의 `print_tree.sh` 실패·성공

## 헷갈리기 쉬운 지점

1. **owner와 같은 이름의 기본 group은 같은 개념이 아니다.** `ls -l`에 두 이름이 나란히 보여도 사용자와 group 필드다.
2. **`rwx`는 대상마다 다시 읽는다.** owner/group/others 중 어느 세 글자인지 먼저 정해야 한다.
3. **파일의 `x`와 directory의 `x`는 체감 역할이 다르다.** 파일은 실행, directory는 그 안의 entry에 접근하는 권한과 연결된다.
4. **숫자 모드와 기호 모드는 경쟁 방식이 아니다.** 전체 상태를 한 번에 정할 때 숫자, 기존 상태에서 일부만 조정할 때 기호가 편리하다.
5. **`chmod`, `chown`, `chgrp`는 서로 다른 것을 바꾼다.** access rights, owner, group을 구분한다.
6. **`sudo`로 만든 artifact는 root 소유가 될 수 있다.** 이후 일반 사용자 작업이 막히면 무조건 `777`로 풀기보다 owner와 필요한 최소 권한을 먼저 확인한다.

## 이전·다음 수업 연결

- 이전: [[summaries/2026-04-23-linux-files-vi|04-23]]의 파일 tree와 `ls -l` 출력이 권한 실습 대상이 되었다.
- 다음: [[summaries/2026-04-27-linux-archive-java-alias|04-27]]에는 `sudo`로 만든 download directory의 drag-and-drop 실패를 `chown`으로 해결하고, 실행·설정 파일 권한을 Java·웹서버 준비에 적용한다.
- 후속 활용: 04-28의 Docker group, EC2의 login user와 SSH key, CI/CD deploy user는 이 원리를 재사용한다. 그러나 AWS Security Group이나 pipeline 권한은 각각 AWS·CI/CD 과목의 후속 책임이다.

## 관련 페이지

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[entities/linux|Linux]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md` — 실제 교시·계정·group·권한·오류·실행 흐름의 최우선 근거
- `raw/KoreaICT/5. Linux/교육 자료/AccessRights.png` — `r/w/x`와 owner/group/others 구분 보조 그림
- `raw/KoreaICT/5. Linux/교육 자료/OwnerShip.png` — owner·group·others의 소유권 범주 보조 그림