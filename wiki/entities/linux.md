---
title: Linux
created: 2026-07-02
updated: 2026-07-18
type: entity
tags: [linux]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.23(목)/2026.04.23(목).md
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 이론.pdf
  - raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# Linux

## 무엇인가

Linux는 server에서 널리 사용하는 Unix 계열 운영체제다. 이 위키에서는 단순 명령어 목록이 아니라, FrontEnd_BackEnd에서 만든 application을 **원격 guest OS에 배치하고 process·service·file·permission·network를 운영하는 환경**으로 배웠다.

## 첫 등장: VirtualBox Ubuntu guest와 SSH

[[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22]]에 VirtualBox가 Ubuntu Server guest VM을 실행하고, guest의 OpenSSH service가 접속을 받으며, Windows의 MobaXterm이 SSH client로 연결하는 구조로 처음 등장했다.

1. Ubuntu ISO로 guest OS를 설치했다.
2. OpenSSH package를 설치하고 `ssh` service를 시작했다.
3. status의 `active (running)`으로 service 실행을 확인했다.
4. VirtualBox adapter를 NAT에서 bridge로 바꾸고 guest IP를 확인했다.
5. MobaXterm이 guest IP의 22번 port에 접속해 일반 사용자 prompt를 열었다.

VirtualBox·Ubuntu·OpenSSH·MobaXterm은 한 제품이 아니다. VM 실행, guest OS, server service, client라는 네 책임을 분리하는 것이 Linux 운영 학습의 출발점이었다. ^[raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md]

## 이 위키에서 Linux가 맡는 책임

| Linux OS가 직접 맡은 것 | Linux 위에서 사용했지만 별도 도구가 맡은 것 |
|---|---|
| user·group·file permission, process, systemd service, UFW·iptables, filesystem, network interface | Git의 source history, Maven의 Java build, Spring Boot의 application logic, Docker의 container lifecycle |

예를 들어 Linux가 Maven package를 대신하거나 Spring Controller를 실행 로직으로 정의하는 것은 아니다. Linux는 Maven·Java·Spring Boot·Docker process가 실행될 OS·file·permission·network 기반을 제공하고 그 상태를 관찰한다.

## 날짜별 학습 이력과 확장

### 04-22 — VM·SSH·prompt·path

- VirtualBox Ubuntu guest 2대를 준비했다.
- bridge network와 guest IPv4를 확인했다.
- OpenSSH 설치·start·status, 22번 UFW, MobaXterm session을 연결했다.
- `$` prompt, `/`, home, 절대·상대 path를 배웠다.

### 04-23 — file·directory·vi

[[summaries/2026-04-23-linux-files-vi|04-23]]에는 방송사 directory tree에서 생성·복사·이동·검색을 수행하고, vi의 명령/입력/마지막 행 mode와 redirection·`more`·`diff`로 file 상태를 확인했다. 이 기능은 후속 server 설정·homepage·Dockerfile 관련 file을 다루는 선행이 됐다.

### 04-24 — user·group·permission·실행

[[summaries/2026-04-24-linux-users-permissions|04-24]]에는 account file, UID/GID, home/login shell, owner/group/others와 `r/w/x`를 읽었다. `chmod`·`chown`·`chgrp`로 access와 ownership을 바꾸고, root 소유 directory와 실행 권한 없는 script의 `Permission denied`를 실패→원인 확인→수정→성공으로 검증했다.

R03의 제목에는 process monitoring이 있었지만 날짜 원본에 보존된 직접 실행은 script 권한과 실행 결과까지다. `ps`·`grep`·`kill`의 일반 process 연결은 R11 복습에서 명시됐으며, R03에 없는 종료 결과를 만들어내지 않는다.

### 04-27 — server file 준비·Java·host web service

[[summaries/2026-04-27-linux-archive-java-alias|04-27]]에는 `apt`, download, archive, ownership, alias로 server file을 준비했다. JDK를 설치해 Java source를 compile/run했고, Apache와 Nginx를 Ubuntu host service로 각각 실행했다. UFW의 22·80·443, `/var/www/html/`의 homepage, service stop/start와 browser 결과가 Linux 운영 기능으로 연결됐다.

### 04-28 — Maven JAR·host process·port 계층·Docker 입문

[[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]]에는 Spring Boot project를 Maven으로 package해 `target` JAR를 만들고 `java -jar` process로 실행했다. Windows host→VirtualBox NAT→guest 80→iptables 9000→Spring process 경로와 UFW rule을 연결해 browser 응답을 확인했다.

같은 날 Docker를 설치하고 Docker service·group을 준비했지만, image/container/network 생명주기는 Linux OS 자체 기능이 아니라 Linux 위의 [[entities/docker|Docker]] 책임이다.

### 04-29 이후 — Linux 기반 위의 별도 도구 확장

04-29~05-01은 Docker network·storage·registry·Dockerfile·Compose, 05-04~05-06은 Git/GitHub 협업으로 확장됐다. 이들은 Linux terminal과 filesystem을 사용했지만 각각 Docker와 Git/GitHub의 직접 학습이다. 전체 연결은 [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]가 맡는다.

## process·service·network가 연결되는 이유

