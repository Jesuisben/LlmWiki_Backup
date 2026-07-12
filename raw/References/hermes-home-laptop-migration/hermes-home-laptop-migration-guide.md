# 집 노트북으로 Hermes Agent를 거의 같은 상태로 옮기는 안내서

> 작성일: 2026-07-12  
> 기준 컴퓨터: 현재 학원/작업용 Windows 10 PC  
> 현재 확인한 Hermes: `Hermes Agent v0.18.2 (2026.7.7.2) · upstream b4829643`

> [!IMPORTANT]
> 집 PC는 가능하면 같은 버전 또는 호환되는 최신 버전으로 설치한다. 먼저 `hermes --version`으로 설치 상태를 확인한 뒤, 이 문서의 경로·파일 구성을 기준으로 복원한다.

## 0. 결론: 무엇을 옮겨야 “같은 나”에 가까운가

Hermes는 설치 프로그램 자체만으로 성격·기억·기술이 복원되지 않는다. **설치된 Hermes 코드**와 별도로 Hermes Home(설정/상태 폴더)에 다음이 들어 있기 때문이다.

| 복원 대상 | 핵심 파일/폴더 | 왜 필요한가 | 집 PC로 복사 권장 |
|---|---|---|---|
| 기본 모델·도구·승인·표시 설정 | `config.yaml` | 모델, 도구 활성화, safe/smart/danger 운영 방식과 관련된 설정 기반 | 예 |
| 에이전트의 정체성/상시 규칙 | `SOUL.md` | 모든 작업에 적용되는 개인화된 정체성 규칙 | 예 |
| 장기 메모리 | `memories/MEMORY.md`, `memories/USER.md` | 사용자의 선호, 환경, 작업에서 축적한 안정적인 기억 | **예 — 가장 중요** |
| 스킬 | `skills/` | TXT→MD 변환, LLM Wiki, Hermes 설정, 개발 작업 등의 재사용 절차 | **예 — 가장 중요** |
| API 키·환경 설정 | `.env` | provider API key, Windows Git Bash 경로 등 | 조건부 예: 비밀 파일로 별도 이관 |
| OAuth 인증/credential pool | `auth.json` | OAuth 로그인 기반 provider 인증 | 조건부 예: 복사 후 재로그인 가능성 있음 |
| 예약 작업 | `cron/` | 실제 생성된 cron job이 있을 때만 | 현재는 job 파일이 확인되지 않아 불필요 |
| Desktop 프로젝트 목록 | `projects.db` | Hermes Desktop의 Project 이름/루트 경로 목록 | 조건부: 두 PC의 Vault 경로가 같을 때만 |
| 대화 기록 전체 | `state.db` | 과거 세션, `session_search` 검색 대상 | 선택: 약 86 MB, 원하면 복사 |

즉, **“집에서도 지금의 에이전트처럼 행동하게”** 만들려면 최소한 다음 5가지를 옮긴다.

1. `config.yaml`
2. `SOUL.md`
3. `memories/`
4. `skills/`
5. `.env` 및 필요 시 `auth.json`

그리고 집 노트북에서 `D:\Study_LLM_Wiki` Vault를 Git clone으로 같은 경로에 복원하면, Vault의 `AGENTS.md`, `wiki/`, `raw/`까지 함께 읽는 현재 작업 방식도 이어진다.

---

## 1. 이 문서의 전제와 안전 원칙

### 현재 PC에서 확인한 사실

- Hermes Home: `C:\Users\ICT02-006\AppData\Local\hermes`
- `default` 프로필만 존재한다.
- 현재 모델 표시: `gpt-5.6-terra`
- Hermes는 **Windows Native 설치**다. WSL의 `~/.hermes`가 아니라 `%LOCALAPPDATA%\hermes`를 사용한다.
- 현재 설치 방식은 git install이며 Hermes source는 다음에 있다.
  - `C:\Users\ICT02-006\AppData\Local\hermes\hermes-agent`
- 메모리 파일과 `SOUL.md`가 존재한다.
- `skills/`에는 번들 스킬과 사용자/에이전트가 누적한 스킬이 존재한다.
- `plugins/`에는 현재 별도 파일이 없다.
- `cron/`에는 잠금/heartbeat 파일만 확인되며, 이 시점에는 옮길 실작업 job 파일이 확인되지 않았다.
- `state.db`는 약 86 MB이다. 대화 히스토리까지 완전히 옮기려는 경우에만 포함한다.

### 절대로 평문으로 올리지 말 것

다음 파일에는 API key, OAuth token 또는 개인적인 대화/인증 정보가 들어갈 수 있다.

