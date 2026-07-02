---
title: Oracle 참조 무결성과 ON DELETE
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
# Oracle 참조 무결성과 ON DELETE

## 참조 무결성

참조 무결성은 부모 테이블과 자식 테이블 사이의 연결이 깨지지 않도록 하는 규칙이다.

수업에서는 다음 조건을 정리했다.

- 부모 테이블의 값이 자식 테이블에서 사용 중이면 함부로 삭제할 수 없다.
- 자식 테이블의 외래키는 부모 테이블에 존재하는 값 또는 `NULL`이어야 한다.

예를 들어 `BOARDS.WRITER`가 `MEMBERS.ID`를 참조한다면, `MEMBERS`에 없는 `hello`라는 작성자를 `BOARDS`에 넣으면 오류가 난다.

```sql
insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'hello', 'abc123', 'db', '그룹 바이', default, '1988/07/17');
```

오류 메시지는 다음처럼 나타났다.

```text
ORA-02291: integrity constraint violated - parent key not found
```

의미는 “자식 테이블에 넣으려는 외래키 값이 부모 테이블의 기본키 목록에 없다”는 뜻이다.

## 제약조건 생성 전 데이터 확인

제약조건을 새로 만들 때 기존 데이터가 조건을 위반하고 있으면 제약조건 생성 자체가 실패한다.

수업에서는 `hello`라는 작성자가 회원 테이블에 없어서 FK 생성 시 오류가 났다.

```text
ORA-02298: cannot validate - parent keys not found
```

해결은 위반 데이터를 삭제하거나 수정한 뒤 제약조건을 다시 만드는 것이다.

```sql
DELETE FROM boards WHERE writer = 'hello';
COMMIT;
```

## ON DELETE 옵션

부모 데이터가 삭제될 때 자식 데이터가 어떻게 될지 정하는 옵션이다.

| 옵션 | 의미 | 수업 예시 |
|---|---|---|
| `ON DELETE SET NULL` | 부모가 삭제되면 자식 FK를 `NULL`로 변경 | 회원 탈퇴 후 게시물은 남기기 |
| `ON DELETE CASCADE` | 부모가 삭제되면 자식 행도 함께 삭제 | 주문 취소 시 주문상세도 삭제 |
| No Action | 자식이 있으면 부모 삭제 제한 | 학과/학생 관계 등 |

수업에서는 다음처럼 상황에 맞게 선택해야 한다고 정리했다.

- 회원이 탈퇴해도 게시물은 남겨야 하므로 `BOARDS.WRITER`는 `SET NULL`이 자연스럽다.
- 주문이 취소되면 주문상세는 함께 사라져야 하므로 `ORDERDETAILS.OID`는 `CASCADE`가 자연스럽다.

## CHECK 제약조건

`CHECK`는 저장 가능한 값의 범위나 조건을 제한한다.

예시는 다음과 같다.

```sql
ALTER TABLE ORAMAN.MEMBERS
ADD CONSTRAINT MEMBERS_PASSWORD_CHECK
CHECK (length(password) >= 3 and length(password) <= 50) ENABLE;
```

다른 예시는 다음과 같다.

- 성별: `gender in ('남자', '여자')`
- 결혼 여부: `marriage in ('결혼', '이혼', '미혼')`
- 급여: `salary >= 100`
- 상품 재고: `stock >= 0`
- 상품 카테고리: `category in ('bread', 'beverage', 'cake', 'macaron')`

## 데이터 사전

Oracle은 사용자가 가진 테이블, 시퀀스 같은 객체 정보를 데이터 사전에 기록한다.

```sql
SELECT table_name FROM user_tables;
SELECT * FROM user_sequences;
```

수업에서는 `user_객체명s` 형태로 이해했다.

- 테이블: `user_tables`
- 시퀀스: `user_sequences`

## 관련 페이지

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/oracle-sequence|Oracle 시퀀스]]

## 출처

- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
