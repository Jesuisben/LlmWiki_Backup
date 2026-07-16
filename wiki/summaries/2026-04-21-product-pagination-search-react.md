---
title: 2026-04-21 React 상품 페이징과 필드 검색 준비
created: 2026-07-06
updated: 2026-07-16
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: high
---

# 2026-04-21 React 상품 페이징과 필드 검색 준비

## 한 줄 요약

전날 만든 `PagingInfo`·`Paging` control을 `ProductList`의 page request와 Spring `Page<Product>` 응답에 연결하고, 검색 입력 state·request parameter·`SearchDto`·`ProductSpecification`을 차례로 준비했지만 검색 조건의 Repository 조회 완성은 다음 날로 남긴 날이다.

## 이전 수업과 오늘의 위치

- 이전 [[summaries/2026-04-20-order-list-scenario|2026-04-20]] 후반에는 `PagingInfo`, `Paging.tsx`, ProductList의 paging state와 control을 만들었다. 당시 상품 GET은 기존 목록 응답을 사용했으므로 control의 존재가 서버 페이징 완료를 뜻하지 않았다.
- 오늘 오전에는 page 번호를 요청하고 Spring Page 응답을 받아 control과 실제 데이터를 연결했다. 오후에는 검색 UI와 요청 parameter를 붙이고 백엔드 조건 객체를 만들었다.
- 다음 [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22]]에는 `ProductRepository`·Service·Controller가 `Specification`과 `Pageable`을 함께 사용하면서 검색 조건이 실제 DB 조회까지 도달한다.

## 왜 이 순서로 배웠는가

목록 화면에 페이지 번호나 검색 form만 그려 놓아서는 데이터가 달라지지 않는다. 먼저 `pageNumber`·`pageSize`를 요청에 넣고 Page 응답의 상품 배열과 페이지 metadata를 React state에 되돌려야 한다. 그 왕복이 동작한 다음 검색 조건도 같은 요청에 추가하고, Spring이 받을 DTO와 동적 WHERE 조건을 준비하는 순서로 확장했다.

## 실제 교시 흐름

1. **1교시 — React page 요청과 Page 응답 연결:** `ProductList`의 GET parameter에 `paging.pageNumber`와 `paging.pageSize`를 넣고, 응답 상품은 `response.data.content`에서 꺼냈다. `totalElements`, `totalPages`, `pageable.pageNumber`, `pageable.pageSize`로 paging state를 갱신하고 현재 page group의 `beginPage`·`endPage`·상태 문구를 계산했다. `paging.pageNumber`를 `useEffect` 의존성에 넣어 page control이 번호를 바꾸면 요청이 다시 실행되게 했다.
2. **1교시 보충 — useEffect 의존성:** 교안의 `useEffect` 두 번째 매개변수를 확인하며 props나 state 변화가 재실행 조건이 된다는 점을 현재 page 번호에 연결했다.
3. **2교시 — 단순 Pageable Service:** `ProductService.listProducts(Pageable)`가 Repository의 `findAll(pageable)`을 호출하도록 추가했다. 이 시점은 검색 조건 없이 page와 sort를 적용하는 단계다.
4. **3교시 — 단순 Page Controller와 화면 control 연결:** 기존 전체 목록 mapping을 주석 처리하고, Controller가 `pageNumber`·`pageSize`를 받아 id 내림차순 `PageRequest`를 만든 뒤 `Page<Product>`를 응답하도록 바꿨다. React의 `Paging` 컴포넌트는 이미 받은 `paging`·`setPaging`으로 page 변경을 일으켰다.
5. **3교시 테스트 — 페이징 결과 확인:** 상품 메뉴 첫 화면에 6개가 보이는지 확인하고, MySQL의 id 내림차순 `LIMIT`·`OFFSET` 조회로 첫째 page와 둘째 page가 어떤 행 구간인지 대조했다.
6. **4교시 — 검색 값의 화면 모델:** Page 조회 API 용어를 짧게 확인한 뒤 `SearchCondition.ts`에 기간·카테고리·검색 mode·keyword의 type과 초기값을 만들었다. `FieldSearch.tsx`는 select와 text input을 이 state에 연결하고 paging 상태 문구도 표시했다.
7. **5교시 — 검색 요청 parameter 연결:** `ProductList`에 `searchCondition` state와 `FieldSearch`를 추가했다. 네 검색값을 GET parameter와 `useEffect` 의존성에 넣어 입력이 바뀌면 같은 상품 목록 endpoint를 다시 요청하도록 했다.
8. **5교시 — Spring 검색 전달 객체 준비:** `SearchDto`에 화면의 기간·카테고리·검색 mode·keyword를 대응시켰다. 그러나 이날 Controller의 Page endpoint는 아직 page 번호와 크기만 받으므로 DTO 생성만으로 검색이 DB에 적용된 것은 아니다.
9. **6교시 — CSR/SSR 용어 보충:** 브라우저와 서버 중 어디에서 화면을 만드는지를 짧게 비교했다. 원본의 “과거/현대 방식” 표기는 지나치게 단순하므로, 이날 상품 요청 구현과 별개의 용어 보충으로만 본다.
10. **7교시 — LIKE 복습과 Specification 시작:** SQL `LIKE`의 앞·중간·뒤 문자열 검색을 복습한 뒤 `ProductSpecification`에 기간, 카테고리, 상품명 포함, 설명 포함 조건을 각각 만드는 메서드를 작성했다. 이 조건들을 조합해 Repository에 넘기는 단계는 다음 날이다.
11. **7교시 후반 — Generic 보충:** 특정 데이터 type 범위를 미리 정하는 개념을 짧게 복습했다. 빈 8교시에는 새 구현 내용이 없다.

