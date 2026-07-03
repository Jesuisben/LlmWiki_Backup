---
title: 데이터 모델링과 정규화
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

# 데이터 모델링과 정규화

## 정의

데이터 모델링은 사용자의 요구사항을 분석해 어떤 데이터가 필요하고 서로 어떤 관계를 가지는지 문서화·설계하는 과정이다. 정규화는 입력·수정·삭제 이상 현상을 줄이기 위해 테이블을 적절한 단위로 분해하는 과정이다.

## 흐름

```text
현실세계 → 문서 → 설계 → 구현 → Database화
```

ERD(Entity-Relationship Diagram)는 엔티티, 속성, 관계를 시각적으로 표현하는 설계도다. DBeaver의 엔티티 관계도는 실제 테이블 사이 FK 관계를 눈으로 확인하게 해준다.

## 왜 중요한가

Spring/React 프로젝트에서 회원, 상품, 주문, 주문상세를 한 테이블에 몰아넣으면 중복과 이상 현상이 커진다. Oracle 수업의 핵심은 왜 테이블을 쪼개고, 어떤 FK와 ON DELETE 옵션을 선택했는가를 설명할 수 있게 되는 것이다.

## 이상 현상

- 삽입 이상: 신설 학과를 넣으려는데 학생 정보까지 필요함
- 갱신 이상: 주민번호 같은 중복 정보 일부만 수정됨
- 삭제 이상: 학생 삭제 시 학과 정보까지 사라짐

## 관련 페이지

- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]
- [[concepts/database-view-index|Database View와 Index]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[comparisons/primary-key-vs-foreign-key|Primary Key vs Foreign Key]]
- [[comparisons/on-delete-set-null-vs-cascade|ON DELETE SET NULL vs CASCADE]]

## 출처

- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf` — p.2~4, p.24~43
