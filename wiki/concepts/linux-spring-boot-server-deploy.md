---
title: Linux에서 Spring Boot 서버 실행
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [linux, spring-boot, backend]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux에서 Spring Boot 서버 실행

## 정의와 수업에서의 등장

Linux에서 Spring Boot 서버를 실행한다는 것은 IDE의 Run 버튼 대신 **source를 build artifact로 만들고, 그 JAR를 Linux process로 띄운 뒤, 외부 요청이 application port까지 도달하는지 확인하는 것**이다.

[[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]] 수업은 전날의 단일 Java class와 host Apache/Nginx에서 한 단계 확장됐다. GitHub의 Spring Boot project를 guest VM에 준비하고, application port를 확인한 뒤 Maven package→`target` JAR→`java -jar`→browser 응답 순서로 IDE 밖 실행을 검증했다. ^[raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md]

## 왜 필요한가

개발 PC에서 application이 실행된다는 사실만으로 server 배포가 끝나지 않는다. Linux에서는 다음 책임을 각각 확인해야 한다.

- source와 `pom.xml`이 있는 project가 준비됐는가
- Maven이 package를 완료해 실행 가능한 JAR를 만들었는가
- Java가 그 JAR를 process로 실행했는가
- Spring Boot가 의도한 port에서 요청을 받고 있는가
- VM과 guest firewall·redirect를 지난 browser 요청이 실제 응답을 받는가

이 수동 흐름을 이해해야 후속 [[entities/amazon-ec2|Amazon EC2]] 배포나 [[concepts/ci-cd-automation|CI/CD 자동화]]에서도 어느 단계가 실패했는지 구분할 수 있다. 다만 EC2 resource와 GitHub Actions workflow는 각각 후속 과목의 직접 구현이며, 04-28 Linux 실습의 결과로 소급하지 않는다.

## 2026-04-28 host JAR 실행 흐름

### 1. 기존 80번 service와 project 준비

전날 설치한 Nginx와 Apache가 80번 port를 점유할 수 있어 두 service를 중지하고 boot 자동 시작도 해제했다. 그 다음 Spring Boot sample project를 clone하고 `application.properties`에서 `server.port=9000`을 확인했다.

여기서 clone 성공은 source 준비 완료일 뿐 build 성공이 아니다. 또한 설정 파일에 9000이 적혀 있다는 사실은 process가 이미 9000에서 실행 중이라는 뜻이 아니다.

### 2. 외부 요청 경로 준비

수업의 browser 요청은 세 계층을 통과했다.

| 계층 | 설정·artifact | 책임 |
|---|---|---|
| Windows host → VirtualBox guest | NAT port forwarding: host 8100 → guest 80 | host browser 요청을 guest 진입 port로 전달 |
| Ubuntu guest 내부 | `iptables` REDIRECT: guest 80 → guest 9000 | guest 안에서 HTTP 진입을 Spring port로 전환 |
| Spring Boot process | `server.port=9000` | application이 요청을 수신 |

guest UFW에는 9000/tcp를 허용했고, `iptables` rule에서 80→9000 redirect가 등록됐는지 별도로 확인했다. VirtualBox NAT, Linux `iptables`, UFW, Spring port는 서로 대체 관계가 아니다.

### 3. Maven package와 JAR artifact

Maven package는 반드시 `pom.xml`이 있는 project root에서 수행했다. Maven 설치 뒤 version을 확인하고 `clean package`를 실행했으며, test는 수업 option으로 건너뛰었다. 성공 뒤 `target/`에서 실행 대상 JAR가 실제로 생성됐는지 확인했다.

- `clean`: 이전 `target` 결과를 정리한다.
- `package`: source와 dependency를 build해 JAR artifact를 만든다.
- `-DskipTests`: test 성공이 아니라 test 실행 생략이다.
- `target` JAR 확인: package 명령 종료와 별개의 artifact 확인 단계다.

자세한 build tool 책임은 [[entities/maven|Maven]]이 맡는다.

### 4. host process와 browser 확인

생성된 JAR에 `java -jar`를 적용해 Spring Boot를 Linux host process로 실행했다. 마지막으로 browser가 host 8100→guest 80→guest 9000 경로를 거쳐 application 응답을 받는지 확인했다.

