---
title: 장바구니와 주문 흐름은 왜 복잡한가
created: 2026-07-16
updated: 2026-07-16
type: query
tags: [spring-boot, react, frontend, backend, project]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: high
---

# 장바구니와 주문 흐름은 왜 복잡한가

## 질문

쇼핑몰의 Cart와 Order는 상품 배열을 저장하고 주문 버튼을 누르는 기능처럼 보이는데, 실제 FrontEnd_BackEnd 수업에서는 왜 Member·Product·Cart·CartProduct·Order·OrderProduct, 여러 DTO·Repository·Service와 transaction까지 필요했는가?

## 짧은 답

장바구니와 주문은 같은 상품·수량을 다루더라도 **관계, 데이터 모양, 생명주기, 상태 전이, 저장 위치가 다르기 때문**이다. 화면의 `checked`, Cart의 `quantity`, Product의 `stock`, 주문의 상태는 서로 다른 값이다. 주문 한 번은 Order/OrderProduct 저장만이 아니라 재고 차감, 선택 CartProduct 삭제, 후속 목록 조회, 완료 또는 취소와 재고 복원까지 이어지는 여러 저장 작업이다.

## 실제 수업에서 질문이 필요해진 날짜와 확장 날짜

| 날짜 | 복잡성이 드러난 단계 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-14-cart-service|2026-04-14]] | 인증 사용자→Cart 조회/생성→동일 Product 수량 누적→목록 DTO 변환 | `CartService`, `CartController`, `CartProductDto`, `CartItemDto` |
| [[summaries/2026-04-15-cart-list-selection-typescript|2026-04-15]] | 화면 선택과 DB 수량 변경이 다른 state임을 확인 | `checked`, `orderTotalPrice`, `changeQuantity`, PATCH |
| [[summaries/2026-04-16-cart-quantity-stock|2026-04-16]] | Cart 조작을 닫고 별도 Order/OrderProduct를 만든 뒤 여러 저장을 한 주문 처리로 연결 | `Order`, `OrderProduct`, `OrderDto`, `OrderService.createOrder` |
| [[summaries/2026-04-17-cart-total-array-some|2026-04-17]] | stock 전달·quantity 0 선검사·상품 상세 즉시 주문·역할별 목록 시작 | `stock`, `some`, `buyNow`, `OrderDetailDto` |
| [[summaries/2026-04-20-order-list-scenario|2026-04-20]] | PENDING 목록을 완료 또는 취소하고, 취소 시 재고를 복원 | `OrderList`, `updateOrderStatus`, `cancelOrder`, transaction |

## 근거 artifact와 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| Cart 추가 | 인증 email + Product id + 요청 quantity | Member/Product 조회→Cart 조회/생성→동일 CartProduct 탐색 | 기존 quantity 누적 또는 새 CartProduct 저장 |
| Cart 목록 | 인증 사용자 | CartProduct·Product 관계 탐색→`CartItemDto` 변환 | React 표에 상품·가격·quantity·후속 stock 표시 |
| 화면 선택 | checkbox event | React 배열의 `checked`만 변경→선택 금액 계산 | 주문 후보와 화면 합계 변경, DB에는 저장하지 않음 |
| Cart 수량 변경 | CartProduct id + quantity | PATCH→연결 Product stock·최소 수량 검사→CartProduct 저장 | 화면 state와 DB quantity 변경 |
| Cart 선택 주문 | user id·PENDING·선택 품목의 CartProduct/Product id·quantity | filter/map→POST→회원·상품·재고 확인→OrderProduct 생성→stock 차감→CartProduct 삭제→Order 저장 | 주문 관계 생성과 Cart 임시 품목 제거 |
| Product 상세 주문 | Product id + quantity | frontend 선검사→같은 Order API→Service 최종 검증 | CartProduct 없이 Order/OrderProduct와 stock 변경 |
| 주문 완료 | ADMIN UI의 Order id·COMPLETED | PUT→Order 조회·상태 검사·변경 | PENDING 목록에서 빠지고 DB 상태 변경 |
| 주문 취소 | USER/ADMIN UI의 Order id | DELETE→transaction→OrderProduct 순회→stock 복원→Order 삭제 | 주문/주문상품 제거, 재고 증가, 화면 목록 제거 |

