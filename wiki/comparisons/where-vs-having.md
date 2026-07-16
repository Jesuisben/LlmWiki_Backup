---
title: WHERE vs HAVING
created: 2026-07-02
updated: 2026-07-15
type: comparison
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
status: growing
confidence: high
---

# WHERE vs HAVING

## 비교 목적

`WHERE`와 `HAVING`은 둘 다 조건을 거는 문법이지만, 조건이 적용되는 시점이 다르다. 2026-03-19 Oracle 수업에서는 `GROUP BY`와 함께 `HAVING`을 배우면서 이 차이가 중요해졌다.

## 한눈에 보기

| 항목 | WHERE | HAVING |
|---|---|---|
| 적용 시점 | 그룹화 전 | 그룹화 후 |
| 대상 | 개별 행(row) | 그룹 결과 |
| 그룹 함수 사용 | 직접 사용하기 어려움 | `count`, `avg`, `sum` 등 사용 |
| 함께 자주 쓰는 문법 | `SELECT ... FROM ... WHERE ...` | `GROUP BY ... HAVING ...` |
| 예시 질문 | 가격이 3500~4500원인 상품 | 상품이 3개 이상인 회사 |

## WHERE

`WHERE`는 테이블의 각 행을 먼저 필터링한다.

```sql
SELECT * FROM products WHERE price BETWEEN 3500 AND 4500 ;
```

이 문장은 상품 하나하나를 보면서 `price BETWEEN 3500 AND 4500` 조건에 맞는 행만 남긴다.

## HAVING

`HAVING`은 `GROUP BY`로 묶은 결과에 조건을 건다.

수업 예시는 회사별 상품 개수를 구하되, 3개 이상인 회사만 출력하는 것이었다.

```sql
SELECT COMPANY, COUNT(*) AS CNT
FROM PRODUCTS
GROUP BY COMPANY
HAVING count(*) >= 3
ORDER BY company;
```

여기서 `count(*)`는 회사별로 묶은 뒤에야 계산된다. 그래서 개별 행을 거르는 `WHERE`가 아니라 그룹 결과를 거르는 `HAVING`에 조건을 쓴다.

## 언제 무엇을 쓰는가

- 개별 행의 값으로 조건을 걸면 `WHERE`
- `GROUP BY`로 묶은 뒤의 집계 결과로 조건을 걸면 `HAVING`
- `count`, `avg`, `sum`, `max`, `min` 같은 그룹 함수 결과를 조건으로 쓰면 보통 `HAVING`

### 구체적인 선택 상황

1. 가격이 3500원 이상 4500원 이하인 **상품 행**만 조회하려면 `WHERE price BETWEEN 3500 AND 4500`을 쓴다.
2. 회사별로 묶은 뒤 상품이 3개 이상인 **회사 그룹**만 보고 싶으면 `HAVING COUNT(*) >= 3`을 쓴다.

둘을 함께 쓰면 먼저 행을 줄이고 그 결과를 그룹화할 수 있다.
이 페이지 위의 두 SQL은 수업에서 실제 사용한 행 필터 예제와 회사별 집계 예제다. 원본에 없는 결합 쿼리를 새로 만들지 않고, 실행 단계만 `WHERE → GROUP BY → HAVING` 순서로 연결해 이해한다.

## 헷갈리기 쉬운 포인트

`HAVING`은 `WHERE`의 고급 버전이 아니다. 역할이 다르다.

- `WHERE`: “그룹으로 묶기 전에 어떤 행을 제외할까?”
- `HAVING`: “그룹으로 묶고 계산한 뒤 어떤 그룹을 제외할까?”
- `HAVING`은 `WHERE`의 고급형도, `GROUP BY`의 별칭도 아니다.
- 집계 결과가 필요하다는 이유만으로 모든 조건을 `HAVING`에 몰아넣지 않는다. 개별 행 조건은 먼저 `WHERE`에서 줄이는 것이 질문 순서와 맞다.

## 관련 페이지

- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[summaries/2026-03-19-oracle-functions-join-subquery|2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
