---
title: Oracle 제약조건과 시퀀스
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md
status: growing
confidence: high
---
# Oracle 제약조건과 시퀀스

## 정의

Oracle에서 **제약조건(constraint)**은 잘못된 데이터가 테이블에 들어오지 못하게 막는 규칙이고, **시퀀스(sequence)**는 게시물 번호나 주문 번호처럼 순차적으로 증가하는 값을 자동으로 만들어주는 객체다.

## 왜 중요한가

데이터베이스는 단순 저장소가 아니라 데이터의 정확성과 관계를 지키는 곳이다. 제약조건은 없는 회원의 게시물, 중복 ID, 음수 가격 같은 문제를 DB 레벨에서 막는다.

## 제약조건의 종류

| 제약조건 | 의미 |
|---|---|
| `NOT NULL` | 반드시 값이 있어야 함 |
| `UNIQUE` | 중복 불가 |
| `PRIMARY KEY` | 행을 식별하는 기본키 |
| `FOREIGN KEY` | 다른 테이블의 기본키 참조 |
| `CHECK` | 값의 범위나 조건 제한 |

## 분리된 하위 주제

- [[concepts/oracle-sequence|Oracle 시퀀스]] — `CREATE SEQUENCE`, `nextval`, 자동 번호 생성
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]] — 외래키, 참조 무결성, `ON DELETE SET NULL/CASCADE`, 데이터 사전

## 자주 헷갈리는 점

- Primary Key는 행을 식별하는 값이고, Foreign Key는 다른 테이블의 Primary Key를 참조하는 값이다.
- 참조 “되는” 쪽이 부모 테이블, 참조 “하는” 쪽이 자식 테이블이다.
- `COMMIT` 전에는 DML 변경을 `ROLLBACK`할 수 있다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-sequence|Oracle 시퀀스]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