## 자세한 설명

### 1. Product 배열이 아니라 관계를 저장한다

Member 한 명의 Cart에는 여러 Product가 들어가고 같은 Product도 회원마다 다른 quantity를 가진다. 그래서 Product 자체에 장바구니 수량을 넣지 않고 `CartProduct`가 Cart·Product를 참조하면서 quantity를 가진다. 주문 후에는 임시 Cart 관계를 그대로 이력으로 쓰지 않고 `Order`와 `OrderProduct`를 별도로 만든다.

이 관계에서 CartProduct와 OrderProduct는 이름이 비슷해도 같은 행의 상태 전이가 아니다. 주문 Service는 선택 품목의 Product·quantity로 **새 OrderProduct**를 만들고, Cart에서 온 경우 기존 CartProduct를 삭제했다. 관계의 주인·FK·cascade는 [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]이 맡는다.

### 2. API마다 데이터 모양이 다르다

장바구니 추가 입력은 `CartProductDto`, 목록 출력은 `CartItemDto`, 주문 생성 입력은 `OrderDto`와 `OrderProductDto`, 주문 목록 출력은 `OrderDetailDto`였다. React의 TypeScript type과 runtime JSON, Java DTO, JPA Entity, DB row도 서로 다른 층이다.

따라서 “Cart 객체 하나를 frontend와 DB가 그대로 공유한다”고 보면 어느 값이 입력이고 출력인지, 어느 값이 화면 전용인지 알 수 없다. 특히 `checked`는 React 화면 선택 상태이며 JPA CartProduct 필드로 저장된 근거가 없다.

### 3. checked·quantity·stock은 서로 다른 질문에 답한다

- `checked`: 이번에 주문 대상으로 선택했는가. React state이며 DB에 저장하지 않았다.
- `quantity`: Cart 또는 주문 품목에 몇 개를 담았는가. CartProduct와 OrderProduct의 업무 데이터다.
- `stock`: Product에 현재 몇 개가 남았는가. 주문 시 차감되고 취소 시 복원된다.

04-17의 `some`은 선택 품목 중 quantity가 0인 원소가 있는지만 검사했다. 합계 계산, stock 초과 검사, backend 최종 검증을 모두 대신하지 않았다.

### 4. 화면 변경과 DB 변경이 동시에 보이지만 주체가 다르다

checkbox 토글과 합계는 React 안에서 끝난다. quantity 변경은 PATCH 성공 뒤 React state와 DB CartProduct가 모두 바뀐다. 주문 성공 뒤 React가 선택 행을 제거한 것은 화면 결과이고, Spring Service가 CartProduct를 삭제하고 Order를 저장한 것은 서버 결과다. 새로고침 전후 정합성을 보려면 두 경계를 모두 추적해야 한다.

### 5. 주문은 여러 저장 작업의 업무 transaction이다

`OrderService.createOrder`는 회원 존재 확인, Product 조회, 재고 검사, OrderProduct 조립, stock 차감, 선택 CartProduct 삭제, Order 저장을 한 흐름에서 수행한다. 04-17에는 transaction을 보강했다. 중간에 예외가 나면 일부만 반영되는 문제를 막아야 하므로 “Repository를 여러 개 호출한다”가 아니라 **한 업무 단위로 일관성을 지켜야 한다**는 점이 복잡성의 핵심이다.

### 6. 주문 생성 뒤에도 생명주기가 계속된다

04-16은 생성, 04-17은 역할별 PENDING 목록, 04-20은 카드·완료·취소였다. 완료는 상태를 COMPLETED로 바꾸지만, 실제 취소 Service는 CANCELED 행을 남기기보다 재고를 복원한 뒤 Order를 삭제했다. 생성·목록·상태 처리·취소를 한 시점으로 합치면 실제 구현이 왜 여러 날짜에 나뉘었는지 사라진다.

## 확인된 구현과 실행 미확정 범위

### 확인된 범위

