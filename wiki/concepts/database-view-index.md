---
title: Database View와 Index
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
status: growing
confidence: high
---
# Database View와 Index

## View

View는 물리적인 테이블을 직접 복사하는 것이 아니라, 기존 테이블의 일부를 보여주는 논리적 가상 테이블이다.

수업에서는 `oraman` 사용자의 테이블 일부를 `gomdori` 사용자에게 보여주는 예시를 다뤘다.

```sql
CREATE VIEW view01
AS
SELECT name, password, gender
FROM MEMBERS
WHERE gender = '남자';
```

다른 사용자에게 View 조회 권한을 줄 수 있다.

```sql
GRANT SELECT ON view01 TO gomdori;
```

권한을 박탈할 때는 `REVOKE`를 사용한다.

```sql
REVOKE SELECT ON view01 FROM gomdori;
```

View는 민감한 테이블 전체를 공개하지 않고 일부 컬럼/행만 보여줄 때 유용하다.

## Index

인덱스는 책의 목차처럼 데이터를 빠르게 찾기 위한 구조다. 수업에서는 인덱스가 주로 다음 시점에 생성된다고 배웠다.

- Primary Key 생성 시
- Unique 제약조건 생성 시

즉 PK/UK는 단순 제약조건일 뿐 아니라 검색 성능과도 연결된다.

## 관련 페이지

- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]

## 출처

- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