- `C:\Users\ICT02-006\AppData\Local\hermes\.env`
- `C:\Users\ICT02-006\AppData\Local\hermes\auth.json`
- `C:\Users\ICT02-006\AppData\Local\hermes\state.db`
- `C:\Users\ICT02-006\AppData\Local\hermes\memories\`

따라서 이 파일들을 다음 위치에 올리면 안 된다.

- GitHub/Git 원격 저장소
- Obsidian Vault의 Git 관리 대상 폴더
- 공개 클라우드 공유 링크
- 채팅창, 스크린샷, 커밋 메시지

집 노트북 이관은 **암호화된 USB**, BitLocker가 켜진 개인 저장장치, 또는 본인만 접근 가능한 암호화 압축파일을 사용한다. `raw/References/` 아래의 이 문서는 이관 방법을 설명하는 문서일 뿐, 비밀값이나 실제 설정 내용을 담지 않는다.

---

## 2. 권장 전략: 새 설치 후 “선별 덮어쓰기”

### 왜 Hermes 폴더 전체를 통째로 복사하지 않는가

`C:\Users\ICT02-006\AppData\Local\hermes` 전체에는 아래처럼 **새 PC에서 재생성하는 편이 좋은 것**도 섞여 있다.

- `hermes-agent/` — 설치된 코드, Python virtualenv, OS/버전 의존 파일
- `bin/`, `lsp/` — 실행 파일 및 설치 산출물
- `cache/` — 모델 메타데이터·임시 파일
- `logs/` — 과거 로그와 잠금 파일
- `state.db-wal`, `state.db-shm` — 실행 중 SQLite 임시 파일
- `processes.json` — 이미 종료된 프로세스 정보일 수 있음
- `state-snapshots/`, `verification_evidence.db` — 선택적 과거 상태/증거

이것들을 무작정 덮어쓰면, 새 PC의 설치 버전과 충돌하거나 경로가 꼬일 수 있다.

### 권장 순서

1. 집 노트북에 Hermes를 **정상 설치하고 한 번 실행**한다.
2. 집 노트북에서 Hermes Desktop/CLI를 **완전히 종료**한다.
3. 현재 PC의 `default` 상태 파일 중 필요한 것만 안전한 오프라인 매체로 복사한다.
4. 집 노트북의 Hermes Home에 같은 상대경로로 **덮어쓴다**.
5. 다시 실행하여 `hermes doctor`, `hermes tools list`, `hermes skills list`로 확인한다.
6. 인증만 실패하면 `.env`/`auth.json`만 다시 검토하거나 `hermes auth`로 재로그인한다.

이 방식은 “성격·기억·스킬·설정”은 최대한 동일하게 가져오면서, 새 PC의 실행 환경은 새 설치로 깨끗하게 유지한다.

---

## 3. 집 노트북 사전 준비

### 3.1 Windows 계정과 경로

이 문서는 집 노트북도 **Windows Native Hermes**를 사용하는 것을 전제로 한다.

집 PC의 사용자명이 현재 PC와 달라도 괜찮다. 예를 들어 집 계정이 `HOMEUSER`이면 Hermes Home은 일반적으로 다음 위치가 된다.

- 현재 PC: `C:\Users\ICT02-006\AppData\Local\hermes`
- 집 PC 예시: `C:\Users\HOMEUSER\AppData\Local\hermes`

중요한 것은 사용자명까지 똑같이 맞추는 것이 아니라, **집 PC에서 `%LOCALAPPDATA%\hermes`라는 실제 Hermes Home에 파일을 넣는 것**이다.

PowerShell에서 현재 집 PC의 Hermes Home 후보를 확인할 때:

```powershell
$env:LOCALAPPDATA + "\hermes"
```

Git Bash에서는 다음처럼 확인할 수 있다.

```bash
echo "$LOCALAPPDATA/hermes"
```

### 3.2 Git과 Obsidian

Vault 작업을 바로 이어가려면 집 PC에 다음을 준비한다.

- Git for Windows
- Obsidian
- GitHub 인증(기존 원격 Vault를 clone/pull 할 수 있는 계정)
- 가능하면 현재와 같은 드라이브 경로: `D:\Study_LLM_Wiki`

> [!TIP]
> `projects.db`까지 똑같이 사용하고 싶다면 Vault를 **정확히 `D:\Study_LLM_Wiki`**로 clone하는 편이 가장 안전하다. 경로가 `C:\Users\...\Documents\Study_LLM_Wiki`처럼 달라져도 Vault 자체는 정상 동작하지만, Desktop Project DB가 옛 경로를 가리킬 수 있다.

### 3.3 Git Bash 설치 확인

현재 에이전트에는 Windows의 WSL shim 대신 Git Bash를 쓰도록 하는 설정이 들어 있다. 집 PC에도 Git for Windows를 설치하고 다음 파일이 있는지 확인한다.

- `C:\Program Files\Git\bin\bash.exe`

파일이 없다면 Git for Windows를 먼저 설치한다. Hermes의 terminal/file 도구가 `WSL ... execvpe(/bin/bash) failed`와 비슷한 오류를 낼 때 이 항목이 특히 중요하다.

---

## 4. 집 노트북에 Hermes 설치

### 4.1 설치 전 주의

- 현재 PC의 `hermes-agent/` 폴더나 `venv/`를 집 PC로 복사하지 않는다.
- 집 노트북에서는 공식 설치 스크립트로 **자기 PC 환경에 맞는 Hermes**를 먼저 설치한다.
- 설치 직후의 setup wizard에서 모델 설정을 해도 되지만, 아래 복원 파일을 덮어쓸 예정이므로 최소 설정만 하고 넘어가도 된다.

### 4.2 Windows Native 공식 설치

집 노트북에서 **PowerShell 또는 Windows Terminal**을 열고 실행한다.

```powershell
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)
```

설치가 끝나면 PowerShell/Windows Terminal을 **완전히 닫았다가 새로 열고** 다음을 실행한다.

```powershell
hermes --version
hermes config path
hermes config env-path
hermes doctor
```

정상이라면 `hermes config path`가 집 PC 사용자 계정 아래의 다음과 비슷한 경로를 보여준다.

```text
C:\Users\<집PC사용자명>\AppData\Local\hermes\config.yaml
```

### 4.3 설치 직후 한 번 실행해야 하는 이유

설치 직후 `hermes` 또는 Hermes Desktop을 한 번 실행하면 기본 폴더·번들 스킬·기본 설정이 생성된다. 그 뒤 종료하고 개인화 상태를 덮어쓰는 것이 안전하다.

Desktop 사용 시:

1. Hermes Desktop을 실행한다.
2. 첫 설정 화면이 나오면 최소한으로 진행하거나 종료한다.
3. 창만 닫지 말고, 트레이 아이콘/백그라운드 프로세스도 종료한다.

CLI 사용 시:

```powershell
hermes
```

한 번 열었다가 `/exit`로 종료한다.

---

## 5. 현재 PC에서 만들 이관 묶음

### 5.1 먼저 Hermes를 완전히 종료한다

현재 PC에서 다음을 먼저 한다.

1. Hermes Desktop의 열린 대화창을 모두 닫는다.
2. 시스템 트레이에 Hermes가 남아 있다면 종료한다.
3. Hermes CLI가 열린 터미널도 `/exit`로 종료한다.
4. gateway를 별도로 사용 중이라면 `hermes gateway stop`으로 멈춘다.

이 과정이 중요한 이유는 `state.db`가 SQLite DB이기 때문이다. 실행 중에 파일만 일부 복사하면 DB 본문과 `state.db-wal`이 어긋날 수 있다.

### 5.2 이관 폴더 구조 만들기

암호화 USB 또는 암호화된 개인 폴더에 다음 구조를 만든다. 예시는 `E:` USB를 사용한다.

```text
E:\Hermes-Migration-2026-07-12\
├── core\
│   ├── config.yaml
│   ├── SOUL.md
│   ├── memories\
│   │   ├── MEMORY.md
│   │   └── USER.md
│   └── skills\
├── secrets\
│   ├── .env
│   └── auth.json
├── optional\
│   ├── state.db
│   └── projects.db
└── README-local.txt
```

`README-local.txt`에는 비밀값을 쓰지 말고, 단지 “이 USB는 Hermes 개인 설정 이관용. Git에 올리지 말 것.” 정도만 적는다.

### 5.3 복사할 파일 목록

다음 표의 **현재 PC 원본**을 위 이관 폴더의 같은 상대 구조로 복사한다.

| 우선순위 | 현재 PC 원본 | 이관 폴더 목적지 | 집 PC에서의 처리 |
|---|---|---|---|
| 필수 | `C:\Users\ICT02-006\AppData\Local\hermes\config.yaml` | `core\config.yaml` | `...\hermes\config.yaml`에 덮어쓰기 |
| 필수 | `C:\Users\ICT02-006\AppData\Local\hermes\SOUL.md` | `core\SOUL.md` | `...\hermes\SOUL.md`에 덮어쓰기 |
| 필수 | `...\hermes\memories\MEMORY.md` | `core\memories\MEMORY.md` | 덮어쓰기 |
| 필수 | `...\hermes\memories\USER.md` | `core\memories\USER.md` | 덮어쓰기 |
| 필수 | `...\hermes\skills\` 전체 | `core\skills\` 전체 | 병합/덮어쓰기 |
| 조건부 | `...\hermes\.env` | `secrets\.env` | 별도 보안 이관 후 덮어쓰기 |
| 조건부 | `...\hermes\auth.json` | `secrets\auth.json` | 별도 보안 이관 후 덮어쓰기 |
| 선택 | `...\hermes\state.db` | `optional\state.db` | 과거 대화도 보존할 때 덮어쓰기 |
| 선택 | `...\hermes\projects.db` | `optional\projects.db` | Vault 절대경로가 같을 때만 덮어쓰기 |

### 5.4 `skills/`는 왜 전체를 복사하는가

현재 Hermes 설치는 번들 스킬과 사용 중 누적된 스킬을 `skills/` 아래에 저장한다. 특히 이 Vault 작업에 필요한 다음 성격의 스킬/규칙이 여기에서 복원된다.

- LLM Wiki Vault 작업 절차
- Hermes Agent 설정/문제 해결 절차
- TXT→MD 변환의 민감정보 검사, canonical 샘플 비교, fence/Markdown 검증 규칙
- 한국어 응답/승인 안내 스타일
- 개발, GitHub, 문서, 연구 등의 하위 스킬

집 PC의 새 설치에도 번들 스킬이 생기지만, **현재 PC에서 수정·추가·사용 이력이 반영된 상태**와 완전히 일치하려면 `skills/` 전체를 복사해야 한다.

집 PC에서 `skills/`를 처리하는 방법은 다음과 같다.

- `skills` 폴더 자체를 삭제하지 않는다.
- `core\skills\` 안의 내용을 집 PC의 `...\hermes\skills\`에 복사한다.
- Windows Explorer에서 “대상에 같은 이름의 파일이 있습니다”가 나오면 **파일 덮어쓰기**를 선택한다.
- 기존 집 PC에서 새로 만든 스킬이 있다면, 복사 전에 별도 백업한다. 현재 PC와 집 PC의 스킬이 서로 다르면 무작정 양방향 병합하지 말고, 현재 PC를 정본으로 삼을지 먼저 정한다.

---

## 6. 비밀 파일: `.env`와 `auth.json`의 정확한 의미

### 6.1 `.env`: 복사해도 되나?

**개인 소유의 두 노트북이며, 암호화된 개인 매체로만 옮긴다면 복사할 수 있다.** 이 파일에는 모델/provider API key, 환경 변수, 도구 설정에 필요한 값이 들어갈 수 있다.

현재 작업 환경에서 특히 의미 있는 항목은 Git Bash 경로 고정이다.

```env
HERMES_GIT_BASH_PATH=C:\Program Files\Git\bin\bash.exe
```

집 PC에도 Git for Windows가 같은 기본 경로에 설치되어 있다면 `.env`를 그대로 덮어써도 된다. 설치 경로가 다르면 이 줄만 실제 경로로 수정한다.

> [!WARNING]
> `.env`를 Git에 commit/push하거나 Obsidian Vault 안에 저장하지 않는다. 이름에 `.env`가 들어간 복사본도 동일하게 취급한다.

### 6.2 `auth.json`: 복사해도 되나?

`auth.json`은 OAuth 기반 provider 로그인과 credential pool을 담을 수 있다. 같은 사용자 본인의 집 노트북으로 옮기는 경우에는 복사할 수 있지만, provider가 기기 변경·토큰 만료·추가 인증을 요구하면 집 PC에서 다시 로그인해야 할 수 있다.

복사 뒤 모델 호출이 실패하면 순서대로 확인한다.

```powershell
hermes doctor
hermes auth
hermes model
```

- `auth.json`을 복사했는데도 인증 실패: `hermes auth`로 해당 provider를 다시 인증한다.
- `.env` 기반 API key provider: `.env` 경로와 키 이름을 확인한다.
- 모델 목록/권한이 다름: `hermes model`에서 현재 계정으로 다시 선택한다.

### 6.3 다른 사람 PC에는 절대 그대로 복사하지 않는다

친구/팀원/다른 사용자에게 “같은 에이전트”를 배포할 때는 `.env`, `auth.json`, `memories/`, `state.db`를 빼야 한다. 그런 경우에는 Hermes의 **Profile Distribution** 방식을 사용하고, 각 사용자가 자신의 API key를 입력하게 해야 한다.

이번 작업은 본인 집 노트북으로의 개인 이관이므로, 비밀 파일 복사는 가능하되 보안 매체만 사용한다.

---

## 7. 집 노트북에서 실제 덮어쓰기 절차

### 7.1 사전 조건 체크

다음 세 가지가 모두 끝난 상태에서 진행한다.

- [ ] 집 PC Hermes 설치 완료
- [ ] 집 PC Hermes를 한 번 실행 후 완전 종료
- [ ] 현재 PC에서도 Hermes가 완전 종료된 상태에서 이관 폴더 생성 완료

### 7.2 집 PC의 Hermes Home 경로 확인

집 PC PowerShell에서 실행한다.

```powershell
hermes config path
hermes config env-path
```

예시 결과:

```text
C:\Users\HOMEUSER\AppData\Local\hermes\config.yaml
C:\Users\HOMEUSER\AppData\Local\hermes\.env
```

그러면 집 PC Hermes Home은 다음이다.

```text
C:\Users\HOMEUSER\AppData\Local\hermes
```

이 아래로 다음 파일을 복사한다.

### 7.3 Explorer로 복사하는 가장 쉬운 방법

1. Hermes Desktop/CLI가 실행 중이 아닌지 다시 확인한다.
2. USB의 `core\config.yaml`을 집 PC Hermes Home 루트에 붙여넣는다.
3. `SOUL.md`도 같은 루트에 붙여넣는다.
4. `core\memories\`를 집 PC Hermes Home의 `memories\`에 붙여넣고, 동일 파일은 덮어쓴다.
5. `core\skills\` 안의 내용을 집 PC Hermes Home의 `skills\`에 붙여넣고, 동일 파일은 덮어쓴다.
6. `secrets\.env`, `secrets\auth.json`은 필요할 때만 같은 루트에 붙여넣어 덮어쓴다.
7. 선택한 경우 `optional\state.db`, `optional\projects.db`를 같은 루트에 붙여넣는다.

### 7.4 명령으로 복사하는 방법 (PowerShell)

아래는 이관 USB가 `E:`이고 집 Hermes Home이 기본 경로라는 예시다. 실행 전 `E:`와 사용자명을 실제 값으로 바꾼다.

```powershell
$source = "E:\Hermes-Migration-2026-07-12"
$home = Join-Path $env:LOCALAPPDATA "hermes"

