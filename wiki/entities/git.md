---
title: Git
created: 2026-06-30
updated: 2026-07-02
type: entity
tags: [curriculum, project, ci-cd]
sources:
  - raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# Git

## 무엇인가

Git은 소스 코드와 프로젝트 파일의 변경 이력을 기록하는 분산 버전 관리 시스템이다. 언제 어떤 파일이 어떻게 바뀌었는지 남기고, 필요하면 이전 상태로 돌아가거나 여러 작업 흐름을 branch로 나눠 관리할 수 있다.

## 이 위키에서의 맥락

국비지원 과정 초반 Java 프로젝트를 만들면서 `D:/java_project/MyJava` 폴더를 Git으로 관리하고 GitHub 원격 저장소와 연결하기 위해 처음 등장했다. Linux 과목 후반에는 Git Bash, SourceTree, IntelliJ Git UI, branch, Pull Request, conflict를 통해 팀 협업 도구로 다시 등장했다.

## 핵심 기능 / 특징

- 변경 이력 관리: 파일 변경사항을 commit 단위로 기록한다.
- 로컬 저장소: 내 컴퓨터의 프로젝트 폴더 안에서 버전 관리를 수행한다.
- 원격 저장소 연결: [[entities/github|GitHub]] 같은 서비스에 저장소를 올려 백업/공유할 수 있다.
- branch: 기능이나 작업 흐름을 분리한다.
- merge/rebase: 서로 다른 작업 흐름을 합치거나 히스토리를 재배치한다.
- conflict 해결: 같은 파일의 같은 근처를 여러 사람이 수정했을 때 수동으로 조정한다.

## 학습 이력

- [[summaries/2026-02-27-github-initial-setup|2026-02-27]]: Git 설치 경로 확인, Java 프로젝트 폴더 이동, `safe.directory`, `user.name`, `user.email`, `git init` 흐름.
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]]: Git Bash로 `init/status/add/commit/push/pull/clone` 흐름과 SourceTree 사용.
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]]: branch, checkout, Pull Request, merge, fetch, pull, conflict/rebase 실습.

## 핵심 명령어

```bash
git init
git status
git config user.name "bluesky"
git config user.email "bluesky@naver.com"
git add -A
git commit -m "message"
git diff
git log
git remote add origin https://github.com/계정/저장소.git
git push -u origin master
git pull
git clone <repo-url> <new-folder>
git fetch
```

## 관련 개념

- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[summaries/2026-02-27-github-initial-setup|2026-02-27 GitHub 초기 설정]]

## 출처

- `raw/Study/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf`
