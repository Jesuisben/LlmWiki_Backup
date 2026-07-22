---
title: Java 인간용 통합 총정리
created: 2026-07-22
updated: 2026-07-22
type: study-guide
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/2026.02.26(목) - 시작/2026.02.26(목) - 시작.md
  - raw/KoreaICT/1. Java/2026.02.27(금)/2026.02.27(금).md
  - raw/KoreaICT/1. Java/2026.03.03(화)/2026.03.03(화).md
  - raw/KoreaICT/1. Java/2026.03.04(수)/2026.03.04(수).md
  - raw/KoreaICT/1. Java/2026.03.05(목)/2026.03.05(목).md
  - raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/KoreaICT/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/2026.03.13(금)/2026.03.13(금).md
  - raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
status: stable
confidence: high
---

# Java 인간용 통합 총정리

## 이 파일의 목적

이 파일은 **“Java에서 무엇을 배웠더라?”라는 생각이 들었을 때 다른 페이지를 열지 않고 과목 전체를 처음부터 끝까지 복습하기 위한 주 교재**다.

- 수업 기간: 2026-02-26 ~ 2026-03-13
- 중심 흐름: 실행 구조 → 변수와 타입 → 연산자 → 조건·반복 → 배열 → 클래스·객체 → 생성자·상속 → 다형성 → 추상 클래스·인터페이스 → `static`·`final`
- 아래 코드는 원본 전체를 복사한 것이 아니라 수업에서 배운 문법을 짧게 되살리기 위한 **복습용 재구성 예제**다.
- 날짜별 세부 흐름이나 원본 코드 전체가 필요할 때만 마지막의 Wiki·Raw 링크를 이용한다.

### 이 파일을 읽는 방법

이 교재는 이미 Java를 아는 사람을 위한 요약표가 아니다. Java를 처음 보는 사람도 앞에서 배운 말만 이용해 다음 절로 넘어갈 수 있도록 작성한다.

1. 각 장의 **왜 필요한가**를 먼저 읽는다.
2. 문법 표에서 낯선 용어를 확인한다.
3. 예제의 **입력 → 처리 → 출력**을 손으로 따라간다.
4. `실행 흐름`과 `자주 하는 실수`를 말로 설명한다.
5. 장 끝의 확인 문제를 코드 없이 먼저 답한 뒤 직접 작성한다.

코드 블록은 두 종류로 구분한다.

- **완전 예제:** 클래스와 `main`을 포함해 별도 파일로 실행할 수 있다.
- **문법 조각:** 특정 문법만 보여 주기 위한 일부 코드다. 주변 클래스나 변수가 생략되어 단독 실행 대상이 아니다.

### 이 교재에서 말하는 “Java 전체”의 범위

여기서 전체는 Java 언어의 모든 기능이 아니라 **2026-02-26부터 2026-03-13까지 실제로 배운 범위 전체**다.

| 구분 | 이 파일에서 다루는 방식 |
|---|---|
| 날짜별 직접 수업 | 본문에서 원리·예제·출력·오류까지 설명 |
| 클래스 숙제에서 복습한 내용 | 직접 수업과 겹치는 부분은 본문에 통합 |
| 숙제에서 조사만 한 메모리·컬렉션·제네릭 | 직접 실습처럼 과장하지 않고 경계만 설명 |
| Java 팀 프로젝트 | 원본에 주제·코드·결과가 없어 수행·코드 검토 사실만 기록 |
| Oracle·Spring으로의 연결 | Java에서 배운 내용이 이후 어디에 쓰이는지만 안내 |

따라서 이 파일만 읽어도 수업 범위는 이해할 수 있어야 하지만, 수업에서 배우지 않은 예외 처리, 파일 입출력, 컬렉션 구현, 제네릭 구현, 람다, 스트림 등을 새 수업 내용처럼 추가하지 않는다.

## 5분 전체 지도

| 단계 | 배운 것 | 다음 단계와의 연결 |
|---|---|---|
| 실행 준비 | 프로젝트·패키지·클래스·`main`·출력 | Java 프로그램이 어디서 시작하는지 이해 |
| 값 다루기 | 변수·자료형·대입·형변환·연산자·입력 | 조건식과 계산식을 만들 수 있음 |
| 흐름 제어 | `if`, `switch`, `for`, `while`, `break` | 반복되는 문제를 자동 처리 |
| 여러 값 묶기 | 배열·인덱스·향상된 `for`·객체 배열 | 여러 객체를 한꺼번에 관리 |
| 객체 설계 | 클래스·필드·메서드·생성자·캡슐화 | 현실의 대상을 Java 타입으로 표현 |
| 객체 확장 | 상속·`super`·오버라이딩·다형성 | 공통 코드와 서로 다른 동작을 함께 설계 |
| 규격과 공유 | 추상 클래스·인터페이스·`static`·`final` | Spring의 계층·DI·Entity/DTO를 배우는 기반 |

---

## 1. Java 프로그램의 기본 구조

### 프로젝트 → 패키지 → 클래스

Java 수업은 IntelliJ에서 프로젝트를 만들고, 그 안에 패키지와 클래스를 만드는 것부터 시작했다.

- **프로젝트(Project):** 프로그램 전체 작업 단위
- **패키지(Package):** 관련 클래스를 묶는 이름 공간
- **클래스(Class):** 필드와 메서드를 담는 사용자 정의 타입이자 코드 단위
- **`main` 메서드:** 일반 Java 프로그램의 출발점
- **세미콜론 `;`:** 문장의 끝에 붙지만 클래스·메서드의 중괄호 뒤에는 보통 붙이지 않음
- Java는 공백과 줄바꿈보다 중괄호와 세미콜론으로 구조를 판단한다.
- 클래스 이름은 보통 대문자로 시작하고, 변수·메서드 이름은 소문자로 시작한다.

### 첫 프로그램

```java
public class HelloJava {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}
```

`main` 안의 문장이 위에서 아래로 실행된다. `System.out.println()`은 출력 후 줄을 바꾼다.

#### 첫 프로그램을 한 줄씩 읽기

| 코드 | 뜻 |
|---|---|
| `public class HelloJava` | `HelloJava`라는 공개 클래스를 정의한다. 파일 이름도 보통 `HelloJava.java`로 맞춘다. |
| `{ ... }` | 클래스나 메서드가 차지하는 본문 범위를 표시한다. |
| `public static void main(String[] args)` | Java가 프로그램 시작점으로 찾는 메서드다. 지금은 이 형태를 하나의 시작 약속으로 기억한다. |
| `System.out` | Java가 기본으로 제공하는 출력 통로다. |
| `println(...)` | 괄호 안의 값을 출력하고 다음 줄로 이동한다. |

Java가 위에서 아무 문장이나 실행하는 것이 아니라 클래스를 읽고 시작점인 `main`을 찾아 그 안의 문장을 순서대로 실행한다고 이해한다. `main` 밖에는 필드나 다른 메서드를 정의할 수 있지만 일반 실행문을 아무 위치에나 둘 수는 없다.

### 주석과 출력

| 문법 | 의미 |
|---|---|
| `// 설명` | 한 줄 주석 |
| `/* 설명 */` | 여러 줄 주석 |
| `System.out.print()` | 출력 후 줄바꿈 없음 |
| `System.out.println()` | 출력 후 줄바꿈 |
| `System.out.printf()` | `%d`, `%f`, `%s`, `%c` 등을 사용한 형식 지정 출력 |
| `\n` | 문자열 안의 줄바꿈 escape sequence |

```java
String name = "홍길동";
int age = 29;
double average = 74.6666;

System.out.printf("이름: %s%n나이: %d%n평균: %.2f%n", name, age, average);
```

예상 출력:

```text
이름: 홍길동
나이: 29
평균: 74.67
```

- `%s` 자리에 `name`, `%d` 자리에 `age`, `%.2f` 자리에 `average`가 순서대로 들어간다.
- `%.2f`는 실수를 소수점 둘째 자리까지 표시하며 다음 자리에서 반올림한다.
- `%n`과 `\n`은 모두 줄바꿈에 쓰인다. 수업에서는 `\n`을 escape sequence로 배웠고, 재구성 예제에서는 운영체제에 맞는 줄바꿈인 `%n`도 함께 사용한다.
- `printf`는 형식 문자열에 줄바꿈을 넣지 않으면 다음 출력이 같은 줄에 이어질 수 있다.

#### 출력 확인 문제

```java
System.out.print("A");
System.out.println("B");
System.out.printf("%s%n", "C");
```

첫 문장은 줄을 바꾸지 않으므로 첫 줄은 `AB`, 두 번째 줄은 `C`가 된다. 코드를 실행하기 전에 몇 줄이 출력될지 먼저 예상하는 습관을 들인다.

### 수업에서 사용한 IntelliJ 단축키

- 설정: `Ctrl + Alt + S`
- 한 줄 복사: `Ctrl + D`
- 코드 자동 정렬: `Ctrl + Alt + L`
- 찾기·바꾸기: `Ctrl + R`
- 이름 변경 refactoring: `Shift + F6`
- 생성 메뉴: `Alt + Insert`

이 단축키는 Java 문법은 아니지만 클래스·생성자·getter/setter를 작성할 때 반복해서 사용한 개발 환경 지식이다.

---

## 2. 변수와 자료형

### 변수의 의미

변수는 값을 저장하는 이름 붙은 공간이다.

```java
int age;       // 선언
age = 29;      // 대입
age = 30;      // 기존 값을 덮어씀
```

`=`는 수학의 “같다”가 아니라 **오른쪽 값을 왼쪽 변수에 저장하는 대입 연산자**다.

```java
int x = 3;
int y = 5;
int sum = x + y;
```

마지막 줄에서는 `x`, `y`의 값을 읽고, 계산 결과를 `sum`에 쓴다. 같은 범위에서 이미 선언한 변수의 타입을 다시 선언하거나 다른 타입으로 바꿀 수는 없다.

### 수업에서 중심적으로 사용한 자료형