Copy-Item "$source\core\config.yaml" "$home\config.yaml" -Force
Copy-Item "$source\core\SOUL.md" "$home\SOUL.md" -Force
Copy-Item "$source\core\memories\*" "$home\memories\" -Recurse -Force
Copy-Item "$source\core\skills\*" "$home\skills\" -Recurse -Force

# 본인 기기 사이의 암호화 이관일 때만 실행
Copy-Item "$source\secrets\.env" "$home\.env" -Force
Copy-Item "$source\secrets\auth.json" "$home\auth.json" -Force

# 과거 대화와 Project 목록까지 원할 때만 실행
Copy-Item "$source\optional\state.db" "$home\state.db" -Force
Copy-Item "$source\optional\projects.db" "$home\projects.db" -Force
```

> [!WARNING]
> `state.db-wal`, `state.db-shm`, `auth.lock`, `*.lock`, `cache/`, `logs/`는 복사 명령에 넣지 않는다. 실행 중인 임시 상태라 새 PC에 옮길 가치가 없거나 충돌할 수 있다.

---

## 8. `state.db`를 옮길지 결정하는 기준

### 옮기지 않는 경우 (기본 권장)

다음 목적이면 `state.db`는 필요 없다.

- 집 PC에서 새 대화를 시작해도 됨
- 메모리/스킬/설정만 같으면 됨
- `session_search`로 현재 PC의 과거 대화를 집에서도 검색할 필요 없음
- 이관 용량과 민감한 대화 데이터 노출 범위를 줄이고 싶음

이 경우에도 `MEMORY.md`, `USER.md`, `SOUL.md`, `skills/`가 있으면 “현재의 나와 비슷한 작업 방식”은 대부분 복원된다.

### 옮기는 경우

다음이 필요하다면 `state.db`도 옮긴다.

- 집 PC에서도 기존 대화 세션을 이어서 보고 싶음
- `session_search`로 예전 작업 내용을 찾아야 함
- 과거 대화에만 남아 있고 메모리/스킬에 정리되지 않은 맥락도 보존하고 싶음

반드시 두 컴퓨터의 Hermes를 모두 종료한 뒤 `state.db`만 복사한다. 집 PC에서 이미 새 대화를 만들었다면 덮어쓰기 전에 집 PC의 `state.db`를 별도로 백업해 둔다.

> [!NOTE]
> `state.db`를 옮겨도 현재 Desktop에서 열려 있던 “실행 중 세션”이 자동으로 이어지는 것은 아니다. 그러나 세션 이력과 검색 가능한 대화 데이터는 복원 대상이 된다.

---

## 9. `projects.db`와 LLM Wiki Project 복원

### 9.1 가장 안정적인 방식: Vault부터 같은 경로로 Git clone

집 PC에서 GitHub 원격 저장소를 clone하여 다음 경로를 만든다.

```text
D:\Study_LLM_Wiki
```

그 안에는 최소한 다음이 있어야 한다.

```text
D:\Study_LLM_Wiki\
├── AGENTS.md
├── raw\
│   ├── KoreaICT\
│   ├── PersonalStudy\
│   ├── PersonalProjects\
│   └── References\
└── wiki\
    ├── index.md
    └── log.md
