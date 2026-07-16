---
title: FrontEnd_BackEnd 총정리
created: 2026-07-03
updated: 2026-07-16
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
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

# FrontEnd_BackEnd 총정리

## 한 줄 요약

로컬 Spring Boot·React·MySQL 환경에서 Fruit 요청·응답을 처음 연결한 뒤 Member 회원가입·JWT 인증, Product CRUD, Cart, Order, 대표 상품, 페이징·검색까지 같은 Controller→Service→Repository→DB 왕복을 기능별로 확장한 18일 과정의 복습 허브다.

## 이 허브를 읽는 방법

- 이 페이지는 R01~R18 날짜 Summary의 순서와 기능 연결을 한눈에 복습하는 지도다. 교시별 구현·오류·테스트는 각 날짜 링크에서 확인한다.
- 총정리 원본 R19는 환경 구성부터 04-15 Cart 삭제까지 자세히 모았고 파일 끝에도 04-15까지 마무리했다고 적혀 있다. 제목의 03-30~04-03 표기와 달리 더 뒤의 Cart 내용도 포함하지만, 04-16~04-22 Order·대표 상품·검색은 날짜 MD로 보완해야 한다.
- 따라서 날짜 귀속은 현재 고도화한 18개 날짜 Summary와 날짜 MD를 우선하고, 총정리 원본의 긴 기능 묶음은 복습 보조로 사용한다.

## 커리큘럼 전체 흐름

| 구간 | 날짜 | 무엇을 연결했는가 | 대표 artifact |
|---|---|---|---|
| 환경과 첫 응답 | [[summaries/2026-03-30-fullstack-environment-setup|03-30]] | MySQL·Spring Boot·Vite React를 각각 실행하고 후속 요청 데이터 준비 | `application.properties`, Vite, `Fruit` |
| Fruit HTML→JSON | [[summaries/2026-03-31-spring-boot-controller-html|03-31]] | Thymeleaf 완성 HTML 응답에서 REST JSON과 React Router 화면으로 전환 | `FruitHtmlController`, `FruitController`, `AppRoutes` |
| 첫 프론트↔백엔드 왕복 | [[summaries/2026-04-01-react-router-spring-boot|04-01]] | React type·axios·state/effect와 Spring API를 CORS 허용 뒤 연결 | `Fruit.ts`, `FruitOne`, `FruitList`, `WebConfig` |
| Home·Member 기반 | [[summaries/2026-04-02-react-bootstrap-homepage|04-02]] | 이미지 carousel 뒤 JPA Member·Validation·Security·Repository 시작 | `HomePage`, `Member`, `SecurityConfig`, `MemberRepository` |
| 회원가입 | [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]] | form 입력→검증·중복 확인→암호화 저장→HTTP 응답 | `SignupPage`, `MemberService`, `MemberController` |
| JWT 발급 준비 | [[summaries/2026-04-06-login-jwt-session-cookie|04-06]] | Cookie/Session/JWT 이론에서 LoginPage·DTO·token 생성으로 이동 | `axiosInstance`, `LoginPage`, `LoginDto`, `JwtTokenProvider` |
| JWT 인증 적용 | [[summaries/2026-04-07-member-api-string-token|04-07]] | Bearer token→Filter 검증→SecurityContext와 사용자 조회·Security 설정 | `JwtAuthenticationFilter`, `MemberDetailsService`, `SecurityConfig` |
| Product 조회 시작 | [[summaries/2026-04-08-product-domain-oci|04-08]] | Product 구조·seed·Repository 테스트에서 목록 API와 React card로 연결 | `Category`, `Product`, `GenerateData`, `ProductList` |
| Product 삭제·등록 시작 | [[summaries/2026-04-09-product-delete-routing-jsx-table|04-09]] | 관리자 삭제 클릭→이미지·DB 처리→목록 갱신 후 등록 form 시작 | `ProductService.deleteProduct`, `ProductInsertForm` |
| Product 등록·수정 form | [[summaries/2026-04-10-react-event-spread-product-form|04-10]] | event·spread·FileReader→POST body→이미지 저장·Validation, 수정 화면 시작 | `ControlChange`, `FileReader`, 등록 Controller |
| Product 수정·상세→Cart | [[summaries/2026-04-13-product-detail-useeffect-service|04-13]] | 수정 GET/PUT과 상세 GET을 마치고 Cart 관계·추가 요청 시작 | `ProductUpdateForm`, `ProductDetail`, `Cart`, `CartProduct` |
| Cart 추가·목록 | [[summaries/2026-04-14-cart-service|04-14]] | 인증 사용자 기준 Cart 품목 누적과 DTO 목록을 React 표로 반환 | `CartService`, `CartItemDto`, `CartList` |
| Cart 선택·수량·삭제 기반 | [[summaries/2026-04-15-cart-list-selection-typescript|04-15]] | 전체/개별 선택·합계, PATCH 수량 변경과 삭제 backend 기반 | `toggleAllCheckBox`, `changeQuantity`, `CartController` |
| Cart 보정→Order 생성 | [[summaries/2026-04-16-cart-quantity-stock|04-16]] | 수량·삭제를 완성하고 선택 Cart 품목을 Order/OrderProduct로 저장 | `Order`, `OrderProduct`, `OrderDto`, `OrderService.createOrder` |
| 즉시 주문·주문 목록 시작 | [[summaries/2026-04-17-cart-total-array-some|04-17]] | stock·`some` 검증, 상품 상세 즉시 주문, 역할별 PENDING 목록 조회 | `buyNow`, `OrderDetailDto`, `OrderList` |
| Order 완료·취소와 대표 상품 | [[summaries/2026-04-20-order-list-scenario|04-20]] | 주문 card·상태 처리·재고 복원 후 DB 대표 상품 carousel과 Paging 시작 | `OrderList`, 완료 PUT, 취소 DELETE, `PagingInfo` |
| page 왕복·검색 준비 | [[summaries/2026-04-21-product-pagination-search-react|04-21]] | page parameter↔Page 응답 연결, 검색 state·request·DTO·개별 Specification 준비 | `Paging`, `FieldSearch`, `SearchDto`, `ProductSpecification` |
| 검색 backend 완성 | [[summaries/2026-04-22-product-repository-pageable-search|04-22]] | Controller parameter→Service 조건 조립·Pageable→Repository 조회→Page 응답 | `ProductRepository`, `Specification`, `PageRequest` |

