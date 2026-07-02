---
title: 데이터 모델링과 정규화
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
status: growing
confidence: high
---
# 데이터 모델링과 정규화

## 정의

**데이터 모델링(data modeling)**은 사용자의 요구사항을 분석해 어떤 데이터가 필요하고 그 데이터들이 어떤 관계를 가지는지 문서화·설계하는 과정이다. **정규화(normalization)**는 입력, 수정, 삭제 이상 현상을 줄이기 위해 테이블을 적절한 단위로 나누는 과정이다.

## 왜 중요한가

DB 테이블을 잘못 설계하면 이후 Java/Spring 프로젝트 전체가 복잡해진다. 회원, 주문, 상품, 주문상세를 왜 나누는지 설명할 수 있어야 한다.

## ERD와 모델링 흐름

ERD(Entity-Relationship Diagram)는 개체-관계 모델을 시각적으로 표현한 도표다.

```text
현실세계 → 문서 → 설계 → 구현 → Database화
```

현실의 업무를 바로 테이블로 만드는 것이 아니라, 요구사항을 분석하고 문서화한 뒤 ERD 같은 설계도를 거쳐 DB로 구현한다.

## 분리된 하위 주제

- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]] — 이상 현상, 함수 종속성, 복합 기본키, 참조 무결성
- [[concepts/database-view-index|Database View와 Index]] — 가상 테이블과 조회 성능 보조 구조

## 자주 헷갈리는 점

- 정규화는 무조건 테이블을 많이 쪼개는 것이 아니라 중복과 이상 현상을 줄이기 위한 설계 과정이다.
- PK와 FK는 정규화 이후 나뉜 테이블을 연결하는 고리다.
- `ON DELETE` 옵션은 기술 문법이 아니라 업무 규칙 선택이다.
- View는 실제 데이터를 저장한 테이블이 아니라 SELECT 결과를 이름 붙여 재사용하는 가상 테이블이다.

## 관련 페이지

- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-referential-integrity|Oracle 참조 무결성과 ON DELETE]]
- [[concepts/database-normalization-functional-dependency|함수 종속성과 정규화]]
- [[concepts/database-view-index|Database View와 Index]]

## 출처

- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
