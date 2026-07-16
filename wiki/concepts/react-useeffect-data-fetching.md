---
title: React useEffect와 데이터 요청
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
status: growing
confidence: high
---

# React useEffect와 데이터 요청

## 정의

`useEffect`는 React가 화면을 렌더링한 뒤 API 요청처럼 렌더링 계산 밖에서 일어나는 side effect를 실행하는 Hook이다. dependency 배열은 effect를 다시 평가할 값의 목록이고, 실제 API 호출 여부는 effect 본문·조건문·요청 함수 호출까지 함께 봐야 한다.

## 왜 중요한가

이 수업의 조회 화면은 처음 진입할 때 데이터를 받아야 했고, 상품 id·로그인 user·page·검색 조건이 바뀌면 최신 조건으로 다시 요청해야 했다. 반대로 등록·수량 변경·삭제처럼 사용자가 버튼이나 submit을 눌러 실행하는 요청은 effect가 아니라 event handler가 담당했다. 두 실행 시점을 섞으면 중복 요청·오래된 화면·아직 연결되지 않은 control을 완성 기능으로 오해하기 쉽다.

## 처음 등장한 날짜와 이후 확장

| 날짜 | effect가 맡은 조회 | dependency·실행 조건 | 대표 artifact |
|---|---|---|---|
| [[summaries/2026-04-01-react-router-spring-boot|04-01]] | Fruit 한 개와 목록 GET | 빈 배열로 첫 화면 진입 뒤 한 번 | `FruitOne`, `FruitList` |
| [[summaries/2026-04-10-react-event-spread-product-form|04-10]]~[[summaries/2026-04-13-product-detail-useeffect-service|04-13]] | Product 수정 기존값·상세 GET | route id와 사용자 조건을 확인해 id 변경 시 조회 | `ProductUpdateForm`, `ProductDetail` |
| [[summaries/2026-04-14-cart-service|04-14]]~[[summaries/2026-04-15-cart-list-selection-typescript|04-15]] | 인증 사용자 Cart 목록 GET | user와 user id가 있을 때 호출, user 변화에 연동 | `CartList`, `fetchCartProducts` |
| [[summaries/2026-04-17-cart-total-array-some|04-17]] | 역할별 PENDING Order 목록 GET | 로그인 user의 id·role을 요청에 사용 | `OrderList`, loading/error/orders state |
| [[summaries/2026-04-21-product-pagination-search-react|04-21]] | Product Page·검색 parameter GET | page 번호와 검색 조건 변화에 따라 재요청 | `ProductList`, `PagingInfo`, `SearchCondition` |

## 실행 시점과 dependency 읽는 법

### dependency가 없거나 빈 배열인 경우

04-01 Fruit는 화면이 처음 나타난 뒤 Spring 데이터를 한 번 읽는 데 빈 dependency 배열을 사용했다. Product 초기 목록도 같은 형태로 시작했다. 빈 배열이라는 문법만 보고 “어떤 상황에서도 전체 생명주기 동안 정확히 한 번”이라고 외우기보다, 해당 component가 mount될 때 effect가 실행된다는 수업 맥락으로 이해한다.

### 값이 있는 dependency 배열

- Product 수정·상세의 route id가 달라지면 새 상품을 조회해야 한다.
- CartList는 user가 있고 id가 존재하는지 effect 안에서 확인한 뒤 목록 함수를 호출했고 user 변화와 연결했다.
- ProductList는 `paging.pageNumber`가 바뀌면 page parameter가 달라져 재요청했다.
- 검색에서는 기간·카테고리·mode·keyword state를 GET parameter와 dependency에 함께 넣었다.

dependency 배열에 값이 있다는 사실만으로 API가 호출되는 것은 아니다. React가 effect를 실행한 뒤 본문 조건이 false이면 요청 함수를 부르지 않을 수 있고, dependency가 바뀌어도 실제 request parameter에 반영하지 않으면 같은 조건을 다시 보낼 수 있다.

## 날짜별 데이터 요청 흐름

### Fruit: 최소 조회

- **입력:** `FruitOne` 또는 `FruitList` component가 mount됨.
- **처리:** effect가 axios GET을 실행하고 Spring `FruitController`의 JSON object/array를 받음.
- **결과:** `Fruit | null` 또는 `Fruit[]` state를 갱신하고 optional chaining·`map`으로 표시함.
- CORS가 막혔을 때 effect 자체가 잘못된 것이 아니라 React 5173→Spring 9000 요청 허용 경계가 문제였다.

### Product: route id에 따른 기존값·상세 조회

- **수정 화면:** route id로 기존 Product를 GET하고 product state에 넣어 form을 채웠다. 그 뒤 submit handler의 PUT은 effect가 아니라 사용자 event로 실행됐다.
- **상세 화면:** Product card에서 온 id로 GET하고 loading/product state에 따라 상세를 표시했다.
- id가 dependency라는 설명과 실제 GET이 다시 나가는 것은 effect 본문의 요청 호출이 함께 있을 때 성립한다.

### Cart: 로그인 사용자 조건과 목록

CartList effect는 user와 id가 있을 때 `fetchCartProducts`를 실행했다. 응답 배열은 `cartProducts` state에 들어갔다. checkbox 선택은 local event handler, quantity PATCH·삭제 DELETE는 사용자 action handler이므로 초기 목록 effect와 실행 계기가 다르다.

### Order: loading/error/orders 반영

