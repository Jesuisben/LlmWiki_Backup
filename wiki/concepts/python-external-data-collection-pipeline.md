---
title: Python 외부 데이터 수집 파이프라인
created: 2026-07-13
updated: 2026-07-22
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

외부 API·웹 페이지에서 데이터를 가져와 DataFrame으로 바꾸고, 전처리·결합·집계·시각화까지 수행하는 Python 실습 흐름이다. 이 Vault에서는 2026-07-06 공공 자전거 API에서 처음 end-to-end 형태로 등장하고, 07-07 동적 웹·지오코딩으로 확장됐다.

## 왜 중요한가

외부 데이터는 요청만 성공한다고 분석 가능한 것이 아니다. 인증 설정, HTTP 응답, JSON/HTML 구조, 결측치, join key, 좌표, 저장 artifact를 단계별로 검증해야 한다. 하나의 호출을 전체 pipeline 성공으로 확대하지 않는 증거 구분이 특히 중요하다.

## 핵심 설명

### 07-06 공공 API

입력은 `.env`에서 읽는 credential, 서비스명, row 범위, 조회 날짜다. 처리 흐름은 HTTP 요청 → JSON 변환 → 서비스 row 추출 → page 반복 → list 누적 → DataFrame → CSV 저장 code다. 이후 정적 대여소 CSV·실시간 CSV·일별 CSV를 문자열 정규화와 index 설정 뒤 병합·집계·지도화했다.

대여소 교육자료 CSV는 물리적으로 존재하지만 API에서 생성하도록 작성한 실시간·일별 CSV와 지도 HTML은 raw에 없다. 따라서 입력 dataset 존재와 수집·저장 code 작성은 확인되지만 전체 API 실행 성공은 미확정이다.

### 07-07 동적 웹과 지오코딩

Selenium으로 클릭·대기 후 화면 상태를 만들고 `page_source`를 BeautifulSoup으로 파싱했다. 주소만 있는 매장은 HTTP 지오코딩 API로 좌표를 보완한 뒤 브랜드별 DataFrame을 `concat`하고 Folium·Plotly·Seaborn으로 표현했다.

원본에는 권한 비활성화 403 오류와 수정 절차가 있으나 최종 재실행 output이 없다. 결측 좌표를 제거한 DataFrame과 원본 DataFrame이 후속 지도 code에서 혼용되고, 일부 변수명 정의가 불명확하며, 저장 대상 파일도 물리적으로 남아 있지 않다. 따라서 end-to-end 성공은 `needs-review`로 남긴다.

## 단계별 완료 조건

| 단계 | 필요한 증거 | 다음 단계로 확대할 수 없는 경우 |
|---|---|---|
| 설정 | 환경변수 존재·프로그램에서 읽힘 | key 문자열이 code에 보인 것만으로 인증 성공 아님 |
| 요청 | status와 응답 구조 확인 | `requests.get()` 호출만 존재 |
| 파싱 | 기대 row·필드·HTML element 확인 | browser가 열렸다는 사실만 존재 |
| 정제 | 결측·자료형·key 정규화 확인 | DataFrame 생성만 존재 |
| 결합·집계 | 미매칭·행 수·집계 기준 확인 | `merge`·`groupby` 호출만 존재 |
| 저장·표현 | 물리 CSV/HTML/PNG와 내용 확인 | `to_csv`·`save`·`plot` 호출만 존재 |

## 자주 헷갈리는 점

- key·개인 환경 경로는 데이터가 아니라 설정값이다. code·CSV·위키에 실제 값을 넣지 않고 `.env`와 `.gitignore`로 분리한다.
- API 200과 `documents`의 실제 row 존재는 별개다.
- BeautifulSoup은 HTML parser이고 Selenium은 browser automation이다.
- join 전에는 columns·문자열·index를 같은 기준으로 정규화한다.
- 지도 object 생성, HTML file 저장, browser 표시 성공은 서로 다른 검증 단계다.
- broad exception 하나로 credential 오류·network 오류·데이터 끝을 모두 처리하면 원인 추적이 어렵다.

## 관련 개념
- [[summaries/2026-07-06-python-public-data-bicycle-analysis|2026-07-06 공공데이터 API와 자전거 분석]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 웹 크롤링·지오코딩·시각화]]
- [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]
- [[concepts/pandas-dataframe-reshape-merge|Pandas DataFrame 결합과 재구조화]]
- [[concepts/pandas-groupby-aggregation|Pandas groupby와 집계]]
- [[comparisons/beautifulsoup-vs-selenium|BeautifulSoup vs Selenium]]
- [[entities/selenium|Selenium]]
- [[entities/folium|Folium]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.06(월)/2026.07.06(월).md`
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
