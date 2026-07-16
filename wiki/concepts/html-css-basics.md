---
title: HTML/CSS 기본
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [html, css, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/tableExam.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/boxModelTest.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/styleExam.html"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/A.html&js&css/outerFile.css"
  - "raw/KoreaICT/3. UI&UX/교육 자료/소스코드 파일들/ui_ux_project/B.nobootstrap/ProductInsertForm.html"
status: growing
confidence: high
---

# HTML/CSS 기본

## 정의

HTML은 웹 문서의 구조를 만드는 markup language이고, CSS는 그 구조를 선택해 모양과 배치를 지정하는 style language다. 이 수업에서는 HTML을 “태그로 뼈대를 만들고”, CSS를 “선택자로 대상을 골라 속성:값을 적용하는 방식”으로 배웠다.

## 왜 중요한가

나중에 React를 쓰더라도 화면은 결국 HTML 요소와 CSS 규칙으로 렌더링된다. Spring Boot가 데이터를 보내도 사용자는 브라우저 화면으로 결과를 본다. 따라서 UI&UX의 HTML/CSS는 전체 웹서비스 흐름에서 프론트엔드의 가장 기본 층이다.

## 핵심 설명

### HTML은 태그·속성·요소로 구조를 만든다

- 태그: `<table>`, `<div>`, `<form>`처럼 구조나 의미를 표시한다.
- 속성: `class`, `id`, `style`, `src`, `alt`, `name`, `type`처럼 태그에 세부 정보를 붙인다.
- 요소: 태그와 내용이 실제 문서 안에서 하나의 객체처럼 존재하는 단위다.

관련 비교: [[comparisons/html-tag-vs-attribute]].

### CSS는 선택자와 선언으로 이루어진다

```css
.myyellow{color: yellow;background-color: black;}
.myblue{color: blue;}
```

이 코드는 2026-03-23 원본에서 `class="myyellow myblue"`처럼 class 이름을 공백으로 함께 지정한 실습과 연결된다. 두 규칙 모두 `color`를 지정하므로 뒤에 선언된 `.myblue`의 파란색이 적용되는 모습을 통해 cascade의 영향을 확인했다.

수업에서는 세 선택자를 반복했다.

| 선택자 | HTML 쪽 | CSS 쪽 | 용도 |
|---|---|---|---|
| 태그 선택자 | `<li>` | `li { ... }` | 해당 태그 전체 |
| class 선택자 | `<li class="myyellow">` | `.myyellow { ... }` | 여러 요소 그룹 |
| id 선택자 | `<ol id="upper-roman">` | `#upper-roman { ... }` | 특정 요소 하나 |

### Box Model은 화면을 사각형으로 보는 관점이다

`width`, `height`, `border`, `margin`, `padding`은 요소를 사각형 박스로 다룬다. `tableExam`과 `boxModelTest`는 이 감각을 익히는 실습이었다.

### display와 position은 배치의 핵심이다

- `display: block`: 한 줄 전체 폭을 차지한다. `div`, `p`, `table` 등이 대표적이다.
- `display: inline`: 글자 흐름처럼 이어진다. `span`이 대표적이다.
- `display: inline-block`: inline처럼 옆에 붙지만 크기 조절도 가능하다.
- `position: relative`: 자기 위치를 기준으로 이동하거나, 자식 absolute의 기준을 만든다.
- `position: absolute`: 기준 요소를 찾아 좌표로 배치한다.

### table과 form은 이후 프로젝트까지 이어진다

`table`은 장바구니/상품 목록처럼 행과 열의 데이터를 보여줄 때 쓰고, `form`은 상품 등록처럼 사용자 입력을 받을 때 쓴다. 원본에서 “form은 입력 양식”이고 “그냥 표 같은 건 table이 좋다”는 구분이 중요하다.

수업 등장 순서도 이 역할 차이를 따른다. 2026-03-23에는 table로 기존 데이터를 표시했고, 2026-03-25에는 form으로 상품 등록 입력을 받았다. 2026-03-26에는 JavaScript가 상품 배열을 DOM에 표시하면서 정적 HTML과 동적 화면을 연결했다.

## 예시

```html
<select id="category" name="category">
	<option value="bread">빵</option>
	<option value="beverage">음료수</option>
	<option value="cake">케이크</option>
	<option value="macaron">마카롱</option>
</select>
```

이 예시는 2026-03-25 원본의 실제 form 구성 일부다. `select`는 태그, `id`·`name`·`value`는 속성, 각 `option`은 사용자가 고를 수 있는 항목이다.

## 자주 헷갈리는 점

- HTML의 `class="myyellow"`와 CSS의 `.myyellow`는 위치가 다르지만 같은 이름으로 연결된다.
- id는 `#id명`, class는 `.class명`으로 선택한다.
- inline style은 빠르지만 유지보수에 약하고, internal/external CSS는 구조화에 좋다. 비교는 [[comparisons/inline-style-vs-internal-css-vs-external-css]].
- CSS 속성의 세미콜론은 선언 끝에 붙는다. HTML 속성값에 임의로 `;`를 붙이는 것이 아니다.
- `태그들.md`에 적힌 `<alt>`는 실제 태그가 아니다. `alt`는 `<img src="..." alt="...">`처럼 이미지 요소에 붙는 속성이다.

## 관련 개념

- [[entities/html]]
- [[entities/css]]
- [[concepts/bootstrap-basics]]
- [[concepts/html-form-controls-submission]]
- [[comparisons/id-vs-class]]
- [[comparisons/custom-css-vs-bootstrap]]
- [[summaries/2026-03-27-uiux-subject-review]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/태그들.md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/속성들.md`
