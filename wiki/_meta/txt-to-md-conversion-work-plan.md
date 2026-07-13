---
title: TXT→MD 남은 과목 변환 작업 인계
created: 2026-07-12
updated: 2026-07-14
type: meta
tags: [curriculum, study-log]
sources:
  - AGENTS.md
  - wiki/index.md
  - wiki/log.md
status: growing
confidence: high
---

# TXT→MD 남은 과목 변환 작업 인계

## 목적

한국ICT인재개발원 과정의 남은 원본 TXT를 사용자 수동 변환본의 canonical Markdown 형식으로 변환한다. `raw/`는 결과 MD가 놓이는 읽기 전용 원본 레이어이므로, 외부 원본 TXT와 `raw/`의 기존 파일을 임의로 수정하지 않는다.

## 확정 작업 순서

이 계획은 단계를 섞지 않는다. 날짜별 변환·검증이 모든 남은 과목에서 끝난 뒤에만 총정리를 만들고, 모든 raw MD가 완성된 뒤에만 wiki 고도화 ingest를 시작한다.

1. **날짜별 MD 변환:** 과목별 실제 외부 원본 TXT만 민감정보 후보 검사한다. 후보가 있으면 전체 경로·실제 줄 번호·감지 근거·비밀값만 `{MASKED}` 처리한 원문을 보고하고, 사용자 `유지하고 이어서` 또는 `수정했어` 재개 지시 전에는 변환하지 않는다. `교육 자료/`, 기존 결과 MD, 사용자 수동 변환본은 검사 입력에서 제외한다.
2. **파일 하나씩 완료:** 날짜별 TXT는 확인된 사용자 수동 변환본을 canonical 스타일로 삼아 대응 `raw/KoreaICT/` MD로 **세션당 파일 1개씩만** 변환한다. 각 파일은 원본 순서/공백, Markdown escape, fence 언어·경계, prose-in-fence, code-outside-fence를 포함한 semantic fence 전수 감사를 고정점으로 통과해야 완료다.
3. **과목 총정리 작성:** 모든 남은 과목의 날짜별 MD 변환·검증이 완료된 뒤에만 과목별 총정리 MD를 만든다. 총정리의 내용은 해당 과목의 날짜별 원본 전체에서 종합하고, 동일한 Markdown·semantic fence 검증을 적용한다.
4. **과목별 고도화 ingest:** 모든 남은 날짜별 MD와 필요한 과목 총정리 MD가 완성된 뒤에만 wiki ingest를 시작한다. ingest는 과목 하나씩 진행하며, `AGENTS.md`의 고품질 기준에 따라 날짜 흐름·구체 실습·개념/엔티티/비교 연결·출처·index/log·고정점 품질 검증을 갖춘 장기 학습용 지식 베이스로 고도화한다.
5. **과목별 lint:** 각 과목의 고도화 ingest가 끝날 때마다 그 과목 범위의 링크·frontmatter·출처·태그·고립 페이지·내용 품질을 lint하고 보정한다.
6. **전체 통합 lint:** 모든 과목의 과목별 lint가 끝난 뒤에만 전체 `wiki/` 범위의 통합 lint를 수행한다.

### 단계 보류 규칙

- 날짜별 MD 변환이 하나라도 남아 있으면 총정리 작성·ingest·lint를 시작하지 않는다.
- 총정리 MD가 하나라도 남아 있으면 ingest·lint를 시작하지 않는다.
- 모든 raw MD가 완성되기 전에는 일부 과목만 선행 ingest하지 않는다.
- 과목별 ingest가 끝나기 전에는 해당 과목 lint를 시작하지 않으며, 모든 과목 lint가 끝나기 전에는 전체 통합 lint를 시작하지 않는다.

### 세션 단위 진행과 인계

- 사용자가 `변환작업 시작`이라고 하면, 이 문서의 완료 기록을 기준으로 **바로 다음 날짜별 대상 파일 1개**와 필요한 선행 점검만 안내하고 그 파일을 작업한다.
- 한 파일의 변환과 고정점 검증이 끝나면, **자동으로 다음 파일을 실행하지 않는 것과 별개로**, 다음 세션에서 바로 이어갈 수 있도록 다음 대상 파일·현재 게이트 상태·금지 범위를 포함한 **복붙용 인계 프롬프트를 반드시 같은 완료 보고의 마지막에 제공한다.**
- 다음 세션은 이 문서와 직전 인계 프롬프트를 기준으로 파일 1개만 처리한다. 다음 파일로 자동 연속 진행하지 않는다.

