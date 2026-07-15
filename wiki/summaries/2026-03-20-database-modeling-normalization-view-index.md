---
title: 2026-03-20 데이터 모델링, 정규화, View, Index
created: 2026-06-30
updated: 2026-07-15
type: summary
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-1.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-2.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-3.sql
  - raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-4.sql
status: growing
confidence: high
---

# 2026-03-20 데이터 모델링, 정규화, View, Index

## 한 줄 요약

ERD와 데이터 모델링으로 “왜 테이블을 나누는가”를 배우고, 정규화·함수 종속성·View 권한·Index까지 DB 설계와 관리 관점으로 확장한 날이다.

## 배운 내용

- ERD는 엔티티, 속성, 관계를 시각적으로 표현한 DB 설계도다.
- 데이터 모델링은 요구사항을 분석해 현실세계를 문서·설계·구현·Database로 옮기는 과정이다.
- 이상 현상에는 삽입 이상, 갱신 이상, 삭제 이상이 있다.
- 정규화는 이상 현상을 줄이기 위해 테이블을 더 적절한 단위로 분해하는 과정이다.
- 함수 종속성과 이행적 함수 종속을 통해 어떤 컬럼이 어떤 컬럼을 결정하는지 분석했다.
- `gomdori`, `bluesky` 사용자를 만들어 정규화 예제 테이블과 FK를 실습했다.
- View는 물리 테이블 일부를 보여주는 가상 테이블이며, `GRANT`/`REVOKE`로 조회 권한을 제어했다.
- Index는 책의 목차처럼 검색을 돕고, PK/UNIQUE 생성 시 내부적으로 만들어질 수 있다.

### 1NF → 2NF → 3NF

| 단계 | 수업 예제에서 확인한 판단 |
|---|---|
| 제1정규형(1NF) | 한 칸에 여러 값을 넣지 않고 행·컬럼 값을 원자값으로 정리한다. 학생 성적 행은 `{학번, 과목 코드}` 조합으로 식별했다. |
| 제2정규형(2NF) | 복합키 일부인 학번만으로 결정되는 학생 이름·주민번호·학과를 성적 관계에서 분리해 부분 함수 종속을 제거한다. |
| 제3정규형(3NF) | `학생번호 → 학과 → 대학/사무실`처럼 키가 아닌 속성을 거쳐 결정되는 정보를 학과 테이블로 분리해 이행적 함수 종속을 줄인다. |

분해 뒤에도 학생·학과·성적의 원래 의미를 JOIN으로 복원할 수 있어야 한다. 정규화는 표를 많이 만드는 작업이 아니라 **이상 현상을 줄이면서 관계를 보존하는 설계**다.

## 왜 이 순서로 배웠나

03-19까지는 이미 만들어진 테이블을 잘 조회하는 방법을 배웠다. 마지막 날에는 질문을 거꾸로 돌려 “처음부터 어떤 테이블과 관계를 만들면 중복·수정·삭제 문제가 줄어드는가”를 ERD와 정규화로 다뤘다. 정규화한 `STUDENTS`·`DEPARTMENTS`·`SUBJECTS`를 DDL과 FK로 구현하고 무결성 오류를 확인한 뒤, 필요한 데이터만 공개하는 View와 조회를 돕는 Index로 객체 학습을 마무리했다.

## 실습 / 예제

```sql
ALTER TABLE GOMDORI.STUDENTS
ADD CONSTRAINT STUDENTS_DEPARTMENTS_FK FOREIGN KEY (DEPARTMENT)
REFERENCES GOMDORI.DEPARTMENTS(DEPARTMENT);

ALTER TABLE GOMDORI.SUBJECTS
ADD CONSTRAINT SUBJECTS_STUDENTS_FK FOREIGN KEY (HAKBUN)
REFERENCES GOMDORI.STUDENTS(HAKBUN);
```

```sql
GRANT CREATE VIEW TO oraman;

CREATE OR REPLACE VIEW view01
AS
SELECT name, password, gender
FROM MEMBERS
WHERE gender = '남자';

GRANT SELECT ON view01 TO gomdori;
SELECT * FROM oraman.view01;
REVOKE SELECT ON view01 FROM gomdori;
```

View 실습은 사용자 역할별로 이어졌다.

1. 관리자 연결이 `oraman`에게 `CREATE VIEW` 권한을 부여했다.
2. `oraman`이 `view01`과 JOIN 기반 `view02`를 만들고 `gomdori`에게 객체 조회 권한을 부여했다.
3. `gomdori` 연결이 `oraman.view01`, `oraman.view02`처럼 소유자 schema를 붙여 조회했다.
4. `oraman`이 `REVOKE` 후 접근 오류를 확인하고 View를 삭제했다.

## 헷갈린 점 / 질문

- 정규화는 무조건 테이블을 많이 쪼개는 것이 아니라 중복과 이상 현상을 줄이기 위한 설계 과정이다.
- 복합 PK는 두 컬럼이 합쳐져야 한 행을 식별할 수 있는 경우에 생긴다.
- View는 데이터를 복사해 저장한 테이블이 아니라 SELECT 결과를 이름 붙여 보여주는 가상 테이블이다.
- `user_views` 같은 데이터 사전은 객체 이름을 대문자로 관리하므로 조건 검색 시 `'VIEW01'`처럼 대문자를 써야 한다.
- 원본의 “X는 기본키, Y는 외래키” 메모는 함수 종속성의 정의가 아니다. `X → Y`는 **X 값이 정해지면 Y 값이 하나로 결정된다**는 뜻이며, X가 반드시 PK이거나 Y가 반드시 FK인 것은 아니다.
- 원본 표의 `이름`, `주소`, `학과`를 모두 외래키라고 적은 부분도 일반 정의로 받아들이면 안 된다. FK 여부는 다른 테이블의 PK/UNIQUE를 실제로 참조하도록 제약조건을 만들었는지로 판단한다.
- 수업 View 예제는 `password` 컬럼을 포함했지만, 실제 서비스에서는 인증 비밀값을 조회용 View에 노출하지 않는 설계가 필요하다. 이는 원본 실습과 운영 보안 관점을 구분한 보충 설명이다.
- `SUBJECTS_STUDENTS_FK`에 삭제 옵션을 쓰지 않은 No Action 상태에서는 자식 성적 행이 남아 있으면 부모 학생 삭제가 막힌다. “학생을 지워도 과목 내역이 남는다”는 뜻이 아니다.

## 이전·다음 흐름

- 이전: 03-19의 JOIN은 분리된 테이블에서 의미를 다시 조합하는 조회 방법이었다.
- 다음: UI&UX 과목에서는 화면 입력·표시를 배우고, 이후 Spring/JPA에서 Entity·Repository가 이 관계형 구조를 애플리케이션 객체와 연결한다. 이 후속 연결은 Oracle 직접 실습과 구분한다.

## 관련 페이지

- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]
- [[concepts/database-view-index|Database View와 Index]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.2~4 데이터 모델링, p.24~43 정규화 예제
- `raw/KoreaICT/2. Oracle/교육 자료/오라클 교안.pdf` — p.446~448 View
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-1.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-2.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-3.sql`
- `raw/KoreaICT/2. Oracle/교육 자료/스크립트들/기타 스크립트/Script-4.sql`
