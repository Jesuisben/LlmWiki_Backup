---
title: Oracle 총정리
type: summary
created: 2026-07-03
updated: 2026-07-15
tags: [oracle, sql, curriculum, study-log]
sources:
  - raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md
  - raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
status: stable
confidence: high
---

# Oracle 총정리

## 한 줄 요약

`Oracle 총정리`는 2026-03-13 설치/접속 준비와 2026-03-16~03-20 Oracle 수업을 “DBMS와 SQL 언어 → 테이블/제약조건/트랜잭션 → 조회·함수·GROUP BY → JOIN/서브쿼리 → ERD/정규화/View/Index”로 다시 엮은 복습 허브다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-03-13-java-project-oracle-start|2026-03-13 Java 팀 프로젝트와 Oracle 시작]]에서 Java 프로젝트 이후 Oracle XE와 DBeaver 환경으로 전환
- 중심 기간: [[summaries/2026-03-16-oracle-dbms-sql-dbeaver|2026-03-16]] ~ [[summaries/2026-03-20-database-modeling-normalization-view-index|2026-03-20]]
- 다음 흐름: DB에 저장된 데이터를 웹 화면과 API에서 사용하기 위해 [[summaries/2026-03-23-html-css-intro|UI&UX]]와 [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]으로 연결
- 보안 메모: 원본에는 로컬 실습용 관리자/사용자 접속값이 등장하지만, wiki 본문에는 비밀번호 값을 재노출하지 않고 역할 중심으로만 설명한다.

## 커리큘럼 흐름으로 다시 보기

### 1. DBMS, Schema, Object, SQL

총정리 원본은 SQL을 Oracle, MySQL, PostgreSQL 등 여러 DBMS에서 통하는 표준 언어로 설명한다. 이 단계에서 잡아야 할 기본 단어는 다음과 같다.

- 행(row): 표의 가로줄, 실제 데이터 1건에 가까움
- 열(column): 표의 세로줄, 데이터의 속성에 가까움
- schema: 사용자가 만든 객체들이 모여 있는 공간
- object: 테이블, 뷰, 인덱스, 시퀀스처럼 DB 안에서 데이터를 관리하기 위해 만들어 둔 도구

Java에서 클래스/객체가 메모리 안의 구조였다면, Oracle에서는 테이블/행/컬럼이 영구 저장 데이터의 구조가 된다. 관련 페이지는 [[concepts/oracle-sql-basics|Oracle SQL 기본]], [[entities/oracle-database|Oracle Database]]다.

### 2. SQL 분류와 트랜잭션

원본은 DQL, DML, DDL, DCL, TCL을 카페/메뉴판 비유로 정리한다. 이 중 수업 복습의 중심은 DQL, DML, DDL, TCL이다.

- DQL: `SELECT`로 데이터를 조회한다.
- DML: `INSERT`, `UPDATE`, `DELETE`로 행 데이터를 조작한다.
- DDL: `CREATE`, `ALTER`, `DROP`으로 테이블·시퀀스·사용자 같은 구조를 바꾼다.
- TCL: `COMMIT`, `ROLLBACK`, `SAVEPOINT`로 트랜잭션을 제어한다.

중요한 차이는 DML은 `COMMIT` 전까지 확정되지 않고 `ROLLBACK`할 수 있지만, Oracle DDL은 실행 전후 암시적 커밋이 일어날 수 있다는 점이다. 이는 SQL 클라이언트인 DBeaver의 Auto Commit 설정과 별개다. 이 구분은 [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]], [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]에서 반복 복습한다.

### 3. DBeaver 접속과 사용자/권한 흐름

총정리에는 DBeaver에서 관리자 권한 연결을 만들고, 수업용 일반 사용자를 생성한 뒤, 일반 사용자 연결로 실습하는 흐름이 정리되어 있다. wiki에서는 민감값을 노출하지 않고 다음 구조만 남긴다.

1. 관리자 권한 연결로 Oracle XE에 접속한다.
2. 수업용 사용자를 생성하고 잠금을 해제한다.
3. 기본 tablespace와 quota를 설정한다.
4. `connect`, `resource` 권한을 부여한다.
5. 일반 사용자 연결로 테이블/시퀀스/제약조건 실습을 진행한다.

이 흐름은 [[entities/dbeaver|DBeaver]]와 [[concepts/oracle-sql-basics|Oracle SQL 기본]]에서 도구 맥락으로 이어진다.

### 4. 테이블, 자료형, PK/FK, 시퀀스

테이블은 최소 하나 이상의 컬럼이 있어야 하고, 수업에서는 `VARCHAR2`, `CHAR`, `NUMBER`, `DATE`를 중심으로 자료형을 다뤘다. `NUMBER(precision, scale)`은 전체 자릿수와 소수 자릿수를 나누어 저장하므로, 소수 자릿수 초과는 반올림될 수 있지만 정수 자릿수 초과는 에러가 날 수 있다.

