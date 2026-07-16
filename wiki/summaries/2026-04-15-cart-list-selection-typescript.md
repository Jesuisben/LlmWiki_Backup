---
title: 2026-04-15 장바구니 목록과 TypeScript props
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
status: growing
confidence: high
---

# 2026-04-15 장바구니 목록과 TypeScript props

## 한 줄 요약

전날 표시한 `CartList`에 로그인 사용자 props, 전체·개별 선택과 선택 금액 계산을 연결한 뒤, 수량 변경 요청을 React 입력에서 Spring Service·Controller와 DB 확인까지 확장하고 삭제 API의 기반을 만든 날이다.

## 이전 수업과 오늘의 위치

- 전날 [[summaries/2026-04-14-cart-service|2026-04-14]]에는 인증 사용자의 Cart를 저장·조회하고 `CartItemDto` 배열을 React 표에 표시했다. checkbox, 수량 input, 삭제 버튼은 보였지만 선택·변경·삭제 동작은 아직 연결되지 않은 control이었다.
- 오늘은 그 표에 화면 state와 event handler를 붙이고, 수량 변경은 실제 PATCH 요청과 Spring 처리까지 연결했다.
- 다음 [[summaries/2026-04-16-cart-quantity-stock|2026-04-16]]에는 수량 검증이 CartProduct의 연결 Product 재고를 직접 보도록 보정하고 React 삭제를 완성한 뒤 Order 도메인을 시작한다.

## 왜 이 흐름으로 배웠는가

장바구니 목록을 보여 주는 것과 사용자가 목록을 조작하는 것은 다른 단계다. 선택은 React 화면 state만 바꾸지만, 수량과 삭제는 DB의 CartProduct도 바꿔야 한다. 따라서 먼저 전체·개별 선택과 합계를 화면 안에서 완성하고, 그 다음 입력값을 URL parameter와 Controller 매개변수로 전달해 서버 상태를 바꾸는 순서로 확장했다.

## 실제 교시 흐름

1. **1교시 — 전체 선택과 합계:** `orderTotalPrice` state를 만들고, 선택된 품목의 `price * quantity`를 누적하는 `refreshOrderTotalPrice`를 작성했다. `toggleAllCheckBox`는 각 객체의 다른 필드는 보존하고 `checked`만 일괄 변경한 새 배열로 합계를 다시 계산했다.
2. **1교시의 props·로그인 조건:** `AppProps`의 `user: User | null`과 `function App({ user }: AppProps)`를 통해 구조 분해와 타입 지정을 설명했다. `useEffect`는 user와 id가 있을 때만 Cart 목록을 요청하고 user 변경을 의존성으로 삼았다.
3. **2교시 — 사용자 표시와 개별 선택:** `MenuItems`에 로그인한 사용자 이름을 표시했다. `toggleCheckBox`는 받은 `cartProductId`와 일치하는 품목의 `checked`만 반전하고, 변경된 배열로 합계를 다시 계산했다. 전체 선택→전체 합계, 전체 해제→0, 개별 토글→합계 재계산 시나리오를 확인했다.
4. **3교시 — 수량 입력 연결:** number input의 문자열 값을 `parseInt`로 바꿔 `changeQuantity`에 전달했다. 숫자가 아니면 해당 화면 수량을 0으로 두고 중단하며, 정상 값이면 CartProduct id와 quantity를 URL에 넣어 PATCH 요청을 보냈다. 성공 후 해당 품목의 화면 quantity와 총액을 갱신했다.
5. **4교시 — Spring 수량 변경 입구:** `CartController`가 path의 CartProduct id와 request parameter의 quantity를 받고 `CartProductService`에 위임했다. Service 메시지가 `오류`로 시작하는지에 따라 bad request와 정상 응답을 나눴고, JOIN SQL로 DB 수량을 확인했다.
6. **5교시 — 재고 검증 보정:** 처음에는 Product 조회 id가 임시값으로 남은 Service가 있었고, 이후 React가 product id를 추가 parameter로 보내고 Controller·Service가 함께 받도록 수정했다. Service는 quantity 최소값, Product 존재, stock 초과, CartProduct 존재를 검사한 뒤 quantity를 덮어써 저장했다.
7. **5교시 용어 보충:** query string에서 `?` 뒤의 parameter 목록, `&` 구분자, 이름=값 구조를 정리하고 quantity와 product id를 한 변수로 조립했다.
8. **6교시 — 삭제 API 기반:** 삭제 버튼에 CartProduct id를 넘기는 방향을 잡고, Service의 Repository 삭제와 Controller의 삭제 응답을 추가했다. 이 날짜 원본에는 React 삭제 함수 본문보다 버튼 연결 안내와 백엔드 구현이 중심이며, confirm→DELETE→state 제거까지의 완성본은 다음 날 나온다.
9. **7교시 — 삭제 테스트:** 로그인 고객의 Cart에서 삭제 버튼을 시험하는 시나리오를 두었다. **8교시는 자습**이었다.

