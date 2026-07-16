---
title: 풀스택 프로젝트 흐름
created: 2026-07-06
updated: 2026-07-16
type: concept
tags: [spring-boot, react, frontend, backend, curriculum]
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
status: growing
confidence: high
---

# 풀스택 프로젝트 흐름

## 정의

풀스택 프로젝트 흐름은 한 번 만든 화면→API→업무 처리→DB→응답 패턴을 더 복잡한 도메인에 반복 적용하면서 기능을 확장하는 절차다. [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]가 계층과 경계를 설명한다면, 이 페이지는 이 수업에서 **무엇을 먼저 최소로 만들고 어떤 기능을 다음에 붙였는지**를 설명한다.

## 왜 중요한가

완성된 쇼핑몰 코드를 한꺼번에 보면 Router·state·Controller·JPA·JWT·재고가 섞여 보인다. 수업은 Fruit 최소 왕복으로 연결을 확인한 뒤 Member, Product, Cart, Order, 검색 순서로 한 가지 복잡성씩 추가했다. 이 확장 원리를 알면 새 기능도 화면·요청·계층·DB·응답·검증 단계로 쪼갤 수 있다.

## 처음 등장한 날짜와 전체 확장

| 단계 | 날짜 | 새로 추가한 복잡성 | 대표 artifact |
|---:|---|---|---|
| 1 | [[summaries/2026-03-30-fullstack-environment-setup|03-30]] | React·Spring·MySQL 실행환경과 공통 설정 | Vite, `application.properties`, `Fruit` |
| 2 | [[summaries/2026-03-31-spring-boot-controller-html|03-31]]~[[summaries/2026-04-01-react-router-spring-boot|04-01]] | Fruit 한 개/목록의 최소 JSON 왕복과 CORS | `FruitController`, `FruitOne`, `FruitList` |
| 3 | [[summaries/2026-04-02-react-bootstrap-homepage|04-02]]~[[summaries/2026-04-03-spring-member-seed-react-comments|04-03]] | JPA Entity·Validation·회원가입 저장 | `Member`, `SignupPage`, `MemberService` |
| 4 | [[summaries/2026-04-06-login-jwt-session-cookie|04-06]]~[[summaries/2026-04-07-member-api-string-token|04-07]] | 로그인 token 발급과 보호 요청 인증 | `LoginDto`, `JwtTokenProvider`, JWT Filter |
| 5 | [[summaries/2026-04-08-product-domain-oci|04-08]]~[[summaries/2026-04-13-product-detail-useeffect-service|04-13]] | Product seed·목록·삭제·등록·수정·상세와 파일 | `ProductList`, `ProductInsertForm`, `ProductUpdateForm` |
| 6 | [[summaries/2026-04-13-product-detail-useeffect-service|04-13]]~[[summaries/2026-04-15-cart-list-selection-typescript|04-15]] | 관계 Entity·인증 사용자 Cart·선택·수량·삭제 | `Cart`, `CartProduct`, `CartItemDto`, `CartList` |
| 7 | [[summaries/2026-04-16-cart-quantity-stock|04-16]]~[[summaries/2026-04-20-order-list-scenario|04-20]] | 주문 snapshot·재고 차감·목록·완료·취소 | `Order`, `OrderProduct`, `OrderList` |
| 8 | [[summaries/2026-04-20-order-list-scenario|04-20]] | 정적 Home 이미지를 DB 대표 상품으로 교체 | Product filter 응답, carousel |
| 9 | [[summaries/2026-04-21-product-pagination-search-react|04-21]]~[[summaries/2026-04-22-product-repository-pageable-search|04-22]] | Page metadata와 동적 검색 조건 | `PagingInfo`, `FieldSearch`, `SearchDto`, Specification |

## 반복되는 구현 절차

