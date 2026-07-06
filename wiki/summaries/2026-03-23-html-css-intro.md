---
title: 2026-03-23 HTML/CSS와 웹 UI 입문
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [html, css, javascript, frontend, curriculum]
sources:
  - "raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/태그들.md"
  - "raw/Study/3. UI&UX/UI&UX 총정리/속성들.md"
  - "raw/Study/3. UI&UX/교육 자료/웹 서비스 Ui&UX.pdf"
  - "raw/Study/3. UI&UX/교육 자료/HTML&JS&CSS 이론(new).pdf"
  - "raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf"
status: growing
confidence: high
---

# 2026-03-23 HTML/CSS와 웹 UI 입문

## 한 줄 요약

Java·Oracle 뒤에 웹 화면 영역으로 넘어오면서, 웹 서비스의 큰 흐름을 `클라이언트 → 프론트엔드 → 백엔드 → 데이터베이스`로 잡고 [[entities/html|HTML]] 문서 구조와 [[entities/css|CSS]] 선택자·박스 모델의 기초를 시작한 날이다.

## 커리큘럼 위치

- 이전 흐름: [[entities/java|Java]]로 로직을 작성하고 [[entities/oracle-database|Oracle Database]]로 데이터를 다루는 방법을 배웠다.
- 이날 전환: 사용자가 실제로 보는 화면은 HTML/CSS가 만들고, 이후 [[concepts/javascript-dom|JavaScript와 DOM]]이 화면을 동적으로 바꾼다는 흐름으로 넘어갔다.
- 다음 흐름: 2026-03-24에는 `div`, `position`, `display`, `innerHTML`을 이용해 레이아웃과 JavaScript 조작을 시작한다.

## 배운 내용

### 1. 웹 서비스 데이터 흐름

원본은 첫 시간에 “클라이언트 - 프론트엔드 - 백엔드 - 데이터베이스”의 개략적 흐름과 `http`를 통신 규약으로 설명한다. 이 단계에서 HTML/CSS는 서버나 DB가 아니라 **브라우저가 해석하는 화면 문서**라는 위치를 잡는 것이 중요하다.^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

### 2. HTML: 태그, 요소, 속성

HTML은 Hyper Text Markup Language이며, 웹 문서의 구조를 표시한다. 원본은 `span`, `ol`, `ul`, `li`, `table`, `tr`, `th`, `td`, `img`, `hr` 같은 태그를 직접 작성하면서 “태그명”, “시작 태그와 종료 태그”, “속성”, “속성값”을 구분한다.

- 태그: `<table>`, `<li>`, `<img>`처럼 문서 안의 구조/의미를 정한다.
- 속성(attribute): `class`, `id`, `style`, `src`, `alt`, `width`처럼 태그에 추가 정보를 붙인다.
- 요소(element): 보통 시작 태그 + 내용 + 종료 태그까지 합친 실제 문서 조각이다.

이 구분은 [[comparisons/html-tag-vs-attribute|HTML 태그 vs 속성]]에서 따로 정리했다.

### 3. CSS 선택자 3종

원본은 CSS 선택자를 세 단계로 학습한다.

| 선택자 | 예시 | 수업상 의미 |
|---|---|---|
| 태그 선택자 | `li { font-size: 12px; }` | 해당 태그 전체에 적용 |
| class 선택자 | `.myyellow { color: yellow; }` | 여러 요소를 그룹으로 묶어 적용 |
| id 선택자 | `#upper-roman { list-style-type: upper-roman; }` | 한 요소를 식별해 적용 |

특히 class는 `class="myyellow myblue"`처럼 여러 값을 줄 수 있고, id는 원칙적으로 중복하면 안 된다는 점이 반복된다. 관련 비교는 [[comparisons/id-vs-class|id vs class]]를 보면 된다.

### 4. table과 이미지

`table`은 이후 상품 목록, 장바구니, 관리자 화면에서 계속 쓰이는 구조다. 원본은 `thead`, `tbody`, `tr`, `th`, `td`로 표를 만들고, CSS로 `width`, `border-top`, `border-left`, `border-right`, `border-bottom`을 주며 표의 선과 크기를 조절한다.

이미지에서는 `img`와 `alt`를 배운다. `alt`는 이미지가 깨졌을 때 대체 텍스트로 보이고, 접근성 측면에서도 의미가 있다.

### 5. Box Model 맛보기

CSS에서 요소는 사각형 박스로 다뤄진다. 원본은 표와 테두리를 만들면서 `width`, `border`, 색상, 단위(px, %)를 사용한다. 이 개념은 다음 날 `div`, `position`, `display`와 연결된다.

## 핵심 실습

### tableExam

`tableExam.html`을 만들면서 표 구조와 CSS 테두리를 연결했다. 단순히 “표를 그린다”가 아니라, HTML은 행/열 구조를 만들고 CSS는 선·폭·색상을 입힌다는 분업을 배운 실습이다.

### class/id 선택자 실습

`ol`, `li`에 class와 id를 붙이고, `<style>` 내부에서 `.class명`, `#id명`으로 스타일을 지정했다. 사용자가 헷갈리기 쉬운 지점은 HTML 속성의 `class="myyellow"`와 CSS 선택자의 `.myyellow`가 **서로 다른 위치에서 같은 이름으로 연결**된다는 점이다.

## 헷갈린 점 / 질문

- `class="upper-alpha;"`처럼 HTML 속성값 안에 세미콜론을 넣는 것이 아니라, 세미콜론은 CSS 선언 내부에서 `속성: 값;` 형태로 쓴다.
- id는 HTML에서는 중복을 써도 브라우저가 위에서부터 처리할 수 있지만, 개발 원칙상 중복시키지 않아야 한다.
- `style` 속성에 직접 쓰는 방식, `<style>` 태그 내부에 쓰는 방식, 외부 CSS 파일 방식은 역할과 유지보수성이 다르다. 자세한 비교는 [[comparisons/inline-style-vs-internal-css-vs-external-css]]에 정리했다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[entities/html]]
- [[entities/css]]
- [[comparisons/html-tag-vs-attribute]]
- [[comparisons/id-vs-class]]
- [[comparisons/inline-style-vs-internal-css-vs-external-css]]

## 출처

- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/태그들.md`
- `raw/Study/3. UI&UX/UI&UX 총정리/속성들.md`
