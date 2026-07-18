---
title: sudo로 만든 디렉터리는 왜 일반 사용자로 수정·복사할 수 없는가
created: 2026-07-18
updated: 2026-07-18
type: query
tags: [linux, debugging, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: stable
confidence: high
---

# sudo로 만든 디렉터리는 왜 일반 사용자로 수정·복사할 수 없는가

## 질문

`sudo`로 만든 디렉터리는 왜 일반 사용자로 파일을 만들거나 MobaXterm으로 복사할 때 `Permission denied`가 나는가?

이 제목은 04-24·04-27의 반복 오류를 다시 찾기 위한 troubleshooting 질문이다. 사용자의 별도 대화 문장을 수업 원문 인용으로 만든 것은 아니다. 04-27 원본에는 drag-and-drop 실패 뒤 실제로 “why?”가 기록돼 있다.

## 짧은 답

`sudo mkdir`의 `mkdir` process가 root 권한으로 실행되면 새 directory의 owner/group이 root가 될 수 있다. 일반 사용자는 owner가 아니고, group/others에도 목적지 directory의 **쓰기(`w`)와 경로 통과(`x`) 권한**이 충분하지 않으면 내부 entry를 생성·복사·이름 변경할 수 없다. 먼저 실행 사용자·owner/group·directory permission을 확인한 뒤, 원래 일반 사용자가 관리할 directory라면 ownership을 의도한 사용자에게 넘기거나 필요한 최소 permission을 설정한다.

## 왜 오류가 생기는가

### 1. 명령 실행 주체가 달라졌다

일반 사용자 prompt에서 입력했더라도 `sudo mkdir`의 실제 directory 생성은 관리자 권한으로 실행된다. 04-24의 `ytn`, 04-27의 download directory는 `ls -l`에서 owner/group이 root로 확인됐다.

### 2. directory permission은 file permission과 다르게 읽는다

- `r`: directory entry 이름 목록을 읽는 데 관련된다.
- `w`: directory 안에 entry를 생성·삭제·이름 변경하는 데 관련된다.
- `x`: 해당 directory를 통과해 내부 entry에 접근하는 데 관련된다.

새 file을 만들거나 외부 file을 복사하려면 목적지 directory의 `w`와 경로를 통과할 `x`가 필요하다. 복사할 file 자체가 읽기 가능하다는 사실만으로 목적지에 쓸 수 있는 것은 아니다.

### 3. owner/group/others 중 현재 사용자가 적용받는 묶음이 다르다

root-owned directory가 일반적인 `drwxr-xr-x`라면 root owner만 쓰기 가능하고 group/others에는 쓰기가 없다. 일반 사용자는 해당 directory 안을 읽거나 통과할 수 있어도 새 file을 만들 수 없다.

## 실제 수업 사례 1: 2026-04-24 `ytn`

1. **입력**: 일반 사용자 home에서 관리자 권한으로 `ytn` directory 생성.
2. **관찰**: `ls -l`에서 owner/group이 root로 표시됨.
3. **오류**: 일반 사용자 `touch`가 `Permission denied`로 실패.
4. **처리**: `chown -R`로 owner/group을 일반 사용자에게 이전.
5. **결과**: 같은 위치에 file 생성 성공, directory 목록에서 확인.

이 사례는 command 문법 오류가 아니라 **생성 process의 권한 → ownership → 목적지 directory write permission**의 문제였다.

## 실제 수업 사례 2: 2026-04-27 MobaXterm drag-and-drop

1. **입력**: 일반 사용자 home 아래 download directory를 `sudo mkdir`로 생성.
2. **오류**: Windows file을 MobaXterm drag-and-drop으로 복사하려 했지만 실패.
3. **진단**: 상세 목록에서 root owner/group 확인.
4. **처리**: 해당 directory의 ownership을 일반 사용자에게 이전.
5. **결과**: drag-and-drop 성공, archive 존재 확인, 압축 해제 진행.

겉으로는 “MobaXterm 복사 오류”처럼 보였지만 원인은 SSH client가 아니라 Linux 목적지 directory의 ownership이었다.

## 진단 순서

1. **실행 주체 확인**: 현재 login user와 root session 여부를 확인한다.
2. **정확한 목적지 확인**: `pwd`와 전체 path를 확인한다.
3. **경로의 directory 상태 확인**: 대상과 상위 directory의 owner/group·permission을 상세 목록으로 확인한다.
4. **필요 동작 판정**: 읽기, file 생성, 복사, 삭제, 실행 중 무엇이 필요한지 정한다.
5. **최소 수정 선택**:
   - 일반 사용자가 소유해야 할 작업 directory라면 ownership 교정
   - 공유 group 작업이라면 group owner와 group permission 설계
   - owner는 유지해야 한다면 필요한 permission만 조정
6. **같은 작업 재시도**: file 생성·복사 결과와 목록을 다시 확인한다.

## `chown`과 `chmod` 중 무엇을 써야 하는가

| 상황 | 우선 검토 | 이유 |
|---|---|---|
| 일반 사용자 개인 작업 directory를 실수로 root가 생성 | `chown` | 관리 주체인 owner를 바로잡음 |
| 여러 사용자가 공유 group으로 작업 | group owner·group permission | 개인 owner 변경만으로 공유 정책이 완성되지 않음 |
| owner는 맞지만 필요한 동작 bit만 부족 | `chmod` | ownership은 유지하고 access rights만 조정 |
| 원인 확인 없이 임시로 모두 허용 | 피함 | `777`은 과도하며 ownership 오류를 숨길 수 있음 |

`chown`은 owner/group을, `chmod`는 permission bit를 바꾼다. 같은 문제처럼 보여도 바꾸는 field가 다르다.

## 자주 틀리는 판단

- **“sudo를 썼으니 이후에도 sudo로만 작업한다”**: root 소유 artifact를 더 늘릴 수 있다.
- **“파일 permission만 보면 된다”**: 목적지와 상위 directory의 `w`·`x`가 중요하다.
- **“MobaXterm 문제다”**: client가 전송하더라도 server-side 목적지 permission이 최종 결정을 한다.
- **“무조건 `chmod 777`”**: 최소 권한과 owner/group 설계를 건너뛴다.
- **“directory가 보이니 쓸 수 있다”**: 목록 읽기와 내부 entry 생성은 다른 권한이다.

## 확인된 범위와 후속 경계

- 직접 확인: 04-24 `touch` 실패→ownership 변경→성공, 04-27 drag-and-drop 실패→ownership 변경→성공.
- 별도 오류: script의 `x` 부족으로 실행이 막힌 사례는 file execute permission 문제다. root-owned directory 문제와 같은 `Permission denied` 문자열만 보고 합치지 않는다.
- Docker 후속: Docker group 등록 뒤 현재 session에는 권한이 반영되지 않아 logout/login이 필요했던 문제는 group membership·session 반영 문제다.
- AWS/CI/CD 후속: EC2 login user·SSH key·deploy user permission은 같은 원리를 재사용하지만 직접 artifact와 정책은 후속 과목 책임이다.
- ACL, umask, setgid directory, sticky bit, SELinux/AppArmor, mount read-only 상태는 현재 원본에서 이 오류의 원인으로 실습하지 않았다.

## 참고한 위키 페이지

- [[summaries/2026-04-24-linux-users-permissions|2026-04-24 사용자·그룹·권한]]
- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27 압축·Java·웹서버]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[comparisons/sudo-vs-sudo-su-vs-root-session|sudo vs sudo su - vs root session]]
- [[entities/linux|Linux]]

## 다음에 볼 것

1. [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]의 file/directory `r/w/x` 차이
2. [[comparisons/sudo-vs-sudo-su-vs-root-session|sudo vs sudo su - vs root session]]의 권한 범위와 artifact owner
3. [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]의 group membership·재로그인 문제

## 출처

- `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md` — root 소유 `ytn`, 일반 사용자 file 생성 실패, ownership 이전 후 성공
- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` — root 소유 download directory, drag-and-drop 실패, ownership 이전 후 archive 반입 성공
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — user/group/permission과 server·Docker 후속 연결 보조
