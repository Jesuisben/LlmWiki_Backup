---
title: 2026-04-13 상품 상세와 useEffect, 서비스 계층
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png
status: growing
confidence: high
---

# 2026-04-13 상품 상세와 useEffect, 서비스 계층

## 한 줄 요약

상품 수정의 GET/PUT과 상세 GET을 Service·Controller·React `useEffect`로 마무리한 뒤, Cart·CartProduct Entity 관계와 상품 상세의 장바구니 추가 요청을 시작하며 Product에서 Cart로 전환한 날이다.

## 이전 수업과 오늘의 위치

- 직전 [[summaries/2026-04-10-react-event-spread-product-form|2026-04-10]]에는 상품 등록 왕복을 완성하고 기존 id·GET·PUT을 사용하는 수정 화면을 시작했다.
- 오늘 오전에는 수정용 GET/PUT과 상세 GET을 실제 백엔드 처리까지 닫았다. 오후에는 상품 상세 화면의 구매 수량을 장바구니 추가 요청으로 바꾸고 Cart 도메인의 Entity·DTO·Repository를 만들기 시작했다.
- 다음 [[summaries/2026-04-14-cart-service|2026-04-14]]에는 이 구조 위에 인증 사용자 기준 `CartService`·`CartController`, 추가와 목록 조회, `CartItemDto`, React `CartList` 표시를 연결한다.

## 왜 이 흐름으로 배웠는가

수정 화면은 기존 값을 먼저 읽은 뒤 바뀐 값을 저장해야 하고, 상세 화면은 같은 id 조회를 읽기 전용 화면에 사용한다. 이 두 Product 단건 흐름을 완성해야 사용자가 상세 화면에서 선택한 상품과 수량을 Cart에 전달할 수 있으므로, 하루 안에서 Product CRUD 마무리와 Cart 시작이 이어졌다.

## 실제 교시 흐름

1. **1교시 — 수정용 GET과 `useEffect`:** 웹/MVC/JDBC 자율 복습 범위를 안내한 뒤, `ProductService.getProductById`와 `ProductController.getUpdate`를 작성했다. 수정 화면의 route id가 바뀌면 `useEffect`가 GET을 호출하고 응답을 product state에 넣어 기존 입력값을 채우는 흐름을 맞췄다.
2. **2교시 — 수정용 PUT:** 기존 Product를 찾고, 수정값으로 이름·가격·카테고리·재고·설명을 옮겼다. 새 image Data URL이 있으면 이전 image를 삭제하고 새 파일을 저장한 뒤 Repository에 반영했다. Controller는 Validation 오류, 상품 부재, 수정 성공·실패를 나누었다.
3. **3교시 전반 — 수정·상세 테스트:** 수정 GET에서는 기존 값들이 폼에 보여야 하지만 file input에는 브라우저 보안상 기존 파일 경로를 기본값으로 넣을 수 없음을 확인했다. PUT 뒤에는 새 image file, DB 행, 목록 표시, 이전 image 삭제를 각각 점검했다.
4. **3교시 후반 — 상품 상세:** Product card 클릭→상세 route→`ProductDetail.tsx`의 `useEffect` GET→loading/product state→상세 화면 표시를 연결했다. Controller의 detail GET과 특정 상품 SQL 조회로 화면 반영을 확인했다.
5. **4~5교시 — Cart 관계 시작:** 장바구니 자료와 Spring 연관관계 매핑을 보고 `Cart`와 `CartProduct` Entity를 만들었다. Member–Cart는 1:1, Cart–CartProduct는 1:N, CartProduct–Product는 N:1로 구성하고, Cart와 Product의 다대다 의미를 수량을 가진 중간 Entity로 풀었다. cascade는 부모의 영속성 상태 변화가 자식으로 전이되는 개념으로 소개됐다.
6. **6교시 — 상세 화면에서 장바구니 추가 준비:** Product 상세에 quantity state와 change handler를 추가하고, 로그인·최소 수량을 확인한 뒤 product id와 quantity를 `/cart/insert`로 POST하는 `addToCart`를 연결했다. `CartProductDto`, Member/Product 조회 메서드, Cart/CartProduct Repository도 준비했다.
7. **7~8교시 — React 시험:** `useState`, 조건부 오류 표시, axios POST, `preventDefault`, Router, Validation 표시, `useEffect`, `map`, 관리자 조건, DELETE, `useParams`, FileReader, PUT, spread 등 지금까지의 FrontEnd_BackEnd 흐름을 문제로 복습했다. 새 Cart 기능 구현 교시는 아니다.

