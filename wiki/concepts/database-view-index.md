---
title: Database View와 Index
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-3.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-4.sql
status: growing
confidence: high
---

# Database View와 Index

## 수업에서 등장한 맥락

03-20 정규화 실습 뒤에는 테이블을 더 나누는 대신, 사용자가 필요한 결과만 다시 보여주는 View와 데이터를 찾는 구조인 Index를 배웠다. View는 조회 결과·권한의 관점, Index는 검색 경로의 관점이므로 같은 객체 단원에 등장했지만 역할은 다르다.

## 왜 중요한가

정규화한 기본 테이블을 그대로 모두 노출하지 않고 필요한 조회 결과와 권한만 제공하는 방법을 익히며, PK/UNIQUE와 함께 조회 경로를 만드는 Index의 위치를 이해한다. 즉 테이블 설계 이후의 **조회 인터페이스와 검색 구조**를 구분하는 단계다.

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

수업의 두 번째 View는 회원과 게시글을 JOIN한 결과였다.

```sql
CREATE OR REPLACE VIEW view02
as
SELECT m.name, m.gender, b.subject, b.content
from members m INNER JOIN boards b
ON m.id = b.writer ;
```

실행 주체도 구분해야 한다. 관리자는 `CREATE VIEW` 시스템 권한을 부여하고, 소유자 `oraman`은 View 생성·객체 권한 부여/박탈을 수행한다. `gomdori`는 `oraman.view01`처럼 schema를 붙여 조회하며, `REVOKE` 뒤에는 View 객체가 남아 있어도 접근이 실패한다.

## 데이터 사전

```sql
SELECT view_name, text FROM user_views;
SELECT view_name, text FROM user_views WHERE view_name = 'VIEW01';
```

Oracle 데이터 사전의 객체 이름은 대문자로 관리되므로 `'view01'`이 아니라 `'VIEW01'`로 검색해야 한다.

## 자주 헷갈리는 점

- 수업 예제는 `password` 컬럼을 View에 포함했지만, 이는 문법 확인용 원본 실습이다. 실제 서비스 설계에서는 인증 비밀값을 조회용 View나 일반 사용자 권한에 노출하지 않는다는 보안 경계를 함께 기억해야 한다.
- View는 조회 결과에 이름을 붙인 가상 테이블이지, 원본 행을 별도 복사한 백업 테이블이 아니다.
- Index는 View와 같은 조회 결과가 아니라 데이터를 찾기 위한 구조다.

## Index

Index는 책의 목차처럼 데이터를 빠르게 찾기 위한 구조다. 수업에서는 Primary Key나 Unique 제약조건 생성 시 내부적으로 인덱스가 만들어질 수 있다고 배웠다.

## 수업에서 직접 확인한 범위

- View: `CREATE OR REPLACE VIEW`, `GRANT SELECT`, schema 접두사 조회, `REVOKE`, `user_views` 확인을 실제 SQL로 수행했다.
- Index: 검색을 돕는 구조라는 개념과 PK/UNIQUE 생성 시 내부 인덱스가 생길 수 있다는 설명까지 다뤘다.
- 원본에는 별도 `CREATE INDEX` 성능 비교나 실행 계획 측정 결과가 없다. 따라서 특정 속도 향상 수치나 운영 튜닝 결과를 이 페이지에서 단정하지 않는다.

## 선행·후속 연결

- 선행: [[concepts/database-modeling-normalization|정규화]]로 기본 테이블을 나누고 [[concepts/oracle-join|JOIN]]으로 관계를 읽는다.
- 후속: Spring/JPA에서는 View나 Index와 별개로 Entity/Repository가 등장한다. Oracle 수업에서는 그 매핑을 직접 구현하지 않았다.

## 관련 페이지

- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전과 schema 객체]]
- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.446~448 View
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-3.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-4.sql`
