---
title: Oracle 서브쿼리
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md
status: growing
confidence: high
---
# Oracle 서브쿼리

## 서브쿼리

서브쿼리는 SQL 안에 들어가는 또 다른 SQL이다. 수업에서는 “최소 급여자의 이름과 급여”를 찾는 예시로 시작했다.

먼저 따로 찾으면 두 단계다.

```sql
SELECT min(salary) FROM members;
SELECT name, salary FROM members WHERE salary = 100;
```

서브쿼리를 쓰면 한 문장으로 합칠 수 있다.

```sql
SELECT name, salary
FROM members
WHERE salary = (SELECT min(salary) FROM members);
```

원본 노트에서는 메인 쿼리와 서브쿼리의 실행 순서를 이렇게 이해했다.

- 서브쿼리: `SELECT min(salary) FROM members` — 먼저 실행
- 메인 쿼리: `SELECT name, salary FROM members WHERE salary = (...)` — 나중에 실행

이 구조는 영어의 that절처럼 “조건 안에 또 하나의 설명을 넣는 방식”으로 이해할 수 있다.

## 단일행 서브쿼리 vs 다중행 서브쿼리

원본에서 중요하게 표시된 부분이다.

### 단일행 서브쿼리

서브쿼리 결과가 하나의 값이면 `=`, `<`, `>`, `<=`, `>=`, `<>` 같은 비교 연산자를 쓴다.

```sql
SELECT name, salary
FROM members
WHERE salary > (SELECT avg(salary) FROM members);
```

### 다중행 서브쿼리

서브쿼리 결과가 여러 행이면 `=`을 쓰면 안 되고, `IN`, `ANY`, `ALL` 같은 연산자를 써야 한다.

```sql
SELECT name, manager
FROM MEMBERS
WHERE manager IN (SELECT id FROM members WHERE name IN('김구', '유관순'));
```

원본 노트의 핵심 표현은 “1대 2 관계라서 `=`을 쓰면 안 됨”이다. 즉, 비교 대상이 하나인지 여러 개인지를 먼저 판단해야 한다.

### 다중컬럼 서브쿼리

여러 컬럼을 한 번에 비교할 수도 있다.

```sql
SELECT name, salary, gender
FROM MEMBERS
WHERE (gender, salary) IN (
  SELECT gender, min(salary)
  FROM members
  GROUP BY GENDER
);
```

이때 메인 쿼리의 `(gender, salary)`와 서브쿼리의 `(gender, min(salary))`가 각각 대응한다.

## 관련 페이지

- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]

## 출처

- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
