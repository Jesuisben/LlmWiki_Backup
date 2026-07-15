---
title: Oracle 함수·조인·서브쿼리
created: 2026-07-02
updated: 2026-07-15
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

이 페이지는 세 주제를 다시 축약하는 사전이 아니라 **03-19 수업의 탐색 지도**다. 함수가 값을 가공하고, 집계가 여러 행을 그룹 결과로 줄이고, JOIN이 여러 테이블의 컬럼을 옆으로 붙이며, 서브쿼리가 한 조회 결과를 다른 조회의 조건으로 넘긴다. 구체 문법과 오류는 위 하위 페이지에서 관리한다.

## 한 흐름으로 보는 실제 SQL

```sql
SELECT m.id, m.Name, count(writer) AS cnt
FROM members m LEFT OUTER JOIN BOARDS b
ON m.id = b.writer
group by m.id, m.NAME
ORDER BY cnt DESC, m.name ASC ;
```

이 쿼리에는 JOIN, 그룹 함수, `GROUP BY`, 정렬이 함께 들어간다. 그룹 결과 조건은 별도의 회사별 집계 예제에서 `HAVING count(*) >= 3`으로 확인했다. 반면 “최소 급여와 같은 회원”처럼 먼저 기준값을 계산해야 하는 질문은 `WHERE salary = (SELECT MIN(salary) ...)`처럼 서브쿼리로 바뀐다.

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
