---
title: GitHub 협업 흐름
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [github, ci-cd, project]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf
status: stable
confidence: high
---

# GitHub 협업 흐름

## 정의

Git·GitHub 협업은 한 작업자의 파일을 곧바로 팀 기준 branch에 덮어쓰는 일이 아니다. 각 local repository에서 변경을 stage·commit하고 작업 branch를 remote에 push한 뒤, GitHub Pull Request로 차이를 검토·merge하고 각자의 local 기준 branch를 다시 최신화하는 상태 전이이다.

## 왜 중요한가

화면에서 “Push”, “Create pull request”, “Merge”가 모두 성공해 보여도 서로 다른 artifact가 바뀐다. 이 차이를 모르면 GitHub에는 파일이 있는데 local에는 없거나, branch push를 `master` 반영으로 오해하거나, push 거부를 곧바로 파일 conflict와 같은 현상으로 해석하기 쉽다.

## 협업 artifact와 상태

| artifact | 위치와 책임 | 이 수업에서 확인한 상태 |
|---|---|---|
| working tree | 현재 checkout한 commit을 바탕으로 실제 파일을 편집하는 공간 | untracked·modified·clean |
| staging area | 다음 commit에 넣을 변경을 선택한 영역 | `add` 전후 `status`로 구분 |
| commit | local repository에 저장된 변경 이력 | commit hash·message와 clean 상태 확인 |
| local branch | 한 local repository에서 commit을 가리키는 작업선 | `master`, 팀장 `animal`, 팀원 `sport` |
| remote branch | GitHub remote repository에 공유된 branch | push 뒤 GitHub와 IDE의 Remote 목록에서 확인 |
| remote-tracking branch | fetch로 갱신되는 local의 remote branch 관찰 지점 | `origin/sport`를 확인한 뒤 별도 local branch 생성 |
| Pull Request | GitHub에서 base와 compare branch의 차이·검토·merge 이력을 묶는 협업 단위 | `animal`·`sport` PR을 각각 생성·확인·merge |
| merge 결과 | 둘 이상의 이력을 통합한 commit과 파일 상태 | remote `master`가 먼저 바뀌고, local `master`는 pull 뒤 바뀜 |

## 2026-05-04 — 기본 상태 전이와 두 작업자 실습

### Git Bash에서 local→remote

1. 빈 directory에서 `git init`을 실행해 `.git`과 working tree를 만들었다.
2. `git status`로 commit 없는 상태, 새 파일의 untracked 상태를 확인했다.
3. `git add` 뒤 staged 상태, `git commit` 뒤 local commit과 clean 상태를 확인했다.
4. remote를 연결하고 local `master`를 push했다. 출력에서 remote의 새 `master`와 upstream 연결을 확인했으므로 이 시점에만 push 성공이다.
5. GitHub에서 만든 `hello.txt`는 remote commit이므로 local에는 자동으로 생기지 않았다. pull 뒤 local 파일을 확인했다.
6. commit하지 않은 working tree·staging area 변경이 있어도 push 자체는 오류 없이 끝났고, remote로 전송된 것은 이미 존재하던 local commit뿐이었다.
7. `clone`으로 두 번째 local repository를 만들고 작업자별 작성자 설정을 분리했다.

### SourceTree 두 작업자와 conflict

첫 local repository에서 `myfile.txt` 수정과 `somefile.txt` 생성을 SourceTree로 stage·commit·push했다. 두 번째 local repository는 pull하여 새 파일과 수정 내용을 받았다. 이후 두 local에서 같은 파일을 다르게 commit하자 뒤늦게 push한 쪽이 remote가 앞서 있다는 이유로 거부됐다.

이 거부는 아직 최종 conflict 해결이 아니다. 먼저 remote 이력과 local 이력을 통합하고, 겹치는 내용은 사람이 선택한 뒤 stage·commit·push해야 remote가 갱신된다. SourceTree는 이 Git 상태를 GUI로 조작했을 뿐 repository나 merge 판단을 대신하지 않았다.

### branch 협업 시작

팀장은 IntelliJ에서 `master`를 기준으로 `animal` branch를 만들고 Cat·Dog class를 commit·push했다. checkout할 때 working tree의 파일 구성이 branch commit에 맞게 달라지는 것을 IDE와 실제 directory에서 확인했다. 마지막에는 collaborator 초대까지 진행했지만 PR merge는 다음 수업일의 별도 단계다.

## 2026-05-06 — branch→PR→merge→local 최신화

### 팀원 준비와 첫 push 거부

팀원은 IntelliJ의 Project from Version Control로 repository를 별도 local directory에 clone했다. 팀원 변경이 먼저 remote `master`에 push된 뒤 팀장이 자신의 뒤처진 local `master`에서 같은 `Main.java`를 다르게 고쳐 push하자 거부됐다. IntelliJ의 3-way merge 화면에서 local·remote·결과를 비교해 수동으로 적용했다.

### `animal`·`sport` Pull Request

1. 팀원은 local `master`에서 `sport` branch를 만들고 Baseball·Football class를 commit·push했다.
2. GitHub에서 팀장의 `animal`을 compare, `master`를 base로 PR을 생성했다.
3. 다른 계정에서 변경과 “base branch와 conflict 없음”을 확인했다.
4. Merge pull request와 Confirm merge 뒤 PR이 merged·closed 상태가 되고 remote `master`에 Cat·Dog가 반영됐다.
5. 같은 흐름으로 팀원의 `sport` PR을 만들고 팀장이 검토·merge해 remote `master`에 Baseball·Football을 반영했다.
6. PR merge 뒤에도 두 사람의 local `master`에는 파일이 자동으로 생기지 않았다. 각자 local `master`를 checkout하고 pull한 뒤 최신 파일을 받았다.

