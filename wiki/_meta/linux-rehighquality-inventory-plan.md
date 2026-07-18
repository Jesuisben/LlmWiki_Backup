---
title: Linux 내용 재고도화 전수 재고와 실행 분할 계획
created: 2026-07-16
updated: 2026-07-18
type: meta
tags: [linux, docker, github, spring-boot, curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/wiki-content-rehighquality-work-plan.md
  - wiki/_meta/frontend-backend-rehighquality-inventory-plan.md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: stable
confidence: high
---

# Linux 내용 재고도화 전수 재고와 실행 분할 계획

## 문서 상태와 범위

이 문서는 내용 재고도화 단계 5 `Linux`의 **세션 1 재고·대응·분류·실행 분할 기준선**이자 분할 세션별 실행 기록이다. 세션 2에서는 Summary 전반부 R01~R05, 세션 3에서는 Summary 후반부·총정리 R06~R11, 세션 4에서는 CLI·파일·vi·권한 Concept 3개, 세션 5에서는 VM·SSH·process·service·network·server Concept/Entity, 세션 6에서는 Docker core Concept 4개, 세션 7에서는 Dockerfile·reverse proxy·Compose Concept/Entity와 registry Concept, 세션 8에서는 Git·GitHub Concept/Entity 4개, 세션 9에서는 최종 Comparison 7개와 Query 1개를 고도화했다. 세션 10에서는 과목 전체 고정점을 전수 검증하고 신규 페이지의 역링크만 최소 교정했다.

- 현재 상태: **최종 완료 — 세션 10 과목 전체 고정점 통과**
- 세션 10 최소 교정 범위: 신규 sudo/root Comparison·permission Query를 관련 Summary 2개·Concept 1개·Linux Entity 1개에서 탐색할 수 있도록 역링크를 보강하고, 이 meta 문서·상위 계획·`wiki/log.md`에 완료 상태를 기록했다.
- 세션 10 비수정 범위: `raw/` 전체, 세션 2~9의 그 밖의 본문, 후속 AWS/CI/CD 경계 15개 본문, `wiki/index.md`
- 다음 실행 단위: 단계 6 `AWS` 실용형 첫 세션. 이 문서에서는 시작하지 않는다.
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

세션 1의 기존 직접 source 지식 페이지는 35개였고, 세션 5의 process/service 진단 Concept, 세션 7의 registry Concept, 세션 9의 sudo/root Comparison·permission Query 신규 생성 뒤 frontmatter `sources`가 `raw/KoreaICT/5. Linux`를 직접 참조하는 현재 지식 페이지는 **39개**다. 앞선 중간 집계에서 세션 5 신규 Concept 1개가 누락됐으며 세션 9 전수 계산으로 바로잡았다.

- 실제 디렉터리 기준: `summaries 11 / concepts 15 / entities 6 / comparisons 6 / queries 1`
- frontmatter `type` 기준: `summary 11 / concept 14 / entity 6 / comparison 7 / query 1`
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
| `wiki/concepts/linux-spring-boot-server-deploy.md` | R05·R07·R11 | Maven→JAR→host process→port→Dockerfile | 부분 보강 완료 | R05의 clone·9000·Maven package·`target` JAR·host `java -jar`와 NAT→guest 80→iptables 9000→UFW→browser를 단계별 완료 조건으로 분리하고, R07 Dockerfile/JAR·EC2·CI/CD를 후속 경계로 고정함 | Linux 직접 / Docker·EC2·Actions 후속 | 5 완료 |
| `wiki/concepts/linux-web-server-apache-nginx.md` | R04~R05·R07·R11 | systemctl/UFW, host webserver, container nginx | 근거 부족→전면 재작성 완료 | 누락된 핵심 R04를 source에 추가하고 Apache/Nginx host 설치·enable/start/status·UFW 22/80/443·document root backup/교체·browser 결과를 복원했다. R05 container webserver와 R07 reverse proxy를 분리함 | Linux 직접 / Docker·AWS Nginx·ALB 후속 | 5 완료 |
| `wiki/concepts/linux-process-service-port-firewall.md` | R01·R03~R05·R11 | SSH·script·systemctl·UFW·iptables·22/80/443/9000 | 신규 생성 완료 | process→service→listening port→firewall→NAT/redirect→client 응답이 SSH·Apache/Nginx·Spring에 반복되는 독립 진단 축이어서 기존 두 server Concept와 Linux Entity의 분산 흡수보다 별도 탐색 책임이 명확함 | Linux 직접 / Docker port·AWS Security Group 후속 | 5 완료 |
| `wiki/concepts/docker-install-permission-setup.md` | R05·R08·R11·P09 | setup script, CRLF, service, socket, docker group | 부분 보강 완료 | root 영역의 script 준비→`dos2unix`→실행 권한→설치→service active→group 등록→새 login session의 일반 사용자 daemon 접근을 별도 완료 조건으로 분리했다. P09는 05-01 반복 checklist로만 사용함 | Linux Docker 직접 / image·Compose·CI 후속 | 6 완료 |
| `wiki/concepts/docker-image-container.md` | R05~R06·R11 | httpd/nginx/MySQL/WordPress, pull/run/stop/rm, port | 부분 보강 완료 | R05 기성 image의 pull→create/start→Up/Exited→remove와 host/container port·browser·DB readiness를 분리했다. R06 commit image, R07 Dockerfile image, registry·CI image는 후속 경계로 고정함 | Docker 직접 / Dockerfile·registry·CI image 후속 | 6 완료 |
| `wiki/concepts/docker-cp-exec-container-files.md` | R05~R06·R11 | Apache/Nginx/MySQL exec, cp 양방향, file artifact | 부분 보강 완료 | `apache81/82`, `nginx83/84`, `mysql85`, `apache01-ctr`, `nginx88`의 서로 다른 container/path를 분리하고 host→container·container→host copy, 내부 확인, commit image를 별도 완료 조건으로 복원함 | Docker 직접 / mount·commit·Dockerfile 후속 | 6 완료 |
| `wiki/concepts/docker-network-volume.md` | R05~R06·R08·R11 | WordPress+MySQL, Redmine+MariaDB, bind/volume, Compose 경계 | 부분 보강 완료 | container name 통신과 host port를 분리하고 `network01/02`, Apache `Index of /`, Nginx 403, `mount-vol` inspect·삭제를 복원했다. R06에는 재생성 뒤 data persistence 실측이 없음을 명시하고 Compose·VPC 경계를 분리함 | Docker 직접 / Compose·AWS networking 후속 | 6 완료 |
| `wiki/concepts/docker-reverse-proxy-load-balancing.md` | R07·I03 | `proxy-net`, mounted `nginx.conf`, upstream/proxy_pass | 전면 재작성 완료 | Apache/Nginx backend 여섯 개→proxy container→browser 왕복과 network·port·config·process·backend·분배 완료 조건을 분리했다. I03은 상담자 업무 분배 비유로만 사용하고 host Nginx·web container·AWS ALB 경계를 고정함 | Docker 직접 / AWS LB 후속 | 7 완료 |
| `wiki/concepts/docker-compose-manifest.md` | R08 | MySQL+Spring·MySQL+WordPress manifest/up/down | 부분 보강 완료 | 두 manifest의 service/container 이름, network·volume·environment·port·depends_on과 YAML 들여쓰기/값 수정 범위를 복원했다. up·Up·DB readiness·browser·down·volume/image 삭제와 Dockerfile·CI/CD·운영 orchestration 책임을 분리함 | Compose 직접 / Passwordless·프로젝트 후속 | 7 완료 |
| `wiki/concepts/docker-registry-tag-push-pull.md` | R06·R11·P08 | local image→tag→login→push→다른 환경 pull/run | 신규 생성 완료 | 독립 7교시 실습과 namespace 누락 오류·credential 저장 경고·수동/CI 경계가 별도 탐색 가치를 가져 신규 Concept로 보존했다. push digest는 확인됐지만 다른 환경의 최종 browser/file 결과는 미보존으로 남김 | Docker 직접 / CI registry 자동화 후속 | 7 완료 |
| `wiki/concepts/git-github-collaboration.md` | R09~R11·P04 | branch/PR/merge/conflict | 전면 재작성 완료 | WorkTree→stage→commit→remote, `animal`·`sport`, PR 생성·merge·local master pull, fetch·conflict·merge/rebase를 artifact와 별도 완료 조건으로 복원하고 합성 fence 2개를 제거 | Linux 과목 협업 직접 / Actions 후속 | 8 완료 |

### Entity 대응 및 분류

| wiki 경로 | raw·수업일 | 대표 역할 | 분류 | 누락·중복 책임 | 직접/후속 경계 | 예정 세션 |
|---|---|---|---|---|---|---:|
| `wiki/entities/linux.md` | R01~R05·R11·P06~P07 | server OS 학습 허브 | 부분 보강 완료 | VirtualBox Ubuntu·OpenSSH·MobaXterm 첫 등장부터 CLI/권한·process/service·UFW/iptables·host server까지 날짜별 이력을 복원했다. Maven/Spring/Docker/Git 도구와 EC2·CI/CD 후속 책임을 OS 기능과 분리함 | Linux 직접 / EC2 OS 후속 | 5 완료 |
| `wiki/entities/maven.md` | R05·R07·R11 | Spring JAR build | 전면 재작성 완료 | FrontEnd_BackEnd의 Maven project 선행 맥락→R05 설치/version/project root/package/`target` JAR→R07 Dockerfile input→CI build 후속으로 기술 이력을 재구성하고 Maven·Java·Docker·workflow 책임을 분리함 | Linux 직접 / Docker·CI 후속 | 5 완료 |
| `wiki/entities/docker.md` | R05~R08·R11·P08 | container platform | 부분 보강 완료 | 04-28 설치/image/container에서 04-29 network/storage/commit/registry, 04-30 Dockerfile/Spring+DB/proxy, 05-01 Compose까지 기술 이력과 artifact를 복원했다. Linux host·Engine·image/container/network/volume·Dockerfile·Compose·registry·CI/CD 책임 및 완료 조건을 분리함 | Docker 직접 / CI·Passwordless 후속 | 7 완료 |
| `wiki/entities/git.md` | R09~R11·P04 + Java 선행 | local VCS | 전면 재작성 완료 | Java 개인 repository 선행과 Linux 팀 협업을 날짜별로 나누고 working tree·stage·local repository·local/remote-tracking/remote branch 및 add~rebase 상태 전이를 복원 | Java 첫 등장 / Linux 협업 직접 / CI 후속 | 8 완료 |
| `wiki/entities/github.md` | R09~R11·P04 + Java·CI/CD | remote collaboration service | 전면 재작성 완료 | remote hosting·branch 공유·PR review/merge와 local Git 명령을 분리하고 branch push·PR 생성·merge·remote master·local pull의 완료 상태 및 Actions 후속 경계를 복원 | Linux PR 직접 / Actions 후속 | 8 완료 |
| `wiki/entities/source-tree.md` | R09~R11·P04 | Git GUI client | 전면 재작성 완료 | 05-04의 두 local repository와 stage·commit·push·pull·history·push 거부·수동 통합을 Git 상태에 대응하고 05-06 IntelliJ 실행 결과와 분리 | Linux 협업 직접 | 8 완료 |

### Comparison 대응 및 분류

| wiki 경로 | raw·수업일 | 대표 비교 | 분류 | 누락·오류·중복 책임 | 직접/후속 경계 | 예정 세션 |
|---|---|---|---|---|---|---:|
| `wiki/concepts/dockerfile-vs-compose.md` | R07~R08·R11·P02~P03 | image recipe vs multi-service manifest | 부분 보강 완료 | 위치/type 불일치는 유지하고 build image와 project runtime, 실제 MySQL+Spring/WordPress 선택·함께 쓰기·readiness/down 경계를 복원 | Docker 직접 / CI 후속 | 9 완료 |
| `wiki/comparisons/docker-commit-vs-dockerfile.md` | R06~R07·R11·P02·P08 | state snapshot vs reproducible recipe | 부분 보강 완료 | 변경 container→commit image→새 container와 Dockerfile→build image의 artifact·검증을 분리하고 registry 전달 가능 여부는 공통점으로 바로잡음 | Docker 직접 / CI 후속 | 9 완료 |
| `wiki/comparisons/docker-cp-vs-bind-mount-vs-volume.md` | R06·R08·R11·P02~P03 | copy vs host link vs managed storage | 부분 보강 완료 | 양방향 일회 copy, 빈 bind source의 Apache listing/Nginx 403, `mount-vol`·Compose volume과 재생성 persistence 미확정을 분리 | Docker 직접 | 9 완료 |
| `wiki/comparisons/git-fetch-vs-pull-vs-clone.md` | R09~R10·R11·P04 | remote 정보/통합/최초 복제 | 부분 보강 완료 | placeholder URL·합성 `bash` fence를 제거하고 R09 clone/pull과 R10 fetch→remote-tracking→local branch를 날짜·상태별 prose·표로 분리 | Linux 협업 직접 | 9 완료 |
| `wiki/comparisons/host-port-forwarding-vs-docker-port-mapping.md` | R05~R07·R11 | VirtualBox NAT·guest iptables/UFW vs Docker publish | 전면 재작성 완료 | Windows host→guest→Spring process와 Docker host→container를 계층별 선택·함께 쓰기·완료 조건으로 분리 | Linux/Docker 직접 / SG·ALB 후속 | 9 완료 |
| `wiki/comparisons/virtual-machine-vs-docker-container.md` | R01·R05·R08·R11·P03 | guest OS vs host-kernel process | 부분 보강 완료 | VM/SSH와 Docker Engine/container의 host/application 계층, 새 VM+Compose 공존, 접속·port·readiness 경계를 복원 | Linux 직접 / EC2 후속 | 9 완료 |
| `wiki/comparisons/sudo-vs-sudo-su-vs-root-session.md` | R01·R03~R05·R08·R11 | 한 명령 privilege vs root login shell·지속 session | 신규 생성 완료 | 명시적 “꼭 root?” 혼동과 package/service·user/group·Docker setup 반복을 독립 선택 축으로 보존하고 root-owned artifact 위험을 연결 | Linux 직접 / EC2·CI/CD 후속 | 9 완료 |

### Query 대응 및 분류

| wiki 경로 | raw·수업일 | 대표 질문 | 분류 | 독립 탐색 책임 | 직접/후속 경계 | 예정 세션 |
|---|---|---|---|---|---|---:|
| `wiki/queries/why-sudo-created-directory-denies-normal-user.md` | R03~R04·R11 | root-owned directory의 일반 사용자 생성·복사 실패 | 신규 생성 완료 | 04-24 `touch`와 04-27 drag-and-drop의 반복 `Permission denied`를 실행 주체→ownership→directory `w/x`→`chown`/`chmod` 선택 순서로 종합 | Linux 직접 / Docker group·EC2·CI/CD 후속 | 9 완료 |

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
| Linux process·service·firewall·port | concept | R01, R03~R05, R11 | 신규 생성 완료 | `ps/kill`, `systemctl`, UFW/iptables, SSH/Apache/Nginx/Spring port를 process→service→listening port→firewall→NAT/redirect→client 응답으로 탐색하는 독립 진단 축이 명확했다. 기존 server Concept·Linux Entity·Maven Entity 4개에서 역링크했다. |
| Docker registry tag·push·pull | concept | R06, P08, R11 | 신규 생성 완료 | local image의 생성/실행과 다른 질문인 registry naming·인증·layer push·다른 환경 retrieval이 독립 교시에 이어지고 namespace 오류·credential 경고·수동/CI 경계도 반복 탐색 가치가 있어 신규 Concept로 보존했다. Docker Entity에서 역링크하고 image/container 기본 책임은 기존 페이지에 위임함. |
| sudo vs `sudo su -` vs root session | comparison | R01, R03~R05, R08 | 신규 생성 완료 | 관리자 권한·root prompt·root 소유권·Docker 설치가 여러 날짜에 반복되고 “사용자 만들기는 꼭 root로 가야 하나?”라는 명시적 혼동이 있다. 기존 권한 Concept의 한 section만으로는 한 명령 상승·login shell·지속 session의 선택 축을 독립 탐색하기 어려워 Comparison으로 보존했다. |
| sudo로 만든 디렉터리는 왜 일반 사용자로 수정·복사할 수 없는가 | query | R03~R04 | 신규 생성 완료 | 04-24 `touch`와 04-27 MobaXterm drag-and-drop에서 같은 class의 `Permission denied`가 반복됐다. Concept 설명을 복제하지 않고 실행 주체→owner/group→directory `w/x`→최소 `chown`/`chmod` 선택의 재사용 troubleshooting 순서로 종합했다. |
| VirtualBox·SSH·MobaXterm 연결 계층 | concept | R01, P06, P10 | 기존 보강으로 흡수 | 04-22 Summary, Linux entity, `virtual-machine-vs-docker-container`에 VM·guest OS·OpenSSH service·bridge/IP·client 층위를 보강한다. |
| vi 편집기 | concept | R02, P05~P07 | 기존 보강으로 흡수 완료 | `linux-cli-files`가 명령/입력/마지막 행 모드, 저장·종료·검색·치환과 외부 확인을 직접 책임한다. 신규 페이지를 만들지 않았다. |
| 절대 경로 vs 상대 경로 | comparison | R01~R02, R11 | 기존 보강으로 흡수 완료 | `linux-cli-files`에 기준 위치와 고정 path/현재 tree 작업의 선택 상황을 보강했다. Comparison을 수정·신설하지 않았다. |
| 파일 권한 숫자 vs 기호 | comparison | R03, I01~I02, R11 | 기존 보강으로 흡수 완료 | `linux-users-permissions`에 전체 최종 상태는 숫자 mode, 기존 상태 일부 조정은 기호 mode라는 선택 기준을 보강했다. Comparison을 수정·신설하지 않았다. |
| image vs container | comparison | R05~R07, R11 | 기존 보강으로 흡수 | `docker-image-container`와 `virtual-machine-vs-docker-container`의 역할이 충분하다. |
| volume vs bind mount | comparison | R06·R08, P02~P03 | 기존 보강으로 흡수 | 기존 `docker-cp-vs-bind-mount-vs-volume`을 실제 사례로 강화한다. |
| Git merge vs rebase | comparison | R10, P04 | 기존 보강으로 흡수 | 원본의 독립 근거가 05-06 일부 실습에 한정되므로 `git-github-collaboration`과 05-06 Summary에 확인 범위·오해를 기록한다. |
| Linux 포트 문제는 어디서 확인하는가 | query | R01·R04~R07, 후속 AWS/CI/CD | 신규 보류 | `linux-process·service·firewall·port` 후보와 `host-port-forwarding-vs-docker-port-mapping` 보강으로 우선 흡수한다. 독립 사용자 질문 기록이 확인될 때만 Query를 만든다. |

## 세션 1 기준 code fence 재고와 현재 잔여

세션 1 기준 직접 source 페이지 35개 중 code fence가 있는 페이지는 13개, fence는 **18개**였다. 세션 4에서 대상 Concept의 `bash` fence 3개, 세션 5에서 대상 기존 페이지의 fence 4개(`bash` 3, `dockerfile` 1), 세션 6에서 Docker core Concept의 `bash` fence 4개를 제거했다. 세션 7에서는 reverse proxy의 합성 `text` 도식과 Compose의 합성 `yaml`·`bash` fence를 제거하고, 합성 `nginx` fence를 R07의 실제 연속 `nginx.conf` 1개로 교체했다. 세션 8에서는 Git 협업 Concept의 합성 `bash` fence 2개를 prose·표로 전환했다. 세션 9에서는 마지막 Git Comparison의 합성 `bash` fence 1개를 prose·표로 전환했다. 현재 미처리 잔여는 **0개**이며, 검증 완료된 `nginx` fence 1개만 유지한다.

- 세션 1 기준 `bash`: 14개 — 모두 Linux 명령이므로 실행 세션에서 `shell`로 교정 대상
- `yaml`: 1개
- `text`: 1개
- `nginx`: 1개
- `dockerfile`: 1개
- 세션 9 이후 미처리 잔여 언어 수: 0. 검증 완료되어 유지한 `nginx` fence 1개는 R07 연속 원문과 일치한다.
- 세션 1의 18개는 모두 선언된 텍스트 raw source의 공백 정규화 연속 부분문자열과 일치하지 않았다. 세션 4에서는 대상 3개를 prose·표로 바꿔 합성 provenance를 해소했다.
- 불일치는 곧 오류 확정이 아니라 **원문 연속 대조가 필요한 합성·일반화 후보**라는 뜻이다. PDF/이미지에서 온 예시는 별도 수동 근거로 판정한다.
- 한국어 설명이나 terminal output이 `bash` fence 안에 직접 섞인 확정 사례는 0개다. 더 큰 문제는 서로 다른 실행 위치·날짜·실습 단계를 한 실행 예제처럼 합친 provenance 오류다.
- `docker-reverse-proxy-load-balancing.md`의 `text` fence 1개는 terminal output이 아니라 합성 설명 도식이다.

| wiki 경로 | fence 수·언어 | 현재 판정 | 실행 세션의 원문 대조 기준 |
|---|---|---|---|
| `wiki/concepts/docker-compose-manifest.md` | 세션 1 `yaml` 1·`bash` 1 → 현재 0 | credential을 포함한 두 실제 manifest와 멀리 떨어진 up/down을 일반화한 합성 fence를 제거 | 두 manifest의 관계·오류·실행·정리를 credential 없는 prose·표로 분리 완료 |
| `wiki/concepts/docker-cp-exec-container-files.md` | 세션 1 `bash` 1 → 현재 0 | R05~R06의 서로 다른 Apache/Nginx container와 떨어진 exec/cp 명령을 합친 fence를 제거 | container/path·copy 방향·내부 확인·commit 연결을 prose·표로 분리 완료 |
| `wiki/concepts/docker-image-container.md` | 세션 1 `bash` 1 → 현재 0 | 실제 R05 대표 흐름에 없는 start/rmi까지 한 lifecycle 예제로 합친 fence를 제거 | 기성 image pull/run/stop/rm과 상태·port·browser 완료 조건을 prose·표로 분리 완료 |
| `wiki/concepts/docker-install-permission-setup.md` | 세션 1 `bash` 1 → 현재 0 | setup·root·group·service의 떨어진 원문 조각을 합친 fence를 제거 | R05 설치 순서와 R08/P09 반복 checklist, socket/group session 반영을 prose·표로 분리 완료 |
| `wiki/concepts/docker-network-volume.md` | 세션 1 `bash` 1 → 현재 0 | R05 network·R06 bind/volume 명령을 한 실습처럼 합친 fence를 제거 | `network01/02`, Apache/Nginx bind, `mount-vol`, R08 Compose 후속을 날짜·artifact별 prose·표로 분리 완료 |
| `wiki/concepts/docker-reverse-proxy-load-balancing.md` | 세션 1 `text` 1·`nginx` 1 → 현재 `nginx` 1 | 합성 text 도식은 실제 artifact 표로 전환하고 일반화 config는 R07의 실제 연속 `nginx.conf`로 교체 | R07 lines 803~844의 공백 정규화 연속 원문 1/1 일치, I03은 prose 비유로만 판정 |
| `wiki/concepts/git-github-collaboration.md` | 세션 1 `bash` 2 → 현재 0 | placeholder URL·합성 feature branch를 사용한 명령 fence를 제거 | R09~R10의 실제 `animal`·`sport`·PR·master pull·conflict를 credential 없는 prose·표로 분리 완료. P04는 page 범위를 기록한 화면 절차 보조이며 fence 수동 예외 없음 |
| `wiki/concepts/linux-cli-files.md` | 세션 1 `bash` 1 → 현재 0 | 여러 날짜·구간 명령을 한 묶음으로 합친 후보를 제거 | R01~R02의 경로·파일·vi 실습을 prose·표와 실제 결과 흐름으로 분리 완료 |
| `wiki/concepts/linux-package-archive.md` | 세션 1 `bash` 1 → 현재 0 | R01 apt와 R04 download/archive를 합친 후보를 제거 | package/download/archive를 서로 다른 단계와 artifact 결과로 분리 완료 |
| `wiki/concepts/linux-spring-boot-server-deploy.md` | 세션 1 `bash` 1·`dockerfile` 1 → 현재 0 | R05 host jar 명령 합성과 R07에서 떨어진 Dockerfile instruction 3줄 합성을 제거 | R05 host source→package→JAR→process→port→browser와 R07 Dockerfile 후속을 prose·표로 분리 완료 |
| `wiki/concepts/linux-users-permissions.md` | 세션 1 `bash` 1 → 현재 0 | R03 계정·그룹과 source 밖 R04 사례를 합친 후보를 제거하고 R04를 source에 추가 | 사용자/group, chmod, chown/chgrp, R04 download directory 오류를 prose·표로 분리 완료 |
| `wiki/concepts/linux-web-server-apache-nginx.md` | 세션 1 `bash` 2 → 현재 0 | host service/UFW와 Docker nginx를 각각 합성한 fence를 제거 | R04 host webserver, R05 container webserver, R07 container proxy를 prose·표로 분리 완료 |
| `wiki/comparisons/git-fetch-vs-pull-vs-clone.md` | 세션 1 `bash` 1 → 현재 0 | placeholder URL과 R09 clone/pull·R10 fetch를 한 실행 예처럼 합친 fence를 제거 | 새 repository 생성·remote-tracking 갱신·현재 branch 통합을 날짜·artifact별 prose·표로 분리 완료 |

### fence 공통 처리 규칙

1. 실행 세션에서 해당 페이지의 모든 fence를 선언된 텍스트 raw와 공백 정규화 연속 부분문자열로 대조한다.
2. PDF/PNG만 근거인 fence는 자동 일치로 가장하지 않고 수동 예외와 page/artifact를 기록한다.
3. Linux·Git·Docker CLI fence는 `shell` 태그를 사용한다. `bash`는 남기지 않는다.
4. 명령·출력·설명문을 한 fence에 섞지 않는다. 출력은 별도 `text` fence 또는 prose로 구분한다.
5. 여러 날짜·멀리 떨어진 원문 명령을 합쳐 수업 원문처럼 보이게 하지 않는다. 설명용 합성이라면 명시하거나 prose/표로 바꾼다.
6. 실제 계정명·저장소 URL·비밀번호·token은 재노출하지 않는다.

## 실행 세션 분할

과목 전체는 총 **10개 세션**으로 분할한다. 세션 1은 기준선 재고, 세션 2~9는 지식 페이지 실행 묶음, 세션 10은 전체 대응·provenance·구조 고정점이다. 세션 10까지 모두 완료했으며 각 세션은 지정 범위만 처리하고 다음 세션을 자동 실행하지 않았다.

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

## 세션 7 실행 결과 — Dockerfile·reverse proxy·Compose Concept/Entity

- 상태: **완료**. 세션 8과 Linux 단계 5 전체 완료 처리는 시작하지 않았다.
- 고도화: `docker-reverse-proxy-load-balancing`, `docker-compose-manifest`, `docker` 3개를 고도화하고 `docker-registry-tag-push-pull` Concept를 신규 생성했다.
- reverse proxy: R07의 `proxy-net`, Apache/Nginx backend 여섯 개, host-mounted `nginx.conf`, host 80의 `reverse-proxy`, URL별 upstream과 browser 분배를 복원했다. container 실행·network·config·proxy process·backend 응답·browser 분배를 별도 완료 조건으로 두고, 독립 `nginx -t`·proxy log·운영 health check는 미보존으로 남겼다. I03은 user 업무를 상담자에게 분배하는 비유일 뿐 network·port·container 증거로 쓰지 않았다.
- Compose: R08의 MySQL+Spring Boot와 MySQL+WordPress를 각각 service 이름·`container_name`·image·network·volume·environment·ports·`depends_on`에 연결했다. 제공 WordPress manifest의 들여쓰기 수정과 요구사항 값 수정을 구분하고, 요구사항 network 이름 불일치와 후속 volume 삭제 이름 불일치도 보존했다. `up`·container `Up`·DB readiness·browser 성공·`down`·image/volume 삭제를 분리했다.
- Docker Entity: R05 설치/image/container→R06 network/storage/commit/registry→R07 Dockerfile/Spring+DB/proxy→R08 Compose의 날짜별 기술 이력과 artifact를 복원했다. Linux host·Docker Engine·image/container/network/volume·Dockerfile·Compose·registry·CI/CD의 책임을 분리했다.
- registry 후보: **신규 Concept로 보존**. local image의 기본 생명주기와 달리 namespace/repository/version naming, login, layer push/digest, 다른 환경 retrieval, namespace 누락 오류, credential 저장 경고, 수동/CI 경계가 독립 탐색 역할을 갖는다. push와 remote repository 확인은 기록됐지만 다른 환경의 최종 browser/file 동일성은 미보존이다.
- fence: 세션 시작 직접 대상 4개(`text 1 / nginx 1 / yaml 1 / bash 1`)를 전수 조사했다. 합성 3개는 credential 없는 prose·표로 전환했고, `nginx` 1개는 R07 lines 803~844의 공백 정규화 연속 원문으로 교체했다. 최종 `1 / 원문 일치 1 / 수동 예외 0 / 실패 0`, Linux/Docker command `bash 0`이다.
- 검증: 대상 frontmatter·source 실경로·허용 tag·wikilink·placeholder, R06·R07·R08·R11 대응 4/4·미분류 0, Total pages 272, credential/실제 식별자 비노출, scoped `git diff --check`, raw status/diff 무변경을 확인했다. 보조 PDF·P08·P09·I03은 날짜 MD에 없는 수업일·성공 결과를 만들지 않았다.
- 범위: Summary·Comparison·Query, 세션 6 Docker core Concept 4개, Git/GitHub 페이지, 상위 계획, `raw/`를 수정하지 않았다.

## 세션 8 실행 결과 — Git·GitHub Entity/Concept

- 상태: **완료**. 세션 9와 Linux 단계 5 전체 완료 처리는 시작하지 않았다.
- 실행 범위: 기존 `git-github-collaboration`, `git`, `github`, `source-tree` 4개를 고도화했다. 신규 지식 페이지는 만들지 않았고 Summary·Comparison·Query·Docker 관련 페이지·sudo/root·permission 후보는 수정하지 않았다.
- raw 대응: R09·R10 날짜 MD를 실제 수업일·교시·artifact·실행 결과의 최우선 근거로, R11을 복습 허브로 사용해 3/3·미분류 0건을 확인했다. P04는 Git Bash P.11~31, SourceTree P.35~60, branch·PR·conflict P.62~131의 화면 절차만 보조했으며 독립 수업일이나 성공 결과를 만들지 않았다.
- 협업 artifact: R09의 `myfile.txt` untracked→stage→commit→remote, commit 없는 `world.txt` push, remote `hello.txt` pull, clone한 두 local repository와 SourceTree push 거부·수동 통합, `animal` branch 시작을 복원했다. R10은 팀원 clone, `sport` push, `animal`·`sport` PR 생성·review·merge, remote `master`→각 local `master` pull, fetch→remote-tracking branch→local branch, `Main.java`·`Cat.java` conflict와 merge/rebase 범위를 복원했다.
- 상태·완료 조건: working tree·staging area·commit·local branch·remote-tracking branch·remote branch·PR·merge 결과를 분리했다. add·commit·push·fetch·pull·merge·rebase의 입력→처리→결과와 branch push·PR 생성·PR merge·remote master 갱신·local master pull·fetch·conflict 해결의 완료 증거를 각각 기록했다.
- 책임·과목 경계: Git의 local 상태·이력, GitHub의 remote hosting·PR review/merge, SourceTree와 IntelliJ의 서로 다른 client 실행, GitHub Actions의 후속 workflow 책임을 분리했다. Java의 개인 local/remote 선행, Linux 05-04~05-06 팀 협업 직접 수업, CI/CD push trigger 후속 활용을 같은 학습일·성공 상태로 합치지 않았다.
- fence·보안: 세션 시작 직접 대상 fence 2개(`bash` 2)를 전수 조사해 placeholder URL·합성 feature branch 명령을 prose·표로 전환했다. 최종 대상 `0 / 원문 검증 0 / 수동 예외 0 / 실패 0`, Git/Linux command `bash` 0개다. P04는 prose 근거만 사용했으며 실제 account·email·repository URL·organization·password·PAT·token·one-time code·credential 재노출은 0건이다.
- 구조·상태: 대상 frontmatter·R09·R10·R11·P04 source 실경로·허용 tag·wikilink·placeholder를 확인했다. 신규 페이지가 없어 Total pages는 272를 유지했고, index는 고도화된 책임 설명과 실제로 어긋난 4개 한 줄 설명만 갱신했다. `raw/KoreaICT/5. Linux`는 수정하지 않았으며 상위 계획·세션 9 대상은 건드리지 않았다.

## 세션 9 실행 결과 — 최종 Comparison/Query

- 상태: **완료**. 세션 10과 Linux 단계 5 전체 완료 처리는 시작하지 않았다.
- 실행 범위: 기존 Comparison 6개를 고도화하고 `sudo-vs-sudo-su-vs-root-session` Comparison과 `why-sudo-created-directory-denies-normal-user` Query를 신규 생성했다. `dockerfile-vs-compose`는 기존 위치·type 불일치를 유지한 채 내용 책임만 고도화했다.
- Docker 비교: R06~R08 날짜 MD를 최우선으로 commit snapshot/Dockerfile recipe/Compose runtime, cp 일회 copy/bind host link/named volume, build·container·network·DB·browser·down 완료 상태를 분리했다. P02~P03·P08은 날짜 MD에 전사된 이론·화면 절차와 registry naming 경고만 보조했으며 실제 account·repository URL·credential은 옮기지 않았다.
- Git·network·VM 비교: R09 clone/pull과 R10 fetch를 새 repository·remote-tracking·현재 branch 통합으로 분리했다. R01·R05~R08은 VM guest OS→Docker host→container, Windows host→VirtualBox NAT→guest iptables/UFW→Spring process, Docker host→container publish를 서로 다른 계층과 함께 쓰는 관계로 복원했다.
- 신규 후보 판정: sudo/root 후보는 R01·R03~R05·R08의 반복 관리자 작업과 R03의 명시적 “꼭 root?” 혼동 때문에 독립 Comparison으로 보존했다. permission 후보는 R03 `touch`와 R04 MobaXterm drag-and-drop의 반복 `Permission denied`를 실행 주체→ownership→directory `w/x`→최소 `chown`/`chmod` 선택으로 종합할 troubleshooting 가치가 있어 Query로 보존했다.
- fence·보안: 기존 `git-fetch-vs-pull-vs-clone`의 placeholder URL·합성 `bash` fence 1개를 prose·표로 제거했다. 세션 9 대상 최종 `0 / 원문 검증 0 / 수동 예외 0 / 실패 0`, `bash` 0개다. Linux 직접 페이지 전체에서 미처리 fence는 0개이고 R07 연속 원문과 일치하는 `nginx` fence 1개만 유지한다. 실제 account·email·repository URL·password·PAT·token·credential 재노출은 0건이다.
- 구조·상태: 8개 대상의 frontmatter·source 실경로·허용 tag·wikilink·placeholder·선택 상황·함께 쓰기·오류·완료 조건을 확인했다. 신규 2개를 index에 등록하고 Total pages를 274로 재계산했다. `raw/KoreaICT/5. Linux`는 수정하지 않았으며 상위 계획·후속 경계 본문은 건드리지 않았다.

## 세션 10 실행 결과 — 과목 전체 고정점

- 상태: **최종 완료**. Linux 직접 source 지식 페이지 39개와 후속 경계 15개, raw R01~R11·P01~P10·I01~I03 대응, 구조·내용·provenance·보안 고정점을 전수 재검증했다. 단계 6 AWS는 시작하지 않았다.
- 세션 9 경고 재검증: 경고 대상 기존 6개는 모두 Git diff와 실제 본문에서 `updated: 2026-07-18`, 선택 상황·함께 쓰는 관계·artifact·오류·완료 조건 보강이 확인됐다. 신규 Comparison·Query, `wiki/index.md`, `wiki/log.md`, 이 inventory와 상호 대조해 부분 적용·본문 누락은 없다고 판정했다.
- 직접 페이지 수: knowledge 디렉터리와 frontmatter를 각각 다시 계산해 39개를 확인했다. 디렉터리 기준은 `summaries 11 / concepts 15 / entities 6 / comparisons 6 / queries 1`, frontmatter type 기준은 `summary 11 / concept 14 / entity 6 / comparison 7 / query 1`이다. 차이는 `concepts/dockerfile-vs-compose.md`의 기존 위치/type 불일치 1개뿐이다.
- raw 대응: R01~R11은 실제 경로 11/11과 직접 page source union 11/11, 대표 anchor와 최초 등장·후속 확장·artifact·오류·완료 조건을 모두 대조했다. P01~P10과 I01~I03은 inventory 실제 경로 10/10·3/3을 유지했다. P01·P05·P10은 독립 page source를 강제하지 않고 각각 AWS 가입 예고·Librarian 반복·OpenSSH 보조 경계로만 남겼다.
- 내용·탐색성: Summary·Concept·Entity·Comparison·Query의 유형별 의미 게이트와 직접/후속 경계를 통과했다. 신규 sudo/root Comparison과 permission Query가 상호 링크뿐 아니라 04-24·04-27 Summary, Linux 권한 Concept, Linux Entity에서 탐색되도록 관련 링크 8개만 최소 보강했다. 후속 AWS/CI/CD 경계 15개는 존재·책임 경계·Linux 비직접 source 상태를 유지했다.
- 구조: 필수 frontmatter·type·status·confidence·허용 tag·source 실경로 오류 0건, 깨진 링크·고립·index 누락·등록 중복 0건이다. `wiki/index.md`의 등록 274개와 실제 page 수 274개가 일치해 index는 수정하지 않았다. actionable placeholder와 `sources: []`, `관련 raw 참조`, `추후 보강 대상`, needs-review/low-confidence는 0건이다.
- 장문 판정: 지식 페이지는 200줄 초과가 없다. 이 inventory 자체만 200줄을 넘지만 raw 대응표·세션별 실행 이력·고정점 근거를 보존하는 단일 운영 문서이므로 이번 단계에서는 분할하지 않는다.
- fence: Linux 직접 source 지식 페이지 전체 fence는 `nginx` 1개뿐이며 미처리 0, `bash` 0이다. `docker-reverse-proxy-load-balancing.md`의 40줄 `nginx` fence는 R07의 실제 fenced 원문과 exact substring으로 일치하고 서로 다른 날짜·명령·출력을 합치지 않았다.
- 보안·Git: Linux wiki 변경분에서 실제 account·email·repository URL·password·PAT·token·credential·one-time code 지표 0건이다. scoped `git diff --check`를 통과했고 `raw/KoreaICT/5. Linux`의 status/diff는 0건이다. Linux 범위 밖 기존 Python raw 변경은 보존했고 Git commit·push는 수행하지 않았다.

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

## 세션 5 실행 결과 — VM·SSH·process·service·network·server Concept/Entity

- 실행 범위: 기존 `linux-spring-boot-server-deploy`, `linux-web-server-apache-nginx`, `linux`, `maven` 4개를 고도화하고, `linux-process-service-port-firewall` Concept 1개를 신규 생성했다. Summary·Comparison·Query·Docker core·세션 4 Concept는 수정하지 않았다.
- raw 대응: R01·R03~R05·R07·R11 6/6을 지정 핵심 근거로 대조했고, Linux Entity의 날짜 이력을 위해 R02도 기존 source로 유지했다. R01 SSH service, R03 script 권한/process 기초, R04 Apache/Nginx·UFW, R05 Maven JAR·9000·NAT/iptables, R07 Dockerfile JAR 후속, R11 복습 연결의 미분류는 0건이다. P06~P07은 기존 Linux Entity의 실습·이론 교안 source를 유지했지만 날짜·실행 성공을 새로 만들지 않았고, P10은 R01에 전사된 9줄 보조 메모로 확인해 page source로 강제하지 않았다.
- Spring Boot·Maven: R05의 기존 80번 service 정리→project/9000 확인→VirtualBox NAT host 8100→guest 80→guest iptables 9000→UFW→Maven 설치/version→project root package→`target` JAR→host `java -jar`→browser를 복원했다. 설치·package·artifact·process·port 경로·browser를 별도 완료 조건으로 두고, R07 Dockerfile COPY/ENTRYPOINT와 CI Maven build는 후속 책임으로 분리했다.
- host web server: 누락됐던 핵심 R04를 `linux-web-server-apache-nginx` frontmatter에 추가했다. Apache/Nginx package·enable/start/status, UFW 22/80/443과 SSH 보호, `/var/www/html/` 기본 index backup·교체·service stop/start·browser 결과를 복원하고 R05 정적 web container, R07 reverse proxy/load balancing과 구분했다.
- Linux Entity: VirtualBox Ubuntu guest→OpenSSH service→bridge/IP→MobaXterm client→CLI/permission→Java·host web service→Spring JAR의 날짜별 이력을 복원했다. Linux OS의 process/service/firewall/filesystem 책임과 Git·Maven·Spring Boot·Docker 도구 책임, EC2 Linux instance·CI/CD deploy target의 후속 적용을 분리했다.
- 신규 후보 판정: process→service→listening port→firewall→NAT/redirect→client 응답은 SSH·Apache/Nginx·Spring에서 반복되는 독립 troubleshooting 축이다. 기존 server Concept와 Linux Entity에 분산 흡수하면 특정 server를 모를 때 탐색성이 떨어지므로 Concept 1개를 생성하고 기존 대상 4개에서 역링크했다. VM·SSH·service·firewall·port 별도 Comparison은 만들지 않았다.
- provenance·보안: 대상 기존 fence 4개(`bash` 3, `dockerfile` 1)는 R05·R07의 떨어진 명령/instruction을 합친 합성 후보여서 prose·표로 해소했다. 최종 대상 5개 fence 전체 0개/선언 source 원문 검증 0개/수동 예외 0개/실패 0개, `bash` 잔존 0개다. 실제 IP·account·email·repository URL·password·token·one-time code 재노출은 0건이다.
- 구조·상태: 대상 5개 frontmatter·source 실경로·허용 tag·wikilink·placeholder 오류 0건, source union에 R01~R05·R07·R11과 P06~P07이 존재한다. 신규 Concept를 index에 등록하고 설명 4개를 현재 내용에 맞춰 최소 수정했으며, 실제 정의 `wiki/**/*.md - index.md - log.md`로 Total pages 271을 확인했다.
- 상태: 세션 5만 완료했다. 단계 5 Linux는 미완료이며 세션 6, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## 세션 6 실행 결과 — Docker core Concept

- 실행 범위: 기존 `docker-install-permission-setup`, `docker-image-container`, `docker-cp-exec-container-files`, `docker-network-volume` 4개만 부분 보강했다. Summary·Entity·Comparison·Query와 Dockerfile·reverse proxy·Compose Concept는 수정하지 않았고 신규 지식 페이지를 만들지 않았다.
- raw 대응: R05·R06·R08 날짜 MD를 수업일·교시·실습 순서와 실행 결과의 최우선 근거로 사용하고 R11은 복습 연결로만 사용했다. 대상 source union은 R05·R06·R08·R11 4/4이며 미분류 0건이다. P09는 05-01 새 VM의 OpenSSH/UFW/Docker setup checklist를 보조했지만 R05 성공 결과를 대체하지 않았다. P02~P03은 필요한 이론·절차가 날짜 MD에 충분히 전사되어 page source나 fence 예외로 강제하지 않았다.
- 설치·권한: setup script 준비→CRLF 교정→실행 권한→설치→Docker service active→일반 사용자 group 등록→재login 후 socket 접근을 분리했다. Linux filesystem/systemd/group·session과 Docker client/daemon의 책임, 설치됨·service·권한 반영·일반 사용자 명령 성공을 별도 완료 조건으로 복원했다.
- image·container: R05의 `httpd`·Nginx·MySQL·WordPress 기성 image와 pull→run→Up/Exited→remove, detached/name, host/container port, browser·DB readiness를 분리했다. R06 commit image는 후속 연결로만 두고 R07 Dockerfile image·registry·CI image와 합치지 않았다.
- exec·cp: R05의 `apache81/82`, `nginx83/84`, `mysql85`와 R06의 `apache01-ctr`, `nginx88`을 각각 실제 document root와 연결했다. host→container·container→host 일회 copy, 내부 file 확인, browser 반영, 변경 container→commit image를 별도 완료 조건으로 두고 mount와 구분했다.
- network·storage: R05 WordPress–MySQL `network01`, R06 MariaDB–Redmine `network02`, Apache/Nginx bind mount, `mount-vol`을 복원했다. container name 통신과 host port, 빈 bind source의 Apache `Index of /`·Nginx 403, bind/named volume 관리 책임을 분리하고 R06에는 container 재생성 후 data persistence 실측이 없음을 명시했다. R08 Compose 선언은 후속 manifest 활용으로만 연결했다.
- provenance·보안: 대상 기존 `bash` fence 4개는 날짜·container·network·mount의 떨어진 명령을 합친 후보여서 prose·표로 해소했다. 최종 대상 fence 전체 0개/선언 source 원문 검증 0개/수동 예외 0개/실패 0개, `bash` 잔존 0개다. 실제 IP·account·email·repository URL·Docker Hub account·password·token·one-time code 재노출은 0건이다.
- 구조·상태: 대상 4개 frontmatter·source 실경로·허용 tag·wikilink·placeholder 오류 0건이다. 신규 페이지와 index 설명 불일치가 없어 `wiki/index.md`는 수정하지 않았고 Total pages는 실제 정의에 따라 271이다. Docker registry 신규 후보는 세션 7 판단으로 유지했다.
- 상태: 세션 6만 완료했다. 단계 5 Linux는 미완료이며 세션 7, 상위 계획의 단계 5 완료 기록, 단계 6 AWS, Git commit·push를 시작하지 않았다.

## 관련 페이지

- [[_meta/wiki-content-rehighquality-work-plan|LLM Wiki 내용 재고도화 작업 계획]]
- [[_meta/frontend-backend-rehighquality-inventory-plan|FrontEnd_BackEnd 내용 재고도화 전수 재고와 실행 분할 계획]]
- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]
- [[entities/linux|Linux]]
- [[entities/docker|Docker]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
