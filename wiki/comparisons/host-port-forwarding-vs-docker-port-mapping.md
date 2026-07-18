---
title: 호스트 포트 포워딩 vs Docker 포트 매핑
created: 2026-07-13
updated: 2026-07-18
type: comparison
tags: [linux, docker, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: stable
confidence: high
---

# 호스트 포트 포워딩 vs Docker 포트 매핑

## 비교 목적

04-28 Spring Boot host 실행은 **Windows host→VirtualBox guest→guest Linux process** 경로였고, Docker web server는 **Docker host→container process** 경로였다. 둘 다 `앞 포트→뒤 포트`처럼 보이지만 적용 계층과 점검 대상이 다르다.

## 한눈에 보기

| 비교 축 | VM/Linux host 포워딩·redirect | Docker 포트 매핑 |
|---|---|---|
| 수업의 입력 | browser의 Windows host port, VirtualBox NAT, guest Linux 80, Spring 9000 | Docker host port와 container service port |
| 설정 주체 | VirtualBox NAT + guest `iptables`·UFW | Docker Engine의 publish option 또는 Compose `ports` |
| 직접 대상 | guest OS에서 직접 실행한 process | 격리된 container 내부 process |
| 실제 예 | host 8100→guest 80→Spring 9000 | host 8888→Apache container 80 |
| 대표 확인 | NAT rule·iptables rule·UFW·JAR process·browser | container `Up`·published ports·내부 service·browser |

## 실제 선택 상황

### 상황 1: Spring Boot JAR를 Ubuntu guest에서 직접 실행

VirtualBox NAT와 guest Linux redirect를 사용했다. application의 실제 port 9000을 확인하고, Windows browser의 8100을 guest 80으로 전달한 뒤 guest `iptables`가 80을 9000으로 redirect했다. UFW 9000과 JAR process·browser 결과를 별도로 확인했다.

### 상황 2: Apache·Nginx를 container로 실행

Docker port mapping을 사용했다. host 8888을 Apache container 80에 publish했고, 여러 web container는 내부 80을 공유해도 host port는 서로 다르게 배정했다. container 상태와 browser page가 모두 확인돼야 했다.

### 상황 3: Docker 안의 Spring Boot와 MySQL

Spring container의 host 9000→container 9000 publish는 browser 진입 경로이고, Spring→MySQL은 같은 Docker network의 service/container 이름 기반 통신이다. port mapping과 container network를 같은 설정으로 보지 않는다.

## 함께 쓰는 관계와 전체 경로

수업 환경처럼 Docker Engine 자체가 Ubuntu VM 안에서 실행되면 두 계층이 함께 존재할 수 있다.

`Windows browser → VirtualBox bridge/NAT → Ubuntu guest(Docker host) → Docker published port → container service`

어느 한 계층이 막히면 뒤쪽 service가 정상이어도 외부에서 접근할 수 없다. reverse proxy를 추가하면 Nginx `listen`·`proxy_pass`와 backend network가 그 뒤에 별도 계층으로 붙는다.

## 실제 오류·완료 조건

| 단계 | 확인 | 아직 보장하지 않는 것 |
|---|---|---|
| process/container 실행 | JAR process 또는 container `Up` | port 경로·readiness |
| guest redirect | 80→9000 rule 조회 | Windows host→guest NAT |
| UFW | 필요한 guest port 허용 | application 응답 |
| Docker publish | host→container port 표시 | container 내부 service 정상 |
| browser 응답 | 최종 page/API 응답 | DB 연결·후속 proxy 분배 |

## 흔한 오해와 확인되지 않은 범위

- `-p 8888:80`의 왼쪽은 Docker host, 오른쪽은 container 내부 port다.
- VirtualBox NAT, guest `iptables`, guest UFW, Docker publish는 모두 다른 설정이다.
- Docker network는 container 간 통신이고 port publish는 host 진입이다.
- UFW와 Docker publish의 일반적인 상호작용은 환경별 rule 구성에 따라 달라질 수 있다. 수업에서 확인한 특정 경로를 모든 host의 절대 규칙으로 일반화하지 않는다.
- AWS Security Group·ALB·Target Group은 후속 cloud 경계다. Linux 직접 실습의 NAT/port 결과로 소급하지 않는다.

## 관련 페이지

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven·Spring Boot·Docker 입문]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — VirtualBox NAT→guest iptables→Spring 9000과 첫 Docker port mapping의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` — web/Redmine container publish와 container network 경계
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` — Spring container·reverse proxy의 후속 Docker 계층
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — VM/host/container port의 복습 경계