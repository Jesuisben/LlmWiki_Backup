---
title: git fetch vs pull vs clone
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [ci-cd, project]
sources:
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# git fetch vs pull vs clone

## 비교 목적

GitHub 협업 수업에서 `clone`, `pull`, `fetch`가 모두 등장했다. 셋 다 “원격 저장소에서 뭔가 가져오는” 명령처럼 보이지만, 쓰는 시점과 결과가 다르다.

## 한눈에 보기

| 명령 | 언제 쓰나 | 결과 |
|---|---|---|
| `git clone` | 처음 원격 저장소를 내 컴퓨터에 받을 때 | 새 로컬 저장소/작업 폴더 생성 |
| `git fetch` | 원격 branch/commit 정보를 확인하고 싶을 때 | 원격 추적 정보만 갱신, 작업 파일은 그대로 |
| `git pull` | 현재 branch에 원격 변경을 반영하고 싶을 때 | fetch 후 merge/rebase로 작업 파일까지 갱신 |

## 수업 예제

```bash
git clone https://github.com/Jesuisben/git_bluerain.git yellowbridge
```

`bluerain` 저장소를 `yellowbridge`라는 새 폴더로 복제하는 초기 작업이다.

```bash
git pull origin master
```

GitHub 또는 다른 작업자가 master에 push한 변경을 현재 로컬 branch에 가져와 합친다.

```bash
git fetch
```

GitHub에 새로 생긴 `origin/sport` 같은 원격 branch 정보를 IntelliJ Git 뷰에 보이게 갱신한다. 작업 파일은 바로 바뀌지 않는다.

## 언제 무엇을 쓰는가

- 프로젝트를 처음 받을 때는 `clone`.
- 이미 clone한 프로젝트에서 최신 master 변경을 내 작업 폴더에 반영할 때는 `pull`.
- 원격에 어떤 branch/commit이 생겼는지 먼저 확인하고 싶을 때는 `fetch`.

## 헷갈리기 쉬운 포인트

- `pull`은 작업 파일을 바꿀 수 있으므로, 내 수정사항이 있으면 충돌이 날 수 있다.
- `fetch`는 안전하게 원격 정보만 가져오므로, 바로 파일이 바뀌지는 않는다.
- `clone`은 기존 저장소 안에서 매번 하는 명령이 아니라, 새 작업 폴더를 만드는 초기 복제 명령이다.
- SourceTree/IntelliJ의 Pull/Fetch 버튼도 내부적으로 같은 Git 동작을 수행한다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04 GitHub, Git Bash, SourceTree 협업 입문]]
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]

## 출처

- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf` — clone, pull, fetch, branch/PR 실습
