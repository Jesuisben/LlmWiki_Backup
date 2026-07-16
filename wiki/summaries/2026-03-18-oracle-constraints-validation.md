---
title: 2026-03-18 Oracle 제약조건 테스트와 유효성 검사
created: 2026-06-30
updated: 2026-07-15
type: summary
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03.Oraman ddl(선생님이 만든 버젼).sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03_2.Oraman ddl 이후 DML.sql
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
- `SAVEPOINT`와 `ROLLBACK TO`는 트랜잭션 전체가 아닌 지정 저장점까지 되돌리는 제어어로 소개됐다.
- Oracle DDL은 실행 전후 암시적 커밋이 일어날 수 있으므로 DML처럼 rollback 감각으로 다루면 안 된다. 이것은 DBeaver의 Auto Commit 설정과 별개다.
- A04 스크립트로 `ALTER TABLE`을 이용한 컬럼 추가/수정/이름변경/삭제, 제약조건 삭제를 실습했다.
- A05 스크립트로 `SELECT`, `WHERE`, `DISTINCT`, alias, `LIKE`, `IN`, `BETWEEN`, `ORDER BY`를 시작했다.

## 왜 이 순서로 배웠나

먼저 동일한 초기 상태를 만들기 위해 실습 사용자를 재생성했다. 그 다음 정상 입력과 PK/NOT NULL/CHECK/FK 위반 입력을 비교해 DB 제약조건의 실제 효과를 확인했다. 데이터가 바뀌는 순간에는 확정·취소가 필요하므로 트랜잭션을 붙였고, 구조를 바꾸는 `ALTER TABLE`을 거친 뒤, 마지막에는 만들어진 데이터를 조건에 맞게 읽는 DQL로 넘어갔다. 즉 **입력 검증 → 변경 안전성 → 구조 변경 → 조회** 순서다.

## 실습 / 예제

```sql
INSERT INTO MEMBERS(ID, NAME, PASSWORD, GENDER, BIRTH, MARRIAGE, SALARY)
VALUES('user01','홍길동','1234','남자',DATE '1990-01-01','미혼',300);
```

같은 ID를 다시 넣으면 `ORA-00001: unique constraint violated`가 발생한다.

DDL 실습:

```sql
ALTER TABLE MEMBERS ADD EMAIL VARCHAR2(100);
ALTER TABLE ORAMAN.MEMBERS MODIFY NAME VARCHAR2(50);
ALTER TABLE ORAMAN.MEMBERS RENAME COLUMN ADDRESS TO ADDR;
ALTER TABLE ORAMAN.MEMBERS DROP COLUMN MANAGER;
ALTER TABLE ORAMAN.PRODUCTS DROP CONSTRAINT PRODUCTS_POINT_CK;
```

마지막 제약조건 삭제는 **날짜 메모의 예시**다. 현재 `A04.DDL 실습.sql` 파일에는 다른 대상이 들어 있으므로 두 출처를 같은 실행문으로 간주하지 않는다.

```sql
ALTER TABLE MEMBERS
DROP CONSTRAINT MEMBERS_PASSWORD_CK;
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
- `GENDER='외계인'` 입력은 CHECK보다 먼저 `VARCHAR2(6)` 길이를 넘어서 `ORA-12899`가 발생했다. 여러 규칙을 동시에 어긴 값은 기대한 CHECK 오류보다 컬럼 길이 검사가 먼저 드러날 수 있다.
- 날짜 메모와 A04 스크립트의 제약조건 삭제 대상은 서로 다르다. 위의 `PRODUCTS_POINT_CK`는 날짜 메모, `MEMBERS_PASSWORD_CK`는 현재 A04 파일의 실제 문장이다.
- A05의 `SELECT * FROM products name NOT LIKE '크로와상%'`는 `WHERE`가 빠진 원본 오타라 실행되지 않는다. `NOT LIKE` 조건은 `FROM products` 뒤의 `WHERE` 절에 와야 한다.
- `NULL`은 `= NULL`로 비교하지 않고 `IS NULL`, `IS NOT NULL`을 쓴다.
- `BETWEEN`은 양 끝값을 포함한다.
- 테이블 이름을 `ORDER`처럼 SQL 키워드와 겹치게 만들지 않는 것이 좋다.
- 폼 유효성 검사는 사용자가 입력하는 화면에서 빠르게 오류를 알려주고, DB 제약조건은 어떤 입력 경로로 들어오더라도 최종 데이터를 지키는 규칙이다. 둘 중 하나로 다른 하나를 완전히 대신하는 관계가 아니다.
- 원본 중 한 테스트 블록에는 “트랜잭션 테스트는 제외함”이라고 적혀 있지만, 같은 날 뒤쪽에서는 `PRODUCTS` 입력 → 조회 → `ROLLBACK` → 재조회 흐름으로 트랜잭션을 실제 학습했다. 삭제된 초안과 실제 학습 구간을 구분해야 한다.

## 이전·다음 흐름

- 이전: 03-17에 PK/FK와 `ON DELETE` 관계를 만들었다.
- 다음: 03-19에는 DQL을 함수·집계·`GROUP BY/HAVING`·JOIN·서브쿼리로 심화한다.

## 관련 페이지

- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.120~124 트랜잭션, p.134~195 DQL
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf` — p.119~127 DDL 실습
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03.Oraman ddl(선생님이 만든 버젼).sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03_2.Oraman ddl 이후 DML.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A05.DQL 실습.sql`
