---
title: Oracle SQL 기본
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
# Oracle SQL 기본

## 정의

**SQL(Structured Query Language)**은 데이터베이스에 데이터를 조회, 추가, 수정, 삭제하거나 테이블 구조를 만들기 위해 사용하는 표준 언어다.

2026-03-16 수업에서는 Oracle Database와 DBeaver를 연결하고, SQL의 기본 분류와 테이블/행/열 개념을 배웠다.

## 왜 중요한가

회원가입, 로그인, 상품 등록, 주문, 장바구니 같은 웹서비스 기능은 모두 DB와 연결된다. SQL은 Spring Boot와 React 프로젝트로 넘어가기 전 반드시 이해해야 하는 기반이다.

## DBMS와 Oracle

DBMS는 Database Management System이다. 이 과정에서는 DBeaver로 Oracle에 접속해 SQL을 실행했고, 이후 Spring 과정에서는 MySQL도 사용한다.

## 기본 용어

| 용어 | 의미 |
|---|---|
| 테이블(table) | 데이터를 저장하는 표 |
| 행(row) | 데이터 한 건 |
| 열(column) | 데이터 항목 |
| 스키마(schema) | 한 사용자가 가진 DB 객체 묶음 |

Oracle에서 처음 다룬 주요 타입은 `VARCHAR2`, `NUMBER`, `DATE`다.

## DBeaver 연결 흐름

수업에서는 관리자 계정 `sys`/`SYSDBA`로 접속한 뒤 실습용 사용자 `oraman`을 만들고 권한을 부여했다.

```sql
create user oraman identified by oracle account unlock;
alter user oraman default tablespace users quota unlimited on users;
grant connect, resource to oraman;
```

## 분리된 하위 주제

- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]] — SQL 분류, `CREATE`, `INSERT`, `COMMIT`, `ROLLBACK`
- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]] — 테이블 규칙과 자동 번호 생성
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]] — 조회 심화

## 자주 헷갈리는 점

- SQL 키워드는 대소문자를 엄격히 가리지는 않지만, 문자열 값은 대소문자가 의미를 가질 수 있다.
- 문자열과 날짜는 작은따옴표를 쓰고 숫자는 따옴표 없이 쓴다.
- DDL은 구조 변경, DML은 데이터 변경이다.

## 관련 페이지

- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
