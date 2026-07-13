Python 총정리 (2026.06.19(금) ~ 2026.07.08(수))

#### \# Python 수업의 전체 흐름
Python 수업은 설치·실행 환경과 변수·문자열·연산자 같은 기초 문법에서 시작해 조건문·반복문·컬렉션으로 흐름을 제어하는 방법을 익히는 과정이었다.

그 다음 함수·람다·모듈·패키지·표준 라이브러리·객체지향을 통해 코드를 재사용 가능한 단위로 나누고, 예외 처리·파일 입출력·정규 표현식·XML·JSON으로 외부 데이터를 읽고 다루는 방법으로 확장했다.

후반부는 Jupyter Notebook에서 Pandas Series와 DataFrame을 만들고, CSV를 읽어 조회·수정·결측치 처리·통계·그래프·데이터 결합·재구조화·그룹 집계를 수행하는 데이터 분석 흐름이었다.

마지막에는 서울 공공데이터 Open API, Selenium 기반 동적 웹 수집, 지도·차트 시각화, 한국어 텍스트 마이닝을 통해 Python이 실제 데이터를 수집·정제·분석·표현하는 도구가 되는 과정을 다뤘다.


#### \# Python 개발 환경과 실행 단위
Python은 코드가 위에서 아래로 실행되는 인터프리터 언어이며, `.py` 파일 단위로 프로그램을 작성할 수 있다.

수업에서는 Python 설치 후 PyCharm으로 소스 파일을 만들고, 변수 선언·출력·입력·형 변환을 반복 실습했다. 이후 데이터 분석 구간에서는 Jupyter Notebook을 사용했다.

- PyCharm
일반 Python 파일을 프로젝트와 모듈 구조로 관리하고 실행하기에 적합한 IDE다.

- Jupyter Notebook
코드를 셀(cell) 단위로 나눠 원하는 순서에 실행하고, 코드·출력·표·그래프·설명을 한 문서에 함께 남길 수 있는 환경이다.

Jupyter에서는 `Ctrl + Enter`로 현재 셀을 실행하고, `Shift + Enter`로 실행 뒤 다음 셀로 이동한다. 데이터 분석은 중간 결과를 확인하면서 진행하므로, 한 번에 전체 프로그램을 실행하는 방식과 구분된다.


#### \# 변수, 자료형, 출력과 문자열
변수는 값을 담고 다시 참조하기 위한 이름이다. Python은 대입한 값에 따라 자료형이 정해지는 동적 타이핑 언어다.

주요 기본 자료형은 다음과 같다.

- `int`: 정수
- `float`: 실수
- `str`: 문자열
- `bool`: 참/거짓
- `None`: 값이 없음을 나타내는 객체

문자열 출력에서는 `print()`와 문자열 포맷팅을 사용했다. `%` 포맷팅, `str.format()`, f-string은 모두 값과 문장을 조합하는 방법이지만, 이후 실습에서는 f-string을 자주 사용했다.

```python
name = "홍길동"
age = 20

print("이름: %s, 나이: %d" % (name, age))
print("이름: {}, 나이: {}".format(name, age))
print(f"이름: {name}, 나이: {age}")
```

문자열은 순서가 있는 시퀀스이므로 인덱싱과 슬라이싱이 가능하다. 문자열 메서드는 원본을 직접 바꾸기보다 새 문자열을 반환하는 경우가 많으므로, 반환값을 변수에 다시 저장하는 습관이 필요하다.


#### \# 연산자, 조건문, 반복문
연산자는 값을 계산하거나 비교한다.

- 산술 연산자: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- 비교 연산자: `==`, `!=`, `>`, `<`, `>=`, `<=`
- 논리 연산자: `and`, `or`, `not`
- 대입 연산자: `=`, `+=`, `-=`, `*=`

조건문은 조건에 따라 다른 코드를 실행한다.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

반복문은 같은 규칙을 여러 데이터에 적용할 때 사용한다.

```python
numbers = [10, 20, 30]
total = 0

for number in numbers:
    total += number

print(total)
```

`range()`는 정수 범위를 표현하는 객체이며, `for`와 함께 반복 횟수를 만들 때 자주 사용한다. `while`은 조건이 참인 동안 반복하므로, 종료 조건과 `break`의 위치를 명확히 확인해야 무한 반복을 피할 수 있다.


