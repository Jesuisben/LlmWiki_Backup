---
title: 2026-07-06 Python 공공데이터 API와 자전거 분석
created: 2026-07-13
updated: 2026-07-13
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
status: growing
confidence: high
---

# 2026-07-06 Python 공공데이터 API와 자전거 분석

## 한 줄 요약
서울 열린데이터광장의 공공 자전거 데이터를 Open API·CSV로 수집하고, Pandas DataFrame의 결합·집계와 Folium 지도 시각화로 연결했다.

## 배운 내용
API URL은 인증키·응답 형식·서비스명·시작/끝 행 같은 요청 인자로 구성되고 JSON을 돌려준다. 실습에서는 `.env`에서 환경변수를 읽고 `requests.get()`으로 응답을 받은 뒤, 페이지 단위 행 목록을 모아 DataFrame과 CSV로 저장했다. 실제 키는 코드나 위키에 기록하지 않는다.

## 실습 / 예제
`itertools.count()`로 페이지 범위를 늘리고, 응답의 자전거 목록을 누적한 뒤 `pd.DataFrame(...).to_csv()`를 실행했다. 대여소 정보와 실시간 정보는 대여소 이름 index를 정규화한 뒤 `pd.merge(..., left_index=True, right_index=True, how='outer')`로 결합했다. 이후 자치구별 대여소·거치대 수를 `groupby`로 집계하고, GeoJSON·MarkerCluster로 지도에 표시했다.

## 헷갈린 점 / 질문
- API 키는 인증이 필요한 설정값이므로 `.env`로 분리하고 저장소에 넣지 않는다.
- `merge` 전에 문자열 공백·컬럼명·index 형태를 맞추지 않으면 같은 대여소도 다른 값으로 취급될 수 있다.

## 관련 페이지
- [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[entities/folium|Folium]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 웹 크롤링·지오코딩·시각화]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
