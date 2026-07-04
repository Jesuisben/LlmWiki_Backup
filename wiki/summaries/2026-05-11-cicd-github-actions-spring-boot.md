---
title: 2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포
author: Hermes Agent
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [ci-cd, spring-boot, aws, backend, curriculum]
sources:
  - raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf
  - raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
status: growing
confidence: high
---

# 2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포

## 한 줄 요약

CI/CD를 “GitHub push를 트리거로 빌드·Docker 이미지 생성·Docker Hub push·EC2 배포를 자동 실행하는 흐름”으로 처음 실습한 날이다.

## 커리큘럼 위치

이 수업은 [[summaries/2026-05-08-aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS]] 다음 단계다. 이전까지는 EC2, RDS, Route 53, Load Balancer를 직접 만들고 접속했다면, 이날부터는 [[concepts/ci-cd-automation|CI/CD 자동화]]로 반복 배포를 줄이는 관점으로 넘어간다. 이후 중간 프로젝트에서는 이 흐름이 [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]으로 확장된다.

## 배운 내용

### 1. 자동화와 트리거

자동화(Automation)는 한 번 규칙을 정해 두면 특정 이벤트가 발생했을 때 정해진 작업을 자동 실행하는 것이다. 수업에서는 대표 트리거를 GitHub `push`로 잡았다. 즉, 개발자가 코드를 올리면 GitHub Actions가 workflow를 시작한다.^[raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md]

### 2. CI와 CD의 역할 분리

수업 흐름은 다음처럼 정리할 수 있다.

```text
개발자
  ↓ git push
GitHub
  ↓ GitHub Actions CI: Maven build, Docker image build/push
Docker Hub
  ↓ CD: EC2에서 docker pull/run
AWS EC2
  ↓
Service Deployed
```

- CI(Continuous Integration): GitHub push 이후 소스 체크아웃, JDK 설정, Maven build, Docker image build/push까지의 통합 검증 흐름.
- CD(Continuous Deployment/Delivery): Docker Hub에 올라간 이미지를 EC2가 받아 컨테이너로 실행해 서비스에 반영하는 흐름.

### 3. Spring Boot 실습 프로젝트 준비

Spring Initializr에서 Maven, Java 21, Jar packaging 기반 Spring Boot 프로젝트를 만들고, `MainController`와 `server.port=9000`을 추가했다. `pom.xml`에는 Web/Thymeleaf 의존성과 `<finalName>cicd</finalName>` 설정을 넣어 빌드 산출물 이름을 고정했다.

### 4. GitHub Actions CI 설정

`.github/workflows/ci.yml` 위치가 중요하다고 정리했다. `master` 브랜치에 push하면 `ubuntu-latest` runner에서 checkout, JDK 21 setup, Maven build가 실행된다.

```yaml
name: Spring Boot CI
on:
  push:
    branches:
      - master
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: maven
      - run: mvn clean package -DskipTests
```

### 5. Docker Hub, GitHub Secrets, EC2 배포

Docker Hub repository를 만들고, Docker Hub Access Token과 EC2 접속 정보를 GitHub Repository Secrets에 등록했다. 원본에는 실습용 token/IP 예시가 포함되어 있으나, 위키에서는 민감값을 재노출하지 않고 `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `EC2_HOST`, `EC2_KEY`, `DOCKER_IMAGE`, `DOCKER_CONTAINER`처럼 이름과 역할만 남긴다.

CI workflow에는 Docker Hub 로그인, 이미지 빌드, 이미지 push 단계가 추가되었다. CD workflow는 EC2에서 기존 컨테이너를 갱신하고 `80:9000` 포트 매핑으로 Spring Boot 컨테이너를 서비스한다.

## 실습 / 예제

1. `D:\ci_cd`에 Spring Boot 실습 프로젝트 생성.
2. GitHub repository를 만들고 initial commit/push.
3. `.github/workflows/ci.yml` 생성 후 Actions에서 build 성공 확인.
4. Docker Hub repository와 access token 준비.
5. GitHub Secrets에 Docker/EC2 관련 값 등록.
6. Dockerfile과 workflow를 이용해 Docker image build/push.
7. EC2에 Docker 설치 후 Actions로 컨테이너 배포.
8. Controller, template, static image를 추가한 뒤 다시 push해서 웹 페이지 변경 반영 확인.

## 헷갈린 점 / 질문

- `ci.yml`은 아무 위치나 두면 안 되고 반드시 `.github/workflows/` 아래에 있어야 한다.
- GitHub Secrets는 값을 숨겨 주지만, Secret 이름과 workflow의 참조 이름이 다르면 배포가 실패한다.
- Actions 성공 표시만으로 끝내면 안 된다. EC2에서 `docker container ps -a`와 실제 URL 접속으로 컨테이너가 떠 있는지 확인해야 한다.
- 실습에서는 `master` 브랜치를 기준으로 했지만, 프로젝트에 따라 `main`일 수 있으므로 workflow의 branch 설정을 저장소 기본 브랜치와 맞춰야 한다.

## 관련 페이지

- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[entities/github|GitHub]]
- [[entities/spring-boot|Spring Boot]]

## 출처

- `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf`
- `raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