#### \# 컬렉션: list, tuple, dict, set
Python의 컬렉션은 여러 값을 묶어 관리하는 자료구조다.

| 자료형 | 특징 | 주 사용 맥락 |
| --- | --- | --- |
| `list` | 순서 있음, 수정 가능 | 여러 값을 순차적으로 저장·수정 |
| `tuple` | 순서 있음, 수정 불가 | 변경하지 않을 묶음 데이터 |
| `dict` | key-value 쌍 | 이름으로 값을 빠르게 찾기 |
| `set` | 중복 없음, 순서 보장 목적 아님 | 중복 제거·집합 연산 |

수업에서는 리스트 인덱싱·슬라이싱, 리스트 메서드, 튜플 언패킹, 사전의 `keys()`·`values()`·`items()`를 다뤘다. 사전은 JSON과 Pandas의 열/값 구조를 이해하는 기반이 되었다.

```python
student = {
    "name": "홍길동",
    "scores": [80, 90, 100],
}

average = sum(student["scores"]) / len(student["scores"])
print(f"{student['name']}의 평균: {average}")
```

Comprehension은 반복과 조건을 짧게 표현하는 문법이다.

```python
numbers = [1, 2, 3, 4, 5]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
```

단, comprehension이 너무 길어지면 일반 `for`문보다 읽기 어려울 수 있으므로, 복잡한 로직은 단계별 코드로 나누는 편이 낫다.


#### \# 함수, 람다, 모듈, 패키지
함수는 반복되는 로직을 이름 붙여 재사용하는 단위다. 입력은 매개변수(parameter), 결과는 `return`으로 다룬다.

```python
def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(1500, 3)
print(result)
```

함수에서 중요한 구분은 다음과 같다.

- 매개변수와 인수
함수를 정의할 때 쓰는 이름이 매개변수이고, 호출할 때 전달하는 실제 값이 인수다.

- 지역 변수와 전역 변수
함수 안에서 만든 지역 변수는 기본적으로 함수 밖에서 사용할 수 없다.

- 가변 인수
`*args`는 여러 위치 인수를 튜플로 받고, `**kwargs`는 여러 키워드 인수를 사전으로 받는다.

- lambda
짧은 함수를 값처럼 전달할 때 사용하는 익명 함수다. `map()`, `filter()`, 정렬 기준 함수와 함께 사용할 수 있다.

모듈은 Python 파일 하나를 기능 단위로 만든 것이고, 패키지는 관련 모듈을 폴더 구조로 묶은 것이다. `import`는 이미 작성된 기능을 현재 프로그램에서 가져오는 방식이다.


#### \# 표준 라이브러리와 객체지향
Python 표준 라이브러리는 별도 설치 없이 쓸 수 있는 기본 도구 모음이다. 수업에서는 `os`, `random`, `datetime` 등을 사용했다.

객체지향 프로그래밍(OOP)에서는 클래스가 객체를 만들기 위한 설계도이고, 객체는 실제 데이터와 기능을 함께 가진 인스턴스다.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name}: {self.price}원")

product = Product("커피", 3000)
product.show_info()
```

`__init__`은 객체 생성 직후 실행되는 초기화 메서드이고, `self`는 현재 객체 자신의 필드와 메서드에 접근할 때 사용한다. 상속은 기존 클래스의 공통 속성·메서드를 물려받아 확장하는 방식이며, Has-A 관계는 다른 객체를 필드로 포함해 협력하는 관계다.


#### \# 예외 처리
예외(Exception)는 실행 중 발생하는 오류 상황이다. 예외 처리는 프로그램이 오류 한 번으로 즉시 종료되지 않게 하고, 오류 원인에 맞는 대응을 작성하는 방법이다.

```python
try:
    value = 10 / 0
except ZeroDivisionError as err:
    print(f"0으로 나눌 수 없습니다: {err}")
except Exception as err:
    print(f"예상하지 못한 오류: {err}")
else:
    print("예외 없이 성공했습니다.")
finally:
    print("항상 실행됩니다.")