## 기능별 대표 요청·응답 왕복

### 1. Fruit — 구조를 배우기 위한 최소 왕복

- **입력:** React Router가 선택한 `FruitOne` 또는 `FruitList`가 Spring `/fruit` 계열 API를 GET으로 요청한다.
- **처리:** `FruitController`가 한 개 또는 목록을 JSON으로 반환한다. 서로 다른 port 때문에 처음 차단된 요청은 `WebConfig`의 CORS 허용 뒤 통과한다.
- **결과:** axios 응답을 `Fruit` type의 state에 넣고 JSX 표에서 렌더링한다.
- 이 작은 왕복이 이후 Member·Product·Cart·Order에 반복되는 화면→API→응답 구조의 출발점이다.

### 2. Member와 회원가입 — 화면 검증에서 저장까지

- **입력:** `SignupPage`의 name·email·password·address state를 JSON body로 POST한다.
- **처리:** Controller의 Validation·`BindingResult`와 이메일 중복 분기 후 Service가 역할·등록일을 설정하고 비밀번호를 인코딩해 Repository에 저장한다.
- **결과:** 필드 오류 Map 또는 가입 성공 응답이 React 화면으로 돌아간다.

### 3. JWT 로그인 — token 발급과 후속 요청 인증

- **입력:** `LoginPage`가 자격정보를 `LoginDto` 형태로 보낸다.
- **처리:** 로그인 경로가 사용자를 조회하고 `JwtTokenProvider`가 token을 만들며, 후속 요청에서는 axiosInstance가 Bearer token을 전달하고 Filter가 검증해 SecurityContext에 인증 객체를 둔다.
- **결과:** React는 로그인 user 상태를 사용하고 Spring의 보호 API는 인증 정보를 읽을 수 있다. Cookie·Session·JWT 설명은 인증 상태 설계의 비교이며 Passwordless 구현이 아니다.

### 4. Product — 조회에서 CRUD·상세로

