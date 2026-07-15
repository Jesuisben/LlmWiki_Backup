---
title: Oracle JOIN
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

# Oracle JOIN

## 정의

JOIN은 서로 다른 두 개 이상의 테이블을 공통 컬럼으로 연결해 하나의 결과처럼 조회하는 기술이다. 수업에서는 `members.id`와 `boards.writer`처럼 PK/FK 연결고리를 기준으로 조인했다.

## 왜 중요하고 수업에서 어떻게 이어졌나

정규화된 DB에서는 회원 이름은 `MEMBERS`, 게시글 제목은 `BOARDS`에 나뉜다. 03-19에는 작성자 ID만 보던 게시글 조회를 이름과 제목이 함께 보이는 결과로 복원했고, 게시물을 쓰지 않은 회원을 포함할지에 따라 inner/outer join을 선택했다. 03-20의 정규화가 “왜 나누는가”라면 JOIN은 “나눈 정보를 어떻게 다시 읽는가”다.

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

## 자주 틀리는 이해: JOIN과 FK를 구분하기

- JOIN은 SELECT 결과를 만드는 조회 방법이다. 두 컬럼 값이 맞으면 FK가 없어도 조인할 수 있다.
- FK는 저장되는 데이터의 참조 관계를 DB가 검사하는 제약조건이다. JOIN을 자동 실행해주는 기능이 아니다.
- outer join에서 `COUNT(*)`는 보존된 회원 행도 세므로 실제 게시글 수는 `COUNT(writer)`처럼 자식 컬럼을 세어야 한다.

## 선행·후속 연결

- 선행: [[concepts/oracle-referential-integrity|참조 무결성]]에서 부모/자식 키 관계를 만들었다.
- 후속: [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]에서 분리한 테이블을 JOIN으로 복원한다.
- 다른 질문: 기준값을 먼저 계산해 조건으로 넘기는 문제는 [[concepts/oracle-subquery|Oracle 서브쿼리]]가 더 자연스럽다.

## 관련 페이지

- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/oracle-inner-vs-outer-join|Oracle Inner Join vs Outer Join]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.347~365 JOIN
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A07 조인 실습.sql`
