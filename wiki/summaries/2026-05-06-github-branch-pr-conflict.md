---
title: 2026-05-06 GitHub branch, Pull Request와 conflict 해결
created: 2026-07-06
updated: 2026-07-18
type: summary
tags: [github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
status: growing
confidence: high
---

# 2026-05-06 GitHub branch, Pull Request와 conflict 해결

## 한 줄 요약

팀장·팀원이 각 local branch에서 작업한 변경을 GitHub Pull Request로 검토·merge하고, remote `master`를 각 local에 다시 pull한 뒤 같은 `Cat.java`를 다르게 고쳐 conflict와 merge/rebase 선택을 재현했다.

## 왜 이 순서로 배웠는가

05-04에는 WorkTree→stage→commit→remote의 기본 상태 전이와 두 local repository의 push 충돌을 배웠고, 마지막에 팀장 `animal` branch와 collaborator 초대까지 진행했다. 이날은 팀원 입장에서 project를 clone하고 `sport` branch를 만든 뒤, branch 변경을 `master`로 가져오는 공식 검토 단위인 Pull Request를 실습했다.

PR merge만으로 협업이 끝나지 않는다. GitHub의 `master`가 바뀐 뒤 각자의 local `master`도 pull해야 하며, remote branch가 local에 없으면 fetch 후 local branch를 만들어야 한다. 마지막에는 같은 파일의 같은 부분을 다르게 수정해 충돌 해결까지 연습했다.

## 역할별 협업 모델

| 역할 | branch·artifact | 주요 책임 |
|---|---|---|
| 팀장 | `master`, `animal`; Main·Cat·Dog | 기준 branch 관리, animal 작업, PR 확인, local master 최신화 |
| 팀원 | `master`, `sport`; Main·Baseball·Football | project clone, sport 작업, PR 생성·확인, local master 최신화 |
| GitHub remote | `master`, `animal`, `sport` | branch 공유, PR 비교·검토·merge 이력 보존 |

이 역할 구분은 권한 정책을 완성했다는 뜻이 아니라, 수업 시나리오에서 누가 어느 branch와 화면을 조작했는지 구분하기 위한 것이다.

## 교시별 학습 전개

### 1교시 — 팀원 clone과 같은 파일 conflict

- 팀원은 IntelliJ의 Project from Version Control로 팀장 repository를 다른 local directory에 clone했다.
- `.git`이 있는 project에서 팀원용 commit 작성자 정보를 설정하는 절차가 있었다. 원본의 `user.email` 명령은 닫는 큰따옴표가 빠져 있고 설정 조회 결과도 없으므로 정상 반영 완료로 확정하지 않는다. 실제 이름과 email은 일반화했다.
- 팀원이 `Main.java`에 한 줄을 추가해 commit·push했다.
- 팀장은 자신의 local `master`에서 같은 `Main.java`에 다른 줄을 추가해 push하려 했다.
- 팀장 local, 팀원 local, GitHub remote의 내용이 달라졌고 push가 거부됐다.
- IntelliJ의 3-way merge 화면에서 내 코드, remote 코드, 병합 결과를 비교해 선택하고 Apply했다.

입력은 공통 base 이후의 서로 다른 두 변경이고, 처리는 remote 이력 확인과 수동 merge이며, 결과는 두 변경을 통합한 새 commit이다.

### 2교시 — IntelliJ Git Bash 설정과 팀원 `sport` branch

- IntelliJ terminal의 shell path를 Git Bash로 설정했다.
- 팀원 local `master`에서 `sport` branch를 만들고 checkout했다.
- Baseball·Football class를 추가해 commit·push했다.

터미널을 Git Bash로 바꾼 것은 Git 자체를 바꾼 것이 아니다. IntelliJ 안에서 같은 Git command 환경을 사용하기 위한 editor 설정이다.

### 3교시 — Pull Request 생성·검토·merge

첫 PR에서는 팀장의 `animal` branch를 `master`에 합쳤다.

1. GitHub에서 base와 compare branch를 선택해 PR을 만든다.
2. 제목과 설명으로 Cat·Dog class 변경 목적을 기록한다.
3. 다른 계정에서 conflict 없음과 변경 내용을 확인한다.
4. Merge pull request와 Confirm merge로 `master`에 반영한다.
5. PR이 merged·closed 상태가 되고 branch를 안전하게 삭제할 수 있다는 안내를 확인한다.
6. Insights에서 활동 이력을 확인한다.

이어 팀원의 `sport` branch도 PR로 올리고 팀장 계정에서 검토·merge했다. PR의 핵심은 “누가 merge 버튼을 눌렀는가”보다 branch 차이를 remote에서 검토하고 합의 기록을 남긴다는 점이다.

### 4교시 — remote `master`와 local 상태 동기화

- GitHub `master`에는 animal·sport file이 merge됐지만, IntelliJ local `master`에는 자동으로 생기지 않았다.
- 팀장과 팀원 모두 local `master`를 checkout한 뒤 pull하여 remote merge 결과를 받았다.
- fetch를 수행하면 IntelliJ Git 창의 Remote branch 정보가 갱신됐다.
- `origin/sport`를 기준으로 새 local branch를 만들어 remote branch를 local에서 사용할 수 있게 했다.

`fetch`는 remote branch 정보를 갱신하는 단계이고, `pull`은 현재 branch에 remote 변경을 반영하는 단계다. remote branch가 보인다고 local working tree가 자동으로 그 branch 내용으로 바뀌는 것은 아니다.

### 4교시 후반 — 같은 `Cat.java` conflict 재현

- 팀장이 `Cat.java`에 한 출력을 추가해 commit·push했다.
- 팀원은 자신의 local에서 같은 파일의 같은 부분에 다른 출력을 추가해 commit·push했다.
- IDE가 Merge 또는 Rebase 선택을 제시했다.
- raw에는 Rebase를 선택하면 현재 push가 취소되고, 충돌을 정리한 뒤 다시 push한 흐름이 기록돼 있다.
- Merge를 선택해 병합하거나 Rebase를 선택해 기준 이력 위에 변경을 다시 적용하는 두 방법을 안내받았다.

이날은 IntelliJ UI에서 선택·해결한 범위다. `git rebase` CLI의 세부 명령, interactive rebase, force push 정책까지 실행한 것으로 확대하지 않는다.

### 5~6교시 — GitHub 협업 반복 실습

원본에는 “깃허브로 협업하기 실습”이라는 기록만 있다. 구체적인 추가 branch·file·결과는 없으므로 앞선 시나리오 반복으로만 보존한다.

### 7~8교시 — 기록된 내용 없음

교시 heading만 있고 실질 기록은 없다. 같은 날짜에 시작한 AWS 수업의 VPC·EC2 내용을 이 Linux/GitHub Summary에 합치지 않는다.

## 대표 실습: branch 변경이 팀 전체 `master`에 도달하는 생명주기

1. 작업자가 local `master`에서 작업 branch를 만들고 checkout한다.
2. class를 추가·수정하고 stage·commit한다.
3. 작업 branch를 GitHub remote에 push한다.
4. GitHub에서 base `master`와 작업 branch를 비교하는 PR을 만든다.
5. 검토자가 변경과 conflict 여부를 확인하고 merge한다.
6. GitHub `master`가 갱신된다.
7. 각 작업자는 local `master`를 checkout하고 pull해 새 commit과 file을 받는다.

PR merge는 remote 상태를 바꾸고, local 최신화는 별도의 pull이다. 이 두 단계를 나누어야 “GitHub에는 파일이 있는데 IntelliJ에는 왜 없는가”를 설명할 수 있다.

## merge와 rebase의 실제 수업 범위

- **merge:** 갈라진 두 이력을 병합하고 충돌 위치에서 유지할 내용을 선택했다.
- **rebase:** IDE가 제시한 선택지로, 팀원 변경을 새 remote 기준 위에 다시 적용해 충돌을 정리하고 재push하는 흐름을 경험했다.
- **공통점:** conflict가 사라지는 마법 버튼이 아니라, 같은 부분의 변경을 사람이 판단해야 한다.
- **범위 밖:** 팀의 rebase 정책, public branch history rewrite, force push는 이날 직접 구현·검증하지 않았다.

## 헷갈리기 쉬운 지점

- **branch push와 PR merge:** branch를 push했다고 `master`에 들어간 것이 아니다. PR 검토·merge가 별도다.
- **remote `master`와 local `master`:** GitHub에서 merge해도 local은 자동 최신화되지 않는다.
- **fetch와 pull:** fetch는 remote 추적 정보 갱신, pull은 현재 branch에 remote 변경 반영이다.
- **checkout과 file 변화:** branch를 바꾸면 working tree가 해당 commit 상태에 맞게 바뀐다.
- **conflict와 push 거부:** remote가 앞선 것과 같은 파일 같은 부분의 충돌은 관련 있지만 동일한 현상은 아니다. 먼저 이력 차이를 받아야 실제 merge 충돌을 판단할 수 있다.
- **merge와 rebase:** 둘 다 통합 방법이지만 commit history 모양이 다르다. 이날은 IDE 실습 범위만 확인했다.
- **PR의 검토자:** 수업에서는 팀장·팀원이 서로 확인했지만 실제 조직의 승인 권한·branch protection 정책까지 설정한 것은 아니다.

## 이전·다음 연결과 과목 경계

- 이전: [[summaries/2026-05-04-git-github-sourcetree|05-04]]의 기본 상태 전이·두 local repository·branch 시작을 PR 협업 루프로 완성했다.
- Linux 과목 마무리: VM·CLI·권한·server·Docker 실행환경을 다룬 뒤 source 협업까지 연결한 마지막 직접 수업일이다.
- 같은 날짜 AWS: [[summaries/2026-05-06-aws-cloud-vpc-ec2|05-06 AWS 입문]]은 별도 과목의 Cloud/VPC/EC2 학습이다. 이 Summary의 7~8교시 빈 기록을 AWS 구현으로 채우지 않는다.
- 후속 CI/CD: GitHub push·branch는 Actions trigger와 배포 자동화로 이어지지만, 이날 workflow 파일이나 자동 배포를 만들지 않았다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[concepts/github-actions-workflow|GitHub Actions workflow]] — 후속 자동화 경계

## 출처

- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`

날짜 MD의 팀장·팀원·PR·fetch·conflict 순서를 우선했다. 실제 account·email·repository URL·credential은 재노출하지 않았고 같은 날짜 AWS는 별도 과목으로 분리했다.
