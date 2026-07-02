---
title: 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [ci-cd, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
status: growing
confidence: high
---

# 2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결

## 한 줄 요약

팀원 역할로 브랜치를 만들고 커밋·푸시한 뒤 Pull Request를 보내 병합하고, master를 pull하며, 같은 파일 수정으로 생기는 충돌 상황을 실습했다.

## 배운 내용

- 팀원 계정의 Git 설정과 IntelliJ 프로젝트 설정을 확인했다.
- `animal`, `sport` 같은 신규 브랜치를 만들어 작업하고 원격으로 push했다.
- GitHub에서 Pull Request를 생성해 master로 병합하는 흐름을 실습했다.
- 병합된 master 브랜치를 로컬로 pull해 최신 상태로 맞췄다.
- fetch를 사용하면 원격 브랜치 정보가 로컬 Git 뷰에 갱신된다는 점을 확인했다.
- 같은 `Main.java`에 서로 다른 팀원이 다른 내용을 넣는 충돌 시나리오를 다뤘다.

## 핵심 실습 흐름

```bash
git config user.name "developer"
git config user.email "developer@daum.net"
# IntelliJ 또는 Git GUI에서 branch 생성 → commit → push
# GitHub에서 Pull Request 생성 → merge
# 로컬 master에서 pull
```

## 왜 중요한가

실무 협업은 한 사람이 master에 직접 push하는 방식보다 기능 브랜치를 만들고 Pull Request로 리뷰·병합하는 흐름을 많이 쓴다. 이 날의 실습은 이후 CI/CD와 팀 프로젝트 협업의 기본 규칙이 된다.

## 헷갈린 점 / 질문

- fetch는 원격 정보를 가져오지만 작업 파일을 바로 바꾸지는 않는다. pull은 fetch 후 현재 브랜치에 병합까지 진행한다.
- Pull Request는 “코드를 원격에 올리는 것”이 아니라, 이미 push된 브랜치를 기준 브랜치에 병합해 달라고 요청하는 절차다.
- 충돌은 Git이 어느 쪽 내용을 선택해야 할지 자동 판단할 수 없을 때 생긴다. 같은 파일의 같은 근처를 여러 사람이 수정하면 자주 발생한다.

## 관련 페이지

- [[concepts/git-github-collaboration|GitHub 협업 흐름]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]

## 출처

- `raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
