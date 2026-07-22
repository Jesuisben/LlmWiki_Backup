---
title: 2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식
created: 2026-07-03
updated: 2026-07-22
type: summary
tags: [python, curriculum]
sources:
  - raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md
status: growing
confidence: high
---

# 2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식

## 한 줄 요약

프로그램 실패를 제어하는 예외 처리에서 시작해 파일을 읽고 변환·저장한 뒤, 문자열 패턴을 찾는 정규표현식 입문까지 외부 데이터 처리의 세 단계를 연결했다.

## 배운 내용

1. `try`·구체 `except`·상위 `Exception`·`else`·`finally`의 실행 순서를 배웠다.
2. 판매하지 않는 메뉴처럼 문법상 오류가 아닌 업무 조건을 `raise ValueError`로 예외화했다.
3. `open`의 `r/w/a/x`, text/binary mode, encoding, `close`와 `with`의 자동 해제를 학습했다.
4. `readline`·`readlines`·`read`로 한 줄/list/전체 문자열을 읽고 `strip`으로 줄바꿈을 정리했다.
5. CSV와 비슷한 텍스트 행을 `split`해 숫자로 바꾸고 계산한 뒤 다른 파일 형식으로 저장했다.
6. 마지막에는 `re.compile`·`match`, 문자 범위, 수량자, `^`·`$`를 이용해 패턴 검증을 시작했다.

예외 → 파일 → 정규표현식 순서는 “실패할 수 있는 외부 입력을 안전하게 열고, 구조를 해석하고, 필요한 패턴을 검증한다”는 하나의 데이터 처리 흐름이다. ^[raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md]

## 대표 실습

### 예외의 첫 발생 지점

한 `try` 안에 0 나눗셈과 잘못된 list 접근 가능성을 함께 두고, 실제로 먼저 실행되는 오류 하나가 해당 `except`로 제어를 넘긴다는 점을 확인했다. `else`는 오류가 없을 때만, `finally`는 발생 여부와 무관하게 실행된다.

### 텍스트 성적 변환

- **입력**: 쉼표로 구분된 학생별 텍스트 행
- **처리**: `readlines` → `strip` → `split` → 점수 `float` 변환 → 총점/평균·성별 표현 계산
- **결과 의도**: 이름/성별/총점/평균을 슬래시 구분 문자열로 만들어 결과 파일에 쓴다.

### 커피 할인 파일

- **입력**: 품명·단가·수량 텍스트와 품명별 할인율 dict
- **처리**: 행을 분해하고 할인율 key가 없으면 기본 할인율을 적용한다.
- **결과 의도**: 계산 결과를 새 list에 모아 결과 파일로 저장한다.

원본에는 입력·생성 예정 파일 내용과 code가 있으나 결과 파일 자체는 이번 직접 raw 범위에 없다. 따라서 저장 구현 근거이지 물리적 artifact 생성의 독립 증거는 아니다.

### 정규표현식 시작

알파벳 개수와 숫자 개수, 파일명 형태, 반복 문자 조건을 패턴으로 표현하고 `compile`한 뒤 각 문자열에 `match`를 적용했다. `^`와 `$`를 붙이면 전체 문자열의 시작·끝을 고정한다.

## 원본에서 확인된 주의점

- 출석 함수는 매개변수 이름을 선언했지만 함수 안에서 바깥 반복 변수에 의존한다. 현재 호출에서는 우연히 같은 값이지만, 독립 함수라면 전달받은 매개변수를 사용해야 한다.
- `w` mode는 기존 내용을 덮어쓸 수 있다. 실습 code를 다시 실행할 때 파일 보존 여부를 먼저 확인해야 한다.
- `readline().strip()` 뒤 빈 문자열을 EOF로 판단하면 실제 빈 줄과 문서 끝을 구분하지 못할 수 있다.
- 정규식의 `match()`는 문자열 앞에서 시작한다. 전체 일치는 anchor 또는 `fullmatch()` 관점으로 구분한다.

## 실행·결과 근거

- 예외·파일·regex code와 여러 출력 예시는 보존되어 있으나 독립 실행 log와 생성 텍스트 파일은 직접 raw 범위에 없다.
- `write()` 호출은 파일 생성 의도를 보여 주지만 성공 artifact를 대신하지 않는다.
- 입력 데이터에 포함된 개인·연락처 형식은 위키에 재출력하지 않았다.

## 헷갈린 점 / 질문

- `except Exception`은 구체 예외보다 아래에 둔다.
- `else`는 “해당 except가 실행되지 않았을 때”가 아니라 `try`가 예외 없이 끝났을 때 실행된다.
- `with open(...)`은 block 종료 시 close를 보장하므로 수동 close 누락을 줄인다.
- `readlines()` 결과의 줄바꿈과 데이터 자체 공백을 구분해 `strip` 범위를 결정한다.
- 정규식의 `.`은 임의 문자이고 문자 그대로의 점은 `\.`로 표현한다.

## 이전·다음 수업 연결

- **이전**: [[summaries/2026-06-25-python-standard-library-oop|06-25]]의 module·class code에 실패 처리와 외부 파일 경계를 추가했다.
- **다음**: [[summaries/2026-06-29-python-regex-xml-json-jupyter|06-29]]에서 `search`·`findall`·`finditer`, XML/JSON과 library/Jupyter 준비로 확장한다.
- **후속**: 파일의 행 데이터를 직접 분해한 경험은 Pandas `read_csv`와 DataFrame 변환의 선행 단계다.

## 관련 페이지

- [[concepts/python-exception-handling|Python 예외 처리]]
- [[concepts/python-file-regex-data-processing|Python 파일 입출력과 텍스트 데이터 처리]]
- [[concepts/python-regular-expression|Python 정규표현식]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md`
