---
title: React와 TypeScript 기본
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [react, typescript, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: medium
---

# React와 TypeScript 기본

## 정의

React는 UI를 컴포넌트 단위로 만드는 프론트엔드 라이브러리이고, TypeScript는 JavaScript에 타입을 더해 실수를 줄이는 언어다.

## 왜 중요한가

학원 실습의 프론트엔드는 상품 목록, 장바구니, 주문 목록처럼 상태가 바뀌는 화면을 React 컴포넌트로 구성한다. TypeScript는 props와 state의 모양을 명확히 해준다.

## 핵심 설명

- 컴포넌트: 화면을 이루는 재사용 가능한 조각이다.
- props: 부모 컴포넌트가 자식에게 넘기는 값이다.
- state: 컴포넌트 내부에서 바뀌는 값이다.
- Hook: `useEffect`처럼 컴포넌트 생명주기나 상태 변화를 다루는 함수다.
- 라우팅: 주소에 따라 다른 컴포넌트를 보여준다.

## 예시

`ProductList.tsx`는 상품 목록 state를 가지고, `useEffect`에서 API를 호출한 뒤 `setProducts()`로 화면을 갱신한다.

## 자주 헷갈리는 점

- 구조 분해 할당은 문법 축약이고, 타입 지정은 데이터 모양을 설명하는 별도 개념이다.
- `event.target`은 이벤트가 발생한 실제 요소를 가리킨다.
- 전개 연산자는 기존 객체/배열을 유지하면서 일부 값만 바꿀 때 자주 쓰인다.

## 관련 개념

- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[entities/react|React]]
- [[entities/typescript|TypeScript]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
