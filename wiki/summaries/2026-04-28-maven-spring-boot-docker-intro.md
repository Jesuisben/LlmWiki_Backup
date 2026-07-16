---
title: 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [linux, docker, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
status: growing
confidence: high
---

# 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문

## 한 줄 요약

GitHub의 Spring Boot project를 Linux에서 Maven JAR로 package해 host process로 실행한 뒤, VirtualBox NAT·guest iptables·UFW의 port 계층을 연결하고 Docker image/container·web/DB container·WordPress–MySQL network까지 확장했다.

## 왜 이 흐름으로 배웠는가

04-27에는 Linux에서 단일 Java class와 host Apache/Nginx를 실행했다. 그러나 실제 Spring Boot project는 source 전체를 build artifact로 만들고, application port와 외부 접근 경로를 맞춰야 한다. 먼저 **host에서 수동 build·run·port 연결**을 완성한 뒤, 같은 실행 환경을 image로 묶어 여러 container를 반복 생성하는 Docker로 넘어갔다.

따라서 이날의 핵심 전환은 `source → Maven JAR → Linux process`와 `image → container` 두 실행 단위를 연속해서 비교한 것이다. 이 수동 과정은 후속 AWS EC2와 CI/CD에서 재사용되지만, cloud resource나 workflow 자동화는 이날 직접 구현하지 않았다.

## 교시별 학습 전개

### 1교시: GitHub clone에서 Spring Boot JAR 실행까지

먼저 80번 port를 사용할 수 있도록 전날의 Nginx와 Apache service를 중지하고 boot 자동 시작도 해제했다. GitHub의 Spring Boot sample project를 clone한 뒤 `application.properties`에서 `server.port=9000`을 확인했다.

외부 browser 요청이 application까지 가는 경로는 세 층이었다.

| 층 | 이날 설정한 전달 |
|---|---|
| Windows host → VirtualBox guest | host 8100 → guest 80 (VirtualBox NAT port forwarding) |
| Ubuntu guest 안 | guest 80 → guest 9000 (`iptables` REDIRECT) |
| Spring Boot process | guest 9000에서 요청 수신 |

guest UFW에는 9000/tcp를 허용했다. 이 구조에서 VirtualBox NAT와 Linux `iptables`는 같은 설정이 아니다. 하나는 host와 guest 경계, 다른 하나는 guest 내부 port redirect다.

이어 Maven을 설치해 version을 확인하고, 반드시 `pom.xml`이 있는 project root에서 `mvn clean package -DskipTests`를 실행했다. 결과 JAR이 `target/`에 생성되었는지 확인한 뒤 `java -jar`로 Spring Boot application을 시작하고 browser로 접속했다.

`-DskipTests`는 test를 성공시킨 것이 아니라 실행을 건너뛰고 package한 option이다. CI/CD는 이 clone·build·run 과정을 자동화하는 후속 개념으로만 소개되었다.

### 2교시: Docker image와 container, Ubuntu 설치

Spring Boot의 code·dependency·JDK·설정·환경을 server마다 따로 준비하는 문제에서 Docker 필요성을 설명했다.

- image는 실행 환경을 만들기 위한 template/설계도다.
- container는 image를 바탕으로 실제 memory에서 실행되는 instance다.
- 하나의 image로 여러 container를 만들 수 있다.
- Docker Hub는 image를 push/pull하는 registry이며 GitHub source repository와 역할이 다르다.

Ubuntu에 Docker를 설치할 때 Windows에서 가져온 setup script를 root 영역에 복사했다. CRLF 문제를 피하려고 `dos2unix`를 적용하고 실행 권한을 준 뒤 script를 실행했다. Docker command help와 `systemctl status docker`의 active 상태로 설치·service를 확인했다.

일반 사용자에게 `docker` group을 추가하고 `groups`로 membership을 확인했다. `docker version`에서 permission error가 나면 기존 login session에 새 group 정보가 반영되지 않은 것이므로 logout/login 뒤 client와 server 정보를 다시 확인했다.

### 3교시: web container 생명주기

Apache `httpd` image로 container를 처음 실행했다. local image가 없자 Docker가 registry에서 image를 pull하고, host 8888을 container 80에 publish했다.

1. `docker container run`으로 이름·background 실행·port mapping·image를 지정했다.
2. 실행 중 목록에서 status `Up`, image, container name, `host:container` port를 확인했다.
3. VM IP와 host port로 browser의 Apache page를 확인했다.
4. `stop` 후 status가 `Exited`로 바뀌는지 확인했다.
5. `rm`으로 container를 삭제하고 전체 목록에서 사라지는지 확인했다.

같은 순서를 Nginx image에도 반복했다. image가 template이고 container가 삭제 가능한 실행 instance라는 설명이 실제 lifecycle과 연결되었다.

### 4교시: 여러 web/DB container와 내부 수정

Apache 2개, Nginx 2개, MySQL 2개를 실행했다. web container의 **host port는 서로 달라야** 했지만 각 container 내부의 HTTP port 80은 같아도 되었다. MySQL은 environment variable로 초기 설정을 전달하고 interactive terminal option을 포함해 실행했다. 실제 password 값은 Summary에서 일반화한다.

실행 중 container 수와 browser page를 확인한 뒤 `docker exec -it ... /bin/bash`로 Apache container 안에서 shell을 실행했다. package source URL 문제를 `sed`로 조정하고 Vim을 설치해 container 내부 document root의 `index.html`을 직접 수정했다.

“container 안으로 들어간다”는 표현은 별도 VM에 login한다는 뜻이 아니라, 실행 중 container에 새로운 shell process를 실행해 그 filesystem과 process namespace에서 작업한다는 뜻이다.

### 5교시: `docker cp`, MySQL, Nginx와 일괄 정리

host의 `index.html`과 image file을 `docker cp`로 Apache container의 document root에 복사하고 browser에서 바뀐 page를 확인했다. MySQL container는 log에서 `ready for connections`를 확인한 뒤 shell과 MySQL client prompt에 들어갔다가 순서대로 나왔다.

Nginx container도 `exec`로 내부 page를 수정하고, 다른 container에는 host file을 `docker cp`로 넣어 결과를 확인했다. 마지막에는 Apache·Nginx·MySQL container 6개를 한 번에 stop하고 remove한 뒤 목록이 비었는지 확인했다.

### 6교시: WordPress–MySQL `network01`

이날 마지막 핵심 실습은 이후 [[concepts/docker-network-volume|Docker 네트워크와 볼륨]] 학습의 **직접 선행 근거**다.

1. 사용자 정의 bridge network `network01`을 만들고 목록에서 확인했다.
2. MySQL container를 같은 network에 연결하고 database와 root credential을 environment variable로 주어 실행했다.
3. WordPress container도 `network01`에 연결하고 DB host를 MySQL container name으로 지정해 실행했다.
4. container 목록과 `docker network inspect`에서 두 container가 `Up` 상태이고 같은 network에 속했는지 확인했다.
5. browser에서 WordPress 설치·login 화면을 확인했다.
6. MySQL prompt에서 database와 sample table/data를 만들고 commit했다.
7. WordPress container에 MySQL client를 설치해 **host port가 아니라 container name**으로 MySQL에 접속하고 같은 table data를 조회했다.
8. container·image·network를 순서대로 정리했다.

registry pull rate limit 때문에 login이 필요했던 오류와, MySQL client의 password option 사용법 오류, container 사이 TLS certificate 불일치도 기록되었다. 이 Summary에서는 실제 one-time code·credential·email을 재노출하지 않는다. `--skip-ssl`은 수업 환경의 우회로 기록된 것이며 일반적인 보안 권장 설정으로 확대하지 않는다. ^[raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md]

### 7~8교시: 반복 실습과 빈 마지막 교시

7교시는 Librarian 후반, Docker setup, WordPress–MySQL 구간을 다시 실습하는 시간으로 기록되어 있다. 8교시는 날짜 노트에 구체 내용이 없다. 앞 교시의 결과를 8교시에 수행한 것으로 소급하지 않는다.

## 대표 실습 A: source에서 browser 응답까지

**입력**은 GitHub의 Spring Boot source, `pom.xml`, application port 9000, VirtualBox NAT와 guest firewall/redirect 설정이었다. **처리**는 clone → port 확인 → Maven package → `target` JAR 확인 → `java -jar` 실행 → host 8100/guest 80/guest 9000 전달이었다. **결과**로 IDE가 없는 Linux VM에서 Spring Boot application이 실행되고 browser 요청이 application에 도달했다.

## 대표 실습 B: WordPress가 MySQL container를 이름으로 찾기

**입력**은 사용자 정의 `network01`, MySQL·WordPress image, 일반화한 DB environment 설정이었다. **처리**는 두 container를 같은 network에 붙이고 WordPress의 DB host를 MySQL container name으로 지정한 뒤 network membership과 DB data를 확인하는 과정이었다. **결과**로 WordPress container에서 `mysql01` 같은 service 이름을 통해 DB에 접속해 sample rows를 조회했다. 이 경험이 04-29의 다중 container network와 05-01 Compose service 연결로 이어진다.

## 대표 artifact와 확인 결과

- clone한 Spring Boot project, `pom.xml`, `application.properties`
- `target/`의 executable JAR과 `java -jar` process
- VirtualBox NAT host 8100→guest 80, guest iptables 80→9000, UFW 9000 rule
- Docker setup script, `dos2unix`, Docker service와 `docker` group
- httpd/Nginx/MySQL image와 web/DB container lifecycle
- `docker exec`, `docker cp`, container document root 변경
- `network01`, MySQL·WordPress container와 network inspect 결과
- WordPress container에서 MySQL sample data 조회 결과

## 헷갈리기 쉬운 지점

1. **Maven package와 JAR 실행은 다르다.** Maven은 artifact를 만들고 `java -jar`는 그 artifact를 process로 실행한다.
2. **VirtualBox NAT, guest iptables, UFW, Spring port는 다른 계층이다.** 하나를 열었다고 전체 경로가 자동 완성되지 않는다.
3. **`-DskipTests`는 test 통과가 아니다.** test 실행을 생략한 package 결과다.
4. **image와 container는 파일과 process처럼 생명주기가 다르다.** container를 지워도 image는 별도로 남을 수 있다.
5. **host port와 container port를 혼동하면 여러 web container를 띄울 수 없다.** host 쪽은 충돌을 피하고 container 내부 port는 각 namespace에서 같을 수 있다.
6. **Docker group 추가와 현재 session 반영은 별개다.** membership을 바꾼 뒤 재login이 필요할 수 있다.
7. **사용자 정의 network는 browser용 port mapping과 역할이 다르다.** 같은 network의 container가 이름으로 서로 찾는 내부 통신 경로다.
8. **Docker network와 AWS VPC는 같은 개념이 아니다.** 둘 다 network라는 이름을 쓰지만 AWS VPC/Subnet/Security Group은 다음 과목의 cloud resource다.

## 이전·다음 수업 연결

- 이전: [[summaries/2026-04-27-linux-archive-java-alias|04-27]]의 Java·Git·host web server를 실제 Spring Boot JAR 실행으로 확장했다.
- 다음: [[summaries/2026-04-29-docker-network-volume-image|04-29]]에는 이날의 `network01` 경험을 MariaDB–Redmine 연결, `exec`/`cp`, bind mount·volume, image commit/registry로 확장한다.
- 후속 활용: EC2에서는 Linux/JAR/Nginx를 cloud VM에 적용하고, CI/CD에서는 GitHub push→Maven build→Docker image→EC2 갱신을 자동화한다. 이날의 결과는 로컬 VirtualBox VM과 수동 Docker 실습에 한정한다.

## 관련 페이지

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[entities/maven|Maven]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]
- [[comparisons/virtual-machine-vs-docker-container|가상 머신(VM) vs Docker 컨테이너]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — 실제 교시·Spring Boot JAR·port 계층·Docker 설치·container·network 실습의 최우선 근거
