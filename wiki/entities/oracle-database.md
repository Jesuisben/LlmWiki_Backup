---
title: Oracle Database
created: 2026-07-02
updated: 2026-07-04
type: entity
tags: [oracle, sql, backend, curriculum]
sources:
  - raw/Study/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/Study/2. Oracle/Oracle 총정리/Oracle 총정리.md
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
2. 테이블/번호/무결성이 헷갈리면 [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]], [[concepts/oracle-sequence|Oracle 시퀀스]], [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]를 본다.
3. 삭제 규칙이 헷갈리면 [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]], [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]를 본다.
4. 조회가 헷갈리면 [[concepts/oracle-sql-functions|Oracle SQL 함수]], [[comparisons/where-vs-having|WHERE vs HAVING]]을 본다.
5. 여러 테이블 조회가 헷갈리면 [[concepts/oracle-join|Oracle JOIN]], [[concepts/oracle-subquery|Oracle 서브쿼리]], [[comparisons/single-row-vs-multi-row-subquery|단일행 서브쿼리 vs 다중행 서브쿼리]]를 본다.
6. 설계가 헷갈리면 [[concepts/database-modeling-normalization|데이터 모델링과 정규화]], [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]], [[concepts/database-view-index|Database View와 Index]]를 본다.

## 다음 과목과의 연결

Oracle에서 배운 테이블, PK/FK, JOIN, 정규화는 이후 웹서비스 프로젝트에서 회원·상품·장바구니·주문 데이터를 설계하는 기반이 된다. Spring Boot의 Entity/Repository/Service 계층은 결국 DB 테이블과 SQL/JPA 조회 흐름 위에 쌓이며, React 화면의 목록·상세·검색·주문 기능도 이 관계형 데이터 구조를 API로 꺼내 쓰는 방식으로 이어진다.

## 보안 메모

수업 원본에는 로컬 실습용 관리자/사용자 접속값이 일부 등장한다. 이 wiki에서는 접속값 자체를 외부로 재노출하지 않고, 관리자 연결·일반 사용자 생성·권한 부여라는 역할과 절차 중심으로만 정리한다.

## 관련 개념

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/oracle-sql-functions|Oracle SQL 함수]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[entities/dbeaver|DBeaver]]

## 출처

- `raw/Study/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/Study/2. Oracle/Oracle 총정리/Oracle 총정리.md`