- **입력:** 목록·등록·수정·상세 화면이 Product type과 route id, form state를 사용해 GET·POST·PUT·DELETE를 보낸다.
- **처리:** Controller가 요청·Validation·응답을, Service가 image file·도메인 로직을, Repository가 DB 저장·조회를 담당한다.
- **결과:** 목록 card, 등록·수정 오류, 상세 화면, 삭제 뒤 local 목록 갱신으로 돌아온다.
- 04-08 seed·조회, 04-09 삭제·등록 시작, 04-10 등록·수정 시작, 04-13 수정·상세 완료의 날짜 경계를 유지한다.

### 5. Cart — 인증 사용자와 품목 관계

- **입력:** 상품 상세가 Product id와 quantity를 보내고, CartList가 선택·수량·삭제 동작을 보낸다.
- **처리:** 인증 email로 Member와 Cart를 찾고, CartProduct가 Product와 quantity를 연결한다. 목록에서는 Entity 관계를 평탄한 `CartItemDto`로 바꿔 반환한다.
- **결과:** 같은 상품은 수량이 누적되고, CartList에는 사용자별 품목·가격·재고·선택 상태가 표시되며 PATCH·DELETE 결과가 화면 state에 반영된다.

### 6. Order — 선택 품목 저장과 상태 생명주기

- **입력:** Cart의 선택 품목 배열 또는 Product 상세 한 건을 Order request body로 POST한다.
- **처리:** Service가 Member·Product·재고를 확인하고 OrderProduct를 구성해 재고를 차감하며 Cart에서 온 품목을 제거하고 Order를 저장한다.
- **결과:** 역할별 PENDING 목록을 조회해 card로 표시하고, 관리자는 완료, 사용자·관리자는 취소를 요청한다. 완료는 상태 변경, 취소 구현은 재고 복원 뒤 Order 삭제로 이어진다.

### 7. 대표 상품과 페이징·검색 — 목록 조회의 확장

- **대표 상품:** HomePage의 선택적 filter→Product 조회→응답 배열→carousel과 상세 이동으로 정적 이미지를 DB 상품으로 바꿨다.
- **페이징:** `pageNumber`·`pageSize`→`PageRequest`→Product Page→`content`와 metadata 분리→상품 card와 Paging 상태 갱신으로 왕복한다.
- **검색:** 기간·카테고리·mode·keyword→`SearchDto`→Specification 조립→Specification+Pageable Repository 조회→Product Page 응답으로 이어진다.
- 04-20의 control 준비, 04-21의 page 왕복·검색 frontend 준비, 04-22의 검색 backend 완성을 구분한다.

## 계층별 반복 역할

| 층 | 반복해서 맡은 역할 | 대표 예 |
|---|---|---|
| React component | 입력·클릭·loading/error·목록 state와 렌더링 | `SignupPage`, `ProductList`, `CartList`, `OrderList` |
| React Router | 사용자가 볼 화면 path와 component 선택 | Fruit·Member·Product·Cart·Order route |
| axios/axiosInstance | Spring API URL로 요청하고 body·parameter·Bearer token 전달 | 회원가입 POST, Cart PATCH, Product page GET |
| Controller | URL·HTTP method·request 변환·Validation·status/body 응답 | Member·Product·Cart·Order Controller |
| DTO | 화면/API에 필요한 데이터 모양을 Entity와 분리 | `LoginDto`, `CartItemDto`, `OrderDto`, `SearchDto` |
| Service | 저장 규칙·재고·파일·조건 조립·transaction 같은 업무 처리 | Product image, Cart 누적, Order 생성, 검색 조건 조립 |
| Repository/JPA | Entity 기준 저장·조회와 page/Specification 적용 | Member·Product·Cart·Order Repository |
| MySQL | 최종 행·관계·재고·검색 결과 확인 | JOIN 시나리오와 검색 SQL |

## 반복 혼동과 판단 기준

