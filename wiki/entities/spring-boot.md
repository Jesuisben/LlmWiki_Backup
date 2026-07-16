---
title: Spring Boot
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [spring-boot, spring, backend]
sources:
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

# Spring Boot

## 정의

Spring Boot는 Spring 기반 애플리케이션을 실행 가능한 프로젝트로 구성하고, HTTP 요청 처리·업무 로직·DB 접근·보안 설정을 연결하는 백엔드 프레임워크다. 이 수업에서는 기능별 세부 원리보다 **Fruit에서 검색까지 커진 백엔드의 기술 이력**을 추적하는 중심 Entity다.

## 왜 중요한가

UI&UX 과목에서 브라우저 안에 머물던 화면이 이 과목에서는 Spring Boot API를 통해 MySQL의 데이터와 왕복했다. 같은 실행환경 안에서 Controller, Service, Repository, Security와 Member·Product·Cart·Order 도메인을 단계적으로 추가했기 때문에, 기능이 커져도 계층과 요청·응답 경계를 유지하는 법을 배울 수 있었다.

## 첫 등장: 2026-03-30 프로젝트 생성과 선택한 dependency

[[summaries/2026-03-30-fullstack-environment-setup|03-30]]에는 Spring Initializr에서 Java 21·Jar·Properties 프로젝트를 만들고 다음 항목을 **생성 시 선택**했다: Spring Boot DevTools, Lombok, Spring Data JPA, MySQL Driver, Thymeleaf, Spring Web, Spring Web Services, H2 Database. 이 목록은 초기 프로젝트에 넣은 dependency이지, 그날 모든 기능을 구현했다는 뜻이 아니다.

- 같은 날 실제로 확인한 것은 `CoffeeApplication` 실행, `server.port`, 정적 `index.html`, MySQL datasource/dialect 설정, Lombok 준비와 `Fruit`·`FruitController` 시작이다.
- Thymeleaf와 HTML `Model` 응답은 03-31에 사용했다.
- Member JPA·Validation·Security는 04-02~04-03, JWT dependency와 token 구성은 04-06~04-07에 별도로 확장했다.
- H2 Database와 Spring Web Services를 실제 기능에서 사용 완료했다는 근거는 날짜 원본에서 확인하지 못했다.

## 대표 artifact와 입력 → 처리 → 결과

| 구간 | 대표 artifact | 입력 | Spring Boot에서 한 처리 | 결과 |
|---|---|---|---|---|
| 03-30~04-01 Fruit | `CoffeeApplication`, `FruitHtmlController`, `FruitController`, `WebConfig` | 브라우저 또는 React의 GET | 정적/Thymeleaf HTML과 REST JSON을 구분하고 CORS 설정 적용 | HTML 또는 Fruit JSON이 화면에 표시됨 |
| 04-02~04-07 Member/JWT | `Member`, `MemberRepository`, `MemberService`, `MemberController`, `SecurityConfig` | 회원가입·로그인 JSON, 후속 Bearer 요청 | Validation, 중복 확인, 비밀번호 인코딩, 인증, token 생성·filter 검증 | 회원 저장, 상태별 응답, `SecurityContext` 인증 정보 |
| 04-08~04-13 Product | `ProductRepository`, `ProductService`, `ProductController` | 상품 조회·등록·수정·삭제 | JPA 조회/저장, 이미지 처리, Validation, HTTP 응답 | Product 목록·상세·오류 body와 DB 변경 |
| 04-13~04-15 Cart | `CartService`, `CartController`, `CartItemDto` | 인증 사용자와 상품·수량 | Cart 조회/생성, CartProduct 누적, DTO 변환, 수량·삭제 처리 | 사용자별 장바구니 목록과 변경 결과 |
| 04-16~04-20 Order | `OrderService`, `OrderController`, `OrderRepository` | 선택 품목 또는 즉시 주문, 상태 변경 | OrderProduct 구성, 재고 차감/복원, Cart 정리, 상태 처리 | 주문 저장·목록·완료·취소 결과 |
| 04-21~04-22 검색 | `SearchDto`, `ProductSpecification`, `PageRequest` | page·size·기간·카테고리·검색어 | Specification 조건과 sort/Pageable 조립, Repository 호출 | `Page<Product>` 응답을 작성한 구조 |

