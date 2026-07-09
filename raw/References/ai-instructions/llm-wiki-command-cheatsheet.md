# LLM Wiki 핵심 명령어 치트시트

이 문서는 `D:\Study_LLM_Wiki` Vault에서 Hermes Agent 또는 다른 AI Agent에게 LLM Wiki 작업을 요청할 때 쓰는 표현을 정리한 참고용 원본 자료다.

> 위치: `raw/References/ai-instructions/llm-wiki-command-cheatsheet.md`  
> 성격: AI에게 줄 수 있는 명령어/작업 표현 참고자료  
> 주의: `raw/`는 원본 자료 레이어이므로, 수정이 필요하면 명시적으로 요청한다.

## 핵심 명령어

| 명령어 | 의미 |
|---|---|
| `ingest` / `처리해줘` / `정리해줘` | `raw/`에 넣은 새 원본 자료를 읽고 `wiki/`에 요약·개념·엔티티 페이지로 정리 |
| `query` / `질문` | 기존 `wiki/`와 필요 시 `raw/`를 참고해서 답변 |
| `lint` / `위키 점검` / `건강검진` | 깨진 링크, 누락된 index, frontmatter 문제, 고립 페이지 등을 점검 |
| `update` / `업데이트` | 기존 위키 페이지를 새 자료나 새 설명에 맞게 보강 |
| `create` / `새 페이지 만들어줘` | 개념·요약·비교·질문 페이지 등을 새로 생성 |
| `compare` / `비교해줘` | 두 개념/기술 차이를 비교하고 필요하면 `wiki/comparisons/`에 저장 |
| `roadmap` / `로드맵 짜줘` | 현재 학습 맥락 기준으로 공부 순서나 복습 계획 작성 |
| `index 확인` | `wiki/index.md` 목차 확인/정리 |
| `log 확인` | `wiki/log.md` 작업 이력 확인 |

## 자주 쓰는 요청 예시

### 새 raw 파일 정리

```text
raw/1. Java/2026.06.30(화)/수업.md ingest 해줘
```

```text
이 raw 파일 위키에 정리해줘
```

AI Agent는 보통 다음 순서로 확인한다.

1. `AGENTS.md`
2. `wiki/index.md`
3. `wiki/log.md`
4. 관련 기존 `wiki/` 페이지
5. 대상 `raw/` 파일

그다음 `wiki/`에 요약·개념·엔티티·비교·질문 페이지를 만들거나 업데이트한다.

## 질문하기

```text
Java에서 클래스랑 객체 차이 query 해줘
```

```text
클래스랑 객체 차이가 뭐였지?
```

질문에 답할 때는 `wiki/`를 먼저 보고, 부족하면 `raw/` 원본 자료를 참고한다.

## 위키 상태 점검

```text
위키 건강검진 해줘
```

```text
lint 해줘
```

주요 점검 대상은 다음과 같다.

- 깨진 위키링크
- `wiki/index.md` 누락 페이지
- frontmatter 누락/형식 오류
- 고립 페이지
- 허용되지 않은 태그
- 출처 없는 요약 페이지
- 너무 긴 페이지
- `status: needs-review` 또는 `confidence: low` 페이지

## 비교 페이지 만들기

```text
JSP랑 Thymeleaf 비교 페이지 만들어줘
```

```text
Spring MVC랑 REST API compare 해줘
```

보존 가치가 있으면 `wiki/comparisons/`에 비교 페이지로 저장하고, `wiki/index.md`와 `wiki/log.md`도 업데이트한다.

## 질문 답변 저장하기

```text
이 답변은 queries에 저장해줘
```

보존 가치가 있는 질문/답변이면 `wiki/queries/`에 질문 보존 페이지로 저장하고, `wiki/index.md`와 `wiki/log.md`도 업데이트한다.

## 제일 많이 쓰면 되는 표현

복잡한 명령어를 외울 필요 없이 아래 표현만 써도 된다.

```text
이 raw 파일 ingest 해줘
이 내용 위키에 정리해줘
이 개념 query 해줘
이 답변 wiki/queries에 저장해줘
위키 건강검진 해줘
index/log 확인해줘
```

## 한 줄 요약

LLM Wiki에서는 주로 `ingest`, `query`, `lint`, `update`, `compare`, `roadmap` 정도만 기억하면 된다.
