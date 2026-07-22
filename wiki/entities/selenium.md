---
title: Selenium
created: 2026-07-13
updated: 2026-07-22
type: entity
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md
status: growing
confidence: high
---

# Selenium

## 무엇인가

Selenium은 실제 브라우저를 자동화해 클릭·페이지 이동·대기 같은 동적 웹 동작을 수행하는 도구다.

## 이 위키에서의 맥락

2026-07-07 Python 수업에서 처음 등장했다. 커피 매장 찾기 화면을 WebDriver로 열고, CSS selector와 `WebDriverWait`로 서울·전체 선택을 수행한 뒤 `page_source`를 BeautifulSoup에 넘겼다.

## 실제 수업 역할

- Chrome WebDriver object 생성과 URL 이동
- 동적 지역 selector click
- element가 click 가능해질 때까지 explicit wait
- browser가 만든 최종 HTML을 `page_source`로 전달

Selenium은 매장 tag를 분석하는 parser가 아니라, JavaScript와 click이 반영된 화면 상태를 만드는 역할이다.

## 설치·실행 증거 경계

노트에는 `pip install selenium` 명령과 IDE 설치 절차가 있지만 설치 성공 output은 없다. browser object type·매장 수를 출력하는 code도 있으나 실제 output과 browser screenshot, 저장 HTML, CSV는 raw에 없다. 따라서 도구 선택과 automation code는 확인되지만 수집 전체 성공은 미확정이다.

## 자주 헷갈리는 점

- page가 정적이면 HTTP 응답과 BeautifulSoup만으로 충분할 수 있다.
- fixed sleep과 explicit wait는 목적이 다르며, 동적 element에는 상태 기반 wait가 더 안정적이다.
- browser가 열렸다는 사실은 selector click·파싱·저장 성공을 증명하지 않는다.
- 사이트 DOM이 바뀌면 CSS selector도 함께 깨질 수 있다.

## 관련 개념
- [[comparisons/beautifulsoup-vs-selenium|BeautifulSoup vs Selenium]]
- [[concepts/python-external-data-collection-pipeline|Python 외부 데이터 수집 파이프라인]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 웹 크롤링·지오코딩·시각화]]
- [[entities/python|Python]]

## 출처
- `raw/KoreaICT/10. Python/2026.07.07(화)/2026.07.07(화).md`