## 대표 artifact

- **`AppProps`와 구조 분해:** 부모가 넘긴 로그인 user가 객체 또는 null일 수 있음을 타입으로 고정한다.
- **`toggleAllCheckBox` / `toggleCheckBox`:** CartProduct 배열의 `checked`만 바꾸고 변경 직후의 배열로 합계를 계산한다.
- **`changeQuantity`:** input 문자열→정수→PATCH URL→응답 성공 후 React state 갱신을 담당한다.
- **`CartProductService` / `CartController`:** 수량·재고·대상 존재를 검사하고 CartProduct quantity를 저장하는 서버 경로를 구성한다.
- **삭제 Service·Controller:** CartProduct id로 Repository 삭제를 호출하는 백엔드 기반이다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| 전체 선택 | 상단 checkbox의 boolean | 모든 품목의 `checked`를 같은 값으로 복사→선택 품목 합계 재계산 | 모든 checkbox와 총 주문 금액이 함께 바뀜 |
| 개별 선택 | 품목의 CartProduct id | 일치 품목의 `checked` 반전→새 배열로 합계 계산 | 한 품목의 선택 상태와 총액 갱신 |
| 수량 변경 | input 문자열, CartProduct id, 후반에는 Product id | 정수 변환→PATCH→Controller→Service 검증→CartProduct 저장 | 성공 시 화면 quantity·총액과 DB 수량 변경 |
| 삭제 기반 | 삭제할 CartProduct id | 버튼에서 id 전달 방향 설정→Controller→Service→Repository 삭제 | 서버 삭제 경로 마련; React 전체 삭제 함수는 다음 날 완성 |

## 화면 control과 실제 연결 상태

- 전체 선택 checkbox는 `onChange`가 `toggleAllCheckBox`에 연결됐고, 개별 checkbox도 `toggleCheckBox`에 연결됐다.
- 총 주문 금액은 단순 표시값이 아니라 선택 handler가 갱신하는 state와 연결됐다.
- 수량 input은 `changeQuantity`와 PATCH 요청까지 연결됐다.
- 삭제 버튼과 서버 삭제 메서드는 등장했지만, confirm·DELETE 호출·React 배열 제거를 포함한 삭제 함수 전체는 이 날짜 원본에서 완결된 형태로 제시되지 않는다.
- 주문하기 버튼은 화면에 있지만 오늘은 주문 handler가 연결되지 않았다. Order 요청은 04-16부터 구현한다.

## 헷갈린 점 / 질문

- **props와 state:** user는 부모가 내려주는 props이고, `cartProducts`·`orderTotalPrice`는 이 화면이 바꾸는 state다. 구조 분해는 props 전달을 state로 바꾸는 문법이 아니다.
- **로그인 조건:** 화면 제목은 optional chaining으로 user 이름을 읽고, 목록 요청은 user와 id가 있을 때만 실행한다. control이 보인다고 비로그인 요청까지 성공하는 것은 아니다.
- **이전 state로 합계를 계산하면 왜 어긋나는가:** setter 직후 기존 state를 읽는 대신 map으로 만든 `updatedProducts`를 합계 함수에 넘겼다.
- **Product id를 따로 보내는 초안:** 오후에는 재고 조회를 위해 product id를 parameter로 추가했지만, 다음 날에는 먼저 CartProduct를 찾고 연결된 Product의 stock을 읽는 방식으로 보정한다.
- **선택과 서버 상태:** `checked`는 화면 선택 상태이므로 오늘 선택 handler는 DB에 저장하지 않는다. quantity와 삭제는 서버 상태를 바꾸는 별도 API다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** CartList 전체/개별 선택, 합계, props·구조 분해, 로그인 사용자 조건, 수량 PATCH와 재고 검증 초안, 삭제 백엔드 기반이다.
- **다음 날짜:** 04-16은 CartProduct 관계를 이용한 재고 보정, React 삭제 완성, Order Entity·DTO·생성 API를 다룬다. 04-17은 stock 표시·오류 Alert·`some` 검증과 주문 목록 조회를 시작한다.
- 검색/페이징은 04-21~04-22이며 Linux·AWS·CI/CD·Passwordless는 운영·배포·인증 확장이다. 오늘 직접 구현으로 합치지 않는다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[comparisons/props-vs-state|props vs state]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
