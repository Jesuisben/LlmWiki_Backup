---
title: 주문 기능 흐름
created: 2026-07-06
updated: 2026-07-16
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# 주문 기능 흐름

## 정의

이 수업의 주문 흐름은 **선택한 Cart 품목 또는 Product 상세의 한 품목을 Order 요청으로 만들고, `Order`·`OrderProduct`로 저장하면서 재고와 Cart를 처리한 뒤, 역할별 PENDING 목록에서 완료·취소를 수행하는 과정**이다. 장바구니의 checked·수량·삭제 자체는 [[concepts/shopping-cart-flow|장바구니 기능 흐름]]이 맡고, 이 페이지는 주문 생성 이후의 생명주기에 집중한다.

## 왜 중요한가

Order는 화면의 POST 한 번으로 끝나지 않는다. 회원·상품·재고를 검증하고 여러 OrderProduct를 구성하며, Cart 주문이면 임시 CartProduct를 지우고 Product stock을 차감한다. 이후 USER와 ADMIN의 조회 범위·버튼이 달라지고, 완료는 상태를 바꾸지만 취소는 실제 구현에서 재고를 복원한 뒤 주문을 삭제했다. 생성·목록·상태 처리 날짜를 나눠야 이 차이가 보인다.

## 처음 등장과 이후 확장 날짜

| 날짜 | 실제 구현 단계 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-16-cart-quantity-stock|2026-04-16]] | OrderStatus·Entity·요청 DTO·Repository를 만들고 선택 Cart 품목 주문 API/Service까지 구현 | `OrderStatus`, `Order`, `OrderProduct`, `OrderDto`, `OrderProductDto`, `OrderService.createOrder`, `OrderController` |
| [[summaries/2026-04-17-cart-total-array-some|2026-04-17]] | Cart 선택 주문 버튼 연결, Product 상세 즉시 주문, transaction 보강, 역할별 PENDING 목록 DTO/API와 초기 React fetch | `onClick={makeOrder}`, `buyNow`, `OrderDetailDto`, 역할별 Repository query, `OrderList` |
| [[summaries/2026-04-20-order-list-scenario|2026-04-20]] | 주문 카드·역할별 버튼, 완료 PUT, 취소 DELETE와 재고 복원 | `changeCompleted`, `cancelOrder`, `updateOrderStatus`, OrderList card |

04-20은 Order Entity와 생성 API를 새로 만든 날이 아니다. 그것들은 04-16에 만들어졌고, 04-17에는 목록 조회를 시작했으며, 04-20에 목록 렌더링과 상태 처리를 완성했다.

## 두 주문 진입점

| 진입점 | 요청 품목 | CartProduct id | 주문 성공 뒤 Cart 처리 |
|---|---|---|---|
| Cart 선택 주문 | `checked`인 품목을 `filter`하고 DTO로 `map` | 있음 | Service가 해당 CartProduct를 삭제하고 React도 주문한 행·합계를 제거 |
| Product 상세 즉시 주문 | 현재 Product id와 입력 quantity 한 건 | 없음 | 삭제할 Cart 품목이 없고, 성공 후 상품 목록으로 이동 |

두 요청은 같은 Order POST API를 재사용하지만 출발점과 후처리가 다르다. Product 상세 주문을 “Cart에 잠시 넣었다가 주문한다”고 설명할 근거는 없다.

선택 주문의 함수·Entity·Service·Controller는 04-16에 작성됐지만, 같은 날 주문 버튼 조각은 삭제 버튼을 반복한 복붙 상태였다. 실제 `onClick={makeOrder}` 연결은 04-17에 확인된다. “생성 API가 존재한 날짜”와 “화면 버튼이 그 API를 호출한 날짜”를 같은 날로 합치지 않는다.

## Order와 OrderProduct 구성

