---
title: 페이징과 검색
created: 2026-07-06
updated: 2026-07-16
type: concept
tags: [spring-boot, react, frontend, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# 페이징과 검색

## 정의

이 수업의 페이징·검색은 Product 목록을 **React의 page/search state→GET parameter→Spring Controller/SearchDto→Service의 Specification·Pageable 조립→Repository Page 조회→React content/metadata 분리**로 왕복시킨 기능이다. 단순히 Pagination control이나 검색 form을 그리는 것이 아니라, UI 값이 실제 DB 조건에 소비되고 결과가 다시 화면 state를 바꾸는 데까지 연결해야 완성된다.

## 왜 중요한가

04-08의 Product 목록은 응답 body 자체가 배열이었다. 데이터가 늘어난 뒤 같은 방식으로 전체 상품을 계속 받는 대신 page 단위로 나누고, 기간·카테고리·상품명/설명 포함 조건을 선택적으로 적용했다. 이 과정에서 “화면이 존재한다”, “요청에 값이 실린다”, “backend가 그 값을 DB 검색에 사용한다”는 서로 다른 완료 단계를 배웠다.

## 3일에 걸친 실제 완성 순서

| 날짜 | 구현 수준 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-20-order-list-scenario|2026-04-20]] | Paging type·초기값·처음/이전/숫자/다음/끝 control과 ProductList state를 준비. 기존 목록 응답이라 서버 Page 왕복은 미완성 | `PagingInfo`, `initialPagingInfo`, `Paging.tsx` |
| [[summaries/2026-04-21-product-pagination-search-react|2026-04-21]] 오전 | page parameter→단순 Pageable 조회→`Page<Product>` 응답→React content/metadata와 재요청 연결 | ProductList GET params, `response.data.content`, `paging.pageNumber` dependency |
| 2026-04-21 오후 | 검색 form/state/request parameter, `SearchDto`, 개별 `ProductSpecification` 조건을 준비. backend 검색 조립은 미완성 | `SearchCondition`, `FieldSearch`, `SearchDto`, `ProductSpecification` |
| [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22]] | Controller가 검색값을 받고 Service가 조건·sort/page를 조립해 Repository 호출까지 연결. 실행 전제는 별도 확인 필요 | `ProductService.listProducts`, `ProductController.listProducts`, `ProductRepository.findAll` |

## Product 배열과 Page 응답

| 응답 형태 | 상품 배열 위치 | 추가 정보 | React 처리 |
|---|---|---|---|
| 04-08 전체 목록 | `response.data` | 별도 page metadata 없음 | Product[] state에 바로 저장 |
| 04-21 이후 Page | `response.data.content` | `totalElements`, `totalPages`, `pageable.pageNumber`, `pageable.pageSize` 등 | content는 상품 카드, metadata는 Paging state에 분리 |

`response.data`를 그대로 Product[]로 넣던 코드를 Page 응답에서도 유지하면 상품 배열 대신 wrapper 객체를 배열처럼 다루게 된다. optional chaining과 `??`는 metadata가 없을 때 안전한 기본값을 고르는 TypeScript 도구이며, Page 구조 자체를 만드는 기능은 아니다.

## 입력 → 처리 → 결과

| 단계 | 입력 | 처리 | 결과 |
|---|---|---|---|
| page 이동 | Paging control이 바꾼 0-based `pageNumber` | state 변경→`useEffect` 재실행→pageNumber/pageSize GET→Controller `PageRequest`→Repository page 조회 | content는 Product 카드, metadata는 현재/전체 page 표시 |
| 검색 화면 | 기간·카테고리·mode·keyword control | `FieldSearch`가 `SearchCondition` 갱신 | controlled search state와 화면 값 일치 |
| frontend 검색 요청 | 네 검색 state 값 | ProductList가 같은 GET의 parameter와 effect dependency에 추가 | 04-21부터 요청에는 실리지만 이날 backend는 아직 소비하지 않음 |
| backend 검색 | Controller가 받은 page와 네 검색값 | `SearchDto` 생성→Service가 값 있는 Specification만 `and`→id 내림차순 `PageRequest`→Repository `findAll` 호출 코드 | 의도한 결과는 조건과 page/sort가 적용된 `Page<Product>`이며 실행 성공은 추가 확인 필요 |
| 검증 | 기간·카테고리·name/description 문자열 | MySQL에서 대응 WHERE·LIKE·AND 시나리오 실행 | 애플리케이션 검색 의도와 DB 결과 비교 기반 |

## UI control·요청·backend 소비의 경계

1. **04-20 UI 준비:** control 클릭이 `setPaging`을 바꾸는 구조는 있었지만 상품 GET은 기존 목록 응답을 사용했다.
2. **04-21 page 연결:** page state가 GET parameter가 되고 `useEffect` dependency가 되어 번호 변경 때 재요청했다. Spring이 `Page<Product>`를 반환해 화면 metadata까지 연결됐다.
3. **04-21 검색 요청 준비:** 검색 input 변경이 state와 GET parameter를 바꿨다. `SearchDto`와 개별 Specification도 작성했지만, Controller의 당시 Page endpoint는 page 번호·크기만 소비했다.
4. **04-22 검색 backend 연결 코드 작성:** Controller가 네 검색 parameter를 `SearchDto`로 묶고, Service가 조건을 조립해 Repository에 Specification과 Pageable을 함께 넘기는 코드를 작성했다.

