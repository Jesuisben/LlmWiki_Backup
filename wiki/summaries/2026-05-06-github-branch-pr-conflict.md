---
title: 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [ci-cd, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결

## 한 줄 요약

팀장/팀원 역할로 branch를 만들고 push한 뒤 GitHub Pull Request로 master에 병합하고, pull/fetch와 충돌 해결·rebase 선택지를 실습한 날이다.

## 배운 내용

- IntelliJ에서 GitHub 저장소를 clone하고 팀원용 폴더 이름을 따로 지정했다.
- 로컬 저장소 안에서 사용자 이름과 이메일을 팀원 계정으로 설정했다.
- master에서 `animal`, `sport` branch를 만들고 checkout하여 서로 다른 기능 파일을 작성했다.
- GitHub에서 Pull Request를 만들고 title/description을 작성했다.
- PR 화면에서 충돌 없음 확인 후 `Merge pull request`와 `Confirm merge`로 병합했다.
- PR로 병합된 master는 로컬 IntelliJ에서 자동으로 최신화되지 않으므로 master checkout 후 pull해야 했다.
- `fetch`는 원격 branch 정보를 가져와 Remote 목록을 갱신하지만, 작업 파일에 바로 병합하지는 않는다는 점을 확인했다.
- 같은 `Main.java`나 `Cat.java`를 서로 다르게 수정하면 push가 거부되거나 merge/rebase 선택지가 나온다.
- IntelliJ conflict 화면에서 Accept Yours, Accept Theirs, Merge 선택지를 보고 수동 병합을 연습했다.

## 핵심 실습 / 예제

```bash
git config user.name "developer"
git config user.email "developer@daum.net"
# IntelliJ에서 branch 생성: animal, sport
# branch에서 파일 작성 → commit → push
# GitHub에서 Pull Request 생성 → Merge pull request → Confirm merge
# 로컬 master checkout → pull
# Git → Fetch로 원격 branch 정보 갱신
```

## 왜 중요한가

실무 협업에서는 master/main에 바로 push하기보다 기능 branch에서 작업하고 Pull Request로 검토·병합하는 흐름이 일반적이다. 이 날은 팀 프로젝트와 CI/CD로 가기 전 Git 협업의 기본 규칙을 익힌 단계다.

## 헷갈린 점 / 질문

- checkout은 현재 작업 branch를 바꾸는 동작이며, branch에 따라 실제 폴더에 보이는 파일도 달라질 수 있다.
- Pull Request는 코드를 올리는 행위가 아니라, 이미 push된 branch를 기준 branch에 병합해 달라고 요청하는 절차다.
- fetch는 원격 정보를 가져오기만 하고, pull은 가져온 뒤 현재 branch에 병합까지 한다.
- conflict는 Git이 자동으로 한쪽을 고를 수 없을 때 생긴다. 같은 파일의 같은 근처를 여러 사람이 수정하면 자주 발생한다.
- rebase는 히스토리를 재배치하는 방식이라 초보 협업에서는 의미를 알고 조심해서 써야 한다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]

## 출처

- `raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf` — p.78~97 IntelliJ 협업/branch, p.108~128 PR, pull/fetch, conflict 흐름
