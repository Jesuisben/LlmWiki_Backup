---
title: Linux에서 Spring Boot 서버 실행
created: 2026-07-02
updated: 2026-07-06
type: concept
tags: [linux, spring-boot, backend]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/Linux 총정리/Linux 총정리.md
status: growing
confidence: high
---

# Linux에서 Spring Boot 서버 실행

## 정의

Linux에서 Spring Boot 서버 실행은 IDE가 아니라 서버 터미널에서 프로젝트를 가져오고, Maven으로 jar를 만든 뒤, Java 명령으로 애플리케이션을 띄우는 과정이다.

## 왜 중요한가

개발 PC에서 실행되는 애플리케이션은 실제 서비스가 아니다. Linux 서버에서 jar 또는 Docker container로 실행할 수 있어야 AWS EC2, CI/CD, 운영 배포로 넘어갈 수 있다.

## 핵심 설명

수업 흐름은 다음 순서였다.

1. GitHub에서 Spring Boot 프로젝트를 Linux 서버로 clone.
2. Spring Boot 포트 번호 확인.
3. 서버 방화벽/포트 허용.
4. Maven 설치.
5. `mvn clean package -DskipTests`로 jar 생성.
6. `java -jar`로 서버 실행.
7. 브라우저에서 VM IP와 포트로 확인.
8. 같은 jar를 Dockerfile에 넣어 컨테이너 실행으로 확장.

## 예시

```bash
git clone https://github.com/계정/프로젝트.git
cd 프로젝트
sudo apt install -y maven
mvn -v
mvn clean package -DskipTests
java -jar target/*.jar
sudo ufw allow 9000
```

Dockerfile로 이어질 때는 jar가 이미지의 실행 대상이 된다.

```dockerfile
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

## 자주 헷갈리는 점

- `mvn clean package`는 빌드이고, `java -jar`는 실행이다.
- 포트가 안 열리면 Spring 코드, VM IP, 방화벽, 포트 점유, Docker port mapping을 함께 확인해야 한다.
- 서버에 소스 코드를 clone하는 방식은 학습용으로 직관적이지만, 이후 CI/CD에서는 빌드 산출물이나 Docker image를 배포하는 흐름으로 발전한다.

## 관련 개념

- [[entities/maven|Maven]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
