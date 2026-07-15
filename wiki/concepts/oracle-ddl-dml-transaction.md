---
title: Oracle DDL, DML, 트랜잭션
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql
status: growing
confidence: high
---

# Oracle DDL, DML, 트랜잭션

## 정의

DDL은 테이블·컬럼·제약조건 같은 구조를 바꾸는 SQL이고, DML은 테이블 안의 데이터를 바꾸는 SQL이다. 트랜잭션은 DML 작업을 하나의 논리적 업무 단위로 묶어 `COMMIT` 또는 `ROLLBACK`으로 끝내는 개념이다.

## 수업에서 등장한 맥락과 중요성

03-16에는 테이블 생성과 첫 INSERT, 03-17에는 주문 입력·삭제와 DBeaver Auto Commit, 03-18에는 `PRODUCTS` 입력 후 `ROLLBACK` 및 `ALTER TABLE`을 연달아 실습했다. 이 순서 덕분에 “구조를 바꾸는 명령”과 “행을 바꾸는 명령”을 문법 이름이 아니라 **되돌릴 수 있는 시점과 업무 단위**로 구분하게 된다. 주문과 주문상세처럼 여러 변경이 한 업무라면 일부만 확정되지 않도록 트랜잭션 경계를 의식해야 한다.

## DDL과 DML의 차이

| 구분 | DDL | DML |
|---|---|---|
| 다루는 대상 | 구조/object | 데이터/row |
| 대표 명령 | `CREATE`, `ALTER`, `DROP` | `INSERT`, `UPDATE`, `DELETE` |
| commit 관계 | Oracle에서 실행 전후 implicit commit 가능 | 직접 `COMMIT`/`ROLLBACK`으로 종료 |
| 수업 예시 | `ALTER TABLE MEMBERS ADD EMAIL` | `INSERT INTO MEMBERS ...` |

비교는 [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]도 참고한다.

## DDL 실습

```sql
ALTER TABLE MEMBERS ADD EMAIL VARCHAR2(100);
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
```

위 `COMMIT`은 해당 변경을 확정하는 시나리오다. `ROLLBACK`은 같은 확정 뒤에 연속 실행해 되돌리는 명령이 아니라, **다른 미확정 DML 시나리오에서 COMMIT 대신 선택**하는 종료 방식이다. 수업에서 트랜잭션은 업무를 처리하는 논리적인 처리 단위이고, 핵심 특징은 ALL-OR-NOTHING이라고 정리했다.

수업에서 확인한 실행 흐름은 다음과 같다.

```sql
INSERT INTO PRODUCTS(NUM, NAME, COMPANY, IMAGE, STOCK, PRICE, CATEGORY, CONTENT, POINT, INPUTDATE)
VALUES(20,'테스트상품','테스트','test.png',10,1000,'bread','rollback 테스트',10,SYSDATE);

SELECT * FROM PRODUCTS;
ROLLBACK;
SELECT * FROM PRODUCTS;
```

첫 조회는 아직 세션에 남은 변경을 보고, `ROLLBACK` 뒤 조회는 취소된 상태를 확인한다. 단, DBeaver가 Auto Commit이면 이 비교가 성립하지 않을 수 있다.

### 저장점

트랜잭션 전체를 취소하지 않고 중간 지점까지만 돌아가기 위한 문법도 소개됐다.

```sql
savepoint 레이블_이름 ;
rollback to 레이블_이름 ;
```

### Oracle DDL의 implicit commit

Oracle DDL은 DBeaver의 버튼 설정과 무관하게 DBMS 차원에서 implicit commit을 일으킬 수 있다. 반면 DBeaver Auto Commit은 클라이언트가 DML 실행 후 자동으로 확정하는 모드다. 둘 다 rollback 결과에 영향을 주지만 원인과 책임 층위가 다르다.

## DBeaver Auto Commit 함정

DBeaver는 기본적으로 Auto Commit이 켜져 있을 수 있다. 이 상태에서 `DELETE`를 실행하면 즉시 확정되어 `ROLLBACK`으로 되돌리지 못할 수 있다. 참조 무결성/삭제 실습을 할 때는 Manual Commit으로 바꾼 뒤 `COMMIT`과 `ROLLBACK`의 효과를 확인해야 한다.

## 자주 틀리는 이해

- `ROLLBACK` 문을 적었다고 항상 복구되는 것은 아니다. 이미 `COMMIT`했거나 Auto Commit으로 확정됐으면 되돌릴 수 없다.
- DDL과 DML의 차이는 “긴 SQL/짧은 SQL”이 아니라 **구조와 행 중 무엇을 바꾸는가**다.
- DBeaver의 Commit 모드는 클라이언트 설정이고, 트랜잭션 자체는 Oracle에서 변경을 확정·취소하는 개념이다.
- 기존 데이터가 새 FK/CHECK를 이미 위반하면 `ALTER TABLE ... ADD CONSTRAINT` 자체가 실패한다. 구조 변경 전에는 현재 데이터가 새 규칙을 만족하는지 먼저 확인해야 한다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]
- [[entities/dbeaver|DBeaver]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.120~124 트랜잭션
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf` — p.119~127 DDL 실습
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A04.DDL 실습.sql`
