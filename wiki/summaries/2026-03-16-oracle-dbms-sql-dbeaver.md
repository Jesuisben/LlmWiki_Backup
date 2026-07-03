---
title: 2026-03-16 Oracle DBMS, SQL, DBeaver 입문
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/Study/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql
  - raw/Study/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql
status: growing
confidence: high
---

# 2026-03-16 Oracle DBMS, SQL, DBeaver 입문

## 한 줄 요약

Oracle DBMS와 SQL의 기본 분류를 배우고, DBeaver에서 관리자 계정과 실습 계정 `oraman`을 연결해 쇼핑몰 예제 테이블을 만들기 시작한 날이다.

## 배운 내용

- DBMS는 Database Management System, 즉 데이터베이스 관리 시스템이다.
- SQL은 데이터를 정의·조작·제어·조회하기 위한 표준 언어다.
- Oracle 교안 p.34~36에서는 SQL을 DQL, DML, DDL, DCL, TCL로 나눈다.
- DBeaver에서 `sys`/`SYSDBA`로 관리자 접속을 만들고, A01 스크립트로 `oraman` 일반 사용자를 생성했다.
- DBeaver 교안 p.55~57의 쇼핑몰 예제를 따라 `MEMBERS` 테이블과 컬럼, PK를 만들었다.

## 핵심 개념

| 개념 | 수업에서의 의미 |
|---|---|
| DBMS | 데이터를 저장·관리·조회하게 해주는 시스템 |
| SQL | DBMS에 요청을 보내는 언어 |
| DQL | `SELECT`로 데이터를 조회 |
| DML | `INSERT`, `UPDATE`, `DELETE`로 데이터를 조작 |
| DDL | `CREATE`, `ALTER`, `DROP`으로 구조를 정의/변경 |
| TCL | `COMMIT`, `ROLLBACK`으로 트랜잭션 제어 |
| 스키마 | 한 사용자가 가진 DB 객체 묶음 |

## 실습 / 예제

관리자가 실습용 DB 계정을 만들어 주는 흐름을 다음 SQL로 실습했다.

```sql
create user oraman identified by oracle account unlock;
alter user oraman default tablespace users quota unlimited on users;
grant connect, resource to oraman;
```

DBeaver UI로 `MEMBERS` 테이블을 만들더라도 SQL Preview의 DDL을 이해해야 한다고 강조했다.

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

## 헷갈린 점 / 질문

- `localhost`는 내 컴퓨터이고, `xe`는 설치한 Oracle XE 데이터베이스 이름이다.
- `VARCHAR2`는 Oracle에서 쓰는 가변 길이 문자열 타입이다.
- 데이터베이스 문자열과 날짜는 작은따옴표를 쓰고, 숫자는 따옴표 없이 입력한다.

## 관련 페이지

- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/교육 자료/오라클 교안.pdf` — p.34~36 SQL 분류
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.47 단축키, p.55~57 쇼핑몰 테이블 구성
- `raw/Study/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql`
- `raw/Study/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql`
