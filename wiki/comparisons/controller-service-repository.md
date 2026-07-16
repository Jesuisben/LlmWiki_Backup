---
title: Controller vs Service vs Repository
created: 2026-07-02
updated: 2026-07-16
type: comparison
tags: [spring-boot, backend, java]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# Controller vs Service vs Repository

## 비교 목적

이 비교는 세 파일 이름을 위에서 아래로 외우기 위한 것이 아니다. React가 보낸 입력이 **어디에서 HTTP 요청으로 해석되고**, **어디에서 업무 규칙과 여러 저장 작업으로 조립되며**, **어디에서 DB 조회·저장 명령이 실행되는지**를 추적하기 위한 기준이다. 전체 계층 구조는 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], 기능을 늘려 간 절차는 [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]에 맡기고, 여기서는 세 계층의 선택 기준만 비교한다.

## 실제 수업에서 비교가 필요해진 이력

- **2026-04-03:** 회원가입에서 `MemberController`가 요청·검증 결과를 받고 `MemberService`를 호출하며, `MemberService`가 `MemberRepository`로 조회·저장하는 초기 세 계층 흐름이 확인된다.
- **2026-04-10:** 상품 등록은 Controller가 `Product` 요청과 `BindingResult`를 받고, Service가 이미지 파일명·등록일을 처리한 뒤 Repository 저장을 호출하는 구조로 확장됐다.
- **2026-04-14~15:** 장바구니 추가·목록·수량·삭제에서 HTTP 입력, 인증 사용자, 재고·동일 품목 규칙, 여러 Repository 호출의 경계가 선명해졌다.
- **2026-04-16~20:** 주문 생성·목록·상태 변경·취소에서 여러 Entity와 저장 작업을 한 업무 단위로 묶는 Service와 transaction 경계가 중요해졌다.
- **2026-04-21~22:** 상품 검색에서 Controller의 query parameter 수신, Service의 `Specification`·정렬·`PageRequest` 조립, Repository의 `findAll(spec, pageable)` 호출이 분리됐다.

## 한눈에 보기

| 판단 항목 | Controller | Service | Repository |
|---|---|---|---|
| 주된 경계 | HTTP 요청·응답 | 업무 use case·transaction | DB 접근 계약 |
| 받는 값 | path/query/body, `Authentication` 등 | Controller가 넘긴 DTO·Entity·식별값 | Entity, id, query 조건, `Pageable` 등 |
| 하는 일 | mapping, 요청 데이터 바인딩, Service 호출, 응답 선택 | 조회·검증·변환·상태 변경 순서 조립 | `findBy...`, `save`, `deleteById`, JPQL/Specification 조회 |
| 반환 결과 | `ResponseEntity`, JSON body, message | Entity·DTO·목록·message 등 use case 결과 | Entity·`Optional`·`List`·`Page`·영향 행 수 등 |
| 수업 artifact | `MemberController`, `CartController`, `OrderController`, `ProductController` | `MemberService`, `CartService`, `OrderService`, `ProductService` | Member/Product/Cart/Order Repository |
| 넣지 말아야 할 중심 책임 | DB query 세부 구현 | URL·status 자체 결정의 전부 | HTTP 응답·화면 상태·업무 시나리오 |

## 실제 선택 상황 1 — 회원가입과 상품 등록

### Member: 세 계층이 처음 연결된 흐름

1. React 회원가입 화면이 데이터를 보낸다.
2. `MemberController`가 요청을 받고 검증·중복 확인 흐름에서 `MemberService`를 호출한다.
3. `MemberService`가 `MemberRepository.findByEmail(...)`과 저장을 사용한다.
4. Controller가 검증·저장 결과에 맞는 HTTP 응답을 반환한다.

이때 04-03 원본은 Controller까지 들어온 데이터를 Service 이후에 처리한다고 설명한다. 따라서 “Controller가 모든 회원 업무를 끝낸다”거나 “Repository가 비밀번호 처리 정책을 결정한다”고 읽으면 계층 경계가 무너진다.

### Product: Entity 직접 수신도 DTO 변환과 별개다

04-10 상품 등록 Controller는 `@RequestBody Product`와 `BindingResult`를 받았다. Service는 이미지 데이터에서 파일을 저장하고 파일명·등록일을 설정한 뒤 Repository 저장을 호출했다. 즉 이 날짜에는 요청 DTO가 아니라 Entity를 직접 받은 구현이 확인되지만, 그렇다고 Controller·Service·Repository가 같은 책임이 되는 것은 아니다.

## 실제 선택 상황 2 — 장바구니 추가와 목록

### 입력 → 처리 → 결과

| 단계 | 확인된 artifact | 책임 |
|---|---|---|
| 입력 | `CartController`의 `CartProductDto`와 `Authentication` | Controller가 요청 body와 인증 사용자 email을 Service 호출 인자로 만든다. |
| 처리 | `CartService.addProductToCart(...)` | 회원·상품·Cart를 찾고 재고를 검사하며, 기존 품목이면 quantity를 누적하고 아니면 새 `CartProduct`를 만든다. |
| DB 접근 | Member/Product/Cart Repository와 `CartProductService`가 사용하는 Repository | 조회·저장 명령을 수행한다. |
| 결과 | 추가 message 또는 `List<CartItemDto>` | Controller가 `ResponseEntity`로 반환한다. |

