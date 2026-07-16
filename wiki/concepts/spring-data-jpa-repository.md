---
title: Spring Data JPA Repository
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [spring-boot, backend, java]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---
# Spring Data JPA Repository

## 정의

이 수업의 Spring Data JPA Repository는 **Entity type과 id type을 선언한 interface를 통해 기본 CRUD를 얻고, method 이름·JPQL·Pageable·Specification 호출로 DB 접근 요구를 확장한 계층**이다. JPA 관계 자체는 [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]], 조건 조립은 [[concepts/spring-data-jpa-specification-pageable|Specification과 Pageable]]에 위임한다.

## 왜 중요한가

Member·Product·Cart·Order의 Service가 `save`, `findById`, 관계 조회, 상태 조회, page 검색을 모두 필요로 하면서 Repository가 “파일 하나를 만들면 끝”이 아니라 도메인 요구에 따라 자라는 과정을 보여 줬다. 특히 원본의 method 선언과 Service 호출 이름이 어긋난 지점, 04-22 검색 코드의 실행 전제가 확인되지 않은 지점을 보존해야 실제 학습 상태를 과장하지 않는다.

## 처음 등장하고 확장된 날짜

| 날짜 | Repository/DB 접근 확장 | 대표 artifact |
|---|---|---|
| [[summaries/2026-03-30-fullstack-environment-setup|03-30]]~[[summaries/2026-03-31-spring-boot-controller-html|03-31]] | Fruit class와 Controller의 객체/List 생성·반환 | `Fruit`, `FruitController` — 아직 JPA Repository가 아님 |
| [[summaries/2026-04-02-react-bootstrap-homepage|04-02]] | 첫 JPA interface 선언 | `MemberRepository extends JpaRepository<Member, Long>` |
| [[summaries/2026-04-03-spring-member-seed-react-comments|04-03]] | seed `save()`와 email derived query | `findByEmail`, `memberRepository.save` |
| [[summaries/2026-04-08-product-domain-oci|04-08]] | Product 기본 CRUD와 id 내림차순 목록 | `ProductRepository`, `findProductByOrderByIdDesc` |
| [[summaries/2026-04-14-cart-service|04-14]] | 관계 기준 Cart 조회와 여러 Repository 조합 | `findByMember`, `findById`, Cart/CartProduct save |
| [[summaries/2026-04-16-cart-quantity-stock|04-16]]~[[summaries/2026-04-17-cart-total-array-some|04-17]] | Order 저장과 member/status별 PENDING 목록 조회 | `OrderRepository`와 derived query |
| [[summaries/2026-04-20-order-list-scenario|04-20]] | method 이름으로 표현하기 어려운 상태 변경 | `@Query` JPQL `updateOrderStatus` |
| [[summaries/2026-04-21-product-pagination-search-react|04-21]]~[[summaries/2026-04-22-product-repository-pageable-search|04-22]] | `Pageable` 목록에서 Specification+Pageable 호출로 확장 | `findAll(spec, pageable)` |

## 접근 방식의 구분

### 1. `JpaRepository` 기본 CRUD

`MemberRepository`와 `ProductRepository`는 Entity/id type을 지정해 `save`, `findById`, `findAll`, `deleteById` 같은 기본 기능을 사용했다. 04-08 이후 Product 등록·수정·삭제, 04-14 Cart 저장, 04-16 Order 저장도 이 기본 기능을 Service에서 호출했다.

03-30의 Fruit는 `entity` package 이름을 사용했지만 `@Entity`·Repository 저장이 확인되지 않고, 03-31 Controller가 직접 객체/List를 만들어 반환했다. Fruit를 JPA 저장/조회 구현으로 소급하지 않고 **Repository 도입 전 데이터 객체 단계**로 둔다.

### 2. method 이름 기반 query

- Member: `findByEmail(String email)`로 email 회원을 조회했다.
- Product: `findProductByOrderByIdDesc()`로 id 내림차순 목록을 조회했다.
- Cart: `findByMember(member)`로 회원의 Cart를 조회하고 Service가 없으면 생성했다. CartProduct의 Cart+Product 관계 조회는 관계 mapping 세부와 함께 다음 세션에서 다룬다.
- Order: 04-17 Repository 선언부는 `findByMemberIdAndStatusOrderByIdDesc`, `findByStatusOrderByIdDesc`를 제시했다.

### 3. `@Query`/JPQL

04-20 `updateOrderStatus`는 `@Modifying`, transaction, `@Query`를 사용해 Order Entity의 `orderStatus`를 id 조건으로 바꿨다. SQL table명이 아니라 Entity·field를 사용하는 JPQL 예시였으며, 단순 조회 derived query와 구분한다.

### 4. `Pageable`

04-21 단순 상품 page 조회에서는 `PageRequest.of(pageNumber, pageSize, sort)`를 만들고 Repository `findAll(pageable)` 결과를 `Page<Product>`로 반환했다. Pageable은 page 번호·크기·정렬 요청이고 Page는 content·전체 개수·전체 page 같은 결과다.

### 5. `Specification`+`Pageable` 호출

04-22 원본은 ProductRepository에 `findAll(Specification<Product> spec, Pageable pageable)` 선언을 추가하고, Service가 여러 조건과 id 내림차순 PageRequest를 만들어 해당 method를 호출하는 코드를 기록했다. Controller는 query parameter를 `SearchDto`로 묶어 Service에 넘기고 Page를 응답했다.

## 입력 → 처리 → 결과

