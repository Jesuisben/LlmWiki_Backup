---
title: Linux 내용 재고도화 전수 재고와 실행 분할 계획
created: 2026-07-16
updated: 2026-07-16
type: meta
tags: [linux, docker, github, spring-boot, curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-content-rehighquality-work-plan.md
  - wiki/_meta/frontend-backend-rehighquality-inventory-plan.md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux 내용 재고도화 전수 재고와 실행 분할 계획

## 문서 상태와 범위

이 문서는 내용 재고도화 단계 5 `Linux`의 **세션 1 재고·대응·분류·실행 분할 기준선**이자 분할 세션별 실행 기록이다. 세션 2에서는 Summary 전반부 R01~R05, 세션 3에서는 Summary 후반부·총정리 R06~R11, 세션 4에서는 CLI·파일·vi·권한 Concept 3개만 고도화했다.

- 현재 상태: **미완료 — 세션 4 CLI·파일·vi·권한 Concept까지 완료**
- 세션 4 수정 범위: 지정 Concept 3개, 이 meta 문서, `wiki/log.md`
- 세션 4 비수정 범위: `raw/` 전체, Summary·Entity·Comparison·Query, 다른 Concept, `wiki/index.md`, 상위 계획의 단계 5 완료 기록
- 다음 실행 단위: 세션 5 `VM·SSH·process·service·network·server Concept/Entity`
- 다음 세션 자동 실행: 하지 않음

## 작업 전 기준선

- 직전 완료 단계: 단계 4 FrontEnd_BackEnd 세션 16 전체 고정점
- 직전 고정점: FrontEnd_BackEnd 지식 페이지 59개, R01~R19·P01~P10·I01~I05 전수 대응, code fence 2/2 원문 일치, Total pages 269
- 저장소 전체: 기존 FrontEnd_BackEnd 지식 페이지 변경, Python raw 변경, Machine Learning raw·사용자 학습 가이드·Query untracked 변경이 존재한다. 모두 이번 Linux 작업과 분리해 보존한다.
- `raw/KoreaICT/5. Linux` 시작 scoped status: 항목 0건
- `raw/KoreaICT/5. Linux` 시작 scoped diff: 항목 0건
- Linux 직접 source 지식 페이지 시작 scoped status/diff: 항목 0건
- `raw/`는 읽기 전용이며 이 계획 작성 과정에서 수정하지 않는다.

## raw 전수 재고 요약

- 실제 파일: **24개**
- 전체 크기: 23,940,604 bytes
- Markdown: **14개**
  - 날짜별 수업 MD: 10개
  - Linux 총정리 MD: 1개
  - 문서형 교육자료 MD: 3개
- PDF: **7개**
- PNG: **3개**
- 날짜별·총정리 MD 11개의 총 줄 수: 8,072줄
- 문서형 교육자료 MD 3개의 총 줄 수: 244줄
- 전체 MD 14개의 총 줄 수: 8,316줄
- 0바이트 파일: 0개
- 과목 내부 byte-identical 중복: 0개
- `raw/KoreaICT` 다른 과목과의 byte-identical 중복: 0개
- 독립 소스 코드·설정·압축 파일: 0개. 코드·명령·출력·설정은 MD 안의 fence 또는 PDF에 포함된다.

## raw 식별자와 실제 전체 경로

식별자는 날짜별/총정리 MD `R`, PDF·문서형 교육자료 `P`, 이미지 `I`로 나눈다. 현재 그 밖의 artifact는 없어 별도 `X` 식별자는 만들지 않는다.

### 날짜별 Markdown과 총정리

| ID | 실제 전체 경로 | 실제 수업일 | 대표 artifact·명령·실습 |
|---|---|---|---|
| R01 | `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` | 2026-04-22 | VirtualBox Ubuntu VM, bridge network, OpenSSH, `systemctl`, MobaXterm SSH, prompt, `/` 구조, 절대/상대 경로 |
| R02 | `raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md` | 2026-04-23 | `tree`, `mkdir`, `touch`, `cp`, `mv`, `find`, vi 3모드, `>`·`>>`, `more`, `diff`, Librarian 세션 |
| R03 | `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md` | 2026-04-24 | `ls -l`, user/group, `/etc/passwd`·`shadow`·`group`, `useradd`·`groupadd`, `chmod` 숫자/기호, `chown`·`chgrp`, shell·process 기초 |
| R04 | `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` | 2026-04-27 | `wget`·`curl`, tar/zip, `rm -rf`, alias와 `.sh`, JDK/JDBC·Java 실행, Git remote, Apache/Nginx, UFW |
| R05 | `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` | 2026-04-28 | Maven package, `java -jar`, 80→9000 iptables/UFW, Docker 설치·권한, image/container, httpd/nginx/MySQL/WordPress |
| R06 | `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` | 2026-04-29 | MariaDB+Redmine network, `docker exec`·`cp`, bind mount/volume, `docker commit`, Docker Hub push, AWS 가입 안내 |
| R07 | `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` | 2026-04-30 | Dockerfile build context, Spring Boot+MySQL container, `ARG`·`COPY`·`ENTRYPOINT`, nginx upstream/proxy_pass load balancing |
| R08 | `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` | 2026-05-01 | Compose YAML, MySQL+Spring Boot services/network/volume/environment/depends_on, Docker Desktop, backend 시험 |
| R09 | `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md` | 2026-05-04 | Git Bash, init/status/add/commit/push/pull/clone/fetch, SourceTree, 두 작업자 충돌, branch 협업 시작 |
| R10 | `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md` | 2026-05-06 | 팀원 branch, IntelliJ Git, Pull Request·검토·merge, master pull, conflict, fetch, merge/rebase 실습 |
| R11 | `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` | 2026-04-22~05-06 복습 | VM/SSH→CLI/권한→Java/Spring server→Docker/Compose→Git/GitHub 전체 복습 허브 |

### PDF·문서형 교육자료

| ID | 실제 전체 경로 | 형식 | 역할·경계 |
|---|---|---|---|
| P01 | `raw/KoreaICT/5. Linux/교육 자료/AWS 계정 생성 및 MFA 로그인.pdf` | PDF, 30쪽 | 04-29의 AWS 계정 준비 보조자료. Linux 직접 운영 지식과 단계 6 AWS 본수업을 구분한다. |
| P02 | `raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` | PDF, 132쪽 | Docker container/network/mount/image/Dockerfile/Compose 실습의 보조 근거 |
| P03 | `raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` | PDF, 114쪽 | image/container, mount, Dockerfile/Compose 이론 보조 근거 |
| P04 | `raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf` | PDF, 188쪽 | Git Bash·SourceTree·branch·PR·conflict 협업 보조 근거 |
| P05 | `raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 실습(Librarian).pdf` | PDF, 89쪽 | R02의 Librarian 별도 세션 파일·디렉터리 실습 보조 근거 |
| P06 | `raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` | PDF, 211쪽 | VM·SSH·CLI·사용자·권한·Java·웹서버까지 Linux 실습의 주 교안 |
| P07 | `raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 이론.pdf` | PDF, 183쪽 | 파일 시스템·경로·shell·권한·mount 등 Linux 이론 보조 근거 |
| P08 | `raw/KoreaICT/5. Linux/교육 자료/docker image를 docker hub에 업로드 하기.md` | Markdown | commit image의 tag/login/push/pull 절차. 실제 계정·주소·credential은 wiki에서 일반화한다. |
| P09 | `raw/KoreaICT/5. Linux/교육 자료/도커 컴포즈 종합 실습.md` | Markdown | OpenSSH/UFW/Docker setup과 Compose 종합 실습 체크리스트 |
| P10 | `raw/KoreaICT/5. Linux/교육 자료/리눅스 실습하기.md` | Markdown | OpenSSH 설치·시작·상태·종료 9줄 보조 메모. 독립 수업일 근거로 사용하지 않는다. |

### 이미지

| ID | 실제 전체 경로 | 크기 | 역할 |
|---|---|---:|---|
| I01 | `raw/KoreaICT/5. Linux/교육 자료/AccessRights.png` | 1437×1094 | owner/group/others의 read/write/execute 권한 설명 보조 |
| I02 | `raw/KoreaICT/5. Linux/교육 자료/OwnerShip.png` | 1691×930 | 파일 소유자·그룹과 권한 구조 설명 보조 |
| I03 | `raw/KoreaICT/5. Linux/교육 자료/로드 밸런싱.png` | 580×263 | 여러 사용자의 요청을 상담자 두 명에게 분배하는 비유 그림. 기술적 port/network 구성 증거로 사용하지 않는다. |

## 중복·보조자료·부재 artifact 경계

- 날짜별 MD가 수업일과 실제 실습 순서의 최우선 근거다. PDF·이미지·교육자료 MD는 보조 근거이며 날짜 귀속을 새로 만들지 않는다.
- R11은 날짜별 MD를 대체하지 않는 과목 복습 허브다.
- P10은 9줄짜리 보조 메모이며 R01의 OpenSSH 흐름을 반복한다. 삭제·통합하지 않고 보조자료로 보존한다.
- P01은 Linux 폴더에 있지만 AWS 계정 준비 자료다. 04-29의 다음 과목 예고만 설명하며 단계 6 AWS 본수업을 Linux 직접 구현으로 소급하지 않는다.
- R06의 Docker Hub 실습에는 계정명·저장소 주소·credential 경고가 등장한다. 향후 지식 페이지에는 역할과 명령 구조만 남기고 실제 식별자·민감값은 일반화한다.
- 독립 `Dockerfile`, Compose YAML, shell script, Java source, nginx config 파일은 현재 raw 재고에 없다. 향후 fence provenance는 MD 안의 실제 연속 원문 또는 PDF/이미지 수동 근거로 구분한다.

## 학습축과 직접 수업 범위

| 학습축 | 주 raw | 직접 수업의 핵심 | 선행·후속 경계 |
|---|---|---|---|
| VirtualBox Ubuntu 설치와 VM | R01, P06 | VM 생성, Ubuntu 설치, bridge 설정, IP 확인 | FrontEnd_BackEnd 로컬 앱 이후 서버 OS 입문. EC2는 후속 cloud VM이다. |
| SSH·MobaXterm·network | R01, P06, P10 | OpenSSH service, 22번/UFW, VM IP, MobaXterm session | AWS에서는 Key Pair·Security Group·Public IP가 추가된다. |
| Linux 경로·파일·디렉터리·redirection | R01~R02, P05~P07 | 절대/상대 경로, 생성·복사·이동·검색, `>`·`>>`, `more`, `diff` | Docker bind mount·배포 파일·로그를 읽는 선행 기초다. |
| vi | R02, P05~P07 | 명령/입력/마지막 행 모드, 저장·종료·수정 | 서버 설정·HTML·nginx/Docker 관련 파일 편집의 선행 도구다. |
| 사용자·그룹·권한·sudo | R03~R05, I01~I02, P06~P07·P09 | account files, UID/GID, chmod 숫자/기호, chown/chgrp, sudo, Docker group | EC2의 `ubuntu` 사용자·SSH key 권한과 CI/CD deploy user로 확장된다. |
| process·service·port | R01, R03~R05, R11 | `ps`·`grep`·`kill`, `systemctl`, SSH/Apache/Nginx, UFW/iptables, 22·80·9000 | AWS Security Group/ALB와 CI/CD health verification은 후속 적용이다. |
| Java/Spring Boot jar 실행 | R04~R05, R07, R11 | JDK/JDBC, Maven package, `java -jar`, port, Dockerfile | FrontEnd_BackEnd 앱을 Linux에서 실행하며 AWS EC2·CI/CD 배포의 선행 실습이 된다. |
| Docker image/container/volume/network | R05~R07, P02~P03·P08, R11 | image/container 생명주기, port mapping, network, exec/cp, bind/volume, commit/build/push | CI/CD에서는 Docker Hub image가 자동 배포 단위가 된다. |
| Docker Compose | R08, P02~P03·P09, R11 | MySQL+Spring Boot 다중 service, YAML, network/volume/environment | Passwordless Docker 서버와 프로젝트 로컬 통합환경은 후속 활용이다. |
| Git·GitHub 협업 | R09~R10, P04, R11 | local/remote, SourceTree, branch, PR, merge, conflict, fetch/rebase | Java의 개인 저장소 사용을 팀 협업으로 확장하고 CI/CD push trigger로 이어진다. |
| Linux→AWS EC2·CI/CD 후속 활용 | R06의 AWS 예고와 후속 과목 raw/wiki | Linux 명령·port·Docker·Git을 후속 환경에서 재사용 | AWS/CI/CD의 직접 학습일·자원·workflow 결과는 각각 단계 6·7에서 고도화한다. |

## 기존 Linux 직접 source 지식 페이지

frontmatter `sources`가 `raw/KoreaICT/5. Linux`를 직접 참조하는 지식 페이지는 **35개**다.

- 실제 디렉터리 기준: `summaries 11 / concepts 13 / entities 6 / comparisons 5 / queries 0`
- frontmatter `type` 기준: `summary 11 / concept 12 / entity 6 / comparison 6 / query 0`
- 차이 원인: `wiki/concepts/dockerfile-vs-compose.md`는 위치는 `concepts/`지만 frontmatter `type: comparison`이다. 이번 단계에서는 무단 이동하지 않고 comparison으로 처리한다.

### Summary 대응 및 분류

| wiki 경로 | raw·실제 수업일 | 대표 artifact·실습 | 분류 | 누락·오류·중복 책임 | 직접 Linux / 후속 경계 | 예정 세션 |
|---|---|---|---|---|---|---:|
| `wiki/summaries/2026-04-22-linux-install-ssh-cli.md` | R01, 04-22 | VM→bridge→SSH service→MobaXterm→경로 | 전면 재작성 완료 | VM 2대·service 상태·bridge/IP/22번 접속·prompt·절대/상대 경로와 EC2 후속 경계를 복원 | Linux 시작 직접 / EC2는 후속 | 2 완료 |
| `wiki/summaries/2026-04-23-linux-files-vi.md` | R02, 04-23 | 방송사 tree, 파일 조작, vi, redirect, Librarian | 전면 재작성 완료 | 방송사 tree→파일 상태 변화→vi 3모드→redirection·grep·more·diff 순서와 실제 오류·결과를 복원 | Linux CLI 직접 / 배포 파일은 후속 활용 | 2 완료 |
| `wiki/summaries/2026-04-24-linux-users-permissions.md` | R03, 04-24 | user/group/account files/chmod/chown | 전면 재작성 완료 | account files·UID/GID·shell·group·chmod 숫자/기호·chown/chgrp·script 실행과 “하지는 않음” 경계를 복원 | Linux 권한 직접 / EC2 user는 후속 | 2 완료 |
| `wiki/summaries/2026-04-27-linux-archive-java-alias.md` | R04, 04-27 | download/archive/alias/JDK/Java/Git/web server | 전면 재작성 완료 | download/archive·permission 오류→alias 지속성→Java compile/run→Git remote→Apache/Nginx/UFW 흐름을 복원 | Linux server 직접 / Spring·Docker 전단계 | 2 완료 |
| `wiki/summaries/2026-04-28-maven-spring-boot-docker-intro.md` | R05, 04-28 | Maven jar, 80→9000, Docker setup, web/DB containers | 전면 재작성 완료 | clone→Maven JAR→VirtualBox NAT·guest iptables/UFW→Docker 설치·생명주기→WordPress–MySQL `network01`을 복원 | Linux jar·Docker 직접 / AWS·CI/CD 후속 | 2 완료 |
| `wiki/summaries/2026-04-29-docker-network-volume-image.md` | R06, 04-29 | MariaDB+Redmine, exec/cp, mount, commit, Hub | 전면 재작성 완료 | network→exec/cp→bind/volume→commit→registry→다른 환경 pull/run과 AWS 가입 예고 경계를 복원 | Docker 직접 / AWS 가입은 예고 | 3 완료 |
| `wiki/summaries/2026-04-30-dockerfile-spring-load-balancing.md` | R07, 04-30 | Dockerfile, Spring+MySQL, nginx upstream | 전면 재작성 완료 | build context·instruction→DB/JAR/log/browser→proxy-net/upstream 분배와 빈 교시를 복원 | Docker 직접 / AWS LB는 후속 | 3 완료 |
| `wiki/summaries/2026-05-01-docker-compose.md` | R08, 05-01 | Compose MySQL+Spring, Desktop, backend 시험 | 전면 재작성 완료 | services/network/volume/environment/depends_on→up/status/DB/browser/down, Desktop·시험·Git 예고 경계를 복원 | Docker/Compose 직접 / Git은 다음 | 3 완료 |
| `wiki/summaries/2026-05-04-git-github-sourcetree.md` | R09, 05-04 | Git Bash·remote·clone/pull/fetch·SourceTree·conflict | 전면 재작성 완료 | WorkTree→stage→local→remote, commit 없는 push, clone·SourceTree·두 작업자 conflict와 branch 시작을 복원 | Linux 과목 협업 직접 / Actions 후속 | 3 완료 |
| `wiki/summaries/2026-05-06-github-branch-pr-conflict.md` | R10, 05-06 | branch→PR review→merge→pull→conflict/rebase | 전면 재작성 완료 | 팀장/팀원 branch·PR 검토·remote/local master·fetch·merge/rebase UI 범위와 같은 날 AWS 분리를 복원 | GitHub 협업 직접 / 같은 날 AWS는 별도 과목 | 3 완료 |
| `wiki/summaries/2026-05-06-linux-subject-review.md` | R01~R11 | 과목 전체 운영·컨테이너·협업 흐름 | 부분 보강 완료 | 날짜별 대표 artifact·전환 이유와 04-27 host 웹서버·04-29 registry·05-01 시험·직접/후속 경계를 가진 복습 허브로 보강 | Linux 허브 / AWS·CI/CD는 후속 | 3 완료 |

### Concept 대응 및 분류

| wiki 경로 | raw·수업일 | 대표 artifact | 분류 | 누락·오류·중복 책임 | 직접/후속 경계 | 예정 세션 |
|---|---|---|---|---|---|---:|
| `wiki/concepts/linux-cli-files.md` | R01~R02·R11 | path, file commands, redirect, vi | 부분 보강 완료 | 방송사 file 상태 변화, Librarian 근거 경계, prompt·절대/상대 path, vi 3모드·검색/치환, redirection·grep·more·diff 결과와 안전 확인 순서를 복원 | Linux 직접 / Docker·EC2·CI/CD 파일 작업은 후속 | 4 완료 |
| `wiki/concepts/linux-package-archive.md` | R01·R04·R11 | apt/wget/curl/tar/zip/chown | 부분 보강 완료 | package 설치·download·archive·move를 분리하고 Vim archive·zip artifact·unzip 결과, root 소유 directory의 `Permission denied`와 ownership 해결 흐름을 복원 | Linux 파일 준비 직접 / Docker setup·배포 artifact는 후속 | 4 완료 |
| `wiki/concepts/linux-users-permissions.md` | R03~R04·R11·I01~I02 | account files, chmod, chown | 부분 보강 완료 | 이미지 표시 요소를 한정 판독하고 UID/GID·기본/보조 group·directory `x`·sudo/root·숫자/기호 mode·chmod/chown/chgrp·script 실행 오류를 복원 | Linux 직접 / Docker group·EC2·CI/CD deploy user는 후속 | 4 완료 |
| `wiki/concepts/linux-spring-boot-server-deploy.md` | R05·R07·R11 | Maven→jar→port→Dockerfile | 부분 보강 | clone→Maven→jar 흐름은 유지 가능하다. VirtualBox NAT→guest 80→iptables 9000→Spring 9000과 container·CI/CD 경계를 분리 | Linux 직접 / EC2·Actions 후속 | 5 |
| `wiki/concepts/linux-web-server-apache-nginx.md` | 현재 R05·R07·R11, 실제 핵심은 R04 | systemctl/UFW, host webserver, Docker nginx | 근거 부족 | host Apache/Nginx 직접 실습은 04-27인데 frontmatter에 R04가 없다. host·container·reverse proxy 주장을 분리하고 source 재설계가 선행되어야 함 | Linux 직접 / AWS Nginx·ALB 후속 | 5 |
| `wiki/concepts/docker-install-permission-setup.md` | R05·R07~R08·P02·P09 | setup script, CRLF, chmod, docker group | 부분 보강 | root/sudo/socket/group 재로그인 흐름과 1개 합성 fence 원문 대조 필요 | Linux Docker 직접 | 6 |
| `wiki/concepts/docker-image-container.md` | R05~R07·R11·P03 | run/start/stop/rm/rmi, port | 부분 보강 | 날짜별 생명주기·기성/사용자 image·Hub 경계와 합성 fence 교정 필요 | Docker 직접 / CI image 후속 | 6 |
| `wiki/concepts/docker-cp-exec-container-files.md` | R05~R06·P02 | exec/cp host↔container | 부분 보강 | 실제 container/path·일회 복사·내부 수정/commit 관계와 합성 fence 교정 필요 | Docker 직접 | 6 |
| `wiki/concepts/docker-network-volume.md` | R06·R08·P02~P03 | Redmine+MariaDB, bind/volume, Compose | 부분 보강 | network/port/storage를 분리하고 15줄 합성 fence를 실제 연속 실습으로 재구성해야 함 | Docker 직접 / EC2 networking은 별도 | 6 |
| `wiki/concepts/docker-reverse-proxy-load-balancing.md` | R07·I03·P02 | nginx upstream/proxy_pass | 전면 재작성 | nginx 설정은 합성이며 I03은 기술 네트워크도가 아니라 상담자 업무 분배 비유다. 실제 `proxy-net`·host-mounted `nginx.conf`와 AWS LB 경계를 다시 구성 | Docker 직접 / AWS LB 후속 | 7 |
| `wiki/concepts/docker-compose-manifest.md` | R08·P02~P03·P09 | MySQL+Spring YAML/up/down | 부분 보강 | 일반화된 YAML·명령 fence 2개가 원문 연속 불일치. 수업 manifest와 최신 문법을 구분 | Compose 직접 / Passwordless·프로젝트 후속 | 7 |
| `wiki/concepts/git-github-collaboration.md` | R09~R10·P04 | branch/PR/merge/conflict | 부분 보강 | 협업 절차 책임은 유지 가능하다. 합성 feature 예시 대신 animal/sport·PR·master 최신화·conflict artifact와 2개 fence를 교정 | Linux 과목 협업 직접 / Actions 후속 | 8 |

### Entity 대응 및 분류

| wiki 경로 | raw·수업일 | 대표 역할 | 분류 | 누락·중복 책임 | 직접/후속 경계 | 예정 세션 |
|---|---|---|---|---|---|---:|
| `wiki/entities/linux.md` | R01~R05·R11·P06~P07 | server OS 학습 허브 | 부분 보강 | 운영체제 허브 역할은 적절하다. process/service/port를 보강하고 04-29 이후 Docker/Git은 Linux OS 기능과 분리 | Linux 직접 / EC2 OS 후속 | 5 |
| `wiki/entities/maven.md` | R05·R07·R11 | Spring jar build | 전면 재작성 | 45행으로 얕다. FrontEnd_BackEnd build 설정→Linux 수동 package→Dockerfile→CI Maven build 책임을 다시 구성 | Linux 직접 / CI 후속 | 5 |
| `wiki/entities/docker.md` | R05~R08·R11·P02~P03·P08~P09 | container platform | 부분 보강 | 4일 실습 artifact·확인/미확정·Hub/CI 경계가 목록형 | Docker 직접 / CI·Passwordless 후속 | 7 |
| `wiki/entities/git.md` | R09~R10·P04 + Java 선행 | local VCS | 유지 | Java 단계에서 이미 고도화됨. Linux 협업 날짜와 merge/rebase 경계만 실행 시 확인 | Java 첫 등장 / Linux 협업 직접 / CI 후속 | 8 |
| `wiki/entities/github.md` | R09~R10·P04 + Java·CI/CD | remote collaboration service | 유지 | Java 단계 고도화 결과를 보존하고 PR/Actions 경계만 확인 | Linux PR 직접 / Actions 후속 | 8 |
| `wiki/entities/source-tree.md` | R09·P04 | Git GUI client | 부분 보강 | 실제 05-04 stage/commit/push/pull/conflict와 CLI 상태 대응이 얕음 | Linux 협업 직접 | 8 |

### Comparison 대응 및 분류

| wiki 경로 | raw·수업일 | 대표 비교 | 분류 | 누락·오류·중복 책임 | 직접/후속 경계 | 예정 세션 |
|---|---|---|---|---|---|---:|
| `wiki/concepts/dockerfile-vs-compose.md` | R07~R08·R11·P02 | image recipe vs multi-service manifest | 부분 보강 | 위치/type 불일치가 있으나 이동은 보류. 실제 Spring+MySQL 선택 상황·원문 경계 보강 | Docker 직접 / CI 후속 | 9 |
| `wiki/comparisons/docker-commit-vs-dockerfile.md` | R06~R07·P02·P08 | state snapshot vs reproducible recipe | 유지 | 현재 선택 기준이 명확함. 실제 container/image 이름과 Hub 후속만 확인 | Docker 직접 / CI 후속 | 9 |
| `wiki/comparisons/docker-cp-vs-bind-mount-vs-volume.md` | R06·R08·P02~P03 | copy vs host link vs managed storage | 유지 | 일회성 복사·host 직접 연결·Docker 관리 저장공간의 선택 축이 명확하다. 실행 시 provenance만 재확인 | Docker 직접 | 9 |
| `wiki/comparisons/git-fetch-vs-pull-vs-clone.md` | R09~R10·R11·P04 | remote 정보/병합/최초 복제 | 부분 보강 | 1개 fence가 합성 placeholder. 실제 05-06 remote branch fetch UI와 pull/clone 흐름 필요 | Linux 협업 직접 | 9 |
| `wiki/comparisons/host-port-forwarding-vs-docker-port-mapping.md` | R04~R07·R11 | host iptables/UFW vs `-p` | 전면 재작성 | VirtualBox NAT host→guest, Linux iptables guest 80→process 9000, Docker host→container를 현재 두 축으로 합쳤다 | Linux/Docker 직접 / SG·ALB 후속 | 9 |
| `wiki/comparisons/virtual-machine-vs-docker-container.md` | R01·R05·R11 | guest OS vs host-kernel process | 부분 보강 | 비교 축은 양호하다. bridge/NAT·SSH·Docker Engine·AWS EC2 후속 경계를 보강 | Linux 직접 / EC2 후속 | 9 |

## 후속 적용 경계 페이지

아래 15개는 Linux raw를 직접 source로 선언하지 않지만 Linux 명령·Docker·Git을 후속 과목에서 적용하는 핵심 경계다. 단계 5에서는 **유지**하며 역링크·경계 문장만 확인하고 AWS/CI/CD 본문을 재고도화하지 않는다.

| 유형 | wiki 경로 | 경계 역할 | 분류 | 예정 세션 |
|---|---|---|---|---:|
| summary | `wiki/summaries/2026-04-03-frontend-backend-subject-review.md` | 로컬 React/Spring 기능에서 Linux 실행환경으로 넘어오는 선행 경계 | 유지 | 10 |
| summary | `wiki/summaries/2026-05-06-aws-cloud-vpc-ec2.md` | Linux 과목 종료와 같은 날 시작한 AWS 별도 과목 경계 | 유지 | 10 |
| summary | `wiki/summaries/2026-05-07-aws-ec2-nginx-rds.md` | VM/SSH/Nginx 지식의 EC2 적용 | 유지 | 10 |
| summary | `wiki/summaries/2026-05-08-aws-rds-resource-cleanup.md` | Linux jar·Nginx·port를 EC2/RDS에 적용 | 유지 | 10 |
| summary | `wiki/summaries/2026-05-08-aws-subject-review.md` | Linux 직접 실습과 cloud 자원 학습 분리 | 유지 | 10 |
| summary | `wiki/summaries/2026-05-11-cicd-github-actions-spring-boot.md` | GitHub push·Maven·Docker image·EC2를 자동화 | 유지 | 10 |
| summary | `wiki/summaries/2026-05-12-route53-alb-https-review.md` | Docker/Nginx load balancing에서 ALB/HTTPS로 확장 | 유지 | 10 |
| concept | `wiki/concepts/aws-cloud-vpc-networking.md` | VM/Docker network와 VPC/Subnet/SG의 층위 구분 | 유지 | 10 |
| concept | `wiki/concepts/aws-ec2-nginx-spring-deploy.md` | Linux Spring jar 실행의 cloud 버전 | 유지 | 10 |
| concept | `wiki/concepts/ci-cd-automation.md` | Linux 수동 build/deploy와 자동 pipeline 구분 | 유지 | 10 |
| concept | `wiki/concepts/github-actions-workflow.md` | GitHub 협업 이후 workflow automation | 유지 | 10 |
| concept | `wiki/concepts/spring-boot-cicd-docker-ec2-flow.md` | Linux Docker image를 EC2 배포 단위로 확장 | 유지 | 10 |
| entity | `wiki/entities/aws.md` | Linux/Docker 다음 cloud platform | 유지 | 10 |
| entity | `wiki/entities/amazon-ec2.md` | VirtualBox Ubuntu VM과 구분되는 cloud instance | 유지 | 10 |
| comparison | `wiki/comparisons/clb-vs-alb.md` | Docker/Nginx load balancing의 후속 AWS 비교 | 유지 | 10 |

## 분류 수치

### 기존 직접 source 페이지 35개

- 유지: 4개
- 부분 보강: 17개
- 전면 재작성: 13개
- 통합 후보: 0개
- 근거 부족: 1개
- 미분류: 0개

### 후속 경계 페이지 15개 포함

- 유지: 19개
- 부분 보강: 17개
- 전면 재작성: 13개
- 통합 후보: 0개
- 근거 부족: 1개
- 미분류: 0개

### 신규 필요 후보

- 신규 필요 후보: Concept 2개, Comparison 1개, Query 1개
- 최종 신규 생성 수는 실행 세션의 중복·직접 근거·탐색 역할 재검증에 따라 0~4개다.

## 신규 후보 판정

| 후보 | 권장 type | 주 raw | 판정 | 기존 흡수 가능성·처리 세션 |
|---|---|---|---|---|
| Linux process·service·firewall·port | concept | R01, R03~R05, R11 | 신규 필요 후보 | `ps/kill`, `systemctl`, UFW/iptables, SSH/Apache/Nginx/Spring port가 여러 날짜에 반복된다. webserver·Spring deploy 페이지를 연결하는 독립 진단 축. 세션 5에서 최종 판단. |
| Docker registry tag·push·pull | concept | R06, P08, R11 | 신규 필요 후보 | local image→tag→login→push→다른 host pull/run의 수동 생명주기가 직접 실습에 있으나 기존 Docker entity에는 짧게만 흡수됐다. CI/CD 자동화와 구분해 세션 7에서 최종 판단. |
| sudo vs `sudo su -` vs root session | comparison | R01, R03~R05 | 신규 필요 후보 | 관리자 권한·root prompt·root 소유권·Docker 설치가 반복되고 “사용자 만들기는 꼭 root로 가야 하나?”라는 명시적 혼동이 있다. 세션 9에서 최종 판단. |
| sudo로 만든 디렉터리는 왜 일반 사용자로 수정·복사할 수 없는가 | query | R03~R04 | 신규 필요 후보 | 실제 `Permission denied`, root 소유권, `chown`, directory write 권한을 종합하는 재사용 가능한 troubleshooting 질문이다. 세션 9에서 최종 판단. |
| VirtualBox·SSH·MobaXterm 연결 계층 | concept | R01, P06, P10 | 기존 보강으로 흡수 | 04-22 Summary, Linux entity, `virtual-machine-vs-docker-container`에 VM·guest OS·OpenSSH service·bridge/IP·client 층위를 보강한다. |
| vi 편집기 | concept | R02, P05~P07 | 기존 보강으로 흡수 완료 | `linux-cli-files`가 명령/입력/마지막 행 모드, 저장·종료·검색·치환과 외부 확인을 직접 책임한다. 신규 페이지를 만들지 않았다. |
| 절대 경로 vs 상대 경로 | comparison | R01~R02, R11 | 기존 보강으로 흡수 완료 | `linux-cli-files`에 기준 위치와 고정 path/현재 tree 작업의 선택 상황을 보강했다. Comparison을 수정·신설하지 않았다. |
| 파일 권한 숫자 vs 기호 | comparison | R03, I01~I02, R11 | 기존 보강으로 흡수 완료 | `linux-users-permissions`에 전체 최종 상태는 숫자 mode, 기존 상태 일부 조정은 기호 mode라는 선택 기준을 보강했다. Comparison을 수정·신설하지 않았다. |
| image vs container | comparison | R05~R07, R11 | 기존 보강으로 흡수 | `docker-image-container`와 `virtual-machine-vs-docker-container`의 역할이 충분하다. |
| volume vs bind mount | comparison | R06·R08, P02~P03 | 기존 보강으로 흡수 | 기존 `docker-cp-vs-bind-mount-vs-volume`을 실제 사례로 강화한다. |
| Git merge vs rebase | comparison | R10, P04 | 기존 보강으로 흡수 | 원본의 독립 근거가 05-06 일부 실습에 한정되므로 `git-github-collaboration`과 05-06 Summary에 확인 범위·오해를 기록한다. |
| Linux 포트 문제는 어디서 확인하는가 | query | R01·R04~R07, 후속 AWS/CI/CD | 신규 보류 | `linux-process·service·firewall·port` 후보와 `host-port-forwarding-vs-docker-port-mapping` 보강으로 우선 흡수한다. 독립 사용자 질문 기록이 확인될 때만 Query를 만든다. |

## 세션 1 기준 code fence 재고와 현재 잔여

세션 1 기준 직접 source 페이지 35개 중 code fence가 있는 페이지는 13개, fence는 **18개**였다. 세션 4에서 대상 Concept의 `bash` fence 3개를 제거해 현재 미처리 잔여는 **10개 페이지·15개 fence**다.

- 세션 1 기준 `bash`: 14개 — 모두 Linux 명령이므로 실행 세션에서 `shell`로 교정 대상
- `yaml`: 1개
- `text`: 1개
- `nginx`: 1개
- `dockerfile`: 1개
- 세션 4 이후 잔여 언어 수: `bash 11 / yaml 1 / text 1 / nginx 1 / dockerfile 1`.
- 세션 1의 18개는 모두 선언된 텍스트 raw source의 공백 정규화 연속 부분문자열과 일치하지 않았다. 세션 4에서는 대상 3개를 prose·표로 바꿔 합성 provenance를 해소했다.
- 불일치는 곧 오류 확정이 아니라 **원문 연속 대조가 필요한 합성·일반화 후보**라는 뜻이다. PDF/이미지에서 온 예시는 별도 수동 근거로 판정한다.
- 한국어 설명이나 terminal output이 `bash` fence 안에 직접 섞인 확정 사례는 0개다. 더 큰 문제는 서로 다른 실행 위치·날짜·실습 단계를 한 실행 예제처럼 합친 provenance 오류다.
- `docker-reverse-proxy-load-balancing.md`의 `text` fence 1개는 terminal output이 아니라 합성 설명 도식이다.

| wiki 경로 | fence 수·언어 | 현재 판정 | 실행 세션의 원문 대조 기준 |
|---|---|---|---|
| `wiki/concepts/docker-compose-manifest.md` | 2: yaml 1, bash 1 | 일반화 YAML과 up/down 명령 합성 후보 | R08/P09의 실제 manifest와 연속 명령 단위로 분리. bash→shell |
| `wiki/concepts/docker-cp-exec-container-files.md` | 1: bash | 여러 exec/cp 명령을 한 예제로 합친 후보 | R06의 실제 apache container/path 연속 구간 우선. bash→shell |
| `wiki/concepts/docker-image-container.md` | 1: bash | run/start/stop/rm/rmi 생명주기 합성 후보 | R05의 실제 container 단위 또는 설명용 예시임을 명시. bash→shell |
| `wiki/concepts/docker-install-permission-setup.md` | 1: bash | setup·root·group 명령이 서로 떨어진 원문 조각일 가능성 | R05/R08/P09의 설치 단계와 권한 반영을 분리. bash→shell |
| `wiki/concepts/docker-network-volume.md` | 1: bash | R05의 network01·MySQL·WordPress와 R06의 volume을 합쳤는데 R05가 source에도 없는 고위험 후보 | R05/R06 source 책임을 먼저 바로잡고 network·bind·volume을 각각 연속 unit으로 분리. bash→shell |
| `wiki/concepts/docker-reverse-proxy-load-balancing.md` | 2: text 1, nginx 1 | text는 설명 도식, nginx는 일반화 config 후보 | I03 설명 도식과 R07의 실제 nginx.conf 연속 구간을 구분 |
| `wiki/concepts/git-github-collaboration.md` | 2: bash | placeholder URL/branch를 사용한 합성 명령 | R09~R10의 실제 실습을 민감 식별자 없이 연속 명령 또는 단계 설명으로 교체. bash→shell |
| `wiki/concepts/linux-cli-files.md` | 세션 1 `bash` 1 → 현재 0 | 여러 날짜·구간 명령을 한 묶음으로 합친 후보를 제거 | R01~R02의 경로·파일·vi 실습을 prose·표와 실제 결과 흐름으로 분리 완료 |
| `wiki/concepts/linux-package-archive.md` | 세션 1 `bash` 1 → 현재 0 | R01 apt와 R04 download/archive를 합친 후보를 제거 | package/download/archive를 서로 다른 단계와 artifact 결과로 분리 완료 |
| `wiki/concepts/linux-spring-boot-server-deploy.md` | 2: bash 1, dockerfile 1 | host jar 명령 합성, Dockerfile 3줄 합성 후보 | R05 host 실행과 R07 Dockerfile을 서로 다른 unit으로 대조. bash→shell |
| `wiki/concepts/linux-users-permissions.md` | 세션 1 `bash` 1 → 현재 0 | R03 계정·그룹과 source 밖 R04 사례를 합친 후보를 제거하고 R04를 source에 추가 | 사용자/group, chmod, chown/chgrp, R04 download directory 오류를 prose·표로 분리 완료 |
| `wiki/concepts/linux-web-server-apache-nginx.md` | 2: bash | host service/UFW와 Docker nginx를 각각 합성한 후보 | R04 host webserver, R05 stop/port, R07 container/proxy를 분리. bash→shell |
| `wiki/comparisons/git-fetch-vs-pull-vs-clone.md` | 1: bash | placeholder URL과 세 명령 합성 예시 | R09 clone/pull과 R10 fetch를 표·단계로 비교하고 필요할 때만 연속 fence 사용. bash→shell |

### fence 공통 처리 규칙

1. 실행 세션에서 해당 페이지의 모든 fence를 선언된 텍스트 raw와 공백 정규화 연속 부분문자열로 대조한다.
2. PDF/PNG만 근거인 fence는 자동 일치로 가장하지 않고 수동 예외와 page/artifact를 기록한다.
3. Linux·Git·Docker CLI fence는 `shell` 태그를 사용한다. `bash`는 남기지 않는다.
4. 명령·출력·설명문을 한 fence에 섞지 않는다. 출력은 별도 `text` fence 또는 prose로 구분한다.
5. 여러 날짜·멀리 떨어진 원문 명령을 합쳐 수업 원문처럼 보이게 하지 않는다. 설명용 합성이라면 명시하거나 prose/표로 바꾼다.
6. 실제 계정명·저장소 URL·비밀번호·token은 재노출하지 않는다.

## 실행 세션 분할

과목 전체는 총 **10개 세션**으로 분할한다. 현재 세션은 1이며, 세션 2~9는 지식 페이지 실행 묶음, 세션 10은 전체 대응·provenance·구조 고정점이다. 각 세션은 지정 범위만 처리하고 다음 세션을 자동 실행하지 않는다.

| 세션 | 구간·유형 | 대상 페이지·후보 | 주 raw |
|---:|---|---|---|
| 1 | 재고·대응·분류·분할 | 이 meta 계획, index, log만 작성 | R01~R11, P01~P10, I01~I03 |
| 2 | Summary 전반부 | 04-22, 04-23, 04-24, 04-27, 04-28 Summary 5개 | R01~R05, P05~P07·P10, I01~I02 |
| 3 | Summary 후반부·허브 | 04-29, 04-30, 05-01, 05-04, 05-06 Summary와 Linux 총정리 Summary 6개 | R06~R11, P01~P04·P08~P09, I03 |
| 4 | Linux CLI·파일·vi·권한 Concept | `linux-cli-files`, `linux-package-archive`, `linux-users-permissions`; vi·경로·권한 comparison 흡수 판단 | R01~R04·R11, P05~P07, I01~I02 |
| 5 | VM·SSH·process·service·network·server Concept/Entity | `linux-spring-boot-server-deploy`, `linux-web-server-apache-nginx`, `linux`, `maven`; process/service/firewall/port 신규 후보와 누락 source 재설계 | R01·R03~R05·R07·R11, P06~P07·P10 |
| 6 | Docker core Concept | `docker-install-permission-setup`, `docker-image-container`, `docker-cp-exec-container-files`, `docker-network-volume` | R05~R06·R08·R11, P02~P03·P09 |
| 7 | Dockerfile·reverse proxy·Compose Concept/Entity | `docker-reverse-proxy-load-balancing`, `docker-compose-manifest`, `docker`; Docker registry 신규 후보 | R06~R08·R11, P02~P03·P08~P09, I03 |
| 8 | Git·GitHub Entity/Concept | `git-github-collaboration`, `git`, `github`, `source-tree` | R09~R11, P04; Java 선행·CI/CD 후속 경계 |
| 9 | 최종 Comparison/Query | 기존 Comparison 6개, sudo/root Comparison과 permission Query 후보, 나머지 흡수 후보 최종 판정 | R01·R03~R11, P02~P04·P08, 후속 경계 최소 확인 |
| 10 | 과목 전체 고정점 | 최종 직접 source 페이지·신규 페이지·경계 페이지, index, log, 상위 계획 완료 기록 | R01~R11, P01~P10, I01~I03 전수 |

## 실행 세션 공통 완료 게이트

- 지정 페이지와 raw 식별자 대응이 100%이며 미분류가 없어야 한다.
- Summary는 실제 교시 흐름, 대표 artifact, 입력→처리→결과, 이전·다음 날짜 연결, 직접/후속 경계를 갖춰야 한다.
- Concept는 실제 수업 명령·설정·오류 사례, 왜 필요한지, 선택 기준, 선행/후속 연결을 포함해야 한다.
- Entity는 첫 등장·날짜별 확장·실제 역할·프로젝트/면접 설명 관점과 직접/후속 경계를 갖춰야 한다.
- Comparison은 표, 최소 2개 선택 상황, 함께 쓰는 관계, 흔한 오해, 실제 수업 근거를 갖춰야 한다.
- Query는 실제 사용자 질문·반복 혼동·여러 페이지 종합 가치가 확인될 때만 만든다.
- 새 fence는 원본에 이미 있는 연속 코드·명령·설정이 필요한 경우에만 작성한다. 합성 예제를 수업 원문으로 제시하지 않는다.
- 기존 fence 18개는 모두 원문 연속 대조 또는 명시적 설명용/수동 예외 판정을 받아야 한다.
- Linux CLI fence에 `bash` 태그가 남지 않아야 하며 `shell`을 사용한다.
- 명령·출력·설명문 혼합 fence와 여러 날짜 합성 fence를 해소한다.
- frontmatter source 실경로, 허용 태그, 위키링크, index 등록, 고립, placeholder, tracked/untracked whitespace를 검사한다.
- 새 지식 페이지가 생기면 index 등록, Total pages 재계산, log 기록을 같은 세션에서 처리한다.
- `raw/KoreaICT/5. Linux` scoped status/diff를 시작·종료 시 확인하고 변경하지 않는다.
- 대상 범위의 `git diff --check`를 통과해야 한다.
- 세션 10 전에는 상위 계획에 단계 5 완료 행을 쓰지 않고 단계 6 AWS를 시작하지 않는다.

## 세션 1 검증 기준

- raw 실제 파일 24개가 식별자 R01~R11·P01~P10·I01~I03에 빠짐없이 1회씩 대응한다.
- 기록한 모든 raw 경로가 실제로 존재한다.
- 직접 source 지식 페이지 35개와 후속 경계 페이지 15개의 대응표 미분류가 0개다.
- 직접 페이지 유형 수 `summary 11 / concept 12 / entity 6 / comparison 6 / query 0`이 실제 frontmatter와 일치한다.
- code fence 수 `18`, 언어 수 `bash 14 / yaml 1 / text 1 / nginx 1 / dockerfile 1`이 실제 페이지와 일치한다.
- 새 meta 페이지가 index에 등록되고 `Total pages`는 `index.md`·`log.md`를 제외한 실제 wiki Markdown 수로 재계산한다.
- `wiki/log.md`에 Linux 세션 1 계획 기록을 남긴다.
- 상위 계획의 단계 5 완료 행은 추가하지 않는다.
- scoped `git diff --check`와 raw 시작/종료 status·diff 동일성을 확인한다.

## 세션 2 실행 결과 — Summary 전반부 R01~R05

- 실행 범위: `2026-04-22-linux-install-ssh-cli`, `2026-04-23-linux-files-vi`, `2026-04-24-linux-users-permissions`, `2026-04-27-linux-archive-java-alias`, `2026-04-28-maven-spring-boot-docker-intro` 5개를 날짜 MD 전체 교시 흐름과 5/5 대응해 전면 재작성했다.
- 주 근거: R01~R05를 수업일·교시·실습 순서의 최우선 source로 사용했다. P05~P07·P10은 날짜 MD에 필요한 내용이 충분히 전사되어 독립 날짜나 page-level source로 강제하지 않았다. I01~I02는 실제 이미지를 판독해 04-24의 `r/w/x`와 owner/group/others 보조 근거로 채택했다.
- 내용 복원: 04-22 VM/bridge/SSH/client/path, 04-23 방송사·Librarian/vi/redirection/diff, 04-24 account file·UID/GID·chmod/chown/chgrp·script, 04-27 download/archive/alias/Java/Git/host web server, 04-28 Maven JAR/port 계층/Docker lifecycle/WordPress–MySQL network를 교시 순서와 입력→처리→결과로 연결했다.
- 오류·경계: 04-24의 “하지는 않음” group 삭제를 실행 결과에서 제외했다. JDBC JAR 준비와 DB 연결, Git Bash와 Linux VM, VirtualBox bridge/NAT·guest iptables·Docker port, Docker network와 AWS VPC, 수동 Linux 실행과 AWS/CI/CD 후속 자동화를 분리했다.
- provenance: 새 code fence는 0개이며 원문 검증 0개·수동 fence 예외 0개다. 실제 account·repository URL·password·token·one-time code는 일반화하거나 재노출하지 않았다.
- 상태: 세션 2만 완료했다. 단계 5 Linux는 미완료이며 세션 3과 Concept·Entity·Comparison·Query, 단계 6 AWS를 시작하지 않았다.

## 세션 3 실행 결과 — Summary 후반부·총정리 R06~R11

- 실행 범위: `2026-04-29-docker-network-volume-image`, `2026-04-30-dockerfile-spring-load-balancing`, `2026-05-01-docker-compose`, `2026-05-04-git-github-sourcetree`, `2026-05-06-github-branch-pr-conflict` 5개를 전면 재작성하고 `2026-05-06-linux-subject-review` 허브를 부분 보강했다. R06~R11과 6/6 대응했다.
- 주 근거: R06~R10 날짜 MD를 수업일·교시·실습 순서의 최우선 source로 사용하고 R11은 날짜별 Summary를 대체하지 않는 복습 허브로 유지했다. P01~P04·P08~P09는 필요한 내용이 날짜 MD에 충분히 전사되어 page source로 강제하지 않았다. I03은 실제 판독해 04-30의 상담자 요청 분배 비유에만 채택했다.
- Docker 흐름: 04-29의 MariaDB–Redmine network→exec/cp→bind mount/named volume→commit→Docker Hub tag·push·pull, 04-30의 build context·Dockerfile instruction→Spring JAR/MySQL→Nginx reverse proxy, 05-01의 Compose services/network/volume/environment/depends_on→up/status/DB/browser/down을 생명주기와 입력→처리→결과로 복원했다.
- Git 흐름: 05-04의 WorkTree→stage→local repository→GitHub remote, commit 없는 push, clone·pull·SourceTree·두 작업자 conflict와 branch 시작을 복원했다. 05-06은 팀장/팀원 branch→PR review/merge→remote master→local pull·fetch→`Cat.java` conflict와 merge/rebase의 IntelliJ 실습 범위를 분리했다.
- 오류·경계: 빈 bind mount의 Apache directory listing/Nginx 403, build·container Up·log·browser의 분리, Compose `depends_on`/readiness와 `down`/volume 삭제, 빈 교시·`이어서 작성`, 05-01 backend 시험, 04-29 AWS 가입 예고, 05-06 같은 날짜 AWS 본수업, 수동 Linux/Docker/Git과 후속 AWS/CI/CD를 구분했다.
- provenance: 새 code fence는 0개이며 원문 검증 0개·수동 fence 예외 0개·실패 0개다. Linux·Git·Docker `bash` fence는 0개이며 실제 account·email·repository URL·password·token·one-time code를 재노출하지 않았다.
- 상태: 세션 3만 완료했다. 단계 5 Linux는 미완료이며 세션 4와 Concept·Entity·Comparison·Query, 단계 6 AWS를 시작하지 않았다. 새 페이지가 없어 Total pages는 270을 유지한다.

## 세션 4 실행 결과 — CLI·파일·vi·권한 Concept

- 실행 범위: `linux-cli-files`, `linux-package-archive`, `linux-users-permissions` 3개만 부분 보강했다. Summary·Entity·Comparison·Query와 다른 Concept는 수정하지 않았고 신규 지식 페이지를 만들지 않았다.
- raw 대응: 날짜 MD R01~R04를 수업일·교시·실습 순서와 실행 결과의 최우선 근거로 사용하고 R11은 연결 허브로만 사용했다. Concept source union은 R01~R04·R11 5/5이며 미분류 0건이다. P05~P07은 필요한 내용이 날짜 MD에 전사되어 page source로 추가하지 않았고, I01~I02는 실제 표시 요소만 판독해 `linux-users-permissions`의 보조 source로 채택했다.
- CLI·vi: prompt의 사용자/host/path, `/`와 `/root`, 절대/상대 path, 방송사 directory의 생성·복사·이동·검색 결과, `>`·`>>`, `grep`·`more`·`diff`, vi 명령/입력/마지막 행 모드와 저장·종료·검색·치환을 복원했다. Librarian 교시는 날짜 MD에 세부 결과가 없어 다른 VM의 성공 결과로 합치지 않았다.
- package·archive: `apt update/install`, `wget`·`curl`, tar+gzip, zip/unzip, download artifact→해제 directory→내부 목록 확인을 분리했다. root 소유 directory의 file 반입 실패와 `chown` 후 성공, archive 생성과 `mv`가 서로 다른 단계임을 기록했다.
- user·permission: account file·UID/GID·home/login shell·기본/보조 group, file/directory `r/w/x`, 숫자/기호 chmod 선택 기준, directory `x`, sudo/root, chmod/chown/chgrp의 책임, root 소유 directory와 script `Permission denied` 해결을 복원했다. vi·경로·권한 숫자/기호 후보는 지정 Concept에 흡수하고 Comparison을 수정·신설하지 않았다.
- provenance·보안: 기존 대상 `bash` fence 3개를 제거하고 새 fence를 만들지 않았다. 최종 code fence 전체 0개/원문 검증 0개/수동 예외 0개/실패 0개, `bash` fence 0개다. 실제 account·email·repository URL·password·token·one-time code 재노출은 0건이다.
- 구조·상태: frontmatter·source 실경로·허용 태그·위키링크·placeholder와 scoped `git diff --check`를 통과했다. 새 페이지가 없어 Total pages는 실제 정의에 따라 270이며 기존 index 설명은 고도화 결과와 어긋나지 않아 수정하지 않았다. `raw/KoreaICT/5. Linux` status/diff는 시작·종료 모두 0건이다.
- 상태: 세션 4만 완료했다. 단계 5 Linux는 미완료이며 세션 5, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## 관련 페이지

- [[_meta/wiki-content-rehighquality-work-plan|LLM Wiki 내용 재고도화 작업 계획]]
- [[_meta/frontend-backend-rehighquality-inventory-plan|FrontEnd_BackEnd 내용 재고도화 전수 재고와 실행 분할 계획]]
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]
- [[entities/linux|Linux]]
- [[entities/docker|Docker]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
