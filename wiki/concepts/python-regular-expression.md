---
title: Python 정규표현식
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# Python 정규표현식

## 정의

정규표현식(regular expression, regex)은 문자열의 문자 종류·위치·반복 규칙을 pattern으로 표현해 검증·검색·추출하는 방법이다. Python에서는 `re` 표준 module을 사용한다.

## 왜 중요한가

문자열 slicing은 위치를 이미 알 때 유용하지만, 실제 file·주소·날짜·filename은 내용의 모양으로 찾는 경우가 많다. 06-26에는 pattern 검증을, 06-29에는 문자열 전체 검색과 모든 일치 추출을 배워 regex의 독립 학습 흐름이 이틀에 걸쳐 반복되었다.

## pattern의 기본 구성

| 표현 | 의미 | 주의 |
|---|---|---|
| `.` | 임의 한 문자 | 문자 그대로의 점은 `\.` |
| `[A-Z]` | 범위 중 한 문자 | 대괄호 안에서 문자 집합 지정 |
| `[^0-9]` | 숫자가 아닌 한 문자 | `^`가 class 안에서는 부정 |
| `*` | 0회 이상 | 빈 문자열도 허용 |
| `+` | 1회 이상 | 최소 한 번 필요 |
| `?` | 0회 또는 1회 | 선택 항목 |
| `{n,m}` | n~m회 | 경계 포함 |
| `^` | 문자열 시작 | 전체 조건의 시작 고정 |
| `$` | 문자열 끝 | 전체 조건의 끝 고정 |
| `\d`·`\s`·`\w` | 숫자·공백·단어 문자 | Unicode/ASCII 문맥 확인 |

06-26에는 알파벳/숫자 개수와 파일명 형식에 `compile`·`match`·anchor를 적용했다. ^[raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md]

## 검색 API 비교

| 함수 | 탐색 범위 | 주 결과 |
|---|---|---|
| `match` | 문자열 시작부터 | 첫 Match 또는 `None` |
| `search` | 문자열 전체 | 첫 Match 또는 `None` |
| `findall` | 모든 일치 | 일치 문자열 list 중심 |
| `finditer` | 모든 일치 | Match 객체 iterator |
| `fullmatch` | 문자열 전체 | 전체 일치 Match 또는 `None` |

Match 객체의 `start`, `end`, `span`, `group`으로 일치 위치와 내용을 구분한다. 06-29에는 날짜·수량·단어·주소의 상세 부분을 찾아 “첫 일치”와 “모든 일치”, “문자열”과 “위치 포함 객체”의 차이를 확인했다. ^[raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md]

## raw string과 escape

pattern에는 역슬래시가 자주 들어가므로 Python 문자열 앞에 `r`을 붙여 source-level escape를 줄인다. 다만 raw string이 regex 특수 문자의 의미를 없애는 것은 아니다. Python 문자열 parser와 regex engine이라는 두 해석 단계를 구분해야 한다.

원본의 일부 escape 예제는 Markdown 변환 중 줄바꿈 모양이 달라져 그대로 실행 가능한 연속 code인지 불명확하다. 따라서 위키에는 합성 code fence를 만들지 않고 개념과 API 역할만 정리했다.

## 대표 판단 흐름

1. **목적**: 전체 형식 검증인가, 일부 검색인가?
2. **pattern**: 문자 종류·수량·anchor를 정한다.
3. **문자열 표현**: raw string과 literal escape를 확인한다.
4. **API 선택**: `fullmatch`/`match`/`search`/`findall`/`finditer` 중 고른다.
5. **결과 확인**: `None` 가능성과 Match/string 반환 차이를 처리한다.
6. **민감정보**: 연락처·계정·domain 같은 원문을 log·wiki에 그대로 남기지 않는다.

## 자주 헷갈리는 점

- `match`는 문자열 어디서나 찾는 함수가 아니다.
- `^`와 `$`는 문자 class 안팎에서 의미가 달라질 수 있다.
- `.`은 문자 그대로의 점이 아니다.
- `findall`에 capture group이 있으면 반환 모양이 달라질 수 있다.
- regex로 가능한 것과 regex로 읽기 좋은 것은 다르다. XML/JSON처럼 parser가 있는 구조는 전용 parser를 우선한다.
- code에 pattern이 있다는 사실만으로 실제 모든 입력 검증 성공이 증명되지는 않는다.

## 선행·후속 연결

- **선행**: [[concepts/python-basic-syntax|Python 기본 문법]]의 문자열 함수·slicing, [[concepts/python-file-regex-data-processing|Python 파일 입출력과 텍스트 데이터 처리]]
- **수업**: [[summaries/2026-06-26-python-exception-file-regex|06-26 입문]], [[summaries/2026-06-29-python-regex-xml-json-jupyter|06-29 심화]]
- **후속**: [[concepts/python-structured-data-xml-json|Python XML/JSON 구조화 데이터 처리]]와 비정형/구조형 데이터 처리의 선택

## 관련 개념

- [[concepts/python-exception-handling|Python 예외 처리]]
- [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md`
- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
