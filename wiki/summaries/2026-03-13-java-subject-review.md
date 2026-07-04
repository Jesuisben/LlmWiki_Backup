---
title: Java 총정리
type: summary
created: 2026-07-03
updated: 2026-07-04
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/2026.02.26(목)/2026.02.26(목).md
  - raw/Study/1. Java/2026.02.27(금)/2026.02.27(금).md
  - raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md
  - raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md
  - raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md
  - raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/Study/1. Java/2026.03.13(금)/2026.03.13(금).md
status: stable
confidence: high
---

# Java 총정리

## 한 줄 요약

`Java 총정리`는 2026-02-26부터 2026-03-13까지의 Java 입문 과정을 “문법을 읽는 법 → 값을 다루는 법 → 흐름을 제어하는 법 → 여러 값을 묶는 법 → 객체를 설계하는 법 → 상속/추상화로 공통 구조를 만드는 법”으로 다시 엮은 복습 허브다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-02-26-orientation|2026-02-26 오리엔테이션과 개발 환경 준비]]부터 [[summaries/2026-03-12-java-abstract-interface-static|2026-03-12 Java 추상 클래스, 인터페이스, static/final]]까지의 날짜별 수업 노트
- 마무리 자료: [[summaries/2026-03-13-java-project-oracle-start|2026-03-13 Java 팀 프로젝트와 Oracle 시작]]에서 Java 팀 프로젝트를 거쳐 [[entities/oracle-database|Oracle Database]]로 넘어감
- 역할: 날짜별 summary를 대체하지 않고, Java 전체 흐름을 다시 찾기 위한 과목 단위 복습 허브

## 커리큘럼 흐름으로 다시 보기

### 1. Java 파일을 읽는 최소 문법

초반부는 프로젝트, 패키지, 클래스, 인터페이스, `main` 메서드, 세미콜론, 중괄호, 주석, 출력 메서드처럼 “Java 코드가 어떤 모양으로 서 있어야 실행되는가”를 다룬다. 이 단계의 핵심은 문법 암기가 아니라, Java에서는 실행할 코드가 클래스 안에 들어가고 문장의 끝은 세미콜론으로 끊는다는 감각을 만드는 것이다.

이 감각은 나중에 [[concepts/java-class-object|Java 클래스와 객체]]에서 클래스가 단순 파일명이 아니라 사용자 정의 타입이자 설계 단위라는 이해로 확장된다.

### 2. 값의 종류와 변수: 읽기/쓰기 감각

총정리 원본은 `char`, `String`, `int`, `double`, `boolean`을 중심으로 변수 선언, 대입, 덮어쓰기, 식별자 규칙을 정리한다. 특히 `x = 3`은 값을 “읽는” 것이 아니라 변수에 값을 “쓰는” 동작이고, `sum = x + y`는 오른쪽 값을 읽은 뒤 왼쪽 변수에 쓰는 동작이라는 설명이 남아 있다.

이 관점은 초보자에게 매우 중요하다. 변수는 값을 저장하는 이름이고, 대입 연산자 `=`는 수학의 같다는 뜻이 아니라 오른쪽 값을 왼쪽 저장공간에 넣는 동작이다. 관련 개념은 [[concepts/java-basic-types|Java 기본 자료형]], [[concepts/java-operators|Java 연산자]], [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]에서 이어진다.

### 3. 형변환과 연산자: 컴퓨터가 타입을 맞추는 방식

암시적 형변환은 더 넓은 타입으로 자연스럽게 이동하는 경우이고, 명시적 형변환은 개발자가 `(int)`처럼 직접 변환을 지시하는 경우다. `14 / 5`와 `(double) 14 / 5`, `(double)(14 / 5)`의 차이는 “언제 형변환이 일어났는가”에 따라 결과가 달라지는 대표 예시다.

문자 `char`도 비교나 계산 상황에서는 숫자 코드처럼 다뤄질 수 있다는 점이 등장한다. 이 내용은 이후 SQL에서 숫자/문자/날짜 타입을 구분하는 [[concepts/oracle-sql-basics|Oracle SQL 기본]] 학습과도 연결된다.

