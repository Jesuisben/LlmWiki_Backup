---
title: Oracle Database
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [oracle, sql, backend, curriculum]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
status: stable
confidence: high
---

# Oracle Database

## 무엇인가

Oracle Database는 데이터를 테이블 형태로 저장하고 SQL로 조회·정의·조작하는 관계형 데이터베이스 관리 시스템(RDBMS)이다.

## 이 위키에서의 맥락

Oracle은 Java 객체지향 학습 다음에 등장했다. Java에서는 객체와 로직을 배웠고, Oracle에서는 그 객체들이 다룰 회원·게시물·상품·주문 데이터를 어떻게 영구 저장하고 관계로 연결하는지 배웠다.

이 과목의 핵심은 “데이터를 그냥 표에 넣는 것”이 아니라, 테이블 구조와 제약조건을 통해 데이터 무결성을 지키고, JOIN/서브쿼리/정규화를 통해 여러 테이블에 흩어진 의미를 다시 조합하는 것이다.

## 왜 중요한가

Oracle 과목은 Java 객체를 영구 데이터 구조와 연결하기 전에 SQL·schema·constraint·transaction·JOIN을 DBMS에 직접 실행해 보는 선행 단계였다. 이 직접 경험이 있어야 FrontEnd_BackEnd에서 JPA Entity와 Repository를 사용할 때도 table·PK/FK·query·transaction이 사라진 것이 아니라 추상화 뒤에서 다른 runtime과 함께 동작한다는 점을 구분할 수 있다.

## 대표 artifact와 입력 → 처리 → 결과

| 수업 단계 | 대표 artifact | 입력 | Oracle이 처리한 것 | 확인된 결과 |
|---|---|---|---|---|
| 사용자·schema 준비 | 관리자/일반 사용자 연결 | 사용자 생성·권한 SQL | 계정·권한과 사용자 소유 schema 분리 | ORAMAN schema와 일반 연결 확인 |
| table·무결성 | `MEMBERS`, `BOARDS`, `PRODUCTS`, 주문 관계 | DDL·INSERT와 위반 데이터 | column type·PK/FK·NOT NULL·CHECK 등 적용 | table 생성과 제약조건 성공/오류 확인 |
| 번호 발급 | `board_seq`, `product_seq` | `NEXTVAL`을 포함한 INSERT | 독립 sequence 객체가 다음 값 제공 | 게시물·상품 id 입력에 사용 |
| 변경 확정 | DML과 `COMMIT`/`ROLLBACK` | 행 추가·수정·삭제 | transaction을 확정하거나 취소 | 전후 조회로 행 상태 확인 |
| 조회·설계 | 함수·GROUP BY·JOIN·서브쿼리·ERD | 조회 조건과 table 관계 | 행 가공·집계·결합·중첩 조회 | 분리된 데이터를 목적에 맞게 조회 |

## 날짜별 학습 이력

- [[summaries/2026-03-13-java-project-oracle-start|2026-03-13]] — Java 프로젝트 마무리와 Oracle XE/DBeaver 설치 시작
- [[summaries/2026-03-16-oracle-dbms-sql-dbeaver|2026-03-16]] — DBMS/SQL/DBeaver 접속, 관리자/일반 사용자 연결, `MEMBERS` 테이블
- [[summaries/2026-03-17-oracle-ddl-dml-constraints-sequence|2026-03-17]] — DDL/DML, `INSERT`, `COMMIT`, 시퀀스, PK/FK, 주문/주문상세
- [[summaries/2026-03-18-oracle-constraints-validation|2026-03-18]] — 제약조건 테스트, 오류 코드, 폼 유효성 검사, 트랜잭션, DQL 시작
- [[summaries/2026-03-19-oracle-functions-join-subquery|2026-03-19]] — 단일행/그룹 함수, `GROUP BY`, `HAVING`, JOIN, 서브쿼리
- [[summaries/2026-03-20-database-modeling-normalization-view-index|2026-03-20]] — ERD, 데이터 모델링, 함수 종속성, 정규화, View, Index
- [[summaries/2026-03-20-oracle-subject-review|Oracle 총정리]] — Oracle/SQL 전체 흐름을 과목 단위로 다시 묶은 복습 허브

## 핵심 기능 / 특징

- SQL 표준 문법을 기반으로 데이터를 조회·조작·정의한다.
- schema 안에 table, sequence, view, index 같은 object를 둔다.
- PK/FK/UNIQUE/NOT NULL/CHECK 같은 제약조건으로 데이터 무결성을 지킨다.
- `COMMIT`/`ROLLBACK`으로 DML 트랜잭션을 확정하거나 취소한다.
- `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`로 조회 결과를 필터링·집계·정렬한다.
- JOIN과 서브쿼리로 여러 테이블과 조건을 조합한다.
- ERD와 정규화로 업무 데이터를 테이블 구조로 설계한다.

## 복습 경로

1. SQL 문법이 헷갈리면 [[concepts/oracle-sql-basics|Oracle SQL 기본]]과 [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]을 먼저 본다.
2. 테이블/번호/무결성이 헷갈리면 [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]], [[concepts/oracle-sequence|Oracle 시퀀스]], [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전과 schema 객체]], [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]를 본다.
3. 삭제 규칙이 헷갈리면 [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]], [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]를 본다.
4. 조회가 헷갈리면 [[concepts/oracle-sql-functions|Oracle SQL 함수]], [[comparisons/where-vs-having|WHERE vs HAVING]]을 본다.
5. 여러 테이블 조회가 헷갈리면 [[concepts/oracle-join|Oracle JOIN]], [[concepts/oracle-subquery|Oracle 서브쿼리]], [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]를 본다.
6. 설계가 헷갈리면 [[concepts/database-modeling-normalization|데이터 모델링과 정규화]], [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]], [[concepts/database-view-index|Database View와 Index]]를 본다.

