---
title: HTML/CSS 기본
type: concept
created: 2026-06-30
updated: 2026-07-02
tags: [html, css, frontend]
sources:
  - raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md
  - raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md
status: growing
confidence: high
---

# HTML/CSS 기본

## 정의

HTML은 웹 문서의 구조를 만드는 마크업 언어이고, CSS는 그 구조의 색·크기·배치·글꼴 같은 표현을 담당하는 스타일 언어다. 수업에서는 웹 서비스 전체 흐름 속에서 먼저 클라이언트 화면을 만들기 위해 HTML/CSS를 배웠다.

## 이 수업에서의 위치

2026-03-23 수업은 Java와 Oracle을 지나 UI&UX 주간으로 넘어가는 시작점이었다. 노트의 흐름은 “클라이언트 → 프론트엔드 → 백엔드 → 데이터베이스”였고, 그중 이번 주에는 사용자가 보는 Client/UI 부분을 먼저 만든다고 정리했다. 이후 React와 Spring Boot 프로젝트에서 화면과 API를 연결하려면, HTML 구조와 CSS 선택자 감각이 먼저 필요하다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

## 핵심 설명

### HTML은 태그, 요소, 속성으로 구조를 만든다

수업에서는 HTML 용어를 다음처럼 나눴다.

- 태그(Tag): `<body>`, `<br>`처럼 꺾쇠괄호로 표현하는 표식
- 요소(Element): 시작 태그와 종료 태그가 묶인 구조
- 셀프 클로징 태그: `<br>`, `<img>`처럼 하나로 요소 역할을 하는 태그
- 속성(Attribute)과 속성값(Value): `<body bgcolor="yellow" text="black">`에서 `bgcolor`, `text`와 그 값

HTML은 엔터와 공백을 그대로 보여주지 않기 때문에 줄바꿈은 `<br>`, 공백이나 특수문자는 문자 엔티티를 써야 한다. 특히 `<`는 태그 시작으로 해석되므로 화면에 문자로 보이고 싶다면 `&lt;`를 써야 한다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

### CSS는 선택자로 “누구에게” 스타일을 줄지 정한다

수업에서는 처음에 태그 안에 직접 `style` 속성을 쓰는 인라인 스타일을 배웠다.

```html
<span style="color: red;">초콜릿</span>
```

이후 `<head>` 안의 `<style>` 태그에서 선택자를 이용해 여러 요소에 스타일을 적용했다.

```html
<style>
    li {
        font-size: 12px;
        color: purple;
    }
</style>
```

즉 HTML은 “무엇이 있는가”를 만들고, CSS는 “그것을 어떻게 보이게 할 것인가”를 정한다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

### class와 id의 차이

수업에서는 class 선택자와 id 선택자를 DB의 개념과 연결해 설명했다.

- `class`: 여러 요소를 같은 그룹으로 묶어 스타일을 줄 때 사용한다.
- `id`: 한 문서 안에서 특정 요소 하나를 식별할 때 사용한다. 노트에서는 DB의 Primary Key처럼 생각할 수 있다고 정리했다.

```html
<li class="myyellow">사과</li>
<ol id="upper-roman">...</ol>
```

```css
.myyellow { color: yellow; background-color: black; }
#upper-roman { list-style-type: upper-roman; }
```

class는 공백으로 여러 개를 동시에 줄 수 있다.

```html
<li class="myyellow myblue">사과</li>
```

여러 class가 같은 속성을 바꾸면 나중에 적용된 규칙이 이기는 top-down 흐름을 함께 봐야 한다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

### 표, 이미지, 링크는 실제 웹 화면의 기본 재료다

허브 소개 테이블 실습에서는 `table`, `caption`, `thead`, `tbody`, `tr`, `th`, `td`를 이용해 표를 만들었다. 이미지는 `img src`, 대체 텍스트는 `alt`, 링크는 `a href`로 연결했다.

```html
<td><a href="https://www.naver.com">바질</a></td>
<td><img src="/images/basil.jpg" alt="바질"></td>
```

`alt`는 이미지가 깨졌을 때 대체 텍스트를 보여주므로, 이후 상품 이미지나 접근성 관점에서도 생활화해야 하는 속성으로 정리할 수 있다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

### CSS 박스 모델은 레이아웃의 기본이다

모든 HTML 요소는 하나의 박스로 볼 수 있다.

