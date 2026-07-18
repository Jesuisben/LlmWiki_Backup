---
title: git fetch vs pull vs clone
created: 2026-07-02
updated: 2026-07-18
type: comparison
tags: [github, ci-cd, project]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md
  - raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf
status: stable
confidence: high
---

# git fetch vs pull vs clone

## 비교 목적

05-04의 `clone`·`pull`과 05-06의 `fetch`는 모두 remote에서 data를 가져오지만 **새 local repository를 만드는가**, **remote-tracking 정보만 갱신하는가**, **현재 branch와 working tree까지 통합하는가**가 다르다.

## 한눈에 보기

| 비교 축 | `git clone` | `git fetch` | `git pull` |
|---|---|---|---|
| 시작 상태 | local repository가 아직 없음 | 이미 remote가 연결된 local repository | 이미 remote/upstream이 연결된 현재 branch |
| 직접 결과 | 새 directory·local repository·working tree·remote 연결 | remote object/ref와 remote-tracking branch 갱신 | fetch 뒤 현재 branch에 merge/rebase, working tree가 바뀔 수 있음 |
| 현재 file 변화 | 새 working tree 생성 | 자동 변경 없음 | 변경 가능 |
| 수업 artifact | 두 번째 작업자용 새 local repository | IDE Remote의 `origin/sport` 갱신 | remote `hello.txt`, PR merge된 class, 동료 변경을 현재 local에 반영 |
| 대표 시점 | 최초 참여·별도 작업 복제 | 통합 전 remote 상태 관찰 | 현재 branch를 최신 remote 상태와 통합 |

## 실제 선택 상황

### 상황 1: 팀 저장소를 처음 받거나 별도 작업자 local 만들기

`clone`을 선택한다. 05-04에는 같은 remote를 다른 이름의 새 directory에 복제해 두 번째 local repository를 만들고 작성자 설정을 분리했다. 05-06 팀원도 IntelliJ의 Project from Version Control로 별도 local directory를 만들었다.

### 상황 2: remote branch를 먼저 보고 local 작업선은 유지하기

`fetch`를 선택한다. 05-06에는 fetch 뒤 IDE Remote 목록의 `origin/sport`가 갱신되었고, 그 remote-tracking branch에서 local branch를 만드는 작업은 별도였다. fetch만으로 현재 branch와 working tree가 sport 내용으로 바뀌지 않았다.

### 상황 3: remote 변경을 현재 local branch에 실제 반영하기

`pull`을 선택한다. 05-04에는 GitHub에서 만든 `hello.txt`가 pull 뒤 local에 나타났고, 두 번째 local repository는 동료가 push한 file과 내용을 pull했다. 05-06 PR merge 뒤에도 각 local `master`는 자동 갱신되지 않아 `master` checkout 후 pull해야 했다.

## 함께 쓰는 관계

처음에는 `clone`으로 local repository를 만든다. 이후에는 `fetch`로 remote 상태를 관찰하고 필요할 때 merge/rebase하거나, 그 둘을 한 흐름으로 수행하는 `pull`을 사용한다. `pull`은 개념상 fetch+통합이지만, 어떤 branch에 어떤 전략으로 통합되는지 확인해야 한다.

## 실제 오류·완료 조건

| 단계 | 완료 증거 | 아직 완료되지 않은 것 |
|---|---|---|
| clone | 새 directory·`.git`·working tree·remote 연결 | 개인 작성자 설정·최신 후속 변경 |
| fetch | remote-tracking branch 갱신 | local branch 생성·checkout·working tree 변경 |
| pull | 현재 branch history와 file 변화 확인 | conflict가 있으면 해결·commit·후속 push |

push 거부는 remote가 앞선 상태일 수 있다는 신호다. pull 또는 fetch 후 통합 과정에서 실제 내용 conflict가 드러날 수 있으며, fetch 자체가 conflict를 해결하지 않는다.

## 흔한 오해와 확인되지 않은 범위

- `clone`은 기존 repository를 매번 최신화하는 명령이 아니다.
- `fetch` 성공은 현재 branch 최신화를 뜻하지 않는다.
- `pull`은 remote 전체를 무조건 현재 branch에 합치는 명령이 아니라 설정된 remote/upstream·지정 branch를 기준으로 통합한다.
- pull 뒤 file이 보이는 것, push 성공, PR merge는 서로 다른 완료 상태다.
- 이날은 IntelliJ의 merge/rebase 선택을 다뤘지만 CLI rebase 세부 옵션·interactive rebase·force push 정책은 확인하지 않았다.
- 후속 CI/CD의 checkout/fetch 동작은 workflow runner 책임이며 Linux 수업의 local 협업 성공과 동일하지 않다.

## provenance 메모

기존의 placeholder repository URL과 세 명령을 한 덩어리로 합친 `bash` fence는 제거했다. `clone`·`pull`은 R09의 서로 다른 연속 구간, `fetch`는 R10의 IDE 절차이므로 수업 원문 한 실행 묶음처럼 제시하지 않는다.

## 관련 페이지

- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04 Git 상태 전이와 SourceTree]]
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 branch·PR·conflict]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md` — 새 local clone, GitHub 변경 pull, 두 작업자 pull의 최우선 근거
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md` — PR merge 뒤 local pull과 fetch→remote-tracking→local branch의 최우선 근거
- `raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf` — Git Bash·SourceTree·branch/PR/fetch 화면 절차 보조
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` — 세 명령의 복습 경계