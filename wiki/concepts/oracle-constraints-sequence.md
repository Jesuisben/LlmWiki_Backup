---
title: Oracle 제약조건과 시퀀스
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03.Oraman ddl(선생님이 만든 버젼).sql
status: growing
confidence: high
---

# Oracle 제약조건과 시퀀스

## 정의

제약조건(constraint)은 잘못된 데이터가 들어오지 못하게 막는 DB 규칙이고, 시퀀스(sequence)는 게시물 번호·상품 번호·주문 번호처럼 증가하는 값을 자동으로 뽑는 객체다.

## 제약조건 5종

| 제약조건 | 의미 | 수업 예시 |
|---|---|---|
| `NOT NULL` | 반드시 값 필요 | `ID`, `MARRIAGE` NULL 금지 |
| `UNIQUE` | 중복 금지 | ID 중복 금지 |
| `PRIMARY KEY` | NOT NULL + UNIQUE, 행 식별 | `MEMBERS.ID`, `BOARDS.NO` |
| `FOREIGN KEY` | 부모 테이블 PK 참조 | `BOARDS.WRITER → MEMBERS.ID` |
| `CHECK` | 값 범위/목록 제한 | `salary >= 100`, `gender in (...)` |

오류 코드 예시는 제약조건을 눈으로 확인하게 해준다.

- `ORA-00001`: PK/UNIQUE 중복
- `ORA-01400`: NOT NULL 컬럼에 NULL 입력
- `ORA-02290`: CHECK 제약조건 위반
- `ORA-02291`: 부모 키 없음
- `ORA-02298`: 기존 데이터 때문에 FK 생성 검증 실패

## 시퀀스

시퀀스는 번호표를 자동으로 만들어주는 기계로 설명되었다.

```sql
create sequence order_seq start with 1 increment by 1 nocache;

insert into orders(oid, mid, orderdate)
values(order_seq.nextval, 'an', sysdate);
```

`cache`는 미리 뽑아둔 번호를 뜻한다. 실습에서는 재현성을 위해 `nocache`를 자주 사용했다.

## 데이터 사전

```sql
SELECT TABLE_NAME FROM user_tables;
SELECT * FROM user_sequences;
```

## 관련 페이지

- [[concepts/oracle-sequence|Oracle 시퀀스]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]
- [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.389~391 제약조건 개요
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03.Oraman ddl(선생님이 만든 버젼).sql`
