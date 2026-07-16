---
title: Linux CLI와 파일 시스템
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux CLI와 파일 시스템

## 이 Concept의 책임

Linux prompt와 경로를 읽고, 명령이 파일·디렉터리의 **위치·이름·내용·존재 여부 중 무엇을 바꾸는지** 판단하는 페이지다. 04-22의 원격 CLI·경로 입문에서 04-23의 방송사 directory와 Librarian 실습, vi·redirection·검색·비교까지 이어진다.

## 왜 필요한가

04-22에는 VirtualBox Ubuntu guest에 MobaXterm으로 접속한 뒤 prompt와 `pwd`를 읽었다. 04-23에는 같은 CLI에서 directory tree를 만들고 파일을 복사·이동·수정했다. 서버에서는 GUI보다 “현재 누구로, 어느 host의, 어느 경로에서 명령을 실행하는가”가 작업 결과를 좌우하므로, 파일 명령을 외우기 전에 prompt와 경로 기준부터 잡았다. ^[raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md]

## prompt와 경로 읽기

prompt는 보통 `사용자@호스트:현재경로$` 형태다.

- **사용자**: 현재 명령을 실행하는 계정이다. 파일 권한과 소유권 판단의 출발점이다.
- **host**: 접속한 Linux 시스템 이름이다. MobaXterm client 이름이나 Windows host와 혼동하지 않는다.
- **현재 경로**: `~`이면 현재 사용자의 home directory다. `pwd`로 실제 절대 경로를 확인한다.
- **`$`와 `#`**: 일반 사용자와 관리자 prompt를 구분한다. prompt 표시는 권한 문제를 진단할 때 실행 주체를 확인하는 단서다.

Linux 파일 시스템은 최상위 **root directory `/`**에서 시작한다. `/root`는 root 계정의 home directory이므로 `/`와 같은 뜻이 아니다.

| 경로 방식 | 기준 | 선택 상황 |
|---|---|---|
| 절대 경로 | `/`부터 전체 위치를 지정 | 현재 위치가 바뀌어도 같은 server file을 가리켜야 할 때 |
| 상대 경로 | 현재 작업 directory | 가까운 하위 artifact를 짧게 다룰 때 |
| `.` / `..` | 현재 / 상위 directory | 현재 위치를 기준으로 이동하거나 명령 대상을 정할 때 |
| `~` | 현재 사용자의 home | account마다 home이 달라도 자기 작업 공간으로 돌아갈 때 |

04-22 문제 풀이에서는 `./하위경로`와 `하위경로`가 같은 현재 위치 기준 결과를 만들 수 있음을 확인했다. 경로의 옳고 그름은 길이가 아니라 **어디를 기준으로 해석하는가**로 판단한다.

## 파일 상태를 바꾸는 명령의 책임

| 확인·처리 | 실제 수업에서 바뀐 상태 |
|---|---|
| `pwd`, `ls`, `ls -l`, `ls -al`, `tree` | 현재 위치·일반/숨김 entry·상세 정보·tree를 읽었다. 파일은 바꾸지 않는다. |
| `cd` | shell의 현재 작업 directory를 바꾼다. 인수 없이 실행하면 home으로 이동했다. |
| `mkdir`, `mkdir -p` | directory를 만든다. 부모가 없던 경로는 일반 `mkdir`가 실패하고 `-p`가 부모까지 생성했다. |
| `touch` | 04-23에는 0-byte 파일을 만들었다. |
| `cp` | 원본을 남기고 다른 path나 이름의 복사본을 만들었다. wildcard로 여러 파일도 복사했다. |
| `mv` | entry를 다른 directory로 이동하거나 목적지 이름으로 바꿨다. 이동과 rename은 같은 명령의 목적지 해석 차이다. |
| `rm`, `rmdir` | 파일 또는 빈 directory를 지운다. `rm -rf`는 04-27 정리 실습에서 tree 전체를 제거했으며 복구가 어려운 위험 명령이다. |
| `find` | 시작 path 아래에서 이름·대소문자·자료형 같은 조건으로 entry를 찾았다. `/`로 먼저 이동하는 것이 필수 조건은 아니다. |

