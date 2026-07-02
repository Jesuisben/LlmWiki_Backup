---
title: GitHub 협업 흐름
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [ci-cd, project]
sources:
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# GitHub 협업 흐름

## 정의

GitHub 협업 흐름은 각자 로컬에서 branch를 만들고 작업한 뒤 원격 저장소에 push하고, Pull Request로 변경 내용을 검토·병합하며, 병합된 기준 branch를 다시 pull해 최신 상태로 맞추는 절차다.

## 수업에서 배운 큰 흐름

1. Git Bash 또는 IntelliJ/SourceTree에서 저장소를 준비한다.
2. 사용자 이름과 이메일을 설정한다.
3. 파일을 수정하고 `add → commit`으로 변경 이력을 만든다.
4. 원격 저장소에 `push`한다.
5. GitHub에서 Pull Request를 만든다.
6. 기준 branch에 merge한다.
7. 로컬 master/main에서 pull해 병합 결과를 가져온다.
8. 같은 파일 수정 시 conflict를 해결한다.

## 개인 작업 명령 흐름

```bash
git init
git status
git config user.name "bluesky"
git config user.email "bluesky@naver.com"
git add myfile.txt
git commit -m "message"
git remote add origin https://github.com/계정/저장소.git
git push -u origin master
git pull
git clone https://github.com/계정/저장소.git yellowbridge
git fetch
```

## Pull Request의 의미

Pull Request는 단순 업로드가 아니다. branch에 올린 변경을 기준 branch에 합쳐도 되는지 요청하고, 리뷰·테스트·충돌 확인을 거쳐 병합하는 협업 절차다.

## 수업 시나리오

- 팀장은 `master`에서 프로젝트를 만들고 `animal` branch를 만들어 `Cat`, `Dog` 클래스를 추가했다.
- 팀원은 clone 후 `sport` branch를 만들어 `Baseball`, `Football` 클래스를 추가했다.
- 각 branch를 GitHub에 push하고 PR을 만들어 master에 병합했다.
- GitHub에서 병합된 결과는 로컬 IntelliJ에 자동 반영되지 않으므로 master checkout 후 pull이 필요했다.
- 같은 `Main.java` 또는 `Cat.java`를 서로 다르게 수정하면 push가 거부되고 merge/rebase 또는 수동 conflict 해결이 필요했다.

## SourceTree/IntelliJ와 Git 명령의 관계

SourceTree와 IntelliJ Git UI는 Git을 대체하지 않는다. 내부적으로는 `git add`, `git commit`, `git push`, `git pull`, `git fetch`, merge 같은 Git 동작을 GUI 버튼으로 실행한다. 따라서 GUI를 쓰더라도 stage/commit/push/pull/branch/PR의 의미를 알아야 한다.

## 자주 헷갈리는 점

- push는 commit된 변경만 원격으로 보낸다.
- fetch는 원격 branch 정보를 가져오지만 현재 작업 파일을 바로 바꾸지 않는다.
- pull은 fetch 후 현재 branch에 병합까지 진행한다.
- clone은 원격 저장소 전체를 새 로컬 작업 폴더로 복제하는 초기 작업이다.
- conflict는 Git이 자동으로 한쪽을 고를 수 없을 때 생긴다.
- rebase는 히스토리를 재배치하는 작업이라 협업 초반에는 의미를 알고 조심해야 한다.

## 관련 수업

- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04 GitHub, Git Bash, SourceTree 협업 입문]]
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]

## 출처

- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf` — Git 초기화, SourceTree, branch, PR, pull/fetch, conflict 실습
