---
title: git fetch vs pull vs clone
created: 2026-07-02
updated: 2026-07-09
type: comparison
tags: [github, ci-cd, project]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/KoreaICT/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# git fetch vs pull vs clone

## 비교 목적

GitHub 협업 수업에서 `clone`, `pull`, `fetch`가 모두 등장했다. 셋 다 “원격 저장소에서 가져오는” 명령처럼 보이지만 쓰는 시점과 결과가 다르다.

## 한눈에 보기

| 명령 | 언제 쓰나 | 결과 |
|---|---|---|
| `git clone` | 처음 원격 저장소를 내 컴퓨터에 받을 때 | 새 로컬 저장소/작업 폴더 생성 |
| `git fetch` | 원격 branch/commit 정보를 확인하고 싶을 때 | 원격 추적 정보만 갱신, 작업 파일은 그대로 |
| `git pull` | 현재 branch에 원격 변경을 반영하고 싶을 때 | fetch 후 merge/rebase로 작업 파일까지 갱신 |

## 언제 무엇을 쓰는가

- 팀 저장소를 처음 받을 때: `git clone`.
- 원격에 뭐가 바뀌었는지만 보고 싶을 때: `git fetch`.
- 내 현재 branch에 원격 변경을 합치고 싶을 때: `git pull`.

## 예시

```bash
git clone https://github.com/계정/저장소.git my-folder
git fetch
git pull origin master
```

## 헷갈리기 쉬운 포인트

- `pull`은 작업 파일을 바꾸므로 작업 중인 변경이 있으면 먼저 status를 확인해야 한다.
- `fetch`는 안전하게 원격 정보만 갱신하지만, 그 자체로 내 파일을 최신화하지 않는다.
- `clone`은 이미 저장소가 있는 폴더에서 반복적으로 쓰는 명령이 아니다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]

## 5과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/5. Linux` 날짜별 MD 10개와 `Linux 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 명령어 사전이 아니라 VM/SSH/CLI → 파일·권한 → Spring Boot jar 실행 → Docker network/volume/Dockerfile/Compose → GitHub branch/PR/conflict 흐름 속에서 읽어야 한다.
- 운영 관점에서는 코드보다 IP/포트/방화벽/권한/컨테이너 네트워크·볼륨이 문제 원인일 수 있음을 함께 기억한다.

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
