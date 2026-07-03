---
title: Oracle 서브쿼리
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/Study/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql
status: growing
confidence: high
---

# Oracle 서브쿼리

## 정의

서브쿼리는 SQL 안에 들어가는 또 다른 SQL이다. 수업 노트에서는 영어의 that절처럼 조건 안에 또 하나의 설명을 넣는 방식으로 이해했다.

## 기본 예시

```sql
SELECT name, salary
FROM members
WHERE salary = (SELECT min(salary) FROM members);
```

실행 순서는 보통 안쪽 서브쿼리가 먼저고, 바깥 메인 쿼리가 나중이다.

## 단일행/다중행/다중컬럼

| 구분 | 결과 | 연산자 |
|---|---|---|
| 단일행 서브쿼리 | 값 1개 | `=`, `<`, `>`, `<=`, `>=`, `<>` |
| 다중행 서브쿼리 | 여러 값 | `IN`, `ANY`, `ALL` |
| 다중컬럼 서브쿼리 | 여러 컬럼 조합 | `(컬럼1, 컬럼2) IN (...)` |

```sql
SELECT name, manager
FROM MEMBERS
WHERE manager IN (SELECT id FROM members WHERE name IN('김구', '유관순'));
```

원본 노트의 핵심은 “1대 2 관계라서 `=`을 쓰면 안 됨”이다.

```sql
SELECT name, salary, gender
FROM MEMBERS
WHERE (gender, salary) IN (
  SELECT gender, min(salary)
  FROM members
  GROUP BY GENDER
);
```

## 관련 페이지

- [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-sql-functions|Oracle SQL 함수]]

## 출처

- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/Study/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
