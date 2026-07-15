---
title: Oracle 시퀀스
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
status: growing
confidence: high
---
# Oracle 시퀀스

## 시퀀스

시퀀스는 자동 번호표 기계처럼 이해할 수 있다. 게시물 번호가 매번 1씩 증가해야 할 때, 이전 번호를 사람이 기억하고 계산하면 피로하고 실수하기 쉽다.

수업에서는 `board_seq`, `product_seq`, `order_seq`, `orderdetail_seq` 같은 시퀀스를 만들었다.

03-16에는 시퀀스 개념을 미리 보고, 03-17에는 `ORDERS`와 `ORDERDETAILS` INSERT에서 실제 번호를 발급했으며, 03-18에는 실습 사용자를 재생성한 뒤 DDL 스크립트로 시퀀스까지 복구했다. 즉 시퀀스는 테이블 생성과 별도로 백업·재생성해야 하는 schema 객체다.

```sql
CREATE SEQUENCE product_seq
START WITH 41
INCREMENT BY 1
MINVALUE 0
NOCYCLE NOCACHE;
```

주요 옵션은 다음과 같다.

| 옵션 | 의미 |
|---|---|
| `START WITH` | 시작값 |
| `INCREMENT BY` | 증가값 |
| `MINVALUE` | 최소값 |
| `MAXVALUE` | 최대값 |
| `NOCYCLE` | 끝까지 가도 다시 처음으로 돌아가지 않음 |
| `NOCACHE` | 미리 번호를 뽑아두지 않음 |

시퀀스의 다음 값은 `nextval`로 가져온다.

```sql
INSERT INTO boards(NO, writer, password, subject, content, readhit, regdate)
VALUES(board_seq.nextval, 'an', 'abc123', '자바', '너무 어려워', default, '1998/12/25');
```

객체 존재와 옵션은 [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전]]으로 확인했다.

```sql
SELECT * FROM user_sequences;
```

## 왜 중요하고 어디서 헷갈리나

- 주문·게시물처럼 여러 사용자가 새 행을 만드는 기능에서 사람이 “현재 최대값 + 1”을 계산하는 방식을 피하게 한다.
- `SELECT MAX(oid)`는 테이블에 저장된 주문번호의 최댓값이고, 시퀀스의 다음 번호를 조회하는 문장이 아니다.
- `order_seq`라는 이름이 `ORDERS`와 관련 있음을 보여줄 뿐, DB가 둘을 자동 연결하지는 않는다. INSERT에서 `order_seq.nextval`을 직접 사용한다.
- PK용 시퀀스를 `CYCLE`로 두면 값이 다시 돌아와 기존 PK와 충돌할 수 있으므로 총정리에서는 `NOCYCLE`을 주의점으로 남겼다.
- `NEXTVAL`로 이미 발급한 번호는 INSERT가 rollback돼도 시퀀스로 반환되지 않는다. 따라서 번호 사이에 빈 값이 생길 수 있으며 시퀀스는 gapless 번호 생성기가 아니다.
- `NOCACHE`는 미리 번호를 보관하지 않는 옵션이지, rollback·동시 실행·실패 상황에서 번호가 절대 비지 않는다는 보장이 아니다.
- 03-30 이후 Spring/JPA 과정은 MySQL 환경에서 시작했다. JPA의 ID 생성 전략은 시퀀스 개념과 연결해 볼 수 있지만, Oracle 시퀀스 실습이 같은 DB 환경으로 그대로 이어진 것은 아니다.

## 관련 페이지

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전과 schema 객체]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.328~330 시퀀스
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md` — MySQL/JPA 후속 환경
