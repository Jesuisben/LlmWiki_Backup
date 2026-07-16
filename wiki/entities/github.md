---
title: GitHub
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [github, ci-cd]
sources:
  - raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf
  - raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md
status: stable
confidence: high
---

# GitHub

## 무엇인가

GitHub는 Git repository를 원격에 hosting하고 branch 공유, 변경 비교, Pull Request review·merge, 활동 이력을 제공하는 협업 서비스다. local file·stage·commit을 직접 관리하는 Git 자체와는 책임이 다르다.

## 이 위키에서의 맥락

- **Java 선행:** 개인 Java 실습 repository를 원격에 두고 IntelliJ local project와 연결하는 용도로 처음 사용했다.
- **Linux 2026-05-04:** remote repository 생성·연결, push/pull/clone, collaborator 초대와 `animal` remote branch를 확인했다.
- **Linux 2026-05-06:** `animal`·`sport` branch를 Pull Request로 비교·검토·merge하고, remote `master`와 각 local `master`가 서로 다른 시점에 갱신됨을 확인했다.
- **CI/CD 후속:** 05-11부터 GitHub Actions workflow와 repository-level 설정이 사용된다. 이는 Linux PR 실습과 별도의 자동화 학습이다.

## Linux 수업에서 맡은 실제 역할

| 기능 | GitHub가 바꾼 것 | local에서 별도로 필요한 것 |
|---|---|---|
| remote repository | push·pull·clone의 공유 endpoint와 remote history | local repository 생성 또는 clone |
| branch 공유 | `animal`·`sport` remote branch 보존 | local branch commit·push |
| collaborator | 다른 계정이 repository에 접근하는 협업 입구 | local 작성자 설정·clone |
| Pull Request | base/compare 차이, 제목·설명, conflict 여부, review 기록 | 작업 branch의 commit·push |
| PR merge | remote `master`에 작업 branch 변경 통합 | 각 local `master` checkout·pull |
| activity/Insights | PR·merge 활동 확인 | local history 확인은 Git client에서 별도 |

## `animal`·`sport` 협업 artifact

1. 팀장은 `animal` remote branch에 Cat·Dog 변경을 push했다.
2. 팀원은 `sport` remote branch에 Baseball·Football 변경을 push했다.
3. `animal`→`master` PR을 만들고 다른 계정에서 conflict 없음과 변경을 확인한 뒤 merge했다.
4. PR이 merged·closed 상태가 되고 remote `master`에 Cat·Dog가 나타났다.
5. `sport`→`master` PR도 반대 역할로 생성·검토·merge해 remote `master`에 Baseball·Football을 반영했다.
6. 두 PR merge 뒤에도 local `master`는 자동으로 갱신되지 않았다. 팀장과 팀원이 각각 pull해야 했다.

이 수업은 PR을 “merge 버튼” 하나로 축소하지 않았다. branch 차이, 검토, merge 기록, remote 기준 branch 결과를 묶는 협업 artifact로 사용했다. 다만 branch protection, 필수 승인 수, 조직 권한 정책을 구성한 것으로 확대하지 않는다.

## 성공 상태를 나누어 확인하기

| 성공 상태 | 확인 지점 | 다음 별도 단계 |
|---|---|---|
| branch push | GitHub branch에 새 commit·file 표시 | PR 생성 |
| PR 생성 | 열린 PR, 올바른 base/compare, 변경 diff | review·merge |
| PR merge | merged·closed, remote `master`의 file·history | local pull |
| remote `master` 갱신 | GitHub 기준 branch에 통합 결과 | 각 작업자의 local 최신화 |
| local `master` 최신화 | Git client에서 checkout·pull 후 file·history | 다음 작업 branch 분기 |

GitHub의 remote branch가 바뀌어도 SourceTree나 IntelliJ working tree는 자동으로 바뀌지 않는다. 반대로 local commit만 만든 상태도 GitHub에는 보이지 않는다.

## Git·client·Actions와의 책임 경계

- [[entities/git|Git]]: working tree, staging area, local commit·branch, fetch/merge/rebase를 관리한다.
- [[entities/source-tree|SourceTree]]·[[entities/intellij-idea|IntelliJ IDEA]]: local/remote Git 상태를 조작·표시하는 client다.
- **GitHub:** remote hosting과 branch 공유, PR review·merge UI를 제공한다.
- [[concepts/github-actions-workflow|GitHub Actions]]: 후속 CI/CD에서 event를 받아 workflow job을 실행하는 platform이다. PR merge 성공과 build·image push·deploy 성공은 별도 상태다.

## conflict에 대한 역할

GitHub와 IDE는 branch 차이와 conflict 여부·해결 UI를 보여 줄 수 있지만, 어느 변경이 업무적으로 맞는지는 결정하지 않는다. 05-06의 `Main.java`·`Cat.java` conflict는 local/remote 이력을 받아 사람이 최종 내용을 선택하고 Git history로 확정해야 했다.

## 학습 이력

- [[summaries/2026-02-27-github-initial-setup|2026-02-27]] — 개인 Java repository와 local 연결 준비
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]] — remote push/pull/clone·collaborator·branch 시작
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]] — PR review·merge·remote/local 최신화·conflict
- [[summaries/2026-05-11-cicd-github-actions-spring-boot|2026-05-11]] — 후속 GitHub Actions 자동화

## 관련 개념

- [[entities/git|Git]]
- [[entities/source-tree|SourceTree]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]

## 출처

- `raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf` — 화면 절차 보조
- `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md` — 후속 Actions 경계

실제 account·email·repository URL·organization·credential은 재노출하지 않았다. P04는 branch·PR 화면 절차를 보조했으며 날짜별 MD의 실행 결과를 대체하지 않는다.