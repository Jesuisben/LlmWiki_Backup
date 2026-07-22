---
title: Python 예외 처리
created: 2026-07-22
updated: 2026-07-22
type: concept
tags: [python, debugging]
sources:
  - raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md
status: growing
confidence: high
---

# Python 예외 처리

## 정의

Python 예외 처리(exception handling)는 실행 중 발생할 수 있는 실패를 감지하고, 오류 유형에 맞는 대체 흐름·정리 작업·업무상 오류 발생을 명시하는 구조다.

## 왜 중요한가

외부 입력, 숫자 계산, collection 조회, file I/O는 모두 실패할 수 있다. 예외를 무시하는 것이 아니라 “어디서 실패할 수 있는지, 어떤 실패만 처리할지, 처리 후 program이 어떤 상태여야 하는지”를 code로 표현해야 한다.

## 기본 실행 흐름

| 구문 | 실행 시점 | 수업에서의 역할 |
|---|---|---|
| `try` | 실패 가능 code 실행 | 나눗셈·list 접근·메뉴 판정 |
| `except 특정예외` | 해당 유형 발생 | `ZeroDivisionError`, `IndexError`, `ValueError` 구분 |
| `except Exception` | 앞에서 잡히지 않은 일반 예외 | 마지막 안전망 |
| `else` | `try`가 예외 없이 끝남 | 정상 처리 전용 흐름 |
| `finally` | 예외 여부와 무관 | 공통 마무리 |
| `raise` | 조건을 예외로 전환 | 판매하지 않는 메뉴 거부 |

구체 예외를 먼저 두고 상위 `Exception`을 뒤에 둔다. 상위 유형을 앞에 두면 뒤의 구체 분기가 도달하지 못한다. ^[raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md]

## 첫 예외에서 제어가 이동한다

한 `try` block 안에 여러 실패 가능 문장이 있어도 첫 예외가 발생한 순간 남은 `try` 문장은 실행되지 않고 일치하는 `except`로 이동한다. 06-26의 0 나눗셈과 list 범위 초과 예제가 이 실행 순서를 설명한다.

따라서 서로 독립적으로 복구해야 하는 작업은 무조건 하나의 큰 `try`에 넣기보다 처리 경계별로 나누는 편이 낫다.

## `raise`로 업무 규칙 표현

문법·타입상 실행 가능한 값이라도 프로그램 규칙에 맞지 않을 수 있다. 수업에서는 판매 대상이 아닌 메뉴를 `ValueError`로 발생시켰다.

이때 좋은 예외는 다음 정보를 가져야 한다.

- 어떤 조건이 잘못되었는가
- caller가 고칠 수 있는 입력인가
- 어느 exception type으로 구분할 것인가
- 민감한 원본 입력을 message에 그대로 노출하지 않는가

## `finally`와 resource 정리

`finally`는 성공·실패와 무관하게 실행되지만, file close에는 `with` context manager가 더 직접적이다. `with`가 file resource 생명주기를 표현하고, 예외 처리는 읽기·파싱·변환 실패를 설명하는 데 집중할 수 있다.

## 수업 code에서 확인할 점

- 구체 exception과 `Exception`의 순서는 올바른 흐름의 핵심이다.
- `raise` 후 같은 `try`의 나머지 문장은 실행되지 않는다.
- 예외 message가 출력되었다고 오류가 “해결”된 것은 아니다. program이 필요한 결과와 일관된 상태를 만들었는지도 확인해야 한다.
- 원본에는 예외 처리 code와 교안형 출력이 있으나 모든 분기의 독립 실행 transcript는 없다.

## 자주 헷갈리는 점

- `else`는 `except`의 반대가 아니라 `try`가 정상 종료했을 때 실행된다.
- `finally` 안에서 새 예외가 발생하면 원래 흐름을 가릴 수 있다.
- 모든 오류를 `Exception` 하나로만 잡으면 원인을 구분하기 어렵다.
- 예외를 잡고 아무것도 하지 않으면 실패가 숨는다.
- 사용자의 잘못된 입력과 programming bug를 같은 방식으로 처리하지 않는다.

## 선행·후속 연결

- **선행**: [[concepts/python-basic-syntax|Python 기본 문법]]의 계산·조건과 [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]의 index/key 조회
- **당일**: [[summaries/2026-06-26-python-exception-file-regex|2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식]]
- **후속**: [[concepts/python-file-regex-data-processing|Python 파일 입출력과 텍스트 데이터 처리]], [[concepts/python-structured-data-xml-json|Python XML/JSON 구조화 데이터 처리]]의 외부 입력 오류 처리

## 관련 개념

- [[concepts/python-oop-basics|Python 객체지향 기본]]
- [[entities/python|Python]]
- [[concepts/python-regular-expression|Python 정규표현식]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md`
