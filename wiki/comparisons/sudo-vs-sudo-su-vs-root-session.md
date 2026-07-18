---
title: sudo vs sudo su - vs root session
created: 2026-07-18
updated: 2026-07-18
type: comparison
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: stable
confidence: high
---

# sudo vs sudo su - vs root session

## 비교 목적

04-22의 package·service 관리, 04-24의 사용자·group 생성, 04-27의 root 소유 directory 오류, 04-28·05-01의 Docker 설치에서 관리자 권한이 반복됐다. 특히 04-24 원본에는 “사용자 만들기는 꼭 root로 가야 하나?”라는 혼동이 남아 있다. 핵심은 **관리자 권한이 필요한가**와 **지속적으로 root shell에 머물러야 하는가**를 분리하는 것이다.

## 용어 먼저 정리

- `sudo 명령`: 현재 일반 사용자 session에서 지정한 한 명령을 높은 권한으로 실행한다.
- `sudo su -`: `sudo`로 `su -`를 실행해 root의 login 환경을 읽는 지속 shell로 전환한다.
- root session: prompt가 `#`인 관리자 shell에서 여러 명령을 연속 실행하는 상태다. 수업에서는 `sudo su -`로 진입했다.

`sudo su -`는 root session에 들어가는 한 방법이다. 따라서 세 항목은 완전히 독립된 세 도구가 아니라 **한 명령의 권한 상승 → root login shell 전환 → 그 결과 지속되는 관리자 session**의 관계다.

## 한눈에 보기

| 비교 축 | `sudo 명령` | `sudo su -` | root session |
|---|---|---|---|
| 권한 범위 | 지정한 명령 하나 | root login shell 진입 명령 | `exit`할 때까지 후속 명령 전반 |
| 환경 | 일반 사용자 session을 유지하며 명령만 상승 | root home·login 환경으로 전환 | root의 현재 directory·환경·prompt 사용 |
| prompt | 보통 `$` 유지 | 실행 뒤 `#`로 바뀜 | `#` |
| 수업 예 | package 설치, service·UFW 관리, `mkdir`, `chown` | 사용자/group 실습과 Docker setup 진입 | `/etc/skel`, `useradd`, Docker 설치 script 연속 작업 |
| 주요 위험 | 생성 artifact가 root 소유가 될 수 있음 | 필요 이상으로 넓은 관리자 shell 시작 | 실수 범위 확대·root 소유 artifact 누적 |

## 실제 선택 상황

### 상황 1: package 하나 설치하거나 service 상태 변경

`sudo 명령`이 적합하다. 04-22에는 OpenSSH 설치·시작·상태·종료, 04-27에는 zip과 web server package·UFW, 04-28에는 Nginx 정리와 port/firewall rule에 개별 `sudo`를 사용했다. 명령이 끝나면 일반 사용자 작업 흐름으로 돌아온다.

### 상황 2: 사용자·group과 system file을 연속 관리

04-24 수업은 `sudo su -`로 root login shell에 들어가 `/etc/skel`, `useradd`, `passwd`, `/etc/passwd`·`/etc/group` 확인을 연속 수행했다. **실행 권한이 필요하다는 사실**과 **root shell이 반드시 유일한 방법이라는 주장**은 다르다. 수업의 직접 결과는 root session에서 실행했다는 것이며, 개별 관리자 명령에 `sudo`를 붙이는 운영 선택까지 비교 실습한 것은 아니다.

### 상황 3: Docker 설치 script를 root 영역에서 연속 실행

04-28과 05-01에는 setup script를 `/root`에 준비하고 `sudo su -` 뒤 CRLF 교정·실행 권한·설치·service 확인을 연속 처리했다. 설치가 끝난 뒤에는 일반 사용자를 Docker group에 추가하고 **새 login session**에서 일반 사용자 Docker 접근을 확인했다. root shell 유지가 Docker 일상 사용의 완료 조건은 아니었다.

### 상황 4: 일반 사용자 home에 작업 directory 만들기

일반 사용자가 직접 쓸 directory라면 불필요한 `sudo mkdir`을 피하는 편이 낫다. 04-24·04-27에는 일반 사용자 home 아래 directory를 `sudo`로 만들어 owner/group이 root가 되었고, 이후 `touch`나 MobaXterm drag-and-drop이 `Permission denied`로 실패했다.

## 함께 쓰는 관계

일반 사용자 session을 기본으로 유지하면서 필요한 system 변경만 `sudo 명령`으로 수행하고, 여러 관리자 작업이 정말 연속될 때만 root session을 시작할 수 있다. root session에서 나온 뒤에는 `ls -ld`·`ls -l`로 생성 artifact의 owner/group을 확인하고, 일반 사용자가 이어서 다룰 대상이라면 의도한 ownership을 설정한다.

## 실제 오류·완료 조건

| 단계 | 수업에서 확인한 결과 | 다음 확인 |
|---|---|---|
| `sudo su -` | prompt가 root `#`로 변경 | 현재 user·directory·환경이 의도와 맞는가 |
| 관리자 명령 실행 | 사용자/package/service/artifact 생성 | 생성 결과와 owner/group 확인 |
| root session 종료 | 일반 사용자 session으로 복귀 | 일반 사용자 작업 성공 여부 |
| Docker group 등록 | account의 group membership 변경 | logout/login 후 Docker daemon 접근 |

## 흔한 오해와 확인되지 않은 범위

- `sudo`를 썼다고 로그인 계정 자체가 영구적으로 root가 되는 것은 아니다.
- 관리자 권한이 필요한 명령이라고 항상 root shell에 들어갈 필요는 없다.
- root session의 `#`와 Markdown heading의 `#`는 전혀 다른 문맥이다.
- `sudo`로 만든 모든 artifact가 언제나 root 소유라고 단정하기보다 실제 `ls -l`로 확인한다. 수업의 `mkdir` 사례에서는 root 소유가 확인됐다.
- root-owned artifact 문제를 무조건 `chmod 777`로 풀지 않는다. ownership과 필요한 최소 permission을 구분한다.
- `sudoers`, `visudo`, 세부 command policy, audit log, `sudo -i`와의 비교는 현재 원본에서 실습하지 않았다.
- AWS EC2 login user와 CI/CD deploy user는 후속 적용이다. Linux 수업의 root session을 운영 배포 정책으로 일반화하지 않는다.

## 관련 페이지

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치·SSH·CLI]]
- [[summaries/2026-04-24-linux-users-permissions|2026-04-24 사용자·그룹·권한]]
- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27 압축·Java·웹서버]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[queries/why-sudo-created-directory-denies-normal-user|sudo로 만든 디렉터리는 왜 일반 사용자로 수정·복사할 수 없는가]]
- [[entities/linux|Linux]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` — 개별 package·service 관리자 명령과 `$`/`#` prompt의 첫 비교
- `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md` — `sudo su -`, root session의 사용자·group 관리, 명시적 혼동, root 소유 directory 오류
- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` — 일반 사용자 home의 root 소유 download directory 확장 사례
- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`와 `2026.05.01(금)` — Docker 설치 root shell과 일반 사용자 group·재로그인 경계
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — 관리자 권한과 후속 Docker/server 흐름의 복습 연결
