---
title: 2026-06-19 Python 설치와 기본 문법 입문
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md
status: growing
confidence: high
---

# 2026-06-19 Python 설치와 기본 문법 입문

## 한 줄 요약

Python 3.11.9와 PyCharm을 설치하고 `print`, 문자열, 형변환, 입력, 연산자, 문자열 함수, 인덱싱/슬라이싱을 통해 Pandas 이전 기본 문법 토대를 만들었다.

## 배운 내용

Python/PyCharm 설치와 인터프리터 연결, `pip` 경로, `print()`의 `sep`/`end`, 이스케이프 문자, `%` 포맷팅과 `format()`, `input()` 반환값의 문자열 성격, `int()`/`float()` 형변환, 조건 표현식, 산술·관계·논리 연산자, 문자열 함수, 인덱싱/슬라이싱을 다뤘다.

## 핵심 개념

- [[entities/python|Python]]
- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 실습 / 예제

대표 흐름은 입력 → 형변환 → 계산 → 출력이다. `input()`으로 받은 점수를 숫자로 바꿔 총점과 평균을 계산하고, 문자열 실습에서는 `strip`, `split`, `join`, `find`, `replace`, `startswith`, `endswith`, `ord`를 사용했다.

## 헷갈린 점 / 질문

`input()`은 숫자를 입력해도 문자열을 반환한다. 문자열과 숫자는 `+`로 바로 연결할 수 없으므로 `str()` 변환이 필요하다. Java의 `(int)3.14`와 달리 Python은 `int(3.14)`처럼 타입 이름을 함수처럼 쓴다.

## 관련 페이지

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md`
