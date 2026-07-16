---
title: UI vs UX
created: 2026-07-15
updated: 2026-07-15
type: comparison
tags: [frontend, curriculum]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어.pdf"
  - "raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어2.pdf"
status: growing
confidence: high
---

# UI vs UX

## 비교 목적

UI(User Interface)와 UX(User Experience)는 같은 말이 아니다. UI는 사용자가 직접 보고 조작하는 접점이고, UX는 그 접점을 포함해 서비스를 이용하면서 겪는 전체 경험이다. UI&UX 첫 수업은 이 차이를 확인한 뒤 HTML/CSS 화면 구현으로 들어갔다.

## 한눈에 보기

| 항목 | UI | UX |
|---|---|---|
| 한국어 | 사용자 인터페이스 | 사용자 경험 |
| 중심 질문 | 사용자가 무엇을 보고 누르는가? | 사용자가 전체 과정을 얼마나 쉽고 만족스럽게 이용하는가? |
| 수업 표현 | 디자인, 시각적 요소, 사용자가 보는 것 | 유용성, 만족감, 사용자가 느끼는 것 |
| 예 | 버튼, 입력창, 메뉴, 색상, 배치 | 버튼 반응, 로딩 속도, 오류 이해도, 목표 달성 흐름 |
| 구현 관계 | HTML/CSS/Bootstrap으로 화면 접점을 구성 | 화면 구조·상태·반응·메시지를 함께 설계 |

## 언제 무엇을 쓰는가

### 상황 1: 상품 등록 화면을 만든다

`input`, `select`, 등록 버튼의 배치와 색상은 UI 문제다. 사용자가 무엇을 입력해야 하는지 알고, 오류가 나면 원인을 이해하며, 등록 완료 여부를 확인할 수 있는지는 UX 문제다.

### 상황 2: 상품 상세 정보를 불러온다

상품 카드와 버튼의 모양은 UI다. 로딩 중인지, 데이터가 없는지, 정상적으로 표시됐는지를 구분해 알려 주는 흐름은 UX다. 교육자료의 `ProductDetail.html`이 `loadingView`, `errorView`, `successView`를 따로 둔 이유가 여기에 연결된다.

## 함께 쓰는 관계

좋은 UX는 UI 없이 전달될 수 없고, 보기 좋은 UI만으로 좋은 UX가 자동 보장되지 않는다. 예를 들어 버튼이 예뻐도 클릭 결과가 없거나 오류 문구가 이해되지 않으면 UX는 나쁘다. 반대로 흐름이 논리적이어도 버튼과 입력창을 찾기 어렵다면 사용자는 목표를 달성하기 어렵다.

## 헷갈리기 쉬운 포인트

- UI는 단순히 “예쁘게 꾸미기”가 아니다. 사용자가 보고 조작하는 구조와 상태 표현까지 포함한다.
- UX는 화면 디자인 한 장이 아니라 사용 전·사용 중·사용 후의 전체 경험이다.
- HTML을 작성했다는 사실만으로 UX가 완성되는 것은 아니다. 로딩, 오류, 입력 안내, 반응 속도 같은 흐름을 함께 확인해야 한다.
- 이 과목에서 직접 구현한 것은 HTML/CSS/Bootstrap/JavaScript/jQuery 기반 화면이다. 후속 React·Spring 구현을 이 단계의 직접 실습으로 섞지 않는다.

## 수업 예제

2026-03-23 원본은 UI를 “디자인, 시각적 요소, 사용자가 보는 것”, UX를 “유용성, 만족감, 사용자가 느끼는 것”으로 구분했다. 이후 수업은 정적 화면에서 시작해 form, 상품 목록·상세, 상태 화면, 이미지 상호작용으로 확장되었다.

## 관련 페이지

- [[summaries/2026-03-23-html-css-intro]]
- [[summaries/2026-03-27-uiux-subject-review]]
- [[concepts/html-css-basics]]
- [[concepts/javascript-dom]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.23(월) - 시작/2026.03.23(월) - 시작.md`
- `raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어.pdf`
- `raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어2.pdf`
