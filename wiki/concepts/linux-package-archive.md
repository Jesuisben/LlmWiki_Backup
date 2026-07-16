---
title: Linux 패키지·다운로드·압축
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux 패키지·다운로드·압축

## 이 Concept의 책임

서버에 필요한 **도구를 package로 설치하는 단계**, 외부 **파일을 download하는 단계**, 파일·directory를 **archive로 묶거나 압축·해제하는 단계**를 분리한다. 세 단계는 연이어 쓰이지만 같은 작업이 아니다.

## 왜 필요한가

04-22에는 SSH 접속과 directory tree 확인에 필요한 `openssh-server`, `tree` 같은 OS package를 설치했다. 04-27에는 외부 Vim source archive를 세 방식으로 가져와 풀고, 방송사 directory를 zip artifact로 만들어 옮겼다. 이후 Java·웹서버·Docker·배포 파일 준비도 “필요한 도구와 artifact를 server에 가져와 확인한다”는 이 기초 위에 놓인다.

## package 설치: OS가 관리하는 도구 준비

Ubuntu/Debian 계열의 `apt`는 package index와 설치 상태를 관리한다.

- `apt update`: 설치 가능한 package 정보(index)를 최신화한다. application 자체를 실행하는 명령이 아니다.
- `apt install`: 지정 package를 설치한다.
- `-y`: 설치 과정의 확인 질문에 자동 동의한다.
- 설치 후 확인: `tree`처럼 명령을 직접 실행하거나, OpenJDK는 `java -version`, Apache·Nginx·SSH는 별도의 `systemctl status`로 확인했다.

04-22의 OpenSSH 사례에서 **설치와 service 실행은 별도**였다. package가 설치되어도 `systemctl start ssh`와 `status`의 `active (running)` 확인 전에는 원격 접속 service 성공으로 보지 않는다. 04-27의 JDK도 `apt update → apt install → java -version`으로 단계별 확인했다. ^[raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md]

## download: 원격 파일을 현재 파일 시스템으로 가져오기

04-27에는 같은 Vim source archive를 `wget`, `curl`, Windows drag-and-drop으로 가져왔다.

| 방식 | 수업에서의 역할 | 생성된 artifact 확인 |
|---|---|---|
| `wget` | URL에서 파일을 내려받고 원격 파일명을 유지 | `v9.1.0000.tar.gz`가 `ls`에 나타남 |
| `curl -L -o` | redirect를 따라가고 local 저장 이름을 직접 지정 | `vim.tar.gz`가 `ls`에 나타남 |
| MobaXterm drag-and-drop | Windows file을 SSH session의 Linux directory로 복사 | 권한 해결 뒤 archive가 directory에 나타남 |

`wget`과 `curl`은 file transfer 도구다. Vim source나 JDBC JAR를 내려받았다고 package 설치·compile·DB 연결이 끝난 것이 아니다. 반대로 `apt install`은 OS package를 관리하며 임의 URL의 file을 지정 이름으로 저장하는 역할이 아니다.

## archive와 압축: 묶기·압축·해제의 흐름

`tar`는 여러 entry를 하나의 archive로 묶거나 푼다. `.tar.gz`는 tar archive에 gzip 압축이 적용된 형식이다. 수업의 `tar -xzvf`에서 `x`는 extract, `z`는 gzip 처리, `v`는 처리 항목 출력, `f`는 뒤의 archive file 지정이었다.

`zip -r`은 directory 하위까지 zip archive로 만들었고, `unzip`은 Windows에서 가져온 homepage zip을 풀었다.

| 작업 | 입력 | 처리 | 결과 확인 |
|---|---|---|---|
| Vim tar.gz 해제 | download한 `v9.1.0000.tar.gz` 또는 `vim.tar.gz` | `tar -xzvf` | archive와 `vim-9.1.0000` directory가 함께 보이고 내부 source 목록을 확인 |
| 방송사 directory 압축 | `morning_garden`, `infinite_challenge`의 현재 내용 | 각 directory에서 `zip -r ... .` | `morning_garden.zip`, `infinite_challenge.zip` 생성 후 다른 directory로 이동 |
| homepage 해제 | Windows에서 옮긴 `my_homepage.zip` | `unzip` | 해제된 web file을 확인한 뒤 Apache document root로 복사 |

archive를 만들거나 푼 다음에는 즉시 `ls`·`tree`로 **생성된 파일명과 해제 directory**를 확인한다. 그 뒤의 `mv`·`cp`는 archive 작업이 아니라 위치를 바꾸는 별도 file operation이다. ^[raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md]

## 실제 실습 1: download → extract → directory 확인

