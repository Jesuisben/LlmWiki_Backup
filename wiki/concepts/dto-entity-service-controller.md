---
title: DTO, Entity, Service, Controller
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [spring-boot, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# DTO, Entity, Service, Controller

## 정의

이 페이지는 **React에서 온 runtime JSON이 Spring Controller·DTO/Entity·Service를 지나며 어떤 데이터 모양으로 바뀌고, 응답용 모양으로 다시 나가는지**를 정리한다. Controller·Service·Repository의 일반적인 배치 기준은 [[comparisons/controller-service-repository|Controller vs Service vs Repository]], Entity와 DTO의 선택 기준은 [[comparisons/entity-vs-dto|Entity vs DTO]]에 위임한다.

## 왜 중요한가

이 수업은 Fruit 한 개에서 시작해 Member form, Product Validation, 관계형 Cart, 주문 입력·목록 출력, 검색 DTO로 확장됐다. 이름이 비슷한 React TypeScript type, HTTP JSON, Java DTO, JPA Entity를 한 객체처럼 보면 “누가 이 필드를 만들었고 어디까지 전달되는가”를 추적할 수 없다.

## 처음 등장하고 확장된 날짜

| 날짜 | 데이터 경계의 변화 | 대표 artifact |
|---|---|---|
| [[summaries/2026-03-31-spring-boot-controller-html|03-31]] | Fruit 객체/List를 Model 또는 JSON으로 전달 | `Fruit`, `FruitHtmlController`, `FruitController` |
| [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]] | Signup JSON을 `Member`로 받고 Service가 role·regdate·password를 변경 | `SignupPage`, `MemberController`, `MemberService` |
| [[summaries/2026-04-06-login-jwt-session-cookie|04-06]]~[[summaries/2026-04-07-member-api-string-token|04-07]] | 로그인 입력 전용 DTO와 사용자+token 응답을 분리 | `LoginDto`, login response map |
| [[summaries/2026-04-08-product-domain-oci|04-08]]~[[summaries/2026-04-10-react-event-spread-product-form|04-10]] | Product Entity·React type·form JSON·Validation body가 만남 | `Product`, `Product.ts`, `ProductController` |
| [[summaries/2026-04-14-cart-service|04-14]] | Cart 추가 입력과 목록 출력을 서로 다른 DTO로 분리 | `CartProductDto`, `CartItemDto` |
| [[summaries/2026-04-16-cart-quantity-stock|04-16]]~[[summaries/2026-04-17-cart-total-array-some|04-17]] | 주문 생성 입력 DTO와 주문 목록 출력 DTO를 분리 | `OrderDto`, `OrderProductDto`, `OrderDetailDto` |
| [[summaries/2026-04-22-product-repository-pageable-search|04-22]] | 여러 query parameter를 `SearchDto`로 묶어 Service에 전달 | `SearchDto` |

## 계층별 데이터 모양

| 층위 | 실제 역할 | 같은 것으로 보면 안 되는 대상 |
|---|---|---|
| React TypeScript type/interface | compile-time에 화면 코드가 기대하는 field 모양을 표현 | Java class, runtime JSON 자체 |
| runtime JSON | HTTP body로 실제 전송된 key/value | TypeScript 선언, Entity 인스턴스 |
| Java 요청 DTO | 특정 요청에 필요한 값을 Controller에서 받음 | 응답 DTO, JPA Entity 전체 |
| Java 응답 DTO/map | 화면에 보낼 field와 body shape를 구성 | 요청 DTO, DB row |
| JPA Entity | DB table·관계·영속 상태와 가까운 객체 | 화면 state, 모든 API body |
| Controller | HTTP 값을 Java 값으로 받고 응답 모양/status를 결정 | 업무 규칙 전체, DB 구현 |
| Service | 여러 Entity/Repository를 이용해 값 검증·변환·저장 흐름 수행 | axios 요청 함수, Controller mapping |

## 도메인별 실제 전달

