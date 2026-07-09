---
title: React 폼 상태와 이벤트
created: 2026-07-02
updated: 2026-07-09
type: concept
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---
# React 폼 상태와 이벤트

## 정의

React 폼 상태 관리는 input/select/checkbox 같은 입력값을 React state로 보관하고, 이벤트 핸들러에서 값을 갱신하는 패턴이다.

## 왜 중요한가

상품 등록, 회원가입, 검색 조건, 장바구니 선택은 모두 사용자의 입력을 화면 상태로 관리한 뒤 API 요청으로 보내는 구조다. 폼 상태를 제대로 다루지 못하면 화면 값과 서버 요청 값이 어긋난다.

## 핵심 설명

React 교안은 이벤트 이름이 `onClick`, `onChange`처럼 camelCase이고, 문자열 호출이 아니라 함수 참조를 전달한다고 설명한다. event object에는 `target`, `currentTarget`, `preventDefault`, `stopPropagation` 등이 있다.

전개 연산자 `...`는 기존 객체/배열을 보존하면서 일부 필드만 바꿀 때 자주 쓴다.

```typescript
setForm({
  ...form,
  [event.target.name]: event.target.value,
});
```

## 수업 예시

- [[summaries/2026-04-10-react-event-spread-product-form|2026-04-10]] — 상품 등록 폼에서 event object와 전개 연산자를 사용했다.
- [[summaries/2026-04-21-product-pagination-search-react|2026-04-21]] — 검색 필드와 검색어를 state로 관리했다.

## 자주 헷갈리는 점

- `event.target`은 실제 이벤트가 발생한 요소이고, `currentTarget`은 핸들러가 붙은 요소다.
- `preventDefault`는 기본 제출/이동 동작을 막고, `stopPropagation`은 이벤트 버블링을 막는다.
- state를 직접 수정하면 React가 변경을 감지하지 못할 수 있다.

## 관련 개념

- [[comparisons/props-vs-state]]
- [[concepts/react-typescript-basics]]
- [[concepts/product-domain-flow]]
- [[entities/react]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
