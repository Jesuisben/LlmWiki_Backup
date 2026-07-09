---
title: 2026-06-25 Python 표준 라이브러리와 객체지향
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md
status: growing
confidence: high
---

# 2026-06-25 Python 표준 라이브러리와 객체지향

## 한 줄 요약

`os`, `random`, `datetime` 표준 라이브러리를 실습하고, Python 클래스의 `__init__`, `self`, 클래스 변수, 상속, Has-A를 Java 객체지향과 비교했다.

## 배운 내용

`os.path.isdir`, `os.mkdir`, `os.path.join`, Windows 경로 이스케이프, `random.seed/random/randint/choice/choices/shuffle/sample`, `datetime.now/strftime/strptime/timedelta/date/time/combine`, 클래스 변수, 인스턴스 변수, `super()`, 상속, 오버라이딩, Has-A 관계를 다뤘다.

## 핵심 개념

- [[entities/python|Python]]
- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 실습 / 예제

폴더 자동 생성, 로또 번호/조 편성 랜덤 추출, `Account`, `Circle`, `Person`-`Employee`/`Student`, `Bag`-`Dosirak` 포함 관계를 실습했다.

## 헷갈린 점 / 질문

`choices()`는 중복 허용, `sample()`은 중복 비허용이다. Python 생성자는 `__init__`이고, `self`는 직접 넘기지 않지만 메서드 정의에는 필요하다.

## 관련 페이지

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.25(목)/2026.06.25(목).md`
