---
title: Oracle Database
created: 2026-07-02
updated: 2026-07-15
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

Oracle 수업에서 **직접 구현한 범위**는 사용자/schema, 테이블·시퀀스·제약조건, DML/트랜잭션, DQL/JOIN/서브쿼리, ERD/정규화/View다. 03-30부터는 MySQL을 설치하고 MySQL Driver·Spring Data JPA를 사용한 별도 FrontEnd_BackEnd 환경으로 전환했다. 이후 Entity/Repository/Service 계층과 JPQL이 등장하고 프로젝트의 목록·상세·검색·주문 요청이 API를 거쳐 관계형 DB에 저장된다. 이 후속 연결은 Oracle에서 JPA를 직접 구현했다는 뜻도, 같은 Oracle 실행환경이 계속됐다는 뜻도 아니며 [[comparisons/jpql-vs-sql|JPQL vs SQL]]에서 경계를 확인한다.

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

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md` — MySQL/JPA 후속 환경
