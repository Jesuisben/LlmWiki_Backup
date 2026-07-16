---
title: 장바구니 기능 흐름
created: 2026-07-06
updated: 2026-07-16
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# 장바구니 기능 흐름

## 정의

이 수업의 장바구니 흐름은 Product 상세에서 선택한 상품과 수량을 로그인 회원의 Cart에 넣고, `CartProduct` 관계를 통해 같은 상품의 수량을 누적한 뒤, 목록 DTO·checkbox 선택·합계·수량 변경·재고 검증·삭제를 거쳐 **선택한 품목만 주문 요청으로 넘기는 과정**이다. Order가 생성된 뒤의 상태·재고·목록 책임은 [[concepts/order-flow|주문 기능 흐름]]으로 넘긴다.

## 왜 중요한가

Cart는 단순 Product 배열이 아니다. 회원별 Cart, Cart와 Product 사이의 중간 Entity, 각 관계가 가진 quantity, 화면에서만 존재하는 checked state, 입력 DTO와 출력 DTO가 동시에 등장한다. 이 값들의 수명과 저장 위치를 구분해야 화면 선택을 DB 관계로 오해하거나, Cart 삭제와 주문 생성을 같은 작업으로 합치지 않는다.

## 날짜별 실제 확장

| 날짜 | Cart 단계 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13]] | Product 상세의 quantity·추가 요청, Cart/CartProduct 관계와 입력 DTO 준비 | `ProductDetail`, `Cart`, `CartProduct`, `CartProductDto` |
| [[summaries/2026-04-14-cart-service|2026-04-14]] | 인증 사용자 Cart 조회/생성, 같은 상품 수량 누적, 목록 DTO와 React 표 | `CartService.addProductToCart`, `CartController`, `CartItemDto`, `CartList` |
| [[summaries/2026-04-15-cart-list-selection-typescript|2026-04-15]] | 전체/개별 선택·합계, 수량 PATCH·재고 검증 초안, 삭제 backend 기반 | `toggleAllCheckBox`, `toggleCheckBox`, `changeQuantity`, `orderTotalPrice` |
| [[summaries/2026-04-16-cart-quantity-stock|2026-04-16]] | 연결 Product 재고로 수량 보정, React 삭제 완성, 선택 Cart 주문 함수·API 작성 | `deleteCartProduct`, 수정된 `CartProductService`, `makeOrder`, `OrderService.createOrder` |
| [[summaries/2026-04-17-cart-total-array-some|2026-04-17]] | stock을 DTO/화면에 추가하고 quantity 0을 `some`으로 차단, 실제 주문 버튼 연결 | `stock`, `hasInvalid`, `onClick={makeOrder}`, 공용 오류 Alert |

## 관계와 데이터 모양

### Entity 관계

- Member–Cart는 1:1, Cart–CartProduct는 1:N, CartProduct–Product는 N:1로 구성했다.
- `CartProduct`는 두 Entity를 연결하는 것에 그치지 않고 품목별 `quantity`를 가진다.
- 같은 Product라도 회원 Cart마다 quantity가 다르므로 Product 자체에 장바구니 수량을 넣지 않는다.

### 입력 DTO와 출력 DTO

| 구분 | 수업 artifact | 방향과 역할 |
|---|---|---|
| 추가 입력 | `CartProductDto` | Product 상세→Spring. product id와 quantity를 전달하며, 실제 사용자는 Controller의 인증 email로 정함 |
| 목록 출력 | `CartItemDto` | CartProduct·연결 Product→React. id·이름·image·가격·quantity, 후속 stock을 평탄한 화면 모양으로 전달 |
| React 화면 type | `CartProduct.ts` | `CartItemDto` 응답 원소와 맞추고 `checked` 같은 화면 선택 상태를 함께 다룸 |

04-13 원본의 `CartProductDto`에는 member id 필드도 보이지만 실제 상세 요청은 product id와 quantity를 보냈고, 04-14 Controller는 `Authentication.getName()`의 email로 회원을 식별했다. 클라이언트가 body에서 Cart 소유자를 임의로 정한 흐름으로 설명하지 않는다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| Product 상세 추가 | 로그인 상태, Product id, quantity | POST→인증 email로 Member 조회→Product/재고 확인→Cart 조회 또는 생성→동일 품목 탐색 | 기존 CartProduct quantity 누적 또는 새 CartProduct 저장 |
| 목록 조회 | 인증 사용자의 GET | email→Member→Cart→CartProduct 목록→`CartItemDto` 변환 | React 표에 image·이름·수량·가격·삭제 control 표시 |
| 전체/개별 선택 | checkbox boolean 또는 CartProduct id | 새 배열에서 `checked` 일괄 변경/반전→선택 품목 `price * quantity` 누적 | checkbox와 `orderTotalPrice` 갱신; DB에는 저장하지 않음 |
| 수량 변경 | number input 문자열→정수, CartProduct id·quantity | PATCH→CartProduct 조회→연결 Product stock·최소 수량·대상 확인→quantity 저장 | React quantity·합계와 DB quantity 변경 |
| 삭제 | CartProduct id | confirm→DELETE→Controller→Service→Repository 삭제 | 성공한 품목을 React 배열에서도 `filter`로 제거 |
| 선택 주문 전환 | `checked`인 Cart 품목 | 선택 `filter`→주문 DTO `map`→Order POST | Order 생성 쪽으로 전달; 성공 후 주문한 Cart 행·합계 제거 |

## 실제 수업 예시: 같은 상품 수량 누적