| 입력 | Repository 호출 | 결과/후속 처리 |
|---|---|---|
| Signup Member | `findByEmail` 중복 확인→`save` | 중복 오류 또는 encoded password·role·date 저장 |
| Product list/id/form | derived 목록, `findById`, `save`, `deleteById` | 목록·상세·등록·수정·삭제 Service 결과 |
| 인증 email+Cart DTO | Member/Product 조회→Cart 관계 조회→Cart/CartProduct 저장 | 기존 수량 누적 또는 새 품목, DTO 목록 변환 |
| Order DTO | Member/Product 조회→Order `save` | Order와 품목 저장, 재고/Cart 후속 변경 |
| memberId·role·PENDING | 역할별 derived query 호출 | Order Entity 목록→`OrderDetailDto` 목록 |
| orderId·status | JPQL update method | 상태 변경 건수/Service message |
| SearchDto+page 정보 | `findAll(spec, pageable)` | 조건부 `Page<Product>` 호출 코드 |

## 원본 불일치와 미확정 경계

### 04-17 Order method 이름

Repository 선언은 `findByMemberIdAndStatusOrderByIdDesc`와 `findByStatusOrderByIdDesc`인데, 같은 원본의 Service 코드는 `findByMemberIdAndOrderStatusOrderByIdDesc`와 `findByOrderStatusOrderByIdDesc`를 호출한다. `status`와 Entity field명으로 보이는 `orderStatus`가 섞였으므로 임의로 한 이름으로 통일하지 않는다. 선언과 호출이 그대로라면 compile/실행 정합성을 별도로 확인해야 한다.

### 04-22 Specification 실행 전제

- 04-08에 확인되는 ProductRepository 전체 선언은 `JpaRepository<Product, Long>` 상속이다.
- 04-22에는 `findAll(Specification<Product>, Pageable)` method 한 줄을 추가하지만 `JpaSpecificationExecutor<Product>` 상속은 원본에서 확인되지 않는다.
- 별도 method 선언만으로 Spring Data가 Specification 실행을 자동 제공하는지 단정하지 않는다.
- Product Entity의 `inputdate`는 `LocalDate`인데 04-21 `hasDateRange`는 `LocalDateTime` startDate를 `greaterThanOrEqualTo(root.get("inputdate"), startDate)`에 사용한다. type 정합성이 확인되지 않았다.
- 04-22는 Service/Controller 호출 코드와 MySQL 검색 시나리오를 기록했지만 실제 API 실행 성공 로그·응답 전문·확정 건수는 없다. 따라서 **호출 코드 작성**과 **검색 실행 검증 완료**를 분리한다.

## 자주 헷갈리는 원인

- **interface만 만들면 모든 query가 생긴다고 생각하기:** 기본 CRUD, derived query, JPQL, Specification executor는 근거와 전제가 다르다.
- **method 선언과 Service 호출을 눈으로 보정하기:** 04-17 이름 불일치는 학습 자료의 검증 대상이지 임의 수정 대상이 아니다.
- **save의 의미를 모두 insert로 보기:** id와 영속 상태에 따라 수정 흐름에서도 `save`가 사용됐다.
- **관계 조회와 관계 mapping을 합치기:** 이 페이지는 Repository method와 호출을 다루고 FK 주인·cascade·fetch는 다음 세션 concept에 위임한다.
- **Pageable과 Specification을 같은 객체로 보기:** 전자는 page/sort, 후자는 조건식이다.
- **코드 존재와 실행 성공:** 04-22의 호출 코드만으로 executor 상속·date type 문제까지 해결됐다고 볼 수 없다.

## 이전 개념과 이후 기능 연결

- 선행: Oracle의 [[concepts/oracle-ddl-dml-transaction|DDL·DML·transaction]]과 Java interface/generics가 Repository 선언 이해의 기반이다.
- 계층 경계: [[comparisons/controller-service-repository|Controller vs Service vs Repository]]의 일반 책임과 [[concepts/dto-entity-service-controller|데이터 모양 변환]]을 이어받는다.
- 관계 확장: [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]에서 Member–Cart–CartProduct–Product, Order–OrderProduct를 다룬다.
- 검색 확장: [[concepts/spring-data-jpa-specification-pageable|Specification과 Pageable]], [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]], [[concepts/pagination-search|페이징과 검색]]으로 이어진다.

## 직접 수업·교안·후속 경계

- **직접 수업:** 03-30~03-31 Fruit baseline, 04-02~04-03 Member Repository, 04-08 Product, 04-14 Cart, 04-16~04-20 Order, 04-21~04-22 page/search 호출이다.
- **교안 보충:** P08의 JPA/Repository 설명은 날짜 MD에 필요한 선언과 호출이 전사돼 있어 PDF를 source에 추가하지 않았다.
- **후속 과목:** Linux·AWS·CI/CD는 DB 접근 코드의 실행·배포 환경이고, Passwordless·중간 프로젝트 Repository는 별도 확장이다. 후속 성공 여부를 4과목의 04-22 검색 실행 검증으로 소급하지 않는다.

## 관련 페이지

- [[summaries/2026-04-03-spring-member-seed-react-comments|2026-04-03 Member seed와 Repository]]
- [[summaries/2026-04-22-product-repository-pageable-search|2026-04-22 Product Repository·Pageable 검색]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[concepts/pagination-search|페이징과 검색]]
- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]

## 출처

- 위 frontmatter의 03-30~04-22 날짜별 Repository 선언·호출 MD
