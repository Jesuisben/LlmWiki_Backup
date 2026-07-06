---
title: Linux 사용자·그룹·권한
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/Study/5. Linux/교육 자료/AccessRights.png
  - raw/Study/5. Linux/교육 자료/OwnerShip.png
  - raw/Study/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux 사용자·그룹·권한

## 정의

Linux 권한은 파일과 디렉터리에 대해 owner, group, others가 각각 read/write/execute를 할 수 있는지를 나타내는 규칙이다.

## 왜 중요한가

서버 배포에서 “파일이 있는데 읽을 수 없음”, “드래그 앤 드롭이 안 됨”, “스크립트 실행이 안 됨”, “Docker 명령 permission denied” 같은 문제는 대부분 권한·소유권·그룹 문제로 이어진다.

## 핵심 설명

`ls -l` 예시의 `-rw-rw-r--`는 다음처럼 읽는다.

| 부분 | 의미 |
|---|---|
| `-` | 일반 파일. 디렉터리는 `d` |
| `rw-` | owner 권한 |
| `rw-` | group 권한 |
| `r--` | others 권한 |

- `r`: 읽기. 파일은 `cat`, 디렉터리는 목록 조회와 관련된다.
- `w`: 쓰기. 파일 내용 수정 또는 디렉터리 안 항목 생성/삭제와 관련된다.
- `x`: 실행. 파일은 실행, 디렉터리는 진입 권한과 관련된다.

## 예시

```bash
ls -l
sudo su -
useradd -m skywalker
passwd skywalker
groupadd jedi
usermod -aG jedi skywalker
cat /etc/passwd
cat /etc/group
sudo chown -R broadcast:broadcast /home/broadcast/downloads/fromwindows/
```

## 자주 헷갈리는 점

- owner와 group 이름이 같아도 둘은 다른 칸이다.
- `/etc/shadow`에는 비밀번호 해시가 있으므로 학습할 때도 실제 값을 외부 문서에 옮기지 않는다.
- `sudo`는 “root로 로그인”과 비슷한 효과를 순간적으로 주지만, 현재 사용자가 누구인지와 파일 소유권은 별개다.
- Docker 그룹에 사용자를 추가한 뒤에는 재로그인해야 권한이 반영될 수 있다.

## 관련 개념

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[entities/linux|Linux]]

## 출처

- `raw/Study/5. Linux/2026.04.24(금)/2026.04.24(금).md`