## 대표 artifact

| 구간 | 대표 artifact | 오늘 맡은 역할 | 완료 수준 |
|---|---|---|---|
| page 화면 상태 | `PagingInfo`, `Paging.tsx`, ProductList paging state | page control 클릭과 현재 page metadata 표시 | 요청·응답과 연결됨 |
| page 요청 | ProductList의 GET parameters·`useEffect` | `pageNumber`·`pageSize`를 보내고 변경 시 재요청 | 연결됨 |
| page 응답 | `Page<Product>`와 `response.data.content` | 상품 배열과 전체 건수·page 수·현재 page 정보를 분리 | 연결됨 |
| 검색 화면 | `SearchCondition.ts`, `FieldSearch.tsx` | 네 검색값을 controlled input state로 관리 | UI와 request parameter 연결됨 |
| 검색 전달 | `SearchDto` | React 검색값을 받을 Java 객체 모양 정의 | 생성됨, Controller 연결은 다음 날 |
| 검색 조건 | `ProductSpecification` | 기간·카테고리·상품명·설명 Predicate 생성 | 개별 조건 작성, Repository 조합은 다음 날 |

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| `Paging`에서 바뀐 page 번호 | paging state 변경→`useEffect` 재실행→page parameter GET→Controller의 `PageRequest`→Repository page 조회 | `content`는 상품 카드로, page metadata는 `Paging` 상태로 반영 |
| 기간·카테고리·mode·keyword 입력 | `FieldSearch`의 `handleChange`가 `searchCondition` 갱신→의존성 변화→검색 parameter를 포함한 GET | 요청에는 값이 실리지만 이날 백엔드는 아직 네 검색 parameter를 소비하지 않음 |
| `SearchDto`의 값 | `ProductSpecification`의 개별 조건 생성 준비 | 실제 조건 조합·Repository 검색은 04-22에 완성 |

## UI control과 실제 연결의 경계

- 04-20에는 Paging control과 ProductList state를 만들었지만 서버 Page 왕복은 아직이었다.
- 오늘 1~3교시에 page control→parameter→Spring Page→React metadata 왕복이 연결됐다.
- 오늘 4~5교시에 검색 form→state→request parameter는 연결됐다.
- `SearchDto`와 `ProductSpecification`도 오늘 작성했지만, Controller→Service→Repository의 검색 조건 조립은 다음 날이다. 따라서 “04-21에 전체 검색 기능이 완성됐다”고 요약하면 안 된다.

## 헷갈린 점 / 질문

- **`response.data`와 `response.data.content`:** 전체 목록 응답에서는 body 자체가 배열이었지만 Spring Page 응답에서는 body 안의 `content`가 상품 배열이고 나머지는 page metadata다.
- **`pageNumber`의 기준:** Spring page 번호는 0부터 시작하지만 화면 상태 문구는 사람에게 보여 줄 때 1을 더했다. 내부 번호와 표시 번호를 섞으면 이동 계산이 어긋난다.
- **optional chaining과 nullish coalescing:** `pageable?.pageNumber`는 중간 값이 없을 때 안전하게 접근하고, `??`는 null 또는 undefined일 때 기본값을 선택한다.
- **검색 input 변경과 page 번호:** 검색 조건 변화가 요청을 다시 실행하지만, 원본에는 검색할 때 page를 0으로 되돌리는 별도 처리까지 확인되지 않는다.
- **Querydsl과 Specification:** 교시 중 Querydsl 관련 Page API 용어가 언급됐지만 실제 작성한 동적 조건 코드는 Spring Data JPA `Specification`이다.

## 직접 수업과 후속 확장 경계

- 직접 구현: ProductList page 요청·Page 응답 처리, Spring의 단순 Pageable 조회, SearchCondition·FieldSearch, 검색 parameter, SearchDto, ProductSpecification 시작.
- 다음 날짜 직접 구현: 검색 조건 조립, sort/page 생성, `Specification + Pageable` Repository 조회, Controller 응답, MySQL 검색 시나리오.
- Linux·AWS·CI/CD는 이 애플리케이션의 실행·배포·자동화 후속 과목이고, Passwordless는 별도 인증 과목이다. CSR/SSR·LIKE·Generic은 이날 구현을 설명하는 보충 학습이지 별도 기능 완성 단계가 아니다.

## 관련 페이지

- [[concepts/pagination-search|페이징과 검색]]
- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
