---
title: Primary Key vs Foreign Key
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
status: growing
confidence: high
---

# Primary Key vs Foreign Key

## 비교 목적

PK와 FK는 관계형 데이터베이스의 연결고리다. 수업에서는 참조되는 컬럼과 참조하는 컬럼으로 구분했다.

## 한눈에 보기

| 항목 | Primary Key | Foreign Key |
|---|---|---|
| 한국어 | 기본키 | 외래키 |
| 역할 | 한 행을 유일하게 식별 | 다른 테이블의 PK를 참조 |
| 위치 | 부모 테이블 | 자식 테이블 |
| 예시 | `MEMBERS.ID` | `BOARDS.WRITER` |
| 제약 | 중복 불가, NULL 불가 | 부모에 있는 값 또는 NULL |

## 예시

```sql
ALTER TABLE ORAMAN.BOARDS
ADD CONSTRAINT BOARDS_MEMBERS_FK
FOREIGN KEY (WRITER)
REFERENCES ORAMAN.MEMBERS(ID)
ON DELETE SET NULL;
```

여기서 `MEMBERS.ID`는 참조되는 기본키이고, `BOARDS.WRITER`는 참조하는 외래키다.

## 헷갈리기 쉬운 포인트

- FK는 자식 테이블에 있지만, 값의 기준은 부모 테이블의 PK다.
- 부모에 없는 값을 FK로 넣으면 참조 무결성 오류가 난다.
- 정규화로 테이블을 나눈 뒤에는 PK/FK로 관계를 다시 연결해야 한다.

## 관련 페이지

- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]
- [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]

## 출처

- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