- 04-14: 인증 사용자 Cart 추가·동일 품목 누적·DTO 목록 응답.
- 04-15~16: checked/합계, quantity PATCH, 재고 보정, Cart 삭제.
- 04-16~17: Order/OrderProduct·요청 DTO·생성 Service/API, 실제 주문 버튼, 즉시 주문, 목록 DTO/API.
- 04-20: 역할별 화면, 완료·취소 API, 취소 transaction과 재고 복원, DB 확인 시나리오.

### 완료로 단정할 수 없는 범위

- 04-14 동일 Cart 품목 누적에서 기존 quantity+새 요청 quantity 전체를 stock과 다시 비교한 코드는 확인되지 않는다.
- OrderProduct에 주문 당시 가격 snapshot 필드는 확인되지 않는다.
- client가 보낸 memberId·role과 JWT principal/authority를 서버가 대조하는 코드는 확인되지 않는다.
- 완료·취소 endpoint의 ADMIN·당사자 서버 인가가 확인되지 않는다.
- 04-16 주문 Service에는 이후 04-17에 transaction이 보강됐다. 04-16 코드만으로 최종 transaction 경계를 소급하지 않는다.

## 잘못된 동일시와 판단 기준

| 잘못된 동일시 | 판단 기준 |
|---|---|
| CartProduct=OrderProduct | 어떤 부모 관계·테이블·생명주기에 속하며 언제 생성·삭제되는가 |
| checked=quantity | 화면 선택값인가, 서버에 저장되는 품목 수량인가 |
| quantity=stock | 주문 희망 수량인가, Product의 가용 재고인가 |
| Cart 삭제=Order 저장 | 사용자의 명시적 Cart DELETE인가, 주문 성공 후 임시 품목 제거인가 |
| React 행 제거=DB transaction 성공 | 서버의 저장·삭제·재고 변경이 모두 성공했고 응답 뒤 화면이 갱신됐는가 |
| 취소=CANCELED 행 보존 | 실제 Service가 상태만 바꾸는가, 재고 복원 뒤 Order를 삭제하는가 |
| role별 버튼=서버 인가 | endpoint가 JWT authority·소유자를 실제 검사하는가 |

## 참고한 위키 페이지

- Summary: [[summaries/2026-04-14-cart-service|04-14]], [[summaries/2026-04-15-cart-list-selection-typescript|04-15]], [[summaries/2026-04-16-cart-quantity-stock|04-16]], [[summaries/2026-04-17-cart-total-array-some|04-17]], [[summaries/2026-04-20-order-list-scenario|04-20]]
- Concept: [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- Comparison: [[comparisons/entity-vs-dto|Entity vs DTO]], [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- Entity: [[entities/react|React]], [[entities/spring-boot|Spring Boot]], [[entities/mysql|MySQL]]

## 후속 과목과 직접 수업의 경계

- 이 질문의 직접 범위는 04-14~04-20의 FrontEnd_BackEnd Cart·Order 구현이다.
- P08과 I01·I02·I04의 관계·JPA 설명은 날짜 MD와 고도화 Summary/Concept에 충분히 전사되어 있어 이 페이지 source에 중복 추가하지 않았다.
- 04-20 후반 대표 상품·Paging은 Product 후속 기능이며 Order 생명주기에 포함하지 않는다.
- Linux·AWS·CI/CD는 실행·배포, Passwordless는 다른 인증 방식, 중간 프로젝트는 실제 적용 설계다. Cart/Order 직접 구현으로 소급하지 않는다.

## 구체적인 raw sources

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`

## 다음에 볼 것

1. [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]에서 CartProduct와 OrderProduct의 FK·owning side·cascade를 복습한다.
2. [[concepts/shopping-cart-flow|장바구니 기능 흐름]]에서 checked·quantity·stock과 Cart API를 날짜순으로 본다.
3. [[concepts/order-flow|주문 기능 흐름]]에서 생성→PENDING 목록→완료·취소·재고 복원 생명주기를 추적한다.
4. [[queries/jwt-role-ui-vs-server-authorization|JWT role UI와 서버 인가는 왜 다른가]]에서 Order의 role UI와 서버 권한 경계를 이어서 본다.
