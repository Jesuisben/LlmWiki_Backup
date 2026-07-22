---
title: 2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치
created: 2026-07-03
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# 2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치

## 한 줄 요약

문자열 패턴 추출을 심화하고 XML/JSON을 Python 객체로 왕복한 뒤, 외부 library와 Jupyter를 준비해 다음 날 Pandas 분석 환경으로 전환했다.

## 배운 내용

1. `match`와 `search`, Match 객체의 `start`·`end`·`group`·`span`을 비교했다.
2. `findall`과 `finditer`로 모든 일치 문자열 또는 Match 객체를 수집했다.
3. raw string과 escape를 이용해 역슬래시·탭·개행·경로·특수 문자를 패턴으로 표현했다.
4. `Element`·`SubElement`·`ElementTree.write`로 XML을 구성하고 `parse`·`getroot`·`findall`로 읽었다.
5. JSON 문자열을 `json.loads`로 dict/list 구조로 바꾸고 중첩 key를 따라 필요한 값을 tuple/list로 재구성했다.
6. `pip` install/uninstall/list, requirements 파일 설치, Pandas·matplotlib 설치 절차를 확인했다.
7. Jupyter Notebook 실행 command와 작업 디렉터리·실행용 command file 구성을 기록했다.

정규식은 비정형 문자열에서 필요한 조각을 찾고, XML/JSON은 이미 구조화된 문서를 계층으로 해석한다. 마지막의 library/Jupyter 준비는 이 데이터를 Pandas 표로 처리하는 다음 단계의 환경 전환이다. ^[raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md]

## 대표 실습

### `match`·`search`·`findall`·`finditer`

- `match`: 문자열 시작 위치에서 조건 확인
- `search`: 문자열 전체에서 첫 일치 탐색
- `findall`: 일치 문자열들을 list로 반환
- `finditer`: 각 일치의 위치와 문자열을 가진 Match 객체를 순회

날짜·구매 수량·단어·주소 뒷부분을 추출하며 “검증”과 “검색”, “문자열 목록”과 “위치 정보”의 차이를 확인했다.

### XML 생성과 파싱

- **생성**: root Element에 속성·자식 tag·text를 추가하고 tree로 저장하는 code를 작성했다.
- **읽기**: XML file을 tree로 parse하고 root → 가족/car element → 자식 tag/attribute를 순회해 tuple/list로 모았다.
- **근거 한계**: write code와 생성 완료 문구는 있지만 생성 XML artifact가 직접 raw에 보존된 것은 아니다. 반면 읽기 예제의 XML 본문은 노트에 함께 들어 있다.

### JSON 중첩 구조 평탄화

- **입력**: 사람 또는 커피별 중첩 JSON object
- **처리**: file text → `json.loads` → dict의 nested key 접근 → 가변 길이 recipe 조립
- **결과**: 필요한 필드를 tuple로 만들고 list에 누적하는 code와 출력 예시가 기록되어 있다.

개인 연락처 형태가 포함된 교육용 JSON은 구조 설명에만 사용하고 실제 값을 위키에 옮기지 않는다.

## 실행·결과 근거

- regex code와 출력 블록은 노트에 보존되어 있으나 모든 예제의 독립 실행을 증명하지는 않는다.
- XML `write`·Jupyter 실행·package 설치 command는 구현/절차 근거다. 생성 XML, notebook 파일, 설치 log는 현재 직접 범위에 없다.
- raw 재고에는 `.ipynb`가 없으므로 Jupyter curriculum과 셀 사용법은 확인되지만 전체 notebook 재실행 가능성은 입증되지 않는다.

## 원본에서 확인된 주의점

- 일반 문자열과 raw string의 escape 설명 일부는 출력 표현(`repr`)과 실제 문자열을 혼동하기 쉽다.
- source 안의 줄바꿈 escape 설명이 Markdown 변환 과정에서 줄로 분리된 부분이 있어, 그대로 실행 가능한 code fence로 위키에 재합성하지 않는다.
- JSON recipe의 마지막 label이 실제 key 의미와 다르게 적힌 부분이 있다. 핵심은 nested key의 종류에 따라 출력 문자열을 다르게 조립한 것이다.
- `pip install` 명령이 적혀 있다는 사실만으로 해당 package 설치 성공을 확정하지 않는다.

## 헷갈린 점 / 질문

- pattern 앞의 `r`은 정규식 문법이 아니라 Python 문자열 escape 처리를 줄이는 raw string 표기다.
- `findall`은 문자열, `finditer`는 Match 객체 iterator를 주로 돌려준다.
- XML attribute와 child element는 둘 다 정보를 담지만 접근 방식이 다르다.
- `json.load(file)`은 file object, `json.loads(string)`은 문자열을 입력받는다.
- Pandas는 표준 module이 아니라 별도 설치하는 Third Party library다.

## 이전·다음 수업 연결

- **이전**: [[summaries/2026-06-26-python-exception-file-regex|06-26]]의 파일 입출력과 regex 검증을 검색·구조화 문서로 확장했다.
- **다음**: [[summaries/2026-06-30-python-pandas-series-dataframe-intro|06-30]]에서 Jupyter 셀 안에서 Series/DataFrame을 만들고 그래프를 그린다.
- **후속**: JSON/dict·XML tree를 해석하는 경험은 이후 외부 데이터 수집의 입력 구조를 이해하는 기반이 된다. 07-01 이후 실습 자체는 이번 고도화 범위에서 다루지 않는다.

## 관련 페이지

- [[concepts/python-regular-expression|Python 정규표현식]]
- [[concepts/python-structured-data-xml-json|Python XML/JSON 구조화 데이터 처리]]
- [[concepts/python-file-regex-data-processing|Python 파일 입출력과 텍스트 데이터 처리]]
- [[entities/jupyter-notebook|Jupyter Notebook]]
- [[entities/pandas|Pandas]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
