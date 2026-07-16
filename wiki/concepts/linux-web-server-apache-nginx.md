---
title: Linux Apache/Nginx 웹서버
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux Apache/Nginx 웹서버

## 정의와 실제 첫 실습

Apache HTTP Server와 Nginx는 browser의 HTTP 요청을 받아 정적 file을 응답할 수 있는 web server다. 이 위키의 직접 host 실습은 [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27]]에 시작했다. 당시 Ubuntu guest에 Apache와 Nginx를 각각 package로 설치하고 service를 전환해 `/var/www/html/`의 page를 browser에 제공했다.

04-28의 web container와 04-30의 Nginx reverse proxy는 이 host 실습의 후속 활용이다. 같은 `Apache`·`Nginx` 이름이 등장해도 실행 위치와 책임을 합치면 안 된다.

## 왜 필요한가

Linux server 운영에서는 “web server package가 설치되어 있다”와 “사용자가 page를 받을 수 있다” 사이에 여러 조건이 있다.

1. package가 설치되어야 한다.
2. service가 시작되어 active 상태여야 한다.
3. HTTP/HTTPS port가 firewall에서 허용되어야 한다.
4. document root에 의도한 file이 있어야 한다.
5. VM network와 browser 요청 경로가 연결되어야 한다.
6. 실제 browser가 HTTP 응답을 받아야 한다.

따라서 접속 실패를 단순히 “Nginx 오류”나 “방화벽 오류”로 단정하지 않고 [[concepts/linux-process-service-port-firewall|process·service·port·firewall 진단 흐름]]으로 나눠 확인해야 한다.

## 2026-04-27 Apache host 실습

### 1. 설치·자동 시작·실행·상태

Apache 실습은 package index update→`apache2` 설치→boot 자동 시작 enable→service start→status 확인 순서였다. `systemctl status apache2`에서 `active (running)`을 확인한 뒤에야 service 실행 완료로 판정했다.

`enable`은 현재 process를 시작하는 명령이 아니라 다음 boot 때 자동 시작하도록 등록하는 설정이다. 현재 실행은 `start`, 현재 상태 검증은 `status`가 담당한다.

### 2. UFW와 SSH 연결 보호

UFW를 활성화할 때 원본에도 현재 SSH 연결이 끊길 수 있다는 경고가 나타났다. 그래서 다음 inbound port를 허용하고 상태를 다시 확인했다.

| port | 수업의 service | 확인 이유 |
|---:|---|---|
| 22 | SSH | MobaXterm 원격 관리 연결을 유지 |
| 80 | HTTP | Apache/Nginx의 기본 web 요청 |
| 443 | HTTPS | HTTPS inbound rule 준비 |

reboot 뒤 MobaXterm으로 다시 접속하고 Apache와 SSH service가 모두 active인지 확인했다. UFW 80만 열고 22를 빼면 web page보다 먼저 원격 관리 연결을 잃을 수 있다는 운영상 순서를 보여 준 실습이다. ^[raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md]

### 3. 기본 page와 document root 교체

guest IP로 Apache 기본 page를 먼저 확인했다. Windows에서 가져온 homepage ZIP을 user home에서 해제하고, Apache document root `/var/www/html/`의 기본 `index.html`을 `index.bak`으로 backup했다. 그 다음 해제한 homepage file을 document root에 복사하고 목록에서 새 `index.html`과 관련 artifact를 확인했다.

service를 stop했을 때 browser 접속이 실패하고, 다시 start했을 때 접속이 성공했으며, 마지막에는 기본 page가 아니라 교체한 homepage가 보이는지 확인했다.

### Apache 완료 조건

| 단계 | 완료 증거 |
|---|---|
| 설치됨 | `apache2` package 설치 종료 |
| 자동 시작 설정 | enable 등록 |
| 현재 실행 | status의 `active (running)` |
| port 허용 | UFW의 22·80·443 rule |
| file 교체 | `/var/www/html/`의 backup과 새 `index.html` |
| 사용자 결과 | browser의 교체 homepage 응답 |

## 2026-04-27 Nginx host 실습

