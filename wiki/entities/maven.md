---
title: Maven
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [spring-boot, backend, linux]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# Maven

## 무엇인가

Maven은 Java 프로젝트의 의존성 관리와 빌드를 수행하는 도구다. Spring Boot 프로젝트에서는 `pom.xml`을 기준으로 필요한 라이브러리와 빌드 과정을 관리한다.

## 이 위키에서의 맥락

Spring Boot 수업에서는 IDE가 많은 빌드 작업을 대신해 줬지만, Linux 수업에서는 서버 터미널에서 직접 Maven을 설치하고 `.jar` 파일을 만드는 과정을 배웠다. Dockerfile로 Spring Boot 이미지를 만들 때도 먼저 Maven package로 jar를 준비했다.

## 학습 이력

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]: `sudo apt install -y maven`, `mvn -v`, `mvn clean package -DskipTests`로 Spring Boot 프로젝트를 패키징했다.
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]]: `target/*.jar`를 Dockerfile의 `ARG JAR_FILE`과 `COPY` 대상으로 사용해 Spring Boot 컨테이너 이미지를 만들었다.

## 핵심 기능 / 특징

- `pom.xml` 기반 의존성 관리.
- `mvn clean package`로 빌드 산출물 생성.
- Spring Boot 배포에서는 `target/` 아래 `.jar` 파일을 만드는 역할.
- Docker 이미지 빌드 전 단계에서 실행 가능한 jar를 준비한다.

## 헷갈리는 점

- Maven은 서버가 아니라 빌드 도구다.
- `mvn package`를 실행하려면 보통 `pom.xml`이 있는 프로젝트 루트에 있어야 한다.
- `-DskipTests`는 테스트를 건너뛰고 패키징하는 옵션이므로, 실무에서는 테스트 생략의 의미를 알고 써야 한다.
- Dockerfile의 `COPY target/*.jar ...`는 Maven 빌드 결과물이 있어야 성공한다.

## 관련 개념

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/java|Java]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf`
