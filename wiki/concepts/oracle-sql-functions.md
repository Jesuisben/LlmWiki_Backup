---
title: Oracle SQL 함수
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/Study/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/Study/2. Oracle/교육 자료/스크립트들/A06.함수 실습.sql
status: growing
confidence: high
---

# Oracle SQL 함수

## 정의

SQL 함수는 컬럼값이나 입력값을 받아 계산·변환·집계 결과를 만드는 도구다. 수업에서는 Java의 메서드와 비슷한 감각으로 이해했다.

## `dual` 테이블

`dual`은 SYS가 가진 1행 1열짜리 특수 테이블로, 간단한 계산과 함수 검증에 사용한다.

```sql
select 5*3 from dual;
select power(2, 10) from dual;
select upper('hello'), lower('HELLO') from dual;
```

## 문자열 함수

| 함수 | 역할 | 예시 |
|---|---|---|
| `length()` | 문자열 길이 | `SELECT LENGTH(NAME) FROM PRODUCTS;` |
| `substr()` | 문자열 일부 추출 | `substr(password, 1, 3)` |
| `||` / `concat()` | 문자열 결합 | `NAME || ' - ' || COMPANY` |
| `replace()` | 문자열 치환 | `REPLACE(NAME, '아', '★')` |
| `instr()` | 문자열 위치 찾기 | `instr(company, '가') > 0` |
| `lpad/rpad` | 패딩 | `lpad(company, 10, '*')` |
| `trim/ltrim/rtrim` | 공백/문자 제거 | `trim('  aa ')` |

Oracle의 `substr`는 Java와 달리 위치가 1부터 시작한다.

## 숫자·날짜 함수

```sql
SELECT abs(-5) FROM dual;
SELECT round(1234.567, 2), trunc(1234.567, 2) FROM dual;
SELECT ceil(1234.567), floor(1234.567) FROM dual;
SELECT sqrt(5) FROM dual;
SELECT NAME, INPUTDATE, SYSDATE - INPUTDATE AS DAYS_DIFF FROM PRODUCTS;
SELECT NAME, ADD_MONTHS(INPUTDATE, 1) AS NEXT_MONTH FROM PRODUCTS;
```

## 단일행 함수와 그룹 함수

| 구분 | 의미 | 예시 |
|---|---|---|
| 단일행 함수 | 각 행마다 하나의 결과 | `upper`, `substr`, `round` |
| 그룹 함수 | 여러 행을 묶어 하나의 결과 | `avg`, `count`, `max`, `min`, `sum` |

`count(*)`는 `NULL` 포함 전체 행 수, `count(expr)`는 해당 컬럼이 `NULL`이 아닌 행 수, `count(distinct expr)`는 중복 제거 후 개수다.

## GROUP BY와 HAVING

```sql
SELECT CATEGORY, AVG(PRICE) AS AVG_PRICE
FROM PRODUCTS
GROUP BY CATEGORY;

SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
HAVING count(*) >= 3
ORDER BY company;
```

`WHERE`와 `HAVING`의 차이는 [[comparisons/where-vs-having|WHERE vs HAVING]]에 정리했다.

## 관련 페이지

- [[summaries/2026-03-19-oracle-functions-join-subquery|2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]

## 출처

- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/Study/2. Oracle/교육 자료/오라클 교안.pdf` — p.217~225, p.296~310
- `raw/Study/2. Oracle/교육 자료/스크립트들/A06.함수 실습.sql`
