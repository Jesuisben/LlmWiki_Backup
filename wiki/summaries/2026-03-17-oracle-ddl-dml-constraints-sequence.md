---
title: 2026-03-17 Oracle DDL/DML, 제약조건, 시퀀스
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/Study/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/Study/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql
  - raw/Study/2. Oracle/교육 자료/스크립트들/A03 Oraman ddl.sql
status: growing
confidence: high
---

# 2026-03-17 Oracle DDL/DML, 제약조건, 시퀀스

## 한 줄 요약

쇼핑몰 예제의 `orders`, `orderdetails`, `products` 데이터를 넣고, 시퀀스·데이터 사전·참조 무결성·`ON DELETE` 옵션을 실제 오류와 함께 배운 날이다.

## 배운 내용

- `order_seq.nextval`, `orderdetail_seq.nextval`로 주문번호와 주문상세 번호를 자동 생성했다.
- `user_tables`, `user_sequences` 같은 데이터 사전으로 내가 가진 객체를 확인했다.
- DBeaver에서 DDL 스크립트를 생성해 테이블/시퀀스를 삭제했다가 다시 만들었다.
- 부모/자식 테이블, PK/FK, 참조 무결성 제약조건을 배웠다.
- `ON DELETE SET NULL`과 `ON DELETE CASCADE`의 업무 의미 차이를 다뤘다.
- DBeaver Auto Commit 때문에 `ROLLBACK`이 기대와 다르게 동작할 수 있음을 확인했다.

## 실습 / 예제

```sql
insert into orders(oid, mid, orderdate)
values(order_seq.nextval, 'an', sysdate);

select max(oid) from orders;

insert into orderdetails(odid, oid, pnum, qty)
values(orderdetail_seq.nextval, 1, 1, 10);
```

부모에 없는 작성자 `hello`가 들어간 상태에서 FK를 만들면 `ORA-02298`이 발생했고, 이후 위반 데이터를 삭제하고 다시 FK를 만들었다.

```sql
DELETE FROM boards WHERE writer = 'hello';
COMMIT;
```

## 헷갈린 점 / 질문

- `COMMIT` 후에는 `ROLLBACK`으로 되돌릴 수 없다.
- DBeaver 기본 Auto Commit이 켜져 있으면 실행 즉시 확정될 수 있으므로, 트랜잭션 실습 전 Manual Commit 설정이 중요하다.
- `ON DELETE`는 단순 문법이 아니라 “데이터를 삭제할 때 무엇을 보존해야 하는가”라는 업무 규칙이다.

## 관련 페이지

- [[concepts/oracle-sequence|Oracle 시퀀스]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]

## 출처

- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.69~73 테이블 정의, p.88~108 주문/참조 무결성 실습
- `raw/Study/2. Oracle/교육 자료/오라클 교안.pdf` — p.389~391 제약조건 개요
- `raw/Study/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql`
- `raw/Study/2. Oracle/교육 자료/스크립트들/A03 Oraman ddl.sql`
