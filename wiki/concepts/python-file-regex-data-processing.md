---
title: Python 파일 입출력과 텍스트 데이터 처리
created: 2026-07-03
updated: 2026-07-22
type: concept
tags: [python]
sources:
  - raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md
  - raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md
status: growing
confidence: high
---

# Python 파일 입출력과 텍스트 데이터 처리

## 정의

Python 파일 입출력은 storage의 byte/text를 program 안으로 읽거나 program의 결과를 밖으로 쓰는 작업이다. 이 페이지는 06-26의 일반 text file 처리에 집중하고, 예외·regex·XML/JSON은 독립 검색 가치 때문에 별도 concept로 연결한다.

## 왜 중요한가

Pandas `read_csv()`를 사용하기 전, 수업은 `open` → 줄 읽기 → `strip`/`split` → 타입 변환 → 계산 → 새 파일 쓰기를 직접 구현했다. 이 흐름을 이해하면 DataFrame API가 어떤 반복 작업을 대신하는지 설명할 수 있다.

## 파일 처리 생명주기

1. 경로·filename·encoding·mode를 결정한다.
2. `open()`으로 file object를 얻는다.
3. `readline`·`readlines`·`read` 또는 반복으로 읽는다.
4. 문자열을 정리·분해·형변환하고 필요한 값을 계산한다.
5. `write` 또는 `print(..., file=...)`로 기록한다.
6. file을 닫아 buffer와 resource를 정리한다.

`with open(...) as file:`을 사용하면 block 종료 때 close가 수행되어 누락 위험을 줄인다. ^[raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md]

## mode와 결과

| mode | 의미 | 중요한 위험/조건 |
|---|---|---|
| `r` | 읽기 | file이 없으면 오류 |
| `w` | 새로 쓰기/덮어쓰기 | 기존 내용 손실 가능 |
| `a` | 뒤에 추가 | 기존 내용 보존 후 append |
| `x` | 새 file만 생성 | 이미 있으면 오류 |
| `t` | text | encoding 적용, 기본 mode |
| `b` | binary | image·PDF 등 byte 처리 |

읽기와 쓰기의 목적을 분리해 file을 열고, text file에서는 encoding을 명시하는 습관이 중요하다.

## 읽기 방법 비교

- `readline()`: 한 줄 문자열, file pointer가 다음 줄로 이동
- `readlines()`: 모든 줄을 문자열 list로 반환
- `read()`: 전체 내용을 하나의 문자열로 반환

수업에서는 각 줄 끝의 개행을 제거하기 위해 `strip()`을 사용했다. 다만 `strip()`은 개행뿐 아니라 양끝 공백 전체를 제거하므로 공백이 의미 있는 데이터에서는 `rstrip("\n")` 같은 더 좁은 처리도 고려한다.

## 대표 데이터 흐름

### 성적 text → 결과 text

- 쉼표 구분 행을 읽는다.
- 각 행을 `split`해 필드 list로 만든다.
- 점수를 숫자로 변환해 총점·평균을 계산한다.
- 필요한 표시값을 조립해 slash 구분 결과를 쓴다.

### 커피 text → 할인 결과

- 품명·단가·수량을 읽는다.
- 할인율 dict에서 품명 key를 찾고 없으면 기본값을 적용한다.
- 계산 결과를 새 문자열 list에 모아 output file로 쓴다.

두 실습 모두 code와 예정 입력/결과가 노트에 있으나 생성 output file 자체는 직접 raw에 보존되지 않았다. 따라서 save call은 구현 근거이며 실제 artifact 존재를 대신하지 않는다.

## 자주 헷갈리는 점

- `write()`가 호출됐다는 기록과 file artifact가 실제로 보존됐다는 사실은 다르다.
- `w` mode는 재실행할 때 기존 file을 덮어쓴다.
- `readlines()`의 list 요소에는 보통 줄바꿈이 남는다.
- 빈 문자열은 EOF일 수 있지만, `strip()` 후 실제 빈 줄도 빈 문자열이 된다.
- 상대 경로는 현재 working directory에 따라 달라진다.
- text와 binary mode를 혼동하면 encoding·타입 오류가 생긴다.

## 역할 분리

- 실패 처리: [[concepts/python-exception-handling|Python 예외 처리]]
- 문자열 패턴 검증·추출: [[concepts/python-regular-expression|Python 정규표현식]]
- 계층형 구조 문서: [[concepts/python-structured-data-xml-json|Python XML/JSON 구조화 데이터 처리]]
- 표 파일의 고수준 처리: [[concepts/pandas-dataframe-basics|Pandas DataFrame 기본]]

## 관련 수업

- [[summaries/2026-06-26-python-exception-file-regex|2026-06-26 Python 예외 처리, 파일 입출력, 정규표현식]]
- [[summaries/2026-06-29-python-regex-xml-json-jupyter|2026-06-29 Python 정규표현식, XML/JSON, 라이브러리 설치]]
- [[entities/python|Python]]

## 출처

- `raw/KoreaICT/10. Python/2026.06.26(금)/2026.06.26(금).md`
- `raw/KoreaICT/10. Python/2026.06.29(월)/2026.06.29(월).md`