04-14 `CartService.addProductToCart`는 인증 email로 Member를 찾고 Product와 재고를 확인했다. 회원 Cart가 없으면 생성하고, 같은 Product의 CartProduct가 이미 있으면 기존 quantity에 요청 quantity를 더했다. 같은 상품이 없을 때만 Cart·Product·quantity를 가진 새 `CartProduct`를 저장했다. “같은 상품을 다시 담으면 행이 하나 더 생긴다”가 아니라 “관계 한 건의 수량이 누적된다”가 이날 구현의 중심이다.

다만 04-14의 재고 검사는 **이번 요청 quantity**와 Product stock을 비교했다. 기존 Cart quantity와 요청 quantity를 더한 누적값을 stock과 다시 비교하는 코드는 이날 원본에 없다. 동일 품목 누적과 누적 후 재고 검증까지 한 번에 완성됐다고 확대하지 않는다.

## checked와 quantity의 경계

- `checked`는 주문할 품목을 고르는 React 화면 state다. 04-15의 전체/개별 선택은 DB에 저장하지 않았다.
- `quantity`는 backend `CartProduct`에도 저장되는 업무 데이터다. 수량 input은 PATCH 성공 뒤 화면 state와 DB를 함께 바꿨다.
- `stock`은 Product의 현재 재고다. 04-17에 `CartItemDto`와 React type으로 전달해 quantity와 나란히 표시했다.
- 합계는 선택된 품목의 현재 가격과 quantity로 React에서 계산했다. 합계 자체를 CartProduct 필드로 저장한 근거는 없다.

## Cart 삭제와 Order 생성의 경계

04-16 오전의 Cart 삭제는 사용자가 장바구니 품목을 직접 지우는 DELETE 흐름이다. 같은 날 오후 Order 생성 Service는 선택된 Cart 품목으로 새 `OrderProduct`를 만들고 재고를 차감한 다음, **Cart에서 온 품목이면 해당 CartProduct를 삭제**했다. 결과에 Cart 행 삭제가 공통으로 보이더라도 사용자 삭제와 주문 처리 후 삭제는 시작 조건과 업무 의미가 다르다.

날짜도 나눠야 한다. 04-16에는 `makeOrder` 함수와 Order API/Service를 작성했지만, 그날 뒤의 “주문하기 Button” 조각은 삭제 버튼을 반복한 복붙 상태였다. 실제 `onClick={makeOrder}` 연결은 04-17 원본에서 확인된다.

## 자주 헷갈리는 원인

- **CartProduct와 React `CartProduct` type:** 전자는 JPA 관계 Entity이고 후자는 응답·화면 state의 TypeScript 모양이다. 이름이 같아도 저장 계층이 다르다.
- **`CartProductDto`와 `CartItemDto`:** 앞은 추가 입력, 뒤는 목록 출력이다. 상품명·가격·image를 추가 body가 모두 보내는 것으로 합치지 않는다.
- **04-14 control 표시와 동작:** checkbox·수량·삭제 control은 보였지만 선택 handler·PATCH·DELETE는 후속 날짜에 연결됐다.
- **04-15 수량 검증 초안과 04-16 보정:** 처음에는 Product id를 별도 parameter로 보냈고, 다음 날 CartProduct의 연결 Product를 직접 읽는 방식으로 정리했다.
- **`some`과 합계:** `some`은 선택 품목에 quantity 0이 하나라도 있는지 확인했다. 합계는 별도 누적이고 선택/DTO 변환은 `filter`·`map`의 책임이다.
- **frontend 검사와 backend 재고 검증:** Cart 선택 주문의 `some`은 quantity 0 존재만 검사했다. Product 상세 즉시 주문의 stock 초과 검사와 backend Service의 재고 검증을 같은 검사로 합치지 않는다.

## 이전 개념과 이후 기능 연결

- 선행 Product: [[concepts/product-domain-flow|상품 도메인 기능 흐름]]의 상세 화면과 Product stock이 Cart 입력이 된다.
- 관계·전달: [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]과 [[comparisons/entity-vs-dto|Entity vs DTO]]에서 CartProduct 관계와 DTO 변환을 더 자세히 본다.
- 화면 state: [[concepts/react-form-state-event|React 폼 상태와 이벤트]]와 [[comparisons/props-vs-state|props vs state]]가 checkbox·수량·로그인 user의 위치를 설명한다.
- 후속 Order: Cart는 선택 품목과 수량을 넘기는 데서 끝난다. Order/OrderProduct 생성·상태·재고 복원은 [[concepts/order-flow|주문 기능 흐름]]이 맡는다.

## 직접 수업·교안·후속 확장 경계

- **직접 수업:** 04-13 관계/추가 준비, 04-14 저장·목록, 04-15 선택·합계·수량/삭제 기반, 04-16 수량/삭제와 선택 주문 함수·API, 04-17 stock·quantity 0 검사·실제 주문 버튼 연결이다.
- **교안/그림 보충:** P08과 I01~I04의 관계·cascade·diagram 내용은 날짜 MD와 고도화 Summary에 충분히 전사되어 있어 별도 source로 추가하지 않았다.
- **R19 범위:** 총정리는 Product 상세→Cart 관계→추가·목록·선택·수량·삭제를 04-15 범위까지 복습한다. 04-16 Order 생성과 04-17 stock/주문 목록을 R19에 귀속하지 않는다.
- **후속 과목:** Linux·AWS·CI/CD는 실행·배포, Passwordless는 별도 인증, 중간 프로젝트는 실제 적용 범위다. Cart 직접 구현과 같은 단계로 합치지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md` — 04-15 Cart 삭제까지의 복습 범위
