---
title: 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문
created: 2026-07-06
updated: 2026-07-13
type: summary
tags: [github, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md
status: growing
confidence: high
---

# 2026-05-04 GitHub, Git Bash, SourceTree 협업 입문

## 한 줄 요약

Git Bash에서 init/add/commit/push/pull/clone을 실습하고 SourceTree로 같은 흐름을 GUI에서 확인하며 GitHub 협업의 기본기를 익혔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

배포와 협업은 GitHub 원격 저장소를 중심으로 진행된다. 명령어와 GUI 흐름을 모두 알아야 팀 프로젝트에서 충돌과 동기화 문제를 해결할 수 있다.

## 핵심 개념

- Git Bash와 `git.exe`의 역할, Git 설치 경로를 확인했다.
- 원격 저장소 생성, 파일 생성, 로컬 저장소 pull, commit 없는 push 실패를 경험했다.
- clone으로 원격 저장소를 새 로컬 폴더에 내려받는 흐름을 배웠다.
- SourceTree 설치 후 commit/push/pull을 GUI로 수행했다.

## 실습 / 예제

한 파일을 GitHub에서 만들고 로컬로 pull한 뒤, 로컬 수정 → commit → push → 다른 폴더에서 pull하는 식으로 동기화 흐름을 실습했다.

## 헷갈린 점 / 질문

push는 commit된 변경을 원격에 올리는 동작이다. working tree에 수정만 있고 commit이 없으면 push할 내용이 없다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]], [[entities/git|Git]], [[entities/github|GitHub]], [[entities/source-tree|SourceTree]]

## 출처

- `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md`