따라서 “검색 form이 보임”, “network 요청에 검색값이 있음”, “DB 결과가 검색값에 따라 달라짐”은 같은 완료 상태가 아니다.

## 구현 연결과 실행 검증의 경계

04-22 원본은 `ProductRepository.findAll(Specification<Product>, Pageable)` signature와 Controller→Service→Repository 호출 흐름을 제시한다. 그러나 앞선 Repository 선언에서 `JpaSpecificationExecutor<Product>` 상속을 추가하는 지시는 확인되지 않고, `Product.inputdate`의 `LocalDate`와 `hasDateRange()` 비교값 `LocalDateTime`도 타입 정합성을 점검해야 한다. 따라서 **검색 backend 코드 흐름은 연결됐지만, 해당 원본만으로 Specification query와 날짜 조건이 정상 실행됐다고 확정하지 않는다.**

## frontend 재요청과 backend 조건 소비

- React는 `paging.pageNumber`와 검색 조건들을 effect dependency에 두어 값이 바뀔 때 목록 요청을 다시 실행했다.
- 원본에는 검색 조건이 바뀔 때 page를 0으로 되돌리는 별도 처리까지 확인되지 않는다.
- backend는 조건 값이 있는 경우에만 날짜·카테고리·name/description Specification을 붙였다.
- `searchMode`는 `"name".equals(searchMode)` 같은 문자열 비교로 분기했다. 이는 null에 안전한 해당 분기 방식이며 모든 참조 자료형 비교를 하나의 규칙으로 단순화하지 않는다.

## Querydsl 언급과 실제 Specification 구현

04-21에 Querydsl 관련 Page API 용어와, 04-17 Repository 설명에서 복잡한 query 대안으로 querydsl이 언급됐다. 그러나 실제 상품 검색 코드는 Spring Data JPA `Specification<Product>`로 기간·카테고리·상품명·설명 조건을 만들고 `Pageable`과 함께 조회했다. “Querydsl 검색을 구현했다”고 바꿔 말하지 않는다.

## 자주 헷갈리는 원인

- **0-based와 화면 번호:** Spring/React 내부 `pageNumber`는 0부터 시작하고 사용자용 문구는 1을 더했다.
- **Specification과 Pageable:** 전자는 동적 검색 조건, 후자는 page·size·sort다. 같은 Repository 호출에 들어가도 책임이 다르다.
- **UI와 기능 단계:** 04-20 control, 04-21 page 왕복/검색 request, 04-22 backend 검색 연결 코드 작성을 날짜별로 구분한다.
- **Page와 Product[]:** `content`만 상품 배열이고 wrapper의 나머지는 metadata다.
- **검색값 변화와 자동 DB 적용:** frontend dependency가 요청을 다시 실행해도 Controller/Service/Repository가 parameter를 소비하지 않으면 결과 조건은 바뀌지 않는다.
- **빈 category 변환:** 원본은 빈 기본값을 사용하지만 enum parameter 변환의 모든 실행환경 성공을 보장한다고 확대하지 않는다.

## 이전 개념과 이후 기능 연결

- 선행 Product: [[concepts/product-domain-flow|상품 도메인 기능 흐름]]의 전체 목록·대표 상품이 page/search 대상으로 확장됐다.
- React 실행 시점: [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]이 dependency와 재요청 조건을 설명한다.
- backend 세부: [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]은 두 객체의 원리, [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]은 Controller→Service→Repository 검색 경로에 집중한다.
- 전체 왕복: [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]에서 화면 state와 DB 결과의 경계를 확인한다.

## 직접 수업·교안·후속 확장 경계

- **직접 수업:** 04-20 UI 준비, 04-21 page 왕복과 검색 frontend/조건 artifact 준비, 04-22 backend 검색 연결 코드·MySQL 시나리오다. Specification 실행 성공은 미확정 경계로 남긴다.
- **교안 보충:** P03·P08·P10의 Page·Specification·필드 검색 설명은 날짜 MD에 구현 순서가 충분히 전사되어 있어 별도 source로 추가하지 않았다.
- **R19 범위:** 총정리 원본은 04-15 Cart 삭제에서 끝나므로 04-20~04-22 Paging·검색의 source가 아니다. 끝 경계 확인에만 사용했다.
- **후속 과목:** 같은 04-22에 시작한 Linux는 별도 과목이다. AWS·CI/CD는 배포, Passwordless는 인증, 중간 프로젝트는 적용 범위이며 검색 기능 직접 구현으로 소급하지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md` — 04-15 Cart 삭제에서 끝나는 경계 확인용
