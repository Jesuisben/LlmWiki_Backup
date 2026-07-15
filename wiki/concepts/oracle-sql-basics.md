---
title: Oracle SQL 기본
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A05.DQL 실습.sql
status: growing
confidence: high
---

# Oracle SQL 기본

## 정의

SQL(Structured Query Language)은 DBMS에 데이터를 조회·추가·수정·삭제하거나 테이블 구조와 권한을 제어하도록 요청하는 언어다. 이 수업에서는 Oracle Database를 DBeaver로 조작하면서 SQL을 배웠다.

## 수업에서 등장한 맥락

03-16에는 관리자 연결과 실습 사용자·`MEMBERS` 테이블을 만들며 DDL/DML을 처음 구분했다. 03-18에는 `PRODUCTS`·`BOARDS`를 대상으로 `SELECT`, `WHERE`, `DISTINCT`, alias, `LIKE`, `IN`, `BETWEEN`, `ORDER BY`를 순서대로 붙였다. 따라서 이 페이지의 SQL은 사전식 분류가 아니라 **환경 생성 → 데이터 입력 → 조건 조회**라는 수업 흐름의 공통 언어다.

## 왜 중요한가

웹서비스의 회원가입, 상품 목록, 상세 보기, 주문, 장바구니는 모두 DB 조회와 변경으로 이어진다. Java 객체가 메모리 안의 데이터를 다룬다면, SQL은 영구 저장소에 있는 데이터를 다룬다.

## SQL 분류

| 분류 | 역할 | 대표 명령 | 수업 맥락 |
|---|---|---|---|
| DQL | 데이터 조회 | `SELECT` | 상품 목록/상세 조회 |
| DML | 데이터 조작 | `INSERT`, `UPDATE`, `DELETE` | 회원/상품/주문 데이터 추가·수정·삭제 |
| DDL | 구조 정의 | `CREATE`, `ALTER`, `DROP` | 테이블·시퀀스·컬럼·제약조건 생성/변경 |
| TCL | 트랜잭션 제어 | `COMMIT`, `ROLLBACK` | DML 결과 확정/취소 |
| DCL | 권한 제어 | `GRANT`, `REVOKE` | View 조회 권한 부여/박탈 |

자세한 차이는 [[comparisons/ddl-vs-dml-vs-dql|DDL vs DML vs DQL]]에 정리했다.

## 기본 조회 문형

```sql
select *|{[distinct] column 리스트|표현식, [alias],
from 테이블 1[, 테이블 2, …]
[where condition]
[group by column]
[having column]
[order by column];
```

수업에서 강조한 것은 `SELECT`와 `FROM`은 기본이고, 나머지는 조건·그룹화·정렬이 필요할 때 붙는다는 점이다.

## DQL 실습 흐름

```sql
SELECT * FROM products;
SELECT name, price FROM products;
SELECT DISTINCT category FROM products;
SELECT name, price * 12 AS annual_price FROM products;
SELECT * FROM products WHERE num = 1;
SELECT * FROM products WHERE price BETWEEN 3500 AND 4500;
SELECT * FROM products WHERE category IN ('cake', 'beverage');
SELECT * FROM boards WHERE writer IS NOT NULL;
SELECT * FROM products WHERE name LIKE '_이%';
SELECT * FROM products ORDER BY category ASC, price DESC;
```

## 자주 헷갈리는 점

- SQL에서 `=`은 Java의 대입이 아니라 같다 비교다.
- 문자열과 날짜는 작은따옴표를 쓰고, 숫자는 따옴표 없이 쓴다. 다만 수업의 `'1990/12/25'` 날짜는 Oracle의 암시적 형변환에 의존하므로 세션의 NLS 날짜 형식에 따라 결과가 달라질 수 있다. 안전한 고정 형식은 `DATE '1990-12-25'` 또는 `TO_DATE`로 구분한다.
- `NULL`은 미지의 값이므로 `= NULL`이 아니라 `IS NULL` 또는 `IS NOT NULL`을 쓴다.
- `BETWEEN`은 양 끝값을 포함한다.
- `LIKE`의 `_`는 한 글자, `%`는 0개 이상의 문자열이다.
- `ORDER`는 SQL 키워드이므로 테이블 이름으로 쓰지 않는 것이 좋다.

## 선행·후속 연결

- 선행: Java에서 변수·객체의 값을 다뤘다면 SQL에서는 행과 컬럼의 영구 데이터를 다룬다. 다만 Oracle 수업에서 객체-테이블 매핑을 직접 구현한 것은 아니다.
- 후속: 기본 DQL에 함수와 집계를 붙이면 [[concepts/oracle-sql-functions|Oracle SQL 함수]], 테이블을 연결하면 [[concepts/oracle-join|Oracle JOIN]], 조회 결과를 조건으로 재사용하면 [[concepts/oracle-subquery|Oracle 서브쿼리]]로 이어진다.
- Spring/JPA 확장: Repository와 JPQL은 뒤 과목에서 등장하며 [[comparisons/jpql-vs-sql|JPQL vs SQL]]에서 직접 SQL과 구분한다.

## 관련 개념

- [[entities/oracle-database|Oracle Database]]
- [[entities/dbeaver|DBeaver]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/oracle-sql-functions|Oracle SQL 함수]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.34~36 SQL 분류, p.134~195 DQL
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/A05.DQL 실습.sql`