- **React Router path vs Spring API URL:** Router는 어떤 화면을 보여 줄지 정하고, axios URL은 어느 backend 자원을 요청할지 정한다. 문자열이 비슷해도 같은 routing이 아니다.
- **UI가 보임 vs 기능이 연결됨:** Cart 삭제·Order 버튼·Paging·검색 form은 먼저 화면에 나타난 뒤 후속 교시나 다음 날짜에 handler/API가 연결됐다. control 존재만으로 완료를 판단하지 않는다.
- **state/props vs 서버 데이터:** props는 부모가 전달하고 state는 component가 갱신한다. 어느 쪽도 DB 자체가 아니며 API 응답을 state에 넣어 화면이 바뀐다.
- **Entity vs DTO:** Entity는 JPA 관계·저장과 가깝고 DTO는 요청·응답 모양과 가깝다. CartItemDto와 OrderDetailDto가 관계형 Entity를 화면에 맞게 평탄화했다.
- **Controller vs Service vs Repository:** Controller는 HTTP, Service는 업무 규칙, Repository는 DB 접근이다. 수업 중 일부 Service가 다른 Repository를 직접 사용했더라도 세 역할을 한 단계로 합치지 않는다.
- **CartProduct vs OrderProduct:** 둘 다 Product와 quantity를 가지지만 CartProduct는 변경 가능한 장바구니 품목이고 OrderProduct는 주문에 포함된 품목이다. 주문 생성 시 Cart 품목을 그대로 보존하는 것이 아니라 OrderProduct를 새로 구성한다.
- **JWT와 사용자 객체:** token 문자열, token에서 만든 Security 인증 객체, React의 user state는 서로 다른 층이다.
- **Specification vs Pageable:** Specification은 WHERE 조건, Pageable은 page·size·sort다. 둘이 Repository의 한 조회에 함께 들어간다.
- **화면 type vs runtime 객체:** TypeScript interface는 React가 기대하는 data shape이며 Java Entity나 실제 JSON object 그 자체가 아니다. key 이름이 맞아야 응답을 안전하게 사용한다.

## 총정리 원본·직접 수업·후속 확장 경계

### 직접 수업

- 03-30~04-22 날짜 MD에 기록된 로컬 Spring Boot·React·MySQL 실습과 Fruit→Member/JWT→Product→Cart→Order→검색 기능이다.
- 총정리 원본 R19는 이 중 환경·Fruit·Member/JWT·Product·Cart를 길게 복습하지만 04-15 Cart 삭제에서 끝난다.

### 교안 보충

- IT 용어, Spring Boot, React, JWT, SQL/LIKE, CSR/SSR, Generic, Collection 같은 설명은 당일 구현을 이해하기 위한 보조 학습이다.
- 교안 용어를 본 사실과 프로젝트에서 해당 기술을 완성한 사실을 구분한다. 예를 들어 Querydsl API 용어를 봤지만 실제 검색 구현은 Specification이었다.

### 후속 과목과 프로젝트 확장

- [[summaries/2026-05-06-linux-subject-review|Linux 총정리]]: VM·SSH·파일·권한·Spring Boot 서버 실행·Docker·GitHub 협업으로 실행환경을 넓힌다.
- [[summaries/2026-05-08-aws-subject-review|AWS 총정리]]: VPC·EC2·RDS에서 애플리케이션과 DB를 클라우드 자원에 배치한다.
- [[concepts/ci-cd-automation|CI/CD 자동화]]: GitHub push에서 build·image·배포를 자동화한다.
- [[summaries/2026-05-14-passwordless-x1280-intro|Passwordless 시작]]: JWT 쇼핑몰 로그인과 별개의 인증 기술·서버를 학습한다.
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·Passwordless 가이드]]: 수업에서 익힌 계층과 인증·배포 지식을 실제 프로젝트 설계로 확장한다.
- 위 후속 내용은 FrontEnd_BackEnd 18일 직접 구현에 소급해 포함하지 않는다.

## 이전·다음 연결

- 이전 과목: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS·JavaScript DOM·Bootstrap·jQuery로 만든 화면이 이 과목에서 React component와 Spring API 화면으로 확장됐다.
- 다음 과목: [[summaries/2026-04-22-linux-install-ssh-cli|Linux 설치·SSH·CLI]]에서 로컬 IDE 안의 애플리케이션을 서버 운영 관점으로 옮기기 시작한다.
- 과목 내부의 세부 순서는 위 18개 날짜 Summary 링크를 따른다. 이 허브가 교시별 기록을 대신하지 않는다.

## 관련 페이지

- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/pagination-search|페이징과 검색]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`부터 `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`까지 날짜별 MD 18개
