---
title: props vs state
created: 2026-07-02
updated: 2026-07-16
type: comparison
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: high
---

# props vs state

## 비교 목적

props와 state는 모두 component가 읽는 값이지만 **소유권과 변경 경로**가 다르다. 수업에서는 Product form, Cart 선택·수량, Paging/Search가 API 데이터와 함께 등장해 “서버에서 온 값=props”, “DB에 저장된 값=state”처럼 잘못 외우기 쉬웠다.

이 페이지는 props/state의 선택 기준만 다룬다. form event와 controlled input은 [[concepts/react-form-state-event|React 폼 상태와 이벤트]], React/TypeScript 표현 도구 전체는 [[concepts/react-typescript-basics|React와 TypeScript 기본]]에 맡긴다.

## 실제 수업에서 비교가 필요해진 이력

- **2026-04-01:** 부모가 `appName`을 `MenuItems`에 props로 전달하는 예와 Fruit 조회값을 `useState`로 관리하는 예가 같은 날 등장해 첫 구분이 필요해졌다.
- **2026-04-06:** LoginPage가 email·password·errors를 local state로 관리하면서 `onLogin` callback을 props로 받아, callback 전달과 state 소유권을 함께 비교하게 됐다.
- **2026-04-10:** Product 등록·수정 form에서 input event가 `product` state와 `errors` state를 바꾸고, 수정 화면은 `user`를 props로 받았다.
- **2026-04-14~15:** Cart 화면은 부모가 준 `user` props를 읽고, API로 받은 Cart 목록·checked·합계·quantity를 local state로 관리했다.
- **2026-04-17:** Cart에서 선택된 state를 주문 요청 object로 만들고, OrderList는 `user` props와 loading/error/orders state를 함께 사용했다.
- **2026-04-20~21:** `Paging` component가 `paging`과 `setPaging`을 props로 받고, 부모 ProductList는 paging·searchCondition state를 소유했다.

## 한눈에 보기

| 판단 항목 | props | state |
|---|---|---|
| 소유자 | 부모 component | 해당 state를 선언한 component |
| 전달·변경 | 부모가 자식에게 전달, 자식이 직접 재할당하지 않음 | setter로 다음 값을 예약해 갱신 |
| 수업 예 | `appName`, `user`, `paging`, `setPaging` | Product form, Cart 목록·checked·합계·quantity, loading/error/orders, searchCondition |
| component 간 계약 | TypeScript Props type/interface로 기대 모양 선언 | `useState<T>`로 local 값 모양 선언 |
| API·DB와의 관계 | 서버에서 왔다는 이유만으로 props가 되지 않음 | state가 바뀐다는 이유만으로 DB가 바뀌지 않음 |
| 결과 | 자식 rendering·handler에 입력 제공 | setter 뒤 재렌더링에 사용할 component 값 변경 |

## 실제 선택 상황 1 — Product 등록·수정 form

### 입력 → 처리 → 결과

1. input의 `event.target`에서 `name`과 `value`를 읽는다.
2. `setProduct({ ...product, [name]: value })` 형태로 Product form state를 갱신한다.
3. file input은 `FileReader` 결과를 Product state에 넣는다.
4. submit handler가 현재 state를 API 요청 body로 보낸다.
5. Spring 검증 오류가 오면 `setErrors(...)`로 오류 state를 갱신하고, 성공하면 초기 state로 되돌린 뒤 화면을 이동한다.

여기서 `setProduct`는 state setter이고 API 호출 함수가 아니다. Product state는 요청 body를 만드는 frontend 값이며, Spring Service·Repository가 DB에 저장하는 단계와 분리된다. 수정 화면의 `user` props는 화면에 전달된 로그인 사용자이고 Product form state의 소유자가 아니다.

## 실제 선택 상황 2 — Cart 선택과 수량

### 부모 입력과 local 변경

- `CartList`는 `user`를 props로 받아 어떤 사용자의 Cart를 조회할지 판단한다.
- 조회 응답은 `setCartProducts(response.data || [])`를 거쳐 Cart 목록 state가 된다.
- 전체/개별 checkbox handler는 `setCartProducts(previous => ...)`로 각 항목의 `checked`를 바꾼다.
- 합계는 checked와 quantity를 읽어 `orderTotalPrice` state에 반영한다.
- quantity 변경은 먼저 local state 보정이 나타나고, 실제 DB 변경은 별도 PATCH 요청과 Spring Controller→Service→Repository 흐름이 있어야 일어난다.

