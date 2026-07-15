---
title: HTML 태그 vs 속성
created: 2026-07-06
updated: 2026-07-15
type: comparison
tags: [html, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html"
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
<img src="/images/basil.jpg" alt="바질">
```

- `img`: 태그
- `src`, `alt`: 속성
- `/images/basil.jpg`, `바질`: 속성값

## 언제 무엇을 쓰는가

- 상황 1 — 상품 이미지를 표시할 때: 구조는 `img` 태그로 만들고, 파일 위치와 대체 텍스트는 `src`·`alt` 속성으로 지정한다.
- 상황 2 — 상품 등록 입력을 만들 때: 입력 구조는 `input` 태그로 만들고, 입력 종류·서버로 보낼 이름·초기 안내는 `type`·`name`·`placeholder` 속성으로 지정한다.

태그와 속성은 경쟁 관계가 아니라 함께 쓰는 관계다. 태그가 먼저 요소의 종류를 정하고, 속성이 그 요소의 식별·동작·데이터를 보충한다.

## 헷갈리기 쉬운 포인트

- `style`은 HTML 속성이지만, 그 값 안에는 CSS 선언이 들어간다.
- `class`와 `id`는 HTML 속성이지만, CSS에서는 `.class명`, `#id명`으로 선택한다.
- `alt`는 태그가 아니라 `img` 태그의 속성이다.
- `태그들.md`의 `<alt>` 표기를 그대로 독립 요소로 외우면 안 된다. 실제 `tableExam.html`에서처럼 `img` 시작 태그 안에 쓴다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[entities/html]]
- [[comparisons/id-vs-class]]
- [[summaries/2026-03-23-html-css-intro]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
