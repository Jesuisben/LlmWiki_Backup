---
title: Spring 상품 검색 흐름
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [spring-boot, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---
# Spring 상품 검색 흐름

## 정의

이 페이지는 **04-21 React의 검색 parameter가 04-22 Spring Controller의 `SearchDto`, Service의 `Specification` 조립, Repository 호출을 거쳐 `Page<Product>`로 돌아오는 실제 왕복**을 추적한다. 화면·DTO·조건 객체의 존재를 검색 완료로 보지 않고, 각 연결 시점과 DB 검증 범위를 분리한다.

## 왜 중요한가

검색 form에 값이 보이더라도 request에 실리지 않을 수 있고, request에 실려도 Controller가 받지 않거나 Service·Repository가 소비하지 않으면 DB 결과는 달라지지 않는다. 이 수업은 한 기능을 **control/state → request → backend 소비 → Page 응답 → DB 대조**로 나눠 확인하는 사례다.

## 처음 등장하고 확장된 날짜

| 날짜 | 검색 흐름에서의 위치 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-20-order-list-scenario|04-20]] | Paging control과 ProductList paging state 준비. 검색 control은 아직 없음 | `PagingInfo`, `Paging.tsx` |
| [[summaries/2026-04-21-product-pagination-search-react|04-21]] 오전 | page parameter와 단순 Pageable Page 왕복 완성 | ProductList GET params, `Page<Product>` |
| 04-21 오후 | 검색 control/state→request parameter, `SearchDto`, 개별 Specification 준비 | `SearchCondition`, `FieldSearch`, `ProductSpecification` |
| [[summaries/2026-04-22-product-repository-pageable-search|04-22]] | Controller 수신→DTO 조립→Service 조건 조립→Repository 호출 코드→Page 응답과 MySQL 시나리오 | `ProductController.listProducts`, `ProductService.listProducts` |

## 대표 artifact와 역할

| artifact | 계층 | 역할과 완료 시점 |
|---|---|---|
| `SearchCondition.ts` | React type/state | 기간·카테고리·mode·keyword의 화면 상태 모양 정의, 04-21 |
| `FieldSearch.tsx` | React UI | select/text control의 값을 state에 반영, 04-21 |
| ProductList GET parameters | React request | page와 네 검색값을 `/product/list` query parameter로 전송, 04-21 |
| `SearchDto` | Spring DTO | Controller가 받은 네 검색값을 Service에 전달할 모양, 04-21 작성·04-22 연결 |
| `ProductSpecification` | Spring 조건 생성 | 기간·카테고리·name/description predicate 제공, 04-21 |
| `ProductService.listProducts` | Spring Service | 필요한 조건만 `and`로 조립하고 sort·PageRequest 생성, 04-22 |
| `ProductRepository.findAll` | Spring Repository | Specification+Pageable 조회 호출의 최종 입구, 04-22 |
| `Page<Product>` | Spring→React 응답 | `content`와 전체 건수·page 수·현재 page metadata 전달 |
| MySQL Workbench SQL | DB 대조 | 기간·카테고리·LIKE·다중 조건의 의도 확인, 04-22 |

## 단계별 실제 왕복

### 1. 검색 control과 state

04-21 `FieldSearch`는 기간, 카테고리, 검색 mode, keyword control을 만들고 `handleChange`로 `SearchCondition` state를 갱신했다. 이 단계는 사용자의 선택을 브라우저 메모리에 반영한 것이며 DB 검색 자체가 아니다.

### 2. request parameter 생성

같은 날 ProductList는 `pageNumber`, `pageSize`와 함께 `searchDateType`, `category`, `searchMode`, `searchKeyword`를 GET parameter에 넣었다. 네 검색 state를 `useEffect` 의존성에도 추가해 값이 바뀌면 요청을 다시 보냈다.

그러나 당시 Spring Page endpoint는 page 번호·크기만 받았다. 따라서 **검색값이 network request에 포함된 것**과 **backend가 검색에 사용한 것**은 다르다.

### 3. Controller parameter 수신과 SearchDto 조립

04-22 `/product/list` Controller는 page 번호·크기와 네 검색값을 `@RequestParam`으로 받고 `SearchDto`를 만들었다. React parameter 이름과 Controller 변수 이름을 맞춰야 같은 값이 전달된다. DTO는 조건을 실행하지 않고 Service로 묶어 보내는 전달 객체다.

### 4. Service의 Specification 조건 조립

Service는 빈 Specification에서 시작했다. 기간 값이 있으면 날짜 조건, category가 있으면 카테고리 조건을 추가했다. mode와 keyword가 함께 있을 때 `name`이면 상품명 포함, `description`이면 설명 포함 조건을 선택했다. `"name".equals(searchMode)`는 해당 문자열 분기에서 null 호출 오류를 피하기 위한 비교였다.

이후 Product id 내림차순 `Sort`와 page 번호·크기를 가진 `PageRequest`를 만들었다. 검색 조건과 page/sort는 한 조회에 들어가지만 서로 다른 책임이다.

### 5. Repository의 Specification+Pageable 호출

Service는 조립한 spec과 pageable을 ProductRepository의 `findAll(spec, pageable)`에 전달하는 코드를 작성했다. 04-22 원본은 이 method 한 줄을 Repository에 추가했지만 interface 전체에서 `JpaSpecificationExecutor<Product>` 상속은 확인되지 않는다. 따라서 이 단계를 **Repository 호출 코드 연결**로 기록하고 runtime 실행 성공과 구분한다.

### 6. Page 응답

