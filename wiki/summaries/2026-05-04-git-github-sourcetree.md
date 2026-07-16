---
title: 2026-05-04 Git 상태 전이, GitHub remote와 SourceTree 협업 입문
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
status: growing
confidence: high
---

# 2026-05-04 Git 상태 전이, GitHub remote와 SourceTree 협업 입문

## 한 줄 요약

Git Bash에서 WorkTree의 untracked·modified 파일을 stage와 local repository를 거쳐 GitHub remote로 보내고, clone한 두 번째 작업자와 SourceTree에서 pull·push·merge를 반복하며 협업 충돌이 생기는 조건까지 확인한 날이다.

## 왜 이 순서로 배웠는가

Docker 수업까지는 “애플리케이션을 어디서 어떻게 실행할지”를 다뤘다. 이제 여러 사람이 그 애플리케이션의 source를 어떻게 나누고 합칠지 배울 차례였다. 그래서 GUI를 먼저 누르지 않고 Git Bash에서 파일의 상태가 어떻게 바뀌는지 확인한 뒤, GitHub remote와 SourceTree가 그 상태 전이를 어떻게 보여 주는지 연결했다.

`init → status → add → commit → remote → push → pull/clone → 두 작업자 충돌 → branch 시작` 순서로 학습해야 push 실패나 merge conflict를 단순 “GitHub 오류”가 아니라 local/remote 이력 차이로 해석할 수 있다.

## 저장 공간과 상태 전이

| 위치·상태 | 수업에서 확인한 의미 |
|---|---|
| WorkTree | 실제 파일을 만들고 수정하는 directory |
| untracked | Git이 아직 추적하지 않는 새 파일 |
| modified | 이미 추적 중인 파일의 working tree 내용이 바뀐 상태 |
| stage | 다음 commit에 넣을 변경을 `git add`로 고른 상태 |
| local repository | `git commit`으로 저장한 내 컴퓨터의 이력 |
| remote repository | GitHub에 공유한 commit과 branch |

`git status`를 각 단계 사이에 반복해 파일 내용뿐 아니라 Git이 인식한 상태가 어떻게 달라지는지 확인했다.

## 교시별 학습 전개

### 1교시 — Git Bash에서 local repository 만들기

- Git Bash와 실제 Git 명령을 처리하는 `git.exe`의 역할을 구분했다.
- 새 directory를 만들고 `git init`을 실행하자 `.git`이 생기며 그 directory가 WorkTree가 됐다.
- 최초 `git status`에서는 commit도 추적 파일도 없는 상태를 확인했다.
- repository별 사용자 이름과 email을 설정하고 `.git/config`에서 반영 여부를 확인했다. 실제 개인 식별자는 이 Summary에 재노출하지 않는다.
- `myfile.txt`를 만들자 untracked로 표시됐고, `git add` 뒤에는 staged new file로 바뀌었다.
- commit 뒤에는 `working tree clean`이 됐고 `git log`에서 commit 식별자·작성자·메시지를 확인했다.
- 추적 파일 수정에는 `commit -am`을 사용했고, 다시 수정한 내용은 `git diff`에서 삭제·추가 행으로 비교했다.

`commit -a`는 이미 추적하는 파일의 변경을 stage할 수 있지만 새 untracked 파일까지 자동 포함하지 않는다는 점을 state 모델과 함께 이해해야 한다.

### 1교시 후반 — GitHub remote와 push

- 새 파일과 수정 파일을 stage·commit했다.
- `git remote -v`가 비어 있으면 아직 remote 연결이 없다는 뜻임을 확인했다.
- remote alias `origin`을 추가하고 `.git/config`의 URL·fetch refspec을 확인했다.
- 최초 push에서 local `master`를 `origin/master`에 연결했고, browser에서 commit이 올라갔는지 확인했다.
- 이후 파일을 다시 수정·commit하고 `git push`로 변경을 반영했다.

원본의 실제 account·email·repository URL은 공개 식별자가 될 수 있으므로 모두 역할 중심으로 일반화했다.

### 2교시 — 기록 공백

원본에는 `이어서 작성`만 있다. 앞뒤 실습을 이 교시에 임의 귀속하지 않는다.

### 3~4교시 — remote 변경을 pull하고 clone으로 두 번째 작업자 만들기

- GitHub browser에서 `hello.txt`를 만들고 commit했다.
- 기존 local repository에서 `git pull`한 뒤 파일 목록과 내용을 확인했다.
- commit하지 않은 `world.txt`를 둔 채 push해도 오류가 나지 않았지만 remote에는 올라가지 않았다.
- stage만 하고 push해도 마찬가지였고, commit한 뒤에야 push 대상이 됐다.
- remote repository를 다른 이름의 directory로 clone해 두 번째 작업자의 local repository를 만들었다.
- 두 번째 작업자는 repository-local 사용자 정보를 다르게 설정했다.
- 이 시점의 `git remote -v` 확인은 원본에 “안 하심”으로 기록되어 있으므로 실행 결과로 만들지 않는다.

여기서 확인한 핵심은 `push`가 working tree 파일이나 stage를 보내는 동작이 아니라 **local commit을 remote에 전달하는 동작**이라는 점이다.

### 4~5교시 — SourceTree 설치와 같은 Git 상태의 GUI 표현

- SourceTree를 설치하고 GitHub 계정을 OAuth로 연결했다.
- 이미 `git init`된 두 local repository를 SourceTree 관리 목록에 추가했다.
- History에서 commit 이력을 확인했다.
- Git Bash에서 만든 새 파일과 수정 파일이 SourceTree의 stage 후보로 보이는지 확인했다.
- SourceTree에서 stage·commit·push를 실행했다.

