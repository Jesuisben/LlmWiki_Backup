---
title: GitHub Actions Secrets 기반 배포
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [github, ci-cd, aws, auth]
sources:
  - raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
  - D:/Study_LLM_Wiki/raw/Study/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - D:/Study_LLM_Wiki/raw/Study/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md
status: growing
confidence: medium
---

# GitHub Actions Secrets 기반 배포

## 정의

GitHub Actions Secrets 기반 배포는 workflow 실행 중 필요한 민감값을 GitHub Repository Secrets에 저장하고, YAML에서는 이름으로만 참조하는 배포 방식이다.

## 왜 중요한가

배포에는 SSH key, 서버 주소, DB 비밀번호, JWT 키처럼 노출되면 안 되는 값이 필요하다. 이 값을 코드나 위키에 적으면 저장소 히스토리에 남아 위험해진다.

## 핵심 설명

- Secret은 GitHub 저장소 설정에서 등록한다.
- workflow에서는 `${{ secrets.SECRET_NAME }}` 형태로 참조한다.
- Secret 이름은 역할 중심으로 짓고, 실제 값은 로그에 출력하지 않는다.
- 실습 원본에 예시 값이 있더라도 위키에는 `<SSH_PRIVATE_KEY>`, `<DB_PASSWORD>` 같은 placeholder만 사용한다.
- 2026-05-11 Spring Boot CI/CD 실습에서는 Docker Hub 계정/token, EC2 host/key, Docker image/container 이름을 repository secrets로 분리했다.

## 예시

```yaml
env:
  SERVER_HOST: ${{ secrets.SERVER_HOST }}
  SERVER_USER: ${{ secrets.SERVER_USER }}
  DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
```

## 자주 헷갈리는 점

- Secret은 “숨겨진 변수”이지, 코드 품질이나 인증 설계를 대신해 주는 기능은 아니다.
- Actions 로그에 `echo $SECRET`처럼 출력하면 감춰지더라도 위험한 습관이다.
- `.env`와 GitHub Secrets는 목적이 비슷하지만 저장 위치와 실행 시점이 다르다.

## 관련 개념

- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[concepts/jwt-rs256-key-flow|JWT RS256 키 흐름]]
- [[entities/github|GitHub]]

## 출처

- `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
- `raw/Study/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md`
- `raw/Study/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