## 대표 artifact

- **`ProductUpdateForm.tsx` + Product GET/PUT:** route id로 기존 상품을 읽어 state에 넣고, 수정 body를 같은 id의 기존 Entity에 반영한다.
- **`ProductDetail.tsx`:** id 기반 상세 GET, loading/상품 부재 처리, 상품 정보 표시, quantity state와 장바구니 추가 버튼을 연결했다.
- **`Cart`·`CartProduct`:** 장바구니 소유자와 품목 목록, 각 품목이 참조하는 Product와 quantity를 Entity 관계로 표현했다.
- **`CartProductDto`:** React가 보낸 product id와 quantity를 장바구니 추가 백엔드로 전달하는 입력 DTO로 시작했다. 원본 클래스에는 member id 필드도 있으나 실제 상세 화면 요청 객체는 product id와 quantity를 보냈고, 다음 날 Controller는 인증 객체에서 사용자를 식별한다.

확인한 장바구니 도식은 한 Cart가 여러 CartProduct를 가지고, 여러 CartProduct가 각각 하나의 Product를 참조하며, quantity는 CartProduct별로 달라지는 구조를 보조한다. 그림의 상품명·가격은 관계를 보여 주는 예시이며 날짜 수업의 실제 DB 값으로 사용하지 않는다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| 수정 화면 조회 | route의 상품 id | React `useEffect` GET→Controller→Service→Repository 조회 | 기존 상품값이 form state에 반영; file input은 기존 파일값 미표시 |
| 상품 수정 | id와 수정 product body | Validation→기존 Product 조회→필드 반영→필요 시 이전/새 image 처리→save | DB와 목록의 상품 정보 변경 |
| 상품 상세 | card 클릭으로 선택한 id | 상세 route→React GET→Controller/Service 단건 조회 | loading 종료 후 이미지·가격·재고·설명 등 표시 |
| 장바구니 추가 준비 | 상세 화면의 product id와 quantity | 로그인·최소 수량 확인→POST body 생성 | 다음 날 인증 사용자 Cart에 저장할 요청 전달 |

## Product 마무리와 Cart 시작의 경계

- **Product 마무리:** 오전의 수정 GET/PUT과 상세 GET, 수정·상세 테스트까지다.
- **Cart 시작:** 오후의 관계 도식, `Cart`·`CartProduct`, quantity, 상세 화면의 추가 요청, 입력 DTO와 Repository 준비부터다.
- 장바구니 추가의 실제 Service/Controller 저장과 목록 조회는 04-14에 이어지므로 오늘 완성된 것으로 서술하지 않는다.

## 헷갈린 점 / 질문

- **수정 GET과 PUT은 왜 둘 다 필요한가:** GET은 기존 값을 form에 채우는 읽기이고 PUT은 사용자가 바꾼 값을 저장하는 변경이다.
- **기존 image 이름이 있는데 file input이 비어 보이는 이유:** 브라우저가 file input의 기본값 설정을 막기 때문이다. 상품 state의 image 정보와 사용자가 새로 고르는 file control을 같은 것으로 보면 안 된다.
- **`useEffect`가 화면을 직접 그리는가:** effect는 id 등 dependency에 맞춰 데이터를 요청하고 state를 갱신한다. 실제 렌더링은 loading/product state에 따라 JSX가 결정한다.
- **Cart와 Product를 바로 다대다로 연결하지 않은 이유:** 같은 Product라도 회원의 Cart마다 quantity가 다르다. 이 관계 자체의 데이터를 `CartProduct`가 보관한다.
- **cascade가 DB의 모든 삭제 규칙과 같은가:** 오늘은 JPA 영속성 전이 개념을 소개한 범위다. Oracle의 FK `ON DELETE`와 동일한 기능이라고 확대하지 않는다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** Product 수정·상세 GET/PUT, `useEffect` state 반영, Cart/CartProduct 관계 시작, 상세 화면 장바구니 요청 준비, React 시험이다.
- **후속 수업:** Cart 추가·목록은 04-14, 선택·수량·삭제는 04-15 이후, Order는 04-16 이후, 검색/페이징은 04-21~04-22다.
- Linux·AWS·CI/CD·Passwordless는 이 기능의 운영·배포·인증 확장이며 오늘 직접 구현 범위가 아니다.

## 관련 페이지

- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 01.png`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/다대일 단방향 매칭(Cart-CartProduct-Product) 02.png`
