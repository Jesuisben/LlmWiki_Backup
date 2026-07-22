---
title: 2026-07-08 Python 한국어 텍스트 마이닝
created: 2026-07-13
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md
status: growing
confidence: medium
---

# 2026-07-08 Python 한국어 텍스트 마이닝

## 한 줄 요약

영화 API는 실행 파일 안내만 확인하고 넘어간 뒤, 한국어 speech text를 Komoran으로 token화하고 사용자 사전·불용어·빈도 조건을 거쳐 CSV·막대그래프·WordCloud로 표현하는 pipeline code를 학습했다.

## 왜 이 순서로 배웠는가

07-06~07에는 JSON·HTML·주소를 DataFrame 행으로 구조화했다. 이날은 비정형 text를 “형태소 → 명사 token → 빈도표”로 구조화해 같은 Pandas·matplotlib 분석 흐름에 연결했다. 07-08 같은 날 Machine Learning 과목이 시작되므로 이 pipeline은 이후 feature extraction과 분류 학습의 선행 경험이 된다.

## 전체 학습 순서

1. 영화 API는 key 발급·환경변수·제공 Python 파일 실행 절차만 간단히 소개했다.
2. KoNLPy가 JVM을 사용하므로 실행 환경의 Java 위치가 필요하다는 점을 확인했다.
3. speech text·사용자 사전·불용어·mask image를 입력으로 준비했다.
4. Komoran `nouns()`로 명사 token을 추출했다.
5. 불용어를 제거하고 집합 차이로 제거 결과를 점검했다.
6. NLTK 빈도 상위 항목을 DataFrame으로 만들어 CSV 저장 code를 작성했다.
7. 길이·빈도 조건으로 단어를 다시 선별했다.
8. 상위 단어 bar chart와 mask image 기반 WordCloud를 만들고 저장하는 code를 작성했다.

## 대표 입력 → 처리 → 결과

- 입력: speech text, 사용자 사전, 불용어 목록, mask image
- 처리: text 읽기 → Komoran 명사 분석 → 불용어 제거 → 빈도 계산 → 길이·빈도 filter → DataFrame/dict 변환
- 의도한 결과: 단어 빈도 CSV, 상위 단어 bar chart PNG, WordCloud PNG

사용자 사전은 특정 복합어를 하나의 고유명사로 인식시키고, 불용어는 빈도가 높아도 분석 의미가 낮은 token을 제거한다. mask image는 WordCloud 모양과 색을 정하는 교육 입력 image다.

## code·output·artifact 경계

- package 설치 명령은 code 주석에 있지만 설치 성공 output은 없다.
- 실행 PC의 Java 경로는 개인 환경값이므로 위키에 재출력하지 않는다.
- token list·빈도 list를 출력하는 code가 있으나 실제 전체 output은 보존되지 않았다.
- `to_csv()`·`savefig()` 호출과 “저장 완료” 출력용 문자열은 있으나 날짜 폴더에 생성 CSV·PNG가 없다.
- 독립 source·notebook·dataOut artifact가 없으므로 전체 pipeline 성공을 확정하지 않는다.

## 헷갈린 점 / 질문

- 형태소 분석은 공백 기준 `split()`이 아니다. 분석기·사용자 사전이 token 경계를 결정한다.
- 불용어 제거 전후 집합 차이는 제거된 단어 종류를 보여 주지만, 각 단어가 몇 번 제거됐는지는 보여 주지 않는다.
- 빈도 상위 500개를 먼저 구한 뒤 길이·빈도 조건을 적용하므로 최종 단어 수는 500보다 작을 수 있다.
- WordCloud 생성과 PNG 저장은 별도 단계이며 mask·font·JVM 의존성 중 하나가 실패해도 전체 결과가 남지 않을 수 있다.

## 관련 페이지

- [[concepts/korean-text-mining-pipeline|한국어 텍스트 마이닝 파이프라인]]
- [[entities/konlpy|KoNLPy]]
- [[entities/pandas|Pandas]]
- [[entities/matplotlib|matplotlib]]
- [[summaries/2026-07-07-python-web-crawling-geocoding-visualization|2026-07-07 Python 웹 크롤링, 지오코딩, 시각화]]

## 출처

- `raw/KoreaICT/10. Python/2026.07.08(수)/2026.07.08(수).md`