Linux server에서 browser 응답이나 SSH 연결은 하나의 설정으로 완성되지 않는다.

| 관찰 축 | 수업 artifact | 묻는 질문 |
|---|---|---|
| process | script, `java -jar`, web server process | 실행 단위가 실제로 떠 있는가 |
| service | SSH·Apache·Nginx·Docker와 `systemctl` | background program의 시작·중지·상태·boot 정책은 무엇인가 |
| listening port | SSH 22, HTTP 80/443, Spring 9000 | 어느 process가 어느 접점에서 요청을 기다리는가 |
| firewall | UFW rule | inbound 요청이 허용되는가 |
| redirect/NAT | VirtualBox NAT, guest `iptables` | 요청이 어느 계층에서 다른 port로 전달되는가 |
| client result | MobaXterm prompt, browser page | 전체 경로를 통과한 최종 응답이 있는가 |

세부 troubleshooting 순서는 [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]이 맡는다.

## 대표 입력 → 처리 → 결과

### SSH로 guest OS 운영 시작

- 입력: 실행 중인 Ubuntu VM, bridge IP, OpenSSH package와 SSH session 정보
- 처리: OpenSSH service start/status→22번 허용→MobaXterm 접속
- 결과: 일반 사용자 prompt와 home path 확인

### Spring Boot를 Linux process로 실행

- 입력: Spring source, `pom.xml`, Maven, application 9000 port, VM/guest network rule
- 처리: package→JAR 확인→`java -jar`→NAT·redirect·UFW 연결
- 결과: IDE 밖 Linux process와 browser HTTP 응답

이 두 실습은 “server에 접속하는 단계”에서 “server가 application 요청을 처리하는 단계”로 Linux의 역할이 확장된 흐름이다.

## 확인된 범위와 경계

### Linux 과목에서 직접 확인

- VirtualBox Ubuntu guest, bridge/NAT, OpenSSH·MobaXterm
- CLI·file·vi·user·group·permission
- JDK/Java, Apache/Nginx host service, UFW·iptables
- Maven JAR와 Spring Boot host process

### 다른 기술의 책임

- Git/GitHub: source와 협업 history
- Maven: `pom.xml` 기반 dependency·build와 JAR artifact
- Spring Boot: application logic와 9000 HTTP service
- Docker: image/container/network/mount/Compose

### 후속 과목에서 적용

AWS EC2는 Linux instance이지만 VPC·Subnet·Public IP·Key Pair·Security Group은 AWS resource다. CI/CD의 deploy target도 Linux server일 수 있지만 workflow trigger·runner·자동 build/deploy는 CI/CD 책임이다. Linux에서 같은 명령을 재사용했다는 이유로 후속 cloud·pipeline 성공을 Linux 직접 수업에 포함하지 않는다.

## 자주 헷갈리는 점

- **VM과 Linux:** VirtualBox VM은 가상 hardware 환경이고 Ubuntu Linux는 그 안의 guest OS다.
- **SSH service와 MobaXterm:** service는 guest에서 접속을 받고, MobaXterm은 요청하는 client다.
- **process와 service:** 모든 service는 process로 실행되지만, `systemctl`로 관리되는 unit의 boot·상태 책임까지 모든 임시 process가 갖는 것은 아니다.
- **UFW와 listening:** firewall 허용은 통행 규칙이며, 요청을 받을 process가 실행 중이어야 한다.
- **bridge와 NAT:** bridge는 guest가 network에서 별도 IP를 받는 방식이고, 04-28 NAT forwarding은 host port를 guest port로 전달하는 경계다.
- **Linux와 Docker:** Docker가 Linux 위에서 실행돼도 image/container 생명주기는 Linux OS 기능과 구분한다.
- **Linux firewall과 AWS Security Group:** UFW는 instance OS 내부 rule, Security Group은 AWS network resource의 rule이다.

## 프로젝트·면접에서 설명할 관점

“Linux 명령어를 배웠다”보다 다음처럼 설명할 수 있다.

> VirtualBox Ubuntu guest에 SSH로 접속해 file·permission을 관리하고, Apache/Nginx와 Spring Boot JAR를 host process/service로 실행했다. 접속 실패를 process, service, listening port, UFW, NAT/iptables, client 응답으로 나눠 확인했으며, 이후 Docker·EC2·CI/CD에서는 이 Linux 기반을 별도 도구와 cloud 계층으로 확장했다.

## 관련 개념

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[comparisons/sudo-vs-sudo-su-vs-root-session|sudo vs sudo su - vs root session]]
- [[queries/why-sudo-created-directory-denies-normal-user|sudo로 만든 디렉터리의 권한 오류 진단]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]
- [[entities/maven|Maven]]
- [[entities/docker|Docker]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md`부터 `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`까지 — VM/SSH→CLI/file/permission→host server/JAR의 날짜별 직접 흐름
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — process·service·port와 Docker/Git 후속 연결의 복습 허브
- `raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — 날짜 MD에 전사된 VM·SSH·권한·web server 절차의 실습 교안
- `raw/KoreaICT/5. Linux/교육 자료/Linux/Linux 이론.pdf` — filesystem·shell·permission의 이론 보조자료
