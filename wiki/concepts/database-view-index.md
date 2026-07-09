---
title: Database View와 Index
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
status: growing
confidence: high
---

# Database View와 Index

## View

View는 물리 테이블의 데이터를 복사해 저장하는 것이 아니라, `SELECT` 결과를 이름 붙여 보여주는 논리적 가상 테이블이다.

```sql
GRANT CREATE VIEW TO oraman;

CREATE OR REPLACE VIEW view01
AS
SELECT name, password, gender
FROM MEMBERS
WHERE gender = '남자';
```

다른 사용자에게 View 조회 권한을 줄 수 있다.

```sql
GRANT SELECT ON view01 TO gomdori;
SELECT * FROM oraman.view01;
REVOKE SELECT ON view01 FROM gomdori;
```

## 데이터 사전

```sql
SELECT view_name, text FROM user_views;
SELECT view_name, text FROM user_views WHERE view_name = 'VIEW01';
```

Oracle 데이터 사전의 객체 이름은 대문자로 관리되므로 `'view01'`이 아니라 `'VIEW01'`로 검색해야 한다.

## Index

Index는 책의 목차처럼 데이터를 빠르게 찾기 위한 구조다. 수업에서는 Primary Key나 Unique 제약조건 생성 시 내부적으로 인덱스가 만들어질 수 있다고 배웠다.

## 관련 페이지

- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.446~448 View
