---
title: Oracle 서브쿼리
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql
status: growing
confidence: high
---

# Oracle 서브쿼리

## 정의

서브쿼리는 SQL 안에 들어가는 또 다른 SQL이다. 수업 노트에서는 영어의 that절처럼 조건 안에 또 하나의 설명을 넣는 방식으로 이해했다.

## 수업에서 등장한 맥락과 중요성

03-19에는 “최소 급여인 회원”, “평균 급여보다 많이 받는 회원”, “김구·유관순이 관리하는 회원”처럼 조건값을 직접 숫자나 ID로 적을 수 없는 질문이 나왔다. `MIN`, `AVG` 같은 집계 결과는 `WHERE`에서 바로 계산해 비교하기 어렵기 때문에, 안쪽 SELECT가 기준값을 만들고 바깥 SELECT가 실제 행을 찾는 두 단계로 나눴다.

## 기본 예시

```sql
SELECT name, salary
FROM members
WHERE salary = (SELECT min(salary) FROM members);
```

학습할 때는 안쪽 서브쿼리가 기준값을 만들고 바깥 쿼리가 사용하는 논리적 두 단계로 읽는다. 다만 Oracle 옵티마이저는 쿼리를 변환할 수 있으므로 실제 물리 실행이 항상 안쪽부터라는 보장은 아니다.

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

## 자주 틀리는 이해

- “안쪽 쿼리는 항상 한 값”이 아니다. 결과 행 수를 먼저 예측한 뒤 `=` 또는 `IN`/`ANY`/`ALL`을 선택한다.
- 다중행 결과에 `=`을 쓰면 “여러 값 중 어느 하나와 같은가”를 표현할 수 없다. 수업의 관리자 2명 조회가 `IN`을 사용한 이유다.
- 단일값 비교 위치에 서브쿼리가 여러 행을 반환하면 scalar subquery 다중행 오류가 난다. “값 1개”보다 **결과 한 행인지**를 먼저 판단한다.
- `NOT IN`의 목록이나 서브쿼리 결과에 `NULL`이 섞이면 비교 결과가 UNKNOWN이 되어 예상과 달리 행이 나오지 않을 수 있다. NULL 가능성이 있으면 별도 제외 조건이나 `NOT EXISTS`를 검토한다.
- JOIN과 서브쿼리는 서로 대체해야 하는 문법이 아니다. 회원과 게시글 컬럼을 한 결과에 붙일 때는 JOIN, 최소 급여처럼 먼저 기준을 계산할 때는 서브쿼리가 질문 구조를 더 직접 표현한다.

## 선행·후속 연결

- 선행: [[concepts/oracle-sql-functions|그룹 함수]]가 서브쿼리 안에서 최소·평균 같은 기준값을 만든다.
- 비교: [[comparisons/single-row-vs-multi-row-subquery|단일행 vs 다중행 서브쿼리]]에서 결과 개수와 연산자를 함께 판단한다.
- 후속: Spring Data JPA의 JPQL에서도 중첩 조회가 가능하지만, Oracle 수업에서 직접 배운 범위는 SQL 서브쿼리다.

## 관련 페이지

- [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-sql-functions|Oracle SQL 함수]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
