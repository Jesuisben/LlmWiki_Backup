---
title: TypeScript
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [typescript, react, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: high
---

# TypeScript

## 정의

TypeScript는 JavaScript 코드에 compile-time type 검사를 추가해 변수·함수·객체·component props가 기대하는 모양을 미리 선언하는 언어다. 실행 중 전달되는 JSON을 바꾸는 기술이 아니라, React 코드를 작성하고 컴파일할 때 잘못된 사용을 찾기 위한 도구다.

## 왜 중요한가

Fruit 한 개에서 Product·Cart·Order 배열과 Page metadata까지 API 데이터가 커지면서, 화면이 어떤 field를 기대하는지 이름과 타입으로 추적할 필요가 생겼다. props·state·event callback의 계약도 명시하여 component 사이 전달과 입력 처리를 읽기 쉽게 만들었다.

## 첫 등장과 실제 사용 시작

- [[summaries/2026-03-30-fullstack-environment-setup|03-30]] Vite 생성 시 `TypeScript + React Compiler` variant를 선택했다. 이는 TypeScript 프로젝트 기반을 만든 시점이다.
- [[summaries/2026-04-01-react-router-spring-boot|04-01]] `Fruit.ts`의 `interface Fruit`, `MenuItemsProps`, `useState<Fruit | null>`와 `Fruit[]`, optional chaining을 사용하면서 데이터·props·state 타입을 실제 화면에 적용했다.

## 대표 artifact와 입력 → 처리 → 결과

| 날짜·기능 | 대표 type/interface | 입력 | compile-time에서 표현한 계약 | runtime 결과와의 관계 |
|---|---|---|---|---|
| 04-01 Fruit | `Fruit`, `MenuItemsProps` | Fruit JSON, app name props | Fruit field, nullable state, 배열 state | JSON을 type이 생성하지 않으며 응답 key가 맞아야 화면에서 사용 가능 |
| 04-03 Signup | `React.SubmitEvent` | form submit event | handler가 받는 event 종류 | `preventDefault()` 등 runtime event 동작은 React/브라우저가 수행 |
| 04-06 Login | `User`, `LoginResponse`, `Props` | login 응답과 callback | user field·role union·token 포함 응답·callback signature | response를 token과 userData로 분리해 state/localStorage에 저장 |
| 04-08~04-10 Product | `Product`, `ProductProps`, form props, `React.ChangeEvent` | Product JSON·form control event | Product field와 입력 element event 종류 | Java Product Entity와 이름을 맞췄지만 같은 객체는 아님 |
| 04-14~04-15 Cart | `CartProduct`, `AppProps` | Cart item 배열·user props | 품목 field·checked·nullable user·`CartProduct[]` state | Spring `CartItemDto` JSON을 화면 배열로 사용 |
| 04-17 Order | `Order`, `OrderItem` | 주문 목록 JSON | 주문·주문품목 배열 구조 | Java DTO/Entity와 별도 frontend 선언 |
| 04-20~04-21 Page/Search | `PagingInfo`, `SearchCondition`, `Props` | Page metadata·검색 control | page 상태, 검색 field, setter/dispatch props | `content`, `totalElements`, `totalPages`, `pageable?.pageNumber`를 runtime 응답에서 읽음 |

## 실제 수업에서 확인된 범위

### 확인된 사용

- `interface`와 `type`을 모두 사용해 API data shape와 component props를 선언했다.
- `Fruit[]`, `Product[]`, `CartProduct[]`, `Order[]`처럼 배열 state를 확장했다.
- `React.SubmitEvent`, `React.ChangeEvent`, `React.MouseEvent`와 callback/dispatch props를 입력 흐름에 적용했다.
- `user?.role`, `pageable?.pageNumber`, null union과 `??`를 이용해 값이 없을 수 있는 상태를 다뤘다.
- Paging/Search에서는 Product 목록뿐 아니라 Page metadata와 검색 조건 state까지 타입 범위가 넓어졌다.

### 확인하지 못한 것

- type/interface가 runtime JSON을 검증하거나 변환했다는 근거는 없다.
- TypeScript `Product`·`CartProduct`·`Order`가 Java Entity/DTO 클래스 또는 MySQL table과 동일한 객체라는 뜻이 아니다.
- 04-21 frontend type과 parameter가 작성됐다는 사실만으로 04-22 검색 API runtime 성공까지 확정되지 않는다.

## 자주 헷갈리는 원인

- **모양이 같음 vs 같은 객체:** TypeScript type, runtime JSON, Java DTO/Entity, DB 행은 서로 다른 계층이다. field 이름을 대응시켜 왕복할 뿐이다.
- **interface vs table schema:** `interface Product`는 DB 제약조건이나 저장 구조를 만들지 않는다.
- **optional chaining vs optional field:** `user?.role`은 null/undefined 접근을 안전하게 하는 연산이고, field 선언 자체를 optional로 바꾸는 설명과 다르다.
- **type 검사 vs 업무 검증:** 숫자 타입이라고 재고 범위가 검증되는 것이 아니다. 재고·Validation은 React handler나 Spring Service/Validation이 맡는다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/java-basic-types|Java 기본 자료형]]과 Java class 학습이 타입을 읽는 기반이 됐지만, Java 정적 타입과 TypeScript frontend type의 실행환경은 다르다.
- 과목 내부: [[concepts/react-typescript-basics|React와 TypeScript 기본]]의 표현 도구가 [[concepts/react-form-state-event|React 폼 상태와 이벤트]], Product·Cart·Order·Paging 기능에 누적됐다.
- 후속: 중간 프로젝트에서도 API contract를 표현하는 도구로 확장할 수 있지만, Linux/AWS/CI/CD/Passwordless의 서버·배포·인증 기술 자체로 소급하지 않는다.

## 날짜별 학습 이력

- **03-30:** Vite TypeScript+React 기반 선택.
- **04-01:** Fruit interface, props type, nullable/array state, optional chaining.
- **04-03~04-06:** submit event, User/LoginResponse, callback props와 role union.
- **04-08~04-10:** Product data·props와 입력 element event type.
- **04-14~04-17:** CartProduct·user props·배열 state에서 Order/OrderItem 배열로 확장.
- **04-20~04-21:** PagingInfo·SearchCondition·setter props와 Page metadata 처리.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[entities/react|React]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/props-vs-state|props vs state]]
- [[concepts/pagination-search|페이징과 검색]]

## 출처

- frontmatter에 선언한 03-30·04-01·04-03·04-06·04-08~04-10·04-14~04-15·04-17·04-20~04-21 날짜 MD