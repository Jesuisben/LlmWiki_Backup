---
title: Spring Data JPA Specification과 Pageable
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [spring-boot, backend, java]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---
# Spring Data JPA Specification과 Pageable

## 정의

이 수업의 `Specification<Product>`는 선택된 상품 검색 조건을 Criteria predicate로 만들고 `and`로 조립하는 객체이고, `Pageable`은 page 번호·크기·정렬을 Repository 조회에 전달하는 객체다. `PageRequest`는 그 `Pageable`을 만드는 구현 방식으로 사용됐고, 조회 결과는 상품 배열만이 아니라 metadata를 포함한 `Page<Product>`로 돌아왔다.

## 왜 중요한가

기간·카테고리·상품명·설명 조건은 사용자가 무엇을 선택했는지에 따라 달라진다. 모든 조합마다 별도 Repository method를 만드는 대신 개별 `Specification`을 준비하고 필요한 조건만 결합하면 한 조회 경로로 여러 조합을 표현할 수 있다. 동시에 `Pageable`을 분리해 같은 조건 결과를 page 단위·id 내림차순으로 받게 했다.

## 이 수업에서 처음 등장하고 확장된 날짜

| 날짜 | 구현 수준 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-20-order-list-scenario|04-20]] | `PagingInfo`·`Paging.tsx`와 ProductList의 paging state/control 준비. 아직 기존 상품 목록 응답을 사용 | page control·state |
| [[summaries/2026-04-21-product-pagination-search-react|04-21]] 오전 | React page parameter→Controller의 `PageRequest`→단순 `findAll(pageable)`→`Page<Product>` 응답 왕복 | `Pageable`, `PageRequest`, `Sort`, `Page<Product>` |
| 04-21 오후 | 검색 state·request parameter·`SearchDto`와 기간·카테고리·상품명·설명 개별 조건 작성 | `ProductSpecification` |
| [[summaries/2026-04-22-product-repository-pageable-search|04-22]] | Service에서 조건을 조립하고 sort·`PageRequest`를 만든 뒤 Specification+Pageable Repository 호출 코드 연결 | `ProductService.listProducts`, `findAll(spec, pageable)` |

04-20의 control 준비, 04-21의 단순 page 왕복과 검색 조건 준비, 04-22의 조건부 조회 연결은 서로 다른 완료 단계다.

## 대표 객체의 책임

| 객체 | 수업에서 확인되는 책임 | 맡지 않는 책임 |
|---|---|---|
| `Specification<Product>` | Product 하나가 기간·카테고리·포함 문자열 조건을 만족하는지 표현 | page 번호·크기·정렬 |
| `ProductSpecification` | `hasDateRange`, `hasCategory`, `hasNameLike`, `hasDescriptionLike` 개별 조건 제공 | HTTP parameter 수신과 Page 응답 |
| `Sort` | 상품 `id` 내림차순 정렬 표현 | 검색 WHERE 조건 |
| `PageRequest` | 0-based `pageNumber`, `pageSize`, sort를 받아 `Pageable` 생성 | 검색값을 DTO로 묶기 |
| `Pageable` | Repository에 page·size·sort 전달 | 조회 결과 목록과 전체 건수 보유 |
| `Page<Product>` | `content`, 전체 상품 수, 전체 page 수, 현재 page 등 결과 보유 | 검색 조건 생성 |

## 실제 수업 예시: 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| page 번호·크기 | 04-21 Controller가 id 내림차순 sort와 `PageRequest`를 만들고 Service의 단순 Pageable 조회 호출 | Product `content`와 page metadata를 가진 `Page<Product>` |
| 기간 선택 | 04-21의 `hasDateRange`가 선택값별 시작 시각을 계산하고 `inputdate` 비교 predicate 준비 | 04-22 Service에서 선택값이 있을 때 spec에 추가 |
| 카테고리 선택 | `hasCategory`가 ALL이면 전체 조건, 그 밖에는 category 일치 조건 준비 | 다른 조건과 `and` 조립 가능 |
| mode=`name` 또는 `description`과 keyword | 각각 name/description의 `%keyword%` LIKE 조건 선택 | 카테고리·기간 조건과 함께 조립 가능 |
| 조립된 spec+page 정보 | id 내림차순 `PageRequest` 생성→Repository `findAll(spec, pageable)` 호출 코드 | 조건부 Product Page 반환 의도 |

04-22 Service는 빈 Specification에서 시작해 값이 있는 조건만 `spec.and(...)`로 누적했다. 문자열 SQL을 직접 합친 것이 아니라 Criteria 조건 객체를 조립한 것이다. Oracle에서 배운 `WHERE`·`AND`와 목적은 연결되지만 구현 계층과 API는 다르다.