## 실제 실습 1: 방송사 directory의 상태 변화

04-23에는 home 아래 방송사와 프로그램을 본뜬 directory tree를 만들었다.

1. **입력**: 빈 방송사/program directory와 `echo`, `touch`로 만든 text file이었다.
2. **처리**: `cp`로 여러 파일과 이름을 바꾼 복사본을 만들고, `mv`로 위치와 이름을 바꿨다. `find`에는 `/home/...` 시작 path와 `-name`, `-iname`, wildcard, `-type d` 조건을 주었다.
3. **결과**: 설정 파일은 다른 program directory로 이동했고, 접두사가 붙은 복사본과 rename된 파일이 남았다. `find` 출력으로 같은 이름의 파일이 서로 다른 두 path에 존재하는 것과 대소문자 무시 검색 결과를 확인했다. ^[raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md]

명령 전후에는 `pwd`로 기준 위치, `ls`·`tree`로 대상과 결과를 확인한다. 특히 `cp`·`mv`의 목적지가 이미 존재하는 파일이면 덮어쓸 수 있고, `rm -rf`는 되돌리기 어려우므로 **실행 주체 → 현재 위치 → source → destination → 실행 후 목록** 순으로 확인한다.

## 파일 내용을 읽고 비교하는 명령

- `cat`: 파일 전체를 출력하고, redirection의 입력으로 사용했다.
- `head -n`, `tail -n`: `total.txt`의 앞·뒤 일부를 확인했다.
- `grep`: 파일 내용에서 pattern을 찾았다. `-i`는 대소문자 무시, `-n`은 line number, `-w`는 whole word 조건이었다.
- `more`: 긴 파일이나 pipe 출력을 화면 단위로 읽었다. 파일을 수정하는 명령이 아니다.
- `diff --brief`: 두 파일이 다른지만 확인했다.
- `diff`: `6c6`, `11c11`과 왼쪽 `<`·오른쪽 `>` 내용을 보여 주어 실제 변경 line을 검증했다.

`find`는 파일 시스템 **entry의 위치**를 찾고, `grep`은 파일 **내용의 pattern**을 찾는다는 책임 차이가 중요하다.

## redirection: 출력이 파일 상태가 되는 과정

04-23에는 Java keyword 파일과 Python keyword 파일을 `total.txt`로 조합했다.

1. `cat`의 출력을 `>`로 보내 새 결과 파일을 만들었다.
2. 다른 파일을 다시 `>`로 보내자 기존 내용이 사라졌다.
3. 원본을 복원한 뒤 `>>`로 두 번째 파일과 문자열을 누적했다.
4. `head`, `tail`, `grep`, `more`로 내용을 읽고, 별도 수정본은 `diff`로 비교했다.

따라서 `>`는 “오른쪽에 기록”만이 아니라 **기존 파일을 새 출력으로 대체할 수 있는 동작**이고, `>>`는 기존 끝에 추가한다. 중요한 설정에는 먼저 backup을 만들고 대상 path를 확인한 뒤 사용한다.

## vi를 이 Concept에 흡수하는 이유

vi는 04-23의 파일 생성·수정·검색·redirection 검증 흐름 안에서 등장한 terminal editor다. 별도 독립 페이지를 만들기보다 “CLI에서 파일 내용을 안전하게 바꾸는 단계”로 이 Concept가 책임진다.

| 모드 | 실제 역할 | 핵심 전환 |
|---|---|---|
| 명령 모드 | cursor 이동, 삭제·undo·복사·붙여넣기 | vi 시작 상태이며 `Esc`로 돌아온다. |
| 입력 모드 | text 입력 | `i`는 cursor 앞, `a`는 cursor 뒤에서 입력을 시작한다. 수업에서는 `o`로 아래 새 line도 열었다. |
| 마지막 행/실행 모드 | 저장·종료·검색·치환·외부 명령 읽기 | 명령 모드에서 `:`, `/`, `?`로 들어간다. |