- `Order`는 Member, OrderProduct 목록, 주문 날짜, 주문 상태를 가졌다.
- `OrderProduct`는 Order와 Product를 참조하고 quantity를 가졌다.
- `OrderProductDto`는 CartProduct id·Product id·quantity를, `OrderDto`는 Member id·상태·주문 품목 목록을 전달했다.
- 04-17의 `OrderDetailDto`는 주문 id·주문자 이름·날짜·상태와 내부 상품명/수량 목록을 출력했고, React `Order.ts`는 이 목록 응답의 화면 type을 표현했다. 생성 입력 DTO와 목록 출력 DTO/type을 같은 모양으로 합치지 않는다.
- 이날 `OrderProduct`에는 별도 주문 가격 snapshot 필드가 확인되지 않는다. Product 참조와 quantity만으로 주문 당시 가격 보존까지 구현됐다고 만들지 않는다.
- cascade와 orphan removal은 Order–OrderProduct JPA 생명주기 설정이다. DB FK의 `ON DELETE`와 같은 계층으로 설명하지 않는다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| Cart 선택 주문 | user id, PENDING, 선택 품목의 CartProduct id·Product id·quantity | React filter/map→POST→회원/상품/재고 검증→OrderProduct 생성→stock 차감→CartProduct 삭제→Order 저장 | 주문·주문상품 저장, Cart 행 제거 |
| Product 상세 즉시 주문 | 로그인 user, Product id, quantity | 1 미만·stock 초과 frontend 검사→한 품목 Order body→같은 POST→Service 최종 검증 | 주문 생성과 stock 차감, 상품 목록 이동 |
| 역할별 목록 | user id·role | ADMIN은 전체 PENDING, USER는 본인 PENDING을 최신 id 순 조회→`OrderDetailDto` 변환 | React `orders` state; 이후 카드 렌더링 |
| 완료 | ADMIN의 Order id·COMPLETED | PUT→Order 조회→CANCELED 여부 검사→상태 변경→React `filter` | PENDING 목록에서 제거되고 DB 상태 COMPLETED |
| 취소 | USER 또는 ADMIN의 Order id | DELETE→transaction Service→OrderProduct 순회→각 quantity만큼 Product stock 복원→Order 삭제→React `filter` | 주문/주문상품 제거와 재고 증가 |

## 역할별 화면과 실제 API 조건

| 역할 | 조회 범위 | 화면 버튼 | 실제 연결 시점 |
|---|---|---|---|
| USER | 본인의 PENDING 주문 | 취소 | 04-17 조회 API/초기 fetch, 04-20 취소 DELETE 연결 |
| ADMIN | 모든 사용자의 PENDING 주문과 주문자 이름 | 완료·취소 | 04-17 조회 API/초기 fetch, 04-20 완료 PUT·취소 DELETE 연결 |

04-20 1교시에는 버튼 UI가 먼저 등장했고 2~4교시에 handler와 Spring API가 연결됐다. 버튼이 보이는 것과 요청이 실제 실행되는 것은 같은 시점이 아니다. role 기반 화면 조건만으로 서버 인가가 완성됐다고도 단정하지 않는다.

원본의 역할별 목록 요청은 React가 `memberId`와 `role`을 query parameter로 보내고 Service가 그 role로 분기한다. 생성 POST도 Controller가 인증 객체가 아니라 body의 `memberId`를 사용했다. 완료·취소 Controller/Service에도 ADMIN·당사자 여부를 다시 검사하는 코드가 확인되지 않으므로, 역할별 UI/API 시나리오와 서버 인가 완성을 구분한다.

## 상태와 취소의 실제 구현

- 주문 생성 body와 enum에는 PENDING·COMPLETED·CANCELED가 등장한다.
- 역할별 목록 조회는 PENDING만 가져왔다.
- 완료는 기존 Order의 상태를 COMPLETED로 바꾸었다.
- 취소 설명에는 CANCELED 전환 표현도 있지만 실제 Service는 Product stock을 복원한 뒤 Order를 삭제했다. 따라서 취소 주문이 CANCELED 행으로 DB에 남는다고 설명하지 않는다.
- Repository에는 JPQL update 예제가 추가됐지만 Service 본문은 Order를 조회해 상태를 설정했다. 두 방식이 한 호출에서 모두 실행됐다고 합치지 않는다.

