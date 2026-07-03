---
title: 2026-03-20 데이터 모델링, 정규화, View, Index
created: 2026-06-30
updated: 2026-07-02
type: summary
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/Study/2. Oracle/교육 자료/오라클 교안.pdf
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

## 헷갈린 점 / 질문

- 정규화는 무조건 테이블을 많이 쪼개는 것이 아니라 중복과 이상 현상을 줄이기 위한 설계 과정이다.
- 복합 PK는 두 컬럼이 합쳐져야 한 행을 식별할 수 있는 경우에 생긴다.
- View는 데이터를 복사해 저장한 테이블이 아니라 SELECT 결과를 이름 붙여 보여주는 가상 테이블이다.
- `user_views` 같은 데이터 사전은 객체 이름을 대문자로 관리하므로 조건 검색 시 `'VIEW01'`처럼 대문자를 써야 한다.

## 관련 페이지

- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]
- [[concepts/database-view-index|Database View와 Index]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]

## 출처

- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.2~4 데이터 모델링, p.24~43 정규화 예제
- `raw/Study/2. Oracle/교육 자료/오라클 교안.pdf` — p.446~448 View
