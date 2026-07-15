---
title: GitHub
created: 2026-07-02
updated: 2026-07-15
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

- [[summaries/2026-02-27-github-initial-setup|2026-02-27]]: `MyJava` 원격 저장소를 준비하고 로컬 Git·IntelliJ와 연결하는 첫 흐름.
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]]: GitHub 원격 저장소와 SourceTree 연동.
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]]: branch/PR/merge/conflict 협업.
- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11]]: GitHub Actions 기반 CI/CD로 확장.

## 구현 역할과 설명 관점

- **Java 수업의 직접 역할:** 개인 Java 실습 저장소를 원격에 두기 위한 서비스로 처음 사용했다.
- **후속 협업·자동화 역할:** branch/PR 검토 공간을 거쳐 GitHub Actions의 push trigger와 Secrets 관리 지점으로 확장됐다.
- **프로젝트/면접 관점:** GitHub를 Git 자체와 동일시하지 않고, Git 저장소 호스팅·리뷰·협업·자동화를 제공하는 서비스라고 설명한다.

## 관련 개념

- [[entities/git|Git]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]

## 최신 원본 대조

2026-05-04의 remote repository, 05-06의 Pull Request·merge·activity·branch 협업을 명시해 GitHub를 백업 장소가 아니라 검토·합의·공유 공간으로 정리했다. 이어 2026-05-11에는 `master` push가 GitHub Actions의 trigger가 되고, Repository Secrets가 Docker Hub 인증·EC2 접속 정보·image/container 이름을 workflow에 안전하게 전달하는 출발점이 되었다. GitHub는 build와 배포 자동화의 제어면으로도 확장된다.

## 출처

- `raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md`
