---
title: 2026-04-10 React 이벤트 객체와 전개 연산자
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---
# 2026-04-10 React 이벤트 객체와 전개 연산자

## 한 줄 요약

React 이벤트 객체와 전개 연산자를 이용해 상품 등록 폼의 상태를 안전하게 갱신하는 방법을 배웠다.

## 커리큘럼 위치와 흐름

상품 삭제 다음으로 상품 등록 화면을 만들며, 사용자가 입력한 값을 React state에 누적하는 패턴을 익혔다. 이는 이후 회원가입, 장바구니 선택, 검색 조건 관리에도 반복된다.

## 배운 내용

- React 교안 p.72~73은 `onClick`, `onChange` 같은 이벤트 이름과 event object의 주요 속성/메서드를 설명한다.
- React 교안 p.41은 전개 연산자 `...`가 배열/객체의 나머지 값 또는 기존 값을 펼쳐 새 객체를 만들 때 쓰임을 보여준다.
- 상품 등록 폼에서 입력값 변경 시 기존 state를 보존하고 특정 필드만 갱신하는 방식으로 연결된다.

## 핵심 실습 / 예제

- `setProduct({...product, [name]: value})` 같은 패턴은 기존 상품 입력값을 유지하면서 변경된 input만 반영하는 핵심 예제다.
- 이미지 업로드/미리보기에서는 `data:image/png;base64,...` 형태의 데이터 URL도 등장했다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- state 객체를 직접 수정하면 React가 변경을 감지하지 못할 수 있다.
- `event.target`과 `event.currentTarget`은 같은 경우도 있지만 이벤트 위임/버블링에서는 다를 수 있다.
- 전개 연산자는 깊은 복사를 자동으로 보장하는 만능 도구가 아니라, 주로 얕은 복사에 쓰인다.

## 관련 페이지

- [[concepts/react-form-state-event]]
- [[comparisons/props-vs-state]]
- [[concepts/product-domain-flow]]
- [[entities/react]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
