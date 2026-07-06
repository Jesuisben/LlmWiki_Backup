---
title: 2026-04-24 Linux 사용자, 그룹, 권한
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/Study/5. Linux/교육 자료/AccessRights.png
  - raw/Study/5. Linux/교육 자료/OwnerShip.png
  - raw/Study/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# 2026-04-24 Linux 사용자, 그룹, 권한

## 한 줄 요약

`ls -l` 출력의 owner/group/others 권한을 해석하고, 사용자·그룹 생성과 `/etc/passwd`, `/etc/shadow`, `/etc/group` 파일을 확인한 날이다.

## 배운 내용

- `ls -l`의 `-rw-rw-r--` 같은 권한 문자열을 파일 종류, owner/group/others 권한으로 나누어 읽었다.
- `r`, `w`, `x`가 각각 read/write/execute를 의미하고, 파일과 디렉터리에서 체감 동작이 다르다는 점을 배웠다.
- `sudo su -`로 root가 된 뒤 `/etc/skel` 템플릿과 신규 사용자 홈 디렉터리 생성 흐름을 확인했다.
- `useradd -m`, `passwd`, `groupadd`, `usermod` 등 사용자·그룹 관리 명령을 실습했다.
- `/etc/passwd`, `/etc/shadow`, `/etc/group`에서 계정 정보, 비밀번호 해시, 그룹 정보를 확인했다.
- 권한 문제가 생기면 소유자/그룹/권한 중 무엇이 원인인지 먼저 읽어야 한다는 감각을 잡았다.

## 핵심 개념

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- owner: 파일/디렉터리의 소유자.
- group: 여러 사용자를 묶는 권한 단위.
- others: 소유자와 그룹에 속하지 않는 나머지 사용자.
- root: 시스템 전체를 관리할 수 있는 관리자 계정.

## 실습 / 예제

```bash
ls -l
sudo su -
cd /etc/skel
useradd -m skywalker
passwd skywalker
cat /etc/passwd
cat /etc/shadow
cat /etc/group
groupadd jedi
usermod -aG jedi skywalker
```

## 헷갈린 점 / 질문

- `broadcast broadcast`처럼 이름이 두 번 보이면 앞은 owner, 뒤는 group이다.
- 신규 사용자 이름과 같은 그룹이 자동으로 만들어질 수 있어 “사용자 이름”과 “그룹 이름”이 같아 보인다.
- `/etc/shadow`는 민감한 비밀번호 해시가 들어 있는 파일이므로 wiki에서는 실제 값이 아니라 역할만 설명한다.
- 권한 문자열의 첫 글자 `-`는 일반 파일, `d`는 디렉터리를 뜻한다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[entities/linux|Linux]]

## 출처

- `raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
- `raw/Study/5. Linux/교육 자료/AccessRights.png`
- `raw/Study/5. Linux/교육 자료/OwnerShip.png`