```

- `try`: 예외가 발생할 수 있는 코드
- `except`: 특정 예외를 처리하는 코드
- `else`: 예외 없이 `try`가 끝났을 때 실행
- `finally`: 예외 발생 여부와 관계없이 항상 실행

구체적인 예외인 `IndexError`, `KeyError`, `TypeError`, `ValueError`, `ZeroDivisionError`를 먼저 처리하고, 모든 예외의 부모인 `Exception`은 마지막에 둬야 한다. `raise`는 개발자가 업무 규칙 위반을 예외로 명시할 때 사용한다.


#### \# 파일 입출력
파일 입출력은 프로그램 밖의 데이터를 읽고 결과를 저장하는 기본 작업이다.

- `r`: 읽기 모드
- `w`: 새로 쓰기 또는 기존 내용 덮어쓰기
- `a`: 파일 끝에 추가 쓰기
- `x`: 파일이 없을 때만 새 파일 생성
- `t`: 텍스트 모드
- `b`: 바이너리 모드

`with open(...)` 문은 블록이 끝날 때 파일을 자동으로 닫아 주므로, 일반적으로 `open()`과 `close()`를 직접 짝지어 쓰는 방법보다 안전하다.

```python
filename = "coffee_list.txt"
coffees = ["아메리카노", "라떼", "카푸치노"]

with open(filename, mode="w", encoding="UTF-8") as file:
    for coffee in coffees:
        file.write(f"{coffee}\n")

with open(filename, mode="r", encoding="UTF-8") as file:
    rows = [line.strip() for line in file.readlines()]

print(rows)
```

`readline()`은 한 줄, `readlines()`는 줄 목록, `read()`는 파일 전체 문자열을 반환한다. 파일에서 읽은 CSV 형태 문자열은 `split()`으로 나누고, 숫자 문자열은 `int()` 또는 `float()`으로 바꾼 뒤 계산했다.


#### \# 정규 표현식
정규 표현식(Regular Expression)은 특정 값 자체가 아니라 문자열의 패턴을 찾고 검사하는 문법이다. Python에서는 `re` 모듈을 사용한다.

```python
import re

text = "주문번호 2026, 수량 15"
pattern = re.compile(r"\d+")

print(pattern.findall(text))
```

주요 메서드는 다음과 같다.

- `match()`: 문자열 처음부터 패턴 검사
- `search()`: 문자열 전체에서 처음 발견한 패턴 검사
- `findall()`: 모든 일치 결과를 리스트로 반환
- `finditer()`: 모든 일치 결과를 반복 가능한 Match 객체로 반환

정규식에서 역슬래시를 많이 사용하므로 raw string인 `r"..."`를 쓰면 이스케이프를 줄이고 패턴을 읽기 쉽게 만들 수 있다. 이메일·전화번호·주소·파일명처럼 일정한 형식의 데이터를 추출하거나 유효성 검사를 할 때 활용한다.


#### \# XML과 JSON 데이터
XML과 JSON은 구조화된 데이터를 파일이나 API 응답으로 표현하는 대표 형식이다.

- XML
태그와 속성으로 계층 구조를 표현한다. `xml.etree.ElementTree`의 `Element`, `SubElement`, `ElementTree`, `parse()`를 사용해 XML을 만들고 읽었다.

- JSON
JavaScript Object Notation의 약자로, Python에서는 주로 `dict`, `list`, 문자열·숫자·불리언·`None`과 대응시켜 다룬다.

```python
import json

source = '{"name": "홍길동", "skills": ["Python", "Pandas"]}'
data = json.loads(source)

print(data["name"])
print(data["skills"])
```

`json.loads()`는 JSON 문자열을 Python 객체로 바꾸고, `json.load()`는 파일 객체에서 JSON을 바로 읽는다. 중첩 JSON은 사전·리스트의 키와 인덱스를 차례로 따라가며 필요한 값을 꺼낸다.


#### \# Pandas: Series와 DataFrame
Pandas는 표 형태 데이터를 다루기 위한 Python 라이브러리다.

- Series
값(value)과 색인(index)이 1:1로 대응되는 1차원 자료구조다.

- DataFrame
여러 Series가 모인 2차원 표 자료구조다. 행 index와 열 columns를 가지고 있어 데이터베이스 테이블과 비슷하게 생각할 수 있다.

```python
import pandas as pd

scores = pd.Series(
    [80, 90, 100],
    index=["국어", "영어", "수학"],
    name="점수",
)

