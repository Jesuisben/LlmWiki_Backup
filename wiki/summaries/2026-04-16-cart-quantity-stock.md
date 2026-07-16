---
title: 2026-04-16 장바구니 수량 변경과 주문 Entity
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
status: growing
confidence: high
---

# 2026-04-16 장바구니 수량 변경과 주문 Entity

## 한 줄 요약

CartProduct에서 연결 Product의 재고를 검사하도록 수량 변경 경로를 보정하고 React 삭제를 완성한 뒤, Order/OrderProduct·DTO·Repository·Service·Controller를 순서대로 만들어 선택 Cart 품목의 주문 저장까지 구현한 날이다.

## 이전 수업과 오늘의 위치

- 전날 [[summaries/2026-04-15-cart-list-selection-typescript|2026-04-15]]에는 선택·합계와 수량 PATCH를 연결했지만, 재고 조회를 위해 Product id를 별도 parameter로 보내는 중간 구현과 React 삭제 함수 미완성 지점이 남았다.
- 오늘 오전 첫 교시에는 그 Cart 기능을 정리하고, 이어서 장바구니와 수명이 다른 주문 도메인으로 전환했다.
- 다음 [[summaries/2026-04-17-cart-total-array-some|2026-04-17]]에는 stock을 응답·화면에 추가하고 `some` 검증과 공통 오류 표시를 붙이며, 상품 상세 즉시 주문과 주문 목록 조회를 시작한다.

## 왜 이 흐름으로 배웠는가

수량을 바꿀 때 CartProduct가 이미 Product를 참조하므로 클라이언트가 Product id를 다시 보내지 않아도 재고를 확인할 수 있다. 이 보정으로 Cart 조작을 닫은 뒤, 임시 품목인 CartProduct를 그대로 주문 이력으로 쓰지 않고 Order와 OrderProduct를 별도 Entity로 만드는 이유를 관계·영속성 전이와 함께 배웠다.

## 실제 교시 흐름

1. **1교시 — Cart 수량 변경 보정:** Service는 먼저 CartProduct id로 품목을 조회하고, 그 객체의 연결 Product에서 stock을 읽어 요청 quantity와 비교했다. Controller의 수량 변경 매개변수도 CartProduct id와 quantity 중심으로 정리했다.
2. **1교시 — React 삭제 완성:** `deleteCartProduct`가 confirm 후 DELETE 요청을 보내고, 성공하면 해당 id를 제외하도록 배열을 filter하고 응답을 알렸다. 이로써 전날 만든 백엔드 삭제 API와 화면 버튼이 실제 왕복으로 연결됐다.
3. **1교시 후반 — Order 시작:** 정규화 복습을 안내한 뒤 `OrderStatus`에 PENDING·COMPLETED·CANCELED를 정의했다. 이 시점부터 장바구니 삭제와 별개로 주문 상태를 관리하는 모델을 시작했다.
4. **2교시 — cascade와 orphan removal:** Order 상태 변경을 연결 OrderProduct에 전파하는 영속성 전이와 부모 관계에서 끊어진 자식 제거를 교안 범위로 살펴봤다. DB `ON DELETE CASCADE`와 유사하다고 메모했지만 동일 기능으로 구현한 것은 아니다.
5. **3교시 — Entity와 요청 DTO:** `Order`는 Member, OrderProduct 목록, 주문 날짜, 상태를 가졌고 `OrderProduct`는 Order와 Product, quantity를 가졌다. `OrderProductDto`는 CartProduct id·Product id·quantity를, `OrderDto`는 Member id·상태·주문 품목 목록을 전달하도록 만들었다. 애플리케이션 재실행 후 orders와 order_products 관련 테이블·시퀀스 생성을 확인하도록 했다.
6. **4교시 — CartList 주문 요청:** 선택된 품목만 filter하고, 선택이 없으면 중단했다. 선택 품목을 DTO 필드명에 맞춰 map한 request body를 POST하고 성공하면 주문한 품목을 화면 Cart 배열에서 제거하고 총액을 0으로 만들었다.
7. **4교시 — `OrderRepository`:** Order Entity를 저장할 JPA Repository를 만들었다.
8. **5교시 — `OrderService.createOrder`:** Member를 확인하고 Order 기본값을 채운 뒤 각 요청 품목의 Product와 재고를 검사했다. OrderProduct를 만들고, Product stock에서 주문 수량을 차감하고, Cart에서 온 품목이면 해당 CartProduct를 삭제했다. 목록을 Order에 넣은 뒤 Order를 저장했다.
9. **5교시 — `OrderController`:** POST request body를 Service에 넘기고 저장된 Order id를 이용한 완료 메시지를 응답했다. **6~8교시는 자습**이었다.