Apache를 다음 실습을 위해 중지한 뒤 Nginx를 설치했다. Nginx service를 시작하고 status를 확인한 다음, GitHub sample repository를 clone했다. 실제 `index.html`이 있는 하위 directory로 이동해 file을 `/var/www/html/`에 복사하고 guest IP로 browser 결과를 확인했다.

Apache와 Nginx가 수업에서 같은 document root를 사용했어도 두 host service를 동시에 80번에 띄운 결과가 아니다. Apache를 중지한 뒤 Nginx로 전환했으므로, 같은 address와 document root를 어느 process가 제공하는지 service 상태로 구분해야 한다.

## 04-28·04-30의 후속 web server와 경계

### 04-28 container web server

[[summaries/2026-04-28-maven-spring-boot-docker-intro|04-28]]에는 host에 설치한 service가 아니라 `httpd`와 `nginx` image로 container를 실행했다. host port를 container 80에 publish하고 browser page를 확인한 뒤 stop/remove로 container 생명주기를 관찰했다.

- host Apache/Nginx: Ubuntu package와 systemd service
- container Apache/Nginx: Docker image에서 생성된 container process
- `systemctl`과 `docker container`는 서로 다른 실행 관리 계층

### 04-30 Nginx reverse proxy/load balancing

[[summaries/2026-04-30-dockerfile-spring-load-balancing|04-30]]에는 Nginx container가 정적 page만 직접 제공하는 데서 더 나아가 reverse proxy가 됐다. `proxy-net`의 Apache·Nginx backend 여섯 개를 upstream으로 묶고, browser path에 따라 요청을 전달했다. 외부에는 reverse proxy의 host 80만 공개했다.

이 페이지는 host Apache/Nginx의 설치·service·document root를 중심으로 설명한다. upstream·`proxy_pass`와 요청 분배의 상세 책임은 [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]에 위임한다. R07의 container proxy를 R04의 host service 성공으로 소급하지 않는다.

## 자주 헷갈리는 점과 선택 기준

- **install vs active:** package가 있어도 service가 stopped면 응답하지 않는다.
- **enable vs start:** enable은 boot 정책, start는 현재 실행이다.
- **active vs port 허용:** service가 running이어도 UFW가 막으면 외부에서 접근할 수 없다.
- **port 허용 vs browser 응답:** firewall rule만으로 document root와 network 경로가 자동 검증되지는 않는다.
- **file 존재 vs 교체 결과:** 새 file을 복사했으면 실제 document root 목록과 browser page를 모두 확인한다.
- **Apache vs Nginx 선택:** 이날은 두 제품의 성능 비교가 아니라 같은 host 정적 web server 역할을 순서대로 실습했다.
- **host vs container vs proxy:** 04-27 host service, 04-28 정적 web container, 04-30 reverse proxy container를 실행 주체로 구분한다.
- **Nginx vs Spring Boot:** Nginx는 정적 file 제공이나 앞단 전달을 맡을 수 있고, Spring Boot는 application logic을 실행한다.

## 선행·후속 연결과 범위 경계

- 선행: [[concepts/linux-package-archive|package·download·archive]]와 [[concepts/linux-users-permissions|권한]]을 이용해 homepage file을 준비하고 system path에 복사했다.
- 직접 Linux: R04의 host Apache/Nginx·UFW·browser 확인이 이 페이지의 핵심이다.
- 후속 Docker: R05의 container web server와 R07의 reverse proxy/load balancing은 별도 실행 단위다.
- 후속 AWS: EC2의 Nginx와 Security Group, ALB는 Linux 지식을 cloud resource에 적용한 것이며 04-27의 직접 구현이 아니다.

## 관련 페이지

- [[entities/linux|Linux]]
- [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/linux-package-archive|Linux 패키지·다운로드·압축]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` — Apache/Nginx host 설치·service·UFW·document root·browser 실습의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — host service와 구분되는 Apache/Nginx container 후속 실습
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` — host web server와 구분되는 Nginx reverse proxy/load balancing 후속 실습
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — host web server→Spring Boot→container proxy 연결 복습
