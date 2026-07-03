---
title: Git
created: 2026-07-02
updated: 2026-07-03
type: entity
tags: [java, ci-cd]
sources:
  - raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/Study/1. Java/교육 자료/Github 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: stable
confidence: high
---

# Git

## 무엇인가

Git은 소스 코드 변경 이력을 기록하고 되돌리거나 공유할 수 있게 하는 분산 버전 관리 시스템이다.

## 이 위키에서의 맥락

Java 첫 주부터 `MyJava` 프로젝트를 Git 저장소로 만들며 사용했다. 이때는 개인 프로젝트 이력 관리가 중심이었고, 이후 Linux/GitHub 수업에서는 branch, pull, push, PR, conflict 같은 협업 흐름으로 확장된다.

## 핵심 기능 / 특징

- `git init`: 현재 폴더를 Git 저장소로 초기화
- `git config --global user.name/user.email`: 커밋 작성자 정보 설정
- `safe.directory`: 신뢰할 수 있는 작업 폴더 등록
- `.git` 폴더: Git 이력 데이터가 저장되는 내부 폴더
- `status`, `add`, `commit`, `push`, `pull`: 이후 협업 흐름의 기본 명령

## 학습 이력

- [[summaries/2026-02-27-github-initial-setup|2026-02-27 GitHub 초기 설정]]: Git 설치, 사용자 정보 설정, `git init`
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04 GitHub, Git Bash, SourceTree 협업 입문]]: Git 명령과 GUI 협업 도구 복습
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결]]: branch/PR/conflict 흐름

## 관련 개념

- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]

## 출처

- `raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/Study/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf`
