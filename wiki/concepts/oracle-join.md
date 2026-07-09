---
title: Oracle JOIN
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql
status: growing
confidence: high
---

# Oracle JOIN

## 정의

JOIN은 서로 다른 두 개 이상의 테이블을 공통 컬럼으로 연결해 하나의 결과처럼 조회하는 기술이다. 수업에서는 `members.id`와 `boards.writer`처럼 PK/FK 연결고리를 기준으로 조인했다.

## Equi Join과 ANSI Join

전통적인 equi join:

```sql
SELECT members.name, boards.SUBJECT
FROM members, boards
WHERE MEMBERS.ID = BOARDS.WRITER;
```

ANSI join:

```sql
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER;
```

alias를 쓰면 이후 컬럼 참조도 alias로 통일해야 하며, 테이블 alias에는 `AS`를 쓰지 않는다.

## Inner/Outer Join

| JOIN | 의미 | 수업 질문 |
|---|---|---|
| Inner Join | 양쪽에 모두 매칭되는 데이터 | 작성자와 게시물이 모두 있는 행 |
| Left Outer Join | 왼쪽 테이블은 매칭 없어도 보존 | 게시물을 안 쓴 회원도 볼래요 |
| Full Outer Join | 양쪽의 전체 합집합 | 작성자를 모르는 게시물도 같이 볼래요 |

```sql
SELECT m.id, m.Name, count(writer) AS cnt
FROM members m LEFT OUTER JOIN BOARDS b
ON m.id = b.writer
GROUP BY m.id, m.NAME
ORDER BY cnt DESC, m.name ASC;
```

자세한 비교는 [[comparisons/oracle-inner-vs-outer-join|Oracle Inner Join vs Outer Join]]에 정리했다.

## 관련 페이지

- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/oracle-inner-vs-outer-join|Oracle Inner Join vs Outer Join]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.347~365 JOIN
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
