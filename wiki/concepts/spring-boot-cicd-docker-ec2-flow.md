---
title: Spring Boot CI/CD Docker-EC2 배포 흐름
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [spring-boot, ci-cd, aws, backend]
sources:
  - raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
status: growing
confidence: high
---

# Spring Boot CI/CD Docker-EC2 배포 흐름

## 정의

Spring Boot CI/CD Docker-EC2 배포 흐름은 Spring Boot 애플리케이션을 jar로 빌드하고 Docker image로 패키징한 뒤, Docker Hub를 거쳐 AWS EC2에서 컨테이너로 실행하는 자동 배포 구조다.

## 왜 중요한가

이전에는 EC2에 직접 접속해 JDK/Maven을 설치하고 `mvn clean package`, `java -jar`를 수동으로 실행했다. CI/CD를 붙이면 push 한 번으로 같은 빌드·이미지 생성·배포 절차를 반복할 수 있어 중간 프로젝트 같은 팀 작업에서 실수를 줄일 수 있다.

## 전체 흐름

```text
Spring Boot code
  ↓ git push
GitHub repository
  ↓ GitHub Actions
Maven build: cicd.jar 생성
  ↓
Docker build: SpringDockerFile 기반 image 생성
  ↓
Docker Hub push
  ↓ SSH 접속/원격 명령
AWS EC2 docker pull
  ↓
기존 container 중지/삭제 후 새 container 실행
  ↓
80:9000 포트 매핑으로 서비스 확인
```

## 단계별 설명

### 1. Spring Boot 프로젝트 준비

- `MainController`에서 `/` 요청에 문자열을 반환한다.
- `application.properties`에서 `server.port=9000`을 설정한다.
- `pom.xml`에 Web/Thymeleaf 의존성을 추가하고 `<finalName>cicd</finalName>`으로 jar 이름을 고정한다.

### 2. CI: GitHub Actions에서 Maven build

GitHub Actions runner가 JDK 21을 준비하고 `mvn clean package -DskipTests`를 실행한다. 여기서 실패하면 Docker image를 만들기 전에 문제를 발견할 수 있다.

### 3. Docker image build/push

workflow가 Docker Hub에 login한 뒤 `SpringDockerFile`을 사용해 image를 만들고 Docker Hub repository에 push한다. Docker Hub token은 [[concepts/github-actions-secrets-deploy|GitHub Secrets]]로 분리한다.

### 4. CD: EC2에서 컨테이너 실행

EC2에는 Docker가 설치되어 있어야 한다. workflow는 EC2에 SSH로 접속해 새 image를 pull하고, 기존 container를 갱신한다. 실습에서는 `0.0.0.0:80->9000/tcp` 형태로 외부 80번 요청을 Spring Boot 9000번 컨테이너 포트로 연결했다.

## 검증 포인트

- GitHub Actions run이 성공했는가?
- Docker Hub에 새 image tag가 올라갔는가?
- EC2에서 `docker container ps -a`에 새 container가 떠 있는가?
- Security Group이 80/9000 등 필요한 포트를 허용하는가?
- 브라우저에서 `/`, `/first`, `/second` 같은 URL이 실제로 응답하는가?

## 자주 헷갈리는 점

- Maven build 산출물(jar)과 Docker image는 다르다. jar는 애플리케이션 파일이고, Docker image는 실행 환경까지 묶은 템플릿이다.
- Docker Hub는 배포 서버가 아니라 image registry다. EC2가 Docker Hub에서 image를 pull해서 실행한다.
- EC2 접속 key, Docker token, image 이름, container 이름은 workflow 코드에 직접 쓰지 말고 Secrets로 관리한다.
- Load Balancer/Route 53/HTTPS 앞단과 이 컨테이너 배포 흐름은 서로 연결되지만 책임이 다르다. 컨테이너가 떠 있어야 ALB health check와 도메인 접속도 의미가 있다.

## 관련 개념

- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[entities/docker|Docker]]
- [[entities/amazon-ec2|Amazon EC2]]

## 출처

- `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
