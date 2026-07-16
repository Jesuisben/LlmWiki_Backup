---
title: Primary Key vs Foreign Key
created: 2026-07-02
updated: 2026-07-15
type: comparison
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
status: growing
confidence: high
---

# Primary Key vs Foreign Key

## 비교 목적

PK와 FK는 관계형 데이터베이스의 연결고리다. 수업에서는 참조되는 컬럼과 참조하는 컬럼으로 구분했다.

## 한눈에 보기

| 항목 | Primary Key | Foreign Key |
|---|---|---|
| 한국어 | 기본키 | 외래키 |
| 역할 | 한 행을 유일하게 식별 | 다른 테이블의 PK 또는 UNIQUE 키를 참조 |
| 위치 | 부모 테이블 | 자식 테이블 |
| 예시 | `MEMBERS.ID` | `BOARDS.WRITER` |
| 제약 | 중복 불가, NULL 불가 | 부모에 있는 값 또는 NULL |

## 예시

```sql
ALTER TABLE ORAMAN.BOARDS
ADD CONSTRAINT BOARDS_MEMBERS_FK
FOREIGN KEY (WRITER)
REFERENCES ORAMAN.MEMBERS(ID)
ON DELETE SET NULL;
```

여기서 `MEMBERS.ID`는 참조되는 기본키이고, `BOARDS.WRITER`는 참조하는 외래키다.

## 구체적인 선택 상황

1. 회원 한 명을 중복 없이 찾으려면 `MEMBERS.ID`를 PK로 둔다. 이름은 동명이인이 있을 수 있어 행 식별 기준으로 쓰기 어렵다.
2. 게시글이 어느 회원의 것인지 연결하려면 `BOARDS.WRITER`를 FK로 둔다. 주문상세가 어느 주문에 속하는지는 `ORDERDETAILS.OID → ORDERS.OID` FK로 표현한다.

```sql
ALTER TABLE ORDERDETAILS ADD CONSTRAINT ORDERDETAILS_ORDERS_FK
FOREIGN KEY (OID) REFERENCES ORDERS(OID) ON DELETE CASCADE;
```

## 헷갈리기 쉬운 포인트

- FK는 자식 테이블에 있지만, 값의 기준은 부모 테이블의 PK 또는 참조 가능한 UNIQUE 키다. 수업 예제는 모두 부모 PK를 참조했다.
- 부모에 없는 값을 FK로 넣으면 참조 무결성 오류가 난다.
- 정규화로 테이블을 나눈 뒤에는 PK/FK로 관계를 다시 연결해야 한다.
- PK는 항상 숫자일 필요가 없다. 수업의 `MEMBERS.ID`는 문자열이지만 행을 유일하게 식별한다.
- FK 컬럼이 자동으로 JOIN을 실행하는 것은 아니다. FK는 무결성을 검사하고 JOIN은 조회 결과를 만든다.
- 함수 종속성 `X → Y`를 “X는 PK, Y는 FK”로 그대로 치환하면 안 된다. 결정 관계와 키/참조 제약은 별도 판단이다.
- FK 자체는 `NULL`을 허용할 수 있지만 컬럼에 NOT NULL이 함께 있으면 허용되지 않는다. `ON DELETE SET NULL`을 선택하려면 해당 FK 컬럼이 nullable이어야 한다.

## 관련 페이지

- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]
- [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
