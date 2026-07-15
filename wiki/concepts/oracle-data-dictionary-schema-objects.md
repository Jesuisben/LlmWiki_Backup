---
title: Oracle 데이터 사전과 schema 객체
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-3.sql
status: growing
confidence: high
---

# Oracle 데이터 사전과 schema 객체

## 정의

Oracle 데이터 사전(data dictionary)은 테이블 안의 업무 데이터가 아니라 **DB 객체의 구조와 상태를 설명하는 metadata**를 조회하는 뷰 집합이다. 수업에서는 현재 사용자 schema가 소유한 테이블·시퀀스·View를 `USER_*` 뷰로 확인했다.

## 수업에서 등장한 맥락

03-17에는 테이블과 시퀀스를 삭제·재생성하면서 실제 객체가 남아 있는지 `USER_TABLES`, `USER_SEQUENCES`로 확인했다. 03-20에는 `view01`, `view02`를 만든 뒤 `USER_VIEWS`에서 View 이름과 SELECT 정의를 조회했다. 따라서 데이터 사전은 객체 문법을 외우는 표가 아니라 **DDL 실행 결과를 검증하는 도구**로 등장했다.

## 핵심 `USER_*` 뷰

| 데이터 사전 뷰 | 수업에서 확인한 대상 |
|---|---|
| `USER_TABLES` | 현재 사용자 소유 테이블 이름 |
| `USER_SEQUENCES` | 현재 사용자 소유 시퀀스와 옵션 |
| `USER_VIEWS` | 현재 사용자 소유 View 이름과 정의 |

`USER_*`는 현재 로그인한 사용자를 기준으로 하므로 `oraman`과 `gomdori` 연결에서 보이는 소유 객체가 같다고 가정하면 안 된다. DBeaver의 connection과 active datasource를 먼저 확인해야 하는 이유다.

## 실제 수업 SQL

```sql
SELECT TABLE_NAME FROM user_tables;
SELECT * FROM user_sequences ;
SELECT view_name, text FROM user_views ;
SELECT view_name, text FROM user_views WHERE view_name = 'VIEW01' ;
```

03-20에는 `'view01'` 조건이 오류 없이 0행을 반환하고 `'VIEW01'`에서 조회되는 차이를 확인했다. 따옴표 없이 만든 Oracle 식별자는 데이터 사전에 보통 대문자로 저장되므로 객체 이름 조건도 대문자로 맞춘다.

## 자주 헷갈리는 점

- 데이터 사전은 회원·상품 행을 조회하는 업무 테이블이 아니라 테이블·시퀀스·View 같은 객체의 metadata를 조회한다.
- SQL 키워드는 대소문자를 구분하지 않는 경우가 많지만, 문자열 리터럴 `'view01'`과 `'VIEW01'`은 같은 값이 아니다.
- “모든 데이터 사전 값이 무조건 대문자”로 일반화하지 않는다. 수업에서 확인한 것은 **따옴표 없이 생성한 객체 이름**이 대문자로 관리되는 동작이다.
- DBeaver 왼쪽 트리에 객체가 보이지 않을 때는 새로 고침만 누르기 전에 active connection과 `USER_*` 조회 결과를 함께 확인한다.
- `USER_TABLES`에서 테이블이 보인다고 FK·CHECK까지 모두 검증한 것은 아니다. 객체 종류에 맞는 metadata를 별도로 확인해야 한다.

## 선행·후속 연결

- [[concepts/oracle-sequence|Oracle 시퀀스]]를 만든 뒤 `USER_SEQUENCES`로 존재와 옵션을 확인한다.
- [[concepts/database-view-index|Database View와 Index]]의 View 생성 결과는 `USER_VIEWS`로 확인한다.
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]에서 DDL 실행 전후의 객체 상태를 검증하는 데 사용한다.
- [[entities/dbeaver|DBeaver]]의 객체 트리와 데이터 사전 SQL은 같은 Oracle schema를 서로 다른 방식으로 보여준다.

## 관련 페이지

- [[summaries/2026-03-17-oracle-ddl-dml-constraints-sequence|2026-03-17 Oracle DDL/DML, 제약조건, 시퀀스]]
- [[summaries/2026-03-20-database-modeling-normalization-view-index|2026-03-20 데이터 모델링, 정규화, View, Index]]
- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/Oracle 총정리/Oracle 총정리.md`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A02.오라맨 스크립트.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-3.sql`
