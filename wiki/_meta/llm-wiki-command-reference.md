---
title: LLM Wiki 명령어 참고
created: 2026-06-30
updated: 2026-06-30
type: meta
tags: [study-log]
sources:
  - raw/References/ai-instructions/llm-wiki-command-cheatsheet.md
  - raw/References/ai-instructions/hermes-agent-llm-wiki-initial-setup.md
status: stable
confidence: high
---

# LLM Wiki 명령어 참고

## 한 줄 요약

LLM Wiki 작업은 주로 `ingest`, `query`, `lint`, `update`, `compare`, `roadmap` 같은 표현으로 요청하면 된다.

## 핵심 명령어

| 명령어 | 쓰는 상황 | 결과 |
|---|---|---|
| `ingest` / `처리해줘` / `정리해줘` | `raw/`에 새 원본을 넣었을 때 | `wiki/`에 요약·개념·엔티티 페이지 생성/수정 |
| `query` / `질문` | 기존 학습 내용에 대해 물어볼 때 | `wiki/` 우선, 부족하면 `raw/`를 참고해 답변 |
| `lint` / `위키 점검` / `건강검진` | 위키 상태를 점검할 때 | 깨진 링크, index 누락, frontmatter 문제 등을 확인 |
| `update` / `업데이트` | 기존 페이지를 보강할 때 | 새 자료나 설명을 기존 페이지에 반영 |
| `create` / `새 페이지 만들어줘` | 특정 개념·요약·질문 페이지가 필요할 때 | 새 위키 페이지 생성 |
| `compare` / `비교해줘` | 두 개념이나 기술을 비교할 때 | 필요하면 `wiki/comparisons/`에 비교 페이지 생성 |
| `roadmap` / `로드맵 짜줘` | 공부 순서나 복습 계획이 필요할 때 | 현재 위키 맥락 기반 학습 계획 생성 |
| `index 확인` | 목차 상태를 볼 때 | `wiki/index.md` 확인/정리 |
| `log 확인` | 작업 이력을 볼 때 | `wiki/log.md` 확인 |

## 자주 쓰는 요청 예시

```text
이 raw 파일 ingest 해줘
이 내용 위키에 정리해줘
이 개념 query 해줘
이 답변 wiki/queries에 저장해줘
위키 건강검진 해줘
index/log 확인해줘
```

## 작업 흐름

새 원본을 처리할 때 AI Agent는 보통 다음 순서로 확인한다.

1. `AGENTS.md`
2. `wiki/index.md`
3. `wiki/log.md`
4. 관련 기존 `wiki/` 페이지
5. 대상 `raw/` 파일

그다음 새 페이지를 만들거나 기존 페이지를 업데이트하고, `wiki/index.md`와 `wiki/log.md`에 반영한다.

## 관련 페이지

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/hermes-default-profile-mode-system|Hermes default 프로필 모드 시스템]]

## 출처

- `raw/References/ai-instructions/llm-wiki-command-cheatsheet.md`
- `raw/References/ai-instructions/hermes-agent-llm-wiki-initial-setup.md`
