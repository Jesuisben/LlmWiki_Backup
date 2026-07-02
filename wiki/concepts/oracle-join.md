---
title: Oracle JOIN
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md
status: growing
confidence: high
---
# Oracle JOIN

## JOIN

JOIN은 서로 다른 두 개 이상의 테이블을 공통 컬럼으로 연결해서 하나의 결과처럼 조회하는 방법이다.

수업에서는 `members`와 `boards`를 예시로 사용했다.

```sql
SELECT members.name, boards.SUBJECT
FROM members, boards
WHERE MEMBERS.ID = BOARDS.WRITER;
```

이 문법은 전통적인 Equi Join 형태다. 같은 의미를 ANSI JOIN으로 쓰면 다음과 같다.

```sql
SELECT m.name, b.SUBJECT
FROM members m JOIN boards b
ON m.ID = b.WRITER;
```

수업에서 짚은 JOIN의 핵심은 다음이다.

| JOIN 종류 | 의미 |
|---|---|
| Inner Join | 양쪽 테이블에 모두 매칭되는 데이터 |
| Left Outer Join | 왼쪽 테이블 기준으로, 매칭이 없어도 왼쪽 데이터는 보존 |
| Right Outer Join | 오른쪽 테이블 기준 |
| Full Outer Join | 양쪽 전체 합집합 |

예를 들어 게시물을 남기지 않은 회원도 보고 싶으면 `LEFT OUTER JOIN`이 필요하다.

```sql
SELECT m.name, b.SUBJECT
FROM members m LEFT OUTER JOIN BOARDS b
ON m.ID = b.WRITER;
```

회원별 게시물 수를 구할 때는 JOIN과 `GROUP BY`가 함께 쓰인다.

```sql
SELECT m.id, m.Name, count(writer) AS cnt
FROM members m LEFT OUTER JOIN BOARDS b
ON m.id = b.writer
GROUP BY m.id, m.NAME
ORDER BY cnt DESC, m.name ASC;
```

## 관련 페이지

- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]

## 출처

- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