### Fruit — 객체 전달의 출발점

03-31 `FruitHtmlController`는 Fruit를 Model 속성으로 template에 전달했고, `FruitController`는 Fruit 또는 List를 바로 반환해 JSON으로 보냈다. 이때 Fruit는 id·name·price를 가진 단순 Java class였으며, 뒤의 Member/Product처럼 JPA Repository로 저장한 Entity라고 확대하지 않는다.

### Member — 요청 Entity 사용과 응답 shape 분기

SignupPage는 name·email·password·address JSON을 보냈고 Controller는 `@RequestBody Member`로 받았다. Service는 같은 Member에 `Role.USER`, `LocalDate.now()`, 인코딩한 password를 설정한 뒤 저장했다. 이는 수업에서 요청 전용 Signup DTO를 둔 흐름이 아니라 **Entity를 요청 body로 직접 사용한 구현**이다.

- Validation/중복 실패: field명→message인 map 자체
- 성공: `회원 가입 성공` 문자열
- Login 입력: email·password만 가진 `LoginDto`
- Login 성공 출력: accessToken·id·name·email·role map

따라서 Signup field map과 login response map은 둘 다 map이어도 목적과 key가 다르다.

### Product — Entity body와 `{message, errors}`

React `Product` interface는 JSON을 화면 코드에서 다룰 모양이고, Spring `Product`는 JPA·Validation 대상이다. 등록/수정 Controller는 Product JSON을 Entity로 직접 받고, Validation 실패 시 **`message`와 `errors`를 가진 중첩 body**를 반환했다. Signup의 field map 자체와 합치지 않는다. 04-10 Service가 저장 뒤 `null`을 반환하는 코드와 Controller의 null→500 분기도 남아 있으므로 선언된 성공 body와 실제 도달 가능성을 구분한다.

### Cart — 입력 DTO와 출력 DTO

- `CartProductDto`: Product 상세에서 장바구니에 넣을 product id·quantity를 받는 입력이다. 사용자 신원은 body의 member id가 아니라 `Authentication.getName()`의 email에서 얻었다.
- `CartItemDto`: CartProduct와 연결 Product에서 cartProduct id·product id·name·image·price·quantity를 꺼내 목록 한 건으로 평탄화한 출력이다. 04-17에는 stock도 추가됐다.
- React `CartProduct` interface: `CartItemDto` JSON 배열을 화면 state에서 다루기 위한 TypeScript 선언이다. Java DTO와 같은 파일·객체가 아니다.

### Order — 생성 입력과 목록 출력

- `OrderProductDto`: 주문 품목의 cartProduct id·product id·quantity를 받는다.
- `OrderDto`: member id·status·`List<OrderProductDto>`를 묶어 주문 생성 입력으로 보낸다.
- `OrderDetailDto`: 조회한 Order Entity와 OrderProduct 목록을 주문자 이름·주문 id·날짜·상태·내부 품목 모양으로 바꾼 출력이다.

Service는 `OrderDto`를 그대로 저장하지 않는다. Member와 Product를 다시 찾고 재고를 검사해 `Order`·`OrderProduct` Entity를 만들며, 조회 때는 Entity 목록을 `OrderDetailDto` 목록으로 바꾼다. React가 보낸 memberId·status·role이 body/query에 있다는 사실만으로 서버가 그 소유권·권한을 검증했다고 단정하지 않는다.

### 검색 — query parameter를 SearchDto로 묶기

04-22 Controller는 page 값과 검색 값들을 개별 `@RequestParam`으로 받고, searchDateType·category·searchMode·searchKeyword를 `SearchDto`로 묶어 Service에 넘겼다. `SearchDto`는 검색 입력 모양이고 `Page<Product>`는 조회 결과 모양이므로 같은 DTO나 같은 방향이 아니다.

## 입력 → 처리 → 결과

