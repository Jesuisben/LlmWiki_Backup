---
title: 상품 도메인 기능 흐름
created: 2026-07-06
updated: 2026-07-16
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# 상품 도메인 기능 흐름

## 정의

이 수업의 상품 도메인 흐름은 `Category`·`Product`를 만든 뒤 **초기 데이터→목록→삭제→등록→수정→상세→대표 상품→페이징/검색**으로 상품의 생명주기를 확장한 과정이다. Cart와 Order는 Product를 참조하는 다음 도메인이지만, 장바구니 선택·수량과 주문 상태·재고 처리의 세부 책임은 각각 [[concepts/shopping-cart-flow|장바구니 기능 흐름]]과 [[concepts/order-flow|주문 기능 흐름]]이 맡는다.

## 왜 중요한가

Product는 React 화면의 카드 한 장이면서 MySQL 행, JPA Entity, API JSON의 출발점이다. 등록·수정에서는 이미지 파일과 DB 파일명이 함께 바뀌고, 삭제에서도 화면 배열·DB 행·이미지 파일을 따로 확인해야 한다. 후반에는 같은 Product 목록이 대표 상품과 Page/search 응답으로 확장되므로, 한 기능의 생명주기를 frontend와 backend 양쪽에서 추적하는 핵심 도메인이 되었다.

## 날짜별 실제 확장

| 날짜 | 상품 기능의 단계 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-08-product-domain-oci|2026-04-08]] | Category/Product 정의→이미지 기반 seed→목록 API→React card | `Category`, `Product`, `GenerateData`, `ProductTest.createProductMany()`, `ProductList` |
| [[summaries/2026-04-09-product-delete-routing-jsx-table|2026-04-09]] | 관리자 삭제 왕복→목록 state 갱신→등록 route/form 시작 | `ProductService.deleteProduct`, `ProductController.delete`, `ProductInsertForm` |
| [[summaries/2026-04-10-react-event-spread-product-form|2026-04-10]] | 등록 form event·Data URL→Spring 파일/DB 저장→Validation 오류→수정 form 시작 | `ProductInsertForm`, `saveProductImage`, `ProductController.insert`, `ProductUpdateForm` |
| [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13]] | 수정 GET/PUT과 상세 GET 완성 | `ProductUpdateForm`, `ProductDetail`, `getProductById` |
| [[summaries/2026-04-20-order-list-scenario|2026-04-20]] | DB 대표 상품을 Home carousel에 표시하고 Paging UI 준비 | HomePage의 `filter=bigs`, `PagingInfo`, `Paging.tsx` |
| [[summaries/2026-04-21-product-pagination-search-react|2026-04-21]]~[[summaries/2026-04-22-product-repository-pageable-search|04-22]] | Page 왕복→검색 form/request 준비→Specification+Pageable 검색 코드 연결. 실행 전제는 별도 확인 필요 | `FieldSearch`, `SearchDto`, `ProductSpecification`, `ProductRepository.findAll` |

## 대표 artifact와 계층별 책임

| 위치 | 대표 artifact | 이 도메인에서 맡은 책임 |
|---|---|---|
| React 화면 | `ProductList`, `ProductInsertForm`, `ProductUpdateForm`, `ProductDetail`, HomePage | route id·입력 state·FileReader·요청·응답·목록/상세/대표 상품 표시 |
| Controller | `ProductController` | HTTP method·path/parameter/body를 받고 Validation·Service 결과를 응답으로 변환 |
| Service | `ProductService` | 목록/단건 조회, 이미지 decode·파일 저장/삭제, Entity 필드 변경, 검색 조건·page 조립 |
| Repository | `ProductRepository` | id 역순 목록, 단건 저장/삭제, 대표 상품 조건, Specification+Pageable 조회 signature 작성 |
| 데이터 | `Category`, `Product`, React `Product` type | enum/Entity의 DB·Validation 구조와 화면이 받는 JSON shape를 각 환경에 표현 |

React의 axios 함수와 Spring `ProductService`는 모두 “상품 처리 함수”처럼 보여도 같은 계층이 아니다. 전자는 HTTP 요청과 화면 state를, 후자는 이미지·상품·검색 업무 규칙을 담당한다. 전체 계층 경계는 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]에서 확인한다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| seed | 이미지 폴더의 `.jpg` 파일명 | `GenerateData`가 Product 생성→Repository `save()` 반복 | products table 초기 데이터 |
| 목록 | React의 Product 목록 GET | Controller→Service→Repository id 역순 조회 | Product JSON 배열→card 목록 |
| 삭제 | 관리자 클릭과 Product id | 버블링 중단→DELETE→상품 조회→image 파일 처리→Repository 삭제 | 성공 후 React `filter`로 해당 카드 제거 |
| 등록 | 빈 `ProductInsertForm`의 필드와 image Data URL | POST→Validation→Data URL decode·파일 저장→파일명을 Product에 반영→Repository save | 원본 Service는 저장 뒤에도 `null`을 반환해 Controller가 500으로 판정; 의도된 성공 경로와 실제 코드 불일치를 확인해야 함 |
| 수정 | route id, 기존 GET 결과, 바뀐 form body | PUT→기존 Product 조회→필드 반영→새 image가 있으면 이전/새 파일 처리→save | 기존 상품·목록·이미지 갱신 |
| 상세 | card가 선택한 Product id | detail route→GET→Service/Repository 단건 조회→state 반영 | 이미지·가격·재고·설명과 후속 Cart 진입 화면 |
| 대표 상품 | HomePage의 선택적 filter | Product 조건 조회→React 배열→carousel `map` | 정적 항목 대신 DB 상품과 상세 이동 |
| 페이징/검색 | page와 기간·카테고리·mode·keyword | React 재요청→Controller `SearchDto`→Service 조건/page 조립→Repository 호출 코드 | 의도한 결과는 `Page<Product>`의 `content`와 metadata이며 실제 실행 전제는 추가 확인 필요 |

