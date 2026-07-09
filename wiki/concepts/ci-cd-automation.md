---
title: CI/CD 자동화
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [ci-cd, backend, curriculum]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf
status: growing
confidence: high
---

# CI/CD 자동화

## 정의

CI/CD는 코드 변경이 들어왔을 때 빌드·검증·패키징·배포 절차를 자동화해, 개발자가 매번 같은 명령을 수동으로 반복하지 않게 만드는 개발/운영 흐름이다.

## 왜 중요한가

수동 배포는 “빌드 파일을 잘못 복사함”, “서버 명령을 빼먹음”, “환경값을 코드에 노출함”, “팀원마다 배포 방식이 다름” 같은 문제가 생기기 쉽다. CI/CD는 이런 절차를 workflow로 고정해 반복 가능하게 만든다.

## 수업에서의 핵심 흐름

```text
개발자
  ↓ git push
GitHub
  ↓ CI: checkout, JDK setup, Maven build, Docker build/push
Docker Hub
  ↓ CD: EC2에서 docker pull/run
AWS EC2
  ↓
사용자가 접속하는 서비스
```

- **CI(Continuous Integration, 지속적 통합)**: push된 코드를 가져와 빌드하고, 필요한 경우 테스트를 돌려 통합 가능한 상태인지 확인한다.
- **CD(Continuous Delivery/Deployment, 지속적 전달/배포)**: 빌드 산출물을 실제 서버나 컨테이너 환경에 반영한다.
- **Trigger**: workflow를 시작하는 사건이다. 수업에서는 GitHub `push`가 대표 trigger였다.

## 예시

Spring Boot 실습에서는 `push`가 발생하면 GitHub Actions가 JDK 21을 준비하고 Maven으로 jar를 빌드했다. 이후 Docker Hub에 이미지를 올리고, EC2가 그 이미지를 받아 컨테이너로 실행하는 구조로 확장했다.

## 자주 헷갈리는 점

- CI/CD는 도구 이름이 아니라 흐름이다. GitHub Actions, Jenkins, GitLab CI/CD, CircleCI는 이 흐름을 구현하는 도구다.
- CI 성공은 “빌드가 됐다”는 뜻이지 “서비스가 사용 가능하다”는 뜻은 아니다. 배포 후 URL/API/컨테이너 상태를 확인해야 한다.
- CD를 자동으로 운영 서버까지 반영할지, 승인 후 반영할지는 팀 정책에 따라 다르다.
- Secret 값은 workflow 파일에 직접 쓰지 않고 [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]로 분리한다.

## 관련 개념

- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11 CI/CD, GitHub Actions, Spring Boot 자동 배포]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[entities/github|GitHub]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_이론).pdf`
