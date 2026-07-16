---
title: 2026-03-17 Oracle DDL/DML, 제약조건, 시퀀스
created: 2026-06-30
updated: 2026-07-15
type: summary
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03 Oraman ddl.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03.Oraman ddl(선생님이 만든 버젼).sql
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
- `PRODUCTS`, `ORDERS`, `MEMBERS` 부모 행을 삭제해 `SET NULL`, `CASCADE`, `ROLLBACK` 결과를 각각 비교했다.
- NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK의 5가지 제약조건 역할을 정리했다.
- schema에서 생성 DDL을 추출하고, 테이블·제약조건·시퀀스를 분리한 교사 버전 DDL로 실습 환경을 다시 만들었다.

## 왜 이 순서로 배웠나

전날 만든 테이블에 주문 데이터를 넣으려면 먼저 사람이 번호를 계산하는 문제를 해결해야 해서 시퀀스를 배웠다. 이어서 `user_tables`, `user_sequences`로 생성된 객체를 확인하고, 테이블을 지웠다가 DDL 스크립트로 복구했다. 구조를 다시 만들 수 있게 된 뒤 `MEMBERS`를 부모로, `BOARDS`·`ORDERS`를 자식으로 연결하면서 “값을 넣는 것”에서 “관계를 깨뜨리지 않는 것”으로 초점이 이동했다.

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

### 제약조건 5종

| 제약조건 | 수업에서 확인한 역할 |
|---|---|
| NOT NULL | 반드시 입력해야 하는 컬럼의 `NULL` 차단 |
| UNIQUE | 중복값 차단, `NULL`은 별도 취급 |
| PRIMARY KEY | NOT NULL과 UNIQUE를 결합해 행 식별 |
| FOREIGN KEY | 부모 키를 참조해 존재하지 않는 관계 차단 |
| CHECK | 급여·성별·카테고리처럼 허용 범위 제한 |

삭제 테스트는 단순히 행을 지우는 연습이 아니었다. 상품 삭제 후 주문상세의 상품 FK, 주문 삭제 후 주문상세 행, 회원 삭제 후 주문의 회원 FK가 어떻게 바뀌는지 조회하고 `ROLLBACK`해 원상복구하면서 `ON DELETE` 업무 규칙을 검증했다.

## 헷갈린 점 / 질문

- `COMMIT` 후에는 `ROLLBACK`으로 되돌릴 수 없다.
- DBeaver 기본 Auto Commit이 켜져 있으면 실행 즉시 확정될 수 있으므로, 트랜잭션 실습 전 Manual Commit 설정이 중요하다.
- `ON DELETE`는 단순 문법이 아니라 “데이터를 삭제할 때 무엇을 보존해야 하는가”라는 업무 규칙이다.
- 제약조건을 추가하기 전에 이미 위반 데이터가 있으면 제약조건 생성 자체가 실패한다. 먼저 현재 데이터를 검사·정리해야 한다.
- `SELECT MAX(oid)`는 현재 테이블의 가장 큰 주문번호를 조회할 뿐, 시퀀스 자체의 다음 값을 뜻하지 않는다. 수업에서는 `order_seq.nextval`이 새 번호를 발급했다.
- 시퀀스는 테이블에 종속된 컬럼이 아니라 별도 Oracle 객체다. 이름을 테이블에 맞추는 것은 관리 관례이지 강제 연결이 아니다.

## 이전·다음 흐름

- 이전: 03-16의 사용자·테이블 생성과 첫 `INSERT`를 실제 쇼핑몰 관계 구조로 확장했다.
- 다음: 03-18에는 정상/위반 데이터를 직접 넣어 제약조건을 테스트하고, `COMMIT`/`ROLLBACK`, DDL 변경, DQL 조건 조회로 이어간다.

## 관련 페이지

- [[concepts/oracle-sequence|Oracle 시퀀스]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.69~73 테이블 정의, p.88~108 주문/참조 무결성 실습
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.389~391 제약조건 개요
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03 Oraman ddl.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A03.Oraman ddl(선생님이 만든 버젼).sql`
