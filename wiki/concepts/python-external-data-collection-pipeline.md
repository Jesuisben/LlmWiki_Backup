---
title: Python 외부 데이터 수집 파이프라인
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# Python 외부 데이터 수집 파이프라인

## 정의
외부 API·웹 페이지에서 데이터를 가져와 DataFrame으로 바꾸고, 전처리·결합·집계·시각화까지 수행하는 Python 실습 흐름이다.

## 핵심 설명
서울 공공데이터 실습은 `.env` 환경변수 로드 → `requests.get()` → JSON 응답 → 페이지 반복 수집 → list → DataFrame → CSV 저장 순서다. 커피 매장 실습은 Selenium의 브라우저 동작과 BeautifulSoup HTML 파싱, 지오코딩으로 확보한 좌표를 DataFrame에 넣어 `concat`·Folium·그래프로 확장했다.

## 자주 헷갈리는 점
키·개인 환경 경로는 데이터가 아니라 설정값이다. 코드·CSV·위키에 실제 값을 넣지 않고 `.env`와 `.gitignore`로 분리한다. API JSON 구조·문자열 index·주소 형식이 맞지 않으면 수집 뒤에도 결합·좌표화가 실패할 수 있다.

## 관련 개념
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 웹 크롤링·지오코딩·시각화]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[comparisons/beautifulsoup-vs-selenium|BeautifulSoup vs Selenium]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
