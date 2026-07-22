---
title: 집 노트북 Git/Obsidian 설정
created: 2026-07-02
updated: 2026-07-22
type: meta
tags: [study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
  - wiki/_meta/hermes-default-profile-mode-system.md
status: growing
confidence: high
---
# 집 노트북 Git/Obsidian 설정

## 1. 현재 컴퓨터에서 먼저 할 일

### 1.1 Obsidian Git으로 최신 상태 push

Obsidian Git 플러그인에서 다음 순서로 처리한다.

```text
stage all → commit → push
```

또는 Git Bash에서 Vault 폴더로 이동한 뒤 확인할 수 있다.

```shell
cd /d/Study_LLM_Wiki
git status
git push
```

GitHub 저장소에 최신 파일이 올라갔는지 확인한다.

```text
https://github.com/Jesuisben/Study_LLM_Wiki.git
```

### 1.2 Hermes Desktop 완전히 종료

설정 파일과 DB를 복사하기 전에 Hermes Desktop을 완전히 종료한다.

이유:

- `state.db` 같은 SQLite DB가 사용 중일 수 있음
- `Local Storage`, `Preferences` 같은 Desktop 설정이 쓰기 중일 수 있음
- 실행 중 복사하면 일부 파일이 빠지거나 손상될 수 있음

가능하면 시스템 트레이에 남아 있는 Hermes도 종료한다.

## 4. 집 노트북에서 설치할 것

집 노트북에 먼저 설치한다.

1. Git for Windows
2. Obsidian
3. Hermes Agent / Hermes Desktop

GitHub push/pull을 편하게 하려면 Git Credential Manager가 포함된 Git for Windows 설치를 권장한다.

## 5. 집 노트북에서 LLM Wiki clone

집 노트북에는 D드라이브가 없으므로 C드라이브 아래 원하는 위치에 둔다.

추천 위치:

```text
C:\Users\집노트북사용자명\Documents\Study_LLM_Wiki
```

Git Bash에서 예시는 다음과 같다.

```shell
cd ~/Documents
git clone https://github.com/Jesuisben/Study_LLM_Wiki.git
```

clone 후 폴더 구조는 다음처럼 되어야 한다.

```text
Study_LLM_Wiki/
├── AGENTS.md
├── raw/
├── wiki/
└── .git/
```

## 6. 집 노트북에서 Obsidian Vault 열기

Obsidian에서 다음 순서로 연다.

```text
Open folder as vault → C:\Users\집노트북사용자명\Documents\Study_LLM_Wiki 선택
```

Community Plugins가 꺼져 있으면 다음을 확인한다.

1. Settings
2. Community plugins
3. Restricted mode 끄기
4. Obsidian Git 플러그인 enable

GitHub 로그인이 필요하면 Obsidian Git이 push/pull할 때 로그인 창을 띄울 수 있다.

## 9. Git 사용자 정보 확인

집 노트북 Git Bash에서 확인한다.

```shell
git config --global user.name
git config --global user.email
```

비어 있으면 설정한다.

```shell
git config --global user.name "Jesuisben"
git config --global user.email "[REDACTED]"
```

Vault 폴더에서 Git 상태를 확인한다.

```shell
cd ~/Documents/Study_LLM_Wiki
git status
git pull
```

`git pull` 또는 `git push` 중 GitHub 로그인이 뜨면 브라우저에서 로그인한다.

## 관련 페이지

- [[_meta/hermes-home-laptop-setup|집 노트북에 LLM Wiki와 Hermes Agent 환경 복제하기]]

## 출처

- `AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_meta/hermes-default-profile-mode-system.md`