```

이 Vault의 핵심은 다음과 같다.

- `raw/`는 사용자가 관리하는 원본 레이어이며 보통 읽기 전용이다.
- `wiki/`는 Hermes가 요약·개념·비교·질문 지식을 유지하는 레이어다.
- `AGENTS.md`는 이 Vault에서의 작업 규칙과 TXT→MD/위키 운영 경계를 제공한다.
- `wiki/index.md`, `wiki/log.md`는 세션 시작 시 과거 맥락 복원에 쓰인다.

### 9.2 Hermes Desktop에서 Project를 새로 연결하는 방법

Vault clone이 끝난 뒤 Hermes Desktop에서 Project를 새로 만든다.

- Project 이름: 예) `LLM Wiki`
- Primary folder: `D:\Study_LLM_Wiki`

이 방법은 `projects.db`를 복사하지 않아도 안전하게 작동한다. 같은 Vault를 정확히 같은 경로에 두었다면, 이전 Project DB를 복사하는 것보다 새 Project 연결이 오히려 단순할 수 있다.

### 9.3 `projects.db`를 복사해도 되는 경우

다음 조건을 만족할 때만 `projects.db`도 덮어쓴다.

- Vault 경로가 현재 PC와 집 PC에서 모두 `D:\Study_LLM_Wiki`이다.
- 집 PC에서 새로 만든 Hermes Desktop Project 정보가 아직 중요하지 않다.
- Desktop Project 이름/연결 정보를 최대한 똑같이 가져오고 싶다.

경로가 다르면 복사하지 말고 Desktop에서 Project를 새로 만든다. `projects.db`에는 프로젝트의 **절대 경로**가 저장될 수 있기 때문이다.

---

## 10. 복원 뒤 반드시 실행할 검증

집 PC에서 Hermes를 다시 실행한 다음 아래를 확인한다.

### 10.1 기본 설치/설정 확인

```powershell
hermes --version
hermes config path
hermes doctor
hermes profile list
```

기대 결과:

- `hermes --version`이 정상 출력된다.
- 프로필 목록에 `default`가 보인다.
- `hermes doctor`가 치명적인 설치 오류를 보고하지 않는다.

### 10.2 모델과 인증 확인

```powershell
hermes model
hermes auth
```

확인할 것:

- 현재와 같은 provider/model을 선택할 수 있는가
- OAuth/API key가 인식되는가
- 모델 호출 시 인증 오류가 나지 않는가

인증 오류가 난다고 해서 메모리/스킬 복원이 실패한 것은 아니다. 인증은 provider가 기기 변경을 감지해 재로그인을 요구한 것일 수 있다.

### 10.3 도구와 스킬 확인

```powershell
hermes tools list
hermes skills list
```

현재 PC에서 활성화되어 있던 대표 도구는 web, browser, terminal, file, code execution, vision, image generation, TTS, skills, todo, memory, session search, clarify, delegation, cron, computer use다. 집 PC에서 목록이 크게 다르면 `config.yaml`/설치 버전/도구 요구조건을 확인한다.

### 10.4 메모리와 정체성 확인

새 대화에서 다음처럼 테스트한다.

```text
내 기본 응답 언어와 답변 스타일, 그리고 LLM Wiki 작업 원칙을 짧게 알려줘.
```

기대하는 확인 포인트:

- 한국어가 기본 응답 언어로 나온다.
- 결론 우선·간결한 형식이라는 선호가 반영된다.
- `D:\Study_LLM_Wiki`에서 `raw/`는 원칙적으로 수정하지 않고, `wiki/` 관리 규칙을 따른다고 설명한다.

### 10.5 LLM Wiki 연결 테스트

Hermes Desktop에서 Project가 `D:\Study_LLM_Wiki`인지 확인한 뒤, 새 채팅에서 다음을 요청한다.

```text
이 Vault의 AGENTS.md, wiki/index.md, wiki/log.md를 읽고 현재 위키 상태를 짧게 요약해줘. 파일은 수정하지 마.
```

정상이라면 Hermes가 Vault의 규칙과 최근 로그를 바탕으로 답한다.

---

## 11. 집에서 TXT → MD 변환을 할 때의 핵심 주의사항

현재 LLM Wiki에는 TXT→MD 작업에 대한 엄격한 규칙이 있다. 집 PC에 스킬·메모리·Vault를 복원한 뒤에도 다음 핵심 원칙을 지켜야 한다.

1. 외부 학원 원본 TXT와 Vault의 `raw/`는 일반적으로 수정하지 않는다.
2. 변환 작업을 명시적으로 요청한 경우에만 `raw/KoreaICT/...`의 대응 Markdown 결과를 생성/덮어쓴다.
3. 변환 전에 **실제 외부 원본 TXT만** 민감정보 후보 검사를 한다.
4. `비밀번호`, `password`, `passwd`, `암호` 등의 문맥 뒤에 실제 값이 있으면 길이와 관계없이 후보로 보고한다.
5. 후보가 하나라도 있으면 원본 전체 경로, 실제 줄 번호, 감지 근거, 비밀값만 `{MASKED}` 처리한 원문을 모두 보고하고 사용자의 명시 재개 전에는 변환하지 않는다.
6. 확정된 수동 변환 MD 샘플을 canonical 기준으로 대조한다.
7. 코드/명령/출력만 fenced code block으로 감싼다. 설명문을 코드 fence에 넣지 않는다.
8. fence 언어는 과목 이름이 아니라 각 block의 실제 문법으로 결정한다.
9. Markdown prose에서 렌더링을 바꾸는 기호와 줄 시작 `N.` 등의 escape 규칙을 검증한다.
10. 완료라고 말하기 전에는 원본 대응, fence 경계, prose/코드 분류, Markdown 렌더링 안전성까지 검사한다.

이 규칙의 상세 절차는 복원된 Hermes `skills/`와 Vault의 `AGENTS.md`에 존재한다. 집 PC에서 변환을 시작할 때도 **먼저 해당 규칙을 읽고**, 대상 범위를 한 과목/한 세션 단위로 작게 잡는다.

---

## 12. 자주 생기는 문제와 해결 순서

### 문제 A. `hermes` 명령을 찾을 수 없음

증상:

```text
hermes : The term 'hermes' is not recognized ...
```

해결:

1. 설치 직후 열어 둔 PowerShell을 닫는다.
2. 새 PowerShell/Windows Terminal을 연다.
3. 다시 `hermes --version`을 실행한다.
4. 계속 실패하면 공식 설치 스크립트를 다시 실행하고 PATH 반영 여부를 확인한다.

### 문제 B. terminal/file 도구에서 WSL bash 오류

증상 예:

```text
WSL ... execvpe(/bin/bash) failed
```

원인: Windows가 Git Bash보다 `C:\Windows\System32\bash.exe` WSL shim을 먼저 잡는 경우가 있다.

해결:

1. Git for Windows를 설치한다.
2. 실제 Git Bash 경로를 확인한다.

```text
C:\Program Files\Git\bin\bash.exe
```

3. 집 PC Hermes의 다음 파일에 아래 값을 넣는다.

```text
C:\Users\<집PC사용자명>\AppData\Local\hermes\.env
```

```env
HERMES_GIT_BASH_PATH=C:\Program Files\Git\bin\bash.exe
```

4. Hermes Desktop/CLI를 완전히 종료했다가 다시 실행한다.

### 문제 C. 메모리/스킬이 현재 PC와 다르게 보임

점검 순서:

1. 집 PC Hermes가 완전히 종료된 상태에서 복사했는지 확인한다.
2. `memories/MEMORY.md`, `memories/USER.md`, `SOUL.md`가 집 Hermes Home에 있는지 확인한다.
3. `skills/` 폴더 안의 내용이 실제로 복사됐는지 확인한다.
4. 새 세션을 시작한다. 도구/스킬 설정은 기존 대화 중간에 즉시 바뀌지 않을 수 있다.
5. `hermes skills list`를 실행한다.

### 문제 D. 모델 인증만 실패함

점검 순서:

1. `.env`가 의도한 집 PC Hermes Home에 있는지 확인한다.
2. `auth.json`을 복사했다면 provider 토큰 만료 가능성을 고려한다.
3. `hermes auth`에서 재로그인한다.
4. `hermes model`에서 provider/model을 다시 고른다.
5. `hermes doctor`를 실행한다.

### 문제 E. Desktop Project가 Vault를 못 찾음

점검 순서:

1. `D:\Study_LLM_Wiki`에 실제 clone이 있는지 확인한다.
2. `AGENTS.md`가 Vault 루트에 있는지 확인한다.
3. Hermes Desktop에서 Project의 Primary folder를 `D:\Study_LLM_Wiki`로 새로 지정한다.
4. `projects.db`를 복사했다면, 옛 PC 절대 경로가 남았을 수 있으므로 새 Project로 다시 연결한다.

---

## 13. “완전히 같은 상태”를 위한 선택지

### 선택 1 — 권장: 실사용 동일성만 복원

복사:

- `config.yaml`
- `SOUL.md`
- `memories/`
- `skills/`
- `.env`, `auth.json` (개인 보안 이관)
- Vault Git clone

결과:

- 행동 방식, 장기 기억, 스킬, 모델/도구 설정을 거의 동일하게 사용한다.
- 집 PC에서는 새 대화 기록부터 시작한다.
- 가장 관리하기 쉽고 안전하다.

### 선택 2 — 과거 대화 검색까지 복원

선택 1 + `state.db`

결과:

- 기존 세션 이력과 `session_search` 맥락도 집 PC에 가져온다.
- 대화 데이터가 포함되므로 보안과 복사 시점(SQLite 종료)을 더 엄격히 관리해야 한다.

### 선택 3 — Hermes 기본 기능을 이용한 전체 백업/복원

현재 PC에서 Hermes가 완전히 종료된 상태 또는 안내에 따라 다음 명령을 사용할 수 있다.

```powershell
hermes backup -o "E:\Hermes-Migration-2026-07-12\hermes-full-backup.zip"
```

`hermes backup`은 Hermes configuration, skills, sessions, data를 archive로 만든다. 다만 Hermes codebase는 제외된다. 집 PC에는 먼저 Hermes를 설치해야 한다.

이 문서는 파일별 선별 이관을 기본으로 설명했지만, 전체 백업은 추가 안전망으로 유용하다. 단, backup zip도 비밀·대화 데이터를 포함할 수 있으므로 GitHub나 공유 드라이브에 올리지 않는다.

### 선택 4 — Profile export/import

Hermes는 프로필 export/import도 제공한다.

```powershell
hermes profile export default -o "E:\Hermes-Migration-2026-07-12\default.tar.gz"
```

집 PC에서:

```powershell
hermes profile import "E:\Hermes-Migration-2026-07-12\default.tar.gz" --name default
```

하지만 현재처럼 **실제 기본 프로필이 `default`이고, Desktop/Windows Native의 현재 환경을 정확히 이해하면서 옮기려는 목적**에는 위의 선별 복사 절차가 더 투명하다. export/import를 쓰더라도 설치 후 `hermes doctor`, `hermes tools list`, `hermes skills list`, 모델 인증, Vault Project 연결 검증은 반드시 한다.

---

## 14. 최종 체크리스트

### 현재 PC

- [ ] Hermes Desktop/CLI/gateway 완전 종료
- [ ] `config.yaml` 복사
- [ ] `SOUL.md` 복사
- [ ] `memories/MEMORY.md`, `memories/USER.md` 복사
- [ ] `skills/` 전체 복사
- [ ] 필요 시 `.env`, `auth.json`을 암호화 매체로 별도 복사
- [ ] 필요 시 `state.db` 복사
- [ ] Vault 변경사항을 Git commit/push하고 최신 상태 확인

### 집 노트북

- [ ] Git for Windows 설치
- [ ] Obsidian 설치
- [ ] Hermes Windows Native 설치
- [ ] `hermes --version`, `hermes doctor` 성공
- [ ] Hermes 한 번 실행 후 완전 종료
- [ ] Vault를 가능한 `D:\Study_LLM_Wiki`에 clone
- [ ] `config.yaml`, `SOUL.md`, `memories/`, `skills/` 복사 및 덮어쓰기
- [ ] 필요 시 `.env`, `auth.json` 복사
- [ ] 새 Hermes 실행
- [ ] `hermes tools list`, `hermes skills list`, `hermes model`, `hermes auth` 확인
- [ ] Hermes Desktop Project를 `D:\Study_LLM_Wiki`에 연결
- [ ] 새 대화에서 Vault 규칙/메모리/스킬 반영 여부 확인
- [ ] 이관 USB/압축파일을 안전하게 보관하거나 필요 없으면 안전 삭제

---

## 15. 한 줄 요약

집 PC에는 Hermes를 **새로 설치**한 뒤, 현재 PC의 `%LOCALAPPDATA%\hermes`에서 `config.yaml` + `SOUL.md` + `memories/` + `skills/`를 같은 위치에 덮어쓰고, 개인 보안 이관으로 `.env`/`auth.json`을 추가 복사한다. Vault는 Git으로 `D:\Study_LLM_Wiki`에 clone하여 Hermes Desktop Project에 다시 연결한다. 과거 대화까지 필요할 때만 Hermes 종료 상태에서 `state.db`를 추가 복사한다.

## 참고한 공식 문서

- Hermes Windows Native Guide: <https://hermes-agent.nousresearch.com/docs/user-guide/windows-native>
- Hermes Profiles: <https://hermes-agent.nousresearch.com/docs/user-guide/profiles>
- Hermes Profile Distributions: <https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions>
- Hermes Configuration: <https://hermes-agent.nousresearch.com/docs/user-guide/configuration>
