---
title: JPA 연관관계 매핑
created: 2026-07-06
updated: 2026-07-16
type: concept
tags: [spring, spring-boot, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
status: growing
confidence: high
---

# JPA 연관관계 매핑

## 정의

JPA 연관관계 매핑은 Java Entity의 객체 참조를 DB 외래키(FK) 관계와 연결하는 방법이다. 이 수업에서는 Cart와 Product를 곧바로 다대다로 묶지 않고, `quantity`를 가진 `CartProduct` 관계 Entity를 사이에 두면서 직접 시작됐다. 이후 04-16에는 주문과 장바구니의 생명주기를 분리하기 위해 `Order`·`OrderProduct` 관계로 확장됐다.

## 왜 중요한가

03-30의 Fruit, 04-02의 Member, 04-08의 Product는 먼저 한 Entity의 필드·식별자·Repository를 익히는 단계였다. 그러나 장바구니부터는 “누구의 Cart인가”, “어느 Cart에 어떤 Product가 몇 개 들어 있는가”를 여러 Entity 사이의 FK와 객체 참조로 함께 표현해야 했다. 관계의 주인(owning side)을 잘못 이해하면 Java 컬렉션만 바꾸고 FK는 갱신되지 않거나, `mappedBy`가 가리키는 필드와 실제 FK 위치를 혼동하기 쉽다.

## 이 수업에서의 등장과 확장

| 날짜 | 관계 학습의 위치 | 대표 artifact |
|---|---|---|
| 03-30~04-08 | Fruit→Member→Product 단일 Entity와 JPA 저장을 익힌 선행 배경 | `Fruit`, `Member`, `Product` |
| 04-13 | Cart 관계의 직접 시작. Member–Cart, Cart–CartProduct, CartProduct–Product를 Entity 코드로 작성 | `Cart`, `CartProduct`, `CartProductDto`, 두 Repository |
| 04-14 | 관계를 실제 추가·목록 use case에서 탐색하고 저장·DTO 변환 | `CartService`, `CartItemDto` |
| 04-16 | 임시 Cart 품목과 주문 이력을 분리하고 Order 관계를 새로 구성 | `Order`, `OrderProduct`, `OrderDto`, `OrderProductDto`, `OrderService` |

[[summaries/2026-04-13-product-detail-useeffect-service|04-13]] 이전의 단일 Entity 단계는 관계 매핑의 선행 배경일 뿐이다. 이 페이지의 직접 중심은 04-13 Cart 설계부터다.

## 관계의 주인, FK, 반대편 연결

관계의 주인은 DB FK 값을 관리하는 Entity 쪽이다. 수업 코드에서는 그쪽에 `@JoinColumn`이 있고, 반대편 컬렉션은 `mappedBy`로 주인 Entity의 Java 필드명을 가리킨다.

| 관계 | 수업 코드의 방향 | owning side와 FK | 반대편·미확정 경계 |
|---|---|---|---|
| Member–Cart | `Cart.member`에 `@OneToOne` | **Cart**가 주인, `carts.member_id` | Member 쪽 반대편 필드는 원본에서 확인되지 않는다. |
| Cart–CartProduct | `CartProduct.cart`에 `@ManyToOne` | **CartProduct**가 주인, `cart_products.cart_id` | `Cart.cartProducts`는 `mappedBy = "cart"`인 반대편 컬렉션이다. |
| CartProduct–Product | `CartProduct.product`에 `@ManyToOne` | **CartProduct**가 주인, `cart_products.product_id` | Product 쪽 반대편 컬렉션은 원본에서 확인되지 않는다. |
| Order–Member | `Order.member`에 `@ManyToOne` | **Order**가 주인, `orders.member_id` | Member 쪽 반대편 주문 컬렉션은 원본에서 확인되지 않는다. |
| Order–OrderProduct | `OrderProduct.order`에 `@ManyToOne` | **OrderProduct**가 주인, `order_products.order_id` | `Order.orderProducts`는 `mappedBy = "order"`인 반대편 컬렉션이다. |
| OrderProduct–Product | `OrderProduct.product`에 `@ManyToOne` | **OrderProduct**가 주인, `order_products.product_id` | Product 쪽 반대편 주문 품목 컬렉션은 원본에서 확인되지 않는다. |

여기서 `mappedBy = "cart"`와 `mappedBy = "order"`는 DB 컬럼명이 아니라 각각 `CartProduct.cart`, `OrderProduct.order`라는 **Java 필드명**이다. 반대로 `@JoinColumn(name = "cart_id")`와 같은 값은 FK 컬럼명을 지정한다.

04-13 코드와 R19의 04-15까지 복습 구간은 Cart 관계의 annotation·FK 위치가 일치한다. 이미지 I01은 회원의 Cart와 품목별 수량을 설명하는 비유, I02는 Cart→CartProduct→Product 분리 구조, I04는 Member 1:1 Cart·Cart 1:N CartProduct·CartProduct N:1 Product와 품목별 quantity를 보여 준다. 세 이미지에는 `mappedBy`나 실제 FK 컬럼명이 적혀 있지 않으므로, owning side와 컬럼명은 이미지가 아니라 04-13 Entity 코드로 확정한다.

## 04-13: Product 상세에서 Cart 관계로 전환

Cart는 Member를 참조하고 CartProduct 목록을 가진다. CartProduct는 Cart와 Product를 각각 참조하면서 `quantity`를 보유한다. 같은 Product라도 회원의 Cart마다 담은 수량이 다르기 때문에, 수량은 Product 자체가 아니라 두 대상을 연결하는 관계 Entity에 놓였다. 이 구조는 Cart–Product의 다대다 의미를 두 개의 다대일 관계로 풀어낸 것이다.

이날 준비된 범위는 다음과 같이 나뉜다.

- **관계 모델:** `Cart`, `CartProduct`, `mappedBy`, FK를 가진 `cart`·`product`, `quantity`를 작성했다.
- **저장 기반:** `CartRepository.findByMember`, `CartProductRepository`, Member/Product id 조회 메서드를 준비했다.
- **요청 준비:** Product 상세 화면이 product id와 quantity를 `/cart/insert`로 보낼 수 있게 했고 `CartProductDto`를 만들었다.
- **아직 미완성:** 인증 사용자 Cart를 조회·생성하고 중복 품목을 누적하는 Service/Controller 저장과 목록 DTO 응답은 다음 날 구현했다.

## 04-14: 관계를 실제로 사용한 Cart Service

[[summaries/2026-04-14-cart-service|04-14]]의 장바구니 추가는 Entity 관계를 실제 객체 탐색과 FK 저장에 사용했다.

| 입력 | 처리 | 결과 |
|---|---|---|
| 인증 객체의 email + `CartProductDto`의 product id·quantity | email→Member 조회→Member의 Cart 조회 또는 생성→Product 조회→Cart의 기존 CartProduct 중 같은 Product 탐색 | 기존 품목이면 quantity 누적, 없으면 Cart·Product·quantity를 연결한 새 CartProduct 저장 |
| 인증 사용자 목록 요청 | email→Member→Cart→CartProduct 목록→각 CartProduct의 Product 참조 사용 | `CartItemDto` 목록으로 변환해 id·상품 정보·가격·quantity를 React에 응답 |

기존 품목을 찾을 때 Service는 `cart.getCartProducts()`를 순회해 각 `CartProduct.product.id`를 비교했다. 새 품목은 `setCart(cart)`, `setProduct(product)`, `setQuantity(...)` 뒤 CartProduct Repository를 통해 저장했다. 즉 Cart의 반대편 컬렉션은 관계를 탐색하는 데 쓰였고, 실제 FK를 가진 CartProduct를 설정·저장하는 것이 관계 생성의 핵심이었다.

## 04-16: CartProduct와 별개인 OrderProduct

[[summaries/2026-04-16-cart-quantity-stock|04-16]]에는 주문 전 임시 상태와 주문 생성 뒤 상태를 분리하기 위해 `Order`와 `OrderProduct`를 새 Entity로 만들었다. `Order`는 Member·주문 날짜·상태·OrderProduct 목록을 가지고, `OrderProduct`는 Order·Product·quantity를 가진다.

`OrderDto`는 주문자·상태·품목 목록을 받고, 각 `OrderProductDto`는 CartProduct id·Product id·quantity를 전달했다. Service는 Member를 확인해 Order를 만들고, 품목마다 Product와 재고를 확인한 뒤 **새 OrderProduct**에 Order·Product·quantity를 설정했다. 완성한 목록을 Order에 넣고 Order Repository에 저장했으며, Cart에서 온 품목이면 해당 CartProduct를 후속 삭제했다.

따라서 CartProduct를 OrderProduct로 바꾸어 같은 행을 저장한 것이 아니다. 둘은 같은 Product와 quantity를 사용하더라도 서로 다른 테이블·FK·생명주기를 가진 Entity다.

## CartProduct와 OrderProduct 비교

| 항목 | CartProduct | OrderProduct |
|---|---|---|
| 관계 | Cart–Product 사이 관계 Entity | Order–Product 사이 주문 품목 Entity |
| 시점 | 주문 전 | 주문 생성 뒤 |
| quantity | 사용자가 변경·삭제할 수 있는 장바구니 수량 | 생성된 주문에 포함된 품목 수량 |
| 수명 | Cart에서 수정·삭제되며 주문 전 상태를 표현 | Order의 품목으로 조립되어 주문 관계를 표현 |
| 04-16 전환 | 선택 품목의 Product·quantity를 주문 DTO로 전달 | 그 값으로 새 OrderProduct를 생성 |
| 가격 경계 | 목록 DTO는 연결 Product의 현재 price를 읽음 | 별도 주문 당시 가격 snapshot 필드는 원본 Entity에서 확인되지 않음 |

가격 snapshot을 구현했다고 단정하지 않는다. 04-16의 OrderProduct 원본 필드는 Order, Product, quantity이며, 주문 시점 가격을 별도 보존하는 필드는 확인되지 않는다.

## cascade·orphanRemoval과 DB ON DELETE의 경계

| 설정 | 이 수업에서 확인한 위치 | 동작 계층과 의미 |
|---|---|---|
| `cascade = CascadeType.ALL` | `Cart.cartProducts`, `Order.orderProducts` | JPA가 부모 Entity에 수행한 영속성 작업을 연결 자식 Entity로 전이하는 설정 |
| `orphanRemoval = true` | `Order.orderProducts`에만 확인 | Order 컬렉션과의 연결이 끊어진 OrderProduct를 고아 Entity로 보고 제거하는 관계 생명주기 설정 |
| DB `ON DELETE CASCADE` | Oracle 직접 수업의 FK DDL | DB 엔진이 부모 행 삭제 시 자식 행을 삭제하는 FK 규칙 |

세 설정은 결과가 비슷해 보일 수 있지만 동일 기능이 아니다. JPA cascade와 orphan removal의 주체는 EntityManager/JPA이고, DB `ON DELETE`의 주체는 DB 엔진과 FK 제약조건이다. 이 페이지에서는 04-13 Cart와 04-16 Order 코드에 실제 적힌 JPA 설정만 설명한다. Oracle의 삭제 업무 규칙은 [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]에서 별도로 비교한다.

또한 Cart에는 `cascade = ALL`이 있지만 `orphanRemoval = true`는 원본에서 확인되지 않는다. Order Service는 양쪽 객체 참조를 조립한 뒤 Order를 저장하므로 cascade가 OrderProduct 저장에 관여한다. 반면 04-14의 새 CartProduct는 Cart 저장에만 기대지 않고 CartProduct Service/Repository로 직접 저장했다. annotation 존재만 보고 모든 Service 저장·삭제가 자동이었다고 일반화하면 안 된다.

## 자주 헷갈리는 원인

- **일대다의 `One` 쪽이 항상 주인이라고 생각함:** 주인은 개수 이름이 아니라 FK를 관리하는 쪽으로 판단한다. 이 수업의 두 1:N 관계는 모두 `Many` 쪽 관계 Entity가 FK를 가진다.
- **`mappedBy`를 FK 컬럼명으로 읽음:** 값은 반대편 Entity의 Java 필드명이다. 실제 컬럼은 주인 쪽 `@JoinColumn`에서 확인한다.
- **Java 컬렉션과 DB 관계를 같은 것으로 봄:** `Cart.cartProducts`나 `Order.orderProducts`는 반대편 탐색 경로다. FK를 가진 CartProduct/OrderProduct의 참조 설정도 함께 봐야 한다.
- **CartProduct와 OrderProduct를 같은 품목으로 봄:** 전자는 주문 전 수정 가능한 Cart 관계이고 후자는 주문 생성 시 새로 조립한 Order 관계다.
- **cascade를 DB 삭제 옵션으로 봄:** JPA 영속성 전이와 DB FK 삭제 규칙은 설정 위치·동작 주체·실행 계층이 다르다.
- **가격도 주문 품목에 보존됐다고 추정함:** 현재 원본에는 가격 snapshot 필드가 없다.

## 이전 개념과 이후 기능 연결

- 선행 원리: [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]], [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]], [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]에서 테이블 분리와 FK를 먼저 배웠다. Oracle 직접 수업의 DB 설계와 4과목 MySQL/JPA 적용을 같은 실습으로 섞지 않는다.
- 계층 사이 데이터 모양: [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]가 DTO/Entity 변환 책임을 맡고, 이 페이지는 Entity 관계와 FK 주인을 맡는다.
- DB 접근: [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]가 Repository 선언·호출을 맡고, 이 페이지는 관계를 따라 어떤 Entity를 조회·저장하는지에만 집중한다.
- 업무 흐름: [[concepts/shopping-cart-flow|장바구니 기능 흐름]]과 [[concepts/order-flow|주문 기능 흐름]]이 선택·수량·상태·재고를 설명한다. 이 페이지는 그 기능을 가능하게 한 관계 구조와 생명주기 경계를 설명한다.
- 전체 계층: [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]는 React→Spring→DB 전체 요청·응답 경계를 맡는다.