| 자료형 | 저장 대상 | 예시 | 구분 |
|---|---|---|---|
| `char` | 문자 한 개 | `'A'` | 기본형 |
| `int` | 정수 | `29` | 기본형 |
| `double` | 실수 | `3.14` | 기본형 |
| `boolean` | 참·거짓 | `true` | 기본형 |
| `String` | 문자열 | `"Java"` | 참조형 객체 |

`byte`, `short`, `long`, `float`도 있다는 사실은 확인했지만 입문 실습의 중심은 아니었다. `String`은 자주 사용해 기본처럼 보이지만 실제로는 클래스에 기반한 참조 자료형이다.

### 값, 리터럴, 변수, 타입을 구분하기

```java
int age = 29;
String name = "홍길동";
```

- `int`, `String`: 어떤 종류의 값을 다룰지 정하는 **타입(type)**
- `age`, `name`: 값을 다시 사용하기 위해 붙인 **변수 이름(identifier)**
- `29`, `"홍길동"`: 코드에 직접 적은 **리터럴(literal)**
- `=`: 오른쪽 값을 왼쪽 저장공간에 넣는 **대입 연산자**

문자 하나는 작은따옴표, 문자열은 큰따옴표를 사용한다.

```java
char grade = 'A';
String course = "Java";
```

`'A'`와 `"A"`는 모양이 비슷해도 각각 `char`와 `String`으로 타입이 다르다.

### 필드·배열 요소와 지역 변수의 기본값

수업에서 `new int[3]`의 칸이 `0`으로 채워지고 객체 필드에 기본값이 생기는 것을 확인했다. 그러나 모든 변수가 자동 초기화되는 것은 아니다.

| 위치 | 자동 기본값 |
|---|---|
| 객체의 필드 | 있음: 숫자 `0`/`0.0`, `boolean`은 `false`, 참조형은 `null` |
| 배열 요소 | 있음: 요소 타입에 맞는 기본값 |
| 메서드 안의 지역 변수 | 없음: 사용 전에 직접 값을 넣어야 함 |

```java
int local;
// System.out.println(local); // 컴파일 오류: 지역 변수 local이 초기화되지 않음

int[] numbers = new int[1];
System.out.println(numbers[0]); // 0
```

### 식별자 규칙

- 첫 글자는 영문자, `_`, `$`로 시작할 수 있다.
- 숫자로 시작할 수 없다.
- 공백과 일반 특수문자를 사용할 수 없다.
- Java 예약어를 변수명으로 사용할 수 없다.
- 의미를 알 수 있는 이름을 쓰는 것이 좋다.

### 형변환(Casting)

**암시적 형변환**은 더 넓은 표현 범위로 이동할 때 Java가 자동 처리한다.

```java
double value = 100;   // int 100이 double 100.0으로 변환
```

**명시적 형변환**은 값 손실 가능성이 있을 때 개발자가 직접 지시한다.

```java
double value = 3.9;
int number = (int) value;   // 3, 소수 부분 손실
```

정수 나눗셈은 계산 시점이 중요하다.

```java
System.out.println(14 / 5);           // 2
System.out.println((double) 14 / 5);  // 2.8
System.out.println((double) (14 / 5)); // 2.0
```

`char`는 문자이지만 비교·계산 문맥에서는 문자 코드의 숫자값으로 다뤄질 수 있다.

```java
char first = 'c';
char second = 'a';

boolean greater = first > second; // 문자 코드 99 > 97
int result = first - second + 5;  // 99 - 97 + 5

System.out.println(greater); // true
System.out.println(result);  // 7
```

수업에서는 `A`가 65, `a`가 97, `0`이 48이라는 문자 코드 예를 이용했다. 핵심은 문자가 영구히 `int`로 바뀐다는 뜻이 아니라 **비교·계산하는 순간 숫자값으로 승격되어 연산에 참여한다**는 점이다.

---

## 3. 연산자

### 연산자 종류

| 종류 | 문법 | 역할 |
|---|---|---|
| 산술 | `+ - * / %` | 계산 |
| 대입 | `=` | 오른쪽 값을 왼쪽에 저장 |
| 복합 대입 | `+= -= *= /=` | 계산과 대입을 함께 수행 |
| 증감 | `++ --` | 값을 1 증가·감소 |
| 비교 | `< <= > >= == !=` | 비교 결과를 `boolean`으로 만듦 |
| 논리 | `! && \|\|` | 조건을 부정하거나 결합 |
| 삼항 | `조건 ? 참값 : 거짓값` | 값 하나를 조건에 따라 선택 |

```java
int a = 3;
int b = 5;
int difference = a >= b ? a - b : b - a;
```

### 연산 결과를 손으로 추적하기

```java
int age = 1;
int before = age++;
int after = ++age;
```

1. `before = age++`는 현재 값 `1`을 `before`에 넣은 뒤 `age`를 `2`로 만든다.
2. `after = ++age`는 `age`를 먼저 `3`으로 만든 뒤 그 값을 `after`에 넣는다.
3. 최종값은 `before == 1`, `age == 3`, `after == 3`이다.

단독 문장 `age++;`에서는 전위·후위 차이가 결과에 드러나지 않지만, 다른 대입식 안에서는 증가 시점이 다르다.

### 논리 연산자의 진리표

| A | B | `A && B` | `A \|\| B` |
|---|---|---|---|
| `true` | `true` | `true` | `true` |
| `true` | `false` | `false` | `true` |
| `false` | `true` | `false` | `true` |
| `false` | `false` | `false` | `false` |

`!A`는 A의 값을 반대로 바꾼다. 예를 들어 `!(age >= 20)`은 “20세 이상이 아니다”라는 뜻이다.

### 연산자 우선순위와 괄호

수업에서는 단항 → 산술 → 관계 → 논리 → 조건 → 대입의 큰 순서를 확인했다. 모든 순서를 암기해 복잡한 식을 만드는 것보다 괄호로 계산 의도를 드러내는 편이 안전하다.

```java
boolean canEnter = (age >= 20) && (hasTicket || isStaff);
```

이 식은 “20세 이상”이면서 “표가 있거나 직원”인 경우다. `age`, `hasTicket`, `isStaff`가 이미 선언된 상황을 보여 주는 문법 조각이다.

### 자주 틀리는 부분

- `=`는 대입, `==`는 값 비교다.
- `&&`는 양쪽이 모두 참이어야 참이다.
- `||`는 하나라도 참이면 참이다.
- `!`는 참·거짓을 반대로 바꾼다.
- `age++`와 `++age`는 단독 문장에서는 모두 1 증가하지만 다른 식 안에서는 증가 시점이 다르다.
- 복잡한 우선순위를 외우기보다 괄호로 의도를 명확히 쓰는 편이 안전하다.

---

## 4. 입력과 조건문

### `Scanner` 입력

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("점수: ");
        int score = scanner.nextInt();

        if (score >= 60) {
            System.out.println("합격");
        } else {
            System.out.println("불합격");
        }
    }
}
```

#### `Scanner` 생성식을 분해해서 읽기

```java
Scanner scanner = new Scanner(System.in);
```

| 부분 | 의미 |
|---|---|
| `Scanner` | 입력 기능을 제공하는 클래스이자 변수의 타입 |
| `scanner` | 앞으로 입력 객체를 부를 변수 이름 |
| `new` | 메모리에 새 객체를 생성하라는 연산자 |
| `Scanner(...)` | 객체를 초기화하는 생성자 호출 |
| `System.in` | 키보드에서 들어오는 표준 입력 통로 |

`import java.util.Scanner;`는 `package` 아래, 클래스 선언 위에 둔다. `import`는 객체를 만드는 명령이 아니라 다른 패키지에 있는 `Scanner`라는 클래스 이름을 현재 파일에서 사용할 수 있게 한다.

- `next()`는 공백 전까지 읽는다.
- `nextLine()`은 한 줄 전체를 읽는다.
- `nextInt()`, `nextDouble()`은 숫자를 읽는다.
- 숫자 입력 뒤 `nextLine()`을 바로 사용하면 남아 있는 줄바꿈 때문에 예상과 다르게 동작할 수 있다.

#### `next()`와 `nextLine()`의 실제 차이

- `next()`는 공백 전까지의 토큰 하나만 읽는다. `홍 길동`을 입력하면 첫 호출은 `홍`까지만 가져온다.
- `nextLine()`은 Enter를 누르기 전까지 한 줄 전체를 읽는다.
- `nextInt()`는 숫자만 읽고 Enter에 해당하는 줄바꿈은 입력 통로에 남길 수 있다.

숫자 뒤에 한 줄 문자열을 받을 때는 남은 줄바꿈을 한 번 소비한다.

```java
System.out.print("나이: ");
int age = scanner.nextInt();
scanner.nextLine(); // 숫자 뒤에 남은 줄바꿈 소비

System.out.print("이름 전체: ");
String fullName = scanner.nextLine();
```

#### 입력 프로그램을 읽는 순서

1. 입력 도구를 `import`한다.
2. `new Scanner(System.in)`으로 입력 객체를 한 번 만든다.
3. 사용자에게 무엇을 입력할지 먼저 출력한다.
4. 입력 메서드로 값을 읽어 타입이 맞는 변수에 저장한다.
5. 저장한 값을 조건식·계산식·배열 처리에 사용한다.

### 조건문 선택 기준

| 문법 | 적합한 상황 |
|---|---|
| `if` | 조건 하나를 검사 |
| `if ~ else` | 두 경우 중 하나를 선택 |
| `else if` | 범위나 복합 조건을 여러 단계로 검사 |
| `switch` | 하나의 값에 대한 여러 정확한 경우를 분기 |
| 삼항 연산자 | 조건에 따라 값 하나를 간단히 선택 |

```java
int score = 85;