### 4. 조건문과 반복문: 실행 흐름을 나누고 반복하기

`if`, `if~else`, `else if`, `switch`는 경우의 수에 따라 실행 경로를 나누는 선택문이다. `for`는 반복 횟수가 비교적 명확할 때, `while`은 반복 종료 조건이 입력이나 상태에 따라 달라질 때 사용한다. 총정리에는 `break`로 반복을 끊는 무한 `while` 흐름과 `Scanner` 입력 함수도 함께 정리되어 있다.

이 단계는 [[concepts/java-conditional-logic|Java 조건 판단]], [[concepts/java-loop|Java 반복문]]의 기반이며, 뒤의 배열 문제에서 “입력 → 반복 → 조건 판단 → 누적”이라는 실습 패턴으로 결합된다.

### 5. 배열과 객체 배열: 여러 값을 순서 있게 묶기

배열은 0번 인덱스부터 시작하고, 이름·타입·요소 개수를 가진 고정 길이 자료구조다. `new` 연산자 기법은 방 개수부터 만들고 값을 나중에 넣는 방식이고, 초기화 기법은 값이 명확할 때 한 번에 넣는 방식이다. 총정리에는 점수 입력 후 홀수/짝수 합계를 계산하는 예시, BTS 멤버 배열 예시, 객체 배열 예시가 이어진다.

객체 배열은 단순 값 배열과 다르게 각 칸에 객체 참조가 들어간다. 그래서 [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]], [[comparisons/array-vs-collection|배열 vs 컬렉션]]으로 넘어갈 때 “배열 칸 자체”와 “그 칸이 가리키는 객체”를 구분해야 한다.

### 6. 클래스와 객체: 사용자 정의 타입 만들기

클래스는 필드, 메서드, 생성자를 묶어 만든 사용자 정의 타입이다. 총정리 원본은 `Product` 예시를 통해 객체 생성, 멤버 변수 값 할당, 멤버 메서드 호출, `void` 메서드와 반환 메서드의 차이, getter/setter, 접근 지정자를 차례로 정리한다.

여기서 중요한 연결은 다음과 같다.

- 필드: 객체가 가진 상태
- 메서드: 객체가 할 수 있는 동작
- 생성자: 객체를 만들 때 한 번 실행되는 초기화 통로
- getter/setter: `private` 필드를 외부에서 안전하게 읽고 쓰는 공개 메서드
- `this`: 매개변수와 필드 이름이 겹칠 때 “이 객체의 필드”를 가리키는 기준점

관련 페이지는 [[concepts/java-class-object|Java 클래스와 객체]], [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]이다.

### 7. 생성자, 오버로딩, 기본 생성자 오류

총정리에서 특히 좋은 복습 포인트는 생성자 오류 설명이다. 클래스에 생성자를 하나도 만들지 않으면 Java가 기본 생성자를 자동으로 제공하지만, 매개변수가 있는 생성자를 직접 하나라도 만들면 기본 생성자는 자동 생성되지 않는다. 그래서 자식 생성자 첫 줄에 숨어 있는 `super()`가 부모의 없는 기본 생성자를 찾으면 오류가 난다.

이 내용은 단순 문법 문제가 아니라 객체 생성 흐름을 이해하는 문제다. “생성자는 객체 생성 시 한 번 호출되고, 메서드는 객체 생성 후 필요할 때 호출된다”는 차이를 기준으로 보면 오버로딩과 상속 생성자 문제가 함께 정리된다.

### 8. 상속, 오버라이딩, 다형성

상속은 비슷한 클래스들의 공통분모를 부모 클래스에 모아 중복을 줄이는 방식이다. 총정리에서는 `Animal`, `Dog`, `Beverage`, `Americano`, `Espresso`, `Latte` 예시를 통해 일반화, `super`, 오버라이딩, `toString()`, 참조 형변환, `instanceof`까지 이어진다.

핵심은 부모 타입으로 여러 자식 객체를 묶어 다룰 수 있다는 점이다. 예를 들어 `Beverage04[]` 배열 안에 `Americano04`, `Espresso04`, `Latte04`를 함께 넣고 반복문으로 공통 메서드를 호출할 수 있다. 자식 전용 기능이 필요하면 `instanceof`로 실제 타입을 확인하고 다운캐스팅한다. 관련 페이지는 [[concepts/java-inheritance|Java 상속]], [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]], [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]이다.

