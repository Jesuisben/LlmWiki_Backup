---
title: 함수 종속성과 정규화
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
status: growing
confidence: high
---
# 함수 종속성과 정규화

## 이상 현상

이상 현상은 테이블 설계가 좋지 않을 때 입력/수정/삭제 과정에서 생기는 비정상적인 문제다.

| 이상 현상 | 의미 | 수업 예시 |
|---|---|---|
| 삽입 이상 | 어떤 데이터를 넣으려면 불필요한 다른 데이터까지 넣어야 함 | 신설 학과 등록 시 학생 정보까지 필요 |
| 갱신 이상 | 같은 정보가 여러 곳에 있어 일부만 수정되는 문제 | 주민번호 변경 시 중복 행 일부만 갱신 |
| 삭제 이상 | 지우면 안 되는 정보까지 같이 사라지는 문제 | 학생 삭제 시 학과 정보까지 사라짐 |

정규화는 이런 이상 현상을 줄이기 위해 테이블을 나누는 과정이다.

## 함수 종속성

함수 종속성은 어떤 속성 X를 알면 다른 속성 Y가 결정되는 관계다.

수업 예시는 다음과 같다.

- 주민번호를 알면 성별을 알 수 있다.
- 생년월일을 알면 나이를 알 수 있다.
- 학생번호를 알면 이름, 주소, 학과를 알 수 있다.
- 학과를 알면 사무실을 알 수 있다.

```text
학생번호 → 이름
학생번호 → 주소
학생번호 → 학과
학과 → 사무실
```

이런 관계를 분석하면 어떤 컬럼을 어떤 테이블로 분리해야 할지 판단할 수 있다.

## 이행적 함수 종속

이행적 함수 종속은 `A → B`, `B → C`이면 `A → C`도 성립하는 관계다.

수업 예시는 다음과 같다.

```text
아이디 → 등급
등급 → 할인율
따라서 아이디 → 할인율
```

이런 구조에서는 할인율을 회원 테이블에 직접 반복 저장하기보다, 등급 테이블로 분리하는 식의 정규화가 필요할 수 있다.

## 제1정규형과 복합 기본키

수업에서는 학생 성적 테이블 예시를 다뤘다.

```text
학번 + 과목 코드 → 성적
```

성적을 알기 위해서는 “누가 들었는가(학번)”와 “어떤 과목인가(과목 코드)”가 함께 필요하다. 그래서 `{학번, 과목 코드}`가 복합 기본키가 된다.

이때 학번은 학생 테이블을 참조하는 외래키가 될 수 있다. 존재하지 않는 학생이 수강 신청하는 오류를 막기 위해 참조 무결성이 필요하다.

## 정규화와 참조 무결성

정규화를 하면 테이블이 여러 개로 나뉜다. 그러면 테이블 사이 연결을 지키기 위해 기본키와 외래키가 필요하다.

수업에서는 다음 예시를 만들었다.

- `DEPARTMENTS`: 학과
- `STUDENTS`: 학생
- `SUBJECTS`: 과목 성적

```sql
ALTER TABLE GOMDORI.STUDENTS
ADD CONSTRAINT STUDENTS_DEPARTMENTS_FK
FOREIGN KEY (DEPARTMENT)
REFERENCES GOMDORI.DEPARTMENTS(DEPARTMENT);
```

```sql
ALTER TABLE GOMDORI.SUBJECTS
ADD CONSTRAINT SUBJECTS_STUDENTS_FK
FOREIGN KEY (HAKBUN)
REFERENCES GOMDORI.STUDENTS(HAKBUN);
```

이후 다음 테스트를 했다.

```sql
-- 존재하지 않는 학생
insert into subjects values(9044555, 'ABC01', 'B');

-- 존재하지 않는 학과 정보 추가
insert into students values(9021777, '김철수', '701223-1111111', '전산과');

-- 자식 테이블에 데이터가 존재하므로 삭제 불가능
delete from departments where department = '가정 의학';
```

이 테스트들은 참조 무결성이 실제로 잘 작동하는지 확인하는 과정이다.

## ON DELETE 옵션을 설계 관점에서 생각하기

수업에서 중요한 문장:

> 나중에 프로젝트를 할 때 왜 테이블을 이렇게 만들었는지 / on delete를 이런 옵션으로 했는지를 계속 생각해야 함.

예를 들어 쇼핑몰에서는 다음처럼 판단할 수 있다.

| 관계 | 가능한 선택 | 이유 |
|---|---|---|
| 회원 → 주문 | `ON DELETE SET NULL` | 회원 탈퇴 후에도 주문 기록은 남길 수 있음 |
| 주문 → 주문상세 | `ON DELETE CASCADE` | 주문이 취소되면 상세도 같이 삭제되어야 자연스러움 |
| 상품 → 주문상세 | `ON DELETE SET NULL` | 상품이 삭제되어도 과거 주문 기록은 남길 수 있음 |

정규화는 단순히 테이블을 쪼개는 것이 아니라, 삭제/수정/조회 시 업무 의미가 유지되도록 설계하는 것이다.

## 관련 페이지

- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]

## 출처

- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
