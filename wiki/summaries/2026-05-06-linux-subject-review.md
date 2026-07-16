---
title: Linux 총정리
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [linux, docker, github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
status: growing
confidence: high
---

# Linux 총정리

## 한 줄 요약

5과목은 Ubuntu VM에 원격 접속해 CLI·권한·service·port를 다루는 데서 시작해 Java/Spring server를 직접 실행하고, Docker image/container/network/storage/Dockerfile/Compose로 실행환경을 재현한 뒤 Git/GitHub branch·PR·conflict 협업으로 마무리한 과정이다.

## 이 페이지의 역할과 출처 경계

이 페이지는 04-22~05-06의 복습 경로를 보여 주는 **과목 허브**다. 각 날짜의 교시·명령·오류·실행 결과를 대신하지 않으며, 구체적인 재현은 연결된 날짜 Summary와 날짜 MD를 우선한다.

- `Linux 총정리.md`는 과목 전체 개념을 한 번에 복습하기 위한 통합 원본이다.
- 실제 수업일·교시·artifact의 최우선 근거는 날짜별 MD 10개다.
- 총정리 원본의 일반 예시와 날짜 실습의 실제 이름·결과가 다르면 날짜 MD를 우선한다.
- Linux에서 직접 수행한 VM·server·Docker·Git 실습과 후속 AWS EC2·CI/CD 적용을 구분한다.

## 왜 이 순서로 배웠는가

1. **접속 기반:** 먼저 server 역할을 할 Ubuntu VM을 만들고 SSH로 들어갈 수 있어야 했다.
2. **운영 기본기:** remote terminal에서 file·vi·user·group·permission을 다뤄야 설치와 설정을 안전하게 수행할 수 있었다.
3. **server 실행:** Java와 Spring Boot artifact를 Linux process로 띄우며 service·port·firewall을 연결했다.
4. **환경 재현:** host에 직접 설치하는 방식의 반복 비용을 image/container/network/storage로 분리했다.
5. **다중 service:** Dockerfile로 image 생성 절차를 기록하고 Compose로 DB+application 관계를 선언했다.
6. **협업:** 실행환경뿐 아니라 source 변경도 여러 작업자가 branch·PR·merge로 관리하게 했다.

즉, “서버에 접속한다 → 파일과 권한을 다룬다 → application을 실행한다 → 실행환경을 image로 재현한다 → 여러 service를 묶는다 → source 변경을 협업한다”는 순서다.

## 날짜별 대표 artifact와 전환 이유

| 날짜 | 대표 artifact·확인 결과 | 다음 단계로 넘어간 이유 |
|---|---|---|
| [[summaries/2026-04-22-linux-install-ssh-cli|04-22]] | VirtualBox Ubuntu VM, bridge IP, OpenSSH service, MobaXterm session, prompt·절대/상대 경로 | remote server에 들어가는 기반을 만든 뒤 실제 file을 다룰 필요가 생김 |
| [[summaries/2026-04-23-linux-files-vi|04-23]] | 방송사·Librarian directory tree, `vi` 3모드, redirection, `more`, `diff` | file 생성·수정 뒤 누가 접근할 수 있는지 permission으로 확장 |
| [[summaries/2026-04-24-linux-users-permissions|04-24]] | account file, UID/GID, owner/group/others, `chmod`·`chown`·`chgrp`, script 실행 오류 | 권한을 갖춘 환경에서 package·Java·web server를 설치·실행할 준비 |
| [[summaries/2026-04-27-linux-archive-java-alias|04-27]] | download/archive, alias, JDK/JDBC, Java compile/run, Git remote, **host Apache·Nginx와 UFW** | host에 직접 server를 설치한 뒤 Spring JAR와 container 실행으로 이동 |
| [[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]] | Maven JAR, `java -jar`, guest 80→9000 경로, Docker install·lifecycle, WordPress–MySQL network | image/container 기본에서 통신·저장·배포 생명주기로 확장 |
| [[summaries/2026-04-29-docker-network-volume-image|04-29]] | MariaDB–Redmine, `exec`·`cp`, bind mount·named volume, `commit`, **Docker Hub tag·push·pull** | snapshot 전달 경험을 재현 가능한 Dockerfile로 바꿀 필요가 생김 |
| [[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30]] | build context, Spring JAR image+MySQL, `proxy-net`, Nginx upstream·`proxy_pass`, browser round-robin | 여러 수동 container 설정을 manifest 하나로 관리할 필요가 생김 |
| [[summaries/2026-05-01-docker-compose|05-01]] | MySQL+Spring Compose YAML, network·volume·environment·`depends_on`, `up/down`, Docker Desktop | 실행환경 묶음을 마친 뒤 source 이력과 팀 협업으로 전환 |
| [[summaries/2026-05-04-git-github-sourcetree|05-04]] | WorkTree→stage→local→remote, Git Bash, clone/pull, SourceTree, 두 작업자 push 충돌, branch 시작 | branch 변경을 검토·merge하는 PR 협업이 필요해짐 |
| [[summaries/2026-05-06-github-branch-pr-conflict|05-06]] | team branch, IntelliJ Git, PR review·merge, master pull, fetch, conflict와 merge/rebase | Linux 과목의 수동 운영·협업 흐름을 마치고 AWS 과목으로 전환 |

## 기능 흐름으로 다시 보기

### 1. VM과 SSH: 작업할 server에 들어간다

VirtualBox host 안에 Ubuntu guest VM을 만들고 bridge network에서 IP를 확인했다. guest에 OpenSSH server를 설치·실행하고 UFW에서 22번을 허용한 뒤 MobaXterm client로 접속했다.

여기에는 네 층이 있다: Windows host, Ubuntu guest OS, guest의 SSH service, MobaXterm client. 이후 [[entities/amazon-ec2|Amazon EC2]]는 cloud VM이지만, Key Pair·Security Group·public network라는 추가 계층을 AWS 과목에서 배운다.

### 2. CLI·파일·vi·권한: server를 안전하게 조작한다

방송사와 Librarian directory 실습에서 생성·복사·이동·검색·redirection·vi를 반복했다. 이어 account file과 UID/GID, owner/group/others, 숫자·기호 mode, 소유권 변경을 학습했다.

`Permission denied`는 application code 오류가 아니라 file/directory owner·permission 또는 실행 주체 문제일 수 있다. 이 기초는 Docker setup script, mount directory, EC2 deploy user에서 다시 나타난다.

### 3. Host web server와 Spring Boot: process·service·port를 연결한다

04-27에는 Linux host에 Apache와 Nginx를 직접 설치하고 document root·service 상태·UFW를 확인했다. 이것은 04-30의 Nginx container reverse proxy와 다른 층위다.

04-28에는 Spring project를 Maven으로 package해 JAR를 만들고 `java -jar`로 process를 실행했다. browser 요청이 guest의 진입 port, iptables redirect, application 9000 port를 거치는 경로를 확인했다. build artifact 생성, process 실행, port 허용, browser 응답은 각각 별도 완료 조건이다.

### 4. Docker core: 실행환경을 분해한다

- image: container를 만들기 위한 실행환경 artifact
- container: image를 실행한 process 단위
- network: container 사이의 이름 기반 통신
- port mapping: host 요청을 container service에 전달
- `docker exec`·`cp`: 실행 중 container 확인과 일회 파일 복사
- bind mount: host 경로 직접 연결
- named volume: Docker 관리 저장공간

04-29에는 수정한 container를 `commit`해 새 image로 만들고 Docker Hub registry에 tag·push했다. 다른 환경에서 registry namespace를 포함해 pull/run함으로써 **container 상태 → image → registry → 새 container** 생명주기를 확인했다.

### 5. Dockerfile·reverse proxy·Compose: 재현과 다중 service

Dockerfile은 base image·JAR·start process를 image recipe로 남겼다. Spring Boot image와 MySQL container를 같은 network에 연결해 DB row와 browser 화면까지 확인했다.

Nginx reverse proxy는 Apache·Nginx backend group 앞에서 `proxy_pass`로 browser 요청을 분배했다. 이는 Linux 과목에서 직접 구성한 container network 실습이며 AWS ALB를 만든 것이 아니다.

Compose는 MySQL+Spring Boot와 MySQL+WordPress의 service·network·volume·environment·port·의존 관계를 YAML로 선언했다. `up`은 관련 자원을 만들고 `down`은 container와 network를 내렸지만 image·volume은 남을 수 있었다.

### 6. Git/GitHub: source 변경을 상태와 이력으로 협업한다

WorkTree의 untracked·modified 파일을 stage하고 local commit으로 저장한 뒤 GitHub remote에 push했다. 다른 local repository는 clone 또는 pull로 변경을 받았다. SourceTree와 IntelliJ는 이 Git 상태를 GUI로 조작했다.

작업 branch를 push한 뒤 PR에서 비교·검토·merge하고, 각 local `master`를 다시 pull했다. 같은 파일의 같은 부분을 다르게 수정해 conflict를 만들고 merge/rebase 선택을 경험했다. GitHub Actions workflow는 아직 만들지 않았다.

## 대표 입력 → 처리 → 결과 연결

### Spring Boot를 재현 가능한 service로 실행

- 입력: Spring source, Maven 설정, DB·image 파일, Dockerfile
- 처리: Maven JAR build → Docker image build → MySQL·Spring container를 같은 network에 실행 → DB sample 입력
- 결과: container `Up`, Spring start log, DB row 조회, browser 9000 응답

### 여러 service를 Compose로 복원

- 입력: 준비된 image와 service 관계를 적은 YAML
- 처리: Compose가 network·volume·container를 생성하고 환경 변수를 전달
- 결과: 상태 목록, DB 작업, browser 화면, `down` 후 image·volume 잔존 확인

### branch 변경을 팀 `master`에 반영

- 입력: 작업 branch의 class 변경과 commit
- 처리: push → PR 생성 → review → merge → local master pull
- 결과: GitHub와 팀원 local에 merge된 file·history가 반영

## 시험·빈 교시·총정리의 경계

- 05-01 6교시는 Servlet/JSP·Spring·JPA를 묻는 **backend 시험**이다. Compose 실습이나 Linux 명령 평가로 합치지 않는다.
- 날짜 MD에 `이어서 작성` 또는 빈 heading만 있는 교시는 다른 자료로 성공 결과를 채우지 않는다.
- Linux 총정리 원본은 날짜별 학습을 압축한 복습 자료이며 독립 수업일이 아니다.
- 04-29 AWS 가입은 다음 과목 준비이고, 05-06 같은 날짜의 Cloud/VPC/EC2 학습은 별도 [[summaries/2026-05-06-aws-cloud-vpc-ec2|AWS Summary]]에 귀속한다.

## 자주 헷갈리는 연결

- **VM·Linux·container:** VM은 guest OS 전체, Linux는 그 OS, container는 Docker Engine 위의 격리된 process 단위다.
- **host web server·container web server·reverse proxy:** 04-27 host Apache/Nginx, 04-28 web container, 04-30 proxy container는 실행 위치와 책임이 다르다.
- **file 권한·network·port 오류:** 모두 browser 접속 실패처럼 보일 수 있지만 owner/permission, service 상태, firewall, port mapping을 따로 확인해야 한다.
- **`docker cp`·bind mount·volume:** 일회 복사, host 경로 연결, Docker 관리 저장공간의 차이다.
- **`commit`·Dockerfile·Compose:** 현재 container snapshot, image build recipe, 다중 service manifest의 차이다.
- **Docker Hub·GitHub:** image registry와 source/commit 협업 service다.
- **clone·fetch·pull:** 최초 복제, remote 정보 갱신, 현재 branch 반영의 차이다.
- **PR merge·local pull:** remote `master` 변경과 각 작업자의 local 최신화는 별도 단계다.

## Linux 직접 수업과 후속 적용 경계

### Linux 과목에서 직접 수행

- VirtualBox Ubuntu·SSH·CLI·user/group/permission
- host Apache/Nginx·Java/Spring Boot JAR 실행·UFW/iptables
- Docker image/container/network/mount/registry/Dockerfile/reverse proxy/Compose
- Git Bash·SourceTree·IntelliJ의 Git/GitHub branch·PR·conflict

### 후속 과목에서 직접 수행

- AWS: VPC·Subnet·Security Group·EC2·RDS·Route 53·ALB와 cloud 비용·자원 생명주기
- CI/CD: GitHub push trigger, Maven test/build, Docker Hub 자동 push, EC2 자동 갱신
- Passwordless·중간 프로젝트: Docker/Compose와 배포 기초의 실제 제품·프로젝트 적용

Linux에서 익힌 명령과 artifact가 후속 과목에 재사용되지만, 후속 resource·workflow의 성공을 Linux 수업 결과로 소급하지 않는다.

## 복습 순서

1. [[summaries/2026-04-22-linux-install-ssh-cli|VM·SSH]]와 [[summaries/2026-04-23-linux-files-vi|CLI·vi]]로 작업 위치와 file 상태를 복원한다.
2. [[summaries/2026-04-24-linux-users-permissions|권한]]과 [[summaries/2026-04-27-linux-archive-java-alias|package·Java·host web server]]를 연결한다.
3. [[summaries/2026-04-28-maven-spring-boot-docker-intro|Spring JAR·Docker 입문]]에서 host process와 container를 구분한다.
4. [[summaries/2026-04-29-docker-network-volume-image|network·mount·registry]], [[summaries/2026-04-30-dockerfile-spring-load-balancing|Dockerfile·proxy]], [[summaries/2026-05-01-docker-compose|Compose]]를 생명주기 순서로 읽는다.
5. [[summaries/2026-05-04-git-github-sourcetree|Git 상태 전이]] 뒤 [[summaries/2026-05-06-github-branch-pr-conflict|PR·conflict]]를 읽는다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[concepts/docker-compose-manifest|Docker Compose manifest]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]
- [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]

## 출처

- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux` 날짜별 MD 10개 — 실제 수업일·교시·artifact의 최우선 근거

이 허브는 날짜별 Summary를 대체하지 않는다. 총정리 원본의 통합 설명은 전체 흐름에 사용하고, 날짜 귀속·실행 결과·시험·빈 교시는 각 날짜 MD로 재조정했다.
