---
title: MySQL
created: 2026-07-01
updated: 2026-07-16
type: entity
tags: [sql, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# MySQL

## 정의

MySQL은 관계형 데이터베이스 관리 시스템(RDBMS)이다. 이 과목에서는 Spring Boot/JPA가 연결되는 로컬 DBMS이자, Member·Product·Cart·Order 데이터와 페이징·검색 SQL을 Workbench에서 확인하는 실행환경으로 사용했다.

## 왜 중요한가

선행 Oracle 수업에서 SQL과 무결성·정규화를 직접 배운 뒤, FrontEnd_BackEnd 과목에서는 Java Entity와 Repository가 실제 DB 행·관계를 읽고 쓰는 환경으로 전환했다. React 화면의 state가 사라져도 데이터가 남고, Service의 재고·Cart·Order 규칙을 table/query 관점에서 대조할 수 있었다.

## 첫 등장: Oracle 직접 SQL에서 MySQL/JPA 환경으로 전환

[[summaries/2026-03-30-fullstack-environment-setup|03-30]]에 MySQL Server와 Workbench를 설치하고 `coffee` DB, JDBC datasource, MySQL dialect 설정을 준비했다. 이는 Oracle schema에서 SQL을 직접 실행하던 수업과 다른 runtime이다.

- Oracle의 `SEQUENCE.NEXTVAL`과 MySQL/JPA의 `@GeneratedValue(strategy = GenerationType.AUTO)`는 같은 구현이 아니다.
- 원본은 `GenerationType.AUTO` 사용을 보여 주지만 실제 MySQL AUTO_INCREMENT 전략과 생성 SQL을 확정하지 않는다.
- Oracle SQL 문법 예시와 04-21~04-22 MySQL LIMIT/OFFSET·CTE/UPDATE·INTERVAL·LIKE 시나리오를 하나의 SQL dialect로 합치지 않는다.

## 대표 artifact와 입력 → 처리 → 결과

| 날짜·도메인 | 대표 DB artifact | 입력·처리 | 원본에서 확인된 결과 범위 |
|---|---|---|---|
| 03-30 환경 | `coffee`, datasource URL, MySQL driver/dialect | Spring Boot가 localhost MySQL 연결 설정 사용 | 설정 작성과 Workbench 준비 확인 |
| 04-02~04-03 Member | `members`, Member JPA, `MemberRepository` | Entity mapping·`save`, 회원 seed/조회 | Workbench에서 members 조회 절차와 seed 3건 기록 |
| 04-08 Product | `products`, Product Entity/Repository | JPA table 생성, 이미지 기반 seed | Hibernate create table 문구와 `desc products` 구조 기록 |
| 04-13~04-15 Cart | `carts`, `cart_products`, Member/Product JOIN | Cart/CartProduct 저장·수량 변경·삭제 뒤 SQL 대조 | table 조회와 JOIN 시나리오가 원본에 있음; 결과 행 전문은 없음 |
| 04-16~04-20 Order | `Order`, `OrderProduct`, `OrderRepository` | 주문 저장·상태·재고 차감/복원 | Entity/JPA/JPQL 구현은 확인되지만 실제 table 구조·결과 행을 임의 확정하지 않음 |
| 04-21 page | `products` LIMIT/OFFSET | page 0/1을 size 6으로 조회 | 1·2페이지 SQL과 화면의 6개 표시 시나리오 기록 |
| 04-22 search | products 날짜·category·name·description 조건 | CTE/UPDATE로 날짜 준비 후 기간·category·LIKE SQL 대조 | SQL 시나리오는 확인되나 API의 확정 결과 건수는 기록되지 않음 |

## 실제 schema·table·query에서 확인된 범위

### 직접 확인 가능한 내용

- 04-02의 `Member`는 `members`와 `member_id`, email·role·regdate 등의 mapping을 작성했다.
- 04-08의 `products`는 `desc products` 표에 product_id, category, description, image, inputdate, name, price, stock이 기록돼 있다.
- 04-14에는 members→carts→cart_products→products JOIN SQL을 작성해 회원별 Cart 품목·수량·가격·재고를 대조했다.
- 04-21에는 `ORDER BY product_id DESC LIMIT 6 OFFSET 0/6`, 04-22에는 기간·category·name/description LIKE 조건 시나리오를 작성했다.

### 미확정 또는 과장 금지

- Entity와 annotation이 보인다고 실제 DB table DDL·constraint가 모두 원본에 보존된 것은 아니다.
- Order/OrderProduct는 Java Entity와 저장 흐름을 확인했지만 이 페이지에서 원본에 없는 실제 table column·결과 행을 만들지 않는다.
- 04-22 SQL 시나리오와 Spring Specification 호출 코드는 확인되지만, `JpaSpecificationExecutor` 상속·날짜 type 정합성·API 성공 결과가 미확정이다.
- Workbench에서 query를 작성했다는 사실과 특정 결과 건수/출력을 확인했다는 사실을 합치지 않는다.

## 자주 헷갈리는 원인

- **Oracle vs MySQL:** 둘 다 RDBMS지만 dialect, 번호 생성, 도구와 이 과목의 runtime이 다르다. Oracle 직접 학습은 [[entities/oracle-database|Oracle Database]]에 둔다.
- **SQL vs JPQL:** MySQL SQL은 table/column을, JPQL은 Entity/field를 대상으로 한다. [[comparisons/jpql-vs-sql|JPQL vs SQL]]에서 비교한다.
- **JPA Entity vs table:** Entity mapping은 DB 구조와 연결되지만 Java 객체와 DB 행이 같은 객체는 아니다.
- **GeneratedValue vs Oracle sequence:** `AUTO` annotation을 Oracle `NEXTVAL`의 다른 표기처럼 설명하면 안 된다. [[concepts/oracle-sequence|Oracle 시퀀스]]에서 경계를 확인한다.
- **schema 확인 vs 기능 완료:** table이나 query가 보인다고 React→Spring→DB 왕복 전체가 자동 완료되는 것은 아니다.

## 이전 개념과 이후 기능 연결

- 선행: Oracle의 DDL/DML/DQL·PK/FK·JOIN·정규화가 Member/Product/Cart/Order 관계를 읽는 기반이 됐다.
- 과목 내부: [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]가 Entity 중심 DB 접근을, [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]이 FK owning side를, [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]이 SQL 대조까지의 왕복을 설명한다.
- 후속: Linux Docker/Compose와 AWS RDS에서는 DB 실행 위치와 운영환경이 확장된다. 03-30~04-22 로컬 MySQL 실습에 이 후속 배포를 소급하지 않는다.

## 날짜별 학습 이력

- **03-30:** MySQL/Workbench 설치, coffee DB와 datasource/dialect 설정.
- **04-02~04-03:** Member JPA mapping·Repository 저장과 Workbench 확인.
- **04-08~04-13:** Product schema/seed·CRUD와 Cart 관계 Entity 시작.
- **04-14~04-15:** Cart 저장·목록·수량 변경을 members/carts/cart_products/products SQL로 대조.
- **04-16~04-20:** Order/OrderProduct 저장·상태·재고 처리와 JPQL 적용.
- **04-21~04-22:** LIMIT/OFFSET page SQL에서 기간·category·LIKE 다중 검색 SQL로 확장.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/oracle-database|Oracle Database]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]
- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]
- [[comparisons/jpql-vs-sql|JPQL vs SQL]]

## 출처

- frontmatter에 선언한 03-30·04-02~04-03·04-08·04-13~04-16·04-20~04-22 날짜 MD