04-17의 OrderList는 로그인 user의 id·role로 역할별 PENDING 목록을 GET했다. 요청 전후 loading을 관리하고 실패는 error state, 성공은 orders state에 반영한 뒤 초기 화면에서 상태별 UI를 나눴다. 04-20의 완료 PUT·취소 DELETE는 버튼 handler이고, 성공 뒤 local orders 배열에서 항목을 제거했다.

### 페이징·검색: UI 준비와 실제 재요청

- 04-20에는 Paging control과 state를 만들었지만 Product GET에 page parameter가 아직 연결되지 않았다.
- 04-21에는 `paging.pageNumber` 변화가 effect 재실행→page parameter GET→Spring Page 응답으로 이어졌다.
- 같은 날 검색 input이 `searchCondition`을 바꾸고 네 값을 dependency와 GET parameter에 넣어 frontend 요청까지 연결했다.
- 검색 parameter를 backend가 실제 조건 조회에 소비한 것은 04-22다. effect가 다시 호출된 것과 검색 결과가 DB 조건으로 달라진 것은 별도 완료 단계다.

## 대표 입력 → 처리 → 결과

| 입력/변화 | effect 내부 처리 | state와 화면 결과 |
|---|---|---|
| Fruit 화면 첫 진입 | axios GET→JSON object/array 수신 | fruit/fruitList state→표 |
| Product route id 변경 | 로그인·id 조건 확인→단건 GET | 기존 수정 form 또는 상세 화면 갱신 |
| 로그인 user 변경 | user/id가 있을 때 Cart 목록 GET | CartProduct 배열 표시 |
| Order 화면 진입과 user role | 역할별 PENDING GET | loading/error/orders 분기 |
| pageNumber 변경 | 새 page parameter로 Product GET | `content`와 metadata를 각각 갱신 |
| 검색 조건 변경 | 검색 parameter를 포함한 Product GET | 04-21 요청 재실행, 04-22 backend 조건 결과 반영 |

## loading·error·state를 함께 보는 이유

API 요청은 즉시 결과를 주지 않는다. ProductDetail과 OrderList처럼 아직 결과가 없는 시점, 실패한 시점, 성공해 데이터가 있는 시점을 state로 나눠야 JSX가 올바른 화면을 고른다.

- loading은 “데이터 없음”과 “아직 기다리는 중”을 구분한다.
- error는 console 기록만이 아니라 사용자에게 실패 상태를 표시할 때 사용한다.
- 성공 응답은 단건·배열·Page인지에 맞춰 state에 저장한다. Page 응답은 body 전체가 배열이 아니므로 `content`와 metadata를 분리했다.

## 자주 헷갈리는 원인

- `useEffect`가 화면을 직접 그리는 것이 아니다. effect가 state를 바꾸면 React가 그 state로 다시 렌더링한다.
- dependency 값이 있다고 무조건 네트워크 요청이 발생하지 않는다. effect 본문의 조건과 요청 함수 호출을 확인해야 한다.
- 반대로 버튼 handler가 POST/PATCH/DELETE를 호출하는 기능을 effect 기반 요청이라고 부르면 실행 계기를 놓친다.
- setter를 dependency로 넣을 필요가 있다는 근거는 이 수업에 없다. 실제로 변화 조건으로 사용한 id·user·page·검색 state를 본다.
- 검색 control이 존재하거나 request가 재실행되는 것만으로 backend 검색 완성이라고 할 수 없다. Controller·Service·Repository가 parameter를 소비해야 한다.
- React `ProductService`와 Spring `ProductService`가 이름이 같아도 effect가 호출하는 것은 HTTP 요청 함수이고 Spring Service는 Controller 뒤의 업무 계층이다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/react-typescript-basics|React와 TypeScript 기본]]의 component·state·type이 있어야 effect 결과를 저장하고 렌더링할 수 있다.
- form과 구분: [[concepts/react-form-state-event|React 폼 상태와 이벤트]]는 사용자 입력·submit·change를, 이 페이지는 화면 진입과 dependency 변화에 따른 조회를 맡는다.
- 이후: Product·Cart·Order·페이징·검색의 조회 화면이 같은 패턴을 확장했다. backend 검색 조건은 [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]에서 이어진다.

## 직접 수업·교안 보충·후속 범위

- **직접 수업:** 04-01 Fruit, 04-10~13 Product, 04-14~15 Cart, 04-17 Order, 04-21 page/search 요청에서 사용한 effect와 state 흐름이다.
- **교안 보충:** React 교안의 function/dependency 설명은 실제 dependency 선택을 이해하는 보조 근거다.
- **후속 범위:** data-fetching library, cleanup·구독, 운영 caching 전략은 이 raw의 직접 실습 근거가 없다. Linux·AWS·CI/CD는 API 실행·배포 환경의 확장이고 Passwordless·중간 프로젝트 polling은 별도 후속 기능이다.

## 관련 페이지

- [[summaries/2026-04-01-react-router-spring-boot|04-01 React axios와 Spring CORS 연결]]
- [[summaries/2026-04-13-product-detail-useeffect-service|04-13 상품 상세와 useEffect]]
- [[summaries/2026-04-21-product-pagination-search-react|04-21 React 상품 페이징과 검색 준비]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[concepts/pagination-search|페이징과 검색]]

## 출처

- 위 frontmatter의 04-01·04-10·04-13·04-14·04-15·04-17·04-21 날짜 MD, `FrontEnd_BackEnd 총정리.md`, React 교안