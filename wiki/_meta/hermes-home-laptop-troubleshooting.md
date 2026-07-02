---
title: 집 노트북 Hermes 이전 문제 해결
created: 2026-07-02
updated: 2026-07-02
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
# 집 노트북 Hermes 이전 문제 해결

## 12. 문제 상황별 해결

### Hermes가 여전히 D드라이브를 찾는 경우

`config.yaml`에서 `D:\Study_LLM_Wiki`가 남아 있는지 다시 검색한다.

바꿀 값:

```text
D:\Study_LLM_Wiki
```

새 값 예시:

```text
C:\Users\집노트북사용자명\Documents\Study_LLM_Wiki
```

### Git push가 안 되는 경우

1. GitHub 로그인 창이 뜨는지 확인
2. Obsidian Git 플러그인 enable 확인
3. Git Bash에서 직접 확인

```bash
git status
git pull
git push
```

### Hermes memory가 안 따라온 것 같은 경우

다음 파일/폴더가 복사되었는지 확인한다.

```text
AppData\Local\hermes\state.db
AppData\Local\hermes\skills\
AppData\Local\hermes\sessions\
```

그래도 안 되면 집 노트북에서 새로 작업하면서 `AGENTS.md`와 `wiki/`를 기준으로 이어가면 된다. LLM Wiki 운영 규칙 자체는 Vault 안에 보존되어 있다.

### 테마가 다르게 보이는 경우

Desktop UI 설정까지 맞추려면 다음 폴더도 복사되어야 한다.

```text
AppData\Roaming\Hermes
```

또는 Hermes 채팅창에서 다음을 사용한다.

```text
/skin list
/skin 테마이름
```

## 13. 최종 체크리스트

집 노트북에서 아래 항목을 확인한다.

- [ ] Git 설치 완료
- [ ] Obsidian 설치 완료
- [ ] Hermes 설치 완료
- [ ] GitHub에서 `Study_LLM_Wiki` clone 완료
- [ ] Obsidian에서 clone한 폴더를 Vault로 열었음
- [ ] `config.yaml`, `state.db`, `skills/`, `projects.db` 복사 완료
- [ ] `.env`, `auth.json`은 복사하지 않았음
- [ ] 집 노트북에서 OpenAI OAuth 새로 연결 완료
- [ ] 필요하면 `AppData\Roaming\Hermes` 복사 완료
- [ ] `config.yaml`의 `cwd`를 C드라이브 Vault 경로로 수정 완료
- [ ] GitHub pull/push 테스트 완료
- [ ] Hermes에서 새 채팅 열고 `AGENTS.md`, `wiki/index.md`, `wiki/log.md` 확인 요청 완료

## 한 줄 요약

```text
집 노트북에서는 Wiki는 GitHub에서 clone하고, Hermes는 인증 파일을 제외한 설정/기억/스킬 파일을 복사한 뒤, OpenAI OAuth는 새로 연결하고, config.yaml의 D:\Study_LLM_Wiki만 C드라이브의 실제 Vault 경로로 바꾸면 된다.
```

## 관련 페이지

- [[_meta/hermes-home-laptop-setup|집 노트북에 LLM Wiki와 Hermes Agent 환경 복제하기]]

## 출처

- `AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_meta/hermes-default-profile-mode-system.md`
