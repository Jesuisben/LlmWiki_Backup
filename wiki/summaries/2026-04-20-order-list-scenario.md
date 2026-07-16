---
title: 2026-04-20 주문 목록과 테스트 시나리오
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: high
---

# 2026-04-20 주문 목록과 테스트 시나리오

## 한 줄 요약

역할별 PENDING 주문을 카드로 표시하고 관리자의 완료·사용자와 관리자의 취소 요청을 Spring 상태 변경·재고 복원과 연결한 뒤, 정적 Home carousel을 DB 대표 상품으로 바꾸고 페이징 타입·컴포넌트를 시작한 날이다.

## 이전 수업과 오늘의 위치

- 이전 [[summaries/2026-04-17-cart-total-array-some|2026-04-17]]에는 Order 생성 이후 USER/ADMIN별 PENDING 목록을 DTO로 조회하고 React `orders` state에 담는 초기 화면까지 만들었다.
- 오늘은 그 배열을 실제 주문 카드로 렌더링하고 역할별 버튼을 붙여, 목록 조회→상태 완료 또는 주문 취소→화면·DB 확인을 완성했다.
- 오후 후반에는 Order를 마무리하고 Product 대표 상품과 paging으로 넘어갔다. 다음 [[summaries/2026-04-21-product-pagination-search-react|2026-04-21]]에는 ProductList의 페이지 요청·응답과 검색 조건을 본격 연결한다.

## 왜 이 흐름으로 배웠는가

주문 생성만으로 업무 흐름은 끝나지 않는다. 관리자는 대기 주문을 완료하고, 사용자 또는 관리자는 대기 주문을 취소할 수 있어야 하며, 취소하면 차감했던 재고도 돌려놓아야 한다. 그래서 먼저 역할별 화면 시나리오를 정하고 버튼→HTTP 요청→Service transaction→DB와 화면 결과를 순서대로 연결했다.

## 실제 교시 흐름

1. **1교시 — 주문 카드 렌더링:** `orders.map`으로 주문 번호·날짜·상태·내부 주문 품목을 Card에 표시했다. 최신 주문 우선, ADMIN은 모든 사용자의 주문과 이름, USER는 본인 주문만 본다는 조회 시나리오를 확인했다.
2. **1교시 — 역할별 버튼 설계:** PENDING 항목만 화면에 있다는 전제에서 ADMIN에는 완료와 취소, USER에는 취소 버튼만 만들었다. 이 단계의 버튼은 보이지만 아직 서버 handler가 연결되지 않은 UI였다.
3. **2교시 — 완료 요청의 React 연결:** ADMIN 완료 버튼이 Order id와 새 상태를 URL에 넣어 PUT 요청을 보내고, 성공하면 해당 Order를 화면 배열에서 filter해 제거하도록 했다.
4. **2교시 — 완료용 Repository:** 긴 derived query 대신 Entity 이름과 필드를 쓰는 JPQL update를 소개하고 수정 쿼리용 annotation과 transaction을 붙인 Repository 메서드를 작성했다.
5. **3교시 — 완료 Service·Controller:** Service는 Order를 찾고 CANCELED 상태는 변경하지 못하게 한 뒤 새 상태를 설정했다. Controller는 path의 Order id와 parameter의 상태를 받아 Service에 넘겼다. MySQL JOIN으로 주문 상태를 확인하고 전체 주문을 PENDING으로 돌리는 후속 테스트 SQL도 사용했다.
6. **3교시 후반 — 취소의 React 연결:** 취소 버튼이 DELETE 요청을 보내고, 성공하면 해당 Order를 화면 목록에서 제거하도록 했다.
7. **4교시 — 취소 Service:** transaction 안에서 Order와 각 OrderProduct를 읽고 주문 quantity를 Product stock에 더해 저장한 뒤 Order를 삭제했다. Order–OrderProduct의 cascade/orphan 설정에 따라 주문 상품 행 삭제도 함께 확인하는 시나리오를 두었다.
8. **4교시 — 취소 Controller와 REST 보충:** Controller가 Order id를 받아 Service 결과를 응답하고, Order가 없을 때 not found 응답을 만들었다. IT 용어 교안의 REST mapping 사용 예를 참고하되, 실제 기능은 위 DELETE 경로로 구현했다.
9. **5교시 — 대표 상품 carousel:** 정적으로 적은 이미지 대신 HomePage가 `filter=bigs`로 Product 목록을 요청하고, Repository의 image 포함 검색→Service→Controller 응답으로 대표 상품을 가져오게 했다. 조회 개수를 먼저 확인한 뒤 `map`으로 carousel을 만들고 이미지 클릭을 상세 화면으로 연결했다.
10. **6교시 — HomePage 동적 표시 완성:** 상품 이름·설명·image를 응답값으로 렌더링하고 긴 설명을 잘라 표시했으며 기존 하드코딩 carousel 항목을 제거하는 흐름을 정리했다.
11. **6~7교시 — 페이징 시작:** `PagingInfo`와 초기값을 만들고 React Bootstrap Pagination으로 처음·이전·숫자·다음·끝 control과 `setPaging`을 연결했다.
12. **8교시 — ProductList 연결 시작:** ProductList에 paging state와 `Paging` 컴포넌트를 추가했다. 이 날짜 코드의 상품 GET은 아직 기존 목록 응답을 사용하므로, page parameter와 Spring Page 응답의 본격 연결은 다음 날 범위다.

## 대표 artifact

