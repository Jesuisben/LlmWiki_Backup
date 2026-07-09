---
title: GitHub Actions workflow
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [ci-cd, backend]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
status: growing
confidence: high
---

# GitHub Actions workflow

## 정의

GitHub Actions workflow는 GitHub 저장소 안의 `.github/workflows/*.yml` 파일로 정의하는 자동화 절차다. push, pull request 같은 이벤트가 발생하면 GitHub가 runner에서 정해진 step을 실행한다.

## 왜 중요한가

수업에서는 Spring Boot 프로젝트를 GitHub에 push했을 때 자동으로 Maven build가 실행되도록 만들었다. 이후 같은 workflow에 Docker Hub login, Docker image build/push, EC2 배포 단계를 붙여 [[concepts/ci-cd-automation|CI/CD 자동화]]로 확장했다.

## 핵심 구조

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
      - name: Checkout source
        uses: actions/checkout@v4

      - name: Set up JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: maven

      - name: Build with Maven
        run: mvn clean package -DskipTests
```

| 구성 | 의미 | 수업 예시 |
|---|---|---|
| `name` | Actions 화면에 보이는 workflow 이름 | `Spring Boot CI` |
| `on` | workflow trigger | `master` branch push |
| `jobs` | 실행할 작업 묶음 | `build` |
| `runs-on` | 실행 환경 | `ubuntu-latest` |
| `steps` | 순서대로 실행할 단계 | checkout, JDK setup, Maven build |
| `uses` | 재사용 action 호출 | `actions/checkout@v4` |
| `run` | shell command 실행 | `mvn clean package -DskipTests` |

## Secret을 쓰는 확장 단계

Docker Hub나 EC2 배포 단계에서는 민감값이 필요하다. 이때 workflow에는 값을 직접 쓰지 않고 다음처럼 GitHub Secrets를 참조한다.

```yaml
- name: Login to DockerHub
  run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

- name: Build Docker Image
  run: docker build -t "${{ secrets.DOCKER_IMAGE }}" -f SpringDockerFile .

- name: Push Docker Image
  run: docker push "${{ secrets.DOCKER_IMAGE }}"
```

## 자주 헷갈리는 점

- workflow 파일 위치는 `.github/workflows/`여야 한다.
- 저장소 기본 브랜치가 `main`인데 YAML은 `master`로 되어 있으면 push해도 실행되지 않을 수 있다.
- Secret 이름은 대소문자와 철자가 정확히 맞아야 한다.
- Actions의 초록 체크는 자동화 절차가 성공했다는 뜻이지, 사용자가 접속하는 도메인까지 정상이라는 뜻은 아니다.

## 관련 개념

- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[entities/github|GitHub]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
