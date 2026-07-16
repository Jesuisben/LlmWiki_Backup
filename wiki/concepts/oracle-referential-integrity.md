---
title: Oracle 참조 무결성과 ON DELETE
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
status: growing
confidence: high
---

# Oracle 참조 무결성과 ON DELETE

## 정의

참조 무결성은 부모 테이블과 자식 테이블 사이의 연결이 깨지지 않도록 지키는 규칙이다. 부모 테이블의 기본키(PK)를 자식 테이블의 외래키(FK)가 참조한다.

## 수업에서 등장한 맥락과 구현 역할

03-17에는 `MEMBERS.ID → BOARDS.WRITER`, `MEMBERS.ID → ORDERS.MID`, `ORDERS.OID → ORDERDETAILS.OID`, `PRODUCTS.NUM → ORDERDETAILS.PNUM` 관계를 만들었다. 부모에 없는 `hello` 작성자 때문에 FK 생성이 실패하는 상황과, 회원·상품·주문 삭제 시 자식을 어떻게 처리할지를 직접 비교했다. 03-20에는 `DEPARTMENTS`·`STUDENTS`·`SUBJECTS` 관계로 같은 원리를 데이터 모델링 단계에서 다시 확인했다.

## 부모/자식 테이블

| 역할 | 예시 | 설명 |
|---|---|---|
| 부모 테이블 | `MEMBERS` | 참조되는 기본키 `ID`를 가짐 |
| 자식 테이블 | `BOARDS` | 부모의 `ID`를 `WRITER`로 참조 |

수업에서는 참조 “되는” 컬럼이 PK, 참조 “하는” 컬럼이 FK라고 정리했다. 비교는 [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]에 따로 정리했다.

## 참조 무결성 오류

부모에 없는 값을 자식에 넣으면 오류가 난다.

```sql
insert into boards(no, writer, password, subject, content, readhit, regdate)
values(board_seq.nextval, 'hello', 'abc123', 'db', '그룹 바이', default, '1988/07/17');
```

```text
ORA-02291: integrity constraint violated - parent key not found
```

이미 위반 데이터가 있는 상태에서 FK를 만들면 `ORA-02298`이 발생할 수 있다. 수업에서는 `hello` 작성자를 지우고 다시 FK를 만들었다.

```sql
DELETE FROM boards WHERE writer = 'hello';
COMMIT;
```

## ON DELETE 옵션

| 옵션 | 의미 | 수업 예시 |
|---|---|---|
| `ON DELETE SET NULL` | 부모 삭제 시 자식 FK를 `NULL`로 변경 | 회원 탈퇴 후 게시물은 남김 |
| `ON DELETE CASCADE` | 부모 삭제 시 자식 행도 삭제 | 주문 취소 시 주문상세도 삭제 |
| No Action | 자식이 있으면 부모 삭제 제한 | 학과에 학생이 있으면 학과 삭제 제한 |

업무 규칙 비교는 [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]에 정리했다.

## 자주 틀리는 이해

- JOIN은 값이 맞으면 FK 없이도 가능하지만, FK가 없으면 부모에 없는 자식 값을 DB가 막아주지 못한다.
- `SET NULL`을 선택하려면 자식 FK 컬럼이 `NULL`을 허용해야 한다. 게시글은 남기되 작성자 연결만 끊는 수업 예제가 이 선택이었다.
- `CASCADE`가 항상 편한 기본값은 아니다. 주문-주문상세처럼 생명주기가 함께 가는 경우와 회원-게시글처럼 기록을 남길 경우를 구분해야 한다.
- Oracle FK DDL에는 `ON DELETE NO ACTION`이라는 문구를 직접 쓰지 않는다. 삭제 옵션을 생략하면 자식 행이 있는 부모 삭제를 제한하는 기본 동작이 된다.

## Oracle 직접 수업과 후속 JPA 연결

Oracle 수업에서는 FK DDL과 삭제 오류·옵션을 SQL로 검증했다. 이후 Spring Data JPA에서는 Entity 연관관계와 cascade/orphan 동작이 별도로 등장하지만, JPA cascade와 DB의 `ON DELETE CASCADE`는 같은 설정이 아니다. 이 페이지는 Oracle의 DB 제약조건 범위까지만 근거로 삼는다.

## 관련 페이지

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.94~108 참조 무결성/ON DELETE
