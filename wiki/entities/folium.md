---
title: Folium
created: 2026-07-13
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# Folium

## 무엇인가

Folium은 위도·경도 데이터로 HTML 기반 대화형 지도를 만드는 Python 라이브러리다.

## 이 위키에서의 맥락

2026-07-06 공공 자전거 실습에서 처음 등장하고 07-07 커피 매장 실습으로 확장됐다. 대여소·매장 DataFrame의 위도·경도를 Marker, MarkerCluster, GeoJSON 경계, HeatMap으로 표현하는 code에 사용했다.

## 날짜별 학습 이력

- 07-06: 자전거 대여소 중심 지도, GeoJSON 자치구 경계, 대여건수 color scale, MarkerCluster
- 07-07: 브랜드별 매장 marker, 전체 매장 heatmap·cluster, service 제공 매장 지도

## 입력과 artifact 경계

입력은 숫자형 위도·경도, marker label, 필요하면 GeoJSON 경계다. 지도 object를 만들고 `save()`를 호출하는 code는 있으나 날짜 raw에 생성 HTML이나 browser screenshot은 없다. 또한 07-07에서는 결측 좌표를 제거한 DataFrame과 원본 DataFrame이 후속 code에서 혼용된다. 그러므로 지도 설계는 확인되지만 최종 저장·표시 성공은 단정하지 않는다.

## 자주 헷갈리는 점

- Folium은 좌표를 수집하지 않는다. API·CSV·지오코딩에서 확보한 좌표를 표현한다.
- `NaN` 좌표는 marker·heatmap 생성 전에 제거하거나 보정해야 한다.
- 지도 object 생성, HTML 저장, browser rendering은 서로 다른 검증 단계다.
- GeoJSON의 지역명 key와 DataFrame의 자치구 이름이 맞아야 경계별 표현이 연결된다.

## 관련 개념
- [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 웹 크롤링·지오코딩·시각화]]
- [[entities/pandas|Pandas]]
- [[entities/matplotlib|matplotlib]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
