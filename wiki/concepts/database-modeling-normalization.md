---
title: 데이터 모델링과 정규화
created: 2026-07-02
updated: 2026-07-22
type: concept
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
status: growing
confidence: high
---

# 데이터 모델링과 정규화

## 정의

데이터 모델링은 사용자의 요구사항을 분석해 어떤 데이터가 필요하고 서로 어떤 관계를 가지는지 문서화·설계하는 과정이다. 정규화는 입력·수정·삭제 이상 현상을 줄이기 위해 테이블을 적절한 단위로 분해하는 과정이다.

## 흐름

**모델링 흐름:** 현실세계 → 문서 → 설계 → 구현 → Database화

ERD(Entity-Relationship Diagram)는 엔티티, 속성, 관계를 시각적으로 표현하는 설계도다. DBeaver의 엔티티 관계도는 실제 테이블 사이 FK 관계를 눈으로 확인하게 해준다.

## 왜 중요한가

Spring/React 프로젝트에서 회원, 상품, 주문, 주문상세를 한 테이블에 몰아넣으면 중복과 이상 현상이 커진다. Oracle 수업의 핵심은 왜 테이블을 쪼개고, 어떤 FK와 ON DELETE 옵션을 선택했는가를 설명할 수 있게 되는 것이다.

여기서 Spring/React는 **후속 확장 관점**이다. 03-20 Oracle 직접 수업에서는 학생·학과·과목 데이터를 보고 ERD, 이상 현상, 함수 종속성, 정규화, DDL/FK를 연결했다. Entity 매핑이나 Repository 구현은 이 날의 실습 범위가 아니다.

## 이상 현상

- 삽입 이상: 신설 학과를 넣으려는데 학생 정보까지 필요함
- 갱신 이상: 주민번호 같은 중복 정보 일부만 수정됨
- 삭제 이상: 학생 삭제 시 학과 정보까지 사라짐

## 수업에서 등장한 맥락과 03-20 실제 학습 흐름

1. 한 표에 반복된 학생·학과·과목 정보를 보고 삽입/갱신/삭제 이상을 찾았다.
2. `학생번호 → 이름/주소/학과`, `학과 → 사무실`, `{학번, 과목코드} → 성적` 같은 결정 관계를 표시했다.
3. 학생·학과·수강/과목 역할로 테이블을 분리하고 복합 PK가 필요한 관계를 확인했다.
4. DBeaver ERD와 DDL로 `STUDENTS`, `DEPARTMENTS`, `SUBJECTS` 관계를 구현했다.
5. 부모가 없는 FK 입력과 자식이 남은 부모 삭제를 실행해 모델이 실제 데이터를 어떻게 제한하는지 확인했다.

### 정규형별 역할

- 1NF: 한 칸의 값을 원자값으로 정리하고 학생 성적 관계의 복합키 `{학번, 과목 코드}`를 확인했다.
- 2NF: 복합키 일부인 학번만으로 결정되는 학생 속성을 성적 관계에서 분리해 부분 함수 종속을 제거했다.
- 3NF: `학생번호 → 학과 → 대학/사무실`처럼 키가 아닌 속성을 거치는 이행적 종속을 학과 테이블로 분리했다.
- 분해 후에는 FK로 잘못된 참조를 막고 JOIN으로 원래 의미를 복원한다.

```sql
ALTER TABLE GOMDORI.STUDENTS
ADD CONSTRAINT STUDENTS_DEPARTMENTS_FK
FOREIGN KEY (DEPARTMENT)
REFERENCES GOMDORI.DEPARTMENTS(DEPARTMENT);
```

## 자주 틀리는 이해

- 정규화는 테이블 수를 늘리는 행위 자체가 목적이 아니다. 중복과 이상을 줄이되 필요한 정보는 JOIN으로 다시 구성할 수 있어야 한다.
- `X → Y`는 X가 반드시 PK이고 Y가 반드시 FK라는 뜻이 아니다. X 값 하나가 Y 값을 하나로 결정한다는 뜻이다.
- 컬럼 이름이 다른 테이블에도 있다고 자동으로 FK가 되는 것은 아니다. 실제 `FOREIGN KEY ... REFERENCES ...` 제약조건이 있어야 DB가 참조를 검사한다.
- No Action FK는 부모 삭제 후 자식을 남기는 옵션이 아니다. 자식이 남아 있으면 부모 삭제 자체를 막는 기본 제한 동작이다.

## 관련 페이지

- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]
- [[concepts/database-view-index|Database View와 Index]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]
- [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.2~4, p.24~43
