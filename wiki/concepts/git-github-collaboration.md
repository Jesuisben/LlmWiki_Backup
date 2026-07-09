---
title: GitHub 협업 흐름
created: 2026-07-02
updated: 2026-07-09
type: concept
tags: [github, ci-cd, project]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# GitHub 협업 흐름

## 정의

GitHub 협업 흐름은 각자 branch에서 작업하고, commit을 원격 저장소에 push한 뒤 Pull Request로 기준 branch에 병합하며, 충돌이 나면 해결하는 절차다.

## 왜 중요한가

개인 프로젝트는 혼자 commit/push하면 되지만, 팀 프로젝트는 여러 사람이 같은 코드베이스를 동시에 수정한다. branch/PR/merge/pull/conflict 흐름을 이해해야 코드 손실 없이 협업할 수 있다.

## 핵심 설명

1. 원격 저장소를 clone하거나 로컬 저장소를 remote와 연결한다.
2. 작업 branch를 만든다.
3. 파일을 수정하고 add/commit한다.
4. 원격 branch로 push한다.
5. GitHub에서 Pull Request를 만든다.
6. 리뷰 또는 확인 후 기준 branch에 merge한다.
7. 로컬 기준 branch에서 pull로 최신 변경을 가져온다.
8. 충돌이 생기면 conflict marker를 정리하고 다시 commit한다.

## 예시

```bash
git clone https://github.com/계정/저장소.git
cd 저장소
git branch feature/member
git checkout feature/member
git add .
git commit -m "회원 기능 수정"
git push origin feature/member
```

기준 branch 최신화:

```bash
git checkout master
git pull origin master
```

## 자주 헷갈리는 점

- `git`은 로컬 버전 관리 도구, `GitHub`는 원격 저장소/협업 플랫폼이다.
- PR은 Git 명령 자체가 아니라 GitHub가 제공하는 협업 단위다.
- SourceTree 버튼도 내부적으로는 `add`, `commit`, `push`, `pull` 같은 Git 명령을 실행한다.
- conflict는 Git이 “무엇을 남겨야 하는지” 판단할 수 없다는 뜻이므로 사람이 최종 내용을 결정해야 한다.

## 관련 개념

- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]

## 5과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/5. Linux` 날짜별 MD 10개와 `Linux 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 명령어 사전이 아니라 VM/SSH/CLI → 파일·권한 → Spring Boot jar 실행 → Docker network/volume/Dockerfile/Compose → GitHub branch/PR/conflict 흐름 속에서 읽어야 한다.
- 운영 관점에서는 코드보다 IP/포트/방화벽/권한/컨테이너 네트워크·볼륨이 문제 원인일 수 있음을 함께 기억한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
