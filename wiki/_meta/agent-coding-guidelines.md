---
title: AI Agent 코딩 작업 지침
created: 2026-06-30
updated: 2026-06-30
type: meta
tags: [debugging, project]
sources:
  - raw/References/ai-instructions/karpathy-agent-guidelines.md
status: seed
confidence: medium
---

# AI Agent 코딩 작업 지침

## 한 줄 요약

AI Agent에게 코딩 작업을 맡길 때는 추측하지 않고, 단순하게 구현하고, 필요한 부분만 수정하며, 검증 가능한 목표를 기준으로 작업하게 해야 한다.

## 핵심 원칙

### 1. 코딩 전에 생각하기

불확실한 부분을 숨기지 않고 드러낸다. 여러 해석이 가능하면 조용히 하나를 고르지 않고 사용자에게 확인하거나 가정을 명시한다.

### 2. 단순함 우선

요청받지 않은 기능, 불필요한 추상화, 과도한 유연성을 추가하지 않는다. 한 번만 쓰는 코드라면 복잡한 구조를 만들지 않는다.

### 3. 외과적 수정

기존 코드를 수정할 때는 요청과 직접 관련된 부분만 바꾼다. 주변 코드 리팩터링, 포맷 변경, 불필요한 정리는 하지 않는다.

### 4. 목표 중심 실행

“버그 수정”이나 “검증 추가”처럼 모호한 목표는 실제 확인 가능한 목표로 바꾼다.

예를 들어:

```text
버그 수정 → 버그를 재현하는 테스트 작성 → 테스트 통과
검증 추가 → 잘못된 입력 테스트 작성 → 검증 로직 통과
```

## 이 Vault에서의 의미

이 지침은 수업 프로젝트나 실습 코드를 AI Agent와 함께 다룰 때 참고할 수 있다. 특히 오류 해결 기록이나 프로젝트 회고를 `wiki/`에 남길 때 다음 기준과 연결된다.

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/hermes-default-profile-mode-system|Hermes default 프로필 모드 시스템]]

## 출처

- `raw/References/ai-instructions/karpathy-agent-guidelines.md`