기본키(PK)는 행을 식별하는 값이고, 외래키(FK)는 다른 테이블의 키를 참조하는 값이다. 시퀀스는 호출할 때마다 다음 번호를 발급하는 독립 객체지만 rollback으로 이미 발급한 번호가 반환되지 않아 빈 번호가 생길 수 있다. 즉 “중복을 피하는 번호 발급”과 “빈 번호 없는 연속 번호”는 같은 뜻이 아니다. 기본키 번호에 사용할 때는 `Cycle` 설정이 중복 위험을 만들 수 있음을 주의해야 한다. 관련 페이지는 [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]], [[concepts/oracle-sequence|Oracle 시퀀스]], [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]다.

### 5. 참조 무결성과 ON DELETE

참조 무결성은 부모 테이블에 없는 값을 자식 테이블의 외래키로 넣지 못하게 하는 규칙이다. 원본은 `MEMBERS`와 `BOARDS`, `ORDERS`, `ORDERDETAILS` 같은 예시를 통해 부모/자식 관계를 설명한다.

`ON DELETE SET NULL`은 부모 데이터가 삭제될 때 자식의 FK를 `NULL`로 남기는 방식이고, `ON DELETE CASCADE`는 자식 행까지 함께 삭제하는 방식이다. “회원 탈퇴 후 게시글은 남길 것인가”, “주문 삭제 시 주문상세도 같이 지울 것인가”처럼 업무 규칙에 따라 선택해야 한다. 관련 페이지는 [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]], [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]다.

### 6. DQL, 함수, GROUP BY/HAVING

조회는 `SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ...` 흐름으로 확장된다. 총정리 원본은 SQL 실행 순서를 `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`로 정리한다. 이 순서를 알면 `WHERE`와 `HAVING`의 차이가 자연스럽게 보인다.

- `WHERE`: 그룹화 전 개별 행을 필터링한다.
- `GROUP BY`: 범주형 컬럼 기준으로 행을 묶는다.
- `HAVING`: 그룹화 후 집계 결과를 필터링한다.

단일행 함수는 각 행에 하나씩 적용되고, 그룹 함수는 여러 행을 모아 하나의 결과를 만든다. `upper`, `lower`, `substr`, `replace`, `round`, `trunc`, `sysdate`는 단일행 함수 쪽이고, `avg`, `count`, `max`, `min`, `sum`은 그룹 함수 쪽으로 복습하면 된다. 관련 페이지는 [[concepts/oracle-sql-functions|Oracle SQL 함수]], [[comparisons/where-vs-having|WHERE vs HAVING]]이다.

### 7. JOIN: 테이블을 연결해서 읽기

JOIN은 두 개 이상의 테이블을 공통 컬럼 또는 매칭 조건으로 합쳐 읽는 기술이다. 총정리에서 중요한 문장은 “참조 관계가 없어도 컬럼 값이 매칭되면 조인할 수 있다”는 점이다. 다만 실제 설계에서 FK를 두면 데이터 무결성을 보장할 수 있다.

수업에서는 Oracle 방식의 equi join, ANSI `JOIN ... ON`, inner join, left/right/full outer join을 다뤘다. 게시물을 작성한 사람만 볼지, 게시물을 작성하지 않은 회원도 포함할지, 작성자 정보가 없는 게시글까지 볼지에 따라 inner/outer join이 달라진다. 관련 페이지는 [[concepts/oracle-join|Oracle JOIN]], [[comparisons/oracle-inner-vs-outer-join|Oracle Inner Join vs Outer Join]]이다.

### 8. 서브쿼리: SQL 안의 SQL

서브쿼리는 메인 쿼리 안에 들어가는 쿼리이며, 학습할 때는 안쪽 쿼리가 조건값을 만들고 바깥 쿼리가 이를 사용하는 논리적 두 단계로 읽는다. 실제 물리 실행 순서는 Oracle 옵티마이저가 바꿀 수 있으므로 “항상 안쪽이 먼저 실행된다”고 보장하는 규칙은 아니다. 총정리 원본은 최소 급여자, 평균 급여보다 많이 받는 사원, 특정 관리자의 사원 목록을 예시로 든다.

핵심 판단은 결과 개수다.

- 단일행 서브쿼리: 결과가 1개라서 `=`, `<`, `>` 같은 비교 연산자를 쓴다.
- 다중행 서브쿼리: 결과가 여러 개라서 `IN`, `ANY`, `ALL` 같은 연산자를 쓴다.
- 다중컬럼 서브쿼리: `(gender, salary) IN (...)`처럼 여러 컬럼 조합을 함께 비교한다.

관련 페이지는 [[concepts/oracle-subquery|Oracle 서브쿼리]], [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]다.

### 9. ERD, 함수 종속성, 정규화

마지막 흐름은 SQL 작성에서 DB 설계로 이동한다. ERD는 엔티티, 속성, 관계를 시각적으로 나타내는 설계도이고, 정규화는 삽입/갱신/삭제 이상을 줄이기 위해 테이블을 더 작은 단위로 분해하는 과정이다.

