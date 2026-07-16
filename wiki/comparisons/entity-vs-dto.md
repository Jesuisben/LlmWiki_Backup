---
title: Entity vs DTO
created: 2026-07-02
updated: 2026-07-16
type: comparison
tags: [spring-boot, backend, java, react, typescript]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# Entity vs DTO

## 비교 목적

수업에서는 Java class, JPA Entity, 요청 DTO, 응답 DTO, `Map` 응답, React TypeScript type, 실제 JSON, DB row가 모두 비슷한 필드 이름을 가졌다. 이들을 “같은 데이터 객체”로 합치면 어느 모양이 DB 생명주기를 따르고, 어느 모양이 API 경계를 위해 만들어졌으며, 어디에서 변환되는지 놓치게 된다.

이 페이지는 Entity와 DTO의 **선택 기준과 변환 지점**을 비교한다. 계층 전체의 데이터 이동 원리는 [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]], 관계와 FK는 [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]에 맡긴다.

## 실제 수업에서 비교가 필요해진 이력

- **2026-03-30~04-01:** Java `Fruit`와 React `Fruit` type, axios가 받은 runtime JSON이 비슷한 필드를 갖지만 서로 다른 runtime·역할이라는 선행 문제가 생겼다.
- **2026-04-06:** `Member` Entity와 로그인 요청용 `LoginDto`, 로그인 응답을 받는 frontend type이 함께 등장해 Entity/DTO 구분이 처음 명시적으로 필요해졌다.
- **2026-04-10:** Product 등록은 별도 요청 DTO가 아니라 `Product` Entity를 Controller가 직접 받았다. “모든 요청은 DTO”라고 일반화할 수 없는 실제 예다.
- **2026-04-14:** 장바구니 추가 입력 `CartProductDto`와 목록 출력 `CartItemDto`, 내부 `Cart`·`CartProduct` Entity가 분리됐다.
- **2026-04-16~17:** 주문 입력 `OrderDto`·`OrderProductDto`, 저장 `Order`·`OrderProduct`, 목록 출력 `OrderDetailDto`로 생명주기와 외부 노출 모양이 더 분명해졌다.
- **2026-04-21~22:** frontend `SearchCondition`, Java `SearchDto`, `Page<Product>` 응답이 검색 조건과 결과를 서로 다른 모양으로 전달했다.

## 한눈에 보기

| 구분 | 실행 위치·생명주기 | 수업 예 | DB 저장 대상인가 | 외부 요청·응답 역할 |
|---|---|---|---|---|
| JPA Entity | Spring/JPA persistence context와 DB 관계 | `Member`, `Product`, `CartProduct`, `Order` | Repository가 조회·저장 | 날짜에 따라 직접 body/응답에 쓰인 경우도 있음 |
| 요청 DTO | HTTP 입력을 Java use case 입력으로 전달 | `LoginDto`, `CartProductDto`, `OrderDto`, `SearchDto` | DTO 자체는 저장하지 않음 | 필요한 입력 필드 묶음 |
| 응답 DTO | Entity를 외부 응답 모양으로 변환 | `CartItemDto`, `OrderDetailDto` | DTO 자체는 저장하지 않음 | 화면에 필요한 필드와 중첩 구조 제공 |
| `Map` 응답 | Controller가 즉석에서 만든 JSON object 모양 | login·Product 등록 응답 | 저장 대상 아님 | token/user/message/errors 등 응답 body 구성 |
| React TypeScript type/interface | compile-time 검사에 쓰는 frontend 선언 | `Fruit`, `Product`, `CartProduct`, `User`, `SearchCondition` | DB 저장 대상 아님 | state·props·axios data의 예상 모양 |
| runtime JSON | HTTP에서 실제 전송·파싱되는 값 | Fruit/Product/Cart/Order/Page 응답 | 그 자체가 JPA Entity는 아님 | Java object가 직렬화되고 JS object로 파싱된 결과 |
| DB row | MySQL table의 실제 저장 데이터 | member/product/cart/order 관련 행 | DB가 보관 | HTTP 객체나 TypeScript type이 아님 |

## 실제 선택 상황 1 — Fruit: 이름이 같아도 하나가 아니다

### 입력 → 처리 → 결과

1. Spring 쪽 `Fruit`가 응답 대상으로 사용된다.
2. HTTP 응답에서 JSON으로 직렬화된다.
3. axios가 JSON을 JavaScript object로 파싱한다.
4. React의 `Fruit` type은 그 object를 다루기 위한 compile-time 계약으로 쓰이고, state가 실제 값을 보관한다.

Java `Fruit`, JSON, TypeScript `Fruit`, React state는 필드 모양이 비슷해도 같은 메모리 객체가 아니다. TypeScript type은 runtime 응답을 생성하지 않고, React state도 DB row를 직접 보관하는 저장소가 아니다.

## 실제 선택 상황 2 — 로그인과 Product 등록

### 로그인: DTO가 필요한 모양

- `LoginDto`는 email과 password라는 로그인 요청 입력을 받는다.
- 인증 뒤 Controller는 token과 사용자 정보를 포함하는 `Map` 응답을 만든다.
- frontend는 이 JSON을 `User`/로그인 응답 type에 맞춰 사용한다.
- `Member` Entity는 Repository 조회·토큰 생성의 내부 도메인 객체다.

### Product 등록: Entity 직접 수신이 확인된 모양

