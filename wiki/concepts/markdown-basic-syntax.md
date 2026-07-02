---
title: Markdown 기본 문법
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [study-log]
sources:
  - raw/markdown-grammar/markdown-grammar.md
status: seed
confidence: high
---

# Markdown 기본 문법

## 정의

Markdown은 일반 텍스트에 간단한 기호를 붙여 제목, 목록, 표, 코드 블록, 링크 등을 표현하는 문서 작성 문법이다.

## 왜 중요한가

이 Vault의 `raw/`와 `wiki/`는 모두 Markdown 파일을 중심으로 운영된다. 따라서 Markdown 문법을 알면 수업 노트, 개념 정리, 코드 예시, 링크 연결을 훨씬 깔끔하게 작성할 수 있다.

## 핵심 문법

| 목적 | 문법 예시 | 결과 |
|---|---|---|
| 제목 1 | `# 제목 1` | 큰 제목 |
| 제목 2 | `## 제목 2` | 중간 제목 |
| 굵게 | `**굵게**` | **굵게** |
| 기울임 | `*기울임*` | *기울임* |
| 취소선 | `~~취소선~~` | ~~취소선~~ |
| 목록 | `- 항목` | 글머리표 목록 |
| 순서 목록 | `1. 순서` | 번호 목록 |
| 인라인 코드 | `` `코드` `` | 짧은 코드 표시 |
| 코드 블록 | <code>&#96;&#96;&#96;java</code> | 여러 줄 코드 표시 |
| 구분선 | `---` | 문단 구분선 |
| 인용 | `> 인용문` | 인용 블록 |
| 체크박스 | `- [ ] 할일` | 할 일 목록 |
| 완료 체크박스 | `- [x] 완료` | 완료된 할 일 |
| 외부 링크 | `[Naver](https://www.naver.com)` | 웹 링크 |
| Obsidian 내부 링크 | <code>&#91;&#91;환영합니다!&#93;&#93;</code> | Vault 내부 노트 연결 |

## 예시

~~~markdown
# Java 수업 정리

## 오늘 배운 것

- 변수
- 자료형
- 출력문

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

관련 페이지: [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
~~~

## 자주 헷갈리는 점

- `#`의 개수로 제목 단계가 달라진다.
- 코드 블록은 백틱 3개로 열고 닫는다.
- Obsidian 내부 링크는 `\[\[페이지명\]\]` 형식을 쓴다.
- 외부 링크는 `[표시 텍스트](URL)` 형식을 쓴다.

## 관련 개념

- [[_meta/llm-wiki-operating-model|LLM Wiki 운영 모델]]
- [[_meta/llm-wiki-command-reference|LLM Wiki 명령어 참고]]

## 출처

- `raw/markdown-grammar/markdown-grammar.md`
