---
title: 2026-04-17 장바구니 합계와 Array some
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: high
---

# 2026-04-17 장바구니 합계와 Array some

## 한 줄 요약

Cart 응답에 stock을 추가해 재고·수량·선택·합계를 한 화면에 맞추고 `some`으로 잘못된 선택 수량을 막은 뒤, 상품 상세 즉시 주문과 역할별 PENDING 주문 목록 조회를 시작한 날이다.

## 이전 수업과 오늘의 위치

- 전날 [[summaries/2026-04-16-cart-quantity-stock|2026-04-16]]에는 Cart 수량·삭제를 정리하고 Order Entity·DTO·생성 API를 구현했다.
- 오늘은 Cart에서 주문하기 전에 현재 stock과 0 수량을 화면에서 검증하도록 보강하고, 장바구니가 아닌 Product 상세 화면에서도 같은 주문 API를 호출했다.
- 다음 [[summaries/2026-04-20-order-list-scenario|2026-04-20]]에는 오늘 만든 OrderList 기본 조회를 카드 목록과 역할별 버튼으로 확장하고 완료·취소 처리를 구현한다.

## 왜 이 흐름으로 배웠는가

주문 생성 Service가 재고를 최종 검사하더라도 사용자가 화면에서 재고와 잘못된 수량을 먼저 확인할 수 있어야 한다. 그래서 DTO→TypeScript→표로 stock을 전달하고 배열 조건 검사와 오류 Alert를 붙였다. 그 다음 같은 Order API를 Cart와 Product 상세 두 진입점에서 사용하고, 생성된 주문을 다시 역할별 목록으로 읽는 방향으로 확장했다.

## 실제 교시 흐름

1. **1교시 — stock 전달:** Spring `CartItemDto`와 그 변환 생성자에 stock을 추가하고 React `CartProduct` type에도 같은 필드를 추가했다. 백엔드 Product 재고가 Cart 목록 응답을 거쳐 화면 타입까지 도달하게 했다.
2. **2교시 — `some` 학습과 실제 적용:** 일반 JavaScript 설명으로 “조건에 맞는 원소가 하나라도 있으면 true”라는 `some`의 역할을 확인했다. 실제 Cart에서는 선택 품목 중 quantity가 0인 항목이 하나라도 있는지 검사해 주문 요청을 중단했다.
3. **2교시 — Cart 화면 보강:** 공용 API 오류 함수와 `errorMessage` Alert를 추가하고, 목록에 재고·수량·단가·품목 금액을 나누어 표시했다. 기존 전체/개별 선택과 `price * quantity` 합계는 유지했으며, 성공 주문 뒤 선택 품목을 제거하고 총액을 0으로 만들었다.
4. **2교시 — 서버 트랜잭션·오류 연결:** 주문 생성 Service에 transaction을 적용하고, Cart 수량 Service 맨 앞에 null·1 미만 검증을 추가했다. ProductService 전체를 다시 정리하면서 OrderService가 사용할 Product 조회·저장 메서드도 포함했다.
5. **3교시 — Product 상세 즉시 주문:** `ProductDetail`의 `buyNow`는 1 미만과 stock 초과를 먼저 막고, Product id와 quantity 한 건을 Order request body로 만들어 같은 POST API를 호출했다. 로그인하지 않았으면 로그인 화면으로 보내고, 성공 후 상품 목록으로 이동하는 버튼 흐름을 연결했다.
6. **4교시 — 즉시 주문 테스트:** 일반 사용자로 로그인해 상품 상세에서 수량을 넣고 주문한 뒤 재고 변화를 확인했다. 0 미만과 stock 초과 입력은 주문이 동작하지 않아야 한다는 시나리오를 두었다.
7. **5교시 — 주문 목록 화면 시작:** 메뉴와 route를 확인하고 `OrderList.tsx`를 만들었다. Spring에는 주문 한 건과 내부 상품 목록을 담는 `OrderDetailDto`를 만들고, 사용자와 관리자의 PENDING 주문 조회 Repository 메서드를 나눴다.
8. **6교시 — 역할별 조회 왕복:** Service는 ADMIN이면 전체 PENDING 주문, USER면 본인 PENDING 주문을 최신 id 순으로 조회하고 Entity 목록을 DTO 목록으로 변환했다. Controller는 member id와 role parameter를 받고, React `useEffect`는 로그인 user의 id·role로 GET 요청해 loading/error/orders state를 갱신했다.
9. **6교시 — React 주문 type과 초기 결과:** `Order.ts`에 주문자·번호·날짜·상태·주문 품목 배열의 모양을 정의했다. 화면은 이 단계에서 loading/error를 처리하고 주문 개수만 표시했다. 카드별 상세 렌더링과 상태 버튼은 다음 날짜 범위다. **7~8교시는 자습**이었다.

