---
title: 상품 도메인 기능 흐름
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf
status: growing
confidence: high
---
# 상품 도메인 기능 흐름

## 정의

상품 도메인 기능 흐름은 Category/Product Entity를 기반으로 상품 등록, 목록, 상세, 수정, 삭제, 검색, 페이징이 React 화면과 Spring Boot API를 통해 연결되는 전체 흐름이다.

## 왜 중요한가

상품은 쇼핑몰 프로젝트의 중심 데이터다. 이후 장바구니는 Product를 참조하고, 주문은 상품 가격/수량을 기록하며, 검색/페이징은 상품 목록이 많아졌을 때 필요한 기능이다.

## 핵심 설명

```text
React 상품 화면
→ ProductController
→ ProductService
→ ProductRepository
→ Product/Category Entity
→ MySQL
```

- Entity는 DB와 연결되는 상품 구조다.
- DTO 또는 TypeScript interface는 화면/API 입출력에 맞춘 데이터 모양이다.
- Service는 등록/수정/삭제/상세/검색 같은 업무 규칙을 모은다.
- Repository는 JPA를 통해 DB 조회를 수행한다.

## 수업 예시

- [[summaries/2026-04-08-product-domain-oci|2026-04-08]] — Category/Product 도메인 시작
- [[summaries/2026-04-09-product-delete-routing-jsx-table|2026-04-09]] — 상품 삭제와 라우팅
- [[summaries/2026-04-10-react-event-spread-product-form|2026-04-10]] — 상품 등록 폼 상태 관리
- [[summaries/2026-04-13-product-detail-useeffect-service|2026-04-13]] — 상품 상세와 `useEffect`
- [[summaries/2026-04-21-product-pagination-search-react|2026-04-21]] / [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22]] — 검색/페이징

## 자주 헷갈리는 점

- Product를 장바구니에 담는다고 Product row가 복제되는 것은 아니다. 장바구니에서는 CartProduct가 Product를 참조한다.
- React의 Product 타입과 Spring의 Product Entity는 이름이 같아도 위치와 책임이 다르다.
- 삭제/수정은 화면에서 버튼을 누르는 것뿐 아니라 백엔드 API, 권한, DB 반영까지 확인해야 한다.

## 관련 개념

- [[concepts/shopping-cart-flow]]
- [[concepts/spring-product-search-flow]]
- [[concepts/react-form-state-event]]
- [[concepts/react-useeffect-data-fetching]]
- [[comparisons/entity-vs-dto]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/필드 검색 기능.pdf`
