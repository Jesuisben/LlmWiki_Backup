---
title: 단일행 서브쿼리 vs 다중행 서브쿼리
title_aliases: [Single-row Subquery vs Multi-row Subquery]
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
status: growing
confidence: high
---

# 단일행 서브쿼리 vs 다중행 서브쿼리

## 비교 목적

서브쿼리를 쓸 때 가장 먼저 판단해야 하는 것은 “서브쿼리 결과가 한 개냐, 여러 개냐”이다. 이 판단에 따라 `=`, `<`, `>` 같은 비교 연산자를 쓸지, `IN`, `ANY`, `ALL` 같은 다중행 연산자를 쓸지가 달라진다.

원본 노트에서도 “1대 2 관계라서 `=`을 쓰면 안 됨”이라고 중요하게 표시되어 있다.

## 한눈에 보기

| 항목 | 단일행 서브쿼리 | 다중행 서브쿼리 |
|---|---|---|
| 결과 개수 | 1개 값 | 여러 행/여러 값 |
| 주로 쓰는 연산자 | `=`, `<>`, `>`, `>=`, `<`, `<=` | `IN`, `ANY`, `ALL` |
| 예시 | 평균 급여보다 높은 사람 | 여러 관리자 밑의 직원 |
| 실수하기 쉬운 점 | 결과가 여러 개인데 `=` 사용 | 단일 값인데 불필요하게 복잡하게 작성 |

## 단일행 서브쿼리

서브쿼리 결과가 하나의 값이면 일반 비교 연산자를 쓴다.

```sql
SELECT name, salary
FROM members
WHERE salary > (SELECT avg(salary) FROM members);
```

`SELECT avg(salary) FROM members`는 평균 급여 하나를 반환한다. 그래서 `salary > (...)`처럼 비교할 수 있다.

최소 급여자를 찾는 예시도 단일행 서브쿼리다.

```sql
SELECT name, salary
FROM members
WHERE salary = (SELECT min(salary) FROM members);
```

## 다중행 서브쿼리

서브쿼리 결과가 여러 행이면 `=`이 아니라 `IN` 등을 사용해야 한다.

```sql
SELECT name, manager
FROM MEMBERS
WHERE manager IN (SELECT id FROM members WHERE name IN('김구', '유관순'));
```

여기서 서브쿼리는 `김구`, `유관순`의 id처럼 여러 값을 반환할 수 있다. 그러므로 `manager = (...)`처럼 하나의 값과 비교하면 맞지 않는다.

## 다중컬럼 서브쿼리와의 연결

수업 후반에는 여러 컬럼을 한꺼번에 비교하는 다중컬럼 서브쿼리도 다뤘다.

```sql
SELECT name, salary, gender
FROM MEMBERS
WHERE (gender, salary) IN (
  SELECT gender, min(salary)
  FROM members
  GROUP BY GENDER
);
```

이 경우에는 `(gender, salary)` 두 컬럼 조합이 서브쿼리의 `(gender, min(salary))`와 대응한다.

## 언제 무엇을 쓰는가

1. 서브쿼리만 따로 실행했을 때 결과가 1개인지 여러 개인지 생각한다.
2. 결과가 1개면 `=`, `<`, `>` 같은 비교 연산자를 쓴다.
3. 결과가 여러 개면 `IN`, `ANY`, `ALL` 같은 다중행 연산자를 쓴다.
4. 여러 컬럼 조합을 비교해야 하면 `(컬럼1, 컬럼2) IN (...)` 형태를 고려한다.

## 관련 페이지

- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]
- [[summaries/2026-03-19-oracle-functions-join-subquery|2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
