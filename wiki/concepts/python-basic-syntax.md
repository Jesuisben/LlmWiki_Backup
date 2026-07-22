---
title: Python 기본 문법
created: 2026-07-03
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md
  - raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md
status: growing
confidence: high
---

# Python 기본 문법

## 정의

Python 기본 문법은 값을 만들고 타입을 변환하며, 입력 → 처리 → 출력 순서를 조건과 반복으로 제어하는 최소 언어 규칙이다. 이 Vault에서는 2026-06-19의 출력·문자열·연산에서 시작해 06-22의 분기·반복까지 이어졌다.

## 왜 중요한가

Pandas도 결국 Python 문법으로 호출한다. Series를 필터링하는 비교식, DataFrame 행을 반복하는 code, 외부 데이터의 문자열을 숫자로 바꾸는 과정 모두 형변환·조건·반복·slicing 위에 서 있다. Java를 먼저 배운 관점에서는 문법 모양보다 “값의 타입과 실행 순서”를 대응시키는 것이 중요하다.

## 이 수업에서의 학습 흐름

1. `print`의 `sep`·`end`와 문자열 포맷으로 값을 표시했다.
2. `input`으로 받은 문자열을 `int`·`float`로 변환해 계산했다.
3. `/`, `//`, `%`, `**`, 복합 대입, 관계·논리 연산자로 새 값을 만들었다.
4. `if`·`elif`·`else`로 조건에 따라 실행 경로를 나눴다.
5. `for`·`range`로 횟수 기반 반복, `while`로 상태 기반 반복을 구성했다.
6. 문자열 함수와 indexing/slicing으로 필요한 조각을 추출했다.

## 핵심 설명

### 입력 → 형변환 → 계산 → 출력

`input()`의 반환값은 항상 문자열이다. 점수 합계처럼 산술 계산을 하려면 먼저 숫자 타입으로 바꿔야 하고, 문자열 연결로 표시하려면 숫자를 다시 문자열로 바꾸거나 포맷을 사용해야 한다. 06-19 노트에는 문자열과 정수를 직접 연결해 발생한 `TypeError`, `str()` 수정, 정상 출력이 연속으로 남아 있다. ^[raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md]

### 조건과 반복

- `if`는 조건이 참일 때 block을 실행한다.
- `elif`는 앞 조건이 거짓일 때 다음 조건을 검사한다.
- `for`는 iterable의 원소를 차례로 꺼낸다.
- `range`는 정수 범위를 만들며 stop은 포함하지 않는다.
- `while`은 조건이 참인 동안 반복한다.

06-22의 커피 판매는 입금액 분기 → 재고 감소 → 재고 0에서 종료로 이어져, 조건과 상태 변화가 반복 종료를 어떻게 만드는지 보여 준다. ^[raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md]

### 문자열도 sequence다

문자열은 순서가 있어 indexing과 slicing이 가능하다. `strip`은 양끝 제거, `split`은 문자열 → list, `join`은 iterable 문자열 → 하나의 문자열, `find`는 위치 검색을 담당한다. 이후 텍스트 파일·regex·Pandas 문자열 전처리로 역할이 확장된다.

## 대표 판단 기준

| 상황 | 먼저 확인할 것 | 선택 |
|---|---|---|
| 입력값 계산 | 현재 타입 | `int()`·`float()` 변환 |
| 횟수가 정해진 반복 | 반복 범위 | `for` + `range` |
| 상태가 바뀔 때까지 반복 | 종료 조건·상태 변화 | `while` |
| 문자열 한 글자 | 위치 하나 | indexing |
| 문자열 일부 범위 | 시작·끝·간격 | slicing |

## 자주 헷갈리는 점

- Python은 변수 선언에 타입을 고정해 적지 않지만, 값에는 항상 실제 타입이 있다.
- `print()`의 기본 `sep`는 공백이고 기본 `end`는 줄바꿈이다. 원본의 두 역할을 뒤바꿔 읽지 않는다.
- Python/Java를 interpreter/compiler로만 양분하지 않는다. 두 언어 모두 source 변환 단계와 runtime 실행 환경을 가진다.
- `/`는 실수 나눗셈이고 `//`는 몫이다.
- `range(1, 5)`는 1~4다.
- slice의 끝 position은 포함하지 않는다.
- `while True`는 `break`나 상태 변화가 없으면 끝나지 않는다.
- 들여쓰기는 꾸밈이 아니라 block 구조다.
- Java의 형변환 표기와 Python의 `타입(값)` 호출 형태를 섞지 않는다.

## 선행·후속 연결

- **선행**: Java 변수·연산자·조건문·반복문과 목적은 같지만 동적 typing과 들여쓰기가 다르다.
- **다음**: [[concepts/python-collections-comprehension|Python 컬렉션과 컴프리헨션]]에서 같은 규칙을 여러 값에 적용한다.
- **후속**: [[concepts/python-file-regex-data-processing|Python 파일 입출력과 텍스트 데이터 처리]]와 [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]에서 입력 source와 데이터 규모가 커진다.

## 관련 수업

- [[summaries/2026-06-19-python-setup-basic-syntax|2026-06-19 Python 설치와 기본 문법 입문]]
- [[summaries/2026-06-22-python-control-flow-collections|2026-06-22 Python 제어문과 컬렉션]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.19(금) - 시작/2026.06.19(금) - 시작.md`
- `raw/KoreaICT/10. Python/2026.06.22(월)/2026.06.22(월).md`