## 실제 수업 예시: 취소 시 재고 복원

04-20 취소 Service는 transaction 안에서 Order와 연결 OrderProduct를 읽었다. 각 품목의 Product stock에 주문 quantity를 더해 저장한 다음 Order를 삭제했다. React는 DELETE 성공 뒤 해당 Order를 `orders` 배열에서 제거했다. 화면 제거, DB 주문 삭제, Product 재고 복원은 한 취소 use case의 서로 다른 결과다.

## 자주 헷갈리는 원인

- **04-16과 04-20의 역할:** Entity·생성 API는 04-16, 목록 조회 시작은 04-17, 카드·완료·취소 UI/API는 04-20이다.
- **CartProduct와 OrderProduct:** CartProduct는 주문 전 수정·삭제 가능한 임시 품목이고, 주문 시 새 OrderProduct가 만들어진다. 같은 Entity를 상태만 바꾼 것이 아니다.
- **frontend 선검사와 Service 검증:** Cart 선택 주문의 `some`은 quantity 0 존재만 검사하고, Product 상세 즉시 주문은 최소 수량·stock 초과를 검사했다. 둘 다 OrderService의 회원·Product·재고 검증을 대신하지 않는다.
- **완료와 취소:** 완료는 상태 변경, 실제 취소 구현은 재고 복원 뒤 주문 삭제다.
- **버튼 표시와 인가:** USER/ADMIN별 렌더링은 UI 조건이며 보호 API의 서버 권한 검사를 모두 증명하지 않는다.
- **주문 가격 snapshot:** 원본 Entity에 확인되지 않은 가격 필드를 만들어 설명하지 않는다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/product-domain-flow|상품 도메인 기능 흐름]]의 Product/stock과 [[concepts/shopping-cart-flow|장바구니 기능 흐름]]의 선택 품목·quantity가 주문 입력이 된다.
- 관계: [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]과 [[comparisons/entity-vs-dto|Entity vs DTO]]에서 Order/OrderProduct와 요청·목록 DTO를 구분한다.
- API·계층: [[concepts/spring-boot-rest-api|Spring Boot REST API]]와 [[comparisons/controller-service-repository|Controller vs Service vs Repository]]가 POST/GET/PUT/DELETE의 backend 경계를 설명한다.
- JPQL/SQL: [[comparisons/jpql-vs-sql|JPQL vs SQL]]은 Entity update 예제와 MySQL 검증 SQL을 같은 언어로 보지 않게 한다.
- 종합 질문: [[queries/why-shopping-cart-order-flow-is-complex|장바구니와 주문 흐름은 왜 복잡한가]]에서 관계·DTO·선택·수량·재고·상태를 한 흐름으로 다시 연결한다.

## 직접 수업·교안·후속 확장 경계

- **직접 수업:** 04-16 주문 모델·생성 함수/API, 04-17 Cart 주문 버튼 연결·즉시 주문·PENDING 목록, 04-20 역할별 카드·완료·취소·재고 복원이다.
- **교안 보충:** P03의 REST/status와 P08의 JPA/cascade 내용은 날짜 MD와 Summary에 충분히 전사되어 있어 별도 source로 추가하지 않았다.
- **R19 범위:** 총정리 원본은 04-15 Cart 삭제에서 끝나므로 Order Entity·생성·목록·상태·재고 복원의 source가 아니다. R19는 “과목 허브의 끝 경계” 확인에만 사용했다.
- **후속 기능/과목:** 같은 04-20 후반의 대표 상품·Paging은 Product 다음 기능이며 Order 책임이 아니다. Linux·AWS·CI/CD는 실행·배포, Passwordless는 다른 인증, 중간 프로젝트는 적용 단계다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md` — 04-15 Cart 삭제에서 끝나는 경계 확인용
