---
title: Git
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
status: stable
confidence: high
---

# Git

## 무엇인가

Git은 소스 코드 변경 이력을 기록하고 되돌리거나 공유할 수 있게 하는 분산 버전 관리 시스템이다.

## 이 위키에서의 맥락

Java 첫 주에는 개인 실습 프로젝트를 Git 저장소로 만들며 등장했다. Linux 과목 후반부에는 Git Bash, SourceTree, GitHub branch/PR/conflict를 통해 팀 협업 흐름으로 확장됐다.

## 핵심 기능 / 특징

- `git init`: 현재 폴더를 저장소로 초기화.
- `git status`: 변경 상태 확인.
- `git add`: commit 대상 stage.
- `git commit`: 변경 이력 저장.
- `git remote`: 원격 저장소 연결.
- `git push`: 로컬 commit을 원격으로 업로드.
- `git pull`: 원격 변경을 로컬 branch에 반영.
- branch/merge/conflict: 협업의 핵심 흐름.

## 학습 이력

- [[summaries/2026-02-27-github-initial-setup|2026-02-27 GitHub 초기 설정]]: Java 프로젝트 Git 초기화.
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]]: Git Bash와 SourceTree로 기본 흐름 복습.
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]]: branch, PR, conflict 해결.

## 관련 개념

- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]

## 5과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/5. Linux` 날짜별 MD 10개와 `Linux 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 명령어 사전이 아니라 VM/SSH/CLI → 파일·권한 → Spring Boot jar 실행 → Docker network/volume/Dockerfile/Compose → GitHub branch/PR/conflict 흐름 속에서 읽어야 한다.
- 운영 관점에서는 코드보다 IP/포트/방화벽/권한/컨테이너 네트워크·볼륨이 문제 원인일 수 있음을 함께 기억한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