| 입력 | Controller/Service 처리 | 결과 모양 |
|---|---|---|
| Signup JSON | `Member` 변환→Validation→Service가 role/date/password 설정 | field map 또는 성공 문자열 |
| Login JSON | `LoginDto`→인증→Member 조회→token 생성 | token+회원 map |
| Product form JSON | `Product` 변환→Validation→파일/저장 처리 | `{message, errors}` 또는 처리별 map |
| Cart 추가 JSON+인증 email | `CartProductDto`→Member/Product/Cart 처리 | 문자열, 이후 `CartItemDto[]` 조회 |
| Order 생성 JSON | `OrderDto`/`OrderProductDto`→Entity 구성·저장 | 송장 id 포함 문자열 |
| Order 목록 query | role/memberId→Entity 조회→`OrderDetailDto` 변환 | DTO 배열 |
| 검색 query | `SearchDto` 생성→Service 조건 조립 | `Page<Product>` |

## 실제 수업 예시에서 확인할 변환 지점

1. **JSON→Java:** `@RequestBody`가 Signup/Product/Cart/Order body를 Java 객체로 받는다.
2. **요청 값 보강:** Member Service는 role·regdate·encoded password를 설정한다.
3. **관계 조립:** Cart·Order Service는 id로 Entity를 다시 찾아 관계와 수량·재고를 처리한다.
4. **Entity→응답 DTO:** CartProduct→`CartItemDto`, Order→`OrderDetailDto`로 화면용 모양을 만든다.
5. **응답 JSON→React state:** runtime JSON이 TypeScript 선언에 맞는다고 기대하며 배열·객체 state에 들어간다.

## 자주 헷갈리는 원인

- **DTO는 무조건 한 방향이라고 생각하기:** Cart와 Order는 입력 DTO와 출력 DTO가 따로 있다.
- **이름이 같으면 같은 객체라고 생각하기:** React `Product`, JSON Product, Java `Product` Entity는 서로 다른 실행 계층이다.
- **모든 요청에 DTO를 썼다고 생각하기:** 수업의 Signup·Product는 Entity를 request body로 직접 사용했다.
- **응답 오류 shape를 통일하기:** Signup field map과 Product `{message, errors}`는 화면 처리 목적이 비슷해도 구조가 다르다.
- **Controller가 Entity를 받으면 곧 저장됐다고 생각하기:** Service 분기·Repository 호출·transaction과 실제 응답까지 확인해야 한다.
- **client id/role을 인증 사실로 생각하기:** body/query 값은 입력일 뿐 서버 ownership·authorization 검증의 증거가 아니다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/java-class-object|Java 클래스와 객체]]와 Oracle의 table·관계가 Java Entity/DTO 구분의 기반이 된다.
- HTTP 경계: [[concepts/spring-boot-rest-api|Spring Boot REST API]]가 method·URL·status/body를 설명한다.
- DB 접근: [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]가 Entity 조회·저장을 맡는다.
- 관계 세부: [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]은 CartProduct·OrderProduct의 FK 주인과 cascade를 다음 세션에서 고도화한다.
- 도메인 흐름: [[concepts/shopping-cart-flow|장바구니]]와 [[concepts/order-flow|주문]]이 각 데이터 모양의 업무 생명주기를 맡는다.

## 직접 수업·교안·후속 경계

- **직접 수업:** Fruit·Member·Product·Cart·Order·Search의 Java 객체/DTO/Entity와 Controller→Service 전달·변환이다.
- **교안 보충:** P08의 Spring 계층·DTO/JPA 설명은 날짜 MD에 필요한 구현이 전사되어 있어 별도 PDF source를 추가하지 않았다.
- **후속 과목:** Linux·AWS·CI/CD는 이 데이터 경계를 실행·배포하고, Passwordless와 중간 프로젝트는 인증 DTO/API를 별도로 확장한다. 그 후속 DTO를 4과목 구현으로 소급하지 않는다.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]

## 출처

- 위 frontmatter의 03-31~04-22 날짜별 직접 구현 MD
