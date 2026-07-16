---
title: Spring Boot REST API
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [spring-boot, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
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

# Spring Boot REST API

## 정의

이 수업의 Spring Boot REST API는 **HTTP method와 URL에 맞춰 path·query·body를 받고, 처리 결과를 status와 JSON·문자열 body로 React에 돌려주는 경계**다. 전체 계층 구조는 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], 각 도메인의 업무 규칙은 Product·Cart·Order concept가 맡고, 이 페이지는 요청과 응답의 실제 모양에 집중한다.

## 왜 중요한가

03-31에는 Spring이 완성 HTML을 반환하는 방식과 객체를 JSON으로 반환하는 방식이 갈라졌고, 04-01에는 React axios와 CORS를 연결해야 비로소 첫 왕복이 완성됐다. 이후 같은 API 경계가 회원가입·로그인, Product CRUD, Cart, Order, `Page<Product>`로 확장되면서 “버튼이 보인다”와 “어떤 요청이 어떤 응답까지 연결됐다”를 날짜별로 구분할 필요가 생겼다.

## 처음 등장하고 확장된 날짜

| 날짜 | HTTP/API 확장 | 대표 artifact |
|---|---|---|
| [[summaries/2026-03-31-spring-boot-controller-html|03-31]] | `@Controller`+Model+Thymeleaf HTML과 `@RestController` JSON을 분리 | `FruitHtmlController`, `FruitController` |
| [[summaries/2026-04-01-react-router-spring-boot|04-01]] | React GET→Spring JSON→state 렌더링, 5173→9000 CORS 허용 | `FruitOne`, `FruitList`, `WebConfig` |
| [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]]·[[summaries/2026-04-07-member-api-string-token|04-07]] | 회원가입 Validation 응답과 로그인 token·회원 정보 응답 | `MemberController.signup()`, `login()` |
| [[summaries/2026-04-08-product-domain-oci|04-08]]~[[summaries/2026-04-13-product-detail-useeffect-service|04-13]] | Product 목록·삭제·등록·수정·상세 CRUD | `ProductController` |
| [[summaries/2026-04-14-cart-service|04-14]]~[[summaries/2026-04-16-cart-quantity-stock|04-16]] | 인증 사용자 Cart 추가·목록·수량 PATCH·삭제 | `CartController` |
| [[summaries/2026-04-16-cart-quantity-stock|04-16]]~[[summaries/2026-04-20-order-list-scenario|04-20]] | Order 생성·목록·완료 PUT·취소 DELETE | `OrderController` |
| [[summaries/2026-04-21-product-pagination-search-react|04-21]]~[[summaries/2026-04-22-product-repository-pageable-search|04-22]] | page·검색 query parameter와 `Page<Product>` 응답 | `ProductController.listProducts()` |

## method·URL·입력 위치

| 목적 | method·URL 예 | 입력 위치 | 수업에서 확인한 결과 |
|---|---|---|---|
| Fruit 한 개·목록 | GET `/fruit`, `/fruit/list` | URL만 사용 | JSON object 또는 array |
| 회원가입·로그인 | POST `/member/signup`, `/member/login` | JSON body | 가입 문자열/필드 오류 map, 로그인 token+회원 map |
| Product | GET `/product/list`, GET `/product/detail/{id}`, POST `/product/insert`, PUT `/product/update/{id}`, DELETE `/product/delete/{id}` | path id, JSON body | 객체·목록·message/error body |
| Cart | POST `/cart/insert`, GET `/cart/list`, PATCH `/cart/edit/{cartProductId}`, DELETE `/cart/delete/{cartProductId}` | 인증 정보, body, path, quantity query | DTO 목록 또는 처리 message |
| Order | POST `/order`, GET `/order/list`, PUT `/order/update/{orderId}`, DELETE `/order/delete/{orderId}` | body, memberId/role query, path/status query | 주문 message·DTO 목록·상태 message |
| 검색 Page | GET `/product/list` | pageNumber·pageSize·searchDateType·category·searchMode·searchKeyword query | `Page<Product>` body |

GET은 조회, POST는 생성·로그인 요청, PUT은 상품 전체 수정·주문 상태 변경, PATCH는 Cart quantity 일부 변경, DELETE는 삭제에 사용됐다. 이것은 수업 artifact의 실제 배치이며 “PUT은 언제나 모든 필드, PATCH는 언제나 한 필드”라는 일반 규칙만으로 각 구현을 추정하지 않는다.

## 실제 status와 body shape

### Member

- Signup Validation 또는 email 중복은 `BAD_REQUEST`와 **field map 자체**를 반환했다. 성공은 `OK`와 `회원 가입 성공` 문자열이다.
- Login 성공은 `OK` body에 `accessToken`, id, name, email, role을 함께 담았다. 코드의 회원 재조회가 null인 분기는 `UNAUTHORIZED`와 `{error: ...}` 모양이다. 자격 증명 인증 실패의 별도 body를 원본 밖에서 만들지 않는다.

### Product