## 다음 과목과의 연결

Oracle 수업에서 **직접 구현한 범위**는 사용자/schema, 테이블·시퀀스·제약조건, DML/트랜잭션, DQL/JOIN/서브쿼리, ERD/정규화/View다. 03-16 원본도 Spring 후속 과정에서는 MySQL을 사용할 예정이라고 경계를 예고했고, [[summaries/2026-03-30-fullstack-environment-setup|03-30]]부터 실제로 MySQL Server·Workbench·MySQL Driver·Spring Data JPA를 사용한 별도 FrontEnd_BackEnd runtime으로 전환했다.

이후 Member·Product·Cart·Order Entity/Repository와 04-21~22 paging/search가 MySQL 환경에서 이어졌다. 이 연결은 Oracle에서 JPA를 직접 구현했다는 뜻도, 같은 Oracle runtime이 계속됐다는 뜻도 아니다.

- Oracle sequence는 DB schema의 독립 객체이고 `NEXTVAL`을 SQL에서 사용했다.
- FrontEnd_BackEnd의 `@GeneratedValue(strategy = GenerationType.AUTO)`는 JPA annotation이다. 실제 MySQL `AUTO_INCREMENT` 또는 전략별 SQL 동작은 원본에서 확정하지 않았다.
- Oracle 직접 SQL과 MySQL Workbench의 SQL은 DBMS·dialect·실행 시점이 다르고, JPQL은 Entity를 대상으로 한다. [[concepts/oracle-sequence|Oracle 시퀀스]]와 [[comparisons/jpql-vs-sql|JPQL vs SQL]]에서 세부 경계를 확인한다.

## 확인된 범위와 미확정 범위

- 확인됨: Oracle XE 설치·DBeaver 연결, 관리자/일반 사용자 분리, SQL 직접 실행, table·sequence·constraint·transaction·조회·설계 실습.
- 확인됨: 03-30부터 FrontEnd_BackEnd의 주 DB runtime이 MySQL/JPA로 전환됐다.
- 미확정: FrontEnd_BackEnd에서 Oracle Driver나 Oracle schema를 application runtime에 연결한 기록은 없다.
- 미확정: JPA `GeneratedValue(AUTO)`가 수업의 MySQL에서 어떤 구체 DB 객체·SQL로 귀결됐는지는 실행 근거 없이 단정하지 않는다.
- 미확정: Oracle SQL 예제를 MySQL `coffee` DB의 실행 결과로 소급하거나, MySQL 검색 SQL을 Oracle에서 실행했다고 설명하지 않는다.

## 자주 헷갈리는 원인

- **DBMS와 client:** Oracle Database가 DBMS이고 DBeaver는 연결·SQL 실행·결과 확인 client다.
- **schema와 database 이름:** Oracle 사용자 소유 schema와 MySQL `coffee` database를 같은 실습 공간으로 합치지 않는다.
- **sequence와 GeneratedValue:** 둘 다 id 생성에 관련되지만 직접 조작한 Oracle schema object와 JPA mapping annotation은 계층과 실행 주체가 다르다.
- **SQL과 JPQL:** SQL은 table/column을, JPQL은 Entity/field를 대상으로 한다.
- **선행 원리와 후속 적용:** Oracle의 정규화·PK/FK/JOIN 학습이 JPA 관계 설계의 선행 지식이라는 사실은 Oracle runtime이 후속 project에서 사용됐다는 뜻이 아니다.

## 구현 역할과 면접 관점

- 회원·게시물·상품·주문·주문상세를 각각 어떤 테이블로 나누고 PK/FK로 어떻게 연결할지 결정한다.
- 제약조건은 애플리케이션 유효성 검사를 통과하지 못한 입력뿐 아니라 다른 경로의 잘못된 데이터도 DB에서 막는 최종 규칙이다.
- 트랜잭션은 주문과 주문상세처럼 함께 성공하거나 함께 취소해야 하는 변경의 경계를 만든다.
- JOIN/서브쿼리는 분리된 테이블에서 화면·보고서에 필요한 결과를 구성한다.
- 면접에서는 “Oracle을 썼다”보다 `MEMBERS-BOARDS`, `ORDERS-ORDERDETAILS` 예제로 **PK/FK 선택, 삭제 정책, COMMIT/ROLLBACK, inner/outer join 차이**를 설명하는 편이 학습 내용을 더 정확히 보여준다.

## 보안 메모

수업 원본에는 로컬 실습용 관리자/사용자 접속값이 일부 등장한다. 이 wiki에서는 접속값 자체를 외부로 재노출하지 않고, 관리자 연결·일반 사용자 생성·권한 부여라는 역할과 절차 중심으로만 정리한다.

## 관련 개념

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전과 schema 객체]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/oracle-sql-functions|Oracle SQL 함수]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[entities/dbeaver|DBeaver]]
- [[entities/mysql|MySQL]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]
- [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]

## 후속 과목 경계

- 직접 수업: 03-13~03-20 Oracle·DBeaver·SQL·설계 실습이다.
- FrontEnd_BackEnd: Oracle 원리를 선행 경계로 참조하지만 runtime은 MySQL/JPA다.
- Linux/AWS/CI/CD: MariaDB/MySQL container·RDS와 deployment pipeline은 별도 runtime·운영 계층이다.
- Passwordless: MariaDB를 사용하는 인증 sample과 Oracle 직접 수업을 같은 database 구현으로 합치지 않는다.
- 중간 프로젝트: 배포·인증 확장 설계에서 DB가 등장해도 실제 선택 DBMS와 schema는 해당 project source로 별도 확인해야 한다.

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md` — MySQL/JPA 후속 환경