if (score >= 90) {
    System.out.println("A");
} else if (score >= 80) {
    System.out.println("B");
} else {
    System.out.println("C 이하");
}
```

조건의 순서도 중요하다. 위 예제에서 `score >= 80`을 먼저 검사하면 90점도 그 조건에서 끝나므로 더 좁거나 높은 기준부터 검사해야 한다.

### `switch`와 `break`

`switch`는 하나의 값이 여러 정확한 후보 중 어디에 해당하는지 검사할 때 편하다.

```java
int month = 3;

switch (month) {
    case 3:
    case 4:
    case 5:
        System.out.println("봄");
        break;
    case 6:
    case 7:
    case 8:
        System.out.println("여름");
        break;
    default:
        System.out.println("다른 계절 범위");
}
```

- 여러 `case`를 연달아 쓰면 여러 값이 같은 실행문으로 합류할 수 있다.
- `break`가 없으면 일치한 `case` 아래의 실행문까지 계속 내려가는 **fall-through**가 발생한다.
- `default`는 어떤 `case`에도 맞지 않을 때 실행되며 `if`문의 마지막 `else`와 비슷한 역할을 한다.

### 조건문 확인 문제

- 범위 비교가 필요하면 `if`, 하나의 값에 대한 정확한 후보 분기라면 `switch`가 자연스럽다.
- `=`를 조건에 쓰려 하지 말고 값 비교에는 `==`를 사용한다.
- 문자열 비교의 심화 규칙은 이 수업의 핵심 범위가 아니므로 여기서는 숫자·문자·논리 조건을 중심으로 연습한다.

---

## 5. 반복문과 보조 제어문

### `for`와 `while`

- **`for`:** 반복 횟수나 제어 변수의 변화가 비교적 명확할 때
- **`while`:** 입력·상태에 따라 종료 시점이 달라질 때
- **`break`:** 반복문을 즉시 종료
- **`continue`:** 현재 반복의 나머지를 건너뛰고 다음 반복으로 이동

```java
int sum = 0;

for (int i = 1; i <= 10; i++) {
    sum += i;
}

System.out.println(sum); // 55
```

```java
int number = 1;

while (true) {
    System.out.println(number);
    if (number == 3) {
        break;
    }
    number++;
}
```

수업의 반복 실습은 주로 **초기값 → 조건식 → 실행 → 값 변경 → 종료** 흐름과 합계·홀짝 누적을 익히는 데 목적이 있었다.

### `for` 실행 순서를 정확히 읽기

```java
for (int i = 1; i <= 3; i++) {
    System.out.println(i);
}
```

1. `int i = 1`: 반복 시작 전에 한 번만 실행한다.
2. `i <= 3`: 참인지 검사한다.
3. 본문에서 현재 `i`를 출력한다.
4. `i++`: 본문이 끝난 뒤 실행한다.
5. 다시 조건식으로 돌아간다.
6. `i`가 `4`가 되면 조건이 거짓이므로 종료한다.

예상 출력은 `1`, `2`, `3` 세 줄이다. 배열을 순회할 때는 같은 원리로 `i = 0`부터 `i < array.length`까지 진행한다.

### `while`과 무한 반복

`while`은 조건을 먼저 검사한다. 입력값에 따라 끝나는 시점이 달라질 때 조건을 직접 관리한다.

```java
int total = 0;
int number = 1;

while (number <= 5) {
    total += number;
    number++;
}

System.out.println(total); // 15
```

`while (true)`는 조건이 항상 참이므로 내부에서 `break`에 도달하지 못하면 끝나지 않는다. 종료 조건을 먼저 설계하고 무한 반복을 사용한다.

#### 음수 입력으로 끝나는 점수 평균 패턴

수업에서는 점수를 몇 개 입력할지 미리 정하지 않고 음수를 종료 신호로 사용하는 흐름도 연습했다.

```java
int total = 0;
int count = 0;

while (true) {
    int score = scanner.nextInt();

    if (score < 0) {
        break;
    }

    total += score;
    count++;
}

double average = (double) total / count;
```

`scanner`가 이미 만들어졌다고 가정한 문법 조각이다. 종료 신호인 음수는 합계와 개수에 포함하지 않으므로 `break` 판정을 누적보다 먼저 한다. 평균을 계산할 때는 정수 나눗셈이 먼저 일어나지 않도록 `(double) total`로 변환한다. 입력이 처음부터 음수라면 `count == 0`이므로 실제 프로그램에서는 0으로 나누지 않도록 별도 조건도 필요하다.

### 직접 학습 범위의 경계

- `break`는 `switch`나 반복문을 즉시 끝내는 용도로 직접 사용했다.
- `do-while`과 `continue`는 원본에 “안 배움”으로 표시되어 있으므로 문법 이름만 알고 직접 수업 범위로 확대하지 않는다.

### 중첩과 향상된 `for`

반복문 안에 조건문을 넣어 홀수·짝수를 나누거나, 반복문 안에 반복문을 넣어 표 형태의 문제를 처리할 수 있다.

```java
int[] scores = {80, 90, 70};
int total = 0;

for (int score : scores) {
    total += score;
}
```

향상된 `for`는 배열의 모든 값을 순서대로 읽을 때 편하지만, 현재 인덱스가 필요하거나 특정 칸을 직접 바꿔야 할 때는 일반 `for`가 더 적합하다.

### 반복문 확인 문제

- 1부터 10까지의 합계를 구할 때 누적 변수는 반복문 **밖에서** `0`으로 준비해야 한다.
- 반복문 안에서 누적 변수를 다시 `0`으로 만들면 이전 반복의 결과가 사라진다.
- 증감식을 빠뜨린 `while`은 조건이 계속 참으로 남아 무한 반복이 될 수 있다.
- 배열의 모든 값만 읽으면 향상된 `for`, 인덱스 출력·특정 칸 수정이 필요하면 일반 `for`를 선택한다.

---

## 6. 배열

### 배열의 핵심

배열은 **같은 타입의 여러 값을 고정된 길이로 묶는 자료구조**다.

- 인덱스는 `0`부터 시작한다.
- 마지막 인덱스는 `length - 1`이다.
- 생성 후 길이를 바꿀 수 없다.
- 존재하지 않는 인덱스에 접근하면 오류가 난다.

### 생성 방법 두 가지

```java
int[] scores = new int[3];
scores[0] = 80;
scores[1] = 90;
scores[2] = 70;
```

```java
int[] scores = {80, 90, 70};
```

첫 번째는 요소 개수만 먼저 정할 때, 두 번째는 값이 이미 명확할 때 편하다.

### 기본값

배열을 `new`로 만들면 타입별 기본값이 들어간다.

- 정수형: `0`
- 실수형: `0.0`
- 논리형: `false`
- 참조형: `null`

### 객체 배열

```java
Product[] products = {
    new Product("키보드", 30000),
    new Product("마우스", 20000)
};

for (Product product : products) {
    System.out.println(product.getName());
}
```

객체 배열의 각 칸에는 객체 자체가 통째로 들어간다기보다 객체를 가리키는 참조가 들어간다고 이해하는 편이 정확하다.

### 입력·배열·반복·조건·누적을 하나로 연결하기

다음은 수업의 홀수·짝수 누적 문제를 초심자가 한 흐름으로 읽을 수 있게 재구성한 완전 예제다.

```java
import java.util.Scanner;

public class EvenOddTotals {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("정수 개수: ");
        int size = scanner.nextInt();
        int[] numbers = new int[size];

        int oddTotal = 0;
        int evenTotal = 0;

        for (int i = 0; i < numbers.length; i++) {
            System.out.print(i + "번째 정수: ");
            numbers[i] = scanner.nextInt();

            if (numbers[i] % 2 == 0) {
                evenTotal += numbers[i];
            } else {
                oddTotal += numbers[i];
            }
        }

        System.out.println("홀수 합계: " + oddTotal);
        System.out.println("짝수 합계: " + evenTotal);
    }
}
```

입력이 `4`, `5`, `3`, `4`, `8` 순서라면 배열은 `{5, 3, 4, 8}`이 되고 홀수 합계는 `8`, 짝수 합계는 `12`다.

#### 실행 흐름

1. 먼저 사용자가 입력한 `size`로 배열의 길이를 정한다.
2. 반복마다 입력값을 `numbers[i]`에 저장한다.
3. `% 2`의 나머지로 홀수·짝수를 판정한다.
4. 홀수와 짝수 누적 변수 중 하나에 현재 값을 더한다.
5. 반복이 끝난 뒤 최종 합계를 한 번 출력한다.

#### 자주 하는 실수

- `i <= numbers.length`라고 쓰면 마지막에 존재하지 않는 인덱스에 접근한다. `<`를 사용한다.
- `oddTotal`과 `evenTotal`을 반복문 안에서 선언하면 매번 다시 만들어져 누적되지 않는다.
- 배열 생성 전에는 길이가 필요하다. 길이를 모르는 상태에서 `new int[]`만 작성할 수는 없다.
- `numbers[i] % 2 == 1`은 이 수업의 양수 입력에서는 동작하지만, 짝수 판정 `== 0`을 먼저 쓰면 음수까지 포함해 더 안정적으로 홀짝을 나눌 수 있다.

### 배열과 컬렉션의 경계

Java 수업에서는 배열이 중심이었다. `List`, `Set`, `Map`, generic, FIFO(선입선출), LIFO(후입선출)는 숙제·사전조사에서 접했지만 이 기간의 핵심 실습 범위로 과장하지 않는다. 배열은 길이가 고정되고, 컬렉션은 이후 여러 객체를 더 유연하게 관리할 때 사용한다.

---

## 7. 클래스와 객체

### 정의

- **클래스:** 객체를 만들기 위한 사용자 정의 타입·설계도
- **객체:** 클래스를 바탕으로 `new`를 통해 생성된 실제 사용 단위
- **참조 변수:** 생성된 객체의 위치를 가리키는 변수

```java
Product product = new Product("노트북", 1200000);
```

`Product`는 타입, `product`는 참조 변수, `new Product(...)`는 객체 생성이다.

#### 클래스에서 객체까지 네 단계

1. **업무 파악:** 상품에 이름과 가격이 필요하고 정보를 출력해야 한다고 정한다.
2. **클래스 정의:** 필드와 메서드로 `Product` 타입을 만든다.
3. **객체 생성:** `new Product(...)`로 실제 상품 하나를 만든다.
4. **멤버 사용:** 참조 변수 뒤에 점(`.`)을 붙여 객체의 공개 메서드를 호출한다.

```java
Product keyboard = new Product("키보드", 30000);
keyboard.printInfo();
```

점(`.`)은 **멤버 참조 연산자**다. `keyboard.printInfo()`는 “`keyboard`가 가리키는 객체 안에서 `printInfo` 메서드를 찾아 실행하라”는 뜻이다.

같은 클래스로 객체를 여러 개 만들면 각 객체는 같은 구조를 사용하지만 서로 다른 상태를 가질 수 있다.

```java
Product keyboard = new Product("키보드", 30000);
Product mouse = new Product("마우스", 20000);
```

두 참조 변수의 타입은 모두 `Product`지만 서로 다른 `new Product(...)` 결과를 가리킨다.

### 클래스의 구성 요소

| 구성 | 의미 | 예시 |
|---|---|---|
| 필드(field) | 객체의 상태 | 상품명, 가격 |
| 메서드(method) | 객체의 동작 | 가격 출력, 가격 변경 |
| 생성자(constructor) | 객체 생성 시 초기값 설정 | 이름·가격을 받아 저장 |

### 하나로 묶어 보기

```java
public class Product {
    private String name;
    private int price;

