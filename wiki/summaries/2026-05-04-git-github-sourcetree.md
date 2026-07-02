---
title: 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [ci-cd, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
status: growing
confidence: high
---

# 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문

## 한 줄 요약

Git Bash에서 `init → status → config → add → commit → remote → push/pull/clone` 흐름을 다시 실습하고, SourceTree GUI로 같은 Git 작업을 수행하는 법을 배웠다.

## 배운 내용

- Git Bash는 Git 명령을 입력하는 터미널 환경으로 사용했다.
- `git init`으로 로컬 저장소를 만들고 `.git/config`를 확인했다.
- `git config user.name`, `git config user.email`로 커밋 작성자 정보를 설정했다.
- `git status`, `git add`, `git commit`, `git remote`, `git push -u origin master` 흐름을 실습했다.
- GitHub 웹에서 파일을 생성하고 로컬로 pull하는 상황을 다뤘다.
- 커밋하지 않은 변경은 push 대상이 아니라는 점을 확인했다.
- `git clone`으로 원격 저장소를 로컬에 복제했다.
- SourceTree 설치 후 commit, push, pull을 GUI로 수행했다.
- 서로 다른 폴더/사용자가 같은 원격 저장소를 사용하는 협업 상황을 준비했다.

## 핵심 실습 흐름

```bash
mkdir GitTest
cd GitTest
git init
git config user.name "bluesky"
git config user.email "bluesky@naver.com"
git status
git add myfile.txt
git commit -m "first commit"
git push -u origin master
```

## 왜 중요한가

2월 GitHub 초기 설정은 개인 프로젝트를 원격에 올리는 시작이었다면, 이 날은 팀 협업을 위한 pull/clone/SourceTree까지 확장한 복습이다. 다음 수업의 브랜치, PR, 충돌 해결로 이어진다.

## 헷갈린 점 / 질문

- push는 “현재 작업 폴더의 모든 파일”이 아니라 commit된 변경만 원격으로 보낸다.
- `-u`는 로컬 브랜치와 원격 브랜치의 기본 추적 관계를 잡아 다음 push/pull을 짧게 만들기 위한 옵션이다.
- SourceTree는 Git을 대체하는 것이 아니라 Git 명령을 GUI로 실행하게 해 주는 도구다.

## 관련 페이지

- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]

## 출처

- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
