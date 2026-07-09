---
title: Python 컬렉션과 컴프리헨션
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md
  - raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md
status: growing
confidence: high
---

# Python 컬렉션과 컴프리헨션

## 정의

Python 컬렉션은 여러 값을 묶어 다루는 자료구조이며, comprehension은 반복과 조건으로 새 컬렉션을 짧게 만드는 문법이다.

## 왜 중요한가

Pandas와 데이터 분석 실습은 이 기초 위에서 진행된다. 사용자가 Java, Oracle, Spring/React를 먼저 배웠기 때문에 Python 개념은 기존의 자료형, 컬렉션, 객체지향, 파일 처리, SQL 테이블 감각과 연결해 이해하는 것이 좋다.

## 핵심 설명

`list`는 수정 가능한 순서형, `tuple`은 수정 불가능한 순서형, `dict`는 key-value 구조, `set`은 중복 없는 집합이다. 중첩 리스트는 표 데이터의 행처럼 쓰이고 dict는 가격표·할인율·JSON 데이터와 연결된다.

## 예시

커피 메뉴 리스트, 빵 가격 dict, 학생 중첩 리스트, 점수 필터링 comprehension, `zip` 결과를 dict로 바꾸는 실습이 대표 예시다.

## 자주 헷갈리는 점

- Python은 타입을 변수 선언에 적지 않고 값에 따라 결정한다.
- 짧은 문법일수록 결과 타입이 무엇인지 확인하는 습관이 필요하다.
- 순수 Python 자료구조와 Pandas DataFrame은 목적은 비슷해도 동작 방식과 제공 함수가 다르다.

## 관련 개념

- [[summaries/2026-06-22-python-control-flow-collections|2026-06-22 Python 제어문과 컬렉션]], [[summaries/2026-06-23-python-dict-comprehension-builtins|2026-06-23 Python dict, comprehension, 내장 함수]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md`
- `raw/KoreaICT/10. Python/2026.06.23(화)/2026.06.23(화).md`