## 실제 수업 예시: image Data URL과 Spring 파일 저장

04-10의 file input은 일반 text input의 `value`가 아니라 `files[0]`을 사용했다. `FileReader.readAsDataURL` 결과를 Product state의 image에 넣어 JSON body로 보냈고, Spring Service는 Base64 부분을 decode해 파일로 저장한 뒤 생성한 파일명을 Product에 반영했다. 04-13 수정에서는 새 Data URL이 있을 때 기존 image를 삭제하고 새 파일을 저장했다. file input에는 브라우저 보안상 기존 파일 경로를 기본값으로 넣을 수 없으므로, “기존 image 정보”와 “새로 선택한 file control”은 같은 값이 아니다.

04-10 등록 코드는 **의도와 실제 반환값을 분리해 읽어야 한다.** `ProductService.insertProduct()`는 image와 Product를 저장한 뒤에도 마지막에 `null`을 반환했고, Controller는 반환값이 `null`이면 500을 응답하도록 작성됐다. React에는 성공 시 state를 초기화하고 목록으로 이동하는 경로가 있지만, 제시된 backend 코드 그대로 그 성공 응답이 실행됐다고 확정하지 않는다. 04-13 수정 흐름은 별도의 기존 상품 GET/PUT 경로다.

## Validation과 오류 표시

`Product` Entity에는 name·price·category·stock·image·description 관련 Validation이 등장했다. Controller는 `@Valid`·`BindingResult`·`FieldError`로 field map을 만들고, React 등록/수정 form은 서버의 `errors`와 `message`를 local 오류 state에 합쳐 feedback을 표시했다. 이 화면별 오류는 [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]의 전역 401 처리와 구분한다.

## 자주 헷갈리는 원인

- **Category를 별도 테이블로 생각하는 경우:** 04-08 구현은 Java enum을 `Product.category`에 문자열로 저장했다.
- **seed와 목록 API를 같은 단계로 보는 경우:** `GenerateData`·`ProductTest`는 DB를 채우고, 목록 Controller/Service/Repository는 저장된 행을 읽는다.
- **관리자 버튼이 보이면 인가가 끝났다고 생각하는 경우:** role 기반 화면 표시는 UI 제어다. 실제 서버 권한 정책 전체와 같다고 단정하지 않는다.
- **삭제 성공을 하나의 상태로 보는 경우:** React 배열, DB Product 행, 운영체제 image 파일은 서로 다른 결과다. 04-09에는 화면/DB 삭제 후 잘못된 파일 경로 때문에 image가 남은 사례를 확인했다.
- **등록과 수정을 같은 요청으로 보는 경우:** 폼·event·Validation은 공통이지만 등록은 빈 state와 새 저장, 수정은 id 기반 기존 GET과 PUT이다.
- **등록 의도와 실제 실행 결과를 합치는 경우:** 04-10 Service의 `return null`과 Controller의 500 판정이 충돌한다. Repository save가 호출됐다는 사실과 React가 성공 응답을 받았다는 주장은 별개다.
- **상품 배열과 Page를 같은 응답으로 보는 경우:** 04-08 목록은 body 자체가 배열이었고, 04-21 이후 Page 응답은 `content`가 상품 배열이며 나머지는 metadata다.
- **검색 코드 연결과 실행 검증을 같은 완료로 보는 경우:** 04-22에는 `findAll(Specification, Pageable)` 호출 흐름을 작성했지만 원본 Repository의 `JpaSpecificationExecutor<Product>` 상속과 `LocalDate`/`LocalDateTime` 날짜 비교 정합성은 확인이 필요하다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[concepts/react-form-state-event|React 폼 상태와 이벤트]], [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]이 Product 화면의 표현·입력·조회 시점을 맡는다.
- backend 기반: [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]와 [[comparisons/controller-service-repository|Controller vs Service vs Repository]]가 저장·조회 계층을 설명한다.
- 후속 목록 확장: [[concepts/pagination-search|페이징과 검색]]이 page/search 조건 왕복의 중심 책임을 맡는다.
- 후속 도메인: Cart는 Product와 quantity를 연결하고, Order는 Product 재고와 주문 상태를 처리한다. 해당 세부 로직을 이 페이지에 중복하지 않는다.

## 직접 수업·교안·후속 확장 경계

- **직접 수업:** 04-08~04-13 Product seed·CRUD·상세, 04-20 대표 상품, 04-21 Page 왕복·검색 준비, 04-22 검색 backend 연결 코드 작성이다. Specification 실행 성공까지 검증됐다고 확대하지 않는다.
- **교안 보충:** React form/event와 Spring JPA·Validation·Pageable, 필드 검색 교안의 필요한 내용이 날짜 MD에 충분히 전사되어 있어 P07·P08·P10을 별도 source로 추가하지 않았다.
- **R19 범위:** 총정리는 Product와 04-15 Cart 삭제까지 복습한다. 대표 상품·페이징·검색은 R16~R18 날짜 MD에 근거하며 R19에 소급하지 않는다.
- **후속 과목:** Linux·AWS·CI/CD는 Product 서비스를 실행·배포·자동화하고, Passwordless와 중간 프로젝트는 인증·실제 적용을 확장한다. 04월 Product 직접 구현과 같은 수업 단계로 합치지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md` — 04-15 Cart 삭제까지의 복습 범위
