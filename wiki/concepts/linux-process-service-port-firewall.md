---
title: Linux process·service·port·firewall 진단
created: 2026-07-16
updated: 2026-07-16
type: concept
tags: [linux, backend, debugging]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
  - raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux process·service·port·firewall 진단

## 정의

Linux server 진단은 “설치했는데 왜 접속이 안 되지?”를 하나의 문제로 보지 않고 **process → service → listening port → firewall → NAT/redirect → client 응답** 순서로 나누어 실패 계층을 찾는 작업이다.

이 축은 04-22 SSH, 04-24 script 실행과 process 기초, 04-27 Apache/Nginx·UFW, 04-28 Spring Boot 9000·iptables에서 반복됐다. web server와 Spring Boot 페이지에 나누어 적을 수는 있지만, 서로 다른 server에서 같은 진단 순서를 다시 찾기 어렵기 때문에 독립 Concept로 보존한다.

## 왜 필요한가

MobaXterm 연결 실패와 browser page 실패는 겉으로는 모두 “접속이 안 됨”이다. 그러나 원인은 다음처럼 다를 수 있다.

- package만 설치되고 service가 시작되지 않음
- process가 종료됐거나 실행 권한이 없음
- service는 active지만 원하는 port에서 요청을 받지 않음
- UFW가 inbound port를 허용하지 않음
- VirtualBox NAT나 guest `iptables` redirect가 다른 destination을 가리킴
- server는 정상인데 client가 잘못된 IP·port로 요청함

원인을 구분하지 않고 package 재설치나 전체 firewall 해제를 반복하면 문제를 가릴 뿐이다. 수업에서 사용한 artifact를 계층별로 읽으면 확인 범위를 좁힐 수 있다.

## 수업에서 어떻게 확장됐는가

### 2026-04-22 — SSH service와 22번 port

[[summaries/2026-04-22-linux-install-ssh-cli|04-22]]에는 OpenSSH package 설치 뒤 `systemctl start ssh`를 실행했다. start 명령에 별도 출력이 없었기 때문에 `systemctl status ssh`의 `active (running)`으로 성공을 확인했다.

그 다음 bridge network의 guest IP와 SSH 기본 port 22를 MobaXterm session에 입력했다. 접속이 되지 않을 때는 VM 전원, guest IP, SSH service, UFW 22, account 정보를 함께 확인했다. ^[raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md]

### 2026-04-24 — 실행 가능한 file과 process 기초

[[summaries/2026-04-24-linux-users-permissions|04-24]]에는 여러 명령을 적은 `print_tree.sh`를 만들었다. 처음에는 실행 권한이 없어 현재 directory의 script 실행이 `Permission denied`로 실패했고, `chmod` 뒤에는 script 안의 명령이 순서대로 실행됐다.

날짜 원본의 heading에는 `ps`, `kill`이 있지만 보존된 실제 단계는 script 작성·권한 오류·실행 성공까지다. 따라서 이날 특정 PID를 찾아 종료한 성공 결과는 만들지 않는다. R11 총정리에서 `ps`·`grep`·`kill`은 process 상태 확인과 종료 도구로 연결되며, 종료 전 실행 사용자와 대상 process를 먼저 확인해야 한다고 정리됐다.

### 2026-04-27 — Apache/Nginx service와 UFW

[[summaries/2026-04-27-linux-archive-java-alias|04-27]]에는 Apache를 install→enable→start→status 순서로 준비했다. UFW를 활성화하면서 SSH 22, HTTP 80, HTTPS 443을 허용하고, reboot 뒤 SSH와 Apache가 active인지 다시 확인했다.

Apache document root의 page를 교체한 뒤 service stop 시 browser 실패, start 시 browser 성공을 확인했다. 이어 Apache를 중지하고 Nginx를 시작해 같은 host의 80번 web server 역할을 전환했다. 이 실습은 package 설치, service active, firewall, file, browser 응답이 서로 다른 완료 조건임을 보여 준다. ^[raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md]

### 2026-04-28 — Spring Boot process와 다층 port 경로

[[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]]에는 Spring Boot JAR를 `java -jar`로 host process로 실행했다. application은 guest 9000에서 요청을 받았고 browser 경로는 다음 세 계층으로 구성됐다.

| 계층 | 전달·허용 | 책임 |
|---|---|---|
| Windows host → guest | VirtualBox NAT: host 8100 → guest 80 | host/guest 경계의 port forwarding |
| guest 내부 | `iptables` REDIRECT: 80 → 9000 | guest 안에서 destination port 변경 |
| guest firewall·application | UFW 9000 허용 + Spring 9000 | 통행 허용과 실제 요청 수신 |

이 중 하나가 맞아도 전체 browser 응답이 자동으로 증명되지는 않는다. Maven package와 JAR 생성도 process 실행보다 앞선 별도 단계다.

## 핵심 개념을 분리해서 읽기

| 개념 | 이 수업에서의 의미 | 대표 확인 대상 |
|---|---|---|
| process | memory에서 실제 실행 중인 program instance | script, `java -jar`, Apache/Nginx 실행 단위 |
| service | systemd가 background program을 unit으로 관리하는 방식 | SSH·Apache·Nginx·Docker의 start/stop/status/enable |
| listening port | process가 network 요청을 기다리는 접점 | 22·80·443·9000 |
| firewall rule | port로 들어오는 traffic의 허용·차단 정책 | UFW status와 allow rule |
| NAT/redirect | 다른 network 계층이나 port로 traffic 전달 | VirtualBox NAT, guest `iptables` REDIRECT |
| client response | 전체 경로를 지난 최종 사용자 관찰 | MobaXterm prompt, browser page |

