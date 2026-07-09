---
title: Oracle Inner Join vs Outer Join
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql
status: growing
confidence: high
---

# Oracle Inner Join vs Outer Join

## 비교 목적

JOIN을 배울 때 핵심은 “매칭되는 데이터만 볼 것인가, 매칭되지 않는 데이터도 기준 테이블에 따라 보존할 것인가”이다.

## 한눈에 보기

| 항목 | Inner Join | Outer Join |
|---|---|---|
| 결과 | 양쪽에 모두 매칭되는 행 | 한쪽 또는 양쪽의 미매칭 행도 포함 |
| 방향성 | 사실상 방향성 약함 | 기준 테이블 방향이 중요 |
| 수업 예시 | 작성자와 게시물이 모두 있는 경우 | 게시물을 안 쓴 회원도 보기 |
| 대표 문법 | `JOIN ... ON ...` | `LEFT/RIGHT/FULL OUTER JOIN ... ON ...` |

## 예시

```sql
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER;
```

```sql
SELECT m.name, b.SUBJECT
FROM members m LEFT OUTER JOIN BOARDS b
ON m.ID = b.WRITER;
```

`LEFT OUTER JOIN`은 왼쪽의 `members`를 기준으로 하므로 게시물을 쓰지 않은 회원도 결과에 남을 수 있다.

## 관련 페이지

- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[summaries/2026-03-19-oracle-functions-join-subquery|2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.347~365 JOIN
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
