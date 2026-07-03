---
title: Oracle DDL, DML, 트랜잭션
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/Study/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf
  - raw/Study/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql
status: growing
confidence: high
---

# Oracle DDL, DML, 트랜잭션

## 정의

DDL은 테이블·컬럼·제약조건 같은 구조를 바꾸는 SQL이고, DML은 테이블 안의 데이터를 바꾸는 SQL이다. 트랜잭션은 DML 작업을 하나의 논리적 업무 단위로 묶어 `COMMIT` 또는 `ROLLBACK`으로 끝내는 개념이다.

## DDL과 DML의 차이

| 구분 | DDL | DML |
|---|---|---|
| 다루는 대상 | 구조/object | 데이터/row |
| 대표 명령 | `CREATE`, `ALTER`, `DROP` | `INSERT`, `UPDATE`, `DELETE` |
| commit 관계 | 자동 commit 성격 | 직접 `COMMIT`/`ROLLBACK` 필요 |
| 수업 예시 | `ALTER TABLE MEMBERS ADD EMAIL` | `INSERT INTO MEMBERS ...` |

비교는 [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]도 참고한다.

## DDL 실습

```sql
ALTER TABLE ORAMAN.MEMBERS ADD EMAIL VARCHAR2(100);
ALTER TABLE ORAMAN.MEMBERS MODIFY NAME VARCHAR2(50);
ALTER TABLE ORAMAN.MEMBERS RENAME COLUMN ADDRESS TO ADDR;
ALTER TABLE ORAMAN.MEMBERS DROP COLUMN MANAGER;
ALTER TABLE ORAMAN.PRODUCTS DROP CONSTRAINT PRODUCTS_POINT_CK;
```

## DML과 트랜잭션

```sql
INSERT INTO MEMBERS(ID, NAME, PASSWORD, GENDER, BIRTH, MARRIAGE, SALARY)
VALUES('user01','홍길동','1234','남자',DATE '1990-01-01','미혼',300);

UPDATE MEMBERS SET SALARY = 50 WHERE ID='user01';
DELETE FROM BOARDS WHERE NO = 2;
COMMIT;
ROLLBACK;
```

수업에서 트랜잭션은 업무를 처리하는 논리적인 처리 단위이고, 핵심 특징은 ALL-OR-NOTHING이라고 정리했다.

## DBeaver Auto Commit 함정

DBeaver는 기본적으로 Auto Commit이 켜져 있을 수 있다. 이 상태에서 `DELETE`를 실행하면 즉시 확정되어 `ROLLBACK`으로 되돌리지 못할 수 있다. 참조 무결성/삭제 실습을 할 때는 Manual Commit으로 바꾼 뒤 `COMMIT`과 `ROLLBACK`의 효과를 확인해야 한다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]
- [[entities/dbeaver|DBeaver]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/Study/2. Oracle/교육 자료/오라클 교안.pdf` — p.120~124 트랜잭션
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf` — p.119~127 DDL 실습
- `raw/Study/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql`
