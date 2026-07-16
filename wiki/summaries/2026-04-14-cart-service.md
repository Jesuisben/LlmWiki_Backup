---
title: 2026-04-14 장바구니 Service와 DTO
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png
status: growing
confidence: high
---

# 2026-04-14 장바구니 Service와 DTO

## 한 줄 요약

인증된 사용자의 email을 기준으로 상품을 기존 Cart에 누적하거나 새 품목으로 저장하고, 장바구니 Entity를 `CartItemDto`로 변환해 React `CartList`의 행으로 표시하는 추가·목록 조회 왕복을 구현한 날이다.

## 이전 수업과 오늘의 위치

- 전날 [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13]]에는 Product 수정·상세를 마무리하고 Cart/CartProduct 관계, quantity, 상세 화면의 `/cart/insert` 요청과 Repository를 준비했다.
- 오늘은 그 요청을 실제 인증 사용자 Cart에 저장하고, 다시 사용자별 Cart 품목을 조회해 React 표에 표시하는 두 use case를 완성했다.
- 다음 [[summaries/2026-04-15-cart-list-selection-typescript|2026-04-15]]에는 표시된 각 품목에 전체/개별 선택, props·구조 분해와 수량 변경·삭제 동작을 붙인다.

## 왜 이 흐름으로 배웠는가

장바구니는 화면의 product id와 quantity만 저장한다고 끝나지 않는다. 누가 요청했는지 인증 정보로 확인하고, 회원의 Cart가 없으면 만들고, 같은 Product가 이미 있으면 수량을 누적해야 한다. 조회할 때는 지연 연관관계 Entity 전체가 아니라 화면에 필요한 품목 모양으로 변환해야 React 타입과 표가 맞는다.

## 실제 교시 흐름

1. **1교시 — `CartProductService`:** `CartProductRepository.save`를 감싼 `saveCartProduct`를 만들어 Cart 품목 저장 책임을 분리했다.
2. **2교시 — `CartService.addProductToCart`:** 인증 email로 Member를 찾고, DTO의 product id로 Product를 조회하고, 요청 quantity와 재고를 비교했다. 회원 Cart가 없으면 생성하고, 같은 Product가 이미 있으면 기존 quantity에 더하며, 없으면 Cart·Product·quantity를 담은 새 `CartProduct`를 저장했다.
3. **3교시 — `CartController` 추가 API와 DB 확인:** `Authentication.getName()`으로 email을 얻어 Service에 DTO와 함께 전달했다. 여러 사용자·상품·반복 추가 시나리오를 수행하고 members–carts–cart_products–products JOIN으로 사용자별 최종 수량을 확인했다.
4. **4교시 — React 목록 뼈대:** 백엔드 응답과 맞출 `CartProduct.ts` interface, `/cart/list` route, 사용자 이름·선택·상품 정보·수량·금액·삭제 열을 가진 `CartList.tsx` 기본 표를 만들었다.
5. **5교시 — 목록 요청과 DTO:** `cartProducts` 배열 state와 `useEffect`, `fetchCartProducts`를 연결해 로그인 user가 있으면 GET 요청을 보내도록 했다. Spring에는 화면의 품목 한 개를 뜻하는 `CartItemDto`를 만들고 CartProduct/연결 Product의 id·이름·image·가격·quantity를 평탄한 필드로 옮겼다.
6. **5교시 후반 — 사용자별 목록 API:** `CartService.getCartItemsByMemberId`가 Member와 Cart를 찾고 CartProduct마다 `CartItemDto`를 만들었다. Controller는 인증 email로 Member를 찾은 뒤 해당 id의 DTO 목록을 응답했다.
7. **6교시 — React 데이터 표시:** `cartProducts.map`으로 품목마다 checkbox, image/name, quantity input, `price * quantity`, 삭제 버튼을 표의 한 행으로 렌더링하고 빈 장바구니 분기를 두었다.
8. **7~8교시 — 자습:** 새 수량 변경·삭제·주문 로직은 추가하지 않았다. 해당 동작은 다음 날짜 범위다.

## 대표 artifact

