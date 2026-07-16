---
title: React와 TypeScript 기본
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png
status: growing
confidence: high
---

# React와 TypeScript 기본

## 정의

[[entities/react|React]]는 화면을 component로 나누고 props와 state 변화에 따라 JSX를 다시 렌더링한다. [[entities/typescript|TypeScript]]는 component가 받는 props, API 응답, 배열 원소, event 객체의 기대 모양을 type/interface로 표현해 작성 중의 잘못된 사용을 줄인다.

## 왜 중요한가

이 수업의 React 코드는 Fruit 한 개에서 Product·Cart·Order·검색 화면까지 계속 커졌다. 데이터가 한 건인지 배열인지, 아직 없는지, 부모가 준 값인지 화면이 바꾸는 값인지, 어떤 control의 event인지 구분하지 않으면 API가 맞아도 화면 코드가 흔들린다. TypeScript는 이 구분을 명시하지만 Java Entity나 runtime 검증을 대신하지는 않는다.

## 처음 등장한 날짜와 이후 확장

| 날짜 | 배운 기본기 | 대표 artifact |
|---|---|---|
| [[summaries/2026-03-31-spring-boot-controller-html|03-31]] | component 조립, JSX, 메뉴, Router로 화면 선택 | `App`, `MenuItems`, `FruitOne`, `FruitList`, `AppRoutes` |
| [[summaries/2026-04-01-react-router-spring-boot|04-01]] | interface, 단건/배열 state, props, optional chaining, `map` | `Fruit.ts`, `Fruit | null`, `Fruit[]`, `MenuItemsProps` |
| [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]] | JSX event·submit type과 조건부 오류 표시 | `SignupPage`, `React.SubmitEvent` |
| [[summaries/2026-04-10-react-event-spread-product-form|04-10]] | union event type, 객체 spread, 계산된 property, FileReader | `ProductInsertForm`, `ProductUpdateForm` |
| [[summaries/2026-04-13-product-detail-useeffect-service|04-13]] | route parameter, loading/product 조건부 렌더링, quantity event | `ProductDetail`, `useParams` |
| [[summaries/2026-04-14-cart-service|04-14]]~[[summaries/2026-04-15-cart-list-selection-typescript|04-15]] | typed props, nullable user, 객체 배열 state, 구조 분해 | `AppProps`, `User | null`, `CartProduct[]` |
| [[summaries/2026-04-21-product-pagination-search-react|04-21]] | Page 응답 type, optional chaining·nullish 기본값, 검색 state | `PagingInfo`, `SearchCondition`, `FieldSearch` |

## 핵심 기본기와 수업 맥락

### component와 JSX

`App`은 메뉴·route 영역·footer를 조립했고 Router는 주소에 맞는 `FruitOne`, `ProductList`, `CartList` 같은 component를 골랐다. JSX에서는 JavaScript 식을 중괄호로 넣고 배열 `map`으로 반복 행·card를 만들었다. component는 Spring Controller나 HTML 파일 이름의 다른 표현이 아니라 브라우저 화면을 구성하는 React 함수 단위다.

### props와 state

- **props:** 부모가 자식에게 전달하는 입력이다. 04-01의 `appName`, 04-15의 로그인 `user`, Paging component가 받은 `paging`·setter가 사례다.
- **state:** component가 현재 화면에서 관리하고 변경하는 값이다. `fruit`, `products`, `cartProducts`, `orders`, form 객체, loading/error, page·검색 조건이 사례다.
- `function App({ user }: AppProps)`의 구조 분해는 props에서 user를 꺼내는 문법이다. props를 state로 바꾸거나 객체를 복사하는 기능이 아니다.

### interface/type과 runtime 데이터

- 04-01의 `Fruit` interface는 Spring JSON을 React가 `id`, `name`, `price` 모양으로 사용할 것이라는 TypeScript 선언이다.
- `AppProps`의 `user: User | null`은 로그인 사용자 객체가 없을 수 있음을 표현한다.
- `Product`, `CartProduct`, `Order`, `PagingInfo`, `SearchCondition`은 화면별 데이터 구조를 나타낸다.
- TypeScript type/interface는 실행 전에 사라지는 개발 시점 정보다. Java class·JPA Entity·DTO도 아니고, 네트워크에서 도착한 runtime JSON 객체도 아니다. 서버 응답 key와 실제 값이 맞는지는 API 계약과 실행 결과로 확인해야 한다.

### 배열 state와 불변 갱신

Fruit 목록은 `Fruit[]`, 상품·장바구니·주문 목록도 각 type의 배열 state로 관리했다. `map`은 화면 반복뿐 아니라 Cart 품목의 `checked`나 quantity를 바꾼 새 배열을 만드는 데 사용했고, `filter`는 삭제·주문 성공 뒤 local 목록에서 항목을 제외하는 데 사용했다. setter에 기존 배열 자체를 직접 고쳐 넣는 대신 새 배열·객체를 만들어 React가 변경을 추적할 수 있게 했다.