- `:w`: 저장
- `:q`: 종료
- `:wq`: 저장 후 종료
- `:q!`: 변경을 저장하지 않고 강제 종료
- `/문자열`: 아래 방향 검색
- `:set nu` / `:set nonu`: line number 표시 전환
- `:%s/기존/새값/g`: 전체 치환

실습에서는 `java.txt`·`python.txt`를 만든 뒤 `Esc`와 `:wq`로 저장하고 `cat`으로 확인했다. `.bak` 파일을 먼저 만든 뒤 `dd`, `3dd`, `u`, `yy`, `3yy`, `p`로 수정·복구를 반복했다. 즉, vi의 완료 기준은 “화면에서 편집했다”가 아니라 **저장 여부를 선택하고, 편집기 밖에서 결과를 다시 확인하는 것**이다.

## Librarian 실습의 근거 경계

04-23 5~6교시는 두 번째 VM의 Librarian session에서 별도 PDF page를 따라 directory 실습을 복습했다. 날짜 MD에는 page 범위만 있고 세부 명령·출력이 없으므로, 첫 VM 방송사 실습 결과를 Librarian에서도 동일하게 성공했다고 합치지 않는다.

## 자주 헷갈리는 점과 선택 기준

1. **root directory와 root home**: `/`는 전체 tree의 뿌리이고 `/root`는 관리자 계정의 home이다.
2. **절대·상대 경로**: 절대 경로는 항상 더 좋은 방식이 아니다. script·server 관리처럼 기준 고정이 중요하면 절대 경로, 현재 tree 안의 짧은 작업이면 상대 경로가 편하다.
3. **`cp`와 `mv`**: `cp`는 원본을 남기고, `mv`는 위치나 이름을 바꾼다. 둘 다 목적지 path를 잘못 쓰면 의도하지 않은 덮어쓰기가 생길 수 있다.
4. **`find`와 `grep`**: entry 이름/path 검색과 파일 내용 검색을 구분한다.
5. **`cat`과 `more`**: 둘 다 읽지만 `more`는 긴 내용을 page 단위로 탐색할 때 쓴다.
6. **`>`와 `>>`**: 덮어쓰기와 누적이다. 실행 전에 대상 내용을 `cat`이나 backup으로 확인한다.
7. **vi 입력과 명령**: 글자를 넣은 상태에서 `:wq`를 그대로 입력하지 않는다. `Esc`로 명령 모드에 돌아온 뒤 마지막 행 명령을 사용한다.

## 선행·후속 연결과 과목 경계

- 선행: [[summaries/2026-04-22-linux-install-ssh-cli|04-22 Linux 설치·SSH·CLI]]에서 VM 접속과 prompt·경로 기준을 만들었다.
- 직접 확장: [[summaries/2026-04-23-linux-files-vi|04-23 파일·vi]]에서 실제 파일 tree와 내용을 바꿨다.
- 다음: [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]은 같은 파일을 “누가 읽고·쓰고·실행할 수 있는가”로 확장한다.
- 후속 활용: Docker bind mount·배포 파일·로그, AWS EC2의 server file, CI/CD의 배포 script에서 같은 CLI 기술을 재사용한다. 그러나 container·cloud resource·workflow의 구현 성공은 각각 Docker·AWS·CI/CD 후속 수업의 책임이다.

## 관련 페이지

- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-cp-exec-container-files|Docker exec/cp와 컨테이너 파일 다루기]]
- [[entities/linux|Linux]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` — prompt·root/home·절대/상대 경로의 첫 수업
- `raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md` — 방송사 tree·파일 상태 변화·vi·redirection·검색·비교의 최우선 근거
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — CLI·파일·vi의 과목 전체 연결을 보조하는 복습 허브