## 구현 완료 범위와 실행 미확정 범위

### 원본에서 확인되는 범위

- 04-21에는 page parameter와 `Page<Product>` 응답이 React의 `content`·metadata 처리까지 연결됐고 MySQL `LIMIT`·`OFFSET` 시나리오도 확인했다.
- 같은 날 검색 control/state, GET parameter, `SearchDto`, 네 개의 개별 Specification을 작성했다.
- 04-22에는 Controller의 검색 parameter 수신, Service 조건 조립, `Sort`·`PageRequest`, Repository의 Specification+Pageable 호출 코드를 작성했다.
- MySQL에서는 기간·카테고리·상품명/설명 포함과 다중 `AND` 조건을 별도 SQL로 시험했다.

### 실행 성공을 단정하지 않는 범위

- 04-08의 ProductRepository 전체 선언에서는 `JpaRepository<Product, Long>`만 확인되고, 04-22 원본에는 method 한 줄을 추가하지만 `JpaSpecificationExecutor<Product>` 상속은 확인되지 않는다. 따라서 Specification 실행 기능이 실제 Repository 구성에 갖춰졌다고 단정하지 않는다.
- Product Entity의 `inputdate`는 04-08 원본에서 `LocalDate`이고, 04-21의 날짜 Specification은 `LocalDateTime` 시작값과 비교한다. 이 Criteria 비교의 type 정합성과 실행 성공은 원본만으로 확정할 수 없다.
- 04-22에는 실제 API 응답 전문·확정 결과 건수·성공 로그가 없다. **호출 코드 연결**과 **runtime 검색 성공**을 분리한다.
- category의 빈 기본값이 enum parameter로 변환되는 모든 실행환경 성공도 단정하지 않는다.

`JpaSpecificationExecutor`는 Specification 기반 조회의 실행 전제를 점검할 때 필요한 이름이지만, 이 수업에서 Repository가 실제로 상속했다고 기록된 artifact는 아니다.

## Querydsl과 실제 구현의 경계

04-21에는 Querydsl 관련 Page API 용어가 보충 설명으로 등장했다. 그러나 실제로 작성한 상품 조건 코드는 Spring Data JPA `Specification<Product>`와 Criteria API다. Querydsl로 상품 검색을 구현했다고 설명하지 않는다.

## 자주 헷갈리는 원인

- **Pageable과 Page:** 전자는 요청 조건, 후자는 조회 결과 wrapper다.
- **Specification과 Pageable:** 전자는 동적 WHERE 조건, 후자는 page·size·sort다. 한 Repository 호출에 함께 들어가도 같은 객체가 아니다.
- **control과 서버 조회:** 04-20에는 control만 준비했고, 04-21에 page 왕복이 연결됐다.
- **개별 조건과 조립:** 04-21에 네 조건을 만들었지만 Service 조립과 Repository 호출은 04-22다.
- **코드와 실행 검증:** 호출 형태가 적혀 있어도 executor 상속과 날짜 type이 미확정이면 runtime 성공을 확정할 수 없다.
- **검색 조건 변화와 page 초기화:** React 재요청은 확인되지만 조건 변경 시 page를 0으로 되돌리는 처리는 원본에서 확인되지 않는다.

## 이전 개념과 이후 기능 연결

- 선행 SQL: [[concepts/oracle-sql-functions|Oracle SQL 함수]]의 날짜·문자열 조건과 [[comparisons/where-vs-having|WHERE vs HAVING]]의 행 필터 관점이 동적 predicate 이해를 돕는다.
- Repository 선언·호출 이력은 [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]가 맡는다.
- frontend부터 DB까지의 기능 왕복은 [[concepts/pagination-search|페이징과 검색]], 실제 04-21~04-22 검색 계층 순서는 [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]이 맡는다.
- Product의 전체 생명주기는 [[concepts/product-domain-flow|상품 도메인 기능 흐름]]에 위임한다.

## 직접 수업·교안·후속 과목 경계

- **직접 수업:** 04-21의 단순 Pageable 왕복·검색 DTO/개별 Specification 준비와 04-22의 조건 조립·PageRequest·Repository 호출 코드다.
- **교안 보충:** inventory의 P08(SpringBoot 교안)·P10(필드 검색 기능)은 날짜 MD에 필요한 개념과 코드가 충분히 전사되어 있어 이번 페이지의 직접 source로 다시 추가하지 않았다.
- **후속 경계:** 같은 04-22에 시작한 Linux, 이후 AWS·CI/CD는 실행·배포 환경이고 Passwordless·중간 프로젝트는 별도 인증·적용 범위다. 이 후속 작업을 검색 runtime 성공 근거로 사용하지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
