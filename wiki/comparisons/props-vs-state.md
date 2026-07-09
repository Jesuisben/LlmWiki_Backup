---
title: props vs state
created: 2026-07-02
updated: 2026-07-09
type: comparison
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---
# props vs state

## 비교 목적

React 장바구니 목록, 상품 등록 폼, 검색 조건 관리에서 props와 state가 반복적으로 등장한다. 둘 다 컴포넌트가 쓰는 값이지만 책임이 다르다.

## 한눈에 보기

| 항목 | props | state |
|---|---|---|
| 누가 소유하나 | 부모 컴포넌트 | 현재 컴포넌트 |
| 변경 방식 | 자식이 직접 바꾸지 않음 | setter로 변경 |
| 용도 | 데이터/함수 전달 | 입력값, 선택 여부, 로딩 상태 등 변하는 값 |
| 예 | 장바구니 행 컴포넌트에 내려준 item | checkbox 선택 여부, 상품 폼 입력값 |

## 언제 무엇을 쓰는가

- 부모가 이미 가진 데이터를 자식에게 보여주려면 props를 쓴다.
- 사용자의 입력, 버튼 클릭, 체크박스 선택처럼 화면 안에서 바뀌는 값은 state로 둔다.
- 자식이 부모 state를 바꿔야 하면 부모가 setter 또는 handler 함수를 props로 내려준다.

## 헷갈리기 쉬운 포인트

- props를 자식에서 직접 수정하려 하지 말고, 이벤트 handler를 통해 부모 state를 바꾸게 한다.
- TypeScript에서는 props 타입을 명시해 컴포넌트가 어떤 데이터를 기대하는지 드러낸다.
- state 객체를 바꿀 때는 기존 값을 직접 수정하지 말고 전개 연산자로 새 객체/배열을 만들어 갱신한다.

## 관련 페이지

- [[concepts/react-typescript-basics]]
- [[concepts/react-form-state-event]]
- [[summaries/2026-04-15-cart-list-selection-typescript]]
- [[summaries/2026-04-21-product-pagination-search-react]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
