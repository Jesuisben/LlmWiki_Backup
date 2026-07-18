---
title: 2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포
author: Hermes Agent
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [ci-cd, spring-boot, aws, backend, curriculum]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
status: growing
confidence: high
---

# 2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포

## 한 줄 요약

GitHub push를 trigger로 Maven·Docker image·registry·EC2 container를 잇는 CI/CD workflow를 구성하고, 최종 container 실행 출력까지 확인한 날이다.

## 커리큘럼 위치

이 수업은 [[summaries/2026-05-08-aws-rds-resource-cleanup|AWS의 EC2·RDS 수동 배포 실습]] 다음 단계다. 이전의 VPC·EC2·RDS 구성을 바탕으로, 이날부터는 [[concepts/ci-cd-automation|CI/CD 자동화]]로 반복 배포를 줄이는 관점으로 넘어간다. Route 53·ALB·HTTPS 구성 절차는 다음 날 2026-05-12에 다뤘다.

## 배운 내용

### 1. 자동화와 트리거

자동화(Automation)는 한 번 규칙을 정해 두면 특정 이벤트가 발생했을 때 정해진 작업을 자동 실행하는 것이다. 수업에서는 대표 트리거를 GitHub `push`로 잡았다. 즉, 개발자가 코드를 올리면 GitHub Actions가 workflow를 시작한다.^[raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md]

### 2. CI와 CD의 역할 분리

수업 흐름은 다음처럼 정리할 수 있다.

개발자가 `git push`하면 GitHub Actions가 checkout·JDK 설정·Maven build를 수행하고, 확장 workflow가 Docker image를 만들어 registry에 올린 뒤 EC2의 container 갱신 단계로 넘기는 순서다. 이 설명은 단계의 책임을 나타내며 각 단계의 성공 결과가 모두 원본에 남았다는 뜻은 아니다.

- CI(Continuous Integration): 기본 `ci.yml`에서 GitHub push 뒤 소스 체크아웃, JDK 설정, Maven build로 애플리케이션이 통합 가능한지 확인하는 흐름.
- CD(Continuous Deployment/Delivery): Docker Hub에 올라간 image를 EC2가 받아 기존 container를 갱신하고 새 container를 실행해 서비스에 반영하는 흐름. 수업에서는 Docker Hub login·image build/push 확장과 별도 `cd.yml` 복사로 이 배포 단계를 연결했다.

### 3. Spring Boot 실습 프로젝트 준비

Spring Initializr에서 Maven, Java 21, Jar packaging 기반 Spring Boot 프로젝트를 만들고, `MainController`와 `server.port=9000`을 추가했다. `pom.xml`에는 Web/Thymeleaf 의존성과 `<finalName>cicd</finalName>` 설정을 넣어 빌드 산출물 이름을 고정했다.

### 4. GitHub Actions CI 설정

`.github/workflows/ci.yml` 위치가 중요하다고 정리했다. `master` 브랜치에 push하면 `ubuntu-latest` runner에서 checkout, JDK 21 setup, Maven build가 실행된다.

원본의 연속 `ci.yml`은 `master` push, `ubuntu-latest`, `actions/checkout@v4`, `actions/setup-java@v4`, JDK 21·Temurin·Maven cache, `mvn clean package -DskipTests`를 차례로 정의한다. `-DskipTests`를 사용했으므로 테스트 성공 증거가 아니라 테스트를 생략한 package 절차다. workflow 파일을 저장소에 추가했다는 사실과 runner에서 build가 성공했다는 결과도 구분해야 한다.

### 5. Docker Hub, GitHub Secrets, EC2 배포

Docker Hub repository를 만들고, Docker Hub Access Token과 EC2 접속 정보를 GitHub Repository Secrets에 등록했다. 원본에는 실습용 token/IP 예시가 포함되어 있으나, 위키에서는 민감값을 재노출하지 않고 `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `EC2_HOST`, `EC2_KEY`, `DOCKER_IMAGE`, `DOCKER_CONTAINER`처럼 이름과 역할만 남긴다.

원본은 `ci.yml`에 Docker Hub login·image build·push 단계를 추가하고, 별도 `cd.yml`을 workflow 경로에 복사해 EC2 배포를 연결하는 순서까지 기록한다. `cd.yml` 전문은 날짜 원본에 없으므로, 위키에서는 특정 SSH action이나 명령을 추정하지 않고 EC2에서 기존 container를 갱신하고 `80:9000` 포트 매핑으로 Spring Boot container를 서비스하는 역할만 보존한다.

## 실습 / 예제

1. `D:\ci_cd`에 Spring Boot 실습 프로젝트를 준비하고 GitHub repository에 첫 push를 기록했다.
2. `.github/workflows/ci.yml`을 만든 뒤 Actions 화면에서 commit과 build history를 확인하는 절차를 기록했다. 성공 로그 본문은 보존되지 않았다.
3. Docker Hub repository·access token과 Docker/EC2 관련 GitHub Secrets를 준비했다.
4. workflow에 Docker login·image build·push 단계를 추가하고 별도 `cd.yml`을 배치했다. image push·원격 배포 log는 원본에 없다.
5. EC2에서 Docker 설치·group 설정을 진행했다. `groups`와 `docker version` 출력은 보존되어 Docker 사용 준비를 확인할 수 있다.
6. `docker container ps -a` 출력에는 Spring Boot container가 실행 중이며 host 80번이 container 9000번으로 연결된 상태가 남아 있다.
7. Controller·template·정적 이미지를 바꾸고 재차 push한 commit 이름과 확인할 URL은 기록했지만, 브라우저 응답 화면이나 변경 내용이 표시된 결과는 보존되지 않았다.

### 보존된 결과와 미보존 경계

| 단계 | 원본에 남은 증거 | 판단 |
|---|---|---|
| 기본 CI | workflow 정의, push·Actions 화면 확인 절차 | build 성공 log 미보존 |
| Docker 준비 | group·Docker client/server version 출력 | EC2 Docker 실행 기반 확인 |
| image build/push·원격 CD | workflow 단계와 `cd.yml` 배치 지시 | image registry·SSH 배포 log 미보존 |
| container | `docker container ps -a`의 `Up`·port mapping 출력 | container 실행은 직접 확인 가능 |
| 웹 변경 | 접속 URL과 재배포 절차 | 실제 browser 응답·변경 화면 미보존 |

## 헷갈린 점 / 질문

- `ci.yml`은 아무 위치나 두면 안 되고 반드시 `.github/workflows/` 아래에 있어야 한다.
- GitHub Secrets는 값을 숨겨 주지만, Secret 이름과 workflow의 참조 이름이 다르면 배포가 실패한다.
- Actions 성공 표시만으로 끝내면 안 된다. Docker Hub image 갱신, EC2의 `docker container ps -a`, 실제 URL 접속을 순서대로 확인해야 한다.
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

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
