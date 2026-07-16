---
title: Oracle 시퀀스
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
status: growing
confidence: high
---
# Oracle 시퀀스

## 정의

시퀀스는 자동 번호표 기계처럼 이해할 수 있다. 게시물 번호가 매번 1씩 증가해야 할 때, 이전 번호를 사람이 기억하고 계산하면 피로하고 실수하기 쉽다.

수업에서는 `board_seq`, `product_seq`, `order_seq`, `orderdetail_seq` 같은 시퀀스를 만들었다.

03-16에는 시퀀스 개념을 미리 보고, 03-17에는 `ORDERS`와 `ORDERDETAILS` INSERT에서 실제 번호를 발급했으며, 03-18에는 실습 사용자를 재생성한 뒤 DDL 스크립트로 시퀀스까지 복구했다. 즉 시퀀스는 테이블 생성과 별도로 백업·재생성해야 하는 schema 객체다.

## 이 수업에서 처음 등장하고 확장된 날짜

| 날짜 | 학습 위치 | 대표 artifact |
|---|---|---|
| 03-16 Oracle | 시퀀스 개념과 게시물·상품 번호 예고 | `board_seq`, `product_seq` |
| [[summaries/2026-03-17-oracle-ddl-dml-constraints-sequence|03-17 Oracle]] | 독립 sequence 생성, `NEXTVAL` INSERT, `USER_SEQUENCES` 확인 | `order_seq`, `orderdetail_seq` |
| [[summaries/2026-03-18-oracle-constraints-validation|03-18 Oracle]] | 사용자·테이블·시퀀스 DDL 복구와 제약조건 테스트 | schema 복구 스크립트 |
| [[summaries/2026-03-30-fullstack-environment-setup|03-30 FrontEnd_BackEnd]] | Oracle 직접 SQL 환경에서 MySQL Driver·dialect를 쓰는 Spring Boot 환경으로 전환 | MySQL datasource/JPA 설정 |
| [[summaries/2026-04-02-react-bootstrap-homepage|04-02 FrontEnd_BackEnd]] | Member id에 JPA `@GeneratedValue(strategy = GenerationType.AUTO)` 등장 | `Member.id` |
| [[summaries/2026-04-16-cart-quantity-stock|04-16 FrontEnd_BackEnd]] | Order·OrderProduct id에도 같은 annotation 사용 | `Order.id`, `OrderProduct.id` |

03-16~03-18은 Oracle sequence 자체의 직접 학습이다. 03-30 이후는 DB와 구현 방식이 바뀐 후속 경계이며, JPA annotation을 Oracle sequence 실습과 같은 구현으로 합치지 않는다.

주요 옵션은 다음과 같다.

| 옵션 | 의미 |
|---|---|
| `START WITH` | 시작값 |
| `INCREMENT BY` | 증가값 |
| `MINVALUE` | 최소값 |
| `MAXVALUE` | 최대값 |
| `NOCYCLE` | 끝까지 가도 다시 처음으로 돌아가지 않음 |
| `NOCACHE` | 미리 번호를 뽑아두지 않음 |

수업의 `product_seq` 예시는 시작값 41, 증가값 1, 최소값 0, `NOCYCLE`, `NOCACHE`로 만들었다. 시퀀스의 다음 값은 `nextval`로 가져오며, 게시물 INSERT의 번호 자리에 `board_seq.nextval`을 사용했다.

객체 존재와 옵션은 [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전]]으로 확인했다.

객체 존재와 옵션을 확인한 조회는 `SELECT * FROM user_sequences;`였다.

## 왜 중요한가와 직접 수업의 헷갈리는 점

- 주문·게시물처럼 여러 사용자가 새 행을 만드는 기능에서 사람이 “현재 최대값 + 1”을 계산하는 방식을 피하게 한다.
- `SELECT MAX(oid)`는 테이블에 저장된 주문번호의 최댓값이고, 시퀀스의 다음 번호를 조회하는 문장이 아니다.
- `order_seq`라는 이름이 `ORDERS`와 관련 있음을 보여줄 뿐, DB가 둘을 자동 연결하지는 않는다. INSERT에서 `order_seq.nextval`을 직접 사용한다.
- PK용 시퀀스를 `CYCLE`로 두면 값이 다시 돌아와 기존 PK와 충돌할 수 있으므로 총정리에서는 `NOCYCLE`을 주의점으로 남겼다.
- `NEXTVAL`로 이미 발급한 번호는 INSERT가 rollback돼도 시퀀스로 반환되지 않는다. 따라서 번호 사이에 빈 값이 생길 수 있으며 시퀀스는 gapless 번호 생성기가 아니다.
- `NOCACHE`는 미리 번호를 보관하지 않는 옵션이지, rollback·동시 실행·실패 상황에서 번호가 절대 비지 않는다는 보장이 아니다.
- 03-30 이후 Spring/JPA 과정은 MySQL 환경에서 시작했다. JPA의 ID 생성 전략은 “새 행의 식별값을 생성한다”는 목적에서 연결되지만, Oracle 시퀀스 실습이 같은 DB 환경으로 그대로 이어진 것은 아니다.

## Oracle sequence와 MySQL/JPA GeneratedValue의 경계

