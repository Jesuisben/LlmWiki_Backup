---
title: Linux에서 Spring Boot 서버 실행
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, spring-boot, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
status: growing
confidence: high
---

# Linux에서 Spring Boot 서버 실행

## 정의

Linux에서 Spring Boot 서버를 실행한다는 것은 IDE의 실행 버튼이 아니라 서버 터미널에서 프로젝트를 빌드하고, 만들어진 `.jar` 파일을 Java로 실행하며, 포트와 방화벽을 열어 브라우저/API 클라이언트가 접근하게 만드는 과정이다.

## 수업에서 배운 흐름

1. 기존 nginx/apache2가 80번 포트 등을 점유하지 않도록 중지했다.
2. GitHub에서 Spring Boot 예제 프로젝트를 clone했다.
3. Maven을 설치했다.
4. `pom.xml`이 있는 프로젝트 루트에서 `mvn clean package -DskipTests`를 실행했다.
5. `target/` 아래 `.jar` 파일을 확인했다.
6. 서버 포트와 방화벽을 설정했다.
7. 브라우저에서 Spring Boot 응답을 확인했다.

## 핵심 명령어

```bash
sudo systemctl stop nginx
sudo systemctl disable nginx
sudo apt install -y maven
mvn -v
mvn clean package -DskipTests
cd target
ls *.jar
sudo ufw allow 9000/tcp
```

## 왜 중요한가

지금까지 [[entities/spring-boot|Spring Boot]]는 개발 PC에서 실행하는 백엔드 프레임워크였다. Linux 수업에서는 이를 서버에서 빌드·실행하는 배포 대상으로 바라보기 시작했다. 이 관점이 Docker 이미지 생성과 CI/CD로 이어진다.

## 자주 헷갈리는 점

- Maven 명령은 `pom.xml`이 있는 위치에서 실행해야 한다.
- `.jar` 생성과 서버 실행은 다른 단계다. `mvn package`는 빌드, `java -jar`는 실행이다.
- 포트가 열려 있어도 방화벽이나 포트 리다이렉션 설정이 맞지 않으면 브라우저 접근이 안 될 수 있다.
- nginx/apache2 같은 기존 웹 서버가 같은 포트를 쓰고 있으면 Spring Boot 확인이 꼬일 수 있다.

## 관련 페이지

- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문]]
- [[entities/maven|Maven]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
