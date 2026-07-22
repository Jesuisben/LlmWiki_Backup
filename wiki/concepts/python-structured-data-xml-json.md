---
title: Python XML/JSON 구조화 데이터 처리
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# Python XML/JSON 구조화 데이터 처리

## 정의

XML과 JSON은 계층 구조를 가진 데이터를 text로 교환하는 형식이다. Python에서는 XML tree와 JSON의 dict/list 구조를 읽어 필요한 field를 추출하고, 필요하면 다시 file로 저장할 수 있다.

## 왜 중요한가

06-29 수업은 일반 text를 `split`하는 단계에서 구조화 문서 parser로 이동했다. 이후 외부 system에서 받은 payload를 Python 객체로 변환하고 표 형태로 정리하려면 “문서 구조 → Python 자료구조 → 분석용 행”의 변환을 이해해야 한다.

## XML과 JSON 비교

| 항목 | XML | JSON |
|---|---|---|
| 기본 구조 | tag·attribute·text | object·array·value |
| Python 수업 API | `Element`, `SubElement`, `ElementTree`, `parse` | `json.loads` |
| Python 변환 중심 | tree/Element 순회 | dict/list 직접 접근 |
| 정보 위치 | attribute와 child text가 나뉨 | key-value와 array nesting |
| 수업 결과 | 자동차·가족 요소를 tuple/list로 정리 | 사람·커피 객체를 tuple/list로 정리 |

## XML 처리 흐름

### 생성

1. root `Element`를 만든다.
2. `SubElement`로 child tag를 추가한다.
3. attribute와 text를 채운다.
4. `ElementTree`로 감싸고 write method로 저장한다.

원본에는 XML 생성 code와 완료 문구가 있지만 생성된 XML artifact는 직접 raw 범위에 보존되지 않았다. 따라서 구현과 수업 결과 서술은 확인되나 file 존재를 독립 검증한 것은 아니다. ^[raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md]

### 읽기

1. file을 `parse`해 tree를 얻는다.
2. `getroot`로 root element를 얻는다.
3. `findall` 또는 child 반복으로 element를 찾는다.
4. attribute는 `get`, child text는 `find(...).text` 같은 방식으로 꺼낸다.
5. 필요한 값을 tuple/list로 모은다.

XML의 `findall`은 regex의 `findall`과 이름이 같아도 tree element를 찾는 다른 API다.

## JSON 처리 흐름

1. JSON text를 준비하거나 file에서 읽는다.
2. `json.loads(text)`로 Python dict/list로 바꾼다.
3. 중첩 key와 array position을 따라 필요한 값을 찾는다.
4. 필드 수가 가변적인 부분은 loop로 조립한다.
5. 분석하기 쉬운 tuple/list 같은 행 구조로 모은다.

수업에서는 중첩 object의 사람이름·연락처·주소와 커피 recipe를 꺼냈다. 실제 개인·연락처 값은 구조 교육용이라도 위키에 재출력하지 않는다.

## `load`와 `loads`

- `json.load(file_object)`: 열린 file object에서 JSON을 읽는다.
- `json.loads(string)`: JSON 문자열을 읽는다.

수업은 text를 `read()`한 다음 `loads`를 적용했다. file을 바로 넘길지 문자열을 먼저 만들지는 API 입력 타입에 따라 선택한다.

## parser를 쓰는 이유

XML/JSON을 regex나 단순 `split`으로 처리하면 nesting, escape, 배열 길이, attribute를 안정적으로 다루기 어렵다. 구조를 아는 전용 parser로 문서를 Python 객체로 변환하고, 그 이후에 일반 collection 처리를 적용하는 것이 핵심이다.

## 실행·결과 근거

- XML 생성·parse, JSON `loads`와 tuple/list 변환 code가 날짜 노트에 있다.
- XML/JSON 본문과 출력 예시는 embedded evidence지만 모든 code의 독립 실행 log는 없다.
- save call과 “생성됨” 문구만으로 생성 file의 현재 존재를 확정하지 않는다.
- 입력에 개인·contact 형태가 포함되어 있어 위키에서는 값 대신 구조만 설명한다.

## 자주 헷갈리는 점

- XML attribute와 child element는 접근 방식이 다르다.
- JSON object는 Python dict, JSON array는 list로 대응되지만 JSON과 Python literal 문법이 완전히 같은 것은 아니다.
- JSON key가 있다고 가정하고 바로 접근하면 `KeyError`가 날 수 있다.
- array 길이가 가변적이면 고정 position 접근을 조심한다.
- XML `findall`과 regex `re.findall`은 다른 함수다.
- write code와 생성 artifact 존재를 같은 증거로 취급하지 않는다.

## 선행·후속 연결

- **선행**: [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]의 dict/list/tuple, [[concepts/python-file-regex-data-processing|Python 파일 입출력과 텍스트 데이터 처리]]
- **당일**: [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- **후속**: [[entities/pandas|Pandas]]에서 tuple/list/dict를 Series/DataFrame으로 구조화하는 단계

## 관련 개념

- [[concepts/python-regular-expression|Python 정규표현식]]
- [[concepts/python-exception-handling|Python 예외 처리]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
