---
title: Python 함수, 모듈, 패키지
created: 2026-07-03
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# Python 함수, 모듈, 패키지

## 정의

- **함수(function)**: 입력을 받아 동작하고 필요하면 값을 반환하는 재사용 단위
- **모듈(module)**: 함수·변수·class·실행문을 담은 Python 파일
- **패키지(package)**: 관련 module을 디렉터리 계층으로 묶어 namespace를 구성하는 단위

## 왜 중요한가

반복 code를 함수로 분리하면 입력과 결과의 경계가 선명해진다. module/package는 파일이 많아져도 기능을 찾고 import할 수 있게 한다. 06-24에는 직접 만든 code를 재사용했고, 06-29에는 같은 import 원리로 표준 module과 Third Party library를 사용했다.

## 함수의 입력과 출력

### 위치·키워드·기본 인수

- 위치 인수는 선언된 순서에 맞춘다.
- keyword 인수는 매개변수 이름으로 연결한다.
- 기본값이 있는 매개변수는 호출 시 생략할 수 있다.
- 위치 인수와 keyword 인수를 섞으면 위치 인수가 먼저 온다.

### 가변 인수

일반 매개변수 → `*args` → `**kwargs` 순서로 선언한다. `*args`는 남은 위치 인수를 tuple로, `**kwargs`는 남은 keyword 인수를 dict로 모은다. 06-24의 category/항목/가격 정보 출력 함수가 실제 수업 예다. ^[raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md]

### 함수도 값이다

lambda는 짧은 단일 표현식을 함수 객체로 만든다. `filter`는 boolean을 반환하는 함수를 이용해 원소를 고르고, `map`은 각 원소를 새 값으로 변환한다. `map(func, data)`에서 `func()`가 아니라 `func`를 넘기는 이유는 지금 실행할 결과가 아니라 반복 과정에서 호출할 동작을 전달하기 때문이다.

## module과 실행 진입점

module을 import하면 함수 정의뿐 아니라 top-level 실행문도 평가된다. `__name__ == "__main__"` 분기는 그 파일을 직접 실행할 때만 demo/test code를 실행하도록 나누는 기본 장치다.

수업의 import 범위는 다음을 포함했다.

- module 전체 import 후 전체 경로 사용
- module에 별칭 부여
- package에서 module import
- module에서 함수 직접 import
- 함수에 별칭 부여

이 차이는 “어떤 이름을 현재 namespace에 넣는가”의 차이다.

## 표준·사용자·외부 module

| 구분 | 만든 주체/배포 | 수업 예 |
|---|---|---|
| built-in function | Python runtime에서 바로 제공 | `print`, `len`, `type` |
| standard module | Python 설치에 포함, import 필요 | `os`, `random`, `datetime`, `re`, `json` |
| user module | 학습자/개발자가 작성 | 문자열 분리·결합, 수학 함수 module |
| Third Party library | 별도 설치 | Pandas, matplotlib |

06-29의 `pip` 명령과 IDE 설치 절차는 외부 library를 가져오는 방법을 보여 주지만 설치 성공 log 자체는 보존되지 않았다. ^[raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md]

## 수업 code에서 배울 점

- 기본 인수 설명과 실제 함수 signature가 맞지 않는 곳은 호출 code를 함께 보고 판정한다.
- 성적 함수는 불합격 분기 문자열이 요구와 어긋나므로 출력 예시를 현재 code의 실행 결과로 단정하지 않는다.
- 전역 list에 결과를 누적하는 최솟값/최댓값 함수는 호출 간 상태가 섞인다. 가능하면 함수 안의 지역 데이터 또는 입력값만으로 결과를 만든다.
- import 시 실행되는 print는 재사용 module의 side effect가 될 수 있다.

## 자주 헷갈리는 점

- Python이 타입 선언을 강제하지 않는 것과 타입이 없는 것은 다르다.
- 함수가 `return`하지 않으면 기본 반환값은 `None`이다.
- `*`·`**`는 정의와 호출에서 “묶기/풀기” 문맥이 달라질 수 있다.
- module은 파일, package는 디렉터리 계층이다.
- `pip`로 설치하는 package 이름과 Python에서 import하는 module 이름이 항상 같지는 않다.

## 선행·후속 연결

- **선행**: [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]의 반복·필터·dict
- **다음**: [[concepts/python-oop-basics|Python 객체지향 기본]]에서 상태와 method를 class에 묶음
- **후속**: [[concepts/python-regular-expression|Python 정규표현식]], [[concepts/python-structured-data-xml-json|Python XML/JSON 구조화 데이터 처리]], [[entities/pandas|Pandas]]의 import와 API 호출

## 관련 수업

- [[summaries/2026-06-24-python-functions-modules|2026-06-24 Python 함수, 람다, 모듈·패키지]]
- [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.24(수)/2026.06.24(수).md`
- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
