---
title: Oracle Database
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [oracle, sql, backend]
sources:
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
status: growing
confidence: high
---

# Oracle Database

## 무엇인가

데이터를 테이블 형태로 저장하고 SQL로 조회·정의·조작하는 관계형 데이터베이스 관리 시스템(RDBMS)이다.

## 이 위키에서의 맥락

- 2026-03-16에 DBMS, SQL, DBeaver 접속, 테이블·행·열·SELECT를 배우며 본격 등장했다.
- 2026-03-17~18에는 DDL/DML, 제약조건, 시퀀스, PK/FK 테스트로 데이터 무결성을 다뤘다.
- 2026-03-19에는 함수, GROUP BY/HAVING, JOIN, 서브쿼리로 조회 능력을 확장했다.
- 2026-03-20에는 ERD, 정규화, View, Index로 DB 설계 관점까지 이어졌다.

## 핵심 기능 / 특징

- `SELECT`, `CREATE TABLE`, `INSERT`, `COMMIT`/`ROLLBACK` 같은 SQL 실행
- PK/FK/CHECK와 시퀀스를 통한 무결성·자동 번호 관리
- JOIN/서브쿼리로 여러 테이블과 쿼리 결과 연결
- Spring Boot/JPA의 Entity·Repository를 이해하는 선행 지식

## 헷갈리기 쉬운 점

Oracle Database는 DBeaver와 다르다. Oracle은 데이터를 저장·관리하는 DBMS이고, DBeaver는 그 DB에 접속해 SQL을 실행하는 IDE다.

## 관련 개념

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[entities/dbeaver|DBeaver]]

## 학습 이력

이 페이지는 단순 정의가 아니라, 수업에서 이 기술이 처음 등장한 맥락과 이후 Java/Oracle/UI&UX/Spring/React 프로젝트 흐름으로 확장된 위치를 추적하기 위한 엔티티 페이지다.

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
