---
title: Oracle 시퀀스
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
# Oracle 시퀀스

## 시퀀스

시퀀스는 자동 번호표 기계처럼 이해할 수 있다. 게시물 번호가 매번 1씩 증가해야 할 때, 이전 번호를 사람이 기억하고 계산하면 피로하고 실수하기 쉽다.

수업에서는 `board_seq`, `product_seq`, `order_seq`, `orderdetail_seq` 같은 시퀀스를 만들었다.

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

## 관련 페이지

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