1. **기능의 화면과 주소를 정한다.** 메뉴·Router·component와 Spring endpoint를 별개로 배치한다.
2. **입력과 응답 모양을 정한다.** React state/type, request body·parameter, Java Entity/DTO 중 필요한 것을 구분한다.
3. **최소 요청을 먼저 연결한다.** Fruit GET처럼 한 번의 왕복이 통과하는지 axios·CORS·Controller 응답으로 확인한다.
4. **백엔드 책임을 나눈다.** Controller는 HTTP, Service는 업무 규칙, Repository는 JPA 조회·저장을 맡는다.
5. **결과를 화면 state에 반영한다.** 단건·배열·Page 응답을 구분하고 loading/error/빈 결과를 렌더링한다.
6. **실패와 권한을 추가한다.** Validation·중복·로그인·재고·상태 조건을 프론트 표시와 서버 판단으로 나눈다.
7. **DB와 화면을 함께 검증한다.** React에서 보이는 결과와 MySQL 행·관계·수량·재고가 모두 기대대로 바뀌었는지 확인한다.

## 기능 확장 원리

### Fruit → Member

Fruit는 DB 관계·인증 없이 JSON 한 개와 배열을 받는 최소 왕복이었다. Member에서는 같은 POST 왕복에 form 입력, Spring Validation, 이메일 중복 조회, 비밀번호 인코딩, Repository 저장이 추가됐다.

### Member → JWT

회원가입으로 저장된 사용자를 로그인 입력으로 사용하고 token을 발급했다. 이후 axiosInstance의 Bearer 전달과 Spring Filter·SecurityContext가 보호 API 앞에 추가되었다. 화면→API 구조를 바꾼 것이 아니라 요청마다 사용자 신뢰를 확인하는 단계가 늘어난 것이다.

### Product CRUD

Product는 목록 GET에서 시작해 삭제, 등록, 수정, 상세로 확장됐다. 등록은 빈 form과 POST, 수정은 route id·기존 GET·PUT이 필요했고, 이미지는 FileReader 문자열과 Spring 파일 저장이라는 별도 경계를 더했다. Product 세부 생명주기는 [[concepts/product-domain-flow|상품 도메인 기능 흐름]]이 맡는다.

### Product → Cart → Order

Cart는 Product를 복사한 단순 배열이 아니라 인증 사용자 Cart와 수량을 가진 CartProduct 관계였다. Order에서는 선택 Cart 품목을 OrderProduct로 새로 구성하고 재고 차감·Cart 품목 삭제를 함께 처리했다. 이후 목록 조회, 완료, 취소·재고 복원으로 상태 생명주기를 확장했다. 상세 내용은 [[concepts/shopping-cart-flow|장바구니 기능 흐름]]과 [[concepts/order-flow|주문 기능 흐름]]으로 분리한다.

### 전체 목록 → 대표 상품 → 페이징·검색

정적 Home carousel을 DB Product 응답으로 교체한 뒤, 전체 배열 응답을 `Page<Product>`로 바꿨다. 04-20에는 control을 준비했고, 04-21에는 page 요청·응답과 검색 form/request를 연결했으며, 04-22에는 검색 조건을 Service·Repository가 실제 소비했다. UI가 먼저 보였다는 사실과 backend 조회가 완성됐다는 사실을 구분한다.

## 대표 입력 → 처리 → 결과

| 반복 단위 | 입력 | 처리 | 결과 |
|---|---|---|---|
| 조회 | 화면 진입·route id·page/search state | GET→Controller→Service→Repository | 단건·배열·Page를 state에 저장해 렌더링 |
| 등록 | controlled form state | POST→Validation→Service 규칙→save | 성공 이동·목록 반영 또는 필드 오류 표시 |
| 수정 | route id와 기존값을 바꾼 state | GET으로 채움→PUT→기존 Entity에 반영 | DB·이미지·화면 값 변경 |
| 삭제/상태 변경 | 버튼 클릭과 대상 id | DELETE/PUT/PATCH→업무 조건 확인 | DB 변경 뒤 local 목록·합계·상태 갱신 |
| 관계 기능 | 로그인 사용자와 Product/Cart 품목 | DTO→Service의 관계 조회·재고 규칙→transaction | CartItem·OrderDetail 형태로 화면에 반환 |