    public Product() {
    }

    public Product(String name, int price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setPrice(int price) {
        if (price >= 0) {
            this.price = price;
        }
    }

    public int getPrice() {
        return price;
    }

    public void printInfo() {
        System.out.printf("%s: %d원%n", name, price);
    }
}
```

```java
public class ProductMain {
    public static void main(String[] args) {
        Product product = new Product("키보드", 30000);
        product.setPrice(28000);
        product.printInfo();
    }
}
```

### 메서드

메서드는 입력(parameter)을 받아 처리하고 결과를 반환하거나 객체의 상태를 변경한다.

```java
public int add(int a, int b) {
    return a + b;
}
```

- `void`: 반환값이 없음
- `return`: 값을 호출한 곳으로 돌려줌
- 매개변수(parameter): 메서드 정의에서 받는 변수
- 인수(argument): 호출할 때 실제로 전달하는 값

#### 메서드 호출에서 값이 이동하는 과정

```java
public int plus5(int x) {
    return x + 5;
}
```

```java
int result = product.plus5(3);
```

주변 클래스가 생략된 문법 조각이며 실행 순서는 다음과 같다.

1. 호출하는 쪽에서 인수 `3`을 보낸다.
2. 메서드의 매개변수 `x`가 `3`을 받는다.
3. 본문이 `x + 5`를 계산해 `8`을 만든다.
4. `return`이 `8`을 호출 위치로 돌려준다.
5. 호출식 `product.plus5(3)` 전체가 값 `8`처럼 동작한다.
6. 대입 연산자가 결과를 `result`에 저장한다.

`void` 메서드는 반환값이 없지만 **아무 일도 하지 않는다는 뜻은 아니다**. 출력하거나 객체 상태를 변경할 수 있다.

```java
public void printInfo() {
    System.out.println(name + ": " + price + "원");
}
```

`product.printInfo();`는 동작을 실행할 수 있지만 반환값이 없으므로 `int result = product.printInfo();`처럼 값으로 저장할 수 없다.

#### 매개변수와 인수를 헷갈리지 않기

| 위치 | 이름 | 예시 |
|---|---|---|
| 메서드를 정의하는 쪽 | 매개변수(parameter) | `int x` |
| 메서드를 호출하는 쪽 | 인수(argument) | `3` |

호출할 때 `plus5(int 3)`처럼 쓰지 않는다. `int x`는 메서드 안에서 값을 받을 변수 선언이고, 호출할 때는 실제 값이나 이미 선언된 변수를 전달한다.

### 생성자와 `this`

생성자는 클래스 이름과 같고 반환형을 쓰지 않는다. 객체 생성 시 한 번 호출된다.

`this.name = name;`에서 `this.name`은 현재 객체의 필드이고, 오른쪽 `name`은 생성자가 받은 매개변수다.

### 오버로딩

같은 클래스에서 메서드나 생성자의 이름은 같지만 **매개변수의 개수·타입·순서**를 다르게 여러 개 정의하는 것이다.

```java
public Product() {
}

public Product(String name) {
    this.name = name;
}

public Product(String name, int price) {
    this.name = name;
    this.price = price;
}
```

반환형만 바꾸는 것은 오버로딩이 아니다.

### 기본 생성자 주의

생성자를 하나도 작성하지 않으면 Java가 매개변수 없는 기본 생성자를 제공한다. 그러나 생성자를 하나라도 직접 작성하면 자동 기본 생성자는 제공되지 않는다. 상속에서 자식 생성자가 암묵적으로 `super()`를 호출할 때 부모의 기본 생성자가 없으면 오류가 발생한다.

### 생성자·메서드·필드 초기화 비교

| 구분 | 호출 시점 | 반환형 | 주된 역할 |
|---|---|---|---|
| 필드 초기값 | 객체가 만들어질 때 준비 | 해당 없음 | 모든 객체의 시작 상태 또는 자동 기본값 |
| 생성자 | `new`와 함께 객체당 생성 시 한 번 | 쓰지 않음 | 객체가 처음 가져야 할 상태 설정 |
| 일반 메서드 | 객체 생성 후 필요할 때마다 | `void` 또는 값의 타입 | 동작 수행·상태 조회·상태 변경 |

### 객체 배열을 단계별로 만들기

```java
Product[] products = new Product[2];
```

이 시점에는 `Product` 객체 두 개가 만들어진 것이 아니다. **Product 참조를 넣을 수 있는 배열 칸 두 개**가 만들어졌고 각 칸의 기본값은 `null`이다.

```java
products[0] = new Product("키보드", 30000);
products[1] = new Product("마우스", 20000);

for (Product item : products) {
    item.printInfo();
}
```

초기화 기법으로 한 번에 작성할 수도 있다.

```java
Product[] products = {
    new Product("키보드", 30000),
    new Product("마우스", 20000)
};
```

#### 객체 배열에서 자주 하는 실수

- 배열만 만들고 각 칸에 객체를 넣지 않은 채 `products[0].printInfo()`를 호출하면 `null`을 통해 메서드를 호출하게 된다.
- 배열의 길이와 실제로 생성한 객체 수를 같은 것으로 생각하지 않는다.
- `products[i]`는 현재 칸의 참조이며, 그 뒤에 `.printInfo()`를 붙여 해당 객체의 메서드를 호출한다.

---

## 8. 접근 지정자와 캡슐화

| 접근 지정자 | 접근 범위의 핵심 |
|---|---|
| `public` | 어디서든 접근 가능 |
| `protected` | 같은 패키지와 상속 관계에서 접근 가능 |
| package-private | 접근 지정자를 쓰지 않으면 같은 패키지에서 접근 가능 |
| `private` | 같은 클래스 내부에서만 접근 가능 |

**캡슐화(Encapsulation)**는 필드를 `private`으로 숨기고 필요한 읽기·쓰기 통로만 메서드로 공개하는 방식이다.

- getter: 값을 읽는 통로
- setter: 값을 검사한 뒤 변경하는 통로
- 모든 필드에 무조건 setter를 만드는 것이 목적은 아니다.
- 객체가 잘못된 상태가 되지 않도록 공개 범위를 조절하는 것이 핵심이다.

### getter와 setter의 값 이동

```java
public int getPrice() {
    return price;
}

public void setPrice(int price) {
    this.price = price;
}
```

- getter는 외부 인수가 없어도 객체가 가진 필드를 읽어 반환할 수 있다.
- setter는 외부에서 새 값을 받아 필드에 저장한다.
- `this.price`는 현재 객체의 필드, 오른쪽 `price`는 setter가 받은 매개변수다.
- `price = price;`라고만 쓰면 가장 가까운 매개변수를 자기 자신에게 다시 대입하므로 객체 필드가 바뀌지 않는다.

캡슐화의 목적은 getter/setter의 개수를 늘리는 것이 아니라 객체가 허용한 통로로만 상태를 읽고 바꾸게 하는 것이다. setter 안에서 음수 가격을 거부하는 검사는 이 원리를 보여 주는 복습용 확장 예제이며, 모든 setter가 반드시 검사를 가져야 한다는 뜻은 아니다.

### 다른 패키지에서 사용할 때

다른 패키지의 `public` 클래스를 사용할 때는 `import`로 클래스 이름을 가져올 수 있다. `import`는 객체를 생성하는 문법이 아니라 클래스 이름을 현재 파일에서 사용할 수 있게 하는 선언이다.

```java
import shop.Product;
```

클래스가 `public`이어도 접근하려는 생성자나 메서드가 공개되어 있지 않으면 다른 패키지에서 사용할 수 없다. **클래스의 공개 여부와 멤버의 공개 여부를 각각 확인**해야 한다.

### 캡슐화 확인 문제

- `private` 필드가 객체에서 사라지는 것은 아니다. 같은 클래스 내부에서 직접 접근할 수 있다.
- 자식 클래스도 부모의 `private` 필드에는 직접 접근할 수 없다.
- 필드 값을 읽기만 허용하고 싶다면 getter만 공개할 수 있다.
- 모든 필드에 setter를 만들면 외부에서 객체 상태를 마음대로 바꿀 수 있으므로 업무 규칙에 맞게 공개 범위를 정한다.

---

## 9. 상속과 오버라이딩

### 상속

상속은 공통 상태와 동작을 부모 클래스에 두고 자식 클래스가 물려받아 확장하는 방식이다.

```java
public class Animal {
    public void sound() {
        System.out.println("동물이 소리를 낸다");
    }
}

class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("멍멍");
    }
}
```

- `extends`: 상속 관계 선언
- `super(...)`: 부모 생성자 호출
- `super.method()`: 부모의 메서드 호출
- Java 클래스는 한 클래스만 직접 상속한다.
- 공통분모를 부모로 올리는 과정을 일반화라고 볼 수 있다.

### 일반화에서 상속으로 가는 사고 과정

아메리카노·에스프레소·라테가 각각 이름과 가격을 중복해서 가진다면 같은 코드가 여러 클래스에 반복된다. 모든 음료가 공통으로 가져야 할 상태와 동작을 `Beverage` 부모에 올리고, 각 음료만의 차이를 자식에 남기는 것이 수업에서 배운 일반화다.

| 부모 `Beverage`에 둘 것 | 자식에 둘 것 |
|---|---|
| 모든 음료의 이름·가격 | 물의 양, 샷 수, 우유 종류처럼 음료별 상태 |
| 이름·가격 출력 같은 공통 동작 | 음료별 제조·마시기 동작 |
| 공통 생성자 초기화 | 자식만의 필드 초기화 |

상속은 단지 코드 줄 수를 줄이는 문법이 아니다. **부모로 묶어 다룰 수 있는 타입 관계**를 만들기 때문에 뒤의 업캐스팅과 다형성으로 이어진다.

### 부모 생성자와 자식 생성자의 호출 순서

```java
public class Beverage {
    private String name;
    private double price;

