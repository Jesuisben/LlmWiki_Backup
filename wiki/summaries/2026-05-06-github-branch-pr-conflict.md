---
title: 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [github, ci-cd, project, curriculum]
sources:
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
  - raw/Study/5. Linux/교육 자료/Github 교안(실습).pdf
status: growing
confidence: high
---

# 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결

## 한 줄 요약

개인 Git 사용에서 팀 협업으로 확장해 branch, push, Pull Request, merge, pull, conflict 해결 흐름을 실습한 날이다.

## 배운 내용

- 각자 branch를 만들고 작업한 뒤 원격 저장소에 push했다.
- GitHub에서 Pull Request를 만들어 변경 내용을 기준 branch에 합치는 흐름을 익혔다.
- 다른 사람이 먼저 merge한 변경을 로컬에 `pull`해 최신 상태를 맞췄다.
- 같은 파일/같은 위치를 수정하면 conflict가 발생할 수 있음을 확인했다.
- conflict marker를 보고 남길 내용과 버릴 내용을 선택한 뒤 다시 add/commit/push하는 흐름을 배웠다.

## 핵심 개념

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]]
- branch: 독립 작업 흐름.
- Pull Request: 변경 제안과 리뷰/병합 단위.
- conflict: Git이 자동으로 합칠 수 없는 변경 충돌.

## 실습 / 예제

```bash
git branch feature/member
git checkout feature/member
git add .
git commit -m "회원 기능 수정"
git push origin feature/member
git checkout master
git pull origin master
```

충돌이 나면 파일 안의 `<<<<<<<`, `=======`, `>>>>>>>` 표시를 보고 최종 내용을 정리한 뒤 다시 commit한다.

## 헷갈린 점 / 질문

- PR은 commit 자체가 아니라 branch의 변경을 기준 branch에 합치자고 제안하는 GitHub 기능이다.
- merge 후 내 로컬 master/main이 자동으로 최신화되는 것은 아니므로 pull이 필요하다.
- conflict 해결은 “오류 제거”가 아니라 두 변경 중 최종 업무 규칙에 맞는 내용을 결정하는 과정이다.

## 관련 페이지

- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]
- [[concepts/ci-cd-automation|CI/CD 자동화]]

## 출처

- `raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
