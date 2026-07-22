---
title: 2026-07-06 Python 공공데이터 API와 자전거 분석
created: 2026-07-13
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md
  - raw/KoreaICT/10. Python/교육 자료/공공 데이터 이용/공공자전거 대여소 정보(25.12월 기준).csv
status: growing
confidence: medium
---

# 2026-07-06 Python 공공데이터 API와 자전거 분석

## 한 줄 요약

Open API의 요청 구조와 credential 분리를 배운 뒤, 공공 자전거의 정적 CSV·실시간 JSON·일별 JSON을 DataFrame으로 바꾸고 결합·집계·지도화하는 end-to-end code를 작성한 날이다.

## 왜 이 순서로 배웠는가

07-01~03에 익힌 CSV·`merge`·`groupby`·그래프를 실제 외부 데이터에 적용했다. 먼저 API 문서의 입력·출력·오류 구조를 읽고, 다음으로 데이터를 수집·저장한 뒤, 마지막으로 서로 다른 자전거 표를 같은 index와 columns로 맞춰 분석했다. 다음 날에는 일별 데이터 분석을 마무리하고 민간 웹·지오코딩으로 수집 경로를 확장한다.

## 전체 학습 순서

1. 서울 열린데이터광장의 인증 절차와 API URL 구성 요소를 읽었다.
2. 대여소 정보는 제공 파일을 정리한 CSV로 준비했다.
3. 실시간 대여 정보는 환경변수의 key를 URL에 조합해 page 단위 JSON을 요청하는 code를 작성했다.
4. 일별 이용 정보는 날짜·page 반복을 중첩해 JSON row를 누적하는 code로 확장했다.
5. 세 dataset을 DataFrame으로 읽고 이름·index·문자열을 정규화했다.
6. 자치구·운영방식·거치율·거치대 수를 집계하고 chart·Folium 지도 code로 표현했다.

## 대표 입력 → 처리 → 결과

### API 수집

- 입력: 환경변수에서 읽은 API credential, service명, 시작·끝 row, 조회 날짜
- 처리: `requests.get()` → JSON 변환 → row list 추출 → page 반복 → list 누적 → DataFrame 변환
- 의도한 결과: 실시간·일별 자전거 CSV 저장

노트에는 page 추출·CSV 저장 code가 있지만 실제 응답 dump, 생성된 `bikeList.csv`, 일별 CSV는 raw에 없다. 테스트용 page 강제 종료와 “더 이상 데이터가 없으면 예외로 종료” 방식도 있어 전체 수집 성공을 단정하지 않는다.

### 대여소 분석

- 입력: 물리적으로 존재하는 대여소 CSV와 code상 생성 대상인 실시간·일별 CSV
- 처리: columns rename, 문자열 공백 정규화, index 설정, `groupby`, `merge`, top-N 정렬
- 의도한 결과: 자치구별 대여소·거치대 chart, 운영방식 pie chart, GeoJSON 경계와 MarkerCluster 지도

보조 CSV는 CP949, 2,799 data row, 11 columns이며 row 폭은 일정하지만 빈 header column 1개가 있다. 이는 입력 dataset의 존재와 schema를 증명할 뿐, 노트의 모든 분석 cell 실행 성공을 증명하지 않는다.

## code·artifact 증거 경계

- `.env` 생성과 credential 사용법은 절차로 기록되어 있으나 실제 값은 위키에 보존하지 않는다.
- `requests.get`, `to_csv`, `mapObject.save` 호출은 작성된 code다.
- 날짜 raw에는 실제 response file, 생성 CSV, 지도 HTML, browser screenshot, 독립 notebook이 없다.
- 노트의 “파일이 저장되었습니다”는 실행 시 출력하도록 작성한 문자열이므로 물리 artifact가 없으면 저장 성공 증거로 사용하지 않는다.
- 07-06 노트 후반은 “이어서 작성”으로 남아 있어 분석 전체 완료본이 아니다.

## 헷갈린 점 / 질문

- API의 page 번호가 아니라 시작 row·끝 row 범위를 조합한다.
- credential 누락과 데이터 끝을 같은 broad `Exception`으로 처리하면 원인을 구분하기 어렵다.
- `merge` 전에 대여소 이름의 공백·점 표기를 맞추지 않으면 같은 대여소가 다른 key가 된다.
- `outer` merge는 양쪽 미매칭 행도 남기므로 `_merge`·결측치를 확인해야 한다.
- 지도 객체 생성과 HTML 파일 존재, browser 표시 성공은 서로 다른 검증 단계다.

## 관련 페이지

- [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]
- [[concepts/pandas-dataframe-reshape-merge|Pandas DataFrame 결합과 재구조화]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[entities/pandas|Pandas]]
- [[entities/folium|Folium]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 Python 웹 크롤링, 지오코딩, 시각화]]

## 출처

- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/교육 자료/공공 데이터 이용/공공자전거 대여소 정보(25.12월 기준).csv`
