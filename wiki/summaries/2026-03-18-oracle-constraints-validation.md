---
title: 2026-03-18 Oracle 제약조건 테스트와 유효성 검사
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A05.DQL 실습.sql
status: growing
confidence: high
---

# 2026-03-18 Oracle 제약조건 테스트와 유효성 검사

## 한 줄 요약

`oraman` 환경을 재생성한 뒤 PK/NOT NULL/CHECK/FK 제약조건을 오류 코드로 검증하고, 트랜잭션과 DDL/DQL 기본형까지 확장한 날이다.

## 배운 내용

- `drop user oraman cascade`로 실습 사용자의 객체를 모두 지우고 A01/A03 스크립트로 환경을 재구성했다.
- `MEMBERS`에 정상 데이터와 오류 데이터를 넣어 PK, NOT NULL, CHECK 제약조건이 어떻게 막는지 확인했다.
- 오류 코드 `ORA-00001`, `ORA-01400`, `ORA-02290` 등을 제약조건 이름과 함께 읽는 법을 배웠다.
- DML 트랜잭션은 최초 DML 실행 시 시작되고 `COMMIT` 또는 `ROLLBACK`으로 종료된다.
- DDL은 자동 commit이므로 DML처럼 rollback 감각으로 다루면 안 된다.
- A04 스크립트로 `ALTER TABLE`을 이용한 컬럼 추가/수정/이름변경/삭제, 제약조건 삭제를 실습했다.
- A05 스크립트로 `SELECT`, `WHERE`, `DISTINCT`, alias, `LIKE`, `IN`, `BETWEEN`, `ORDER BY`를 시작했다.

## 실습 / 예제

```sql
INSERT INTO MEMBERS(ID, NAME, PASSWORD, GENDER, BIRTH, MARRIAGE, SALARY)
VALUES('user01','홍길동','1234','남자',DATE '1990-01-01','미혼',300);
```

같은 ID를 다시 넣으면 `ORA-00001: unique constraint violated`가 발생한다.

DDL 실습:

```sql
ALTER TABLE ORAMAN.MEMBERS ADD EMAIL VARCHAR2(100);
ALTER TABLE ORAMAN.MEMBERS MODIFY NAME VARCHAR2(50);
ALTER TABLE ORAMAN.MEMBERS RENAME COLUMN ADDRESS TO ADDR;
ALTER TABLE ORAMAN.MEMBERS DROP COLUMN MANAGER;
ALTER TABLE ORAMAN.PRODUCTS DROP CONSTRAINT PRODUCTS_POINT_CK;
```

DQL 기본형:

```sql
select * from products;
select distinct category from products;
select name, price * 12 as annual_price from products;
select * from products where price between 3500 and 4500;
select * from products where name like '_이%';
select * from products order by category asc, price desc;
```

## 헷갈린 점 / 질문

- 제약조건 이름을 명확히 지으면 오류 분석이 쉬워진다.
- `NULL`은 `= NULL`로 비교하지 않고 `IS NULL`, `IS NOT NULL`을 쓴다.
- `BETWEEN`은 양 끝값을 포함한다.
- 테이블 이름을 `ORDER`처럼 SQL 키워드와 겹치게 만들지 않는 것이 좋다.

## 관련 페이지

- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.120~124 트랜잭션, p.134~195 DQL
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf` — p.119~127 DDL 실습
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A05.DQL 실습.sql`