총정리 원본은 학생/학과/수강과목 예시를 통해 다음 순서를 보여준다.

1. 반복·중복 데이터와 이상 현상을 찾는다.
2. 함수 종속성을 파악한다.
3. 복합 기본키가 필요한지 판단한다.
4. 부분 종속과 이행적 함수 종속을 제거한다.
5. 분해된 테이블들이 조인으로 원래 정보를 복원할 수 있는지 확인한다.

관련 페이지는 [[concepts/database-modeling-normalization|데이터 모델링과 정규화]], [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]], [[concepts/database-view-index|Database View와 Index]]다.

> 원본의 “X는 PK, Y는 FK”라는 메모는 함수 종속성의 일반 정의로는 정확하지 않다. 함수 종속성은 결정 관계이고, PK/FK는 행 식별·테이블 참조를 강제하는 키/제약조건이다. 이번 정리는 이 둘을 분리한다.

### 10. View와 Index의 직접 학습 범위

View는 `CREATE OR REPLACE VIEW`로 조회 결과에 이름을 붙이고, `GRANT SELECT`로 다른 schema 사용자에게 공개한 뒤 `REVOKE`와 `DROP VIEW`까지 실습했다. 반면 Index는 검색을 돕는 구조와 PK/UNIQUE 생성 시 함께 만들어질 수 있다는 입문 설명까지만 확인했다. 별도 `CREATE INDEX`, 실행 계획, 성능 수치 실습은 원본에 없다.

## 핵심 실습 / 예제 앵커

- DBeaver 관리자 연결과 일반 사용자 연결 생성
- 사용자 생성, tablespace/quota 설정, 권한 부여
- `MEMBERS`, `BOARDS`, `ORDERS`, `ORDERDETAILS` 테이블 생성
- `INSERT`, `COMMIT`, `ROLLBACK`으로 DML 확정/취소 확인
- PK/FK/Check 제약조건 생성과 ORA 오류 해석
- 시퀀스 `NEXTVAL`로 자동 번호 입력
- `SELECT`, `WHERE`, `ORDER BY`, `LIKE`, `IN`, `BETWEEN`, `IS NULL` 조회
- 단일행 함수와 그룹 함수, `GROUP BY`, `HAVING`
- ANSI JOIN과 outer join으로 회원/게시글 연결 조회
- 단일행/다중행/다중컬럼 서브쿼리
- ERD를 보며 정규화된 테이블과 참조 무결성 제약조건 구성

대표 흐름 하나를 SQL로 묶으면 다음과 같다. 구조를 만든 뒤 데이터를 넣고 확정하고, 관계를 따라 조회한다.

```sql
INSERT INTO orders(oid, mid, orderdate)
VALUES(order_seq.nextval, 'an', sysdate);
COMMIT;

SELECT m.name, b.subject
FROM members m LEFT OUTER JOIN boards b
ON m.id = b.writer;
```

## 헷갈린 점 / 질문

- SQL의 `=`는 비교이고, Java의 대입문 `x = 1`과 다르다.
- DML은 데이터를 바꾸지만 `COMMIT` 전까지 확정이 아니고, DDL은 구조를 바꾸면서 자동 커밋된다.
- `NULL`은 알 수 없는 값이므로 `= NULL`이 아니라 `IS NULL`로 확인한다.
- `COUNT(*)`는 `NULL` 포함 전체 행 수이고, `COUNT(컬럼)`은 해당 컬럼이 `NULL`인 행을 제외한다.
- `WHERE`는 그룹화 전 행 필터, `HAVING`은 그룹화 후 집계 결과 필터다.
- JOIN은 FK가 있어야만 가능한 것은 아니지만, FK는 데이터가 깨지지 않도록 지키는 설계 규칙이다.
- 서브쿼리 결과가 여러 개인데 `=`을 쓰면 1대다 비교가 되어 오류가 난다.
- 정규화는 테이블을 쪼개는 것이 목적이 아니라, 이상 현상을 줄이면서 조인으로 원래 의미를 복원할 수 있게 만드는 과정이다.

## 다음 과목과의 연결

Oracle에서 **직접 실습한 범위**는 SQL, 테이블, 제약조건, 트랜잭션, JOIN/서브쿼리, ERD/정규화다. 03-30부터 시작한 FrontEnd_BackEnd 과정에서는 MySQL 환경과 Spring Boot/JPA의 Entity·Repository가 등장한다. 따라서 Oracle→JPA 연결은 PK/FK·JOIN·SQL 사고방식의 학습 연결이지 같은 Oracle 실행환경이 이어진다는 뜻이 아니다. 프로젝트에서는 React 화면의 상품·장바구니·주문 요청이 API를 거쳐 관계형 DB로 이어지며, 자세한 경계는 [[comparisons/jpql-vs-sql|JPQL vs SQL]]에서 확인한다.

## 관련 페이지

- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/oracle-sql-functions|Oracle SQL 함수]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]
- [[comparisons/where-vs-having|WHERE vs HAVING]]
- [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]

## 출처

- `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`
- `raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