| 구분 | Oracle 직접 수업 | 4과목 MySQL/JPA 후속 |
|---|---|---|
| 선언 위치 | `CREATE SEQUENCE ...` DDL로 DB schema 객체 생성 | Entity id 필드에 `@GeneratedValue(strategy = GenerationType.AUTO)` 작성 |
| 사용 방식 | INSERT에서 `order_seq.nextval`처럼 sequence 이름과 `NEXTVAL`을 직접 사용 | Entity 저장 시 JPA/provider에 식별값 생성을 위임 |
| 확인 방식 | `USER_SEQUENCES`와 DDL 스크립트로 객체 존재·옵션 확인 | Entity annotation과 애플리케이션 재실행 후 생성 대상 안내 확인 |
| DB 환경 | Oracle | MySQL dialect를 설정한 Spring Boot 과정 |
| 이번 원본의 확정 범위 | sequence 이름·옵션·NEXTVAL·데이터 사전 조회 | `GenerationType.AUTO` annotation 존재 |

R14는 애플리케이션 재실행 뒤 `orders`, `order_products`와 관련 생성 대상을 확인하도록 기록하지만, 이 사실만으로 Oracle sequence와 동일한 schema 객체를 사용했다고 해석하지 않는다. `GenerationType.AUTO`가 실제 MySQL에서 어떤 내부 전략을 선택했는지, MySQL `AUTO_INCREMENT`를 정확히 어떤 DDL로 설정했는지는 이번 원본에 확인되는 범위를 넘어선다.

따라서 “Oracle sequence = `@GeneratedValue`”가 아니다. 둘은 새 행의 식별값 생성이라는 기능 목적은 비슷하지만, 선언 주체·DB 객체·호출 방식·provider 관여가 다르다.

## 입력 → 처리 → 결과

| 단계 | 입력 | 처리 | 결과 |
|---|---|---|---|
| Oracle 번호 발급 | 새 주문·주문상세 INSERT | 각각 `order_seq.nextval`, `orderdetail_seq.nextval` 사용 | OID·ODID 값 발급 후 행 저장 |
| Oracle 객체 검증 | 현재 사용자 schema | `USER_SEQUENCES` 조회 | 소유 sequence와 옵션 확인 |
| Oracle 복구 | 테이블·sequence 삭제 뒤 DDL 스크립트 | schema 객체 재생성 | sequence도 테이블과 별도로 복구 |
| JPA 후속 | 새 Member·Order·OrderProduct Entity 저장 | id 필드의 `GenerationType.AUTO`에 생성 위임 | 저장 후 id를 사용하는 코드 경로; 실제 DB 전략은 미확정 |

## 구현 완료 범위와 미확정 범위

- **Oracle 직접 완료 범위:** sequence 생성, NEXTVAL INSERT, `MAX(oid)`와의 차이, `USER_SEQUENCES` 확인, 삭제·재생성이 확인된다.
- **MySQL/JPA 확인 범위:** 03-30 MySQL 환경 전환, 04-02 Member와 04-16 Order/OrderProduct의 `@GeneratedValue(strategy = GenerationType.AUTO)`가 확인된다.
- **미확정:** MySQL `AUTO_INCREMENT`의 실제 DDL, `GenerationType`별 DB 동작 일반표, provider가 선택한 실제 생성 전략, Oracle sequence와 동일 객체 사용은 원본으로 확정하지 않는다.

## 자주 헷갈리는 원인

- **목적이 같으면 구현도 같다고 봄:** 식별값 생성 목적은 비슷하지만 Oracle DB sequence와 JPA annotation은 다른 계층이다.
- **sequence 이름이 테이블과 자동 연결된다고 봄:** Oracle INSERT에서 `NEXTVAL`을 직접 써야 했다.
- **`MAX(id)+1`을 sequence로 봄:** 저장된 최댓값 조회와 다음 번호 발급은 다르다.
- **`AUTO`를 `AUTO_INCREMENT`와 같은 단어로 치환함:** 실제 DB/provider 전략을 원본 없이 확정하면 안 된다.
- **JPA가 Oracle 수업의 연속 DB라고 봄:** 4과목은 MySQL Driver와 MySQL dialect로 시작했다.

## 이전 개념과 이후 기능 연결

- Oracle schema 객체의 존재 확인은 [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전과 schema 객체]]가 맡는다.
- 번호 발급과 PK/FK 검증이 한 INSERT에서 만난 흐름은 [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]로 연결된다.
- 4과목의 Entity id와 관계 세부는 [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]], 저장 호출은 [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]에 위임한다.
- Oracle 직접 SQL과 후속 JPA query 계층은 [[comparisons/jpql-vs-sql|JPQL vs SQL]]에서 구분한다.

## 직접 수업·교안·후속 과목 경계

- **직접 수업:** 03-16~03-18 Oracle sequence 생성·사용·검증·복구다.
- **교안 보충:** Oracle 교안 p.328~330의 sequence 설명은 기존 직접 수업 내용을 보강하는 source로 유지한다.
- **FrontEnd_BackEnd 후속:** R01은 MySQL/JPA 환경 전환, 04-02·R14는 `GeneratedValue(AUTO)` 등장과 확장 근거다. Oracle sequence 직접 수업에 합치지 않는다.
- **더 뒤의 경계:** Linux·AWS·CI/CD는 실행·배포, Passwordless는 인증, 중간 프로젝트는 응용 범위다. 식별자 생성 방식의 직접 학습 근거가 아니다.

## 관련 페이지

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/oracle-data-dictionary-schema-objects|Oracle 데이터 사전과 schema 객체]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.328~330 시퀀스
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md` — Oracle 이후 MySQL/JPA 환경 전환
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md` — Member의 `GeneratedValue(AUTO)` 첫 등장
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md` — Order·OrderProduct의 `GeneratedValue(AUTO)` 확장