모든 service는 결국 process로 실행되지만, 모든 임시 process가 systemd service인 것은 아니다. 04-28의 `java -jar`는 수업에서 host process로 직접 실행했으며 별도 systemd unit을 만든 기록은 없다.

## 진단 순서

### 1. 실행할 artifact와 권한 확인

- script나 JAR가 실제 위치에 있는가
- 현재 사용자가 file을 읽고 실행할 권한이 있는가
- Maven package처럼 선행 artifact 생성 단계가 끝났는가

04-24의 script `Permission denied`는 network 문제가 아니었고, 04-28의 JAR 부재는 firewall을 열어도 해결되지 않는다.

### 2. process 또는 service 상태 확인

- 임시 program이면 실행이 시작됐는가
- systemd service면 start 뒤 status가 active인가
- enable과 start를 혼동하지 않았는가
- 같은 port를 사용할 기존 Apache/Nginx가 남아 있지 않은가

04-28에는 Spring Boot 실행 전에 host 80을 사용할 수 있는 Nginx·Apache service를 중지하고 자동 시작도 해제했다.

### 3. listening port와 application 설정 확인

- SSH 22, web server 80, Spring 9000처럼 기대 port가 맞는가
- 설정 file의 port와 실제 실행 process의 port를 같은 것으로 단정하지 않았는가
- 하나의 host port를 여러 process가 동시에 점유하려 하지 않는가

수업 원본에는 설정과 status·browser 결과가 중심이며, 모든 날짜에서 별도의 listening socket 명령 결과가 보존된 것은 아니다. 그러므로 “설정에 9000이 있다”를 독립 listening 검증 결과로 바꾸지 않는다.

### 4. firewall rule 확인

- UFW가 active인가
- 필요한 inbound port가 허용됐는가
- 원격 작업 중 UFW를 켤 때 SSH 22를 먼저 보호했는가

firewall allow는 server process를 시작하지 않는다. 반대로 service active는 firewall 통과를 보장하지 않는다.

### 5. NAT·redirect·port mapping 계층 확인

- 04-22 bridge처럼 guest가 별도 LAN IP를 받는가
- 04-28 VirtualBox NAT forwarding처럼 host port가 guest port로 전달되는가
- guest `iptables`가 80을 Spring 9000으로 redirect하는가
- Docker를 사용하는 후속 실습이라면 host:container port publishing이 별도로 있는가

VirtualBox NAT, Linux `iptables`, Docker `-p`는 모두 port가 등장하지만 적용 경계가 다르다. 상세 비교는 [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]에 연결한다.

### 6. client에서 최종 응답 확인

- SSH: MobaXterm에서 guest prompt가 열리는가
- host web server: guest IP에서 기본 page와 교체 homepage가 보이는가
- Spring Boot: host browser 요청이 8100→80→9000을 지나 application page를 받는가

client 결과는 전체 경로의 마지막 검증이다. 중간 status 하나가 성공했다고 이 단계를 생략하지 않는다.

## 완료 조건 행렬

| 단계 | 성공 예 | 다음 단계와 분리해야 하는 이유 |
|---|---|---|
| 설치 | OpenSSH·Apache·Nginx·Maven package 설치 | 실행되지 않을 수 있음 |
| build/artifact | `target` JAR 존재 | process가 아직 없음 |
| process/service | `active (running)` 또는 application 시작 | 외부 traffic이 차단될 수 있음 |
| port 설정/경로 | 22·80·9000과 redirect rule | 실제 listening·응답은 별도 |
| firewall | UFW allow rule | destination process를 만들지 않음 |
| browser/SSH 응답 | page 또는 prompt 확인 | 이때 전체 사용자 경로가 닫힘 |

## 경계: Docker와 AWS에서는 무엇이 추가되는가

### Docker

04-28 이후에는 container process와 host:container port publishing, 사용자 정의 network가 추가된다. host Apache/Nginx의 systemd 상태와 container의 Docker 상태를 같은 명령으로 관리하지 않는다. `container Up`도 application log와 browser 응답을 자동 보장하지 않는다.

### AWS

EC2에서도 Linux process·service·UFW를 사용할 수 있지만, VPC·Subnet·route·Public IP·Security Group 계층이 추가된다. Security Group은 Linux UFW와 같은 rule file이 아니라 AWS resource다. 이 페이지는 Linux 직접 수업의 진단 축을 설명하며 AWS cloud network 성공 결과를 소급하지 않는다.

## 자주 헷갈리는 점

- **install = running이 아니다.** package 뒤 process/service 상태를 확인한다.
- **enable = start가 아니다.** boot 자동 시작과 현재 실행을 분리한다.
- **active = reachable이 아니다.** port·firewall·NAT·client 경로가 남아 있다.
- **port open = application response가 아니다.** 요청을 받을 process와 정상 application 처리가 필요하다.
- **process = service가 아니다.** 직접 실행한 JAR process와 systemd service를 구분한다.
- **bridge = NAT forwarding이 아니다.** guest가 별도 IP를 받는 방식과 host port 전달 방식의 차이다.
- **UFW = `iptables` redirect가 아니다.** 허용/차단 정책과 destination 변경 규칙을 구분한다.
- **Linux firewall = AWS Security Group이 아니다.** OS 내부와 cloud network resource의 계층이 다르다.

## 관련 페이지

- [[entities/linux|Linux]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` — OpenSSH service·22번·bridge·MobaXterm 연결
- `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md` — script 실행 권한 오류와 process 기초의 직접 범위
- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` — Apache/Nginx service·UFW 22/80/443·document root·browser 결과
- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — Spring Boot JAR process·9000·VirtualBox NAT·iptables·UFW·browser 경로
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — `ps`·`grep`·`kill`과 process/service/port 전체 복습 연결
