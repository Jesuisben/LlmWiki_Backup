---
title: 함수 종속성과 정규화
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
status: growing
confidence: high
---

# 함수 종속성과 정규화

## 정의

함수 종속성은 어떤 속성 X를 알면 다른 속성 Y가 결정되는 관계다. 정규화에서는 이 관계를 분석해 테이블을 어떻게 나눌지 판단한다.

## 왜 중요한가

중복 표를 느낌대로 쪼개지 않고, 어떤 값이 다른 값을 결정하는지 근거를 세워 학생·학과·성적의 저장 위치를 정하게 한다. 그 결과 삽입·갱신·삭제 이상을 줄이고 분리한 관계를 PK/FK와 JOIN으로 구현·복원할 수 있다.

## 이 수업에서 처음 등장하고 확장된 날짜

| 날짜 | 학습 위치 | 대표 artifact |
|---|---|---|
| [[summaries/2026-03-20-database-modeling-normalization-view-index|03-20 Oracle]] | 함수 종속성·이상 현상·1NF~3NF로 학생·학과·성적 테이블을 분해하고 FK DDL과 오류로 검증 | `STUDENTS`, `DEPARTMENTS`, `SUBJECTS` |
| [[summaries/2026-03-30-fullstack-environment-setup|03-30 FrontEnd_BackEnd]] | Oracle 직접 SQL 수업에서 MySQL·Spring Data JPA 애플리케이션 환경으로 전환 | MySQL dialect·Spring Data JPA dependency |
| [[summaries/2026-04-16-cart-quantity-stock|04-16 FrontEnd_BackEnd]] | 주문과 주문 품목을 별도 Entity로 두고 Product·Member 관계를 표현한 후속 적용 | `Order`, `OrderProduct`, `OrderRepository` |

정규화 원리는 03-20 Oracle에서 직접 배웠다. 04-16의 Order/OrderProduct는 그 원리를 다시 설명한 수업이 아니라, 이미 분리된 업무 대상을 MySQL/JPA 애플리케이션 모델로 표현한 후속 사례다.

## 자주 틀리는 이해

> 03-20 원본의 “X는 기본키, Y는 외래키”라는 메모는 함수 종속성의 일반 정의로 사용하지 않는다. 결정자 X가 후보키가 아닐 수도 있고, 종속 속성 Y가 FK가 아닐 수도 있다. PK/FK 여부는 행 식별과 다른 테이블 참조라는 별도 설계 판단이다.

## 수업 예시

- `학생번호 → 이름`
- `학생번호 → 주소`
- `학생번호 → 학과`
- `학과 → 사무실`

`학생번호 → 학과`이고 `학과 → 사무실`이면 `학생번호 → 사무실`도 성립한다. 이것이 이행적 함수 종속이다.

## 이상 현상과 정규화

| 이상 현상 | 의미 | 수업 예시 |
|---|---|---|
| 삽입 이상 | 불필요한 데이터까지 넣어야 함 | 신설 학과 등록 시 학생 정보 필요 |
| 갱신 이상 | 중복 데이터 일부만 바뀜 | 주민번호 변경이 일부 행에만 반영 |
| 삭제 이상 | 보존할 정보까지 사라짐 | 학생 삭제 시 학과 정보도 사라짐 |

## 복합 기본키

학생 성적 예제에서는 성적을 알기 위해 “학번 + 과목 코드”가 함께 필요했다.

수업 표의 핵심 결정 관계는 `{학번, 과목 코드} → 성적`이다.

그래서 `{학번, 과목 코드}`가 복합 기본키가 된다. 학번은 학생 테이블을 참조하는 외래키가 될 수 있다.

## 정규화 판단으로 연결하기

- `학생번호 → 이름/주소/학과`: 학생 한 명의 속성은 학생 테이블에 둔다.
- `학과 → 사무실`: 학과마다 반복되는 사무실은 학과 테이블에 분리해 갱신 이상을 줄인다.
- `{학번, 과목 코드} → 성적`: 한 학생의 한 과목 성적은 두 값의 조합으로 식별한다.
- 분리 후에는 FK를 만들어 부모에 없는 학과나 학생을 참조하지 못하게 한다.