세부 HTTP·계층·Repository 원리는 각각 [[concepts/spring-boot-rest-api|Spring Boot REST API]], [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]], [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]에 위임한다.

## 실제 수업에서 확인된 완료 범위와 미확정 범위

### 확인된 구현

- Fruit HTML/JSON과 React CORS 왕복, Member 회원가입과 로그인, JWT filter 연결을 날짜별로 작성하고 테스트했다.
- Product CRUD·상세, Cart 추가/목록/수량/삭제, Order 생성/목록/완료/취소 코드를 기능별로 확장했다.
- 04-21에는 단순 Pageable 왕복과 MySQL LIMIT/OFFSET를, 04-22에는 검색 parameter→DTO→Specification→Pageable Repository 호출 코드를 작성했다.

### 실행 또는 결과가 미확정인 부분

- dependency를 선택했다는 사실만으로 H2·Web Services 사용 완료를 주장하지 않는다.
- 04-10 원본의 Product 저장 Service 반환값과 Controller의 성공 판정에는 불일치가 남아 있다.
- 04-17 Order Repository 선언명과 Service 호출명 일부가 맞지 않는다.
- 04-22 원본에는 `ProductRepository`의 `JpaSpecificationExecutor<Product>` 상속이 확인되지 않고, Product의 `LocalDate`와 검색 조건의 `LocalDateTime` 정합성도 미확정이다. 따라서 검색 연결 코드는 확인되지만 실제 API 성공 응답과 확정 건수까지 완료됐다고 단정하지 않는다.

## 자주 헷갈리는 원인

- **dependency 선택 vs 기능 구현:** 프로젝트 생성 화면에서 선택한 시점과 Controller·JPA·Security에서 실제 사용한 날짜는 다르다.
- **Spring Boot vs 계층:** Spring Boot가 Controller·Service·Repository를 한 역할로 만드는 것이 아니다. 각 계층의 책임은 분리된다.
- **코드 작성 vs runtime 성공:** annotation·method·Repository 호출이 보인다고 DB 결과와 API 성공까지 자동으로 증명되지는 않는다.
- **React role UI vs 서버 인가:** 화면에서 ADMIN 버튼을 보이는 것과 Spring Security endpoint authorization은 같은 증거가 아니다.

## 이전 개념과 이후 기능 연결

- 선행: [[entities/java|Java]] 클래스·인터페이스·예외, [[entities/oracle-database|Oracle Database]]의 SQL·무결성·정규화, [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]의 HTTP 화면 입력이 기반이 됐다.
- 과목 내부: [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]에 따라 Fruit 최소 왕복에서 Member/JWT→Product→Cart→Order→검색으로 반복 확장했다.
- 후속: Linux에서 jar 실행과 Docker, AWS에서 EC2/RDS, CI/CD에서 build·image·배포, Passwordless에서 별도 인증 서버 연동 대상으로 확장됐다. 이 후속 배포·인증은 03-30~04-22 직접 구현에 소급하지 않는다.

## 날짜별 학습 이력

- **03-30~04-01:** 생성·설정→HTML/JSON Controller→React CORS 첫 왕복.
- **04-02~04-07:** Member JPA/Validation/Security→회원가입→JWT 생성·검증·SecurityContext.
- **04-08~04-13:** Product Entity/Repository seed→조회·삭제·등록·수정·상세.
- **04-13~04-15:** Cart 관계→Service/Controller→DTO 목록·수량·삭제.
- **04-16~04-20:** Order/OrderProduct→생성·목록·상태·재고 복원, 대표 상품.
- **04-21~04-22:** Pageable page 왕복→Specification 검색 연결 코드와 MySQL 시나리오.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[queries/why-shopping-cart-order-flow-is-complex|장바구니와 주문 흐름은 왜 복잡한가]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`부터 `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`까지 날짜별 MD 18개