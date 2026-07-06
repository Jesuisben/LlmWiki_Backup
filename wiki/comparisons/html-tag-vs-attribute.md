---
title: HTML 태그 vs 속성
created: 2026-07-06
updated: 2026-07-06
type: comparison
tags: [html, frontend]
sources:
  - "raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/태그들.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
status: growing
confidence: high
---

# HTML 태그 vs 속성

## 비교 목적

UI&UX 원본은 초반에 태그와 속성을 함께 다룬다. 둘을 구분하지 못하면 `class`, `id`, `style`, `src`, `alt`가 어디에 붙는지 헷갈린다.

## 한눈에 보기

| 항목 | 태그(tag) | 속성(attribute) |
|---|---|---|
| 역할 | 문서의 구조/의미를 만든다 | 태그에 추가 정보를 붙인다 |
| 위치 | `<태그명>` | 시작 태그 안 `이름="값"` |
| 예시 | `<table>`, `<img>`, `<form>` | `class`, `id`, `src`, `alt`, `style` |
| CSS 연결 | 선택 대상이 될 수 있음 | class/id/style 등으로 CSS와 연결 |

## 예시

```html
<img src="/images/americano01.png" alt="아메리카노 이미지" class="img-fluid">
```

- `img`: 태그
- `src`, `alt`, `class`: 속성
- `/images/americano01.png`, `아메리카노 이미지`, `img-fluid`: 속성값

## 언제 무엇을 보는가

- “이게 제목인가, 표인가, 입력 양식인가?” → 태그를 본다.
- “어떤 이미지 파일인가, 어떤 class인가, 어떤 id인가?” → 속성을 본다.

## 헷갈리기 쉬운 포인트

- `style`은 HTML 속성이지만, 그 값 안에는 CSS 선언이 들어간다.
- `class`와 `id`는 HTML 속성이지만, CSS에서는 `.class명`, `#id명`으로 선택한다.
- `alt`는 태그가 아니라 `img` 태그의 속성이다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[entities/html]]
- [[comparisons/id-vs-class]]
- [[summaries/2026-03-23-html-css-intro]]

## 출처

- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/태그들.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
