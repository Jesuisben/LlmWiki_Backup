---
title: SourceTree
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [ci-cd]
sources:
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
status: growing
confidence: high
---

# SourceTree

## 무엇인가

SourceTree는 Git 저장소의 변경 사항, 브랜치, commit, push, pull 등을 GUI로 관리할 수 있게 해 주는 Git 클라이언트다.

## 이 위키에서의 맥락

Git Bash로 Git 명령어 흐름을 복습한 뒤, 같은 작업을 시각적으로 수행하기 위해 SourceTree를 설치하고 사용했다. 명령어에 익숙하지 않은 초반 협업 단계에서 저장소 상태를 눈으로 확인하는 데 도움이 된다.

## 학습 이력

- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04]]: SourceTree 설치, 저장소 연결, commit/push/pull 실습.

## 핵심 기능 / 특징

- 변경 파일 확인.
- stage/add, commit, push, pull.
- 브랜치와 원격 저장소 상태 확인.
- GitHub 협업 흐름을 GUI로 따라가기.

## 헷갈리는 점

- SourceTree는 Git 자체가 아니라 Git을 조작하는 GUI 도구다.
- 버튼을 눌러도 내부적으로는 `git add`, `git commit`, `git push`, `git pull` 같은 명령이 실행된다.
- GUI가 편해도 충돌이 나면 Git의 기본 개념을 알아야 해결할 수 있다.

## 관련 개념

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]

## 출처

- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