- 등록·수정 Validation은 `BAD_REQUEST`와 `{message, errors}`다. Signup field map과 같은 shape가 아니다.
- 등록 성공은 message와 image, 수정 성공은 message를 담은 map이다. 상세·수정 대상이 없을 때는 `NOT_FOUND` 또는 body 없는 not-found 응답이 등장한다.
- 삭제는 성공 문자열, 대상 없음 `badRequest()` 문자열, 무결성·기타 예외 `internalServerError()` 문자열로 나뉜다. 등록·수정의 파일/DB 예외는 500과 message/error map이다.
- 04-10 Service의 등록 메서드가 저장 뒤에도 `null`을 반환하는 코드와 Controller의 null→500 분기가 함께 남아 있어, 성공 body가 실제로 도달했다고 일괄 단정하지 않는다.

### Cart·Order·Page

- Cart 추가·수량·삭제는 문자열, 목록은 `List<CartItemDto>`다. 수량 Service message가 `오류`로 시작하면 Controller가 bad request 문자열을 반환했다.
- Order 생성은 저장된 송장 id를 포함한 문자열, 목록은 `List<OrderDetailDto>`, 완료는 message, 취소는 성공 message 또는 not-found 응답이다.
- Page 응답은 상품 배열 하나가 아니라 `content`와 전체 개수·전체 page·현재 page 같은 metadata를 함께 가진다. React가 이를 분리해 소비하는 책임은 [[concepts/pagination-search|페이징과 검색]]에 위임한다.

## 입력 → 처리 → 결과

| 입력 | API 경계 처리 | 결과 |
|---|---|---|
| React Fruit 화면 진입 | axios GET→CORS 허용→`FruitController` | JSON을 state에 넣어 한 개·표 목록 표시 |
| Signup form body | `@RequestBody` 변환→`@Valid`/`BindingResult`→응답 분기 | field map 400 또는 성공 문자열 200 |
| Product id·form body | path id/body→Controller 검증→Service 호출 | 조회/CRUD별 status와 서로 다른 body |
| 인증 사용자+Cart 입력 | 인증 객체, body/path/query를 조합 | Cart DTO 목록 또는 처리 message |
| Order body·목록 조건 | body 또는 memberId/role query→Service | 주문 생성 message 또는 역할별 DTO 목록 |
| page·검색 query | 기본값 적용→`SearchDto`→Service→Repository 호출 | `ResponseEntity.ok(productPage)` |

## UI 표시와 실제 연결 날짜

- 03-31의 `FruitOne`·`FruitList`는 자리표시 화면이었고 실제 axios/CORS 왕복은 04-01이다.
- Cart의 checkbox·quantity·삭제 control은 04-14~04-15에 먼저 보였지만 수량·삭제의 최종 연결은 04-15~04-16으로 이어졌다.
- Order Entity·생성 API는 04-16, Cart 주문 버튼의 실제 연결과 목록 API는 04-17, 완료·취소 버튼과 API는 04-20이다.
- 04-20 Paging control 준비, 04-21 단순 page 왕복과 검색 request 준비, 04-22 검색 조건을 포함한 backend 호출 코드를 구분한다.

## 자주 헷갈리는 원인

- **React Router와 API URL:** 화면 path와 Spring endpoint가 같은 문자열이어도 서버와 역할이 다르다.
- **body shape 합치기:** Signup field map, Product `{message, errors}`, 로그인 map, Cart/Order 문자열은 서로 다른 계약이다.
- **client 조건과 서버 검증:** React의 role 버튼·input 조건은 표시/사전 검사다. Spring Validation·인증·업무 Service의 검증과 동일하지 않다.
- **status만 보고 body 추정:** 같은 200·400·500 계열이어도 body가 문자열·map·DTO 목록·Page로 다르다.
- **Controller와 업무 처리:** Controller가 method·URL·입력을 받는 것과 Service/Repository가 실제 변경을 수행하는 것은 별도 단계다.

## 이전 개념과 이후 기능 연결

- 선행: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]의 정적 화면·DOM 흐름이 API 데이터 왕복으로 확장됐다.
- 데이터 모양: [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]가 body가 Java 객체와 계층 사이에서 어떻게 바뀌는지 설명한다.
- 인증: [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]과 [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]가 Bearer header 전후를 맡는다.
- 도메인: [[concepts/product-domain-flow|상품]], [[concepts/shopping-cart-flow|장바구니]], [[concepts/order-flow|주문]]은 각 API 뒤의 업무 생명주기를 설명한다.
- DB 접근: [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]가 Service 이후 조회·저장 방식을 맡는다.

## 직접 수업·교안·후속 경계

- **직접 수업:** 03-31~04-22의 로컬 React 5173↔Spring Boot 9000 HTTP 왕복과 Fruit→Member→Product→Cart→Order→Page 확장이다.
- **교안 보충:** REST·HTTP status·CORS·Spring mapping 용어는 P03·P08 범위와 연결되지만 필요한 구현이 날짜 MD와 고도화 Summary에 전사되어 있어 PDF를 억지로 source에 추가하지 않았다.
- **후속 과목:** Linux·AWS·CI/CD는 실행·배포, Passwordless는 별도 인증 방식, 중간 프로젝트는 실제 조합 단계다. Passwordless 외부 API client 역할을 이 페이지의 4과목 직접 구현에 섞지 않는다.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]

## 출처

- 위 frontmatter의 03-31~04-22 날짜별 직접 구현 MD