### 날짜별 파일 완료 보고 게이트 (필수)

날짜별 TXT→MD 한 파일의 완료 보고는 아래 항목이 모두 있을 때만 완료다.

1. 변경 파일 목록과 고정점 검증 결과
2. 다음 파일을 자동 실행하지 않았다는 범위 확인
3. **첫 줄이 `smart 모드로 진행한다.`인 바로 다음 작업 단위 1개의 새 세션 복붙 프롬프트**

3번을 빼먹거나 첫 줄에 작업 모드를 명시하지 않으면 변환·검증이 통과했더라도 사용자 보고는 미완료로 취급한다. 다음 단위가 과목의 첫 날짜 파일이거나, 날짜별 변환 종료 뒤의 총정리 작성이라도 동일하게 정확한 다음 단위를 제시한다.

## 작업 단위 완료 기록 (append-only)

각 날짜별 TXT→MD 또는 과목 총정리 MD를 완료할 때마다 이 문서에 즉시 한 항목을 추가한다. 완료 기록 없이 작업을 완료로 보고하지 않는다.

| 완료일 | 작업 단위 | 외부 원본 TXT | 결과 MD | 새 생성·덮어쓰기 | 검증 결과 | 상태 / 다음 작업 |
|---|---|---|---|---|---|---|
| 기록 대기 | 변환을 실제로 마친 날짜별 파일 또는 총정리 1개 | 전체 경로 | 대응 `raw/KoreaICT/` 경로 | `완료` | 원본·공백·escape·semantic fence·scoped diff 결과 | `완료` 및 다음 미완료 단위 |

### 기록 규칙

1. 한 파일을 끝낼 때마다 같은 세션 안에서 이 표에 한 행을 추가한다. 여러 파일을 묶어 “완료”라고만 기록하지 않는다.
2. `새 생성·덮어쓰기` 열에는 항상 `완료`를 적고, 기존 MD가 있었는지도 괄호로 남긴다. 예: `완료 (기존 MD 덮어씀)`.
3. 검증 결과에는 최소한 원본 순서·공백, Markdown escape, semantic fence 전수 감사, scoped `git diff --check`의 실제 결과를 요약한다.
4. 검증 실패·보류·민감정보 게이트 대기는 완료로 기록하지 않고, `상태 / 다음 작업`에 사유와 재개 조건을 적는다.

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
- 민감정보 후보 탐지·사용자 확인·처리는 완료되었다.
- 외부 원본이나 해당 MD는 이 작업 계획에서 수정하지 않는다.

## 10. Python

### 변환 범위

- `2026.06.19(금) - 시작`부터 `2026.06.25(목)`까지의 날짜별 원본 TXT만 변환한다.

### 제외 범위

- `2026.06.25(목)` 이후 파일은 사용자가 이미 MD로 변환했거나 처음부터 MD로 작성한 자료이므로 제외한다.
- 10. Python 과목 총정리는 원래 사용자 작성 범위였으나, 2026-07-13 사용자의 명시 지시에 따라 완료된 날짜별 MD 전체를 근거로 Agent가 작성했다.
- 11. Machine Learning 과목 총정리도 사용자가 작성한다.

## 새 세션 시작 체크리스트

1. `AGENTS.md`, `wiki/index.md`, `wiki/log.md`를 읽는다.
2. 이 문서의 범위와 현재 `todo` 상태를 확인한다.
3. 5~10과목의 지정 TXT→MD·총정리와 9. 중간 프로젝트 공부의 민감정보 처리가 모두 완료되었음을 전제로 한다.
4. 다음 단계인 과목별 고도화 ingest를 시작할 때는 대상 과목의 현재 `raw/KoreaICT/` MD와 기존 wiki 페이지를 먼저 대조한다.
5. ingest가 끝난 과목부터 과목별 lint를 수행하고, 모든 과목의 lint가 끝난 뒤 전체 통합 lint를 수행한다.
6. 사용자 제외 범위를 추측으로 포함하거나 `raw/` 원본을 수정하지 않는다.

## 관련 문서

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/llm-wiki-command-reference|LLM Wiki 명령어 참고]]
- [[_meta/wiki-quality-audit-2026-07-02|2026-07-02 LLM Wiki 품질 감사 리포트]]