## 대표 artifact

- **`stock` 필드:** Product→`CartItemDto`→React `CartProduct`→Cart 표로 재고를 전달한다.
- **`some` 기반 `hasInvalid`:** 선택된 품목 중 quantity 0이 하나라도 있으면 주문을 막는다.
- **공용 오류 Alert:** 서버 응답 오류와 네트워크 오류를 `errorMessage` state로 화면에 표시한다.
- **`buyNow`:** 상품 상세의 한 품목을 Order request body로 만들어 기존 주문 API를 재사용한다.
- **`OrderDetailDto`와 `Order.ts`:** Entity 관계를 React 목록 한 건과 내부 품목 배열 모양으로 변환한다.
- **역할별 Order 조회:** Repository→Service 변환→Controller→React `useEffect`로 USER/ADMIN 범위를 나눈다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| Cart 표시·검증 | Cart 목록 DTO의 stock·quantity·price·checked | React type/state 저장→재고·수량·단가·금액 표시→선택 합계 계산 | 사용자가 주문 전 재고와 선택 결과를 함께 확인 |
| `some` 검증 | 선택된 Cart 품목 배열 | quantity가 0인 원소가 하나라도 있는지 확인 | 잘못된 품목이 있으면 POST 전에 중단 |
| 상품 상세 주문 | 로그인 user, Product id, 입력 quantity | 1 미만·stock 초과 검사→Order body 한 건 구성→POST | 재고가 차감되는 주문 생성 후 상품 목록 이동 |
| 주문 목록 | user id·role | GET→Controller→Service의 역할별 PENDING 조회→Entity를 DTO로 변환 | React orders state와 초기 주문 개수 표시 |

## 일반 배열 메서드와 Cart 기능의 구분

- 일반 설명에서 `some`은 조건을 만족하는 원소의 **존재 여부**를 boolean으로 답한다.
- 실제 Cart에서는 선택된 품목 배열에 quantity 0이 하나라도 있는지를 묻는 데 사용했다.
- `filter`는 선택 품목만 추리거나 주문 후 남길 미선택 품목을 만드는 데, `map`은 주문 DTO 품목 배열이나 화면 목록을 만드는 데 사용했다. `forEach`는 선택 금액 누적에 사용됐다.
- 따라서 `some`이 합계를 계산하거나 품목 배열을 변환한 것은 아니다. 합계는 기존 `forEach`, 선택/잔존 목록은 `filter`, DTO 변환은 `map`의 역할이다.

## 헷갈린 점 / 질문

- **stock과 quantity:** stock은 Product의 현재 재고이고 quantity는 Cart 또는 주문 요청 수량이다. 화면에 둘 다 보인다고 같은 state는 아니다.
- **0만 검사하면 충분한가:** 이날 실제 `some` 조건은 quantity 0을 찾는다. 음수·stock 초과의 최종 방어는 input 조건, 상세 화면 검사, Cart Service와 Order Service 검증에 나뉘어 있다.
- **화면의 주문 성공과 transaction:** React가 행을 지운 것은 화면 결과이고, Service transaction은 주문·재고·Cart 삭제의 서버 변경을 한 단위로 다루기 위한 것이다.
- **Cart 주문과 즉시 주문:** Cart 요청에는 CartProduct id가 있어 주문 뒤 Cart 품목을 지울 수 있고, Product 상세 요청에는 그 값이 없다. 두 요청은 같은 Order API를 쓰지만 출발점과 후처리가 다르다.
- **주문 목록이 오늘 완성됐는가:** 역할별 PENDING 조회와 초기 React 화면까지 구현했다. 주문 카드, 완료·취소 버튼과 서버 상태 변경은 04-20에 이어진다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** stock 전달·표시, Cart 오류 처리와 `some`, 주문 transaction 보강, Product 상세 주문, Order 목록 DTO·역할별 조회·초기 React 화면이다.
- **이전 날짜에서 이어온 것:** 전체/개별 선택과 합계는 04-15, Order Entity·DTO와 주문 생성은 04-16에 처음 구현됐다. 오늘 새 기능처럼 다시 귀속하지 않는다.
- **다음 날짜 이후:** 04-20은 상태 완료/취소와 대표 상품, 04-21~04-22는 검색/페이징이다. Linux·AWS·CI/CD·Passwordless는 후속 과목이다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
