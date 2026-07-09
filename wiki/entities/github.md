---
title: GitHub
created: 2026-07-02
updated: 2026-07-09
type: entity
tags: [github, ci-cd]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf
  - raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
status: stable
confidence: high
---

# GitHub

## 무엇인가

GitHub는 Git 저장소를 온라인에 보관하고, 다른 사람과 코드 이력과 변경 사항을 공유하는 개발 협업 서비스다.

## 이 위키에서의 맥락

Java 수업 초기에 `MyJava` 원격 저장소를 만들며 처음 등장했다. Linux 과목에서는 Git Bash/SourceTree를 통해 branch, Pull Request, merge, conflict 같은 팀 협업 흐름을 학습했고, 이후 CI/CD에서는 GitHub Actions의 트리거가 된다.

## 핵심 기능 / 특징

- 원격 repository 생성과 관리.
- local Git 저장소와 remote URL 연결.
- push/pull/clone을 통한 코드 공유.
- branch, Pull Request, merge로 팀 협업.
- conflict 해결 흐름 지원.
- GitHub Actions와 Repository Secrets를 통한 CI/CD 확장.

## 학습 이력

- [[summaries/2026-02-27-github-initial-setup|2026-02-27]]: Java 실습 저장소 준비.
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]]: GitHub 원격 저장소와 SourceTree 연동.
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]]: branch/PR/merge/conflict 협업.
- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11]]: GitHub Actions 기반 CI/CD로 확장.

## 관련 개념

- [[entities/git|Git]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]

## 5과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/5. Linux` 날짜별 MD 10개와 `Linux 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 명령어 사전이 아니라 VM/SSH/CLI → 파일·권한 → Spring Boot jar 실행 → Docker network/volume/Dockerfile/Compose → GitHub branch/PR/conflict 흐름 속에서 읽어야 한다.
- 운영 관점에서는 코드보다 IP/포트/방화벽/권한/컨테이너 네트워크·볼륨이 문제 원인일 수 있음을 함께 기억한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
