---
title: 2026-07-07 Python 웹 크롤링, 지오코딩, 시각화
created: 2026-07-13
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: needs-review
confidence: medium
---

# 2026-07-07 Python 웹 크롤링, 지오코딩, 시각화

## 한 줄 요약

자전거 일별 분석을 마무리한 뒤 Selenium으로 동적 화면을 만들고 BeautifulSoup·HTTP 요청으로 매장 정보를 파싱하며, 지오코딩·Pandas·Folium·matplotlib/Seaborn/Plotly로 수집 데이터를 표현하는 code를 작성했다.

## 왜 이 순서로 배웠는가

전날의 공공 API는 구조화된 JSON을 직접 받았다. 이날은 같은 DataFrame 전처리·결합 기술을 웹 화면과 주소 데이터에 적용하면서, “브라우저 동작 → HTML → 행 데이터 → 좌표 → 지도·chart”로 수집 pipeline을 확장했다. 다음 날의 텍스트 마이닝은 외부 데이터를 구조화하는 관점을 문자열 token으로 옮긴다.

## 전체 학습 순서

1. 일별 자전거 CSV의 columns·문자열·결측치를 정리했다.
2. 성별·연령·대여구분별 평균 이동거리와 자치구별 최대 대여건수를 집계했다.
3. Selenium 설치 명령과 BeautifulSoup/Selenium의 역할 차이를 배웠다.
4. 브라우저에서 지역을 클릭한 뒤 `page_source`를 BeautifulSoup으로 파싱하는 code를 작성했다.
5. 주소만 있는 매장은 지오코딩 API로 위도·경도를 보완했다.
6. 세 브랜드 DataFrame을 결합하고 결측 좌표를 걸러 지도·heatmap·cluster·여러 chart를 만들었다.

## 대표 입력 → 처리 → 결과

### 동적 페이지 수집

- 입력: 매장 찾기 웹 화면
- 처리: WebDriver 시작 → URL 이동 → CSS selector 클릭·대기 → `page_source` 확보 → 태그·속성 파싱
- DataFrame 결과: 브랜드·상호·주소·구·위도·경도 columns를 가진 행 목록

Selenium 설치는 명령과 IDE 절차만 기록되어 있고 설치 성공 출력은 없다. 브라우저 객체 type 확인·매장 수 출력 code가 있으나 실제 output은 보존되지 않았다.

### 지오코딩과 오류 수정

주소 API 호출 code에는 권한 비활성화로 인한 403 오류와 주소별 `None` 후보가 기록되어 있다. 이후 제품 설정 활성화와 주소 단순화·재요청·DataFrame 좌표 보정 흐름을 작성했다. 그러나 보존된 원본에는 최종 재실행 output이 없고, 이디야 DataFrame 생성 시 앞에서 정의되지 않은 변수명이 사용된 후보도 있어 최종 수집 성공은 미확정이다.

### 시각화

결합 DataFrame을 이용해 Folium Marker·HeatMap·MarkerCluster, Plotly 지도, pie/bar/count/scatter plot code를 작성했다. 여러 `save()` 호출이 있지만 날짜 raw에는 HTML·PNG·CSV·notebook 물리 artifact가 없다. 또한 같은 PNG 이름을 두 그래프가 재사용하는 구간이 있어 실행했다면 앞 결과를 덮어쓸 수 있다.

## code·output·artifact 경계

- 실제 Traceback은 없지만 403 오류 text와 수정 절차가 있다.
- URL 이동·click·request·CSV/HTML/PNG 저장은 code 또는 출력용 문자열로 존재한다.
- `starbucks.html`, 매장 CSV, 지도 HTML, chart PNG는 raw에 없다.
- 좌표 결측을 제거한 `mapFrame`이 있는데 cluster 구간은 원본 `coffeeFrame`을 순회해 결측 좌표가 다시 들어갈 수 있다.
- 따라서 수업 pipeline과 오류 원인은 확인되지만 end-to-end 재현·최종 artifact 성공은 `needs-review`다.

## 헷갈린 점 / 질문

- Selenium은 클릭·대기 등 동적 상태를 만들고, BeautifulSoup은 확보한 HTML을 파싱한다. 둘은 대체재가 아니라 조합될 수 있다.
- API 200은 주소 document가 반드시 존재한다는 뜻이 아니므로 빈 documents를 별도로 처리해야 한다.
- 결측치 제거 후에는 이후 모든 지도 code가 정제된 DataFrame을 사용하는지 확인해야 한다.
- `save` 호출과 물리 파일 존재, browser에서 정상 표시되는 것은 각각 다른 완료 조건이다.

## 관련 페이지

- [[comparisons/beautifulsoup-vs-selenium|BeautifulSoup vs Selenium]]
- [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]
- [[concepts/pandas-dataframe-reshape-merge|Pandas DataFrame 결합과 재구조화]]
- [[entities/selenium|Selenium]]
- [[entities/folium|Folium]]
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 Python 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-08-python-korean-text-mining|2026-07-08 Python 한국어 텍스트 마이닝]]

## 출처

- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
