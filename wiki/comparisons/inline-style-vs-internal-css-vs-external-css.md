---
title: inline style vs internal CSS vs external CSS
created: 2026-07-02
updated: 2026-07-15
type: comparison
tags: [html, css, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/styleExam.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/outerFile.css"
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

- 상황 1 — 수업에서 `<hr>` 하나의 폭만 즉시 확인할 때: `style="width: 30%;"` 같은 inline style.
- 상황 2 — `tableExam.html` 한 문서의 table/th/td를 함께 꾸밀 때: `<style>` 안의 internal CSS.
- 상황 3 — 여러 HTML에서 같은 Bootstrap 버튼·grid를 공유할 때: CDN `<link>`로 가져온 external CSS.

세 방식은 함께 존재할 수 있다. 예를 들어 external Bootstrap을 연결한 문서에서 internal CSS로 교육용 이미지 크기를 정하고, 특정 카드에만 inline `cursor:pointer`를 줄 수 있다. 다만 적용 범위와 우선순위를 추적하기 어려워지므로 실제 프로젝트에서는 의도적으로 선택한다.

## 헷갈리기 쉬운 포인트

- HTML의 `style="..."` 안에는 CSS 선언을 직접 쓴다.
- `<style>` 태그 안에서는 선택자를 먼저 쓰고 `{ 속성: 값; }`을 쓴다.
- class 선택자는 HTML에서는 `class="myyellow"`, CSS에서는 `.myyellow`로 쓴다.
- external CSS가 항상 inline보다 우선하는 것은 아니다. 수업에서 본 cascade처럼 어떤 선택자와 선언 위치가 충돌하는지 함께 봐야 한다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[entities/css]]
- [[comparisons/id-vs-class]]
- [[concepts/bootstrap-basics]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