1. **입력**: 빈 `wgettest` 또는 `curltest` 작업 directory와 동일한 원격 Vim archive였다.
2. **처리**: `wget`은 원격 이름을 유지했고, `curl -L -o`는 `vim.tar.gz`라는 local 이름을 지정했다. 각각 `tar -xzvf`로 해제했다.
3. **결과**: download 전에는 비어 있던 directory에 archive가 생겼고, 해제 후에는 `vim-9.1.0000` directory가 추가되었다. 그 안에서 `src`, `runtime`, README, Makefile 등 source tree를 확인했다.

이 흐름의 완료 지점은 “명령이 끝났다”가 아니라 **download file 존재 → extract directory 존재 → 내부 목록 확인**이다.

## 실제 실습 2: 권한 때문에 file 반입·archive 이동이 막힌 경우

Windows archive를 받을 directory를 `sudo mkdir`로 만들자 owner/group이 root가 되었다. 일반 사용자 MobaXterm drag-and-drop은 `Permission denied`로 실패했고, `ls -al`로 ownership을 확인한 뒤 `chown -R`로 일반 사용자에게 넘기자 복사가 가능해졌다.

방송사 directory를 zip으로 만들고 목적지로 옮길 때도 owner와 directory 접근 권한을 먼저 조정했다. 따라서 archive 명령 오류처럼 보여도 다음 순서로 나눈다.

1. 현재 사용자와 source·destination path를 확인한다.
2. `ls -ld` 또는 상세 목록으로 directory owner/group과 permission을 확인한다.
3. 필요한 경우 ownership 또는 최소 권한을 바로잡는다.
4. archive 생성·이동을 다시 수행하고 결과 파일을 확인한다.

무조건 `777`을 주는 것은 package·archive의 해결법이 아니다. 원인은 [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]에서 분리해 판단한다.

## 선택 기준과 자주 헷갈리는 점

1. **`apt install` vs `wget`/`curl`**: repository가 관리하는 OS 도구는 `apt`, 특정 URL의 artifact를 파일로 보존할 때는 `wget`/`curl`을 사용한다.
2. **`wget` vs `curl`**: 수업에서는 원격 이름 유지가 편하면 `wget`, redirect 추적과 local 이름 지정이 필요하면 `curl -L -o`를 사용했다.
3. **tar vs gzip**: tar는 archive 묶음, gzip은 압축이다. `.tar.gz`는 둘이 결합된 결과다.
4. **zip vs unzip**: `zip -r`은 묶어 압축하고 `unzip`은 해제한다. 수업에서는 `zip` package를 먼저 설치했다.
5. **download vs extract vs move**: `curl`로 저장하고, `tar`로 풀고, `mv`로 옮기는 세 단계의 입력과 결과를 따로 확인한다.
6. **설치 후 확인**: package manager가 끝난 것, 명령 version이 보이는 것, service가 active인 것, browser 결과가 나오는 것은 서로 다른 완료 조건이다.
7. **삭제 위험**: download test 정리의 `rm -rf`는 archive 해제가 아니라 tree 삭제다. `pwd`·목록·대상 path를 확인한 뒤 사용한다.

## 직접 수업과 후속 활용 경계

- Linux 직접 수업: OpenSSH·tree·zip·JDK·Apache·Nginx package 설치, Vim/JDBC/homepage file download, tar/zip/unzip artifact 확인.
- Docker 후속: Docker setup package와 image build context를 준비할 때 같은 package·file 기술을 재사용한다. Docker image 자체는 archive 해제 결과와 동일하지 않다.
- AWS EC2 후속: cloud VM에 package와 배포 artifact를 준비하지만 EC2·Security Group·cloud resource 성공은 AWS 과목 책임이다.
- CI/CD 후속: workflow가 build artifact와 image를 자동 준비하지만, 04-27에는 자동 pipeline을 구현하지 않았다.

## 선행·후속 연결

- 선행: [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]의 path·`ls`·`mkdir`·`mv`가 모든 작업 위치와 결과 확인의 기반이다.
- 직접 수업: [[summaries/2026-04-27-linux-archive-java-alias|04-27 압축·Java·웹서버]]에서 download/archive/permission을 실제로 연결했다.
- 다음: [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]은 package로 JDK·Maven을 준비하고 source를 JAR artifact로 build한다.
- 권한 진단: [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]은 root 소유 directory와 이동 실패 원인을 설명한다.

## 관련 페이지

- [[summaries/2026-04-22-linux-install-ssh-cli|04-22 Linux 설치·SSH·CLI]]
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[entities/maven|Maven]]
- [[entities/linux|Linux]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` — `apt` package 설치와 설치·service 실행 분리
- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` — download·tar/zip/unzip·권한 오류·artifact 확인의 최우선 근거
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — package·download·archive와 후속 server 준비의 연결 보조
