---
title: 집 노트북 Hermes 백업과 보안 원칙
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
# 집 노트북 Hermes 백업과 보안 원칙

## 2. 현재 컴퓨터에서 백업할 폴더

### 2.1 필수 백업: Hermes 로컬 홈 중 인증 파일을 제외한 핵심 파일

OpenAI OAuth는 집 노트북에서 새로 연결할 예정이므로, Hermes 로컬 홈 전체를 무조건 통째로 복사하기보다 **인증 파일을 제외하고** 필요한 파일/폴더를 복사하는 방식을 권장한다.

원본 폴더 위치:

```text
C:\Users\ICT02-006\AppData\Local\hermes
```

이 안에서 우선 복사할 항목은 다음이다.

| 파일/폴더 | 복사 여부 | 의미 |
|---|---:|---|
| `config.yaml` | 권장 | 모델, provider, 작업 폴더, 표시 설정 |
| `state.db` | 권장 | memory, user profile, session_search용 대화 DB |
| `skills/` | 권장 | Hermes가 쓰는 스킬들 |
| `projects.db` | 권장 | Desktop Project 정보 |
| `sessions/` | 선택 | 세션 관련 파일. 있으면 과거 세션 보존에 도움 |
| `profiles/` | 선택 | 별도 프로필을 만들었다면 해당 프로필 정보 |
| `hermes-agent/` | 보통 불필요 | Hermes Agent 설치본 / 소스 / venv. 집 노트북에 새로 설치하면 굳이 옮기지 않아도 됨 |
| `.env` | 제외 권장 | API 키와 환경변수. 집 노트북에서 새로 설정 |
| `auth.json` | 제외 권장 | OAuth 로그인 정보. 집 노트북에서 새로 로그인 |

따라서 권장 복사 목록은 다음이다.

```text
C:\Users\ICT02-006\AppData\Local\hermes\config.yaml
C:\Users\ICT02-006\AppData\Local\hermes\state.db
C:\Users\ICT02-006\AppData\Local\hermes\skills\
C:\Users\ICT02-006\AppData\Local\hermes\projects.db
```

선택 복사 목록:

```text
C:\Users\ICT02-006\AppData\Local\hermes\sessions\
C:\Users\ICT02-006\AppData\Local\hermes\profiles\
```

복사하지 않을 항목:

```text
C:\Users\ICT02-006\AppData\Local\hermes\.env
C:\Users\ICT02-006\AppData\Local\hermes\auth.json
```

### 2.2 선택 백업: Hermes Desktop UI 설정

Desktop 앱의 화면, 테마, localStorage까지 최대한 맞추고 싶으면 다음 폴더도 복사한다.

```text
C:\Users\ICT02-006\AppData\Roaming\Hermes
```

이 폴더에는 대략 다음이 들어 있다.

| 파일/폴더 | 의미 |
|---|---|
| `Preferences` | Electron 앱 설정 |
| `Local Storage/` | Desktop 테마, UI localStorage 설정 가능성 |
| `window-state.json` | 창 위치/크기 |
| `native-theme.json` | 네이티브 테마 설정 |
| `composer-images/` | 채팅에 붙였던 이미지 캐시 |

## 3. 보안 주의사항

OpenAI OAuth와 API 인증은 집 노트북에서 새로 연결할 예정이라면 다음 파일은 **옮기지 않는다.**

```text
C:\Users\ICT02-006\AppData\Local\hermes\.env
C:\Users\ICT02-006\AppData\Local\hermes\auth.json
```

이 두 파일은 비밀번호처럼 취급한다.

주의:

- 절대 GitHub에 올리지 않는다.
- 공개 클라우드 폴더에 올리지 않는다.
- 집 노트북에서 OpenAI OAuth를 새로 연결할 거라면 복사하지 않는다.

다음 파일도 대화 기록과 memory가 들어 있을 수 있으므로 민감한 파일로 취급한다. 다만 현재 환경의 기억을 이어가려면 복사 대상이다.

```text
C:\Users\ICT02-006\AppData\Local\hermes\state.db
```

특히 `.env`, `auth.json`에는 API 키나 OAuth 토큰이 들어 있을 수 있다.

## 관련 페이지

- [[_meta/hermes-home-laptop-hermes-config-migration|집 노트북 Hermes 설정 마이그레이션]]

## 출처

- `AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_meta/hermes-default-profile-mode-system.md`
