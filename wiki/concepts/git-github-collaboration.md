---
title: GitHub 협업 흐름
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [ci-cd, project]
sources:
  - raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md
  - raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md
status: growing
confidence: high
---

# GitHub 협업 흐름

## 정의

GitHub 협업 흐름은 각자 로컬에서 브랜치를 만들고 작업한 뒤 원격 저장소에 push하고, Pull Request로 변경 내용을 검토·병합하며, 병합된 기준 브랜치를 다시 pull해 최신 상태로 맞추는 절차다.

## 수업에서 배운 흐름

1. Git Bash 또는 SourceTree/IntelliJ에서 저장소를 준비한다.
2. 사용자 이름과 이메일을 설정한다.
3. 파일을 수정하고 `add → commit`으로 변경 이력을 만든다.
4. 원격 저장소에 `push`한다.
5. GitHub에서 Pull Request를 만든다.
6. 기준 브랜치에 merge한다.
7. 로컬 master/main에서 pull해 병합 결과를 가져온다.
8. 같은 파일 수정 시 충돌을 해결한다.

## 핵심 명령어

```bash
git init
git status
git config user.name "bluesky"
git config user.email "bluesky@naver.com"
git add myfile.txt
git commit -m "message"
git push -u origin master
git clone <repo-url>
git pull
git fetch
```

## Pull Request의 의미

Pull Request는 단순 업로드가 아니다. 브랜치에 올린 변경을 기준 브랜치에 합쳐도 되는지 요청하고, 리뷰·테스트·충돌 확인을 거쳐 병합하는 협업 절차다.

## 자주 헷갈리는 점

- push는 commit된 변경만 원격으로 보낸다. 수정만 하고 commit하지 않은 파일은 push되지 않는다.
- fetch는 원격 브랜치 정보를 가져오지만 현재 작업 파일을 바로 바꾸지 않는다. pull은 가져온 뒤 병합까지 진행한다.
- 충돌은 Git이 자동으로 한쪽을 고를 수 없을 때 생긴다. 같은 파일의 같은 근처를 여러 사람이 수정하면 발생하기 쉽다.
- SourceTree/IntelliJ는 Git의 GUI일 뿐, 내부 원리는 Git 명령과 같다.

## 관련 수업

- [[summaries/2026-05-04-git-github-sourcetree|2026-05-04 GitHub, Git Bash, SourceTree 협업 입문]]
- [[summaries/2026-05-06-github-branch-pr-conflict|2026-05-06 GitHub 브랜치, Pull Request, 충돌 해결]]
- [[entities/git|Git]]
- [[entities/github|GitHub]]
- [[entities/source-tree|SourceTree]]

## 출처

- `raw/Study/5. Linux/2026.05.04(월)/2026.05.04(월).md`
- `raw/Study/5. Linux/2026.05.06(수)/2026.05.06(수).md`
