---
title: id vs class
created: 2026-07-06
updated: 2026-07-06
type: comparison
tags: [html, css, frontend]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md"
  - "raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md"
status: growing
confidence: high
---

# id vs class

## 비교 목적

UI&UX 수업은 CSS 선택자에서 class와 id를 반복해서 다룬다. JavaScript DOM 조작과 jQuery 선택자에서도 둘의 차이가 계속 중요하다.

## 한눈에 보기

| 항목 | id | class |
|---|---|---|
| HTML | `id="upper-roman"` | `class="myyellow"` |
| CSS 선택자 | `#upper-roman` | `.myyellow` |
| 중복 | 원칙적으로 한 문서에서 유일 | 여러 요소에 반복 사용 가능 |
| 여러 값 | 보통 하나 | `class="myyellow myblue"`처럼 여러 개 가능 |
| JS 사용 | `getElementById`로 특정 요소 찾기 좋음 | 여러 요소 그룹 처리에 좋음 |

## 핵심 설명

id는 “한 요소를 식별하는 이름”이고, class는 “공통 스타일/기능을 묶는 이름”이다. 원본에서는 id가 중복되면 브라우저가 top-down으로 먼저 만나는 값을 잡을 수 있다고 설명하지만, 실제 개발 원칙은 id를 중복하지 않는 것이다.

## 예시

```html
<ol id="upper-roman">
  <li class="myyellow myblue">사과</li>
</ol>
```

```css
#upper-roman { list-style-type: upper-roman; }
.myyellow { color: yellow; }
.myblue { background-color: blue; }
```

## 헷갈리기 쉬운 포인트

- HTML에서는 `id="..."`, CSS에서는 `#...`.
- HTML에서는 `class="..."`, CSS에서는 `.class명`.
- Bootstrap은 대부분 class 선택자 기반으로 동작한다.
- jQuery도 `$("#id")`, `$(".class")`처럼 CSS 선택자 문법을 그대로 활용한다.

## 관련 페이지

- [[concepts/html-css-basics]]
- [[concepts/javascript-dom]]
- [[concepts/jquery-basics]]
- [[entities/css]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/KoreaICT/3. UI&UX/2026.03.24(화)/2026.03.24(화).md`
- `raw/KoreaICT/3. UI&UX/UI&UX 총정리/UI&UX 총정리.md`
