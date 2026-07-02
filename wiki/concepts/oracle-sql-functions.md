---
title: Oracle SQL 함수
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md
status: growing
confidence: high
---
# Oracle SQL 함수

## 수업 흐름으로 보는 핵심 설명

### 1. `dual` 테이블과 함수 실습

`dual`은 Oracle에서 간단한 계산이나 함수 테스트를 할 때 쓰는 1행 1열짜리 특수 테이블이다.

```sql
select 계산식 from dual;
```

수업에서는 다음처럼 `dual`을 계산기처럼 사용했다.

```sql
select 5*3 from dual;
select power(2, 10) from dual;
select upper('hello'), lower('HELLO') from dual;
select mod(14, 5) from dual;
```

여기서 중요한 연결점은 **SQL 함수가 Java 메서드와 비슷한 역할을 한다**는 점이다. 원본 노트에서도 `upper`, `lower`를 Java의 문자열 메서드와 연결해서 이해하려고 했다.

### 2. 문자열 함수

수업에서 다룬 주요 문자열 함수는 다음과 같다.

| 함수 | 역할 | 예시 |
|---|---|---|
| `length()` | 문자열 길이 | `SELECT LENGTH(NAME) FROM PRODUCTS;` |
| `substr()` | 문자열 일부 추출 | `select substr(password, 1, 3) from employees;` |
| `concat()` / `||` | 문자열 결합 | `SELECT NAME || ' - ' || COMPANY FROM PRODUCTS;` |
| `replace()` | 특정 문자열 치환 | `REPLACE(NAME, '아', '★')` |
| `instr()` | 문자열 위치 찾기 | `instr(company, '가') > 0` |
| `lpad()`, `rpad()` | 왼쪽/오른쪽 패딩 | `lpad(company, 10, '*')` |
| `trim()`, `ltrim()`, `rtrim()` | 공백/문자 제거 | `trim('  aa ')` |

특히 `substr()`는 Java와 다르게 **Oracle의 시작 위치가 1부터 시작한다**는 점이 중요하다.

```sql
select substr(password, 1, 3) from employees;
select substr(password, 1) from employees;
select substr(password, -2, 2) from employees;
```

원본 노트에서는 `substr(password, 1, 3)`과 `substr(password, 1)`처럼 인자 개수가 달라지는 모습을 Java의 오버로딩과 비슷하게 연결해 이해했다.

### 3. 숫자 함수와 날짜 함수

숫자 함수는 값을 계산하거나 반올림/버림할 때 사용한다.

```sql
SELECT -5, abs(-5) FROM dual;
SELECT round(1234.567), trunc(1234.567) FROM dual;
SELECT round(1234.567, 2), trunc(1234.567, 2) FROM dual;
SELECT ceil(1234.567), floor(1234.567) FROM dual;
SELECT sqrt(5) FROM dual;
```

날짜 함수는 상품 입고일처럼 날짜 기준 검색을 할 때 중요하다.

```sql
SELECT NAME, INPUTDATE, SYSDATE - INPUTDATE AS DAYS_DIFF
FROM PRODUCTS;

SELECT NAME, ADD_MONTHS(INPUTDATE, 1) AS NEXT_MONTH
FROM PRODUCTS;
```

이후 Spring/React 상품 검색에서 “1일/1주일/1개월” 같은 기간 검색 조건으로 이어진다.

### 4. 단일행 함수와 그룹 함수

수업에서는 함수를 크게 두 종류로 나눴다.

| 구분 | 의미 | 예시 |
|---|---|---|
| 단일행 함수 | 각 행마다 하나씩 적용 | `upper`, `lower`, `substr`, `round` |
| 그룹 함수 | 여러 행을 모아 하나의 결과를 계산 | `avg`, `count`, `max`, `min`, `sum` |

그룹 함수 예시는 다음과 같다.

```sql
SELECT AVG(PRICE) AS AVG_PRICE FROM PRODUCTS;
SELECT MAX(PRICE) AS MAX_PRICE FROM PRODUCTS;
SELECT SUM(STOCK) AS TOTAL_STOCK FROM PRODUCTS;
```

`count`는 특히 헷갈리기 쉽다.

| 표현 | 의미 |
|---|---|
| `count(*)` | `NULL` 포함 전체 행 수 |
| `count(expr)` | 해당 컬럼이 `NULL`이 아닌 행 수 |
| `count(distinct expr)` | 중복을 제거한 개수 |

원본에서는 `count(*) - count(price)`로 `price`가 `NULL`인 개수를 구하는 예시도 다뤘다.

### 5. `GROUP BY`와 `HAVING`

`GROUP BY`는 특정 컬럼 기준으로 행을 묶는 문법이다.

```sql
SELECT category, count(*)
FROM products
GROUP BY category;
```

카테고리별 평균 가격이나 최고 가격도 구할 수 있다.

```sql
SELECT CATEGORY, AVG(PRICE) AS AVG_PRICE
FROM PRODUCTS
GROUP BY CATEGORY;
```

`HAVING`은 `GROUP BY` 결과에 조건을 거는 문법이다.

```sql
SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
HAVING count(*) >= 3
ORDER BY company;
```

헷갈리기 쉬운 핵심은 다음이다.

- `WHERE`: 행을 그룹화하기 **전**에 필터링한다.
- `HAVING`: `GROUP BY`로 묶은 **후** 그룹 결과를 필터링한다.
- `WHERE`에는 그룹 함수 조건을 직접 쓰기 어렵고, `HAVING`은 그룹 함수 조건에 사용한다.

## 관련 페이지

- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]

## 출처

- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
