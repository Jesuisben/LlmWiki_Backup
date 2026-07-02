---
title: 2026-03-23 HTML/CSS와 웹 UI 입문
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [html, css, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md
  - raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf
  - raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf
  - raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf
  - raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html
status: growing
confidence: high
---

# 2026-03-23 HTML/CSS와 웹 UI 입문

## 한 줄 요약

Java/Oracle로 데이터와 로직을 배운 뒤, 웹서비스에서 사용자가 직접 보는 Client/UI 층을 만들기 위해 HTML 구조와 CSS 스타일의 가장 기본 문법을 시작한 날이다.

## 커리큘럼 위치

수업 첫머리에서 흐름을 `클라이언트 → 프론트엔드 → 백엔드 → 데이터베이스`로 잡았다. 백엔드는 DB에 쿼리를 던져 결과를 받고, 프론트엔드는 그 응답을 가공해 사용자에게 보여준다. 이 날은 그중 Client 화면을 직접 만드는 출발점이다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

## 배운 내용

- UI는 사용자가 보는 버튼·메뉴·입력창 같은 접점이고, UX는 그 화면을 쓰며 느끼는 유용성·만족감이다. ^[raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf]
- HTML은 Hyper Text Markup Language로, 태그·요소·속성·속성값을 이용해 웹 문서 구조를 만든다. ^[raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf]
- `<br>`, `<hr>`, `<h1>~<h6>`, `<span>`, `<ol>`, `<ul>`, `<li>`, `<table>`, `<img>`, `<a>` 같은 기본 태그를 실습했다.
- CSS는 인라인 style, `<style>` 태그, 태그/class/id 선택자로 화면 표현을 바꾼다.
- 문자 엔티티 `&nbsp;`, `&lt;`, `&gt;`, `&amp;`, `&copy;` 등은 `<`처럼 HTML 문법으로 오해될 수 있는 문자를 화면에 표시할 때 필요하다. ^[raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf]

## 핵심 실습

### 허브 소개 표 만들기

`tableExam.html`은 표·이미지·링크·CSS 테두리를 한 번에 묶은 대표 실습이다.

- `table`, `caption`, `thead`, `tbody`, `tr`, `th`, `td`로 표 구조를 만든다.
- `img src="/images/basil.jpg" alt="바질"`처럼 이미지 경로와 대체 텍스트를 지정한다.
- `a href="https://www.naver.com"`처럼 링크를 연결한다.
- CSS에서 `border-collapse: collapse`, `padding`, `background-image`, `background-repeat`, `background-attachment`를 적용했다. ^[raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html]

## 헷갈린 점 / 질문

- HTML에서 엔터와 공백은 그대로 보이지 않는다. 줄바꿈은 `<br>`, 공백/특수문자는 entity를 써야 한다.
- `class`는 여러 요소를 묶는 이름이고, `id`는 한 문서 안에서 한 요소를 식별하는 이름이다. 수업에서는 id를 DB의 Primary Key와 비슷하게 설명했다.
- CSS는 단순히 “아래 코드가 이긴다”가 아니라 선택자 우선순위와 선언 순서가 함께 작동한다.

## 관련 페이지

- [[concepts/html-css-basics|HTML/CSS 기본]]
- [[comparisons/inline-style-vs-internal-css-vs-external-css|inline style vs internal CSS vs external CSS]]
- [[entities/html|HTML]]
- [[entities/css|CSS]]

## 출처

- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf` p.2~5
- `raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf` p.2~5, p.13
- `raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf` p.2~4
- `raw/Study/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html`