## [2026-07-12] 5. Linux 날짜별 TXT→MD 완료 기록

| 2026-07-12 | 5. Linux 2026.04.24(금) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.04.24(금)/2026.04.24(금).txt` | `raw/KoreaICT/5. Linux/2026.04.24(금)/2026.04.24(금).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux 2026.04.27(월) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.04.27(월)/2026.04.27(월).txt` | `raw/KoreaICT/5. Linux/2026.04.27(월)/2026.04.27(월).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux 2026.04.28(화) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.04.28(화)/2026.04.28(화).txt` | `raw/KoreaICT/5. Linux/2026.04.28(화)/2026.04.28(화).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux 2026.04.29(수) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.04.29(수)/2026.04.29(수).txt` | `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux 2026.04.30(목) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.04.30(목)/2026.04.30(목).txt` | `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux 2026.05.01(금) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.05.01(금)/2026.05.01(금).txt` | `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux 2026.05.04(월) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.05.04(월)/2026.05.04(월).txt` | `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux 2026.05.06(수) | `C:/Users/rktng/Desktop/한국ICT인재개발원/교육/5. Linux/2026.05.06(수)/2026.05.06(수).txt` | `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 통과, Markdown escape·semantic fence·언어 교차 감사 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-12 | 5. Linux Linux 총정리 | 날짜별 원본 기반 MD 10개: `raw/KoreaICT/5. Linux/2026.04.22(수) - 시작/2026.04.22(수) - 시작.md` ~ `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md` | `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` | 완료 (기존 MD 덮어씀) | 날짜별 MD 전체 흐름 대조, 시간대 heading 미삽입, Markdown escape, fence 균형·빈 본문·언어 semantic inventory 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 6. AWS 2026.05.06(수) - 시작 | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/6. AWS/2026.05.06(수) - 시작/2026.05.06(수).txt` | `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, Markdown escape, semantic fence 전수 감사(실제 fence 없음), scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 6. AWS 2026.05.07(목) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/6. AWS/2026.05.07(목)/2026.05.07(목).txt` | `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, Markdown escape, semantic fence 전수 감사(실제 fence 없음), scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 6. AWS 2026.05.08(금) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/6. AWS/2026.05.08(금)/2026.05.08(금).txt` | `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, Markdown escape, semantic fence 51개(`bash`/`text`/`sql`) 전수 감사, fence 밖 명령형 템플릿 2개는 prose로 분류, scoped `git diff --check` exit 0 | 완료 |

## [2026-07-13] 5. Linux 지정 범위 재변환·고정점 검증

| 2026-07-13 | 5. Linux 2026.04.29(수) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/5. Linux/2026.04.29(수)/2026.04.29(수).txt` | `raw/KoreaICT/5. Linux/2026.04.29(수)/2026.04.29(수).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, shell prose fence 1건 해제, fence 81개 전수 감사·Markdown escape·scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 5. Linux 2026.04.30(목) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/5. Linux/2026.04.30(목)/2026.04.30(목).txt` | `raw/KoreaICT/5. Linux/2026.04.30(목)/2026.04.30(목).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, prose/command 경계 2곳 보정, fence 96개 전수 감사·Markdown escape·scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 5. Linux 2026.05.01(금) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/5. Linux/2026.05.01(금)/2026.05.01(금).txt` | `raw/KoreaICT/5. Linux/2026.05.01(금)/2026.05.01(금).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, fence 밖 `sudo su -` 보정, fence 44개 전수 감사·Markdown escape·scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 5. Linux 2026.05.04(월) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/5. Linux/2026.05.04(월)/2026.05.04(월).txt` | `raw/KoreaICT/5. Linux/2026.05.04(월)/2026.05.04(월).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, prose Dockerfile fence와 분리된 Java closing brace 3개 보정, fence 72개 전수 감사·Markdown escape·scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 5. Linux 2026.05.06(수) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/5. Linux/2026.05.06(수)/2026.05.06(수).txt` | `raw/KoreaICT/5. Linux/2026.05.06(수)/2026.05.06(수).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치, Java code unit 4개와 누락된 `println` 1개 보정, fence 5개 전수 감사·Markdown escape·scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 5. Linux Linux 총정리 | Linux 날짜별 원본 TXT 10개 | `raw/KoreaICT/5. Linux/Linux 총정리/Linux 총정리.md` | 완료 (재검증) | 총정리 구조·Markdown escape, fence 46개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 |
| 2026-07-13 | 7. Ci&CD 2026.05.11(월) - 시작 | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월).txt` | `raw/KoreaICT/7. Ci&CD/2026.05.11(월) - 시작/2026.05.11(월) - 시작.md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백(후행 공백·EOF 빈 줄 정규화) 역대조, Markdown escape, fence 18개 semantic inventory, prose-in-fence·code-outside-fence 0건, scoped `git diff --check` exit 0 | 완료 / 다음: 7. Ci&CD 2026.05.12(화) |
| 2026-07-13 | 7. Ci&CD 2026.05.12(화) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/7. Ci&CD/2026.05.12(화)/2026.05.12(화).txt` | `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조(끝 탭 정규화만 적용) 통과, Markdown escape(흐름 화살표·강조표) 통과, shell fence 4개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 7. Ci&CD 2026.05.13(수) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/7. Ci&CD/2026.05.13(수)/2026.05.13(수).txt` | `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md` | 완료 (기존 MD 덮어씀) | 원본 순서·공백 역대조 0건 불일치(날짜 줄 제거·끝 공백 정규화 예외), Markdown escape, fence 12개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 8. Passwordless 2026.05.14(목) - 시작 | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.txt` | `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md` | 완료 (기존 MD 덮어씀) | 민감정보 후보 0건, 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 및 EOF 공백 정규화 예외), Markdown escape, fence 0개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 8. Passwordless 2026.05.15(금) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.15(금)/2026.05.15(금).txt` | `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md` | 완료 (기존 MD 덮어씀, 후속 정정) | leading `N.` 12개 escape·교시 heading `N.` 8개 복원 후 비공백 308행·leading `N.` 33개·교시 heading 8개 원본 전수 매핑 0건 불일치, shell fence 16개 균형·빈 fence 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 8. Passwordless 2026.05.18(월) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.18(월)/2026.05.18(월).txt` | `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md` | 완료 (기존 MD 덮어씀, 후속 재검증) | 본문 수정 없음. 비공백 311행·leading `N.` 40개·교시 heading 8개 원본 전수 매핑 0건 불일치, fence 39개(`shell` 35·`sql` 2·`properties` 2) 균형·빈 fence 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 8. Passwordless 2026.05.19(화) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.19(화)/2026.05.19(화).txt` | `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md` | 완료 (기존 MD 덮어씀) | 사용자 `유지하고 이어서` 후 원본 순서·공백 역대조 0건 불일치(날짜 줄·직후 선행 공백 제거와 EOF 공백 정규화 예외), Markdown escape, shell fence 14개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 8. Passwordless 2026.05.20(수) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.20(수)/2026.05.20(수).txt` | `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md` | 완료 (기존 MD 덮어씀) | 사용자 `수정했어` 후 민감정보 재검사 0건, 원본 순서·공백 역대조 0건(날짜 줄·직후 선행 공백 및 EOF 빈 줄 정규화 예외), Markdown escape, shell fence 1개 semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 8. Passwordless 2026.05.21(목) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/8. Passwordless/2026.05.21(목)/2026.05.21(목).txt` | `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md` | 완료 (기존 MD 덮어씀) | 사용자 `수정했어` 후 민감정보 재검사 0건, 원본 순서·공백 역대조 0건(날짜 줄·직후 선행 공백 및 EOF 빈 줄·후행 탭 정규화 예외), Markdown escape, fence 12개(`shell` 11·`json` 1) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음: 10. Python 2026.06.19(금) - 시작 |
| 2026-07-13 | 10. Python 2026.06.19(금) - 시작 | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.txt` | `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md` | 완료 (기존 MD 덮어씀) | 민감정보 후보 0건, 원본 순서·공백 역대조 0건(날짜 줄·직후 선행 공백 및 EOF 빈 줄 정규화 예외), Markdown escape, fence 29개(`python` 26·`text` 3) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음: 10. Python 2026.06.22(월) |
| 2026-07-13 | 10. Python 2026.06.22(월) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/10. Python/2026.06.22(월)/2026.06.22(월).txt` | `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md` | 완료 (기존 MD 덮어씀) | 민감정보 후보 0건, 원본 순서·공백 역대조 0건(날짜 줄·직후 선행 공백 및 후행 공백 정규화 예외), Markdown escape, fence 30개(`python` 22·`text` 8) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음: 10. Python 2026.06.23(화) |
| 2026-07-13 | 10. Python 2026.06.23(화) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/10. Python/2026.06.23(화)/2026.06.23(화).txt` | `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md` | 완료 (기존 MD 덮어씀) | 민감정보 후보 0건, 원본 순서·공백 역대조 0건(날짜 줄·직후 선행 공백 제거 및 terminal EOF 빈 줄 정규화 예외), Markdown escape, fence 36개(`python` 27·`text` 9) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음: 10. Python 2026.06.24(수) |
| 2026-07-13 | 10. Python 2026.06.24(수) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/10. Python/2026.06.24(수)/2026.06.24(수).txt` | `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md` | 완료 (기존 MD 덮어씀) | 민감정보 후보 0건, 원본 순서·공백 역대조 0건(날짜 줄·직후 선행 공백 제거, 빈 줄의 trailing whitespace 2건 정규화 예외), Markdown escape, fence 33개(`python` 26·`text` 7) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음: 10. Python 2026.06.25(목) |
| 2026-07-13 | 10. Python 2026.06.25(목) | `C:/Users/ICT02-006/Desktop/한국ICT인재개발원/교육/10. Python/2026.06.25(목)/2026.06.25(목).txt` | `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md` | 완료 (기존 MD 덮어씀) | 민감정보 후보 0건, 원본 순서·공백 역대조 0건(날짜 줄·직후 선행 공백 제거와 줄끝 공백 11건 정규화 예외), Markdown escape, fence 24개(`python` 20·`text` 4) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / Python 지정 날짜별 변환 종료; 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 6. AWS AWS 총정리 | AWS 날짜별 원본 TXT 및 완료 MD 3개: `2026.05.06(수) - 시작`~`2026.05.08(금)` | `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md` | 완료 (기존 MD 덮어씀) | 날짜별 흐름 근거 대조, Markdown escape, fence 14개(`shell` 10·`text` 2·`properties` 1·`sql` 1) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit·실제 credential 값 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 7. Ci&CD Ci&CD 총정리 | 완료된 Ci&CD 날짜별 MD 3개: `2026.05.11(월) - 시작`~`2026.05.13(수)` | `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md` | 완료 (새 MD 생성) | 날짜별 흐름 근거 대조, Markdown escape, fence 20개(`java` 1·`properties` 2·`xml` 2·`yaml` 2·`shell` 7·`text` 3·`hcl` 1·`json` 1·`sql` 1) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 8. Passwordless Passwordless 총정리 | 완료된 Passwordless 날짜별 원본/결과 MD 6개: `2026.05.14(목) - 시작`~`2026.05.21(목)` | `raw/KoreaICT/8. Passwordless/Passwordless 총정리/Passwordless 총정리.md` | 완료 (새 MD 생성) | 날짜별 전체 흐름 근거 대조, Markdown escape(흐름 화살표 5개 모두 `-\>`), fence 8개(`shell` 5·`properties` 1·`sql` 1·`json` 1) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 및 새 파일 `--no-index --check` 출력 없음 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 10. Python Python 총정리 | 날짜별 MD 14개: `2026.06.19(금) - 시작`~`2026.07.08(수)` | `raw/KoreaICT/10. Python/Python 총정리/Python 총정리.md` | 완료 (새 MD 생성, 사용자 명시 지시) | 날짜별 전체 흐름 근거 대조, Markdown escape(흐름 화살표 4개 모두 `-\>`), fence 18개(`python` 18) semantic inventory, prose-in-fence·code-outside-fence·분리 code unit 0건, scoped `git diff --check` exit 0 및 새 파일 `--no-index --check` 출력 없음 | 완료 / 다음 파일 자동 진행 안 함 |
| 2026-07-13 | 9. 중간 프로젝트 공부 민감정보 후보 처리 | 사용자가 이미 작성한 중간 프로젝트 MD 범위 | 해당 없음 (변환·재작성 대상 아님) | 완료 (문서 상태 동기화) | 민감정보 후보 탐지·사용자 확인·처리 완료 사실을 사용자 확인으로 반영함. 외부 원본과 `raw/`는 수정하지 않음 | 완료 / TXT→MD 정리 단계 종료, 다음: 과목별 고도화 ingest |