frame = scores.to_frame()
print(frame)
```

Pandas에서는 위치(position)와 라벨(label)을 구분하는 것이 중요하다.

- `iloc`: 정수 위치 기반 조회
- `loc`: 행·열 라벨 기반 조회
- `values`: 내부 배열 값 확인
- `dtypes`: 열별 데이터 타입 확인
- `shape`, `size`, `count()`: 데이터 크기와 존재하는 값 확인

```python
frame = pd.DataFrame(
    [[10, 20], [30, 40]],
    index=["가", "나"],
    columns=["A", "B"],
)

print(frame.iloc[0, 1])
print(frame.loc["나", "A"])
```

라벨 슬라이싱은 마지막 라벨을 포함할 수 있지만, 위치 슬라이싱은 일반 Python 규칙처럼 끝 위치를 포함하지 않는다. 이 차이를 혼동하지 않아야 한다.


#### \# DataFrame 조회, 수정, 통계, 결측치
DataFrame에서는 열을 선택해 Series로 만들고, 조건식으로 행을 필터링하며, `loc`로 특정 행·열을 수정했다.

```python
result = frame.loc[frame["A"] >= 20, ["A", "B"]]
frame.loc[:, "합계"] = frame["A"] + frame["B"]
```

기본 점검과 통계에는 다음을 사용했다.

- `head()`, `info()`, `describe()`
- `min()`, `max()`, `mean()`, `median()`, `std()`, `sum()`
- `isnull()`, `notnull()`, `fillna()`, `dropna()`
- `value_counts()`, `unique()`, `isin()`, `query()`

결측치인 `NaN`은 계산 결과와 자료형에 영향을 줄 수 있다. 데이터를 분석하기 전에는 결측치가 어느 열에 얼마나 있는지 확인하고, 제거·대체·보존 중 어떤 처리가 업무적으로 맞는지 판단해야 한다.


#### \# CSV 입출력, 시각화, 데이터 결합
CSV는 표 데이터를 텍스트 파일로 저장하는 형식이다. Pandas에서는 `read_csv()`로 읽고 `to_csv()`로 저장한다. 한글 파일은 `UTF-8`과 `CP949` 같은 인코딩을 원본에 맞춰 지정해야 한다.

```python
payment = pd.read_csv("payment.csv", encoding="UTF-8")
payment.to_csv("payment_result.csv", encoding="UTF-8", index=False)
```

Matplotlib는 Pandas 결과를 선·막대·파이·산점도·히스토그램·박스플롯으로 그리는 데 사용했다. 한글이 깨지지 않도록 `Malgun Gothic` 글꼴을 지정했다.

```python
import matplotlib.pyplot as plt

plt.rc("font", family="Malgun Gothic")
chart_data = payment["식비"].value_counts()
chart_data.plot(kind="bar")
plt.title("식비 빈도")
```

여러 DataFrame을 연결할 때는 목적에 따라 방법을 구분한다.

| 기능 | 의미 | SQL과의 연결 |
| --- | --- | --- |
| `concat()` | 행 또는 열 방향으로 이어 붙이기 | UNION과 비슷한 맥락 |
| `merge()` | 공통 열 또는 index 기준으로 가로 결합 | JOIN과 비슷한 맥락 |
| `pivot()` | 긴 형식을 넓은 형식으로 변환 | 행·열 재배치 |
| `melt()` | 넓은 형식을 긴 형식으로 변환 | 분석용 정규화 형태 |
| `pivot_table()` | 그룹화·집계를 포함한 피벗 | GROUP BY + 집계와 비슷한 맥락 |


#### \# 그룹화와 범주화
`groupby()`는 같은 범주에 속한 행을 묶어 합계·평균·최댓값·최솟값·개수 같은 집계를 수행한다.

```python
summary = payment.groupby(["출장지역", "성별"])[["교통비", "출장기간"]].agg(
    ["sum", "mean"]
)
```

`transform()`은 그룹별 계산 결과를 원래 행 수에 맞춰 되돌려야 할 때 사용했다. 예를 들어 학생별·월별 첫 주 점수를 기준으로 향상 비율을 계산할 수 있다.

연속형 수치 데이터를 구간으로 나누는 범주화에는 `pd.cut()`을 사용했다. 소득처럼 연속값인 데이터를 저소득·중소득·고소득 같은 범주로 나눈 뒤, 성별·범주별 평균을 집계하고 그래프로 표현했다.


#### \# 공공데이터 Open API와 비밀값 관리
서울 열린데이터광장의 공공 자전거 데이터 실습에서는 Open API의 URL 구조, 요청 파라미터, 응답 JSON, 페이지 단위 수집을 다뤘다.

API 키처럼 환경마다 달라지고 공개하면 안 되는 값은 코드에 직접 쓰지 않고 `.env` 파일과 환경 변수로 분리했다.

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SEOUL_API_KEY")

if not api_key:
    raise ValueError("API 설정 정보가 없습니다.")
```

