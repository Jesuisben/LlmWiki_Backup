---
title: 2026-04-09 상품 삭제, 라우팅, JSX와 표
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---
# 2026-04-09 상품 삭제, 라우팅, JSX와 표

## 한 줄 요약

상품 삭제 기능을 구현하면서 React 라우팅, JSX 내부 JavaScript 표현, 이벤트 버블링 방지, HTML 표 병합을 함께 다뤘다.

## 커리큘럼 위치와 흐름

상품 Entity를 만든 뒤 CRUD 중 삭제와 화면 이동을 다뤘다. 이때 React 화면 라우팅과 API 호출 URL이 다시 만났고, JSX 안에서 JavaScript를 쓰는 방식도 함께 익혔다.

## 배운 내용

- `JwtTokenProvider` 일부 수정과 상품 삭제 API/화면 연결을 다뤘다.
- `AppRouters.tsx`에서 상품 관련 경로를 설정했다.
- 라우터 설명 이미지는 Router가 관객을 알맞은 극장으로 안내하듯 URL에 맞는 화면 컴포넌트를 선택한다는 비유를 제공한다.
- JSX 안에서 조건/표현식, 필드 검색 영역 주석, 이벤트 버블링 방지 등을 확인했다.

## 핵심 실습 / 예제

- 삭제 버튼 클릭 시 이벤트가 부모 요소로 전파되면 의도치 않은 상세 이동 등이 일어날 수 있으므로 `stopPropagation` 같은 이벤트 제어가 중요하다.
- HTML table의 `rowSpan`, `colSpan`은 관리자 화면이나 목록 테이블 구성에 재사용된다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- React Router의 삭제 화면 이동과 Spring의 DELETE API 호출을 구분해야 한다.
- JSX의 `{}`는 JavaScript 표현식을 넣는 자리이지, 임의의 문장을 아무렇게나 넣는 공간은 아니다.
- 이벤트 버블링을 이해하지 못하면 버튼 클릭이 행 클릭과 동시에 처리될 수 있다.

## 관련 페이지

- [[comparisons/react-router-vs-spring-api-url]]
- [[concepts/product-domain-flow]]
- [[concepts/react-form-state-event]]
- [[entities/react]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
