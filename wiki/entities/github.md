---
title: GitHub
created: 2026-07-02
updated: 2026-07-03
type: entity
tags: [java, ci-cd]
sources:
  - raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/Study/1. Java/교육 자료/Github 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
  - raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
  - raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf
status: stable
confidence: high
---

# GitHub

## 무엇인가

GitHub는 Git 저장소를 온라인에 보관하고, 다른 사람과 코드 이력과 변경 사항을 공유하는 개발 협업 서비스다.

## 이 위키에서의 맥락

Java 수업 초기에 `MyJava` 저장소를 만들며 처음 등장했다. 당시에는 개인 Java 실습 코드를 원격 저장소에 올리는 목적이었고, 이후에는 팀 협업과 Pull Request 흐름으로 확장되었다.

## 핵심 기능 / 특징

- 원격 저장소(repository) 생성
- 로컬 Git 저장소와 remote URL 연결
- 코드 백업과 공유
- 팀 협업에서 branch, PR, merge, conflict 해결 지원
- GitHub Actions로 push 기반 CI/CD workflow 실행
- Repository Secrets로 Docker token, EC2 key 같은 민감값 분리

## 학습 이력

- [[summaries/2026-02-27-github-initial-setup|2026-02-27]]: `MyJava` 원격 저장소 준비와 IntelliJ 연동
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]]: GitHub/Git Bash/SourceTree 협업 입문
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]]: PR과 충돌 해결
- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11]]: GitHub Actions workflow와 Secrets로 Spring Boot CI/CD 자동화

## 관련 개념

- [[entities/git|Git]]
- [[entities/intellij-idea|IntelliJ IDEA]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]

## 출처

- `raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/Study/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf`
- `raw/Study/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
- `raw/Study/7. Ci&CD/교육 자료/CI&CD(SpringBoot_실습).pdf`
