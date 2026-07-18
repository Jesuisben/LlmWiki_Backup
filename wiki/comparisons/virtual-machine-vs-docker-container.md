---
title: 가상 머신(VM) vs Docker 컨테이너
created: 2026-07-13
updated: 2026-07-18
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
status: stable
confidence: high
---

# 가상 머신(VM) vs Docker 컨테이너

## 비교 목적

Linux 과목은 VirtualBox Ubuntu VM 두 대와 SSH session을 만든 뒤, 그 Ubuntu에서 Docker Engine과 web·DB·Spring container를 실행했다. 둘 다 격리된 컴퓨터처럼 보이지만 VM은 **가상 하드웨어 위의 guest OS**, container는 **Docker host kernel을 공유하는 격리된 process·filesystem·network 단위**다.

## 한눈에 보기

| 비교 축 | VirtualBox VM | Docker container |
|---|---|---|
| 수업 artifact | Broadcast·Librarian Ubuntu guest | Apache·Nginx·MySQL·WordPress·Spring container |
| 격리 기준 | virtual hardware와 guest OS | process·filesystem·network namespace |
| 시작 입력 | VM 설정, ISO, CPU·memory·disk, account | image, name, port, network, volume, environment |
| 실행 주체 | VirtualBox hypervisor | Ubuntu 위 Docker Engine |
| 접속 | guest IP·22번 OpenSSH에 MobaXterm | Docker client/daemon, `exec`로 container 내부 process 실행 |
| 주요 목적 | OS·service·user·permission·firewall 실습 | application 실행환경을 image로 반복 생성 |

## 실제 선택 상황

### 상황 1: Ubuntu 자체와 SSH·systemd·UFW를 학습

VM을 선택한다. 04-22에는 Ubuntu 설치, account·CPU·memory·disk 설정, bridge network, guest IP, OpenSSH service, MobaXterm session을 확인했다. `active (running)`과 SSH login이 별도 완료 조건이었다.

### 상황 2: Apache·Nginx·MySQL을 여러 개 빠르게 반복

container를 선택한다. 04-28에는 기성 image로 여러 web/DB container를 만들고, 각각 name·host port·running 상태·browser/DB readiness를 확인했다. guest OS 전체를 새로 설치하지 않고 application 실행 단위를 분리했다.

### 상황 3: 새 VM에서 동일한 다중 service 환경 재현

VM을 새 host 경계로 준비하고 그 안에 Docker를 설치한 뒤 Compose로 MySQL+WordPress를 실행했다. VM과 container는 대체 선택만이 아니라 **host 계층과 application 계층으로 함께 사용**됐다.

## 함께 쓰는 관계

수업의 실제 계층은 다음과 같다.

`Windows host → VirtualBox → Ubuntu guest → Docker Engine → image → container → application process`

MobaXterm은 Ubuntu guest의 OpenSSH service에 접속하는 client이고, Docker `exec`는 이미 실행 중인 container 안에서 명령 process를 시작한다. 둘은 “안으로 들어간다”는 화면 경험만 비슷하다.

## 실제 오류·완료 조건

| 단계 | 확인 | 아직 보장하지 않는 것 |
|---|---|---|
| VM 실행 | guest console/login | network·SSH |
| bridge/NAT·guest IP | network interface와 IP | OpenSSH service·firewall |
| SSH service | `active (running)` | MobaXterm 인증 성공 |
| Docker service·권한 | daemon과 일반 사용자 client 접근 | image/container 존재 |
| container `Up` | 주 process 실행 | application readiness·browser 응답 |
| port publish | host→container port 표시 | VM 밖에서의 전체 접속 경로 |

## 흔한 오해와 확인되지 않은 범위

- MobaXterm은 VM이 아니라 SSH client다.
- `docker exec`는 VM에 SSH login하는 것이 아니다.
- container마다 Ubuntu kernel 전체가 새로 설치되는 것은 아니다. host kernel을 공유한다.
- container image와 VM disk image/ISO는 이름이 비슷해도 같은 artifact가 아니다.
- VM bridge/NAT·guest UFW와 Docker network/port mapping은 별도 계층이다.
- AWS EC2는 후속 cloud instance다. VirtualBox VM에서 배운 Linux 운영 지식은 재사용되지만 EC2·Security Group·cloud 비용 관리는 AWS 과목 책임이다.
- 수업에서는 hypervisor 종류 비교, kernel namespace/cgroup 내부 구현, container 보안 격리 한계의 실측까지 다루지 않았다.

## 관련 페이지

- [[summaries/2026-04-22-linux-install-ssh-cli|2026-04-22 Linux 설치·SSH·CLI]]
- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven·Spring Boot·Docker 입문]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/linux|Linux]]
- [[entities/docker|Docker]]
- [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` — VM 설치·bridge/IP·OpenSSH·MobaXterm의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — Ubuntu 위 Docker 설치와 web/DB container lifecycle·port 결과
- `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` — 새 VM host 준비 뒤 Docker/Compose 반복
- Docker 이론 PDF와 Linux 총정리 — guest OS와 container 실행 단위의 개념·복습 보조