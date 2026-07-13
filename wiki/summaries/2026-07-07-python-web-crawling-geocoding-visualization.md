---
title: 2026-07-07 Python 웹 크롤링, 지오코딩, 시각화
created: 2026-07-13
updated: 2026-07-13
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# 2026-07-07 Python 웹 크롤링, 지오코딩, 시각화

## 한 줄 요약
자전거 DataFrame 전처리·피벗 분석을 이어서 수행하고, Selenium·BeautifulSoup·지오코딩으로 커피 매장 데이터를 수집해 지도와 차트로 표현했다.

## 배운 내용
자전거 일별 데이터는 `rename`, 문자열 정규화, `dropna`, index 설정으로 전처리했다. 성별·연령·대여구분코드별 평균 이동거리는 `pivot_table`로 만들고, 자치구·대여구분코드별 대여건수는 `groupby` 후 정렬·중복 제거로 최대 항목을 찾았다.

## 실습 / 예제
Selenium WebDriver로 동적 매장 페이지를 열고 CSS selector 클릭 뒤 `page_source`를 BeautifulSoup으로 파싱했다. 주소만 있는 행은 지오코딩 API로 좌표를 보완했으며, 브랜드별 DataFrame은 `concat`으로 합쳤다. Folium의 Marker·HeatMap·MarkerCluster, Plotly 지도, Seaborn/Pandas 그래프로 위치·브랜드·구별 분포를 확인했다.

## 헷갈린 점 / 질문
- BeautifulSoup은 이미 받은 HTML 파싱에, Selenium은 클릭·대기처럼 브라우저 동작이 필요한 경우에 쓴다.
- 지오코딩 API 키도 `.env`로 분리하며, 주소 형식이 맞지 않으면 좌표가 없을 수 있으므로 결측 처리와 보정 절차가 필요하다.

## 관련 페이지
- [[comparisons/beautifulsoup-vs-selenium|BeautifulSoup vs Selenium]]
- [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]
- [[entities/selenium|Selenium]]
- [[entities/folium|Folium]]
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 한국어 텍스트 마이닝]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
