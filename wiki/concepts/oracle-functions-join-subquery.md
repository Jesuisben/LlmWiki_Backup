---
title: Oracle 함수·조인·서브쿼리
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
status: growing
confidence: high
---
# Oracle 함수·조인·서브쿼리

## 정의

Oracle SQL에서 **함수(function)**는 컬럼 값을 가공하거나 계산하는 도구이고, **JOIN**은 여러 테이블을 공통 컬럼으로 연결하는 방법이며, **서브쿼리(subquery)**는 한 SQL 문 안에 다른 SQL 문을 넣어 조건이나 값을 만들어내는 방식이다.

## 왜 중요한가

상품명 검색, 카테고리별 상품 수, 게시글 작성자 이름 연결, 평균보다 높은 값 조회처럼 실제 웹서비스 조회 기능은 함수, JOIN, 서브쿼리 사고방식을 필요로 한다.

## 학습 흐름

2026-03-19 수업에서는 다음 순서로 SQL 조회 심화를 배웠다.

1. `dual` 테이블로 함수 실습
2. 문자열/숫자/날짜 함수
3. 단일행 함수와 그룹 함수
4. `GROUP BY`와 `HAVING`
5. JOIN
6. 서브쿼리
7. 단일행/다중행/다중컬럼 서브쿼리 구분

## 분리된 하위 주제

- [[concepts/oracle-sql-functions|Oracle SQL 함수]] — 문자열/숫자/날짜 함수, 단일행 함수와 그룹 함수, `GROUP BY`/`HAVING`
- [[concepts/oracle-join|Oracle JOIN]] — 여러 테이블을 연결하는 조회
- [[concepts/oracle-subquery|Oracle 서브쿼리]] — SQL 안의 SQL, 단일행/다중행/다중컬럼 서브쿼리

## 자주 헷갈리는 점

- `WHERE`는 그룹화 전 행 필터링, `HAVING`은 그룹화 후 집계 결과 필터링이다.
- JOIN은 테이블을 옆으로 연결하고, 서브쿼리는 한 쿼리 결과를 다른 쿼리 조건/값으로 사용한다.
- 서브쿼리 결과가 여러 행이면 `=` 대신 `IN`, `ANY`, `ALL` 같은 연산자를 고려해야 한다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-sql-functions|Oracle SQL 함수]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
