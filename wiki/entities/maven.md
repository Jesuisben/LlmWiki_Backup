---
title: Maven
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [spring-boot, backend, linux]
sources:
  - raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Maven

## 무엇인가

Maven은 Java project의 dependency와 build lifecycle을 `pom.xml` 중심으로 관리하는 build tool이다. 이 수업에서는 IntelliJ에서 작성했던 Spring Boot source를 Linux server와 Docker image에서 실행할 수 있는 **JAR artifact로 만드는 역할**로 중요해졌다.

Maven은 Spring Boot application을 계속 실행하는 runtime도 아니고, Docker image를 만드는 도구도 아니다. Maven의 직접 결과는 `target/` 아래 build artifact다.

## 선행 맥락과 Linux에서의 첫 직접 build

[[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]에서는 Spring Initializr로 Jar project를 만들고 IntelliJ 안에서 Member·Product·Cart·Order 기능을 작성·실행했다. 이 단계가 Maven project 구조와 `pom.xml`을 가진 source의 선행 맥락이다.

Maven 자체를 Linux terminal에서 설치하고 package→JAR 결과까지 직접 확인한 핵심 수업은 [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]이다.

1. Ubuntu에 Maven package를 설치했다.
2. `mvn -v`로 Maven version을 확인했다.
3. `pom.xml`이 있는 project root로 이동했다.
4. clean package를 test 생략 option과 함께 실행했다.
5. `target/`에서 실제 JAR artifact를 확인했다.
6. Java runtime이 그 JAR를 Spring Boot process로 실행했다.

설치 확인, build 성공, artifact 확인, runtime server 성공은 각각 다른 완료 조건이다. ^[raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md]

## `pom.xml`과 build 요소의 역할

| 요소 | Maven에서의 책임 | 수업에서 연결된 결과 |
|---|---|---|
| project root | Maven 명령이 project 설정을 찾는 기준 위치 | `pom.xml`이 있는 directory에서 package 수행 |
| `pom.xml` | dependency·plugin·packaging·build 설정 선언 | Spring Boot source를 build할 규칙 제공 |
| dependency | compile/runtime에 필요한 library 좌표 | source와 필요한 library의 build classpath 구성 |
| plugin | compile·test·package 같은 lifecycle 작업 실행 보조 | executable JAR 생성 과정에 참여 |
| `clean` | 이전 build output 제거 | 과거 `target` 결과와 새 build 혼동 방지 |
| `package` | compile·test 단계와 packaging lifecycle 수행 | JAR artifact 생성 |
| `target/` | build output directory | 실행·Docker COPY 대상 JAR 확인 |

이 표는 Maven의 책임을 설명한다. 수업 원본은 dependency/plugin 각각의 resolve log나 개별 plugin 설정을 분석한 것이 아니라, `pom.xml` 기반 package와 JAR 결과를 중심으로 다뤘다.

## 대표 입력 → 처리 → 결과

### 04-28 Linux 수동 package

- 입력: clone한 Spring Boot source, project root의 `pom.xml`, 설치된 Maven/JDK
- 처리: 이전 `target`을 정리하고 source·dependency를 build해 package
- 결과: `target` directory의 executable JAR

`-DskipTests`를 사용했으므로 test suite 통과가 결과에 포함되지는 않는다. package 명령이 끝났더라도 `target`에 기대한 JAR가 있는지 확인해야 artifact 단계가 닫힌다.

### Maven과 `java -jar`의 책임 분리

| 단계 | 실행 주체 | 결과 |
|---|---|---|
| package | Maven | JAR file artifact |
| application 실행 | Java runtime | Linux의 Spring Boot process |
| 외부 접속 | OS/network/browser | port 경로를 지난 HTTP 응답 |

Maven build 성공은 runtime server 성공이 아니다. JAR가 생성돼도 Java version, application 설정, DB 연결, port·firewall 문제로 실행 또는 browser 확인이 실패할 수 있다. 상세 runtime 흐름은 [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]과 [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]에 연결한다.

## 2026-04-30 Dockerfile에서의 후속 활용

[[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]]에는 Spring Boot+MySQL container 실습을 위해 Maven을 다시 사용했다.

1. `pom.xml`의 build final name과 Linux profile 관련 file을 확인했다.
2. project root에서 package를 수행했다.
3. `target`의 named JAR를 확인했다.
4. Dockerfile이 `ARG`·`COPY`로 JAR를 image에 넣었다.
5. Dockerfile의 `ENTRYPOINT`가 container 시작 시 Java runtime을 호출했다.

여기서 Maven은 image build 앞의 JAR producer다. Docker가 image를 만들고 container를 실행하며, Java가 JAR process를 시작한다. R07의 Dockerfile instruction은 실제 원본에서 여러 설명 사이에 각각 분리되어 있으므로, 이 페이지에서는 이를 하나의 연속 Maven 원문 fence처럼 합성하지 않는다. ^[raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md]

## CI/CD에서의 후속 역할

후속 [[concepts/github-actions-workflow|GitHub Actions workflow]]에서는 runner가 Maven build를 자동 실행할 수 있다. 이는 04-28의 사람이 terminal에서 수행한 수동 package를 pipeline 단계로 옮긴 것이다.

- Linux R05: 사람이 project root에서 수동 build하고 JAR를 확인
- Linux R07: JAR를 Docker image input으로 수동 사용
- CI/CD 후속: push trigger 뒤 runner가 test/build/image/deploy 단계를 자동 수행

GitHub Actions가 Maven을 호출해도 source checkout·workflow 실행·Docker push·EC2 배포가 Maven의 책임으로 바뀌지는 않는다.

## 확인된 범위와 확정하지 않는 것

### 확인된 것

- Linux Maven 설치와 version 출력
- `pom.xml`이 있는 root에서 package 수행
- R05 `target` JAR 확인과 host `java -jar` 실행
- R07 named JAR 확인과 Dockerfile COPY/ENTRYPOINT 후속 활용

### 같은 결과로 합치지 않는 것

- `-DskipTests` package를 test 성공으로 보지 않는다.
- JAR 생성과 Spring Boot process 시작을 한 완료 조건으로 보지 않는다.
- image build와 container `Up`, Spring log, DB 연결, browser 응답을 Maven build 성공으로 보지 않는다.
- CI Maven build와 R05 수동 package를 같은 수업일의 자동화 결과로 보지 않는다.

## 자주 헷갈리는 점

- **Maven 설치 vs project build:** `mvn -v`가 보여도 현재 project가 build된 것은 아니다.
- **project root:** 임의의 directory가 아니라 `pom.xml`이 있는 위치에서 lifecycle을 실행한다.
- **dependency vs JAR:** dependency는 project가 필요로 하는 library 정보이고, `target` JAR는 build 결과 artifact다.
- **package vs 실행:** Maven은 JAR를 만들고 Java runtime은 JAR를 실행한다.
- **`clean` vs 오류 해결:** 이전 output을 제거할 뿐 source·dependency·test 오류를 자동 해결하지 않는다.
- **`-DskipTests`:** test 성공이 아니라 실행 생략이다.
- **Maven vs Docker:** Maven JAR는 Docker build input이 될 수 있지만 image/container 생명주기는 Docker 책임이다.
- **Maven vs CI/CD:** Maven은 pipeline 안의 build tool이며 workflow 전체가 아니다.

## 프로젝트·면접에서 설명할 관점

> FrontEnd_BackEnd에서 만든 Spring Boot Maven project를 Linux에서 `pom.xml` 기준으로 package해 `target` JAR를 확인했다. Maven build, Java process 실행, port와 browser 응답을 별도 완료 조건으로 검증했고, 이후 Dockerfile의 image input과 CI workflow의 자동 build 단계로 확장되는 책임 경계를 이해했다.

## 학습 이력

- 선행: [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] — Spring Boot Jar project와 `pom.xml`을 가진 application source 작성
- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]] — Linux Maven 설치·version·수동 package·`target` JAR·host 실행
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]] — named JAR를 Dockerfile image에 포함해 container runtime으로 확장
- 후속: [[concepts/ci-cd-automation|CI/CD 자동화]] — 수동 Maven build를 workflow 단계로 자동화

## 관련 개념

- [[entities/spring-boot|Spring Boot]]
- [[entities/linux|Linux]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]]
- [[entities/docker|Docker]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` — Maven 설치·version, project root, package, `target` JAR, host `java -jar`의 직접 근거
- `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` — named JAR와 Dockerfile COPY/ENTRYPOINT 후속 활용
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — Maven build와 Java runtime·port·Docker 연결 복습