- **`CartProductService`:** CartProduct 한 건 저장을 Repository에 위임한다.
- **`CartService`:** 추가 시 사용자·상품·재고·Cart·중복 품목을 판단하고, 목록 조회 시 Entity 목록을 DTO 목록으로 변환한다.
- **`CartController`:** request body의 상품/수량과 `Authentication`의 사용자 신원을 결합해 추가·조회 use case를 시작한다.
- **`CartItemDto` ↔ `CartProduct.ts`:** 백엔드 목록 한 건과 프론트 배열 원소의 필드 모양을 맞춘다.
- **`CartList.tsx`:** GET 응답을 state에 저장하고 각 DTO를 표 한 행으로 표시한다.

쇼핑 카트 도식은 Member 1명당 Cart 1개, Cart 1개당 CartProduct 여러 개, 각 CartProduct가 Product 1개를 참조하고 quantity를 가진다는 구조를 보여 준다. 오늘 Service의 “같은 상품이면 수량 누적, 아니면 새 CartProduct” 분기가 이 구조를 실제 저장 로직으로 옮긴 부분이다.

## 입력 → 처리 → 결과

| use case | 입력 | 처리 | 결과 |
|---|---|---|---|
| 장바구니 추가 | request body의 product id·quantity + 인증 email | Member/Product 조회→재고 확인→Cart 조회/생성→동일 품목 탐색→수량 누적 또는 새 품목 저장 | 인증 사용자 Cart의 CartProduct와 quantity 변경 |
| 장바구니 목록 | 인증된 사용자의 GET 요청 | email→Member→Cart→CartProduct 목록→각 항목을 `CartItemDto`로 변환 | React가 사용할 평탄한 DTO 배열 응답 |
| 화면 표시 | DTO 배열 | state 저장→`map`→상품별 표 행과 금액 계산 | image·이름·수량·품목 금액·삭제 버튼 표시 또는 빈 장바구니 문구 |

## 추가 DTO와 목록 DTO의 구분

- `CartProductDto`는 상세 화면에서 장바구니에 **추가할 때 들어오는 값**을 받는다. 실제 Controller는 사용자 신원을 request body의 member id에 의존하지 않고 인증 객체의 email에서 얻었다.
- `CartItemDto`는 장바구니 **목록으로 나갈 값**이다. CartProduct와 Product 관계에서 화면에 필요한 필드만 꺼내 React `CartProduct` interface에 맞춘다.
- Entity 관계와 DTO 화면 모양을 같은 것으로 보면, 어느 값이 DB 관계이고 어느 값이 API 응답용인지 혼동하기 쉽다.

## 헷갈린 점 / 질문

- **사용자를 왜 body의 member id로 정하지 않는가:** 오늘 Controller는 로그인 인증 객체의 이름(email)을 사용한다. 어떤 사용자의 Cart인지 클라이언트가 임의로 정하는 흐름과 구분해야 한다.
- **같은 상품을 다시 담으면 행이 하나 더 생기는가:** Service는 기존 CartProduct를 찾아 quantity를 누적하고, 기존 품목이 없을 때만 새 CartProduct를 만든다.
- **재고 검사는 무엇을 비교하는가:** Product의 현재 stock과 이번 DTO의 요청 quantity를 비교한다. 기존 장바구니 수량까지 합친 후속 재고 보정은 다음 날짜들의 점검 대상이다.
- **Cart가 없을 때 목록 조회는 어떻게 되는가:** 원본 구현은 빈 Cart를 만들 수 있으나 `cartProducts`가 초기화되지 않은 경우의 처리까지 완결됐다고 단정할 수 없다. 오늘의 중심은 DTO 변환과 목록 응답 연결이다.
- **체크·수량·삭제가 오늘 동작하는가:** 오늘은 필드와 control을 표시한 단계다. 선택 handler, 수량 변경 API, 삭제 API는 후속 수업 범위다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** 인증 사용자 기준 Cart 추가, 동일 품목 수량 누적, DB 확인, DTO 목록 변환, React CartList 요청·표시다.
- **후속 수업:** 선택·수량 변경·삭제는 04-15~04-16, Order는 04-16 이후, 검색/페이징은 04-21~04-22다.
- Linux·AWS·CI/CD·Passwordless는 장바구니 기능의 운영·배포·다른 인증 확장이며 오늘 직접 수업이 아니다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png`
