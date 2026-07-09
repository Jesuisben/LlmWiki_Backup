---
title: 중간 프로젝트 CI/CD 배포 흐름
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [project, ci-cd, aws, spring-boot, react]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
  - D:/Study_LLM_Wiki/raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - D:/Study_LLM_Wiki/raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md
status: growing
confidence: medium
---

# 중간 프로젝트 CI/CD 배포 흐름

## 정의

중간 프로젝트 CI/CD 배포 흐름은 GitHub 저장소의 변경을 기준으로 빌드, Docker image 생성/전송, 서버 반영, 서비스 확인을 자동화하는 절차다. 2026-05-11 수업의 Spring Boot 단일 프로젝트 CI/CD 실습이 중간 프로젝트 배포 가이드의 기반이 된다.

## 왜 중요한가

수동 배포는 파일 누락, 서버 명령 실수, 환경 변수 노출 위험이 크다. CI/CD를 쓰면 같은 절차를 반복 가능하게 만들고, 팀 프로젝트에서 “내 PC에서는 됨” 문제를 줄일 수 있다.

## 핵심 설명

- **코드 저장소**: GitHub가 변경 이력과 workflow 실행의 출발점이다.
- **빌드 단계**: Spring Boot는 jar로 빌드하고, 필요하면 Docker image로 패키징한다. React는 정적 파일 또는 프론트엔드 산출물로 준비된다.
- **Registry 단계**: Spring Boot Docker image는 Docker Hub 같은 registry에 push할 수 있다.
- **Secrets 단계**: Docker token, 서버 IP, SSH key, DB 접속값, JWT 키 같은 민감값은 workflow 파일에 직접 쓰지 않고 GitHub Secrets에서 읽는다.
- **배포 단계**: EC2에서 새 image를 pull하거나 산출물을 복사하고 기존 프로세스/container 상태를 갱신한다.
- **확인 단계**: 웹 접속, API 응답, Actions log, container/process/port 상태를 확인한다.

## 예시 흐름

```yaml
# 구조 예시: 실제 secret 값은 저장하지 않는다.
name: deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build and deploy
        run: echo "build/deploy steps"
```

## 자주 헷갈리는 점

- workflow YAML에는 Secret **값**이 아니라 `${{ secrets.NAME }}` 같은 참조만 남긴다.
- EC2 접속 정보와 RDS 접속 정보는 역할이 다르다.
- 배포 성공은 Actions 성공 표시만 보지 말고 실제 서비스 URL/API 응답까지 확인해야 한다.
- 05-11 수업의 실습용 Docker token, EC2 IP, key 값은 학습 원본에 있어도 wiki와 저장소에는 재노출하지 않는다.

## 관련 개념

- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/aws-s3-file-upload|AWS S3 파일 업로드 흐름]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[entities/github|GitHub]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md`
