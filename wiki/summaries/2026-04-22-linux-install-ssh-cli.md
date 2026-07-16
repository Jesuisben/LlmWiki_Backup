---
title: 2026-04-22 Linux 설치, SSH 접속, 기본 CLI
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md
status: growing
confidence: high
---

# 2026-04-22 Linux 설치, SSH 접속, 기본 CLI

## 한 줄 요약

VirtualBox에 Ubuntu Server VM을 만들고, 브리지 네트워크와 OpenSSH 서비스를 준비해 MobaXterm으로 접속한 뒤 prompt·최상위 디렉터리·절대/상대 경로까지 확인한 Linux 첫날이다.

## 왜 이 흐름으로 배웠는가

앞선 FrontEnd_BackEnd 수업에서는 IntelliJ와 브라우저에서 Spring Boot·React 기능을 만들었다. 이제 그 결과물을 IDE 밖에서 실행하려면 먼저 **서버 역할을 할 별도 운영체제**, 그 서버에 원격 접속하는 방법, 그리고 GUI 없이 위치를 표현하는 경로 규칙이 필요하다. 그래서 `VM 준비 → 네트워크 연결 → SSH 서비스 → 원격 접속 → CLI와 경로` 순서로 기반을 만들었다.

이날의 VirtualBox Ubuntu는 Linux 명령을 연습하는 로컬 guest OS다. 이후 [[entities/amazon-ec2|Amazon EC2]]에서도 Ubuntu와 SSH를 다시 사용하지만, EC2의 Public IP·Key Pair·Security Group은 AWS 과목에서 추가되는 후속 책임이다.

## 교시별 학습 전개

### 1~3교시: Linux 전환 전 준비

오전 1~3교시는 날짜 노트에 구체 학습 내용이 기록되어 있지 않다. 따라서 이후 교시의 설치 내용을 오전에 수행한 것으로 소급하지 않는다.

### 4교시: 설치 도구와 VM 역할 구분

- Ubuntu ISO는 VM에 설치할 운영체제 이미지다.
- VirtualBox는 VM을 만들고 실행하는 가상화 프로그램이다.
- MobaXterm은 실행 중인 VM의 SSH 서버에 접속하는 클라이언트다.
- VirtualBox의 기본 VM 저장 위치를 정한 뒤 첫 Ubuntu Server VM에 이름·계정·메모리·CPU·가상 디스크를 설정하고 설치했다.

세 도구를 한 덩어리로 외우는 것이 아니라 `VirtualBox가 guest OS를 실행하고, Ubuntu의 SSH service가 접속을 받고, MobaXterm이 접속을 요청한다`는 층위로 구분하는 것이 핵심이다.

### 5교시: OpenSSH 설치·서비스 확인·종료

VM console에서 일반 사용자로 로그인한 뒤 관리자 권한이 필요한 작업에 `sudo`를 붙였다.

1. `apt`로 `openssh-server` 패키지를 설치했다.
2. `systemctl start ssh`로 SSH service를 시작했다.
3. `systemctl status ssh`에서 `active (running)`을 확인했다.
4. `poweroff`로 VM을 안전하게 종료했다.

여기서 패키지 설치와 서비스 실행은 다른 단계다. OpenSSH가 설치되어 있어도 service가 실행 중이지 않으면 SSH 접속을 받을 수 없다. `systemctl start`가 아무 메시지를 내지 않은 것은 실패 결과가 아니라, 뒤의 `status`로 성공 여부를 확인해야 하는 상황이었다. ^[raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md]

### 5~6교시: 브리지 네트워크와 MobaXterm SSH

VM을 종료한 상태에서 VirtualBox network adapter를 NAT에서 **Bridged Adapter**로 바꾸고 재부팅했다. guest에서 `ip addr`를 실행해 loopback(`lo`)과 실제 adapter(`enp0s3`), IPv4의 `inet` 값을 구분했다.

확인한 guest IP를 MobaXterm의 `Remote host`에 넣고, Ubuntu 사용자명과 기본 SSH port `22`로 session을 만들었다. 접속 후 `$` prompt가 보이는 것으로 일반 사용자 session임을 확인했다. 두 번째 VM도 같은 절차로 설치해, **VM이 켜져 있고 SSH service·IP·방화벽이 맞아야 client session이 연결된다**는 조건을 반복했다. 접속이 막힐 때는 guest UFW에서 22번 port 허용 여부도 점검했다.

### 6교시 후반: `apt`, `sudo`, `systemctl` 읽기

