---
title: 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결
created: 2026-07-06
updated: 2026-07-13
type: summary
tags: [github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md
status: growing
confidence: high
---

# 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결

## 한 줄 요약

팀원 브랜치 생성, commit/push, Pull Request, master 병합 후 pull, 충돌 시나리오를 실습하며 GitHub 협업 흐름을 마무리했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

팀 프로젝트에서는 모두가 master/main에 직접 push하지 않고 브랜치와 PR로 변경을 검토·병합한다. 충돌 해결은 협업에서 반드시 겪는 문제다.

## 핵심 개념

- 팀원 역할로 새 브랜치를 만들고 IntelliJ 설정과 함께 변경을 commit/push했다.
- GitHub Pull Request 생성, 검토, merge 흐름을 실습했다.
- PR로 병합된 master 브랜치를 로컬에 pull해 최신화했다.
- 같은 파일을 서로 다르게 수정해 충돌을 만들고 해결하는 시나리오를 다뤘다.

## 실습 / 예제

branch 생성 → 작업 commit → push → PR → merge → master pull → conflict 해결 순서로 팀 협업 기본 루프를 익혔다.

## 헷갈린 점 / 질문

clone은 새 복사본을 만드는 것이고, pull은 이미 있는 로컬 저장소에 원격 변경을 반영하는 것이다. PR merge 후에는 로컬 master도 pull해야 최신 상태가 된다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]], [[comparisons/git-fetch-vs-pull-vs-clone|git fetch vs pull vs clone]], [[entities/github|GitHub]]

## 출처

- `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md`