## 실제 수업 예시

- 04-01 Fruit는 `response.data`를 `Fruit | null` 또는 `Fruit[]` state에 넣었다. 이 성공이 이후 도메인 API의 연결 점검 기준이 됐다.
- 04-03 회원가입은 오류가 있으면 필드 Map을 반환하고, 유효·비중복 회원만 role·등록일·인코딩된 비밀번호와 함께 저장했다.
- 04-10 Product 등록은 event의 name/value로 만든 객체와 FileReader의 image 문자열을 한 request body로 보냈다.
- 04-15 Cart 선택의 `checked`는 React state였지만 quantity PATCH는 서버 CartProduct를 바꿨다. 화면 상태와 지속 상태를 같은 것으로 보지 않았다.
- 04-21 검색 input은 request parameter까지 연결됐지만, 조건이 실제 Repository 조회에 적용된 시점은 04-22였다.

## 자주 헷갈리는 원인

- **Summary 허브와 이 페이지:** [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]는 18일 날짜 지도를 제공한다. 이 페이지는 날짜 내용을 다시 복제하지 않고 기능을 늘리는 공통 절차를 추출한다.
- **CRUD 순서:** Product는 Create→Read→Update→Delete 순서로만 배우지 않았다. seed·목록, 삭제, 등록, 수정·상세 순으로 실제 수업이 진행됐다.
- **표시와 완성:** form·버튼·Paging control이 먼저 만들어지고 handler·API·backend가 나중에 연결되는 경우가 많았다.
- **한 요청과 한 계층:** 요청 하나가 Controller만 거치는 것이 아니다. Validation·Service 분기·Repository 결과·응답과 React state 반영까지 닫혀야 한 기능 왕복이다.
- **총정리 원본 범위:** R19는 실제로 04-15 Cart 삭제까지 자세히 담고 있다. 04-16 이후 Order·대표 상품·검색은 고도화된 날짜 Summary와 각 날짜 raw의 흐름으로 보완하며 R19에 소급하지 않는다.

## 이전 개념과 이후 기능 연결

- 선행: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]의 화면·event·form이 React component/state로 이어지고, Java 객체·Oracle 관계형 DB 학습이 Spring Entity/JPA로 적용됐다.
- 과목 내부: React 기본기는 [[concepts/react-typescript-basics|React와 TypeScript 기본]], 입력은 [[concepts/react-form-state-event|React 폼 상태와 이벤트]], 조회 재실행은 [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]에서 자세히 본다.
- 후속: Linux·AWS·CI/CD는 이 로컬 프로젝트의 실행·배포·자동화를 확장한다. Passwordless와 중간 프로젝트는 JWT 쇼핑몰을 그대로 재현한 것이 아니라 별도 인증 기술과 실제 프로젝트 조합으로 확장한 범위다.

## 직접 수업·교안 보충·후속 범위

- **직접 수업:** 03-30~04-22의 환경→Fruit→Member/JWT→Product→Cart→Order→검색 구현 순서다.
- **교안 보충:** React event/Hook, Spring 계층/JPA, HTTP·JSON·CORS 용어는 날짜별 구현을 이해하는 보조 설명이다.
- **후속 범위:** [[summaries/2026-05-06-linux-subject-review|Linux]], [[summaries/2026-05-08-aws-subject-review|AWS]], [[concepts/ci-cd-automation|CI/CD]], [[summaries/2026-05-14-passwordless-x1280-intro|Passwordless]], [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트]]를 4과목 직접 구현에 섞지 않는다.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/pagination-search|페이징과 검색]]

## 출처

- 위 frontmatter의 날짜별 MD와 `FrontEnd_BackEnd 총정리.md`
- 04-16~04-22의 세부 날짜 귀속은 연결된 고도화 날짜 Summary를 우선 대조했다.