- **`OrderList.tsx`:** 주문 카드, ADMIN/USER별 버튼, 완료 PUT과 취소 DELETE, 성공 후 local 목록 제거를 담당한다.
- **Order 완료 경로:** React→Controller→Service의 상태 검증·변경→Order 저장 상태로 이어진다. 원본에는 JPQL update Repository 예제도 같은 구간에 등장하지만 Service 본문은 조회한 Entity의 상태를 바꾸는 방식이다.
- **Order 취소 경로:** React→Controller→transaction Service→OrderProduct 순회→Product stock 복원→Order 삭제로 이어진다.
- **MySQL 시나리오:** members–orders–order_products–products JOIN으로 주문 상태와 stock을 전후 비교한다.
- **HomePage 대표 상품 경로:** `filter=bigs` 요청→image 포함 Product 조회→응답 배열→carousel `map`과 상세 이동이다.
- **`PagingInfo`·`Paging.tsx`:** 다음 Product 목록 페이징을 위한 화면 상태와 control이다.

## 입력 → 처리 → 결과

| 기능 | 입력 | 처리 | 결과 |
|---|---|---|---|
| 주문 목록 표시 | 전날 받아 둔 역할별 PENDING DTO 배열 | `orders.map`→Order 카드와 내부 `orderItems.map` | ADMIN은 전체 사용자 주문, USER는 본인 주문 표시 |
| 주문 완료 | ADMIN의 완료 클릭, Order id, COMPLETED | PUT→Controller→Service의 Order 조회·상태 검사·변경→React filter | PENDING 목록과 DB에서 해당 주문이 완료 상태로 이동 |
| 주문 취소 | USER/ADMIN의 취소 클릭, Order id | DELETE→Controller→transaction Service→각 주문 수량만큼 stock 복원→Order 삭제→React filter | 화면·orders·order_products에서 주문 제거, Product 재고 증가 |
| 대표 상품 | HomePage의 선택적 filter | Product Controller→Service→Repository image 포함 검색→React 배열 | DB 상품으로 동적 carousel과 상세 이동 구성 |
| 페이징 준비 | 초기 `PagingInfo`, control 클릭 | `setPaging`으로 pageNumber 계산·변경 | UI paging state 마련; 서버 Page 왕복은 다음 날 완성 |

## Order 생성과 오늘 상태 처리의 경계

- Cart 선택→Order request body→Order/OrderProduct 저장→재고 차감→CartProduct 삭제는 04-16에 구현됐다.
- Order 목록용 DTO·역할별 PENDING 조회·초기 React fetch는 04-17에 시작됐다.
- 오늘은 새 Order Entity나 생성 DTO를 만든 날이 아니라, 받은 목록을 표시하고 이미 생성된 Order를 완료·취소하는 날이다.
- 원본의 취소 설명에는 CANCELED 상태 변경 표현도 있지만 실제 Service 코드는 재고를 복원한 뒤 Order를 삭제한다. 따라서 “취소 행이 상태값으로 남는다”고 단정하지 않는다.

## 헷갈린 점 / 질문

- **버튼이 보이는 것과 기능이 연결된 것:** 1교시에는 역할별 버튼 UI를 만들었고, 2~4교시에 각각 완료·취소 handler와 Spring 경로를 연결했다.
- **완료와 취소:** 완료는 Order 상태를 COMPLETED로 바꾸고 PENDING 목록에서 제거한다. 취소 구현은 stock을 되돌리고 Order를 삭제한다.
- **상태 변경 구현 두 가지가 왜 함께 보이는가:** Repository에는 JPQL update 예제가 추가됐지만 Service 본문은 Order를 조회해 상태를 설정한다. 원본만으로 두 방식이 한 호출에서 모두 실행된다고 합치지 않는다.
- **ADMIN/USER 조회와 버튼 권한:** 전날 조회 범위를 역할로 나눴고 오늘 화면 버튼도 역할로 나눴다. 이 화면 조건만으로 서버 인가가 완성됐다고 단정할 수는 없다.
- **map의 의미:** React 배열 `map`은 주문 카드·품목·carousel을 반복 생성한다. Java Collection의 메서드나 DB 조회 자체와 동일한 처리가 아니다.
- **Order와 검색/페이징:** 대표 상품과 Paging 시작은 Order 후반에 같은 날 등장한 다음 기능이다. 주문 처리 단계로 묶지 않는다.

## 직접 수업과 후속 확장 경계

- **직접 수업:** OrderList 렌더링, 역할별 버튼, 완료·취소 요청과 Spring 처리, MySQL 검증, 대표 상품 carousel, Paging 타입·컴포넌트와 ProductList 연결 시작이다.
- **이전 날짜:** Order Entity·DTO·생성 API는 04-16, 목록 DTO·조회 API·초기 화면은 04-17이다.
- **다음 날짜:** 04-21~04-22에 Product 검색/페이징의 React parameter→Spring Specification/Pageable→DB 흐름을 완성한다.
- Linux·AWS·CI/CD·Passwordless는 서버 운영·클라우드 배포·자동화·다른 인증 방식의 후속 과목이며 오늘 직접 구현이 아니다.

## 관련 페이지

- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[comparisons/jpql-vs-sql|JPQL vs SQL]]
- [[concepts/pagination-search|페이징과 검색]]
- [[queries/why-shopping-cart-order-flow-is-complex|장바구니와 주문 흐름은 왜 복잡한가]]
- [[queries/jwt-role-ui-vs-server-authorization|JWT role UI와 서버 인가는 왜 다른가]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
