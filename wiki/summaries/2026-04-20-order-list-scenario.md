---
title: 2026-04-20 주문 목록과 테스트 시나리오
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf
status: growing
confidence: high
---
# 2026-04-20 주문 목록과 테스트 시나리오

## 한 줄 요약

장바구니 다음 단계로 주문 목록 화면과 주문 상태 변경 테스트 시나리오를 만들었다.

## 커리큘럼 위치와 흐름

장바구니는 사용자가 구매 전 담아두는 임시 상태이고, 주문은 구매 의사와 상태 관리가 들어가는 업무 데이터다. 이 날은 OrderList 화면과 관리자/사용자 시나리오를 통해 기능 검증 관점을 배웠다.

## 배운 내용

- `OrderList.tsx`에서 주문 목록을 보여주고 상태 변경 버튼을 구성했다.
- 테스트 시나리오를 작성해 일반 사용자와 관리자 관점에서 주문 완료 처리 흐름을 확인했다.
- 장바구니 선택 상품이 주문으로 전환되는 흐름을 전체 풀스택 기능 관점에서 연결했다.

## 핵심 실습 / 예제

- 주문 상태 변경 버튼은 단순 UI가 아니라 서버의 주문 상태를 바꾸는 API와 연결된다.
- 테스트 시나리오는 “화면이 뜬다”를 넘어서, 역할별로 어떤 버튼이 보이고 어떤 상태 전이가 가능한지 확인하는 기준이 된다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- 장바구니 상품과 주문 상품은 생명주기가 다르다. 주문이 생성된 뒤에는 가격/수량 기록을 보존해야 한다.
- 관리자 기능과 일반 사용자 기능을 같은 화면에서 다룰 때 권한 조건이 필요하다.
- 상태 변경은 PUT/PATCH 계열 API와 잘 연결된다.

## 관련 페이지

- [[concepts/order-flow]]
- [[concepts/shopping-cart-flow]]
- [[concepts/fullstack-project-flow]]
- [[comparisons/controller-service-repository]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf`