### event type과 입력값

상품 form의 일반 control은 input·textarea·select를 합친 `React.ChangeEvent<...>`로 받고, 파일 control은 `React.ChangeEvent<HTMLInputElement>`로 좁혔다. Cart 수량 input의 `event.target.value`는 문자열이므로 `parseInt`를 거쳐 숫자 state/API 값으로 사용했다. 자세한 입력 처리 책임은 [[concepts/react-form-state-event|React 폼 상태와 이벤트]]로 분리한다.

### optional chaining과 조건부 렌더링

04-01의 `fruit?.id`는 초기 `null` state에서 속성 접근 오류를 피했고, Cart의 `user?.name`은 로그인 사용자 부재를 고려했다. 04-21의 `pageable?.pageNumber ?? 0`은 중간 객체가 없을 때 안전하게 접근한 뒤 null/undefined일 때 기본값을 선택했다. optional chaining은 로그인 권한 검사나 데이터 존재 검증을 자동으로 수행하지 않는다.

## 대표 입력 → 처리 → 결과

| 입력 | React/TypeScript 처리 | 결과 |
|---|---|---|
| Spring의 Fruit JSON object/array | `Fruit | null` 또는 `Fruit[]` state에 저장 | optional chaining 또는 `map`으로 표 렌더링 |
| 부모의 로그인 user | `AppProps`로 허용 모양을 고정하고 구조 분해 | Cart 제목·조건부 요청·역할별 화면에 사용 |
| Product form event | event type으로 target 범위를 정하고 객체 state 갱신 | typed request body 준비 |
| Cart 품목 배열 | `map`으로 checked/quantity를 바꾼 새 배열 생성 | checkbox·합계·수량 화면 갱신 |
| Spring Page 응답 | `content`와 metadata를 Product/Paging state로 분리 | 상품 card와 page control이 함께 갱신 |

## 실제 수업 예시

- Fruit 한 개는 처음에 없을 수 있어 `Fruit | null`, 목록은 빈 배열에서 시작하므로 `Fruit[]`로 나눴다.
- Product 등록/수정은 같은 Product 모양과 event handler를 공유하지만 수정 화면에는 route id와 기존값 조회가 추가됐다.
- CartList는 부모의 `user` props와 내부의 `cartProducts`·`orderTotalPrice` state를 함께 사용했다. 둘의 변경 주체가 다르다.
- 04-21에는 검색 조건 state가 바뀌면 ProductList 요청이 다시 실행되도록 dependency와 GET parameter를 맞췄다.

## 자주 헷갈리는 원인

- `interface Fruit`와 Java `Fruit` class의 필드가 비슷해도 같은 type system이나 같은 객체가 아니다.
- props로 받은 user를 component가 읽는 것과 Cart/Order API가 인증 사용자를 서버에서 확인하는 것은 별도 단계다.
- JSX의 `map`은 DB 조회가 아니다. 이미 state에 들어온 배열을 화면 element 배열로 바꾸는 처리다.
- optional chaining으로 오류가 사라져도 데이터 요청·인증·권한이 성공한 것은 아니다.
- `useEffect`, Router, form 처리까지 모두 React 기본기에 속하지만, 이 페이지는 문법과 데이터 표현만 맡는다. 재요청 조건과 form 입력 세부는 각각 별도 concept로 연결한다.

## 이전 개념과 이후 기능 연결

- 이전: UI&UX의 JavaScript 배열·객체·DOM event와 HTML form이 component·JSX·typed state로 이어졌다.
- 이후: 이 기본기는 Product CRUD, Cart 선택·수량, Order 목록, Paging/검색 화면의 공통 재료가 됐다.
- backend 연결: [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]에서 React type/state와 Java DTO/Entity·JSON 경계를 함께 본다.

## 직접 수업·교안 보충·후속 범위

- **직접 수업:** 03-31~04-21 React 화면에서 실제 사용한 component, JSX, props/state, interface/type, event type, 배열 state, optional chaining이다.
- **교안 보충:** React 교안의 event·spread·Hook 문법과 라우터 그림의 화면 안내 비유는 실제 코드를 이해하는 보조 근거다.
- **후속 범위:** Linux·AWS·CI/CD는 React/TypeScript 문법 수업이 아니라 완성 애플리케이션의 운영·배포 확장이다. Passwordless와 중간 프로젝트에서 React state가 다시 쓰여도 4과목 직접 구현과 구분한다.

## 관련 페이지

- [[summaries/2026-04-01-react-router-spring-boot|04-01 React axios와 Spring CORS 연결]]
- [[summaries/2026-04-15-cart-list-selection-typescript|04-15 장바구니 목록과 TypeScript props]]
- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[comparisons/props-vs-state|props vs state]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]

## 출처

- 위 frontmatter의 날짜별 MD, `FrontEnd_BackEnd 총정리.md`, React 교안과 라우터 설명 그림