    public Beverage(String name, double price) {
        this.name = name;
        this.price = price;
    }
}
```

```java
public class Americano extends Beverage {
    private double waterAmount;

    public Americano(String name, double price, double waterAmount) {
        super(name, price);
        this.waterAmount = waterAmount;
    }
}
```

`new Americano("아메리카노", 4000.0, 200.0)`의 값은 다음 순서로 이동한다.

1. `Americano` 생성자의 매개변수 세 개가 값을 받는다.
2. 첫 문장 `super(name, price)`가 부모 생성자를 호출한다.
3. 부모가 자기 `name`, `price` 필드를 먼저 초기화한다.
4. 부모 생성자가 끝나면 자식으로 돌아온다.
5. 자식이 자기 `waterAmount`를 초기화한다.

부모 부분이 먼저 준비되어야 완전한 자식 객체가 만들어질 수 있으므로 `super(...)`는 자식 생성자의 첫 문장이어야 한다.

### 숨은 `super()` 오류를 해석하기

자식 생성자에서 부모 생성자 호출을 적지 않으면 Java는 첫 줄에 `super()`가 있다고 본다. 그런데 부모가 매개변수 생성자만 직접 가지고 기본 생성자 `Beverage()`가 없다면 숨은 `super()`가 호출할 대상을 찾지 못해 컴파일 오류가 난다.

해결은 두 가지다.

1. 부모에 필요한 기본 생성자 `Beverage()`를 직접 만든다.
2. 자식 생성자에서 실제 부모 생성자와 맞는 `super(name, price)`를 호출한다.

아무 기본값으로 부모를 만들면 안 되는 설계라면 두 번째 방식이 더 자연스럽다. 단지 오류를 없애려고 의미 없는 기본 생성자를 추가하기보다 객체가 반드시 가져야 할 값을 생각한다.

### 부모의 `private` 필드를 다루는 세 관점

- getter/setter 같은 부모의 공개 메서드를 이용한다.
- 자식 접근이 필요하면 `protected`를 고려할 수 있지만 공개 범위가 넓어진다.
- 생성 시 필요한 값은 `super(...)`로 부모 생성자에 전달한다.

수업에서는 세 방법을 비교한 뒤 음료 예제에서 생성자 전달을 집중적으로 추적했다. 상속받았다는 말과 자식 소스에서 직접 접근할 수 있다는 말은 다르다.

### 오버라이딩

부모에게 물려받은 메서드를 자식이 같은 signature로 다시 구현하는 것이다. `@Override`를 붙이면 잘못된 재정의를 compiler가 확인해 준다.

오버라이딩한 메서드 안에서 `super.sound()`를 호출할 수도 있고 호출하지 않을 수도 있다. 부모 동작을 유지한 뒤 자식 동작을 추가하려면 호출하고, 부모 동작을 완전히 교체하려면 호출하지 않는다. `super.sound()`가 없어도 부모와 같은 signature로 다시 정의했다면 오버라이딩이다.

#### 오버라이딩 확인 조건

- 부모·자식 상속 관계가 있어야 한다.
- 메서드 이름뿐 아니라 매개변수 목록이 맞아야 한다.
- 반환형과 접근 범위도 Java의 오버라이딩 규칙에 맞아야 한다.
- `@Override`를 붙여 컴파일러의 검사를 받는 습관이 안전하다.

### `Object` 메서드

모든 일반 클래스는 궁극적으로 `Object`를 상속한다. 수업에서는 객체 정보를 읽기 쉽게 표현하기 위해 `toString()`을 오버라이딩하는 흐름을 다뤘다.

```java
@Override
public String toString() {
    return "Product{name='" + name + "', price=" + price + "}";
}
```

객체를 `System.out.println(product);`로 출력하면 Java가 `product.toString()`을 이용한다. 재정의 전에는 클래스 이름과 해시 형태의 기본 문자열이 보일 수 있고, 재정의 후에는 사람이 읽기 쉬운 필드 정보를 반환할 수 있다.

수업 원본의 “메서드 은닉화” 표현은 자식에서 가까운 재정의가 선택되어 부모 쪽 구현이 바로 보이지 않는 상황을 설명한다. 일반적인 instance method에서는 **오버라이딩과 동적 메서드 선택**으로 이해하고, 뒤에서 다룬 `static` 메서드의 method hiding과 구분한다.

---

## 10. 참조 형변환과 다형성

### 업캐스팅

자식 객체를 부모 타입 참조 변수로 다루는 것이다. 자동으로 가능하다.

```java
Animal animal = new Dog();
animal.sound(); // 실제 Dog의 오버라이딩 메서드 실행
```

부모 타입 변수로 여러 자식 객체를 한 배열에 묶을 수 있다.

```java
Animal[] animals = {new Dog(), new Cat()};

for (Animal animal : animals) {
    animal.sound();
}
```

이것이 수업에서 음료 객체들을 부모 `Beverage` 배열로 묶어 공통 메서드를 호출한 다형성 흐름과 같다.

### 참조 변수 타입과 실제 객체 타입

```java
Animal animal = new Dog();
```

이 한 줄에는 타입이 두 개 보인다.

- 왼쪽 `Animal`: 참조 변수를 통해 **사용할 수 있다고 보이는 멤버의 범위**
- 오른쪽 `Dog`: 실제로 생성된 객체의 타입이며 **오버라이딩된 메서드가 실행될 때 선택되는 타입**

따라서 `animal.sound()`는 `Animal`에 `sound()`가 선언되어 있어 호출할 수 있고, 실행할 때는 실제 `Dog`가 재정의한 `sound()`가 선택된다. 반면 `Dog`에만 있는 `wagTail()`은 `Animal` 타입 참조로 바로 호출할 수 없다.

### 다형성이 해결하는 문제

다형성이 없다면 `Dog[]`, `Cat[]`처럼 자식 종류마다 배열과 반복문을 따로 만들 수 있다. 부모 타입 배열을 사용하면 서로 다른 자식을 같은 반복 구조로 처리하면서, 공통 메서드 호출의 실제 동작은 각 자식이 결정한다.

```java
Animal[] animals = {new Dog(), new Cat()};

for (Animal item : animals) {
    item.sound();
}
```

반복문은 `sound()`를 한 번만 작성하지만 실제 출력은 `Dog`와 `Cat`의 오버라이딩에 따라 달라진다. 이것이 단순한 형변환보다 다형성이 중요한 이유다.

### 다운캐스팅

부모 타입 참조를 다시 실제 자식 타입으로 바꾸는 것이다. 자식 전용 기능이 필요할 때 사용하지만 실제 타입이 맞는지 먼저 확인해야 한다.

```java
if (animal instanceof Dog) {
    Dog dog = (Dog) animal;
    dog.wagTail();
}
```

- 업캐스팅 후에는 부모 타입에 선언된 멤버만 바로 호출할 수 있다.
- 실행되는 오버라이딩 메서드는 실제 객체 타입을 따른다.
- 잘못된 다운캐스팅은 runtime 오류를 만든다.

### `instanceof`로 실제 타입을 확인하기

수업의 음료 배열에서는 공통 정보 출력 뒤 특정 음료만 가진 기능을 호출하기 위해 실제 타입을 검사했다.

```java
for (Beverage beverage : beverages) {
    beverage.showInfo();

    if (beverage instanceof Americano) {
        Americano americano = (Americano) beverage;
        americano.adjustWater(50);
    } else if (beverage instanceof Espresso) {
        Espresso espresso = (Espresso) beverage;
        espresso.addShot();
    }
}
```

`beverages`, `showInfo`, 각 클래스가 앞에서 선언되어 있다고 가정한 문법 조각이다.

1. 부모 타입으로 공통 기능을 먼저 사용한다.
2. `instanceof`가 실제 객체의 출신 타입을 `boolean`으로 확인한다.
3. 타입이 맞을 때만 명시적으로 다운캐스팅한다.
4. 자식 전용 기능을 호출한다.

다운캐스팅은 객체를 다른 종류로 새로 만드는 동작이 아니다. 원래 자식 객체였던 것을 부모 타입으로 보고 있다가, 실제 타입을 확인한 뒤 다시 자식 관점으로 다루는 것이다.

### 다형성 확인 문제

- `Animal animal = new Dog()`에서 객체는 `Dog`다.
- 부모 타입으로 업캐스팅해도 자식이 오버라이딩한 메서드의 동적 실행은 유지된다.
- 부모 타입에 선언되지 않은 자식 전용 메서드는 바로 보이지 않는다.
- 실제 객체가 `Cat`인데 `Dog`로 강제 변환하면 runtime 오류가 발생한다.
- 자식 기능을 매번 `instanceof`로 나눠 호출하는 코드가 많아지면 공통 동작을 부모의 추상 메서드나 인터페이스로 올릴 수 있는지도 생각한다.

---

## 11. 추상 클래스와 인터페이스

### 추상 클래스

공통 상태·기본 동작을 가지면서 일부 동작의 구현을 자식에게 강제할 때 사용한다.

```java
public abstract class Beverage {
    private String name;
    private double price;

