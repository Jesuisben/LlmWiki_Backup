---
title: DDL vs DML vs DQL
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/Study/2. Oracle/교육 자료/오라클 교안.pdf
status: growing
confidence: high
---

# DDL vs DML vs DQL

## 비교 목적

SQL을 처음 배울 때 구조를 바꾸는 것, 데이터를 바꾸는 것, 데이터를 조회하는 것을 구분해야 `COMMIT`, `ROLLBACK`, 오류 원인을 이해하기 쉽다.

## 한눈에 보기

| 항목 | DDL | DML | DQL |
|---|---|---|---|
| 대상 | 구조/object | 데이터/row | 데이터 조회 결과 |
| 대표 명령 | `CREATE`, `ALTER`, `DROP` | `INSERT`, `UPDATE`, `DELETE` | `SELECT` |
| commit 관계 | 자동 commit 성격 | `COMMIT`/`ROLLBACK` 필요 | 보통 데이터 변경 없음 |
| 수업 예시 | 컬럼 추가/수정/삭제 | 회원/상품/주문 입력 | 상품 목록/조건 검색 |

## 언제 무엇을 쓰는가

- 테이블, 컬럼, 제약조건, 시퀀스 구조를 바꾸면 DDL이다.
- 행 데이터를 넣고 바꾸고 지우면 DML이다.
- 화면에 보여줄 데이터를 가져오면 DQL이다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[summaries/2026-03-18-oracle-constraints-validation|2026-03-18 Oracle 제약조건 테스트와 유효성 검사]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/Study/2. Oracle/교육 자료/오라클 교안.pdf` — p.34~36, p.120~124, p.134~195