04-10 Controller는 `@RequestBody Product`와 `BindingResult`를 받았다. Service는 이미지와 날짜를 처리하고 Repository로 저장했다. 이는 수업의 실제 구현이지만, “Entity 직접 수신이 항상 최선” 또는 “Product 요청 DTO가 있었다”는 근거는 아니다. Product 등록 응답도 저장 Entity 자체만 반환하지 않고 message·id·name·image를 담은 응답 모양을 만들었다.

## 실제 선택 상황 3 — Cart의 요청 DTO와 응답 DTO

| 경계 | 데이터 모양 | 입력 → 처리 → 결과 |
|---|---|---|
| React → Controller | `CartProductDto` | productId·quantity를 받아 인증 email과 함께 Service로 전달 |
| Service 내부 | `Member`, `Product`, `Cart`, `CartProduct` Entity | Repository 조회, 재고 검사, 기존 품목 누적 또는 새 관계 생성·저장 |
| Service → Controller → React | `CartItemDto` 목록 | `CartProduct`마다 화면에 필요한 상품·수량 정보를 DTO로 변환해 반환 |
| React 내부 | `CartProduct` TypeScript type과 state | runtime JSON을 목록·checked·합계·수량 UI에서 사용 |

`CartProductDto`와 `CartItemDto`는 이름이 비슷하지만 방향과 목적이 다르다. frontend의 `CartProduct` type에는 UI용 `checked`도 등장하므로 JPA `CartProduct` Entity와 동일시할 수 없다.

## 실제 선택 상황 4 — Order의 생명주기와 변환

1. React가 선택 상품으로 `OrderDto`와 그 안의 `OrderProductDto`에 대응하는 요청 object를 만든다.
2. Service가 회원·상품 Entity를 조회하고 별도 `Order`·`OrderProduct` Entity를 생성한다.
3. Repository가 Order를 저장한다.
4. 목록 조회에서는 Repository의 `Order` 목록을 Service가 `OrderDetailDto` 목록으로 변환한다.
5. Controller가 DTO 목록을 반환하고 React의 `Order` type/state가 runtime JSON을 사용한다.

Cart 품목과 Order 품목은 생명주기가 다르며, DTO는 그 둘 사이의 저장 객체가 아니다. Order 가격 snapshot 필드는 원본에서 확인되지 않으므로 만들어 설명하지 않는다.

## 함께 사용하는 관계

- DTO는 Entity를 없애는 대체물이 아니다. Controller/Service 경계에서 DTO로 입력을 받고, Service가 Entity를 조회·생성한 뒤 응답 DTO로 변환할 수 있다.
- Entity를 직접 요청·응답에 쓴 날짜도 있다. 수업 전체를 “항상 DTO” 규칙으로 고쳐 쓰지 않는다.
- TypeScript type은 Java DTO와 필드 계약을 맞출 수 있지만, 서로 다른 언어·실행 시점의 선언이다.
- runtime JSON은 Java object와 frontend object 사이의 전송 표현이며 DB row와도 구분된다.

## 확인된 구현 범위와 실행 미확정 범위

- 확인: LoginDto 입력, Product Entity 직접 수신, Cart 요청/응답 DTO 분리, Order 입력/저장/목록 DTO 변환, SearchDto 조립.
- 확인: 04-17 `Order` Entity 목록을 `OrderDetailDto` 목록으로 바꾸는 Service 변환 코드.
- 미확정: 모든 Entity에 별도 DTO가 존재하거나 모든 API가 DTO만 노출한다는 주장.
- 미확정: 04-22 Specification 검색의 실제 성공 응답과 확정 건수. `Page<Product>` 반환 코드가 있다는 사실과 runtime 성공은 분리한다.
- 미확정: TypeScript type이 서버 runtime JSON을 자동 검증한다는 주장. 수업의 type 선언은 compile-time 도구다.

## 자주 헷갈리는 원인과 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| Entity = DB row | Entity는 JPA가 관리하는 Java object이고 row와 매핑되지만 같은 실행 객체는 아니다. |
| DTO = 화면 객체 | 요청 DTO와 응답 DTO를 먼저 나누고, frontend type/state와도 분리한다. |
| TypeScript type = Java DTO | 필드 대응은 가능하지만 compile-time 선언과 Java runtime class는 다르다. |
| JSON = Entity | JSON은 HTTP 전송 표현이다. 어느 Java object에서 직렬화됐는지 확인한다. |
| DTO는 Repository에 저장한다 | Repository는 Entity를 중심으로 DB에 접근하고 DTO는 전달·변환 경계에 둔다. |
| Entity 직접 수신 사례가 있으므로 DTO가 필요 없다 | 실제 Product 구현과 Cart/Order의 DTO 분리 사례를 날짜별로 함께 본다. |

## 선행 개념과 후속 기능 경계

- 선행: [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- 변환 원리: [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]], [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- 후속 기능: [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[concepts/pagination-search|페이징과 검색]]
- 날짜 Summary: [[summaries/2026-04-06-login-jwt-session-cookie|04-06 로그인]], [[summaries/2026-04-14-cart-service|04-14 Cart DTO]], [[summaries/2026-04-16-cart-quantity-stock|04-16 Order]], [[summaries/2026-04-17-cart-total-array-some|04-17 Order 목록]], [[summaries/2026-04-22-product-repository-pageable-search|04-22 SearchDto]]
- Linux/AWS/CI/CD는 이 데이터 모양을 실행·배포하는 후속 환경이고, Passwordless·중간 프로젝트는 새로운 인증 DTO와 외부 서비스 경계를 추가하는 후속 범위다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
