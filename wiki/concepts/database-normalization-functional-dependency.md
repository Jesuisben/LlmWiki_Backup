---
title: 함수 종속성과 정규화
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
status: growing
confidence: high
---

# 함수 종속성과 정규화

## 정의

함수 종속성은 어떤 속성 X를 알면 다른 속성 Y가 결정되는 관계다. 정규화에서는 이 관계를 분석해 테이블을 어떻게 나눌지 판단한다.

## 수업 예시

```text
학생번호 → 이름
학생번호 → 주소
학생번호 → 학과
학과 → 사무실
```

`학생번호 → 학과`이고 `학과 → 사무실`이면 `학생번호 → 사무실`도 성립한다. 이것이 이행적 함수 종속이다.

## 이상 현상과 정규화

| 이상 현상 | 의미 | 수업 예시 |
|---|---|---|
| 삽입 이상 | 불필요한 데이터까지 넣어야 함 | 신설 학과 등록 시 학생 정보 필요 |
| 갱신 이상 | 중복 데이터 일부만 바뀜 | 주민번호 변경이 일부 행에만 반영 |
| 삭제 이상 | 보존할 정보까지 사라짐 | 학생 삭제 시 학과 정보도 사라짐 |

## 복합 기본키

학생 성적 예제에서는 성적을 알기 위해 “학번 + 과목 코드”가 함께 필요했다.

```text
학번 + 과목 코드 → 성적
```

그래서 `{학번, 과목 코드}`가 복합 기본키가 된다. 학번은 학생 테이블을 참조하는 외래키가 될 수 있다.

## 정규화 실습

```sql
ALTER TABLE GOMDORI.STUDENTS
ADD CONSTRAINT STUDENTS_DEPARTMENTS_FK FOREIGN KEY (DEPARTMENT)
REFERENCES GOMDORI.DEPARTMENTS(DEPARTMENT);

ALTER TABLE GOMDORI.SUBJECTS
ADD CONSTRAINT SUBJECTS_STUDENTS_FK FOREIGN KEY (HAKBUN)
REFERENCES GOMDORI.STUDENTS(HAKBUN);
```

## 관련 페이지

- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]

## 출처

- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.24~43 정규화 예제