Controller는 Service가 반환한 `Page<Product>`를 응답 body로 돌려주는 코드를 작성했다. 전날 React 처리 경로는 `response.data.content`를 Product 배열로, `totalElements`·`totalPages`·`pageable` 정보를 paging state로 나눴다.

### 7. MySQL 검색 결과 검증

04-22에는 Product 입고일을 날짜별로 분산한 뒤 1일·1주·1개월, `beverage`·`cake`, 카테고리+상품명, 카테고리+설명 조건을 MySQL SQL로 실행했다. 이는 Spring 조건과 같은 검색 의도를 DB에서 대조한 시나리오다.

다만 원본에는 애플리케이션 API의 실제 응답 전문이나 조건별 확정 건수가 없다. SQL 시나리오 실행을 곧바로 Specification API runtime 성공으로 바꾸어 말하지 않는다.

## 입력 → 처리 → 결과

| 단계 | 입력 | 처리 | 원본에서 확인되는 결과 |
|---|---|---|---|
| 화면 | select/text 변경 | FieldSearch→SearchCondition state 갱신 | control과 state 연결 |
| 요청 | page+네 검색 state | ProductList가 query parameter 생성·GET 재요청 | 04-21 request에 값 포함 |
| 수신 | Controller의 여섯 parameter | 네 검색값으로 SearchDto 생성 | 04-22 Service 입력 마련 |
| 조건 | SearchDto | 필요한 Specification만 `and`, id desc sort, PageRequest | Repository 호출 인자 마련 |
| 조회 | spec+pageable | ProductRepository `findAll` 호출 코드 | `Page<Product>` 반환 의도, runtime 성공 미확정 |
| 응답 | Product Page | Controller OK body→React `content`/metadata 분리 경로 | 코드상 왕복 연결 |
| DB 대조 | 기간·category·LIKE | MySQL WHERE·AND 시나리오 | 검색 의도별 DB 조회 확인, API 결과 건수는 미확정 |

## 구현 완료 범위와 실행 미확정 범위

### 확인되는 구현 범위

- 04-21 page control→parameter→단순 Pageable 조회→Page 응답→React metadata 왕복은 연결됐다.
- 검색 control/state, request parameter, `SearchDto`, 네 개의 개별 Specification은 04-21에 준비됐다.
- 04-22에는 Controller→SearchDto→Service 조건 조립→sort/PageRequest→Repository 호출→Page 응답 코드가 연결됐다.
- MySQL에서 기간·카테고리·포함 문자열·다중 조건 시나리오를 실행했다.

### 미확정 경계

- ProductRepository의 `JpaSpecificationExecutor<Product>` 상속은 원본에서 확인되지 않는다.
- Product의 `inputdate`는 `LocalDate`, 날짜 Specification의 비교값은 `LocalDateTime`이므로 Criteria type 정합성이 확인되지 않는다.
- category의 빈 기본값이 enum으로 변환되는 동작과 검색 조건 변경 시 page를 0으로 되돌리는 처리는 확인되지 않는다.
- 실제 API 성공 응답·확정 결과 건수는 없다. 따라서 “04-22 backend 검색 코드 연결”은 확인되지만 “모든 조합의 runtime 검색 성공”은 단정하지 않는다.

## Querydsl과 Specification

04-21에 Querydsl 관련 Page API 용어가 보충으로 등장했지만, 실제 상품 검색 구현 artifact는 Spring Data JPA `Specification`과 Criteria API다. Querydsl 검색 구현으로 합치지 않는다.

## 자주 헷갈리는 원인

- **control/state와 request:** 입력값이 화면 state에 있어도 query parameter를 만들지 않으면 서버로 가지 않는다.
- **request와 backend 소비:** parameter가 전송돼도 Controller·Service가 받지 않으면 DB 조건이 되지 않는다.
- **DTO와 query:** SearchDto는 값 묶음이며 WHERE 조건 자체가 아니다.
- **Specification과 PageRequest:** 검색 조건과 page/sort 요청이다.
- **Page 응답과 Product 배열:** Product 배열은 `content`이고 나머지는 metadata다.
- **MySQL SQL과 JPA runtime:** 같은 의도를 시험할 수 있지만 서로 다른 실행 경로다.
- **코드 연결과 실행 성공:** executor 상속·date type이 미확정이면 성공을 확정할 수 없다.

## 이전 개념과 이후 기능 연결

- 전체 계층 경계는 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], DTO 모양은 [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]가 맡는다.
- React 재요청 시점은 [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]], 전체 page/search 기능 허브는 [[concepts/pagination-search|페이징과 검색]]이 맡는다.
- Specification·Pageable의 객체별 책임과 미확정 실행 전제는 [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]], Repository 선언 이력은 [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]가 맡는다.
- 상품 CRUD·대표 상품 등 검색 이전 생명주기는 [[concepts/product-domain-flow|상품 도메인 기능 흐름]]에 위임한다.

## 직접 수업·교안·후속 과목 경계

- **직접 수업:** 04-21 React page/search 준비와 개별 Specification, 04-22 Controller·Service·Repository 연결 코드와 MySQL 시나리오다.
- **교안 보충:** P08(SpringBoot 교안)·P10(필드 검색 기능)의 필요한 내용은 R17·R18과 고도화된 날짜 Summary에 충분히 전사되어 있어 PDF를 직접 열거나 source에 추가하지 않았다.
- **후속 경계:** Linux·AWS·CI/CD는 서버 실행·배포·자동화이고 Passwordless·중간 프로젝트는 별도 인증·적용 범위다. 후속 과목을 이 검색 기능의 실행 성공 근거로 사용하지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