원본 표에서 이름·주소·학과를 모두 “외래키”로 적은 부분도 그대로 일반화하지 않는다. 이 예제에서 실제 FK인지는 다른 테이블의 키를 참조하는 DDL이 있는지로 판정한다.

## 원리에서 구현으로 내려가는 계층

| 계층 | 답하는 질문 | 이 수업의 예 |
|---|---|---|
| 함수 종속성 | 어떤 속성이 어떤 속성을 결정하는가 | `학과 → 사무실`, `{학번, 과목 코드} → 성적` |
| 정규화·테이블 분해 | 중복과 이상을 줄이려면 정보를 어디에 나눌 것인가 | 학생·학과·성적 관계 분리 |
| PK/FK·제약조건 | 행을 어떻게 식별하고 분리한 테이블의 참조를 DB가 어떻게 검사할 것인가 | 복합 PK, `FOREIGN KEY ... REFERENCES ...` |
| JOIN | 분리한 정보를 조회 결과에서 어떻게 다시 조합할 것인가 | 학생·학과·성적 연결 조회 |
| JPA Entity 관계 | Java 애플리케이션에서 분리된 테이블 관계를 어떤 객체 참조로 표현할 것인가 | 04-16 Order와 OrderProduct의 후속 적용 |

함수 종속성을 PK/FK와 같은 말로 바꾸면 분석 원리와 구현 장치를 섞게 된다. 정규화가 끝났다고 JPA annotation이 자동으로 정해지는 것도 아니다. DB 설계 결과를 실제 Entity와 관계로 옮기는 세부 책임은 [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]이 맡는다.

### 정규형과 함수 종속성의 연결

| 정규형 | 이 예제에서 줄이려는 문제 |
|---|---|
| 1NF | 한 칸의 반복값을 원자값으로 정리하고 `{학번, 과목 코드}`로 한 성적 행을 식별한다. |
| 2NF | 복합키 일부인 학번만으로 결정되는 이름·주민번호·학과를 성적 관계에서 분리한다. |
| 3NF | `학생번호 → 학과 → 대학/사무실`처럼 키가 아닌 속성을 거치는 이행적 종속을 학과 테이블로 분리한다. |

## 정규화 실습

수업 DDL은 `STUDENTS.DEPARTMENT`가 `DEPARTMENTS.DEPARTMENT`를 참조하는 `STUDENTS_DEPARTMENTS_FK`와, `SUBJECTS.HAKBUN`이 `STUDENTS.HAKBUN`을 참조하는 `SUBJECTS_STUDENTS_FK`를 추가했다.

이 SQL은 함수 종속성 그 자체를 선언하는 문법이 아니라, 분석 결과로 나눈 테이블 사이 참조 무결성을 DB에 구현하는 단계다. **함수 종속성 분석 → 테이블 분해 → PK/FK DDL → JOIN으로 복원** 순서를 구분해야 한다.

## 04-16 Order/OrderProduct 후속 적용 경계

04-16에는 Order가 주문의 공통 정보와 주문 품목 목록을, OrderProduct가 개별 Product와 quantity를 표현했다. Service는 요청 품목마다 새 OrderProduct를 만들고 Order에 모아 저장했다. 이 구조는 주문 한 건과 여러 주문 품목을 분리한 관계형 설계의 후속 적용 사례로 볼 수 있다.

그러나 이 페이지에서는 FK owning side, `mappedBy`, cascade, orphan removal, 관계 Entity 생명주기를 다시 설명하지 않는다. 그 책임은 세션 10에서 고도화한 [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]]에 있다. 또한 04-16 원본의 “정규화 공부하기” 안내와 Order 코드가 있다고 해서, 그날 함수 종속성을 다시 분석해 Order schema를 도출했다고 단정하지 않는다.

## 입력 → 처리 → 결과