## 직접 수업·교안·후속 과목 경계

- **직접 수업:** 04-13 Cart/CartProduct 관계와 상세 요청 준비, 04-14 관계를 사용한 추가·목록 DTO 변환, 04-16 Order/OrderProduct 관계와 주문 생성 Service다.
- **교안 보충:** P08의 cascade·orphan removal 내용은 R11·R14 날짜 MD에 필요한 페이지와 설명이 전사되어 있어 PDF 자체를 별도 source로 추가하지 않았다.
- **이미지 보충:** I01·I02·I04는 Cart 구조와 quantity 이해에 실제 사용했다. I03은 React Router 설명 그림이라 JPA 관계 근거에서 제외했다.
- **R19 범위:** R19는 실제로 04-15 Cart 삭제에서 끝난다. Cart 관계 복습에는 사용하지만 04-16 Order·OrderProduct·주문 생성의 근거로 소급하지 않는다. Order 관계의 직접 근거는 R14와 04-16 Summary다.
- **후속 경계:** 04-17~04-20의 주문 목록·상태·재고 복원, 04-21~04-22의 검색은 후속 기능이다. Linux·AWS·CI/CD·Passwordless·중간 프로젝트는 운영·배포·다른 인증 적용 단계이며 이 관계를 직접 만든 수업이 아니다.

## 신규 페이지 후보 판단

`CartProduct vs OrderProduct`는 관계 Entity의 생명주기 비교로, `JPA cascade vs DB ON DELETE`는 Entity 생명주기와 DB FK 규칙의 계층 비교로 이 페이지 안에서 충분히 설명할 수 있다. 기존 Cart·Order concept와 Oracle comparison으로 세부 업무 흐름을 위임할 수 있으므로 이번 세션에는 독립 comparison/concept를 만들지 않았다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md` — Fruit와 JPA 환경의 선행 배경
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md` — Member 단일 Entity 선행 배경
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md` — Product 단일 Entity 선행 배경
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md` — 04-15 Cart 삭제까지의 보조 복습 범위
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
