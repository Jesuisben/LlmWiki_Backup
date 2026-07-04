---
title: Python 객체지향 기본
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [python]
sources:
  - raw/Study/10. Python/2026.06.25(목)/2026.06.25(목).md
status: growing
confidence: high
---

# Python 객체지향 기본

## 정의

Python 객체지향 기본은 `class`, `__init__`, `self`, 인스턴스 변수, 클래스 변수, 메서드, 상속, 포함 관계를 이용해 객체와 동작을 묶는 방식이다.

## 왜 중요한가

Pandas와 데이터 분석 실습은 이 기초 위에서 진행된다. 사용자가 Java, Oracle, Spring/React를 먼저 배웠기 때문에 Python 개념은 기존의 자료형, 컬렉션, 객체지향, 파일 처리, SQL 테이블 감각과 연결해 이해하는 것이 좋다.

## 핵심 설명

Python 생성자는 `__init__`이고, `self`는 Java의 `this`와 비슷하다. `class Employee(Person)`으로 상속하고 `super().__init__()`으로 부모 초기화를 호출한다. 클래스 변수는 `Account.bankname`처럼 객체 없이 접근할 수 있다.

## 예시

`Account`, `Circle`, `Person`/`Employee`/`Student`, `Bag`/`Dosirak`, `Sales`/`Fruit` 실습으로 상속과 Has-A 관계를 익혔다.

## 자주 헷갈리는 점

- Python은 타입을 변수 선언에 적지 않고 값에 따라 결정한다.
- 짧은 문법일수록 결과 타입이 무엇인지 확인하는 습관이 필요하다.
- 순수 Python 자료구조와 Pandas DataFrame은 목적은 비슷해도 동작 방식과 제공 함수가 다르다.

## 관련 개념

- [[summaries/2026-06-25-python-standard-library-oop|2026-06-25 Python 표준 라이브러리와 객체지향]], [[concepts/java-class-object|Java 클래스와 객체]], [[concepts/java-inheritance|Java 상속]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 출처

- `raw/Study/10. Python/2026.06.25(목)/2026.06.25(목).md`