    protected Beverage(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public abstract void make();
}
```

- `abstract` 클래스는 직접 객체로 만들 수 없다.
- 추상 메서드는 body가 없고 자식이 구현해야 한다.
- 일반 필드·생성자·일반 메서드도 함께 가질 수 있다.

### 인터페이스

특정 기능을 수행할 수 있다는 규격을 별도로 정의한다.

수업에서는 기능 이름을 역할별로 분리했다.

```java
public interface WaterAdjustable {
    void adjustWater(double amount);
}

public interface ShotAddable {
    void addShot(int count);
}

public interface MilkAddable {
    void changeMilk(String milkType);
}
```

각 인터페이스는 별도 파일에 둔다고 가정한 문법 조각이다. 수업 시점에는 인터페이스 메서드를 구현 없는 기능 계약으로 작성했다. 현대 Java 인터페이스에는 `default`, `static`, `private` 메서드도 가능하지만 이 과목의 직접 실습 범위는 아니다.

하나의 클래스가 부모 클래스 하나를 상속하면서 여러 기능 인터페이스를 구현할 수 있다.

```java
public class SpecialCoffee extends Beverage
        implements WaterAdjustable, ShotAddable, MilkAddable {

    private double waterAmount;
    private int shotCount;
    private String milkType;

    public SpecialCoffee(String name, double price,
                         double waterAmount, int shotCount, String milkType) {
        super(name, price);
        this.waterAmount = waterAmount;
        this.shotCount = shotCount;
        this.milkType = milkType;
    }

    @Override
    public void make() {
        System.out.println("스페셜 커피를 만든다");
    }

    @Override
    public void adjustWater(double amount) {
        this.waterAmount = amount;
    }

    @Override
    public void addShot(int count) {
        this.shotCount += count;
    }

    @Override
    public void changeMilk(String milkType) {
        this.milkType = milkType;
    }
}
```

위 코드는 앞의 재구성 `Beverage`와 연결한 문법 조각이다. 실제 수업 클래스명은 `Beverage05`, `SpecialCoffee05`였고 기능 계약은 `WaterAdjustable`, `ShotAddable`, `MilkAddable`이었다.

#### 왜 모든 기능을 부모에 넣지 않는가

모든 음료가 우유 변경 기능을 갖는 것은 아니다. 부모 `Beverage`에 `changeMilk()`를 넣으면 우유가 없는 음료도 의미 없는 메서드를 가져야 한다. 기능 인터페이스로 분리하면 필요한 클래스만 해당 계약을 구현한다.

- `extends Beverage`: “스페셜 커피는 음료의 한 종류다.”
- `implements WaterAdjustable`: “물의 양을 조절할 수 있다.”
- `implements ShotAddable`: “샷을 추가할 수 있다.”
- `implements MilkAddable`: “우유 종류를 바꿀 수 있다.”

### 추상화 단계의 실행 흐름

1. 부모 추상 클래스가 모든 음료의 공통 상태와 반드시 구현할 동작을 정한다.
2. 자식이 추상 메서드를 오버라이딩해 구체적인 동작을 만든다.
3. 선택 기능은 인터페이스로 잘게 나눈다.
4. 필요한 자식만 여러 인터페이스를 구현한다.
5. 부모 타입 배열로 모든 음료의 공통 동작을 반복 호출한다.
6. 선택 기능이 필요할 때 실제 타입·인터페이스 구현 여부를 확인해 사용한다.

### 추상 클래스·인터페이스 확인 문제

- 추상 클래스도 필드·생성자·일반 메서드를 가질 수 있다.
- 추상 클래스와 인터페이스는 이 수업에서 직접 객체로 만들 대상이 아니다.
- 추상 메서드를 가진 구체 자식은 해당 메서드를 구현해야 한다.
- 클래스 상속은 하나지만 인터페이스는 여러 개 구현할 수 있다.
- 공통 상태까지 공유하면 추상 클래스, 독립적인 기능 계약을 붙이면 인터페이스가 자연스럽다.

### 추상 클래스 vs 인터페이스

| 판단 기준 | 추상 클래스 | 인터페이스 |
|---|---|---|
| 중심 목적 | 공통 상태와 기본 구조 공유 | 기능 규격·역할 부여 |
| 관계 | “무엇의 한 종류이다” | “무엇을 할 수 있다” |
| 상속·구현 | 클래스는 하나만 상속 | 여러 인터페이스 구현 가능 |
| 수업 예 | 공통 `Beverage` | 물·샷·우유 조절 기능 |

---

## 12. 메모리 관점, `static`, `final`

### 입문 수준의 메모리 구분

| 영역 관점 | 무엇을 떠올리면 되는가 |
|---|---|
| stack | 메서드 호출과 지역 변수·참조 변수의 실행 단위 |
| heap | `new`로 만든 객체와 배열 |
| static 영역 | 클래스가 load될 때 준비되는 class 공용 멤버 |

이 구분은 실제 JVM 세부 구현을 모두 설명하는 모델이 아니라 객체와 class member의 생명주기를 이해하기 위한 입문 관점이다.

### `static`

`static` 멤버는 객체마다 따로 생기는 값이 아니라 클래스에 속한 공용 멤버다.

```java
public class Cafe {
    private static int count = 0;

    public Cafe() {
        count++;
    }

    public static int getCount() {
        return count;
    }
}
```

#### instance 필드와 static 필드를 비교하기

```java
public class BeverageCountExample {
    private String name;
    private static int beverageCount = 0;

    public BeverageCountExample(String name) {
        this.name = name;
        beverageCount++;
    }

    public String getName() {
        return name;
    }

    public static int getBeverageCount() {
        return beverageCount;
    }
}
```

```java
public class BeverageCountMain {
    public static void main(String[] args) {
        new BeverageCountExample("아메리카노");
        new BeverageCountExample("라테");

        System.out.println(BeverageCountExample.getBeverageCount()); // 2
    }
}
```

- `name`은 객체마다 따로 존재한다.
- `beverageCount`는 클래스에 하나만 존재하고 모든 생성자가 같은 값을 증가시킨다.
- 필드는 `private static`으로 보호하면서 `public static` getter로 객체 없이 읽을 수 있다.
- 객체 두 개를 만들었으므로 공유 카운터는 `2`가 된다.

- `static` 메서드는 객체 없이 `Cafe.getCount()`처럼 호출할 수 있다.
- `static` 메서드에서는 객체가 있어야 존재하는 instance field를 바로 사용할 수 없다.
- 부모와 자식에 같은 `static` 메서드가 있으면 instance method overriding과 같은 동적 다형성이 아니라 method hiding으로 구분한다.
- `private static` 필드는 class 내부에서만 공유하고, 필요한 경우 `public static` 메서드로 읽는다.

#### static 메서드에서 instance 필드를 바로 못 쓰는 이유

instance 필드는 어떤 객체의 값인지 정해야 한다. 반면 static 메서드는 특정 객체 없이 `ClassName.method()`로 호출할 수 있다. 따라서 static 메서드 안에서 객체 선택 없이 `name` 같은 instance 필드를 바로 사용하면 “어느 객체의 이름인가?”를 결정할 수 없다.

```java
public static void printName() {
    // System.out.println(name); // 특정 객체가 없어 컴파일 오류
}
```

### `final`

`final`은 변경을 제한한다.

- `final` 변수: 한 번 대입한 뒤 다시 대입할 수 없음
- `final` 메서드: 자식이 오버라이딩할 수 없음
- `final` 클래스: 상속할 수 없음

```java
public static final String STORE_NAME = "G-CAFE";
```

상수는 보통 `static final`로 만들고 대문자와 `_`를 사용해 이름을 작성한다.

수업에서 직접 중심적으로 확인한 것은 `public static final String STORE_NAME`과 같은 클래스 상수다. `final` 메서드·클래스는 숙제 조사와 Java 일반 규칙으로 구분한다.

#### final 참조의 정확한 뜻

```java
final Product product = new Product("키보드", 30000);
// product = new Product("마우스", 20000); // 다른 객체로 재대입 불가
product.setPrice(28000); // 객체가 변경 가능하게 설계됐다면 내부 상태 변경 가능
```

`final`이 참조 변수에 붙으면 참조가 다른 객체를 가리키도록 다시 대입할 수 없다는 뜻이다. 참조한 객체의 모든 내부 값이 자동으로 불변이 된다는 뜻은 아니다.

### `static`·`final` 확인 문제

- 객체마다 달라야 하는 이름·가격은 instance 필드가 자연스럽다.
- 전체 객체가 공유하는 생성 개수는 static 필드가 자연스럽다.
- 클래스 공용 값이어도 외부에서 마음대로 바꾸면 안 되면 `private static`과 공개 메서드를 조합한다.
- 모든 객체가 공유하고 바뀌지 않을 상수는 `static final`로 둔다.
- static method hiding은 instance method overriding처럼 실제 객체 타입에 따라 동적으로 선택되는 기능이 아니다.

---

## 13. 오버로딩·오버라이딩·은닉 한 번에 구분

| 구분 | 오버로딩 | 오버라이딩 | static method hiding |
|---|---|---|---|
| 위치 | 보통 같은 클래스 | 부모·자식 관계 | 부모·자식 관계 |
| 조건 | 같은 이름, 다른 매개변수 | 같은 signature의 instance method 재정의 | 같은 signature의 `static` method 재선언 |
| 선택 시점 | compiler가 인수 형태로 선택 | runtime 실제 객체 타입에 따라 동작 | 참조에 사용된 class 기준 |
| 목적 | 다양한 입력 방법 제공 | 자식별 동작 변경 | class member 이름 가림 |

---

## 14. 수업 전체를 관통하는 미니 예제

아래 구조는 수업의 Product와 Beverage 실습을 한 흐름으로 복습하기 위한 것이다.

1. 클래스로 상품·음료 같은 대상을 표현한다.
2. 필드를 `private`으로 숨긴다.
3. 생성자로 초기값을 넣는다.
4. getter나 업무 메서드로 필요한 기능만 공개한다.
5. 공통 상태·동작은 부모 클래스로 일반화한다.
6. 자식마다 다른 동작은 오버라이딩한다.
7. 선택 기능은 인터페이스로 분리한다.
8. 부모 타입 배열과 향상된 `for`로 여러 자식 객체를 함께 처리한다.
9. 공용 값은 `static`, 변경하지 않을 값은 `final`로 둔다.

이 흐름을 이해하면 Java 문법이 서로 떨어진 암기 항목이 아니라 **데이터와 동작을 객체로 묶고, 공통점과 차이점을 타입 구조로 표현하는 한 과정**으로 보인다.

### 완전 예제: 한 파일로 실행하는 음료 주문 복습

다음 `CafeReviewApp.java`는 수업에서 배운 핵심을 한 파일 안에 재구성한 완전 예제다. 실제 수업 파일 여러 개를 그대로 합친 것이 아니라 복습을 위해 이름과 구조를 정돈했다.

```java
public class CafeReviewApp {
    public static final String STORE_NAME = "G-CAFE";