- `apt`는 Ubuntu/Debian 계열의 package 관리 도구다. Node.js의 `npm`과 비슷한 “설치 도구”라는 첫 비유를 사용했지만, JavaScript package가 아니라 OS package를 관리한다.
- `sudo`는 뒤의 명령을 관리자 권한으로 실행한다.
- `systemctl`은 SSH처럼 background에서 동작하는 service의 시작·중지·상태를 관리한다.
- `-y`는 설치 중 확인 질문에 자동으로 동의하는 option이다.

### 7~8교시: prompt, 파일 시스템, 절대·상대 경로

파일은 데이터를 저장하는 기본 단위이고, directory는 파일과 다른 directory를 담아 논리적으로 구성한다. prompt의 `사용자@호스트:현재위치$` 구조를 읽고 `pwd` 결과가 사용자의 home directory 경로임을 확인했다.

Linux 경로의 출발점은 최상위 `/`다.

| 구분 | 판단 기준 | 이날 사용한 관점 |
|---|---|---|
| 절대 경로 | `/`부터 전체 위치를 표현 | 현재 위치가 바뀌어도 같은 대상을 가리켜 server 관리·script에 명확함 |
| 상대 경로 | 현재 작업 directory를 기준으로 표현 | `.`·`..`·`./`·`../`·`~/`를 이용하며 현재 위치에 따라 결과가 달라짐 |

경로 문제를 풀면서 `./하위경로`와 바로 `하위경로`가 같은 현재 위치 기준 결과를 낼 수 있음을 확인했다.

## 대표 실습: VM 생성에서 원격 CLI까지

**입력**은 Ubuntu ISO와 VM 설정, guest 계정, OpenSSH package, bridge adapter, guest IP, SSH session 정보였다. **처리**는 VirtualBox가 Ubuntu guest를 부팅하고, `systemctl`이 SSH service를 실행하며, MobaXterm이 22번 port로 guest IP에 접속하는 과정이다. **결과**로 MobaXterm에서 일반 사용자 `$` prompt와 `pwd`의 home 경로를 확인하고 Linux 명령을 입력할 수 있게 되었다.

이 실습은 “MobaXterm을 설치했으니 Linux가 생겼다”가 아니라, 서버와 client 사이의 조건을 순서대로 맞추는 첫 연결 진단 실습이다.

## 대표 artifact와 확인 결과

- VirtualBox Ubuntu Server VM 2대
- VM network의 Bridged Adapter 설정
- OpenSSH server package와 `ssh` service
- `systemctl status ssh`의 `active (running)` 상태
- `ip addr`에서 확인한 guest IPv4
- MobaXterm SSH session과 일반 사용자 `$` prompt
- `/`, home directory, 절대·상대 경로 문제 풀이

## 헷갈리기 쉬운 지점

1. **VirtualBox와 MobaXterm은 같은 역할이 아니다.** VirtualBox는 VM을 실행하고 MobaXterm은 SSH client다.
2. **설치와 실행은 다르다.** `apt install openssh-server` 뒤에 `systemctl start/status ssh`가 필요한 이유다.
3. **`$`와 `#`는 단순 장식이 아니다.** 일반 사용자와 관리자 prompt를 구분하며, 관리자 작업은 `sudo` 또는 root session과 연결된다.
4. **브리지와 NAT를 같은 포트 전달로 보면 안 된다.** 이날은 VM을 LAN에 연결하는 bridge를 사용했고, 04-28의 VirtualBox NAT host-port 전달은 별도 계층이다.
5. **SSH 접속 실패 원인은 하나가 아니다.** VM 전원, guest IP, SSH service, port 22, UFW, 계정 정보를 차례로 확인해야 한다.
6. **절대 경로와 상대 경로의 차이는 길이가 아니라 기준점이다.** `/`에서 시작하는지, 현재 directory에서 시작하는지가 판단 기준이다.

## 이전·다음 수업 연결

- 이전: [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]에서 로컬 애플리케이션을 완성한 뒤 운영 환경 학습으로 전환했다.
- 다음: [[summaries/2026-04-23-linux-files-vi|04-23]]에는 이날 배운 `/`, home, 절대·상대 경로를 실제 방송사 directory tree와 파일 생성·복사·이동·편집에 적용한다.
- 후속 활용: Docker는 이 Ubuntu host 위에서 container를 실행하고, AWS EC2는 cloud VM에서 같은 Linux·SSH 기본기를 재사용한다. CI/CD는 이 접속·명령 과정을 자동화하지만 이날 직접 구현한 내용은 아니다.

## 관련 페이지

- [[concepts/linux-cli-files|Linux CLI와 파일 시스템]]
- [[entities/linux|Linux]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]
- [[concepts/linux-users-permissions|Linux 사용자·그룹·권한]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` — 실제 수업일·교시·설치·SSH·경로 흐름의 최우선 근거