## 완료 조건을 한 단계씩 판정하기

| 완료 조건 | 확인 대상 | 통과해도 아직 증명되지 않는 것 |
|---|---|---|
| Maven 설치 | `mvn -v`의 version 정보 | project build 성공 |
| package 성공 | Maven 종료 결과 | JAR 이름·위치와 runtime 성공 |
| artifact 생성 | `target/`의 JAR | process 실행 |
| process 실행 | `java -jar` 뒤 application 시작 | 외부 port 접근 |
| port 경로 준비 | NAT·iptables·UFW·9000 설정 | browser HTTP 응답 |
| browser 응답 | host browser의 실제 page | 후속 Docker·EC2·CI/CD 성공 |

이 구분은 [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]의 핵심 사례다. “build가 성공했으니 server가 열렸다”거나 “UFW를 허용했으니 page가 보여야 한다”는 식으로 단계를 합치지 않는다.

## 2026-04-30 Dockerfile/JAR 후속 활용

[[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]]에는 같은 JAR 실행 원리를 container image로 옮겼다.

1. project root에서 Maven package를 수행해 `target` JAR를 확인했다.
2. Dockerfile의 `ARG`와 `COPY`가 그 JAR를 image에 넣었다.
3. `EXPOSE 9000`은 container가 사용할 port를 문서화했다.
4. `ENTRYPOINT`가 container 시작 시 `java -jar`를 자동 실행했다.
5. image build, container `Up`, Spring start log, DB 연결, browser 9000 응답을 각각 확인했다.

이것은 **R07의 container 활용**이며, R05의 host `java -jar` 실행과 같은 runtime으로 합치지 않는다. Dockerfile의 실제 instruction은 R07에 각각 분리된 연속 원문으로 존재하지만, 이 페이지에서는 서로 떨어진 조각을 하나의 수업 원문 fence로 합성하지 않고 역할만 설명한다. ^[raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md]

## 자주 헷갈리는 점과 선택 기준

- **Maven vs Java:** Maven은 dependency와 build lifecycle을 처리해 JAR를 만들고, Java runtime은 JAR를 process로 실행한다.
- **host JAR vs container JAR:** 04-28은 Ubuntu guest에 직접 띄운 process이고, 04-30은 image 안의 `ENTRYPOINT`가 띄운 container process다.
- **NAT vs redirect vs firewall:** NAT는 host→guest 경계, `iptables` REDIRECT는 guest 내부 port 전환, UFW는 허용/차단 규칙이다.
- **port 설정 vs listening:** `server.port=9000`은 의도한 설정이다. 실제 process가 실행되어 해당 port를 받아야 listening 상태가 된다.
- **build 성공 vs runtime 성공:** JAR가 생겨도 Java version, DB 설정, process 오류 때문에 server가 시작되지 않을 수 있다.
- **browser 실패:** source·build부터 다시 하지 말고 process→listening port→firewall/redirect→VM 경로 순으로 실패 지점을 좁힌다.

## 선행·후속 연결과 범위 경계

- 선행: [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]에서 IntelliJ로 작성·실행한 Spring Boot project가 Linux에서 package할 source가 됐다.
- 직접 Linux: [[summaries/2026-04-27-linux-archive-java-alias|04-27]]의 JDK·Java 실행과 host web server에서 R05의 Spring Boot JAR 실행으로 확장했다.
- 후속 Docker: R07의 Dockerfile은 JAR를 image artifact로 재사용했다.
- 후속 AWS·CI/CD: EC2 Linux instance와 GitHub Actions의 Maven build는 이 수동 흐름을 cloud와 workflow로 확장하지만, Linux 직접 실습과 별도다.

## 관련 페이지

- [[entities/maven|Maven]]
- [[entities/linux|Linux]]
- [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[comparisons/host-port-forwarding-vs-docker-port-mapping|호스트 포트 포워딩 vs Docker 포트 매핑]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — host project 준비, 9000 port, NAT·iptables·UFW, Maven package, JAR와 browser 확인
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` — Maven JAR를 Dockerfile image와 container process로 확장한 후속 실습
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — Maven→JAR→process→port 연결의 과목 복습 허브
