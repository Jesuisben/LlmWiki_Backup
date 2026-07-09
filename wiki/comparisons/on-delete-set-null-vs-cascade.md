---
title: ON DELETE SET NULL vs CASCADE
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
status: growing
confidence: high
---

# ON DELETE SET NULL vs CASCADE

## 비교 목적

부모 테이블의 행이 삭제될 때 자식 테이블을 어떻게 처리할지 정하는 옵션이다. 수업에서는 게시물·주문·주문상세 예제로 업무 의미에 맞게 선택해야 한다고 배웠다.

## 한눈에 보기

| 항목 | SET NULL | CASCADE |
|---|---|---|
| 동작 | 자식 FK 값을 `NULL`로 바꿈 | 자식 행을 함께 삭제 |
| 데이터 보존 | 자식 행은 남음 | 자식 행도 사라짐 |
| 수업 예시 | 회원 탈퇴 후 게시물 보존 | 주문 취소 후 주문상세 삭제 |
| 사용 기준 | 원 기록은 남기고 연결만 끊을 때 | 부모 없이는 자식 의미가 없을 때 |

## 예시

```sql
ALTER TABLE ORAMAN.BOARDS
ADD CONSTRAINT BOARDS_MEMBERS_FK
FOREIGN KEY (WRITER)
REFERENCES ORAMAN.MEMBERS(ID)
ON DELETE SET NULL;
```

```sql
ALTER TABLE BLUESKY.ORDERDETAILS
ADD CONSTRAINT ORDERDETAILS_ORDERS_FK
FOREIGN KEY ("OID")
REFERENCES BLUESKY.ORDERS("OID")
ON DELETE CASCADE;
```

## 헷갈리기 쉬운 포인트

`ON DELETE`는 “문법적으로 뭐가 맞나”보다 “업무적으로 무엇을 보존해야 하나”의 문제다. 게시물은 작성자가 탈퇴해도 남길 수 있지만, 주문상세는 주문이 사라지면 독립적으로 의미를 갖기 어렵다.

## 관련 페이지

- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
