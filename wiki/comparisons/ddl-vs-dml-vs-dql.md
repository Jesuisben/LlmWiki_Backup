---
title: DDL vs DML vs DQL
created: 2026-07-02
updated: 2026-07-15
type: comparison
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
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
| commit 관계 | Oracle에서 실행 전후 implicit commit 가능 | `COMMIT`/`ROLLBACK`으로 종료 | 보통 데이터 변경 없음 |
| 수업 예시 | 컬럼 추가/수정/삭제 | 회원/상품/주문 입력 | 상품 목록/조건 검색 |

## 언제 무엇을 쓰는가

- 테이블, 컬럼, 제약조건, 시퀀스 구조를 바꾸면 DDL이다.
- 행 데이터를 넣고 바꾸고 지우면 DML이다.
- 화면에 보여줄 데이터를 가져오면 DQL이다.

### 구체적인 선택 상황

1. 회원 이메일 컬럼을 새로 추가하려면 `ALTER TABLE ... ADD`인 DDL을 쓴다. 기존 회원의 급여 값을 바꾸는 것은 `UPDATE`인 DML이다.
2. 주문을 저장하려면 `INSERT` 후 업무 단위가 정상인지 보고 `COMMIT`/`ROLLBACK`한다. 저장된 주문 목록을 화면에 표시하려면 `SELECT`인 DQL을 쓴다.

```sql
ALTER TABLE MEMBERS ADD EMAIL VARCHAR2(100);
UPDATE MEMBERS SET SALARY = 50 WHERE ID='user01';
SELECT * FROM products WHERE price BETWEEN 3500 AND 4500 ;
```

## 흔한 오해

- DDL과 DML은 SQL 길이로 구분하지 않는다. 구조를 바꾸면 DDL, 행을 바꾸면 DML이다.
- `SELECT`가 결과를 화면에 만들더라도 저장된 행을 수정하는 것은 아니다.
- `ROLLBACK`은 이미 확정된 DML이나 Oracle implicit commit이 일어난 DDL을 되돌리는 만능 명령이 아니다.
- Oracle DDL의 implicit commit은 DBMS 동작이고, DBeaver Auto Commit은 클라이언트가 DML을 자동 확정하는 설정이다. 같은 원인으로 묶지 않는다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[summaries/2026-03-18-oracle-constraints-validation|2026-03-18 Oracle 제약조건 테스트와 유효성 검사]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.34~36, p.120~124, p.134~195
