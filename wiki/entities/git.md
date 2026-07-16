---
title: Git
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
status: stable
confidence: high
---

# Git

## 무엇인가

Git은 파일 변경을 local commit 이력과 branch로 관리하고, 여러 repository 사이에서 그 이력을 교환·통합하는 분산 버전 관리 시스템이다. GitHub, SourceTree, IntelliJ가 없어도 Git repository와 commit은 존재할 수 있다.

## 이 위키에서의 맥락

- **Java 선행 — 2026-02-27:** 개인 `MyJava` 폴더를 `git init`으로 local repository로 만들고 작성자·safe directory를 설정한 뒤 IntelliJ와 GitHub remote 연결을 준비했다.
- **Linux 직접 — 2026-05-04:** Git Bash에서 working tree→stage→commit→remote push를 상태 출력으로 확인하고 clone·pull, SourceTree 두 작업자의 동기화와 push 거부, `animal` branch를 실습했다.
- **Linux 직접 — 2026-05-06:** IntelliJ에서 팀원 clone, `sport` branch, PR 전후 local/remote 상태, fetch, merge/rebase conflict를 실습했다.
- **CI/CD 후속:** GitHub push는 Actions trigger로 재사용되지만 workflow 실행·build·deploy는 Git 기능이 아니다.

## Git이 관리하는 상태

| 상태 | 책임 | 바뀌는 대표 동작 |
|---|---|---|
| working tree | 현재 checkout한 commit을 실제 파일로 펼치고 편집 | 파일 편집, checkout/merge/pull 결과 |
| staging area | 다음 commit에 포함할 변경 선택 | `add`, unstage |
| local repository | commit object와 branch 이력 저장 | `commit`, merge, rebase |
| local branch | local commit을 가리키는 이동 가능한 ref | commit, merge, rebase, checkout |
| remote-tracking branch | 마지막 fetch 시점의 remote branch 관찰값 | fetch, pull의 fetch 단계 |
| remote branch | 다른 repository에 존재하는 branch | push 또는 remote 측 merge |

local branch와 `origin/...`은 같은 branch의 복사본처럼 보이지만 자동 동기화되지 않는다. fetch는 remote-tracking branch를 갱신하고, pull·merge·rebase 같은 별도 통합이 local branch와 working tree를 바꾼다.

## 명령의 책임과 상태 전이

| 명령 | 입력 | 처리 | 결과 |
|---|---|---|---|
| `init` | 일반 directory | `.git` metadata 생성 | local repository 시작; remote는 생기지 않음 |
| `status` | working tree·stage·현재 branch | 상태 비교 | 상태를 표시할 뿐 변경하지 않음 |
| `add` | working tree 변경 | commit 후보 선택 | stage 변경 |
| `commit` | staged 변경 | local snapshot·message 기록 | local branch가 새 commit을 가리킴 |
| `push` | local의 새 commit | remote로 object·ref 전송 | remote branch 갱신; PR merge와 별개 |
| `fetch` | remote의 새 object·ref | local로 다운로드 | remote-tracking branch 갱신; working tree 유지 |
| `pull` | 현재 local branch와 upstream | fetch 후 merge 또는 설정된 통합 | local branch·working tree 갱신 가능 |
| `merge` | 현재 branch와 다른 branch | 공통 base 이후 변경 통합 | fast-forward/merge commit 또는 conflict |
| `rebase` | local commit과 새 base | commit을 새 base 위에 재적용 | local history 재구성 또는 conflict |
| `clone` | remote repository | history·refs·working tree 복제 | 독립 local repository와 remote 설정 생성 |

## 실제 수업 artifact

- 05-04 `myfile.txt`는 untracked→staged→committed→pushed 상태를 순서대로 확인하는 artifact였다.
- `hello.txt`는 GitHub remote에서 만든 뒤 pull로 local에 내려온 artifact였다.
- commit 없는 `world.txt` 변경은 push해도 remote로 가지 않았다. push는 working tree나 stage가 아니라 commit을 전송한다.
- 두 local repository가 같은 `myfile.txt`를 다르게 commit한 뒤 후발 push가 거부됐다. remote 이력 통합과 수동 내용 판단이 필요했다.
- 팀장 `animal`과 팀원 `sport`는 local/remote branch를 구분하고 PR로 `master`에 통합하기 위한 실제 작업선이었다.
- 05-06 `Main.java`와 `Cat.java`는 push 거부·3-way merge·merge/rebase conflict를 재현한 artifact였다.

## Git이 하지 않는 일

- GitHub 계정·repository hosting·Pull Request review UI를 제공하지 않는다.
- SourceTree나 IntelliJ 화면 자체가 아니다. 두 도구는 Git client다.
- GitHub Actions workflow를 실행하거나 Maven build·Docker image·EC2 deploy를 수행하지 않는다.
- conflict에서 어느 업무 로직이 맞는지 결정하지 않는다. 사람의 판단이 필요하다.

## 완료 조건

- commit 완료: local history와 현재 branch에 새 commit이 보인다.
- push 완료: remote branch가 해당 commit을 가리킨다.
- fetch 완료: remote-tracking branch가 새 remote 상태를 반영한다.
- pull 완료: 현재 local branch와 working tree에 통합 결과가 반영된다.
- conflict 해결 완료: unresolved 항목이 사라지고 선택한 결과가 stage·commit되며, 필요하면 후속 push까지 확인한다.

## 학습 이력

- [[summaries/2026-02-27-github-initial-setup|2026-02-27 GitHub 초기 설정]] — 개인 local repository와 remote 준비
- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]] — Git Bash 상태 전이·clone/pull·SourceTree·branch 시작
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06]] — 팀 branch·fetch·merge/rebase conflict

## 관련 개념

- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[entities/intellij-idea|IntelliJ IDEA]]
- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]] — 후속 경계

## 출처

- `raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md`
- `raw/KoreaICT/1. Java/교육 자료/Github 교안(실습).pdf`
- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
- `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md`
- `raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf` — 화면 절차 보조

Java의 개인 저장소 첫 등장과 Linux의 팀 협업 확장을 날짜별로 분리했다. 실제 작성자 정보·remote URL·credential은 재노출하지 않았다.