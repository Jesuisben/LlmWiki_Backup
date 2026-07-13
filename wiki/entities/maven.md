---
title: Maven
created: 2026-07-02
updated: 2026-07-13
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

Maven은 Java 프로젝트의 의존성 관리와 빌드를 수행하는 도구다. Spring Boot 프로젝트에서는 `pom.xml`을 기준으로 필요한 라이브러리와 빌드 과정을 관리한다.

## 이 위키에서의 맥락

Spring Boot 수업에서는 IDE가 빌드 작업을 많이 대신해 주었지만, Linux 수업에서는 서버 터미널에서 직접 Maven을 설치하고 `.jar` 파일을 만드는 과정을 배웠다. Dockerfile로 Spring Boot 이미지를 만들 때도 먼저 Maven package로 jar를 준비했다.

## 핵심 기능 / 특징

- `pom.xml` 기반 의존성 관리.
- `mvn -v`로 설치와 버전 확인.
- `mvn clean package -DskipTests`로 jar 생성.
- 생성된 `target/*.jar`를 `java -jar` 또는 Dockerfile `COPY` 대상으로 사용.

## 학습 이력

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28]]: Linux 서버에서 Maven 설치와 Spring Boot jar 패키징.
- [[summaries/2026-04-30-dockerfile-spring-load-balancing|2026-04-30]]: jar를 Docker image에 포함해 컨테이너로 실행.

## 관련 개념

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/docker|Docker]]

## 출처

- `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md`
