---
title: Python 파일·정규표현식 데이터 처리
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [python]
sources:
  - raw/Study/10. Python/2026.06.26(금)/2026.06.26(금).md
  - raw/Study/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# Python 파일·정규표현식 데이터 처리

## 정의

Python 파일·정규표현식 데이터 처리는 텍스트 파일을 읽고 쓰며 문자열을 규칙에 따라 분리·검증·추출하는 작업이다.

## 왜 중요한가

Pandas와 데이터 분석 실습은 이 기초 위에서 진행된다. 사용자가 Java, Oracle, Spring/React를 먼저 배웠기 때문에 Python 개념은 기존의 자료형, 컬렉션, 객체지향, 파일 처리, SQL 테이블 감각과 연결해 이해하는 것이 좋다.

## 핵심 설명

`open`, `with`, `readline`, `readlines`, `read`, `write`, `strip`, `split`, `re.compile`, `match`, `search`, `findall`, `finditer`, XML `parse`, JSON `loads`를 이용한다. 이는 Pandas `read_csv()` 이전에 순수 Python으로 데이터 처리 구조를 직접 이해하는 단계다.

## 예시

성적 텍스트를 읽어 결과 파일을 만들고, 커피 판매 파일에 할인율을 적용하고, 이메일/주소/파일명 패턴을 정규표현식으로 추출하고, XML/JSON을 list/tuple로 바꿨다.

## 자주 헷갈리는 점

- Python은 타입을 변수 선언에 적지 않고 값에 따라 결정한다.
- 짧은 문법일수록 결과 타입이 무엇인지 확인하는 습관이 필요하다.
- 순수 Python 자료구조와 Pandas DataFrame은 목적은 비슷해도 동작 방식과 제공 함수가 다르다.

## 관련 개념

- [[summaries/2026-06-26-python-exception-file-regex|2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식]], [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 출처

- `raw/Study/10. Python/2026.06.26(금)/2026.06.26(금).md`
- `raw/Study/10. Python/2026.06.29(월)/2026.06.29(월).md`
