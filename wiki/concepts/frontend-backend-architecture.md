---
title: Frontend/Backend 구조
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [frontend, backend, spring-boot, react]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png
status: growing
confidence: high
---

# Frontend/Backend 구조

## 정의

이 수업의 Frontend/Backend 구조는 사용자가 조작하는 [[entities/react|React]] 화면, HTTP 요청을 받는 [[entities/spring-boot|Spring Boot]] API, 업무 규칙을 처리하는 Service, JPA로 데이터를 읽고 쓰는 Repository, 그리고 [[entities/mysql|MySQL]]을 서로 다른 책임으로 나눈 구조다. React가 Spring 내부 계층을 직접 호출하는 것이 아니라 axios로 API 경계를 넘고, Spring은 결과를 주로 JSON으로 돌려준다.

## 왜 중요한가

UI&UX 과목에서는 브라우저 안의 정적 화면과 DOM 변경이 중심이었다. 2026-03-30부터는 React 5173, Spring Boot 9000, MySQL 3306이 각각 별도 실행 영역이 되었고, 한 기능을 고치려면 화면 state·요청 URL·Controller mapping·Service 규칙·Repository 조회·DB 행 중 어느 경계에서 문제가 생겼는지 추적해야 했다.

## 수업에서 처음 등장하고 확장된 날짜

| 날짜 | 구조가 확장된 지점 | 대표 artifact |
|---|---|---|
| [[summaries/2026-03-30-fullstack-environment-setup|03-30]] | Spring·React·MySQL을 따로 실행하고 후속 응답 자료인 `Fruit` 준비 | `application.properties`, Vite, `Fruit` |
| [[summaries/2026-03-31-spring-boot-controller-html|03-31]] | Spring 완성 HTML에서 REST JSON과 React Router 화면으로 전환 | `FruitHtmlController`, `FruitController`, `AppRoutes` |
| [[summaries/2026-04-01-react-router-spring-boot|04-01]] | axios 요청·CORS·state 반영으로 첫 실제 왕복 완성 | `Fruit.ts`, `FruitOne`, `FruitList`, `WebConfig` |
| [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]] | 화면 입력을 Controller→Service→Repository 저장 흐름으로 확장 | `SignupPage`, `MemberController`, `MemberService` |
| [[summaries/2026-04-10-react-event-spread-product-form|04-10]] | JSON form body·파일 문자열·Validation 오류 응답 경계 추가 | `ProductInsertForm`, `ProductController` |
| [[summaries/2026-04-14-cart-service|04-14]]~[[summaries/2026-04-15-cart-list-selection-typescript|04-15]] | 인증 사용자 Cart와 DTO 목록, 수량 PATCH로 관계형 데이터를 화면에 연결 | `CartService`, `CartItemDto`, `CartList` |
| [[summaries/2026-04-17-cart-total-array-some|04-17]]~[[summaries/2026-04-20-order-list-scenario|04-20]] | Order 조회·상태 변경·취소와 Product 재고를 왕복 | `OrderList`, `OrderDetailDto` |
| [[summaries/2026-04-21-product-pagination-search-react|04-21]]~[[summaries/2026-04-22-product-repository-pageable-search|04-22]] | page·검색 parameter와 `Page<Product>`·Specification 조회 연결 | `FieldSearch`, `SearchDto`, `PageRequest` |

## 대표 artifact가 보여 주는 계층

`프로그램 흐름 그림.png`의 Controller→Service→Repository→Database 흐름은 Spring 내부 책임을 보여 준다. 이 수업에서는 그 앞에 React component·Router·axios가 있고, 응답 뒤에는 React state·JSX 렌더링이 있다.

| 경계 | 맡는 일 | 수업의 실제 예 |
|---|---|---|
| React Router | 현재 주소에 맞는 화면 component 선택 | Fruit·Member·Product·Cart·Order 화면 path |
| axios / axiosInstance | Spring API 주소로 method·body·parameter·token 전달 | Fruit GET, 회원가입 POST, Cart PATCH |
| Controller | URL/method mapping, 요청 변환, Validation, HTTP 응답 | `MemberController`, `ProductController`, `CartController` |
| Service | 중복 확인·비밀번호 인코딩·파일·수량·재고·주문 같은 업무 규칙 | `MemberService`, `ProductService`, `CartService` |
| Repository/JPA | Entity를 기준으로 저장·조회·page 조건 적용 | Member·Product·Cart·Order Repository |
| MySQL | 회원·상품·관계·수량·재고의 지속 상태 | Workbench·JOIN·검색 시나리오로 확인 |

## 주소·상태·데이터 경계