### 9. 추상 클래스, 인터페이스, static/final

추상 메서드는 “해야 할 행동의 이름은 정해두되 구현은 자식에게 맡기는” 메서드다. 추상 메서드가 들어간 클래스는 추상 클래스가 되어야 하고, 자식 클래스는 강제로 오버라이딩해야 한다. 인터페이스는 기능 규격을 분리해 `implements`로 붙이는 방식이며, 수업에서는 다중 상속의 대안처럼 소개된다.

`static`은 객체가 아니라 클래스에 속하는 멤버를 만들 때 쓰고, `final`은 더 이상 바꾸지 못하게 고정할 때 쓴다. `public static final String STORE_NAME = "G-CAFE"` 같은 상수 예시는 객체마다 달라지는 값과 클래스 전체가 공유하는 값을 구분하게 해준다. 관련 페이지는 [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]], [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]], [[concepts/java-memory-static-final|Java 메모리, static, final]]이다.

## 핵심 실습 / 예제 앵커

- `System.out.println`, `print`, `printf`로 출력 방식 구분
- `Scanner`로 이름/나이 입력을 받고 변수에 저장
- `for`, `while`로 1~10 합계와 홀짝 합계 계산
- `String[]`, `int[]` 배열을 `new` 기법과 초기화 기법으로 생성
- `Product` 클래스로 필드, 메서드, 생성자, getter/setter 실습
- 객체 배열에 여러 `Product03` 객체를 담아 반복 출력
- `Beverage` 계열 클래스로 상속, `super`, 오버라이딩, 다형성, `instanceof` 확인
- `WaterAdjustable` 같은 인터페이스로 기능 규격을 분리

## 헷갈린 점 / 질문

- `String`은 수업 초반에 기본처럼 자주 쓰지만 실제로는 참조 자료형이다.
- `=`는 같다는 뜻이 아니라 대입이다. SQL의 `WHERE num = 1`과 Java의 `x = 1`은 의미가 다르다.
- `Scanner.next()`는 공백 전까지만 읽고, `nextLine()`은 한 줄 전체를 읽는다.
- 오버로딩은 같은 이름을 매개변수 차이로 여러 번 정의하는 것이고, 오버라이딩은 상속받은 메서드를 자식 클래스에서 재정의하는 것이다.
- 생성자를 직접 만들면 기본 생성자가 사라질 수 있으므로, 상속 관계에서는 부모 기본 생성자와 `super(...)` 호출을 함께 봐야 한다.
- 업캐스팅 후에는 부모 타입에 보이는 멤버만 바로 사용할 수 있고, 자식 전용 기능은 안전한 다운캐스팅이 필요하다.
- 추상 클래스와 인터페이스는 모두 강제 규격을 만들 수 있지만, 추상 클래스는 공통 상태/기본 구현을 함께 둘 수 있고 인터페이스는 기능 규격 분리에 더 가깝다.

## 다음 과목과의 연결

Java에서 배운 “객체와 로직”은 Oracle에서 배울 “데이터 저장 구조”와 이어진다. 예를 들어 Java의 `Product` 객체는 메모리 안의 상품이고, Oracle의 `PRODUCTS` 테이블은 프로그램이 꺼져도 남는 상품 데이터 저장소다. 이후 Spring Boot에서는 Java 객체(Entity/DTO/Service)가 Oracle/MySQL 같은 DB의 테이블 데이터와 연결된다.

## 관련 페이지

- [[entities/java|Java]]
- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/2026.02.26(목)/2026.02.26(목).md`
- `raw/Study/1. Java/2026.02.27(금)/2026.02.27(금).md`
- `raw/Study/1. Java/2026.03.03(화)/2026.03.03(화).md`
- `raw/Study/1. Java/2026.03.04(수)/2026.03.04(수).md`
- `raw/Study/1. Java/2026.03.05(목)/2026.03.05(목).md`
- `raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/Study/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/Study/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/Study/1. Java/2026.03.13(금)/2026.03.13(금).md`
