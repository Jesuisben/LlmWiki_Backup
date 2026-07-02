---
title: Oracle DDL, DML, 트랜잭션
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
status: growing
confidence: high
---
# Oracle DDL, DML, 트랜잭션

## SQL의 종류

수업에서는 SQL을 다음처럼 구분했다.

| 분류 | 의미 | 예시 역할 |
|---|---|---|
| DQL | 데이터 조회 | `SELECT` |
| DML | 데이터 조작 | `INSERT`, `UPDATE`, `DELETE` |
| DDL | 구조 정의 | `CREATE`, `ALTER`, `DROP` |
| TCL | 트랜잭션 제어 | `COMMIT`, `ROLLBACK` |
| DCL | 권한 제어 | `GRANT`, `REVOKE` |

수업 노트에서는 DCL을 제외한 나머지는 알아야 한다고 표시했다. 하지만 이후 View 권한 실습에서 `GRANT`, `REVOKE`도 등장한다.

## 테이블 생성 예시

DBeaver UI로 테이블을 만들면 SQL Preview에 실제 DDL이 보인다. 수업에서는 이 SQL을 이해해야 한다고 했다.

```sql
CREATE TABLE ORAMAN.MEMBERS (
    ID VARCHAR2(30) NOT NULL,
    NAME VARCHAR2(30) NULL,
    PASSWORD VARCHAR2(30) NULL,
    GENDER VARCHAR2(6) NULL,
    BIRTH DATE DEFAULT sysdate NULL,
    MARRIAGE VARCHAR2(30) DEFAULT '미혼' NOT NULL,
    SALARY NUMBER(10,2) DEFAULT 0 NULL,
    ADDRESS VARCHAR2(255) NULL,
    MANAGER VARCHAR2(50) NULL,
    CONSTRAINT "MEMBERS_id_pk" PRIMARY KEY (ID)
)
TABLESPACE USERS;
```

여기서 중요한 요소는 다음이다.

- `CREATE TABLE`: 테이블 생성
- `VARCHAR2(30)`: 최대 길이 30의 문자열
- `NOT NULL`: 반드시 값 필요
- `DEFAULT`: 기본값
- `PRIMARY KEY`: 행을 식별하는 기본키
- `COMMENT`: 테이블/컬럼 설명

## INSERT 기본

데이터 추가는 `INSERT INTO ... VALUES ...`로 한다.

```sql
insert into members(id, name, password, gender, birth, marriage, salary, address, manager)
values('yoon', '윤봉길', 'abc1234', '남자', '1990/12/25', '미혼', 230, '용산', 'yusin');
```

컬럼명을 명시하면 원하는 순서로 값을 넣을 수 있다. 일부 컬럼을 생략하면 테이블 생성 시 지정한 기본값이 들어갈 수 있다.

```sql
insert into members(id, name, password, gender, birth, marriage, address, manager)
values('nongae', '논개', 'abc1234', '여자', '1990/12/25', '미혼', '강남', 'soon');
```

## COMMIT과 ROLLBACK

DML로 데이터를 바꾼 뒤에는 `COMMIT`으로 영구 저장할 수 있다.

```sql
commit;
```

반대로 확정 전 변경을 되돌릴 때는 `ROLLBACK`을 사용한다.

```sql
rollback;
```

수업에서는 DBeaver의 Auto Commit 설정 때문에 `ROLLBACK`이 기대처럼 동작하지 않는 상황도 겪었다. Auto Commit이 켜져 있으면 실행 즉시 확정되어 되돌리기 어렵다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[entities/oracle-database|Oracle Database]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
