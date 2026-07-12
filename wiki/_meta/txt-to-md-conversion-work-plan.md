---
title: TXT→MD 남은 과목 변환 작업 인계
created: 2026-07-12
updated: 2026-07-12
type: meta
tags: [curriculum, study-log]
sources: []
status: growing
confidence: high
---

# TXT→MD 남은 과목 변환 작업 인계

## 목적

한국ICT인재개발원 과정의 남은 원본 TXT를 사용자 수동 변환본의 canonical Markdown 형식으로 변환한다. `raw/`는 결과 MD가 놓이는 읽기 전용 원본 레이어이므로, 외부 원본 TXT와 `raw/`의 기존 파일을 임의로 수정하지 않는다.

## 공통 작업 순서

1. 과목별 실제 외부 원본 TXT만 민감정보 후보 검사한다. `교육 자료/`, 기존 결과 MD, 사용자 수동 변환본은 검사 입력에서 제외한다.
2. 후보가 있으면 전체 경로·실제 줄 번호·감지 근거·비밀값만 `{MASKED}` 처리한 원문을 모두 보고하고, 사용자 `유지하고 이어서` 또는 `수정했어` 재개 지시 전에는 변환하지 않는다.
3. 날짜별 TXT는 확인된 사용자 수동 변환본을 canonical 스타일로 삼아 대응 `raw/KoreaICT/` MD로 변환한다.
4. 변환 후 원본 순서/공백, Markdown escape, fence 언어·경계, prose-in-fence, code-outside-fence를 포함한 semantic fence 전수 감사까지 고정점 검증한다.
5. 모든 변환이 끝나기 전에는 wiki ingest를 시작하지 않는다.

## 5~8과목

### 적용 범위

- 5. Linux
- 6. AWS
- 7. CI/CD
- 8. Passwordless

### 날짜별 파일

- 각 과목의 날짜별 외부 원본 TXT를 내용 근거로 사용한다.
- 대응하는 날짜별 `raw/KoreaICT/` MD를 만든다.

### 과목 총정리 파일

- 이 과목들에는 총정리용 원본 TXT가 없다.
- 따라서 총정리 MD는 기존 사용자가 만든 과목 총정리 MD의 **표현·형식**을 실제로 대조해 따른다.
- 총정리의 **내용**은 해당 과목 날짜별 원본 TXT 전체에서 종합한다. 기존 총정리의 내용을 복사하거나 단순 재조합하지 않는다.
- 총정리에도 날짜별 변환과 같은 Markdown escape·fence·공백·semantic fence 검증을 적용한다.

## 9. 중간 프로젝트 공부

- 사용자가 이미 직접 MD로 변환했으므로 변환·재작성하지 않는다.
- 해당 MD의 민감정보 후보만 탐지해 보고한다.
- 후보가 있더라도 사용자의 추가 지시 없이 원본이나 MD를 수정하지 않는다.

## 10. Python

### 변환 범위

- `2026.06.19(금) - 시작`부터 `2026.06.25(목)`까지의 날짜별 원본 TXT만 변환한다.

### 제외 범위

- `2026.06.25(목)` 이후 파일은 사용자가 이미 MD로 변환했거나 처음부터 MD로 작성한 자료이므로 제외한다.
- 10. Python 과목 총정리는 사용자가 작성한다.
- 11. Machine Learning 과목 총정리도 사용자가 작성한다.

## 새 세션 시작 체크리스트

1. `AGENTS.md`, `wiki/index.md`, `wiki/log.md`를 읽는다.
2. 이 문서의 범위와 현재 `todo` 상태를 확인한다.
3. 시작할 과목 하나만 정하고, 해당 과목의 실제 외부 원본 TXT 경로와 대응 `raw/KoreaICT/` 경로를 먼저 매핑한다.
4. 민감정보 검사 → 사용자 재개 지시 → 변환 → 고정점 검증 순서를 지킨다.
5. 다른 과목의 미완료 작업을 추측으로 포함하거나, 사용자 제외 범위를 건드리지 않는다.

## 관련 문서

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/llm-wiki-command-reference|LLM Wiki 명령어 참고]]
- [[_meta/wiki-quality-audit-2026-07-02|2026-07-02 LLM Wiki 품질 감사 리포트]]