1. content: 실제 내용
2. padding: 내용과 테두리 사이의 내부 여백
3. border: 테두리
4. margin: 다른 요소와의 외부 여백

수업에서는 테이블의 `padding`, `border`, `border-collapse`, 배경 이미지, `width` 등을 적용하면서 화면 요소가 왜 그 위치와 크기로 보이는지 확인했다. ^[raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md]

### block과 inline은 배치 감각의 출발점이다

2026-03-24 수업에서는 요소를 block element와 inline element로 나눴다.

- block element: 한 줄을 크게 차지하고 너비·높이 제어가 잘 된다. 예: `<p>`, `<div>`
- inline element: 콘텐츠 크기만큼만 차지하고 옆으로 배치된다. 예: `<span>`

`<div>`는 웹 페이지의 논리적 구역을 나누는 컨테이너 역할을 하고, `<span>`은 문장 일부처럼 작은 범위를 꾸밀 때 좋다. ^[raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md]

### position, display, float, z-index는 배치를 조절한다

박스 모델 실습에서는 부모 `div#mydiv`를 `position: relative`로 두고, 안쪽 자식 `div`들을 `position: absolute`와 `top`, `left`로 배치했다. 자식의 위치는 부모의 위치를 기준으로 계산될 수 있다는 점이 중요하다.

또한 다음 속성들이 소개되었다.

- `overflow`: 내용이 박스 범위를 넘을 때 표시 방식
- `display`: block, inline, inline-block, none 등 화면 표시 방식
- `z-index`: 겹친 요소의 앞뒤 순서
- `float`: 이미지와 텍스트처럼 서로 다른 성질의 요소를 배치할 때 사용

## 자주 헷갈리는 점

### 태그 속성, 인라인 style, CSS 선택자를 구분해야 한다

```html
<li style="color: purple;">...</li>
```

위 코드는 태그 안에 직접 스타일을 넣은 것이다. 반면 아래는 CSS 선택자로 `li` 전체에 스타일을 적용한다.

```css
li { color: purple; }
```

처음에는 둘 다 “색을 바꾼다”로 보이지만, 유지보수 측면에서는 어떤 범위에 적용되는지 구분해야 한다.

### id는 중복하지 않는 것이 원칙이다

수업 노트에는 HTML에서 id가 중복되어도 화면이 완전히 멈추지는 않지만, top-down 방식 때문에 가장 위쪽 id가 인식될 수 있다고 정리되어 있다. 실무에서는 JavaScript DOM 선택, CSS, 접근성, 테스트가 모두 꼬일 수 있으므로 id는 한 문서 안에서 하나만 쓰는 것이 원칙이다.

### CSS는 위에서 아래로 읽히지만 우선순위도 함께 작동한다

수업에서는 `li` 태그 선택자로 보라색을 준 뒤, `.myyellow` class로 노란색을 주면 나중 규칙이 적용되는 top-down 흐름을 확인했다. 다만 실제 CSS에서는 선택자의 구체성도 작동하므로 “항상 아래가 이긴다”가 아니라 “우선순위와 선언 순서를 함께 본다”가 더 정확하다.

## 이전/이후 학습과의 연결

- 이전: Java/Oracle에서는 데이터와 로직을 배웠고, HTML/CSS부터는 사용자가 보는 화면을 만든다.
- 이후: [[concepts/bootstrap-basics|Bootstrap 기본]]은 CSS를 직접 모두 작성하지 않고 준비된 class로 화면을 빠르게 만드는 단계다.
- 이후: [[concepts/javascript-dom|JavaScript와 DOM]]은 HTML 요소를 JavaScript 객체로 읽고 바꾸는 단계다.
- 프로젝트: React에서도 JSX는 결국 HTML과 비슷한 구조를 만들고, className과 CSS/Bootstrap으로 표현을 입힌다.

## 관련 개념

- [[entities/html|HTML]]
- [[entities/css|CSS]]
- [[concepts/bootstrap-basics|Bootstrap 기본]]
- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[summaries/2026-03-23-html-css-intro|2026-03-23 HTML/CSS와 웹 UI 입문]]
- [[summaries/2026-03-24-css-layout-javascript-intro|2026-03-24 CSS 레이아웃과 JavaScript 입문]]

## 출처

- `raw/Study/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/Study/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