수집 흐름은 다음과 같다.

인증키 발급 -\> 환경 변수 로드 -\> `requests.get()` 요청 -\> JSON 응답 변환 -\> 페이지 반복 수집 -\> DataFrame 생성 -\> CSV 저장 -\> 집계·시각화

공공 자전거 대여소·실시간 대여·일별 이용 데이터를 읽은 뒤, 컬럼 이름을 이해하기 쉬운 한글로 바꾸고, 문자열·성별·연령대 값을 전처리한 뒤 `merge()`와 `groupby()`로 분석했다.


#### \# 웹 크롤링, 지오코딩, 지도 시각화
정적 HTML은 BeautifulSoup으로 파싱할 수 있지만, 클릭·화면 이동처럼 브라우저 동작이 필요한 동적 데이터는 Selenium을 사용했다.

수업에서는 Selenium WebDriver로 커피 매장 페이지를 열고, CSS selector로 지역을 선택하며, `page_source`를 BeautifulSoup으로 파싱해 매장명·주소·좌표 정보를 DataFrame으로 만들었다.

주소만 있고 좌표가 없을 때는 지오코딩 API로 위도·경도를 얻었다. 이 API 키도 `.env`로 분리해야 한다.

Folium은 좌표 데이터를 지도에 표시하는 라이브러리다. Marker, MarkerCluster, GeoJSON 경계, HeatMap을 사용해 대여소·커피 매장 같은 위치 데이터를 지도 위에 표현했다.


#### \# 텍스트 마이닝
텍스트 마이닝 실습에서는 한국어 문장에서 의미 있는 단어를 추출하고 빈도를 계산해 표·그래프·워드클라우드로 표현했다.

- KoNLPy와 Komoran
한국어 형태소 분석을 수행한다. 사용자 사전으로 특정 단어를 하나의 형태소로 인식하도록 보정할 수 있다.

- NLTK
단어 빈도 계산과 텍스트 처리에 사용했다.

- 불용어(stopword)
자주 나오지만 분석에 큰 의미가 없는 단어를 제거하는 목록이다.

- WordCloud
단어별 빈도수를 시각적 크기로 표현한다.

텍스트 마이닝 흐름은 다음과 같다.

텍스트 파일 읽기 -\> 형태소 분석 -\> 명사 추출 -\> 불용어 제거 -\> 빈도 계산 -\> DataFrame·CSV 저장 -\> 막대 그래프·워드클라우드 생성

KoNLPy는 Java JVM을 사용하므로 실행 환경에서 Java 경로와 관련 라이브러리 설치 상태를 함께 확인해야 한다.


#### \# Python 수업을 다시 연결하기
Python 수업의 핵심 흐름은 다음과 같이 이어진다.

기본문법·컬렉션 -\> 함수·객체지향 -\> 예외 처리·파일 입출력 -\> 정규 표현식·XML·JSON -\> Pandas 표 데이터 -\> 집계·시각화 -\> API·크롤링·지도·텍스트 마이닝

초반 문법은 단순한 출력 연습으로 끝나지 않는다. 리스트·사전·함수·예외 처리는 JSON 응답과 CSV 행을 처리하는 기반이 되고, 파일 입출력은 Pandas의 CSV 처리와 연결된다. Pandas의 `merge`, `groupby`, `pivot_table`은 Oracle SQL에서 배운 JOIN·GROUP BY·집계와 연결해서 이해할 수 있다.

마지막 실습들은 Python이 단순 알고리즘 학습 언어가 아니라, 외부 API와 웹에서 데이터를 가져와 비밀값을 안전하게 관리하고, 정제·분석·시각화 결과를 만들어 내는 실무 도구라는 점을 보여준다.
