---
title: 2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md
status: growing
confidence: high
---

# 2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식

## 한 줄 요약

`try/except/else/finally`, `raise`, 파일 읽기/쓰기, 텍스트 데이터 변환, `re` 정규표현식 입문을 배우며 외부 데이터를 안전하게 처리하는 흐름에 들어갔다.

## 배운 내용

예외 처리 순서, `Exception`의 위치, `raise ValueError`, `open(file, mode, encoding)`, `read`, `readline`, `readlines`, `write`, `with`, 텍스트 파일의 줄 처리, `re.compile`, `match`, `^`, `$`, 문자 범위, 반복 횟수 `{n,m}`를 배웠다.

## 핵심 개념

- [[entities/python|Python]]
- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 실습 / 예제

`jumsu.txt`를 읽어 이름/성별/총점/평균 형식의 결과 파일을 만들고, `coffee.txt`를 읽어 할인율 사전과 기본 할인율을 적용한 결과 파일을 만들었다.

## 헷갈린 점 / 질문

`except Exception`은 구체 예외보다 아래에 둔다. `readlines()` 결과에는 줄바꿈이 남으므로 `strip()`을 함께 쓴다. 정규식에서 진짜 점은 `\.`로 쓴다.

## 관련 페이지

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md`
