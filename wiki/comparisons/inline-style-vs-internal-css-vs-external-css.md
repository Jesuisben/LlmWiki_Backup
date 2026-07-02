---
title: inline style vs internal CSS vs external CSS
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [html, css, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md
  - raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md
  - raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf
status: growing
confidence: high
---

# inline style vs internal CSS vs external CSS

## 비교 목적

UI&UX 수업 초반에는 태그 안에 직접 `style`을 쓰는 방식에서 시작해, `<style>` 태그 안의 선택자 방식으로 넘어갔다. 이 차이를 이해해야 Bootstrap class와 나중의 외부 CSS 파일도 자연스럽게 이해할 수 있다.

## 한눈에 보기

| 방식 | 위치 | 장점 | 단점 | 수업 맥락 |
|---|---|---|---|---|
| inline style | HTML 태그의 `style` 속성 | 바로 확인 쉬움 | 반복·유지보수 어려움 | `<span style="color:red">` |
| internal CSS | HTML 문서의 `<style>` 태그 | 한 문서 안에서 여러 요소에 적용 | 파일이 커지면 복잡 | `li { color: purple; }` |
| external CSS | 별도 `.css` 파일 | 여러 HTML에서 재사용 | 파일 연결 필요 | `outerFile.css`, Bootstrap CDN |

## 언제 무엇을 쓰는가

처음 학습할 때는 inline style이 빠르지만, 같은 스타일을 여러 곳에 적용하려면 internal CSS가 낫다. 프로젝트가 커지면 외부 CSS 파일로 분리해 여러 HTML에서 재사용하는 편이 유지보수에 좋다.

Bootstrap CDN은 외부 CSS를 내 HTML에 연결하는 대표 예다. 직접 `.btn-primary`를 쓰지 않아도, 외부 Bootstrap CSS에 정의된 class를 HTML에서 호출한다.

## 헷갈리기 쉬운 포인트

- `style="color: purple"`는 태그 속성이고, `li { color: purple; }`는 CSS 선택자 규칙이다.
- HTML의 `class="myyellow"`는 이름표이고, `.myyellow { ... }`가 실제 스타일 규칙이다.
- `link href="...css"`는 외부 CSS 파일을 연결하는 것이다. 파일 내용이 내 HTML 안으로 복사되는 것은 아니다.

## 관련 페이지

- [[summaries/2026-03-23-html-css-intro|2026-03-23 HTML/CSS와 웹 UI 입문]]
- [[summaries/2026-03-24-css-layout-javascript-intro|2026-03-24 CSS 레이아웃과 JavaScript 입문]]
- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[concepts/bootstrap-basics|Bootstrap 기본]]

## 출처

- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf`