    interface WaterAdjustable {
        void adjustWater(double amount);
    }

    interface ShotAddable {
        void addShot(int count);
    }

    abstract static class Beverage {
        private String name;
        private int price;
        private static int beverageCount = 0;

        protected Beverage(String name, int price) {
            this.name = name;
            setPrice(price);
            beverageCount++;
        }

        public String getName() {
            return name;
        }

        public int getPrice() {
            return price;
        }

        public void setPrice(int price) {
            if (price >= 0) {
                this.price = price;
            }
        }

        public static int getBeverageCount() {
            return beverageCount;
        }

        public void showInfo() {
            System.out.printf("%s: %d원%n", name, price);
        }

        public abstract void make();

        @Override
        public String toString() {
            return name + "(" + price + "원)";
        }
    }

    static class Americano extends Beverage implements WaterAdjustable, ShotAddable {
        private double waterAmount;
        private int shotCount;

        public Americano(String name, int price, double waterAmount) {
            super(name, price);
            this.waterAmount = waterAmount;
            this.shotCount = 2;
        }

        @Override
        public void adjustWater(double amount) {
            this.waterAmount = amount;
        }

        @Override
        public void addShot(int count) {
            this.shotCount += count;
        }

        @Override
        public void make() {
            System.out.printf("물 %.0fml, 샷 %d개로 아메리카노 제조%n",
                    waterAmount, shotCount);
        }
    }

    static class Latte extends Beverage {
        private String milkType;

        public Latte(String name, int price, String milkType) {
            super(name, price);
            this.milkType = milkType;
        }

        @Override
        public void make() {
            System.out.println(milkType + "로 라테 제조");
        }
    }

