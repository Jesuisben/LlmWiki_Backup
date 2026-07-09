---
title: LLM Wiki 운영 모델
created: 2026-06-30
updated: 2026-06-30
type: meta
tags: [study-log]
sources:
  - raw/References/ai-instructions/hermes-agent-llm-wiki-initial-setup.md
status: stable
confidence: high
---

# LLM Wiki 운영 모델

## 한 줄 요약

LLM Wiki는 `raw/` 원본 자료를 직접 고치는 대신, AI Agent가 `wiki/`에 요약·개념·비교·질문 페이지를 누적해 가는 개인 지식 베이스 운영 방식이다.

## 핵심 아이디어

일반적인 RAG 방식은 질문할 때마다 원본 문서 조각을 다시 검색하고 조합한다. 반면 LLM Wiki는 새 원본을 넣을 때마다 AI가 내용을 읽고 기존 위키에 통합한다.

즉, 지식이 매번 새로 계산되는 것이 아니라 다음 형태로 누적된다.

- 원본 자료는 `raw/`에 보존한다.
- 정리된 지식은 `wiki/`에 저장한다.
- 연결은 Obsidian 위키링크 형식으로 남긴다.
- `wiki/index.md`는 전체 목차 역할을 한다.
- `wiki/log.md`는 작업 이력 역할을 한다.

## 이 Vault에서의 적용

이 Vault는 국비지원 웹서비스 풀스택 개발자 과정의 학습 내용을 장기적으로 추적하기 위한 위키다.

주요 목표는 다음과 같다.

1. 며칠에 무엇을 배웠는지 추적한다.
2. Java, Oracle, Spring, React, Linux, AWS 등 커리큘럼 지식을 연결한다.
3. 새 세션이나 다른 AI Agent도 `AGENTS.md`, `wiki/index.md`, `wiki/log.md`를 읽고 맥락을 복원하게 한다.
4. 중요한 질문과 답변은 대화창에만 두지 않고 `wiki/queries/`에 보존한다.

## 세 계층 구조

### 1. Raw sources

`raw/`는 원본 자료 레이어다. 사용자가 넣은 수업 노트, AI 지시문, 문법 정리, 참고 문서를 보관한다. AI는 읽을 수 있지만 기본적으로 수정하지 않는다.

### 2. Wiki

`wiki/`는 AI가 관리하는 컴파일된 지식 레이어다. 요약, 개념, 엔티티, 비교, 질문 페이지를 만든다.

### 3. Schema

`AGENTS.md`는 이 위키의 운영 규칙이다. 다른 AI Agent가 이 Vault를 열었을 때도 먼저 읽어야 하는 기준 문서다.

## 관련 페이지

- [[_meta/llm-wiki-command-reference|LLM Wiki 명령어 참고]]
- [[_meta/hermes-default-profile-mode-system|Hermes default 프로필 모드 시스템]]
- [[_meta/agent-coding-guidelines|AI Agent 코딩 작업 지침]]
- [[_meta/wiki-quality-audit-2026-07-02|2026-07-02 LLM Wiki 품질 감사 리포트]]
- [[concepts/markdown-basic-syntax|Markdown 기본 문법]]
- [[_meta/hermes-home-laptop-setup|집 노트북에 LLM Wiki와 Hermes Agent 환경 복제하기]]

## 출처

- `raw/References/ai-instructions/hermes-agent-llm-wiki-initial-setup.md`
