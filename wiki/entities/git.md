---
title: Git
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

- [[summaries/2026-02-27-github-initial-setup|2026-02-27 GitHub 초기 설정]]: `MyJava` 폴더에서 사용자 정보와 `safe.directory`를 설정하고 `git init`으로 로컬 저장소를 시작했다.
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]]: Git Bash와 SourceTree로 기본 흐름 복습.
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]]: branch, PR, conflict 해결.

## 구현 역할과 설명 관점

- **Java 수업의 직접 역할:** 실습 코드가 있는 로컬 폴더를 변경 이력 관리 대상으로 만드는 출발점. 이때 `git init`과 GitHub 업로드는 같은 작업이 아니었다.
- **후속 협업 역할:** Linux 과목에서 staging·commit·remote·branch·merge·conflict로 확장됐다.
- **프로젝트/면접 관점:** Git은 파일 공유 서비스가 아니라 변경 이력과 분기·병합을 관리하는 도구라고 설명하고, GitHub와 구분할 수 있어야 한다.

## 관련 개념

- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]

## 최신 원본 대조

2026-05-04의 working tree/staging/local commit/remote push와 05-06의 branch·merge·rebase·PR 연결을 보강했다. SourceTree는 같은 Git 상태를 GUI로 보여 주는 도구다.

## 출처

- `raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
