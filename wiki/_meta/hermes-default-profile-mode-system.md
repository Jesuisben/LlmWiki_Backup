---
title: Hermes default 프로필 모드 시스템
created: 2026-06-30
updated: 2026-07-01
type: meta
tags: [study-log]
sources:
  - raw/ai-instructions/hermes-default-profile-instructions.md
status: stable
confidence: high
---

# Hermes default 프로필 모드 시스템

## 한 줄 요약

Hermes Desktop에서는 여러 프로필을 나누기보다 default 프로필 하나를 유지하고, 대화 중 `safe`, `smart`, `danger` 모드로 작업 권한 수준을 바꾸는 방식이 이 Vault의 기본 운영 방식이다.

## 왜 default 프로필 하나를 쓰는가

여러 Hermes 프로필을 만들면 세션, 프로젝트, memory, skills, 설정이 분리된다. 이는 격리에는 좋지만, 사용자가 원하는 장기 연속성에는 불리하다.

따라서 이 Vault에서는 다음 방식을 선호한다.

```text
default 프로필 하나
+ 대화 중 safe/smart/danger 모드 전환
+ 같은 memory/project/session 흐름 유지
```

## 모드별 의미

### safe 모드

읽기, 검색, 분석, 설명은 자유롭게 수행하지만 파일 생성·수정·삭제, git 변경, 설정 변경처럼 상태가 바뀌는 작업은 먼저 승인받는다.

### smart 모드

일반적인 프로젝트 내부 수정과 검증은 자율적으로 진행한다. 삭제, 대량 변경, git push/reset, 설정 변경, secret 접근 등 위험한 작업은 먼저 승인받는다.

### danger 모드

조사, 파일 수정, 테스트, 빌드, 문서 업데이트는 높은 자율성으로 진행한다. 다만 삭제, git push/reset/rebase, 시스템/Hermes 설정 변경, 비용 발생 작업, credential 접근은 여전히 승인받는다.

## LLM Wiki 작업에서의 적용

- `raw/`는 어떤 모드에서도 기본적으로 읽기 전용이다.
- `safe` 모드에서는 `wiki/` 생성/수정도 승인 후 진행한다.
- `smart`/`danger` 모드에서는 사용자가 ingest, 정리, 업데이트, 질문 보존을 요청하면 `wiki/` 내부 생성/수정은 자율적으로 진행할 수 있다.
- 새 위키 페이지를 만들면 반드시 `wiki/index.md`에 등록한다.
- 의미 있는 작업은 `wiki/log.md`에 기록한다.

## 관련 페이지

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/llm-wiki-command-reference|LLM Wiki 명령어 참고]]

## 출처

- `raw/ai-instructions/hermes-default-profile-instructions.md`


## 원본 수정 반영 (2026-07-01)

- `raw/ai-instructions/hermes-default-profile-instructions.md`가 수정된 상태임을 확인했다.
- 현재 운영 원칙은 safe/smart/danger 모드 전환과 승인 기준을 중심으로 유지한다.
- 이 페이지는 실제 Hermes 시스템 지시문이 아니라, 위키에 보존된 운영 참고 문서다.