    public static void main(String[] args) {
        Beverage[] menu = {
                new Americano("아메리카노", 4000, 200),
                new Latte("카페라테", 4500, "우유")
        };

        System.out.println("어서 오세요. " + STORE_NAME + "입니다.");

        int totalPrice = 0;

        for (Beverage beverage : menu) {
            beverage.showInfo();
            beverage.make();
            totalPrice += beverage.getPrice();

            if (beverage instanceof Americano) {
                Americano americano = (Americano) beverage;
                americano.addShot(1);
                americano.adjustWater(250);
                americano.make();
            }
        }

        System.out.println("메뉴: " + menu[0] + ", " + menu[1]);
        System.out.println("가격 합계: " + totalPrice + "원");
        System.out.println("생성된 음료 수: " + Beverage.getBeverageCount());
    }
}
```

예상 출력:

```text
어서 오세요. G-CAFE입니다.
아메리카노: 4000원
물 200ml, 샷 2개로 아메리카노 제조
물 250ml, 샷 3개로 아메리카노 제조
카페라테: 4500원
우유로 라테 제조
메뉴: 아메리카노(4000원), 카페라테(4500원)
가격 합계: 8500원
생성된 음료 수: 2
```

### 통합 예제를 기능별로 해부하기

| 배운 내용 | 예제의 위치 | 의미 |
|---|---|---|
| 변수·자료형 | 이름, 가격, 물의 양, 샷 수 | 상태에 맞는 타입 선택 |
| 조건문 | 음수 가격 거부, `instanceof` | 조건에 따라 실행 흐름 분기 |
| 배열·반복 | `Beverage[] menu`, 향상된 `for` | 여러 객체를 한 구조로 처리 |
| 클래스·객체 | `Americano`, `Latte`, `new` | 사용자 정의 타입과 실제 객체 |
| 캡슐화 | `private` 필드, getter/setter | 직접 접근을 막고 공개 통로 제공 |
| 생성자·`this`·`super` | 각 생성자 | 부모 상태와 자식 상태 초기화 |
| 상속·오버라이딩 | `extends Beverage`, `make()` | 공통 구조와 서로 다른 동작 |
| 다형성 | 부모 타입 배열에서 `make()` | 같은 호출로 실제 자식 동작 실행 |
| 인터페이스 | 물 조절·샷 추가 | 선택 기능 계약 분리 |
| `static` | 음료 생성 수 | 모든 객체가 하나의 값을 공유 |
| `final` | `STORE_NAME` | 바뀌지 않는 클래스 공용 상수 |
| `toString()` | 메뉴 출력 | 객체를 사람이 읽을 문자열로 표현 |

### 통합 예제를 변형해 볼 과제

1. `Latte`에도 우유 변경 인터페이스를 추가한다.
2. 가격이 `0` 미만이면 기존 가격을 유지하는 현재 setter의 동작을 설명한다.
3. `Espresso` 자식을 추가해 부모 배열에 넣는다.
4. 일반 `for`로 바꿔 메뉴 번호까지 출력한다.
5. 총가격 평균을 `double`로 계산해 정수 나눗셈과 비교한다.
6. `toString()`을 제거했을 때 객체 출력이 어떻게 달라지는지 확인한다.

---

## 15. Java 수업에서 함께 접한 주변 내용

### Git과 GitHub 입문

Java 첫 과정 중 IntelliJ 프로젝트를 Git 저장소로 만들고 GitHub remote와 연결하는 초기 설정도 진행했다. 이것은 Java 문법은 아니지만 이후 협업의 기반이다.

- Git은 local 변경 이력을 관리한다.
- GitHub는 remote repository를 제공한다.
- Java source와 IDE 설정 전체를 무분별하게 올리는 것이 아니라 추적할 파일을 구분해야 한다.

#### Java 수업에서 진행한 초기 연결 흐름

1. Git을 설치하고 명령을 실행할 수 있는지 준비한다.
2. terminal에서 Java 프로젝트 폴더로 이동한다.
3. `git init`으로 현재 프로젝트를 local repository로 초기화한다.
4. Git 작성자 이름·이메일과 필요 시 safe directory를 설정한다.
5. GitHub에 `MyJava` 원격 repository를 준비한다.
6. IntelliJ의 Git/VCS 기능에서 local project와 remote를 연결한다.
7. 변경 내용을 commit한 뒤 remote에 push하는 흐름을 시작한다.

여기서 `git init`은 GitHub에 파일을 업로드하는 명령이 아니다. 현재 폴더에 local Git 저장소를 만드는 단계다. commit은 local 이력을 만들고, push는 그 이력을 remote에 전송한다. 자세한 branch·Pull Request·conflict 협업은 뒤의 Linux 과정에서 본격적으로 확장됐다.

실제 사용자 이름·이메일·repository URL은 개인 설정값이므로 이 교재에 복제하지 않는다.

### Java 팀 프로젝트와 Oracle 전환

마지막에는 Java 팀 프로젝트·코드 검토를 거쳐 Oracle 설치와 DB 학습으로 이동했다. Java의 `Product` 객체가 실행 중 memory에 존재하는 데이터라면, DB table은 프로그램이 종료돼도 남는 데이터를 저장한다. 이후 Spring Boot에서 Java Entity와 DB table의 연결을 배우게 된다.

### 숙제·사전조사의 경계

memory 세부 구조, collection, generic, FIFO/LIFO 같은 내용은 일부 숙제·사전조사에서 다뤘다. 이들은 이후 학습을 위한 배경지식이지만 02-26~03-13 직접 실습의 중심 범위와 구분한다.

---

## 16. 가장 많이 헷갈리는 것

1. **`=` vs `==`:** 대입과 비교는 다르다.
2. **기본형 vs 참조형:** 기본형 변수는 값 중심, 참조형 변수는 객체 위치를 가리키는 참조 중심이다.
3. **클래스 vs 객체:** 클래스는 타입·설계도, 객체는 그 클래스로 만든 instance다.
4. **필드 vs 지역 변수:** 필드는 객체 상태, 지역 변수는 메서드 실행 중 사용하는 값이다.
5. **메서드 vs 생성자:** 메서드는 필요할 때 호출하고, 생성자는 객체 생성 시 초기화한다.
6. **오버로딩 vs 오버라이딩:** 매개변수가 다른 같은 이름과 상속받은 동작 재정의를 구분한다.
7. **배열 칸 vs 객체:** 객체 배열의 칸에는 객체를 가리키는 참조가 들어간다.
8. **업캐스팅 vs 다운캐스팅:** 부모 타입으로 넓혀 다루는 것과 실제 자식 타입으로 좁히는 것을 구분한다.
9. **추상 클래스 vs 인터페이스:** 공통 기반과 선택 기능 규격의 차이다.
10. **instance vs `static`:** 객체마다 가진 값과 class 전체가 공유하는 값을 구분한다.
11. **`final` 참조:** 참조를 다시 바꾸지 못한다는 뜻이지, 참조한 mutable 객체 내부가 항상 불변이라는 뜻은 아니다.
12. **UI에 코드가 보임 vs 실행됨:** 코드를 작성한 것과 실제 실행 결과가 확인된 것은 다르다.

---

## 17. 복습 체크리스트

### 설명할 수 있어야 하는 것

- [ ] 프로젝트·패키지·클래스·`main`의 관계를 설명할 수 있다.
- [ ] `print`, `println`, `printf`의 차이를 설명할 수 있다.
- [ ] 변수 선언·대입·읽기·덮어쓰기를 구분할 수 있다.
- [ ] 기본형과 참조형의 차이를 설명할 수 있다.
- [ ] 암시적·명시적 형변환과 정수 나눗셈을 설명할 수 있다.
- [ ] 비교·논리·삼항 연산자로 조건을 만들 수 있다.
- [ ] `if`, `switch`, `for`, `while`의 선택 기준을 말할 수 있다.
- [ ] 배열의 인덱스·길이·기본값을 설명할 수 있다.
- [ ] 클래스·객체·참조 변수의 차이를 설명할 수 있다.
- [ ] 필드·메서드·생성자의 역할을 구분할 수 있다.
- [ ] `this`와 `super`가 각각 무엇을 가리키는지 설명할 수 있다.
- [ ] 접근 지정자와 getter/setter의 목적을 설명할 수 있다.
- [ ] 오버로딩과 오버라이딩을 예와 함께 구분할 수 있다.
- [ ] 상속과 다형성을 부모 타입 배열로 설명할 수 있다.
- [ ] 안전한 다운캐스팅에 `instanceof`가 필요한 이유를 설명할 수 있다.
- [ ] 추상 클래스와 인터페이스를 언제 선택하는지 설명할 수 있다.
- [ ] instance member와 `static` member의 차이를 설명할 수 있다.
- [ ] `final` 변수·메서드·클래스의 의미를 구분할 수 있다.

### 직접 작성해 볼 것

- [ ] 이름과 점수를 입력받아 등급을 출력하는 프로그램
- [ ] 배열에 저장된 숫자의 합계와 평균을 계산하는 프로그램
- [ ] `Product` 클래스에 `private` 필드·생성자·getter를 작성하기
- [ ] 부모 `Animal`과 자식 `Dog`, `Cat`을 만들고 오버라이딩하기
- [ ] 부모 타입 배열에서 여러 자식의 메서드를 반복 호출하기
- [ ] 공통 상태는 추상 클래스, 선택 기능은 인터페이스로 나누기

### 실행 결과를 손으로 추적할 수 있어야 하는 것

- [ ] `age++`와 `++age`가 다른 식 안에서 언제 값을 증가시키는지 추적할 수 있다.
- [ ] `14 / 5`, `(double) 14 / 5`, `(double) (14 / 5)`의 결과를 계산 순서로 설명할 수 있다.
- [ ] `if ~ else if` 조건 순서를 바꾸면 결과가 달라지는 예를 들 수 있다.
- [ ] `switch`에서 `break`를 빼면 어디까지 실행되는지 예상할 수 있다.
- [ ] `for`의 초기식·조건식·본문·증감식 실행 순서를 적을 수 있다.
- [ ] `while`에서 증감식이나 `break`가 없을 때 왜 끝나지 않는지 설명할 수 있다.
- [ ] 입력값이 배열의 어느 인덱스에 저장되고 누적 변수에 어떻게 더해지는지 표로 추적할 수 있다.
- [ ] 메서드 인수가 매개변수에 들어가고 `return`이 호출 위치로 돌아오는 경로를 그릴 수 있다.
- [ ] `new Product[2]` 직후 두 칸이 객체가 아니라 `null` 참조라는 점을 설명할 수 있다.
- [ ] 자식 생성자 → `super(...)` → 부모 필드 → 자식 필드의 초기화 순서를 적을 수 있다.
- [ ] 부모 타입 참조와 실제 자식 객체 타입이 각각 무엇을 결정하는지 설명할 수 있다.
- [ ] 객체 두 개를 만들 때 static 카운터가 왜 하나의 값으로 `2`가 되는지 설명할 수 있다.

### 오류를 보고 원인을 찾을 수 있어야 하는 것

- [ ] 지역 변수를 초기화하지 않고 읽을 때의 컴파일 오류
- [ ] `i <= array.length` 때문에 마지막 인덱스를 넘는 오류
- [ ] 숫자 입력 뒤 `nextLine()`이 빈 문자열을 읽는 입력 오류
- [ ] `price = price` 때문에 객체 필드가 바뀌지 않는 논리 오류
- [ ] 매개변수 생성자를 만든 뒤 기본 생성자 호출이 실패하는 오류
- [ ] 부모의 `private` 필드에 자식이 직접 접근하려는 오류
- [ ] 실제 타입을 확인하지 않은 잘못된 다운캐스팅 오류
- [ ] static 메서드가 특정 객체 없이 instance 필드를 직접 읽으려는 오류
- [ ] `final` 변수에 두 번째 값을 대입하려는 오류

### 단계별 실습 코스

한 번에 통합 예제를 외우지 말고 아래 순서로 직접 작성한다.

1. **기초:** 이름·나이·평균을 변수에 저장하고 `printf`로 출력한다.
2. **분기:** 점수를 입력받아 높은 기준부터 학점을 판정한다.
3. **반복:** 1부터 입력값까지의 합계를 `for`와 `while`로 각각 구한다.
4. **배열:** 입력한 여러 정수의 홀수·짝수 합계를 구한다.
5. **클래스:** `Product`에 이름·가격 필드와 출력 메서드를 둔다.
6. **캡슐화:** 필드를 `private`으로 바꾸고 생성자·getter·setter를 연결한다.
7. **객체 배열:** 여러 `Product`를 배열에 넣고 전체 가격을 계산한다.
8. **상속:** `Beverage` 공통 부모와 두 자식을 만든다.
9. **다형성:** 부모 배열에서 각 자식의 오버라이딩 메서드를 호출한다.
10. **추상화:** 공통 필수 동작은 추상 메서드, 선택 기능은 인터페이스로 나눈다.
11. **공유 상태:** 생성된 객체 수를 `private static`으로 세고 getter로 읽는다.
12. **통합:** `CafeReviewApp`을 보지 않고 비슷한 구조를 다시 만든다.

### 이 과목을 복습 완료했다고 볼 기준

- [ ] 코드를 보지 않고 각 핵심 용어를 자신의 말로 설명한다.
- [ ] 짧은 코드의 출력과 오류를 실행 전에 예상한다.
- [ ] 기초→배열→객체→상속 순서의 실습을 빈 파일에서 작성한다.
- [ ] 예제 실행 결과가 예상과 다르면 출력·변수값을 추가해 원인을 좁힌다.
- [ ] 직접 수업 내용과 숙제 조사·후속 Spring 연결을 구분한다.
- [ ] 통합 예제의 각 줄이 어떤 수업 개념에 해당하는지 표 없이 설명한다.

---

## 18. 다음 과목·프로젝트와의 연결

- **Oracle:** Java 객체의 값을 프로그램 밖 DB table에 영구 저장하는 관점으로 확장한다.
- **UI&UX:** Java console 입출력 대신 HTML/CSS/JavaScript 화면에서 사용자가 입력하고 결과를 본다.
- **Spring Boot:** Java 클래스가 Controller·Service·Repository·Entity·DTO 역할로 나뉜다.
- **JPA:** Java Entity와 관계형 DB table을 연결한다.
- **React와 API:** Java 객체가 JSON 응답으로 바뀌어 frontend state에 들어간다.

Java에서 가장 중요한 기반은 문법 항목의 개수보다 **값을 타입으로 구분하고, 흐름을 제어하며, 상태와 동작을 객체로 묶고, 공통점과 차이점을 상속·인터페이스로 표현하는 사고방식**이다.

## 더 자세히 볼 때만 여는 Wiki

- 과목 근거 허브: [[summaries/2026-03-13-java-subject-review|Java 총정리]]
- 기술 이력: [[entities/java|Java]]
- 값과 흐름: [[concepts/java-basic-types|Java 기본 자료형]], [[concepts/java-operators|Java 연산자]], [[concepts/java-conditional-logic|Java 조건 판단]], [[concepts/java-loop|Java 반복문]], [[concepts/java-array|Java 배열]]
- 객체지향: [[concepts/java-class-object|Java 클래스와 객체]], [[concepts/java-method-constructor-overloading|Java 메서드·생성자·오버로딩]], [[concepts/java-inheritance|Java 상속]], [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- 추상화: [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]], [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]], [[concepts/java-memory-static-final|Java 메모리·static·final]]
- 비교: [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]], [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]], [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]], [[comparisons/array-vs-collection|배열 vs 컬렉션]]

## 출처

- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/2026.02.26(목) - 시작/2026.02.26(목) - 시작.md`부터 `raw/KoreaICT/1. Java/2026.03.13(금)/2026.03.13(금).md`까지의 날짜별 Java 수업 기록
- `raw/KoreaICT/1. Java/2026.02.27(금)/깃허브 초기 설정.md` — Java 실습 프로젝트의 Git/GitHub 초기 연결 범위
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md` — 직접 수업 복습과 메모리·컬렉션·제네릭 조사 범위의 경계 확인
- 기존 Wiki의 Java Summary·Concept·Comparison은 원본 범위와 개념 연결을 교차 확인하는 데 사용했다.

본문은 원본의 부정확한 표현을 그대로 복제하지 않는다. 예를 들어 원본의 “모든 인터페이스 메서드는 추상 메서드”, instance overriding 문맥의 “메서드 은닉화”, 입력 메서드 철자 등은 현재 Java 규칙과 세부 Wiki의 교정 내용을 기준으로 설명하고, 직접 배운 범위와 현대 Java의 확장 범위를 구분했다.
