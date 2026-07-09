---
title: 2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# 2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치

## 한 줄 요약

정규표현식의 `match`/`search`/`findall`/`finditer`를 확장하고, XML·JSON 파일을 읽고 쓰며, `pip`, Pandas, matplotlib, Jupyter Notebook 설치·실행 흐름을 준비했다.

## 배운 내용

`match()`와 `search()` 차이, Match 객체의 `start/end/group/span`, `findall`, `finditer`, raw string, XML `Element/SubElement/ElementTree/parse`, JSON `loads`, `pip install/uninstall/list`, `pip install -r requirements.txt`, Jupyter 실행 명령을 다뤘다.

## 핵심 개념

- [[entities/python|Python]]
- [[concepts/python-basic-syntax|Python 기본 문법]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 실습 / 예제

주소 문자열에서 상세주소를 추출하고, 이메일의 아이디/도메인을 분리하고, XML 자동차 정보와 JSON 사람/커피 정보를 tuple/list로 변환했다.

## 헷갈린 점 / 질문

`^`와 `$`가 있으면 전체 시작/끝 조건이 강해진다. Pandas는 Python 기본 모듈이 아니라 `pip`로 설치하는 외부 라이브러리다.

## 관련 페이지

- [[entities/python|Python]]
- [[entities/pandas|Pandas]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[concepts/python-file-regex-data-processing|Python 파일·정규표현식 데이터 처리]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
