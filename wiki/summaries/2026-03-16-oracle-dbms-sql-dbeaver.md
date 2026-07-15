---
title: 2026-03-16 Oracle DBMS, SQL, DBeaver 입문
created: 2026-06-30
updated: 2026-07-15
type: summary
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql
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
- `MEMBERS` 데이터는 전체 컬럼 순서 입력, 컬럼명 명시, 일부 컬럼 생략으로 기본값 사용, 컬럼 순서 재배치의 네 방식으로 넣었다.
- `Ctrl+Enter`는 현재 SQL 한 문장, `Alt+X`는 선택한 여러 문장을 실행하는 DBeaver 단축키로 사용했다.
- `COMMIT`과 `ROLLBACK`의 기본 뜻을 확인한 뒤 `BOARDS`, `PRODUCTS`, `board_seq`, `product_seq`까지 schema 객체를 확장했다.
- `board_seq.nextval`을 `BOARDS.NO`에 직접 사용해 시퀀스가 번호를 발급하는 흐름을 확인했다.

## 왜 이 순서로 배웠나

먼저 DBMS와 SQL 분류로 “무엇을 어떤 언어로 조작하는가”를 잡고, 그 다음 관리자 연결 → 실습 사용자 생성 → 일반 사용자 연결 → 테이블 생성 순으로 내려갔다. 관리자와 일반 사용자의 책임을 나눈 뒤에야 수업용 schema에서 DDL/DML을 안전하게 반복할 수 있기 때문이다. 마지막에는 `COUNT(*)`와 시퀀스를 미리 보면서 다음 날의 주문·게시물 번호 자동 생성으로 이어졌다.

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

관리자가 실습용 DB 계정을 만들고 권한을 부여하는 흐름을 실습했다. 원본의 로컬 실습 비밀번호 값은 wiki에 다시 싣지 않고 역할만 남긴다.

```sql
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

후반부에는 데이터 건수를 확인하고 시퀀스를 SQL로 직접 만들었다.

```sql
SELECT count(*) FROM members ;

CREATE SEQUENCE product_seq
START WITH 41
INCREMENT BY 1
MINVALUE 0
nocycle nocache ;
```

## 헷갈린 점 / 질문

- `localhost`는 내 컴퓨터이고, `xe`는 설치한 Oracle XE 데이터베이스 이름이다.
- `VARCHAR2`는 Oracle에서 쓰는 가변 길이 문자열 타입이다.
- 데이터베이스 문자열과 날짜는 작은따옴표를 쓰고, 숫자는 따옴표 없이 입력한다.
- 수업의 `'1990/12/25'` 날짜 입력은 Oracle의 암시적 형변환에 기대는 예제다. 세션 날짜 형식에 따라 달라질 수 있으므로 안전한 SQL에서는 `DATE '1990-12-25'` 또는 형식을 명시한 `TO_DATE`와 구분한다.
- 컬럼 목록을 생략하면 테이블 컬럼 순서와 값 개수가 정확히 맞아야 한다. 컬럼을 명시하면 일부 컬럼의 기본값을 활용하거나 입력 순서를 바꿀 수 있다.
- 시퀀스는 테이블과 이름이 비슷해도 자동 종속되지 않으며, INSERT에서 `sequence_name.nextval`을 직접 써야 한다.
- DBeaver는 SQL을 작성·실행하는 클라이언트이고 Oracle Database가 실제 데이터를 저장·관리하는 DBMS다. 둘을 같은 제품으로 보면 접속 오류의 위치를 찾기 어렵다.
- DBeaver 화면에서 만든 테이블도 결국 SQL Preview의 `CREATE TABLE`이 실행된 결과다. UI 작업과 DDL은 별개의 결과가 아니다.

## 이전·다음 흐름

- 이전: 03-13에 Oracle/DBeaver를 설치하고 Java 과정에서 DB 과정으로 전환했다.
- 다음: 03-17에는 생성된 `MEMBERS`, `BOARDS`, `ORDERS`, `ORDERDETAILS`를 대상으로 시퀀스·데이터 사전·PK/FK·삭제 규칙을 검증한다.

## 관련 페이지

- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.34~36 SQL 분류
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.47 단축키, p.55~57 쇼핑몰 테이블 구성
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A01.관리자 사용자 생성하기.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql`