## 대표 artifact

- **수정된 `CartProductService`:** CartProduct 조회→연결 Product stock 확인→quantity 덮어쓰기→Repository 저장 순서를 담당한다.
- **`deleteCartProduct`:** confirm→DELETE→React 배열 filter로 서버와 화면의 삭제를 연결한다.
- **`OrderStatus`·`Order`·`OrderProduct`:** 주문의 상태와 한 주문에 포함된 여러 상품을 표현한다.
- **`OrderDto`·`OrderProductDto`:** React가 보낸 선택 품목을 주문 생성 Service로 전달한다.
- **`OrderService.createOrder`:** 회원·상품·재고 검증, 주문 상품 생성, 재고 차감, Cart 품목 삭제, Order 저장을 한 주문 처리 안에서 수행한다.
- **`OrderController`:** 주문 POST 요청을 받고 저장 결과를 HTTP 응답으로 바꾼다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| Cart 수량 변경 | React number input→CartProduct id·quantity PATCH | Controller→Service→CartProduct 조회→연결 Product stock 검증→quantity 저장 | 성공 응답 뒤 React quantity·합계 갱신, DB CartProduct 수량 변경 |
| Cart 품목 삭제 | 삭제 버튼의 CartProduct id | confirm→DELETE→Controller→Service→Repository 삭제 | 성공한 품목을 React 배열에서도 제거 |
| 장바구니 주문 | 로그인 user id, 상태, 선택 품목의 CartProduct id·Product id·quantity | 선택 filter/map→POST→Controller→Service의 회원·상품·재고 검증→OrderProduct 구성→재고 차감·Cart 품목 삭제→Order 저장 | 주문/주문상품 저장, 성공 메시지, 주문한 Cart 행과 합계 제거 |

## Cart에서 Order로 바뀐 데이터의 의미

- CartProduct는 주문 전 사용자가 수량을 바꾸거나 삭제할 수 있는 임시 품목이다.
- OrderProduct는 Order에 포함된 주문 상품이다. 오늘 구현은 Cart에서 받은 Product와 quantity로 새 OrderProduct를 만들고, CartProduct 자체는 삭제했다.
- `cascade = ALL`과 `orphanRemoval = true`는 Order–OrderProduct Entity 생명주기 설정이다. Oracle에서 배운 DB FK의 `ON DELETE` 규칙과 비슷한 결과가 있을 수 있어도 적용 계층과 동작 주체는 다르다.

## 헷갈린 점 / 질문

- **Product id를 왜 수량 PATCH에서 없앴는가:** CartProduct를 먼저 찾으면 연결된 Product를 통해 stock을 읽을 수 있다. 클라이언트가 보낸 별도 Product id와 CartProduct의 실제 Product가 어긋날 여지를 줄인다.
- **화면 갱신과 DB 저장:** React는 PATCH 성공 뒤 local state를 바꾸고, Spring은 Repository에 CartProduct를 저장한다. 한쪽만 바뀌면 새로고침 전후 결과가 달라질 수 있다.
- **삭제와 주문이 같은 날 직접 구현됐는가:** Cart 삭제는 첫 교시 React 함수까지 연결됐다. 주문은 enum·Entity·DTO 작성에 그치지 않고 오후에 POST·Service·Controller와 Order 저장까지 구현됐다.
- **OrderProduct가 가격을 보존하는가:** 이날 Entity에는 Product 참조와 quantity가 있으며 별도 주문 가격 snapshot 필드는 원본에서 확인되지 않는다. 현재 Product 값과 주문 당시 값의 보존 문제를 임의로 보완해 서술하지 않는다.
- **상태 CANCELED와 실제 취소 처리:** enum 값은 오늘 정의했지만 완료·취소 버튼과 상태 변경·재고 복원은 04-20 범위다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** Cart 수량 보정·삭제 완성, OrderStatus, Order/OrderProduct, 요청 DTO, Repository, CartList 주문 요청, 주문 생성 Service와 Controller다.
- **다음 날짜:** 04-17은 Cart stock·오류·`some`, 상품 상세 즉시 주문, 역할별 PENDING 주문 목록 조회를 다룬다. 04-20은 목록 카드·상태 버튼·완료/취소와 재고 복원을 구현한다.
- 검색/페이징은 04-20 후반~04-22이며 Linux·AWS·CI/CD·Passwordless는 후속 과목이다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