SourceTree는 source editor가 아니며 Git을 대신하는 별도 version control system도 아니다. Git repository의 status·history·remote operation을 GUI로 보여 주는 client다.

### 6교시 — 두 작업자 pull과 같은 파일 충돌

- 두 번째 local repository에서 첫 작업자의 새 commit을 pull했다.
- 새 파일이 생기고 기존 파일 내용이 바뀐 것을 `ls`와 `cat`으로 확인했다.
- 두 작업자가 같은 파일의 마지막 부분을 서로 다르게 수정했다.
- 첫 작업자가 먼저 push한 뒤 두 번째 작업자가 push하자 remote에 자신에게 없는 commit이 있어 거부됐다.
- 해결 흐름은 remote 변경을 pull하고, 서로 다른 내용을 merge한 뒤 stage·commit·push하는 것이었다.

충돌은 “두 사람이 같은 project를 썼기 때문”이 아니라, **공통 기준 commit 이후 같은 파일의 같은 부분에 서로 다른 변경을 만들고 한쪽 remote 이력이 먼저 진행됐기 때문**이다.

### 7교시 — branch 협업의 시작

- IntelliJ project와 GitHub remote를 연결하고 팀장 역할의 `master`를 push했다.
- `animal` branch를 `master`에서 만들고 checkout했다.
- branch에만 Cat·Dog class를 추가해 commit·push했다.
- `master`에는 Main만, `animal`에는 Main과 Cat·Dog가 보이는 것을 GitHub·IntelliJ·실제 directory에서 확인했다.
- repository collaborator를 초대하고 팀원 계정이 초대를 수락하는 단계까지 진행했다.

branch를 바꿀 때 working tree의 파일 구성이 달라지는 것을 직접 본 것이 중요하다. branch는 단순 폴더 복사 이름이 아니라 서로 다른 commit 계보를 가리킨다.

### 8교시 — 후속 작성 표지만 존재

원본에는 `이어서 작성`만 있다. 팀원 branch와 PR의 직접 실습은 05-06으로 이어진다.

## 대표 실습: 두 local repository의 remote 동기화

1. 첫 local repository에서 파일을 수정하고 stage·commit·push한다.
2. 두 번째 local repository에서 pull해 새 파일과 수정 내용을 확인한다.
3. 두 repository가 같은 파일의 같은 위치를 다르게 수정한다.
4. 첫 작업자가 먼저 commit·push한다.
5. 두 번째 작업자의 push는 remote가 더 앞서 있어 거부된다.
6. 두 번째 작업자는 pull로 remote 변경을 받고 conflict를 merge한 뒤 다시 commit·push한다.

입력은 서로 다른 local 변경, 처리는 commit graph 비교와 merge, 결과는 두 변경을 반영한 새 commit과 동기화된 remote다.

## `clone`·`pull`·`fetch`의 이날 범위

- `clone`: remote 전체를 새로운 local directory로 처음 복제했다.
- `pull`: 이미 연결된 local repository에 remote commit을 가져와 현재 branch에 반영했다.
- `fetch`: `.git/config`의 fetch refspec과 remote 추적 정보가 등장했지만, 독립적인 `git fetch` 실행과 결과 확인은 이날 기록에 없다. remote branch를 fetch해 local branch로 만드는 실습은 05-06에 이어진다.

## 헷갈리기 쉬운 지점

- **Git과 GitHub:** Git은 local history와 branch를 관리하고, GitHub는 remote 공유·협업 service다.
- **Git Bash와 SourceTree:** terminal과 GUI의 차이일 뿐 같은 repository 상태를 조작한다.
- **WorkTree·stage·commit·remote:** 파일 수정, 다음 commit 선택, local 이력 저장, remote 공유는 서로 다른 단계다.
- **stage만 하고 push:** push는 stage가 아니라 commit을 전송하므로 remote 변화가 없다.
- **pull과 push 순서:** remote가 앞서면 먼저 변경을 받아 통합해야 한다. 무조건 push로 덮는 것이 아니다.
- **branch와 directory 복사:** clone은 별도 local repository를 만들고 branch는 한 repository 안의 commit 계보를 전환한다.
- **사용자 이름/email:** commit 작성자 식별 정보이지 GitHub 인증 credential 그 자체는 아니다.

## 이전·다음 연결과 과목 경계

- 이전: [[summaries/2026-05-01-docker-compose|05-01]]까지 실행환경을 선언한 뒤, 이날부터 source와 변경 이력을 협업하는 방법으로 전환했다.
- 선행: Java 초기에 개인 repository를 만들었던 경험을 팀장·팀원 remote 동기화와 branch로 확장했다.
- 다음: [[summaries/2026-05-06-github-branch-pr-conflict|05-06]]에는 팀원 branch, Pull Request, review·merge, master 최신화와 conflict/rebase를 실습한다.
- 후속: GitHub push가 [[concepts/github-actions-workflow|GitHub Actions workflow]]의 trigger가 되는 것은 CI/CD 과목의 직접 범위다. 이날은 수동 협업만 다뤘다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]] — 실행환경 변경 기록과 source 변경 이력의 책임 비교에 도움

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`

날짜 MD의 Git Bash·SourceTree·IntelliJ 순서를 최우선으로 사용했다. 실제 account·email·repository URL·OAuth credential은 재노출하지 않았다.
