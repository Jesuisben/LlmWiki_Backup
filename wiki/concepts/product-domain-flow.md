---
title: 상품 도메인 기능 흐름
created: 2026-07-06
updated: 2026-07-09
type: concept
tags: [spring-boot, react, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# 상품 도메인 기능 흐름

## 정의

상품 도메인 기능 흐름은 Category/Product Entity를 기준으로 상품 등록, 목록, 상세, 수정, 삭제, 페이징, 필드 검색을 Spring Boot와 React가 함께 구현하는 흐름이다.

## 왜 중요한가

상품은 쇼핑몰 프로젝트의 중심 데이터다. 이후 장바구니와 주문은 모두 Product를 참조하므로, 상품 도메인을 먼저 안정적으로 만들어야 전체 서비스가 이어진다.

## 핵심 설명

- Spring: Category enum과 Product Entity를 만들고 Controller/Service/Repository로 등록·조회·수정·삭제 API를 구성한다.
- React: Product TypeScript type, ProductList/ProductInsertForm/ProductDetail 같은 페이지, form state, `useEffect`, axios 요청을 작성한다.
- 검증: Spring `@Valid`와 `BindingResult`가 오류를 모으고 React는 `errors` 객체를 화면에 표시한다.
- 권한: 관리자만 등록/수정/삭제 버튼을 보이게 하되 실제 권한 검사는 백엔드에서도 필요하다.
- 검색/페이징: React는 page/search parameter를 보내고 Spring은 Specification + Pageable로 Page 결과를 반환한다.

## 수업 예시

2026-04-08에는 Category/Product 기본 구조, 04-09에는 삭제와 관리자 조건부 렌더링, 04-10에는 등록/수정 form state, 04-13에는 상세 조회와 `useEffect`, 04-21~04-22에는 Pageable과 필드 검색으로 확장했다.

## 관련 개념

- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]
- [[concepts/pagination-search|페이징과 검색]]
- [[comparisons/entity-vs-dto|Entity vs DTO]]

## 4과목 현재 raw MD 기준 재검증 메모

- 2026-07-09에 `raw/KoreaICT/4. FrontEnd_BackEnd` 날짜별 MD 18개와 `FrontEnd_BackEnd 총정리.md`를 기준으로 다시 대조했다.
- 이 페이지는 단순 일반론이 아니라 Spring Boot Controller/Service/Repository, React Router/page/state, JWT 인증, Product/Cart/Order/Pageable 기능 흐름과 연결해 읽어야 한다.
- 핵심 복습 순서는 환경 세팅 → REST API/JSON/CORS → Member/JWT → Product → Cart → Order → Pageable/검색이다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
