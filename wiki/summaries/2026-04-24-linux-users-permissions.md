---
title: 2026-04-24 Linux 사용자, 그룹, 권한
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
status: growing
confidence: high
---

# 2026-04-24 Linux 사용자, 그룹, 권한

## 한 줄 요약

`ls -l` 출력의 권한 문자열을 해석하고, root 권한으로 사용자·그룹을 생성하며, `/etc/passwd`, `/etc/shadow`, `/etc/group` 같은 계정 관리 파일의 의미를 배웠다.

## 배운 내용

- `ls -l`의 첫 글자는 파일 종류, 이어지는 9글자는 owner/group/others 권한을 뜻한다.
- `r`, `w`, `x`는 읽기, 쓰기, 실행 권한이다.
- `sudo su -`로 root 계정 셸에 들어가 사용자 생성 작업을 수행했다.
- `/etc/skel`은 새 사용자 홈 디렉터리에 복사되는 기본 템플릿 디렉터리다.
- `useradd -m skywalker`로 홈 디렉터리가 있는 사용자를 만들고, 홈 아래 기본 파일을 확인했다.
- `useradd -m -d /home/sunnyday -u 7000 -s /bin/bash sunnyday`처럼 홈, UID, 셸을 명시하는 방식도 배웠다.
- `/etc/shadow`의 password aging 정보가 보안과 연결된다는 점을 확인했다.

## 핵심 실습 흐름

```bash
sudo su -
cd /etc/skel
ls -al
useradd -m skywalker
ls -al /home/skywalker
cat /etc/passwd
cat /etc/group
```

## 왜 중요한가

서버 운영에서는 “파일이 있는데 실행이 안 된다”, “권한이 없어 수정이 안 된다”, “컨테이너나 배포 스크립트가 특정 사용자로 실행된다” 같은 문제가 자주 생긴다. Linux 권한은 배포·보안·Docker 볼륨 문제를 이해하는 기본 문법이다.

## 헷갈린 점 / 질문

- `broadcast` 같은 일반 사용자와 `root`는 권한 범위가 다르다. 모든 명령을 root로 하면 편하지만 실무에서는 위험하다.
- `useradd`는 사용자를 만들지만, 옵션을 빼면 홈 디렉터리나 셸 설정이 기대와 다를 수 있다.
- 권한 문자열은 `rwxr-xr-x`처럼 붙어 있어 처음엔 암호처럼 보이지만, 3글자씩 owner/group/others로 끊어 읽으면 된다.

## 관련 페이지

- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]

## 출처

- `raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
