---
title: inline style vs internal CSS vs external CSS
created: 2026-07-02
updated: 2026-07-06
type: comparison
tags: [html, css, frontend]
sources:
  - "raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
status: growing
confidence: high
---

# inline style vs internal CSS vs external CSS

## 비교 목적

UI&UX 수업 초반에는 `<hr style="width: 30%;">` 같은 inline style과 `<style>` 태그 내부 CSS를 함께 다뤘다. 세 방식은 모두 CSS를 적용하지만 유지보수성과 적용 범위가 다르다.

## 한눈에 보기

| 방식 | 위치 | 예시 | 장점 | 단점 |
|---|---|---|---|---|
| inline style | 태그의 `style` 속성 | `<hr style="width: 30%;">` | 빠르게 한 요소만 수정 | 재사용·관리 어려움 |
| internal CSS | HTML 문서의 `<style>` | `.myyellow { color: yellow; }` | 한 문서 안에서 정리 가능 | 여러 HTML에 공유 어려움 |
| external CSS | 별도 `.css` 파일 | `<link rel="stylesheet" ...>` | 여러 문서 공유, 유지보수 좋음 | 파일 분리 이해 필요 |

## 언제 무엇을 쓰는가

- 실습 중 한 요소를 빨리 확인할 때: inline style
- 한 HTML 파일 안에서 여러 요소를 통일할 때: internal CSS
- 실제 프로젝트에서 여러 페이지가 같은 디자인을 공유할 때: external CSS
- Bootstrap을 쓸 때: external CSS를 CDN으로 가져와 class를 조합하는 방식

## 헷갈리기 쉬운 포인트

- HTML의 `style="..."` 안에는 CSS 선언을 직접 쓴다.
- `<style>` 태그 안에서는 선택자를 먼저 쓰고 `{ 속성: 값; }`을 쓴다.
- class 선택자는 HTML에서는 `class="myyellow"`, CSS에서는 `.myyellow`로 쓴다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[entities/css]]
- [[comparisons/id-vs-class]]
- [[concepts/bootstrap-basics]]

## 출처

- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
