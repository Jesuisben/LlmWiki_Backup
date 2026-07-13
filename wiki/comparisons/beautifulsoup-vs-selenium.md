---
title: BeautifulSoup vs Selenium
created: 2026-07-13
updated: 2026-07-13
type: comparison
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# BeautifulSoup vs Selenium

## 비교 목적
웹 데이터를 수집할 때 HTML을 읽는 도구와 실제 브라우저를 조작하는 도구를 구분한다.

## 한눈에 보기
| 항목 | BeautifulSoup | Selenium |
|---|---|---|
| 주 역할 | 받은 HTML 파싱 | 브라우저 자동화 |
| 적합한 대상 | 이미 응답에 있는 정적 HTML | 클릭·이동·대기 후 생기는 동적 화면 |
| 수업 사용 | `page_source`에서 매장 태그·속성 추출 | 매장 찾기 화면 열기와 지역 선택 |

## 언제 무엇을 쓰는가
클릭 없이 HTTP 응답 HTML만으로 필요한 데이터가 있으면 BeautifulSoup으로 파싱한다. JavaScript 실행·로그인·버튼 클릭처럼 브라우저 동작이 있어야 데이터가 보이면 Selenium으로 화면을 만든 뒤, 필요하면 결과 HTML을 BeautifulSoup에 넘긴다.

## 헷갈리기 쉬운 포인트
Selenium이 HTML 파싱을 대체하는 것이 아니라, 동적 상태를 만든다. 수업도 Selenium으로 클릭한 뒤 `driver.page_source`를 BeautifulSoup으로 파싱하는 조합을 사용했다.

## 관련 페이지
- [[entities/selenium|Selenium]]
- [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 웹 크롤링·지오코딩·시각화]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
