---
title: Python 함수, 모듈, 패키지
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# Python 함수, 모듈, 패키지

## 정의

함수는 재사용할 동작을 이름 붙인 코드 단위이고, 모듈은 Python 파일, 패키지는 관련 모듈을 묶은 폴더 구조다.

## 왜 중요한가

Pandas와 데이터 분석 실습은 이 기초 위에서 진행된다. 사용자가 Java, Oracle, Spring/React를 먼저 배웠기 때문에 Python 개념은 기존의 자료형, 컬렉션, 객체지향, 파일 처리, SQL 테이블 감각과 연결해 이해하는 것이 좋다.

## 핵심 설명

`def`, 기본 매개변수, 위치/키워드 인수, `*args`, `**kwargs`, `lambda`, `filter`, `map`, `import`, `from ... import ...`, `__name__ == "__main__"`를 배웠다. Python 함수는 Java와 달리 반환 타입과 매개변수 타입을 선언하지 않는다.

## 예시

랜덤 리스트 생성 함수, 성적 출력 함수, 문자열 분리/결합 모듈, `somefolder.mymath.MathModule` import 방식들이 대표 실습이다.

## 자주 헷갈리는 점

- Python은 타입을 변수 선언에 적지 않고 값에 따라 결정한다.
- 짧은 문법일수록 결과 타입이 무엇인지 확인하는 습관이 필요하다.
- 순수 Python 자료구조와 Pandas DataFrame은 목적은 비슷해도 동작 방식과 제공 함수가 다르다.

## 관련 개념

- [[summaries/2026-06-24-python-functions-modules|2026-06-24 Python 함수, 람다, 모듈·패키지]], [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md`
- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
