---
title: JPQL vs SQL
created: 2026-07-06
updated: 2026-07-09
type: comparison
tags: [spring, spring-boot, backend, sql]
sources:
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

## 헷갈리기 쉬운 포인트

SQL에서 `orders` 테이블을 조회하던 감각으로 JPQL에 테이블명을 쓰면 동작하지 않을 수 있다. JPQL에서는 Entity 이름과 필드명을 기준으로 쓰고, DBeaver에서 직접 실행하는 SQL은 실제 테이블/컬럼명을 써야 한다.

## 관련 페이지

- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/spring-data-jpa-specification-pageable|Spring Data JPA Specification과 Pageable]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
