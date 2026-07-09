---
title: Oracle 참조 무결성과 ON DELETE
created: 2026-07-02
updated: 2026-07-02
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

## 관련 페이지

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.94~108 참조 무결성/ON DELETE
