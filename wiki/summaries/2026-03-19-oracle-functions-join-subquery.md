---
title: 2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A06.함수 실습.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql
status: growing
confidence: high
---

# 2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리

## 한 줄 요약

`dual`로 함수 테스트를 시작해 문자열/숫자/날짜 함수, 그룹 함수, `GROUP BY/HAVING`, JOIN, 서브쿼리까지 DQL 심화 흐름을 배운 날이다.

## 배운 내용

- `dual`은 SYS가 가진 1행 1열 테스트용 테이블이며 모든 사용자가 함수 검증에 사용할 수 있다.
- SQL 함수는 Java 메서드처럼 입력값을 받아 결과를 만든다고 이해했다.
- 문자열 함수 `upper`, `lower`, `length`, `substr`, `replace`, `instr`, `trim` 등을 다뤘다.
- 숫자 함수 `abs`, `round`, `trunc`, `ceil`, `floor`, `sqrt`와 날짜 계산을 실습했다.
- 단일행 함수와 그룹 함수의 차이를 배웠다.
- `GROUP BY`는 범주형 컬럼으로 묶고, `HAVING`은 그룹 결과에 조건을 거는 문법으로 정리했다.
- `members`와 `boards`를 이용해 equi join, ANSI join, outer join, alias를 배웠다.
- 단일행/다중행/다중컬럼 서브쿼리를 구분했다.

## 실습 / 예제

```sql
select 5*3 from dual;
select power(2, 10) from dual;
select upper('hello'), lower('HELLO') from dual;
select mod(14, 5) from dual;
```

```sql
SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
HAVING count(*) >= 3
ORDER BY company;
```

```sql
SELECT m.id, m.Name, count(writer) AS cnt
FROM members m LEFT OUTER JOIN BOARDS b
ON m.id = b.writer
GROUP BY m.id, m.NAME
ORDER BY cnt DESC, m.name ASC;
```

```sql
SELECT name, manager
FROM MEMBERS
WHERE manager IN (SELECT id FROM members WHERE name IN('김구', '유관순'));
```

## 헷갈린 점 / 질문

- Oracle의 `substr` 시작 위치는 Java와 달리 1부터 시작한다.
- `WHERE`는 그룹화 전 행 필터링이고, `HAVING`은 그룹화 후 집계 결과 필터링이다.
- JOIN에서 alias를 쓰면 이후 컬럼 참조도 alias로 통일해야 한다.
- 서브쿼리 결과가 한 개인지 여러 개인지 먼저 판단해야 연산자를 고를 수 있다.

## 관련 페이지

- [[concepts/oracle-sql-functions|Oracle SQL 함수]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]
- [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]
- [[comparisons/oracle-inner-vs-outer-join|Oracle Inner Join vs Outer Join]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.217~225 `dual`/문자열 함수, p.296~310 그룹 함수, p.347~365 JOIN
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A06.함수 실습.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
