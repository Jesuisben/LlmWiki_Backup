---
title: CSS
created: 2026-07-02
updated: 2026-07-15
type: entity
tags: [css, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/2026.03.27(금)/2026.03.27(금).md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/styleExam.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/outerFile.css"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/jQueryImageTest/jQueryImageTest.html"
status: growing
confidence: high
---

# CSS

## 무엇인가

CSS(Cascading Style Sheets)는 HTML 요소의 색상, 크기, 여백, 배치, 글꼴, 표시 방식을 지정하는 스타일 언어다.

## 이 위키에서의 맥락

UI&UX 수업에서는 CSS를 선택자와 속성 중심으로 배웠다. `style` 태그 내부에서 태그 선택자, class 선택자, id 선택자를 작성하고, 이후 Bootstrap class와 jQuery 선택자 이해의 기반이 되었다.

## 핵심 기능 / 특징

- 선택자: 태그 선택자, `.class`, `#id`, 그룹 선택자, 속성 선택자, pseudo-class
- 크기/테두리: `width`, `height`, `border`
- 배치: `position`, `top`, `left`, `display`, `z-index`
- 넘침/표시: `overflow`, `hidden`, `block`, `inline`, `inline-block`
- 텍스트: `font-family`, `font-style`, `line-height`, `text-decoration`
- 목록/표: `list-style-type`, `list-style-position`, `vertical-align`

## 화면 구현 역할

수업에서 CSS는 표의 선·폭·색상, div 박스의 좌표, 글꼴과 행간, 이미지 hover/gray/active 상태를 담당했다. 특히 `position: relative`인 부모와 `position: absolute`인 자식을 함께 써서 배치 기준을 만들었고, 2026-03-27에는 pseudo-class와 class 토글로 사용자 상태를 시각화했다.

## 프로젝트·면접 설명 관점

- 프로젝트: 공통 스타일은 class로 재사용하고, JavaScript가 class를 추가·제거해 상태를 표현하도록 역할을 나눈다고 설명할 수 있다.
- 면접: CSS cascade는 여러 규칙이 같은 속성을 지정할 때 우선순위와 선언 순서에 따라 최종값이 정해지는 성질이다. 수업의 `.myyellow`와 `.myblue`가 같은 `color`를 지정한 예가 출발점이다.
- 범위 경계: UI&UX에서는 직접 CSS와 Bootstrap utility/class를 사용했다. CSS module·styled-components 같은 React 생태계 방식은 후속 범위다.

## 관련 개념

- [[concepts/html-css-basics]]
- [[concepts/bootstrap-basics]]
- [[comparisons/inline-style-vs-internal-css-vs-external-css]]
- [[comparisons/id-vs-class]]
- [[comparisons/custom-css-vs-bootstrap]]
- [[entities/html]]

## 학습 이력

- [[summaries/2026-03-23-html-css-intro]] — 선택자 3종과 table style
- [[summaries/2026-03-24-css-layout-javascript-intro]] — Box Model, position, display, 글꼴
- [[summaries/2026-03-27-jquery-ui-interaction]] — pseudo-class, transition, 이미지 스타일 변경

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