| 학습 단계 | 입력 | 처리 | 결과 |
|---|---|---|---|
| 03-20 분석 | 반복된 학생·학과·과목·성적 표 | 이상 현상과 함수 종속성 식별→1NF~3NF 판단 | 학생·학과·성적 관계 분해 근거 |
| 03-20 DB 구현 | 분해한 테이블 설계 | PK/FK DDL과 위반 INSERT·부모 DELETE 테스트 | 참조 무결성으로 잘못된 관계 차단 |
| 03-20 조회 복원 | 분리된 관계 | JOIN | 분해 전 업무 의미를 조회 결과로 재구성 |
| 04-16 후속 적용 | 주문자·주문 상태·여러 상품과 수량 | 별도 Order/OrderProduct Entity·Repository·Service 구성 | MySQL/JPA 애플리케이션의 주문 저장 모델 |

## 구현 완료 범위와 미확정 범위

- **Oracle 직접 확인:** 이상 현상, 함수 종속성, 1NF~3NF, 학생·학과·성적 분해, FK DDL, 위반 데이터 테스트가 확인된다.
- **03-30 전환 확인:** Spring Boot 프로젝트가 Oracle Driver 대신 MySQL Driver·Spring Data JPA를 사용하고 MySQL dialect를 설정했다.
- **04-16 후속 확인:** Order·OrderProduct Entity와 주문 생성 경로가 작성됐다.
- **단정하지 않는 범위:** 04-16 Order 구조를 특정 함수 종속성 분석 결과로 도출했다는 기록, 프로젝트 전체 schema가 정규형을 모두 만족한다는 검증, DB 모델링과 JPA runtime 성공의 일괄 완료는 원본에서 확인되지 않는다.

## 자주 헷갈리는 원인

- **결정자를 PK로만 봄:** 후보키가 아닌 속성도 다른 속성을 결정할 수 있다.
- **종속 속성을 FK로 봄:** Y가 다른 테이블을 참조한다는 뜻이 아니라 X가 정해질 때 Y가 하나로 정해진다는 뜻이다.
- **분해와 FK를 같은 단계로 봄:** 분해는 설계 판단이고 FK는 그 결과의 참조를 DB에 구현하는 제약조건이다.
- **FK와 JOIN을 같은 기능으로 봄:** FK는 잘못된 저장을 막고 JOIN은 분리된 데이터를 조회한다.
- **정규화와 JPA mapping을 같은 작업으로 봄:** 전자는 관계형 설계 원리, 후자는 그 관계를 Java Entity에 표현하는 애플리케이션 mapping이다.
- **Order 관계 코드가 곧 정규화 증명이라고 봄:** 후속 적용 사례일 뿐, 04-16에 함수 종속성 분석을 다시 수행한 근거는 없다.

## 이전·후속 학습 연결

- 전체 모델링 흐름과 이상 현상→분해→FK→JOIN은 [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]가 맡는다.
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성]]은 PK/FK와 삭제 규칙, [[concepts/oracle-join|Oracle JOIN]]은 분리된 정보의 조회 복원을 맡는다.
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]에서 행 식별과 테이블 참조를 비교한다.
- 4과목의 Entity 관계 표현은 [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]], 주문 업무 생명주기는 [[concepts/order-flow|주문 기능 흐름]]으로 이어진다.

## 직접 수업·교안·후속 과목 경계

- **직접 수업:** 함수 종속성·정규화·테이블 분해·PK/FK 구현은 03-20 Oracle 범위다.
- **교안 보충:** DBeaver 교안 p.24~43의 정규화 예시는 기존 Oracle 고도화에서 직접 확인한 근거를 유지한다.
- **FrontEnd_BackEnd 후속:** R01은 MySQL/JPA 환경 전환, R14는 Order/OrderProduct 적용 사례다. Oracle 직접 학습으로 소급하지 않는다.
- **더 뒤의 경계:** Linux·AWS·CI/CD는 실행·배포, Passwordless는 인증, 중간 프로젝트는 실제 설계 적용 범위다. 어느 것도 03-20 정규화 직접 수업이 아니다.

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.24~43 정규화 예제
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md` — Oracle 직접 수업 이후 MySQL/JPA 환경 전환
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md` — Order/OrderProduct 후속 적용 사례
