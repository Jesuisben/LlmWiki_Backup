---
title: Oracle Inner Join vs Outer Join
created: 2026-07-02
updated: 2026-07-15
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

## 구체적인 선택 상황

1. 게시글 목록에 실제 작성자가 연결된 행만 필요하면 inner join을 쓴다. `MEMBERS.ID = BOARDS.WRITER`가 성립하는 행만 남는다.
2. 회원별 게시글 수를 집계하면서 게시글이 0개인 회원도 보여야 하면 `MEMBERS`를 왼쪽에 둔 left outer join을 쓴다.

```sql
SELECT m.id, m.Name, count(writer) AS cnt
FROM members m LEFT OUTER JOIN BOARDS b
ON m.id = b.writer
group by m.id, m.NAME
ORDER BY cnt DESC, m.name ASC ;
```

## 흔한 오해

- outer join이 항상 더 완전한 정답은 아니다. 미매칭 행을 포함할 필요가 없으면 inner join이 질문을 더 정확히 표현한다.
- JOIN은 FK가 있어야만 실행되는 문법이 아니다. 값이 맞으면 조인할 수 있지만 FK가 없으면 참조 무결성은 보장되지 않는다.
- left outer join에서 `COUNT(*)`를 쓰면 게시글이 없는 회원의 보존 행도 셀 수 있다. 실제 게시글 수는 `COUNT(b.writer)`처럼 자식 컬럼을 센다.

## 관련 페이지

- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[summaries/2026-03-19-oracle-functions-join-subquery|2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.347~365 JOIN
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
