---
title: Java 총정리
type: summary
created: 2026-07-03
updated: 2026-07-03
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
status: growing
confidence: high
---

# Java 총정리

## 한 줄 요약

`Java 총정리`는 2026-02-26부터 2026-03-13까지 배운 Java 입문 흐름을 “문법 → 제어 흐름 → 배열 → 클래스/객체 → 상속/추상화” 순서로 다시 묶은 복습 노트다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-02-26-orientation|2026-02-26 오리엔테이션과 개발 환경 준비]]부터 [[summaries/2026-03-12-java-abstract-interface-static|2026-03-12 Java 추상 클래스, 인터페이스, static/final]]까지의 날짜별 수업 노트
- 다음 흐름: [[summaries/2026-03-13-java-project-oracle-start|2026-03-13 Java 팀 프로젝트와 Oracle 시작]]에서 Java 프로젝트를 거쳐 [[entities/oracle-database|Oracle Database]] 학습으로 이동
- 역할: 날짜별 수업 요약을 대체하는 새 진도 페이지가 아니라, 기존 Java 개념 페이지를 다시 찾기 위한 복습 허브

## 배운 내용

### 1. Java 프로그램의 기본 모양

초반부는 프로젝트, 패키지, 클래스, 인터페이스, `main` 메서드, 세미콜론, 중괄호 같은 Java 파일의 외형을 정리한다. Java는 모든 실행 흐름이 클래스 안에서 출발하므로, 이후 [[concepts/java-class-object|Java 클래스와 객체]]를 이해하기 위한 문법적 바탕이 된다.

### 2. 변수, 자료형, 형변환

`char`, `String`, `int`, `double`, `boolean`을 중심으로 값의 종류를 나누고, 변수 선언·대입·덮어쓰기·식별자 규칙을 정리한다. 특히 `String`은 수업에서는 기본처럼 자주 쓰지만 실제로는 객체이므로 [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]에서 다시 비교해야 한다.

### 3. 연산자와 제어문

산술/대입/비교/논리/삼항 연산자 이후 `if`, `switch`, `for`, `while`, `break`, 입력 함수로 이어진다. 총정리에는 “경우의 수를 나누는 선택문”과 “반복해서 계산하는 반복문”이라는 관점이 남아 있어 [[concepts/java-conditional-logic|Java 조건 판단]], [[concepts/java-loop|Java 반복문]]의 복습 출처로 적합하다.

### 4. 배열과 객체 배열

배열은 0번 인덱스부터 시작하며 “이름, 타입, 요소 개수”를 가진 고정 길이 자료구조로 정리되어 있다. 뒤쪽의 객체 배열 예시는 단순 값 배열에서 여러 객체를 묶어 다루는 흐름으로 넘어가는 다리 역할을 하며, 이후 컬렉션 학습 전 [[comparisons/array-vs-collection|배열 vs 컬렉션]]을 볼 때 기준점이 된다.

### 5. 클래스, 메서드, 생성자, 오버로딩

클래스는 필드와 메서드를 묶어 사용자 정의 타입을 만드는 단위로 정리된다. `getter/setter`, 접근 지정자, 생성자, `this`, 오버로딩은 “객체를 어떻게 만들고 안전하게 다루는가”라는 하나의 흐름으로 봐야 한다. 관련 페이지는 [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]이다.

### 6. 상속, 오버라이딩, 일반화, 생성자 오류

후반부는 Beverage 예시를 중심으로 상속, 오버라이딩, 일반화, 부모 생성자 호출 문제를 다룬다. 특히 “매개변수 생성자를 직접 만들면 기본 생성자가 자동 생성되지 않는다”는 설명은 상속에서 `super()` 호출 오류를 이해하는 데 중요하다.

## 헷갈린 점 / 질문

- `String`은 자주 쓰지만 기본 자료형이 아니라 참조 자료형이다.
- “오버로딩”은 같은 클래스 안에서 매개변수 구성이 다른 같은 이름의 메서드/생성자를 여러 개 두는 것이고, “오버라이딩”은 부모 메서드를 자식 클래스에 맞게 재정의하는 것이다. 자세한 비교는 [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]] 참고.
- 생성자를 하나라도 직접 만들면 Java가 기본 생성자를 자동으로 만들어주지 않는다. 그래서 자식 생성자의 묵시적 `super()`가 부모의 없는 기본 생성자를 찾다가 오류가 날 수 있다.
- 클래스/인터페이스/추상 클래스는 모두 “설계”와 관련되지만 역할이 다르다. 비교는 [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]] 참고.

## 관련 페이지

- [[entities/java|Java]]
- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]

## 출처

- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
