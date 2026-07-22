---
title: 집 노트북 Hermes 설정 복사와 검증
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
# 집 노트북 Hermes 설정 복사와 검증

## 7. 집 노트북에 Hermes 설정 복사

### 7.1 Hermes 종료

집 노트북에서도 Hermes Desktop을 완전히 종료한다.

### 7.2 AppData 폴더에 복사

현재 컴퓨터에서 백업한 핵심 파일/폴더를 집 노트북의 사용자 폴더 아래로 복사한다.

현재 컴퓨터:

```text
C:\Users\ICT02-006\AppData\Local\hermes\config.yaml
C:\Users\ICT02-006\AppData\Local\hermes\state.db
C:\Users\ICT02-006\AppData\Local\hermes\skills\
C:\Users\ICT02-006\AppData\Local\hermes\projects.db
C:\Users\ICT02-006\AppData\Roaming\Hermes
```

집 노트북:

```text
C:\Users\집노트북사용자명\AppData\Local\hermes\config.yaml
C:\Users\집노트북사용자명\AppData\Local\hermes\state.db
C:\Users\집노트북사용자명\AppData\Local\hermes\skills\
C:\Users\집노트북사용자명\AppData\Local\hermes\projects.db
C:\Users\집노트북사용자명\AppData\Roaming\Hermes
```

이때 다음 파일은 복사하지 않는다.

```text
.env
auth.json
```

집 노트북에서는 Hermes 설치 후 OpenAI OAuth를 새로 연결한다.

이미 집 노트북에 같은 폴더가 있다면, 먼저 백업해두는 것이 안전하다.

예:

```text
hermes_backup_before_copy
Hermes_backup_before_copy
```

## 8. config.yaml에서 작업 폴더 경로 수정

가장 중요한 단계다.

현재 컴퓨터의 설정은 다음처럼 되어 있다.

```yaml
terminal:
  backend: local
  cwd: D:\Study_LLM_Wiki
```

집 노트북에는 D드라이브가 없으므로, 집 노트북의 실제 Vault 경로로 바꾼다.

예:

```yaml
terminal:
  backend: local
  cwd: C:\Users\집노트북사용자명\Documents\Study_LLM_Wiki
```

수정할 파일:

```text
C:\Users\집노트북사용자명\AppData\Local\hermes\config.yaml
```

`D:\Study_LLM_Wiki`가 다른 곳에도 들어 있을 수 있으므로, 설정 파일에서 `D:\Study_LLM_Wiki`를 검색해서 모두 집 노트북 경로로 바꾼다.

## 10. Hermes 실행 후 확인

Hermes Desktop을 실행한 뒤 새 채팅에서 이렇게 말한다.

```text
이 컴퓨터에서는 LLM Wiki 경로가 C:\Users\집노트북사용자명\Documents\Study_LLM_Wiki야.
AGENTS.md, wiki/index.md, wiki/log.md 읽고 현재 상태 확인해줘.
```

정상이라면 Hermes는 다음 규칙을 다시 따를 수 있다.

- `raw/`는 원본 자료라 수정하지 않음
- `wiki/`는 LLM이 생성/수정하는 지식 베이스
- 작업 시작 시 `AGENTS.md`, `wiki/index.md`, `wiki/log.md` 확인
- 새 페이지 생성 시 `wiki/index.md` 업데이트
- 의미 있는 작업 후 `wiki/log.md` 기록

## 11. 옮겨진 기억과 스킬 확인

Hermes 설정 폴더를 제대로 복사했다면 다음이 따라올 수 있다.

| 항목 | 따라오는 조건 |
|---|---|
| memory / user profile | `state.db` 또는 관련 memory 저장소 복사 |
| 과거 session 검색 | `state.db`, `sessions/` 복사 |
| skills | `skills/` 복사 |
| 모델/provider 설정 | `config.yaml` 복사 |
| OAuth/API 인증 | 복사하지 않고 집 노트북에서 새로 로그인 권장 |
| Desktop 테마/UI | `AppData\Roaming\Hermes` 복사 |

집 노트북에서는 OAuth/API 인증을 새로 설정한다.

```shell
hermes auth
```

또는 모델/provider 설정을 다시 연다.

```shell
hermes setup
hermes model
```

## 관련 페이지

- [[_meta/hermes-home-laptop-hermes-config-migration|집 노트북 Hermes 설정 마이그레이션]]
- [[_meta/hermes-home-laptop-troubleshooting|집 노트북 Hermes 이전 문제 해결]]

## 출처

- `AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_meta/hermes-default-profile-mode-system.md`
