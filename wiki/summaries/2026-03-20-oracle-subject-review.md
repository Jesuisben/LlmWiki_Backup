---
title: Oracle 총정리
type: summary
created: 2026-07-03
updated: 2026-07-03
tags: [oracle, sql, curriculum, study-log]
sources:
  - raw/Study/2. Oracle/Oracle 총정리/Oracle 총정리.md
status: growing
confidence: high
---

# Oracle 총정리

## 한 줄 요약

`Oracle 총정리`는 2026-03-16부터 2026-03-20까지 배운 Oracle/SQL 학습을 “DBMS와 SQL 기본 → 테이블/제약조건/트랜잭션 → 조회 함수/JOIN/서브쿼리 → ERD와 정규화” 흐름으로 묶은 복습 노트다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-03-13-java-project-oracle-start|2026-03-13 Java 팀 프로젝트와 Oracle 시작]] 이후 Oracle 설치와 DBeaver 사용으로 전환
- 중심 기간: [[summaries/2026-03-16-oracle-dbms-sql-dbeaver|2026-03-16]] ~ [[summaries/2026-03-20-database-modeling-normalization-view-index|2026-03-20]]
- 다음 흐름: DB에 저장된 데이터를 웹 화면과 API에서 사용하기 위해 [[summaries/2026-03-23-html-css-intro|UI&UX]]와 [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]으로 연결

## 배운 내용

### 1. SQL과 관계형 데이터베이스의 기본 언어

총정리는 SQL을 Oracle, MySQL, PostgreSQL 같은 여러 DBMS에서 통하는 표준 언어로 설명한다. 행(row), 열(column), 테이블, 뷰, 인덱스, 시퀀스 같은 용어를 먼저 잡고, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE` 같은 명령의 역할을 구분한다.

### 2. SQL 분류와 트랜잭션

DQL은 조회, DML은 행 단위 데이터 조작, DDL은 구조 정의, TCL은 트랜잭션 제어로 정리된다. 특히 DML은 `COMMIT` 또는 `ROLLBACK`으로 작업을 확정하거나 취소해야 하고, DDL은 자동 커밋된다는 차이가 중요하다. 이 구분은 [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]의 핵심 근거다.

### 3. 테이블, 자료형, PK/FK, 시퀀스

테이블 이름, 컬럼, `VARCHAR2`, `NUMBER`, `DATE`, `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, 시퀀스가 함께 등장한다. 기본키는 행을 식별하고, 외래키는 다른 테이블의 행을 참조하며, 시퀀스는 게시물/주문/상품 같은 번호를 자동 생성하는 도구다.

### 4. 참조 무결성과 삭제 규칙

부모 테이블과 자식 테이블의 관계에서 부모 데이터 삭제가 막히는 이유, 자식 테이블에는 부모가 가진 값 또는 `NULL`만 들어갈 수 있다는 규칙이 정리되어 있다. `ON DELETE SET NULL`과 `ON DELETE CASCADE`는 “삭제를 막을지, NULL로 남길지, 같이 지울지”라는 업무 규칙의 표현이다.

### 5. DQL, 함수, GROUP BY/HAVING

조회 학습은 단일행 함수, 그룹 함수, `GROUP BY`, `HAVING`으로 확장된다. 총정리의 흐름상 `WHERE`는 그룹화 전 행 필터, `HAVING`은 그룹화 후 집계 결과 필터라는 차이를 [[comparisons/where-vs-having|WHERE vs HAVING]]과 함께 복습하기 좋다.

### 6. JOIN, 서브쿼리, ERD, 정규화

JOIN은 두 개 이상의 테이블을 공통 컬럼으로 합쳐 조회하는 기술이며, 총정리에서는 “참조 관계가 없어도 컬럼 값이 매칭되면 조인할 수 있다”는 점을 강조한다. 서브쿼리는 메인 쿼리 안에 넣는 쿼리로, 단일행/다중행/다중컬럼 결과에 따라 연산자가 달라진다. 마지막에는 ERD, 이상 현상, 함수 종속성, 정규화로 DB 설계 관점이 정리된다.

## 헷갈린 점 / 질문

- DML은 데이터를 바꾸지만 `COMMIT` 전까지 확정이 아니고, DDL은 구조를 바꾸면서 자동 커밋된다.
- 조인은 “FK가 있어야만 가능”한 것이 아니라, 조회 시점에 매칭할 수 있는 컬럼 조건이 있으면 가능하다. 다만 실제 설계에서는 FK가 데이터 무결성을 보장한다.
- `WHERE`와 `HAVING`, 단일행/다중행 서브쿼리, PK/FK, 삭제 옵션은 비교 페이지로 반복 복습해야 한다.

## 관련 페이지

- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/oracle-join|Oracle JOIN]]
- [[concepts/oracle-subquery|Oracle 서브쿼리]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]

## 출처

- `raw/Study/2. Oracle/Oracle 총정리/Oracle 총정리.md`
