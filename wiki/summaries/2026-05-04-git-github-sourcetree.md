---
title: 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [github, ci-cd, project, curriculum]
sources:
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문

## 한 줄 요약

Linux/Docker 배포 흐름 뒤에 GitHub 협업 흐름을 복습하며, Git Bash 명령과 SourceTree GUI로 init/add/commit/push/pull/clone을 실습한 날이다.

## 배운 내용

- Git 저장소 초기화와 사용자 정보 설정을 복습했다.
- `status → add → commit → remote → push` 흐름으로 로컬 변경을 GitHub에 올렸다.
- `pull`과 `clone`의 사용 시점을 구분했다.
- SourceTree에서 local repository를 추가하고 stage/commit/push/pull을 GUI로 수행했다.
- CLI와 GUI가 다른 도구처럼 보이지만 내부적으로 같은 Git 동작을 실행한다는 점을 이해했다.

## 핵심 개념

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[entities/git|Git]], [[entities/github|GitHub]], [[entities/source-tree|SourceTree]]

## 실습 / 예제

```bash
git init
git status
git config user.name "사용자명"
git config user.email "이메일"
git add myfile.txt
git commit -m "first commit"
git remote add origin https://github.com/계정/저장소.git
git push -u origin master
git pull
git clone https://github.com/계정/저장소.git
```

## 헷갈린 점 / 질문

- Git은 내 컴퓨터의 버전 관리 도구이고, GitHub는 원격 저장소/협업 서비스다.
- SourceTree는 Git을 대체하는 것이 아니라 Git 명령을 GUI로 실행하게 해 주는 도구다.
- `clone`은 처음 받을 때, `pull`은 이미 받은 저장소를 최신화할 때 사용한다.
- push 전에는 반드시 어떤 파일이 stage/commit 되었는지 확인해야 한다.

## 관련 페이지

- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]

## 출처

- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
