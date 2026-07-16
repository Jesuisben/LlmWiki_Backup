---
title: JPQL vs SQL
created: 2026-07-06
updated: 2026-07-16
type: comparison
tags: [spring, spring-boot, backend, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: high
---

# JPQL vs SQL

## 비교 목적

2026-04-20 주문 상태 변경 실습에서 “JPQL은 테이블 이름 대신 Entity 이름을 쓰고 대소문자를 구분한다”는 주의가 나왔다. Oracle/SQL을 먼저 배운 상태에서는 SQL과 JPQL이 비슷해 보여 헷갈리기 쉽다.

## 한눈에 보기

| 항목 | JPQL | SQL |
|---|---|---|
| 기준 대상 | JPA Entity와 필드명 | DB 테이블과 컬럼명 |
| 사용 위치 | Spring Data JPA `@Query`, EntityManager | DBeaver, DB 콘솔, native query |
| 장점 | DB 종류에 덜 종속적이고 객체 모델과 맞음 | DB 기능을 직접 쓰기 좋음 |
| 주의점 | Entity 이름/필드명 대소문자에 민감 | DB 스키마 이름과 문법에 민감 |

## 언제 무엇을 쓰는가

- 일반적인 JPA 조회/수정은 JPQL이나 Repository 메서드, Specification으로 처리한다.
- DB 고유 기능, 복잡한 성능 튜닝, 실제 스키마 확인은 SQL로 접근한다.
- FrontEnd_BackEnd 수업의 주문 상태 변경처럼 Entity 기반 업무 로직 안에서 쓰는 쿼리는 JPQL로 이해하는 것이 좋다.

### 구체적인 선택 상황

1. DBeaver에서 Oracle의 실제 `ORDERS` 테이블 행을 확인할 때는 SQL을 쓴다.
2. Spring Repository에서 `Order` Entity의 `orderStatus` 필드를 수정할 때는 04-20 수업처럼 JPQL `@Query`를 쓴다.

```sql
select * from orders ;
```

```java
@Modifying // 이 쿼리는 select 구문이 아니고, 데이터 변경을 위한 쿼리입니다.
@Transactional // import jakarta.transaction.Transactional; // 롤백할 수도 있으니까
@Query("update Order o set o.orderStatus = :status where o.id = :orderId")
int updateOrderStatus(@Param("orderId") Long orderId, @Param("status") OrderStatus status);
```

## Oracle 직접 수업과 후속 확장 경계

03월 Oracle 수업에서는 DBeaver에서 Oracle 테이블·컬럼을 대상으로 SQL을 실행했다. 03-30 FrontEnd_BackEnd 시작일에는 MySQL과 MySQL Driver, Spring Data JPA를 새 환경으로 설치했다. 위 JPQL 예제는 04-20 Spring Data JPA 수업의 후속 학습이며 Oracle 과목에서 직접 작성한 코드가 아니다. 04-22에는 긴 동적 조건을 JPQL 문자열 하나로 몰기보다 `Specification<Product>`와 `Pageable`을 조합하는 흐름까지 이어졌다.

## 헷갈리기 쉬운 포인트

SQL에서 `orders` 테이블을 조회하던 감각으로 JPQL에 테이블명을 쓰면 동작하지 않을 수 있다. JPQL에서는 Entity 이름과 필드명을 기준으로 쓰고, DBeaver에서 직접 실행하는 SQL은 실제 테이블/컬럼명을 써야 한다.

- JPQL이 “Oracle SQL의 별칭”인 것은 아니다. JPA가 Entity 모델을 기준으로 해석하는 질의 언어다.
- `Order` Entity 이름과 `orders` 테이블 이름, `orderStatus` 필드와 실제 컬럼 이름을 같은 층위로 섞지 않는다.
- 모든 조회를 JPQL로 직접 작성해야 하는 것은 아니다. 간단한 조건은 Repository 메서드, 동적 조건은 수업의 Specification 방식이 선택지가 된다.

## 관련 페이지

- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