`CartService`가 여러 Repository와 작은 `CartProductService`를 함께 호출한다는 사실이 핵심이다. 계층은 반드시 “Controller 한 번 → Service 한 번 → Repository 한 번”으로만 내려가는 직선이 아니다. 한 use case가 여러 조회·저장을 조율할 수 있다.

## 실제 선택 상황 3 — 주문과 transaction 경계

- 04-16 `OrderController`는 `OrderDto`를 받고 `OrderService.createOrder(...)` 결과로 message를 만들었다.
- Service는 회원·상품을 찾고, 주문 품목을 만들고, 재고를 줄이고, Cart 품목을 삭제한 뒤 Order를 저장하는 순서를 조립했다.
- 04-17에는 `createOrder(...)`에 `@Transactional`을 추가한 기록이 확인된다. 따라서 04-16 작성 시점부터 transaction 연결이 완성됐다고 소급하지 않는다.
- 04-20 주문 상태 변경과 취소 Service에는 transaction 표시와 상태 변경·재고 복원·삭제 흐름이 확인된다.

transaction은 “Service라는 이름이면 자동으로 생기는 기능”이 아니다. 원본에서 실제 annotation이 확인된 메서드와 날짜에만 transaction 경계가 있다고 기록해야 한다.

## 실제 선택 상황 4 — 페이징·검색

1. React가 page·size와 검색 조건을 query parameter로 보낸다.
2. `ProductController`가 값을 받아 `SearchDto`를 만들고 Service를 호출한다.
3. `ProductService`가 조건별 `Specification`, `Sort`, `PageRequest`를 조립한다.
4. `ProductRepository.findAll(spec, pageable)`이 DB 조회를 맡는다.
5. `Page<Product>`가 Controller를 거쳐 응답된다.

이 흐름에서 검색 조건의 **업무 조립**은 Service 책임이고, `findAll`의 **DB 접근 계약**은 Repository 책임이다. 다만 04-22 원본에는 `JpaSpecificationExecutor<Product>` 상속, 날짜 type 정합성, 실제 API 성공 응답·확정 건수가 모두 확인되지 않으므로 runtime 검색 완료를 단정하지 않는다.

## 확인된 구현 범위와 실행 미확정 범위

- 확인: Member 회원가입, Product 등록, Cart 추가·목록·수량·삭제, Order 생성·목록·상태·취소, Product page/search에서 날짜별 Controller·Service·Repository 작성·호출 범위.
- 확인: 04-17 주문 생성과 04-20 상태 변경·취소에서 실제 표시된 transaction 경계.
- 미확정: 모든 기능이 처음 등장한 날부터 세 계층과 transaction을 완성했다는 주장.
- 미확정: 04-22 검색의 `JpaSpecificationExecutor` 상속·날짜 type 정합성·runtime 성공 응답.

## 함께 사용하는 관계

- Controller와 Service는 대체 관계가 아니라 HTTP 경계와 업무 경계를 연결한다.
- Service는 Repository를 호출하지만 Repository의 기능과 동의어가 아니다. 조회 결과를 어떻게 검증·결합·변환할지는 Service가 결정한다.
- Service가 다른 Service를 호출할 수 있다. Cart와 Order 수업에서 Member/Product/CartProduct Service가 함께 사용됐다.
- 단순 조회·저장 한 번인 날도 있고 세 계층이 모두 완성되지 않은 기능도 있다. 실제 작성·호출이 확인된 범위만 그 날짜의 구현으로 본다.

## 자주 헷갈리는 원인과 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| Controller는 모든 처리를 하는 파일이다 | HTTP 입력을 Java 값으로 받고 Service 결과를 HTTP 응답으로 바꾸는 경계인지 본다. |
| Service는 Repository를 한 번 감싼 파일이다 | 재고·중복·상태 전이·여러 저장 순서처럼 업무 규칙이 있는지 본다. |
| Repository가 DB에서 가져왔으니 반환 모양도 정한다 | DB 조회 결과와 외부 응답 DTO 변환은 다른 책임이다. |
| `@Transactional`은 모든 Service에 이미 적용됐다 | 원본에서 실제 annotation과 적용 메서드·날짜를 확인한다. |
| 세 계층은 항상 완성된 직선 호출이다 | Member·Product·Cart·Order·검색별로 실제 클래스와 호출 범위를 따로 추적한다. |

## 선행 개념과 후속 기능 경계

- 선행: [[concepts/spring-boot-rest-api|Spring Boot REST API]], [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]], [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- 후속 기능: [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]
- 날짜 Summary: [[summaries/2026-04-03-spring-member-seed-react-comments|04-03 회원가입]], [[summaries/2026-04-14-cart-service|04-14 Cart Service]], [[summaries/2026-04-16-cart-quantity-stock|04-16 주문 시작]], [[summaries/2026-04-20-order-list-scenario|04-20 주문 상태]], [[summaries/2026-04-22-product-repository-pageable-search|04-22 상품 검색]]
- 이 페이지는 FrontEnd_BackEnd 직접 구현까지만 다룬다. Linux의 jar 실행, AWS 배포, CI/CD 자동화, Passwordless 및 중간 프로젝트의 인증 확장은 세 계층 위에 이어지는 후속 운영·통합 범위다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
