---
title: 2026-04-15 장바구니 목록과 TypeScript props
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
status: growing
confidence: high
---
# 2026-04-15 장바구니 목록과 TypeScript props

## 한 줄 요약

React 장바구니 목록에서 전체 선택, props 구조 분해, 타입 지정, 로그인 사용자 조건 처리를 다뤘다.

## 커리큘럼 위치와 흐름

백엔드 장바구니 API를 만든 뒤, React 화면에서 장바구니 데이터를 목록으로 보여주고 선택 상태를 관리하는 단계다. TypeScript 타입과 props/state 구분이 중요해진다.

## 배운 내용

- 장바구니 목록 컴포넌트에서 부모가 내려준 props를 구조 분해해 사용했다.
- 전체 선택/개별 선택 상태를 관리하며, 선택된 상품만 주문 또는 합계 계산에 반영하는 흐름을 준비했다.
- 쇼핑 카트 다이어그램의 CartProduct 단위가 화면의 한 행과 연결된다.

## 핵심 실습 / 예제

- `CartList.tsx`에서 cartProducts 배열을 렌더링하고, checkbox 상태를 state로 관리한다.
- 로그인 사용자의 장바구니만 보여줘야 하므로 인증 정보와 API 요청이 연결된다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- props는 부모가 내려주는 읽기 중심 입력이고, state는 컴포넌트 내부에서 바뀌는 값이다.
- 전체 선택은 단순 boolean 하나로 끝나지 않고 각 항목의 선택 상태와 동기화해야 한다.
- TypeScript 타입은 API 응답의 실제 모양과 어긋나면 렌더링 오류를 숨기지 않고 드러낸다.

## 관련 페이지

- [[concepts/shopping-cart-flow]]
- [[comparisons/props-vs-state]]
- [[concepts/react-typescript-basics]]
- [[entities/typescript]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