- **React Router 주소와 Spring API 주소:** `/fruit`처럼 문자열이 같아도 Router path는 어떤 화면을 보여 줄지 고르고, axios의 9000번 URL은 어떤 Controller가 데이터를 처리할지 고른다. 자세한 구분은 [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]가 맡는다.
- **frontend state와 backend/DB 데이터:** `Fruit | null`, `Product[]`, `cartProducts`, `orders` state는 현재 화면이 들고 있는 값이다. API 응답으로 갱신되지만 DB 행 자체는 아니며, local 배열에서 항목을 지운 것만으로 DB가 삭제되는 것도 아니다.
- **JSON 경계:** Java 객체·목록·DTO·Page 응답은 HTTP body의 JSON 표현으로 전달되고 React는 `response.data` 또는 Page의 `response.data.content`를 읽는다. TypeScript type은 이 JSON을 다룰 때 기대하는 모양이지 runtime JSON 객체 자체가 아니다.
- **CORS 경계:** 04-01에는 React 5173에서 Spring 9000으로 보낸 Fruit 요청이 브라우저 정책에 막혔고 `WebConfig` 허용 뒤 통과했다. CORS는 Router나 파일 경로 오류가 아니다.
- **DTO 경계:** Cart의 JPA 관계를 그대로 화면에 노출하기보다 `CartItemDto`로 품목·가격·수량·재고를 평탄화했다. Entity와 DTO의 세부 구분은 [[comparisons/entity-vs-dto|Entity vs DTO]]가 맡는다.

## 실제 기능의 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| Fruit | `FruitOne`·`FruitList` 화면 진입 | Router가 화면 선택→axios GET→`FruitController` JSON→CORS 허용 | `Fruit`/`Fruit[]` state가 표로 렌더링 |
| Member | `SignupPage`의 name·email·password·address | POST→Validation·중복 확인→Service 인코딩→Repository 저장 | 필드 오류 Map 또는 가입 성공 응답 |
| Product | form state·route id·이미지 Data URL | POST/PUT→Controller 검증→Service 파일/도메인 처리→Repository | 오류 표시, 등록·수정·상세·삭제 결과가 화면에 반영 |
| Cart | 인증 사용자, Product id, quantity | Controller가 인증 email과 DTO 수신→Service가 Cart/CartProduct 처리 | `CartItemDto[]` 또는 수량·삭제 결과가 CartList state에 반영 |
| Order | 선택 Cart 품목 또는 상세 상품 한 건 | Service가 회원·상품·재고 확인→OrderProduct 구성→저장 | 역할별 주문 목록과 완료·취소 결과 표시 |
| 페이징·검색 | page·기간·카테고리·mode·keyword | Controller→SearchDto→Service 조건 조립→Repository의 Specification+Pageable | Product `content`와 page metadata가 각각 state에 반영 |

## 자주 헷갈리는 원인

- 이름이 같은 `ProductService`가 React 요청 보조 파일과 Spring 업무 Service에 각각 있을 수 있다. 파일 위치와 호출 방향으로 구분한다.
- React에 `Product` type이 있고 Spring에 `Product` Entity가 있어도 같은 객체가 아니다. JSON key가 맞아야 경계를 통과해 사용할 수 있을 뿐이다.
- React의 `isInvalid`·오류 state는 표시 장치이고, 가입·상품 저장 허용 여부는 Spring Validation과 업무 규칙이 다시 판단한다.
- Controller가 요청을 받았다는 사실과 Repository가 DB를 변경했다는 사실은 다르다. 중간 Service 분기와 실제 응답까지 확인해야 한다.
- 화면에 버튼·검색 control이 존재해도 handler·API·backend 소비가 연결되지 않았을 수 있다. Cart 삭제, Order 버튼, Paging, 검색은 날짜를 넘겨 단계적으로 완성됐다.

## 이전 개념과 이후 기능 연결

- 이전: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]의 HTML/CSS·JavaScript DOM·Bootstrap 화면이 React component와 state 기반 화면으로 확장됐다.
- 내부 확장: 최소 Fruit 왕복에서 Member/JWT, Product, Cart, Order, 검색으로 갈수록 같은 경계에 Validation·인증·DTO·재고·Page가 추가됐다. 반복 구현 순서는 [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]에서 설명한다.
- 이후: Linux는 로컬 애플리케이션을 서버에서 실행하고, AWS는 애플리케이션/DB를 클라우드 자원에 배치하며, CI/CD는 build·배포를 자동화한다. Passwordless와 중간 프로젝트는 인증 경계와 실제 프로젝트 조합을 확장한다.

## 직접 수업·교안 보충·후속 범위

- **직접 수업:** 03-30~04-22 로컬 React·Spring Boot·MySQL에서 Fruit→Member/JWT→Product→Cart→Order→검색을 구현한 범위다.
- **교안·그림 보충:** Frontend/Backend 역할과 프로그램 계층 그림은 구조를 이해하기 위한 보조 근거다. 날짜별 구현 순서보다 우선하지 않는다.
- **후속 범위:** [[summaries/2026-05-06-linux-subject-review|Linux]], [[summaries/2026-05-08-aws-subject-review|AWS]], [[concepts/ci-cd-automation|CI/CD]], [[summaries/2026-05-14-passwordless-x1280-intro|Passwordless]], [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트]]는 이 구조의 운영·배포·인증·프로젝트 확장이지 4과목 직접 구현이 아니다.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]

## 출처

- 2026-03-30~04-21의 위 frontmatter 날짜 MD와 `FrontEnd_BackEnd 총정리.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png`