따라서 `checked`는 화면 선택 state이지 DB의 CartProduct field라고 단정할 수 없다. 반대로 quantity는 화면 state와 backend 저장값 양쪽에 나타나지만, setter와 API/Repository는 같은 동작이 아니다.

## 실제 선택 상황 3 — Paging component와 callback/setter props

ProductList가 `paging` state를 소유하고 Paging component에 `paging`과 `setPaging`을 props로 전달했다. 자식은 전달받은 setter를 호출할 수 있지만, 이는 “자식이 props를 직접 수정”하는 것이 아니다. 부모가 소유한 state의 갱신 함수를 계약으로 내려준 것이다.

검색에서도 `searchCondition` state가 바뀌었다는 사실, axios 요청에 조건이 실렸다는 사실, Spring이 조건을 소비했다는 사실은 날짜별로 따로 확인해야 한다. 04-21에는 frontend state·request와 개별 Specification 준비가, 04-22에는 Service 조건 조립과 Repository 호출 코드가 이어졌다.

## 함께 사용하는 관계

- 부모는 자신의 state 값을 props로 내려줄 수 있다.
- 부모는 handler나 setter callback을 props로 내려 자식 event를 부모 state 변경으로 연결할 수 있다.
- 04-06의 `onLogin` callback은 자식 LoginPage가 부모의 로그인 처리 함수를 호출하는 계약이다. callback 자체가 state이거나 자식이 부모 state를 직접 수정하는 것은 아니다.
- API 응답은 받은 즉시 “state라는 종류의 데이터”가 되는 것이 아니라 setter에 전달될 때 해당 component의 state 값이 된다.
- state를 API body/query로 보낼 수 있지만 backend 저장은 Controller·Service·Repository가 별도로 처리한다.

## 확인된 구현 범위와 실행 미확정 범위

- 확인: 04-01 `appName` props와 Fruit state, 04-10 Product/error state, 04-15 user props와 Cart 선택·합계·수량 state.
- 확인: 04-06 LoginPage의 `onLogin` callback prop과 email·password·errors local state가 같은 component에 함께 선언됨.
- 확인: 04-20 Paging의 `paging`·`setPaging` props, 04-21 paging/searchCondition state와 요청 parameter.
- 확인: Cart quantity setter와 PATCH API가 별도 단계로 작성됨.
- 미확정: frontend의 `user.role`·버튼 표시가 server authorization을 완성한다는 주장.
- 미확정: 모든 state 변경이 DB에 저장되거나 모든 server data가 state로 영구 보존된다는 주장.

## 자주 헷갈리는 원인과 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| props = server data | 어느 component가 값을 소유하고 누가 누구에게 전달했는지 본다. |
| state = DB data | setter 뒤 React 값만 바뀌는지, 별도 API·backend 저장까지 연결됐는지 본다. |
| setter = callback = API | setter는 state 갱신 함수, callback은 전달 가능한 함수 관계, API 호출은 HTTP 요청이다. |
| 자식이 setter props를 호출하면 props 수정이다 | 부모가 소유한 state 갱신 함수를 자식에게 위임한 것이다. |
| TypeScript Props type이 runtime 값을 만든다 | Props type은 compile-time 계약이고 실제 값은 부모가 전달한다. |
| checked와 quantity는 모두 DB field다 | checked는 수업의 UI 선택값이고 quantity만 별도 backend 변경 흐름이 확인된다. |

## 선행 개념과 후속 기능 경계

- 선행: [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- 조회 시점: [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- 도메인 확장: [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/pagination-search|페이징과 검색]]
- 날짜 Summary: [[summaries/2026-04-01-react-router-spring-boot|04-01 Fruit 연동]], [[summaries/2026-04-10-react-event-spread-product-form|04-10 Product form]], [[summaries/2026-04-15-cart-list-selection-typescript|04-15 Cart 선택]], [[summaries/2026-04-21-product-pagination-search-react|04-21 페이징·검색]]
- Linux/AWS/CI/CD는 React build와 API를 실행·배포하는 후속 환경이고, Passwordless·중간 프로젝트의 인증 상태는 기존 props/state 규칙 위에 추가되는 별도 통합 범위다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
