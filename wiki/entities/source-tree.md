---
title: SourceTree
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [github, ci-cd]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf
status: stable
confidence: high
---

# SourceTree

## 무엇인가

SourceTree는 기존 Git repository의 working tree·stage·commit history·local/remote branch를 표시하고 Git 동작을 GUI로 실행하는 client다. 파일 내용을 편집하는 editor도, repository hosting service도, Git 자체도 아니다.

## 이 위키에서의 맥락

2026-05-04 Git Bash에서 `status`·`add`·`commit`·`push`를 먼저 확인한 뒤, 같은 두 local repository를 SourceTree 관리 목록에 추가했다. SourceTree 화면으로 stage·commit·push·pull과 history를 따라가고, 두 작업자가 같은 파일을 다르게 바꿨을 때 remote가 앞서 발생한 push 거부와 수동 통합 흐름을 경험했다.

05-06의 branch·PR·fetch·merge/rebase는 IntelliJ와 GitHub 화면에서 수행했다. 이 결과를 SourceTree 버튼으로 실행한 것처럼 합치지 않는다.

## 화면 동작과 Git 상태 대응

| SourceTree에서 한 일 | 입력 상태 | Git 상태 변화 | 완료 확인 |
|---|---|---|---|
| local repository 추가 | 이미 `.git`이 있는 directory | repository 내용은 바꾸지 않고 client에 등록 | History와 현재 branch가 표시됨 |
| 변경 파일 확인 | modified `myfile.txt`, untracked `somefile.txt` | 읽기만 함 | working tree 항목이 구분됨 |
| stage | 선택한 working tree 변경 | staging area에 추가 | staged/unstaged 목록 이동 |
| commit | staged 변경과 message | local repository에 commit 생성 | History에 새 commit 표시 |
| push | local `master`의 새 commit | GitHub remote `master` 갱신 | remote와 branch 상태 확인 |
| pull | 두 번째 local의 뒤처진 `master` | fetch 후 local branch에 통합 | 새 `somefile.txt`와 수정된 `myfile.txt` 확인 |
| branch·checkout 관찰 | R09 후반 IntelliJ의 `master`·`animal` | checkout한 commit에 맞게 working tree 전환 | 활성 branch·파일 구성이 달라짐; SourceTree 실행 결과로 합치지 않음 |
| conflict 처리 | local과 remote의 겹치는 변경 | 사람이 결과를 선택하고 stage·commit | unresolved 항목 제거와 후속 push 확인 |

## 2026-05-04 두 작업자 흐름

1. Git Bash로 만든 첫 번째·두 번째 local repository를 각각 SourceTree에 추가했다.
2. 첫 번째 local에서 `myfile.txt`를 수정하고 `somefile.txt`를 만들었다.
3. SourceTree에서 두 변경을 stage하고 message와 함께 commit한 뒤 push했다.
4. 두 번째 local은 pull하여 새 파일과 수정 내용을 받았다.
5. 두 local에서 같은 `myfile.txt`의 끝을 서로 다르게 고치고 각각 commit했다.
6. 먼저 push한 변경으로 remote `master`가 앞섰고, 뒤 작업자의 push가 거부됐다.
7. 뒤 작업자는 remote 변경을 먼저 받아 local 변경과 합치고, 최종 내용을 직접 편집·stage·commit한 뒤 다시 push해야 했다.

push 거부, conflict 표시, conflict 해결, 통합 commit, 재push는 각각 다른 상태다. SourceTree가 자동으로 어느 문장을 남길지 결정했다고 해석하지 않는다.

## SourceTree가 보여 주는 것과 하지 않는 것

- History는 local commit graph와 선택한 ref의 관계를 시각화한다.
- staged/unstaged 목록은 working tree와 staging area의 차이를 보여 준다.
- local/remote branch 표시는 branch 위치를 관찰하게 하지만 remote branch와 local branch를 자동으로 같은 상태로 만들지는 않는다.
- Push·Pull 버튼은 Git 동작을 실행하지만 Git의 commit·branch·remote 규칙을 대체하지 않는다.
- GitHub 계정 연동은 remote 접근을 돕지만 Pull Request review·merge는 GitHub의 협업 기능이다.
- conflict UI가 있더라도 최종 source 의미 판단과 검증은 사람이 한다.

## IntelliJ와의 경계

05-04 SourceTree는 `myfile.txt`·`somefile.txt`와 두 local repository의 stage/commit/push/pull·conflict에 사용됐다. 05-06 IntelliJ는 `Main.java`·`Cat.java`, `animal`·`sport`, fetch와 merge/rebase 선택에 사용됐다. 두 도구는 모두 Git client지만 화면 동작과 관찰된 결과를 서로 바꾸어 기록하지 않는다.

## 학습 이력

- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]] — 설치·계정 연동, local repository 등록, stage·commit·push·pull·history·conflict
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]] — IntelliJ/GitHub 협업과 SourceTree의 책임 경계

## 관련 개념

- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/intellij-idea|IntelliJ IDEA]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md` — IntelliJ와의 경계
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf` — SourceTree P.35~60의 화면 절차 보조

날짜 MD의 실제 파일·작업자·오류·결과를 우선했다. PDF의 계정 연결 화면은 절차 보조로만 사용했고 실제 account·email·repository URL·OAuth/PAT·credential은 재노출하지 않았다.