### fetch와 local branch 생성

fetch는 remote branch 정보를 갱신해 IDE의 Remote 목록에 `origin/sport`가 보이게 했다. 그 remote-tracking branch를 기준으로 새 local branch를 만드는 동작은 별도였다. fetch 성공만으로 현재 branch·working tree가 `sport` 내용으로 바뀐 것은 아니다.

### `Cat.java` conflict와 merge/rebase 경계

팀장 push 뒤 팀원이 같은 `Cat.java` 부분을 다르게 수정해 push했을 때 IDE가 Merge 또는 Rebase를 제시했다. 원본에는 Rebase를 선택하면 현재 push가 취소되고, 변경을 새 기준 위에서 정리한 뒤 다시 push한 흐름이 기록돼 있다.

- merge는 갈라진 이력을 합치며 해결 결과를 새 merge 이력으로 남기는 선택이다.
- rebase는 local 변경을 새 remote 기준 위에 다시 적용하는 선택이다.
- 둘 다 어느 코드를 남길지 자동 결정하지 않는다.
- 이날은 IntelliJ 선택·해결 범위만 확인했다. CLI rebase 세부 명령, interactive rebase, force push 정책을 실행한 것으로 확대하지 않는다.

## 명령별 입력 → 처리 → 결과

| 동작 | 입력 상태 | 처리 | 직접 결과 |
|---|---|---|---|
| `add` | working tree의 untracked·modified 변경 | 다음 commit 대상을 선택 | staging area가 바뀌고 remote는 그대로 |
| `commit` | staged 변경 | local history에 snapshot 기록 | local branch가 새 commit을 가리키고 remote는 그대로 |
| `push` | local branch의 remote에 없는 commit | remote branch로 object·ref 전송 | remote branch 갱신; PR·base merge는 아직 아님 |
| `fetch` | remote의 새 ref·object | remote 정보 다운로드 | remote-tracking branch 갱신; 현재 branch·working tree는 자동 통합되지 않음 |
| `pull` | 현재 branch와 연결된 remote branch | fetch 후 현재 branch에 통합 | local branch와 working tree가 바뀔 수 있음 |
| `merge` | 갈라진 두 branch 이력 | 공통 base 이후 변경을 통합 | fast-forward 또는 merge commit; 겹치면 수동 해결 필요 |
| `rebase` | local commit과 새 기준 commit | local commit을 새 기준 위에 재적용 | commit 기반이 바뀌며 겹치면 수동 해결 필요 |
| `clone` | remote repository | history·branch·working tree를 새 directory에 복제 | 별도 local repository와 remote 연결 생성 |

## 완료 조건을 따로 확인하기

| 단계 | 완료 증거 | 아직 완료되지 않은 것 |
|---|---|---|
| push 성공 | remote branch 갱신 출력과 GitHub branch의 commit 확인 | PR 생성·base branch merge |
| PR 생성 | 열린 PR과 base/compare 차이 확인 | review·merge |
| PR merge | merged·closed 상태와 remote `master` 파일·history 확인 | 각 local `master` 최신화 |
| local `master` 최신화 | `master` checkout 후 pull, 파일·history 확인 | 다른 작업 branch checkout |
| fetch 성공 | Remote 목록·remote-tracking branch 갱신 | local branch 생성·working tree 전환 |
| conflict 해결 | 최종 내용 선택, unresolved 상태 제거, 통합 commit과 후속 push 확인 | 팀 정책상 검토·PR 완료 |

## 도구와 과목 경계

- [[entities/git|Git]]은 working tree·stage·commit·branch·fetch/merge/rebase 상태를 관리한다.
- [[entities/github|GitHub]]는 remote repository hosting과 branch 공유, PR review·merge 화면을 제공한다.
- [[entities/source-tree|SourceTree]]와 [[entities/intellij-idea|IntelliJ IDEA]]는 Git 상태를 조작·표시하는 서로 다른 client다. 05-04 SourceTree 결과와 05-06 IntelliJ 결과를 같은 화면 실습으로 합치지 않는다.
- Java 단계에서는 개인 `MyJava` local/remote 연결을 먼저 배웠다. Linux 05-04~05-06에는 두 작업자 branch·PR·conflict로 확장했다.
- [[concepts/github-actions-workflow|GitHub Actions workflow]]는 후속 CI/CD에서 push를 trigger로 사용한다. Linux 수업의 push·PR 성공이 workflow build·deploy 성공을 뜻하지 않는다.

## 자주 헷갈리는 점

- local branch, remote branch, remote-tracking branch는 같은 이름처럼 보여도 위치와 갱신 시점이 다르다.
- push 거부는 remote history가 앞섰다는 신호일 수 있고, 실제 내용 conflict는 이력을 통합하는 과정에서 판정된다.
- branch push, PR 생성, PR merge, local pull은 네 개의 별도 완료 상태다.
- checkout은 branch 이름만 바꾸는 표시가 아니라 working tree를 해당 commit 상태에 맞춘다.
- PR은 Git 명령이 아니라 GitHub의 검토·합의 artifact다.

## 관련 개념

- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04 Git 상태 전이와 SourceTree]]
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 branch·PR·conflict]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — 복습 허브
- `raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf` — Git Bash P.11~31, SourceTree P.35~60, branch·PR·conflict P.62~131의 화면 절차 보조

날짜별 MD의 실제 교시·artifact·성공 결과를 우선했다. PDF는 화면 절차를 보조했으며 실제 account·email·repository URL·credential은 일반화하거나 생략했다.