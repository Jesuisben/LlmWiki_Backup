---
title: 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [ci-cd, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문

## 한 줄 요약

Git Bash에서 `init → status → config → add → commit → remote → push/pull/clone` 흐름을 복습하고, SourceTree GUI로 Git 상태와 commit/push/pull을 시각적으로 다룬 날이다.

## 배운 내용

- Git 설치 경로에서 `git-bash.exe`와 `git.exe`의 역할을 구분했다.
- Git Bash는 Windows 위에서 Linux식 명령을 쓸 수 있는 터미널처럼 사용했다.
- `git init`으로 `.git` 디렉터리를 만들고, work tree를 Git 저장소로 초기화했다.
- `git status`로 untracked/staged/committed 상태를 확인했다.
- `git config user.name`, `git config user.email`로 커밋 작성자 정보를 저장했다.
- `git add`, `git commit`, `git diff`, `git log`, `git remote add origin`, `git push -u origin master`를 실습했다.
- GitHub 웹에서 파일을 만들고 `git pull`로 로컬에 가져왔다.
- `git clone <url> <새폴더>`로 같은 원격 저장소를 다른 작업 폴더에 복제했다.
- SourceTree를 설치하고 Git 저장소 추가, history, staging, commit, push, pull을 GUI로 확인했다.
- 서로 다른 폴더/사용자가 같은 파일을 수정하면 push 거부와 merge 필요 상황이 생긴다는 것을 봤다.

## 핵심 실습 / 예제

```bash
mkdir GitTest
cd GitTest
mkdir bluerain
cd bluerain
git init
git config user.name "bluesky"
git config user.email "bluesky@naver.com"
git status
git add myfile.txt
git commit -m "myfile committed"
git diff
git remote add origin https://github.com/Jesuisben/git_bluerain.git
git push -u origin master
git pull
git clone https://github.com/Jesuisben/git_bluerain.git yellowbridge
```

## 왜 중요한가

이 날은 단순히 개인 저장소를 push하는 수준에서 벗어나, 여러 작업 폴더와 원격 저장소를 오가며 협업의 기본 단계를 연습했다. 다음 수업의 branch, Pull Request, conflict 해결로 이어진다.

## 헷갈린 점 / 질문

- push는 commit된 변경만 원격으로 보낸다. 수정만 하거나 stage만 한 파일은 push 대상이 아니다.
- `git commit -am`은 이미 추적 중인 수정 파일에는 편하지만, 새 파일은 별도 `git add`가 필요하다.
- `-u origin master`는 로컬 master와 원격 origin/master의 추적 관계를 잡아 다음부터 `git push`만으로 동작하게 한다.
- SourceTree는 Git을 대체하는 도구가 아니라 Git 명령을 GUI로 실행하게 해 주는 도구다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]

## 출처

- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf` — p.2~14 Git 설치/초기화/status, p.31~35 clone/SourceTree, p.52~62 SourceTree/pull
