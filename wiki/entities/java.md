---
title: Java
created: 2026-07-02
updated: 2026-07-13
type: entity
tags: [java, backend, curriculum]
sources:
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
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# Java

## 무엇인가

Java는 클래스 기반 객체지향 프로그래밍 언어이며, 이 위키에서는 백엔드 개발과 Spring Boot 학습의 출발점이다.

## 이 위키에서의 맥락

사용자는 2026-02-26부터 Java를 배우기 시작했다. 첫 흐름은 IntelliJ에서 프로젝트·패키지·클래스를 만들고 출력문을 실행하는 것이었고, 이후 변수/자료형/연산자, 제어문, 배열, 클래스/객체, 생성자, 상속, 다형성, 추상 클래스, 인터페이스, `static`/`final`까지 이어졌다.

이 과목의 핵심은 “코드를 실행하는 문법”에서 “현실의 업무 대상을 객체로 설계하는 사고”로 이동하는 것이다. Java의 `Product`, `Beverage`, `Animal` 예시는 이후 Spring Boot에서 Entity, DTO, Service 같은 객체를 이해하는 기초가 된다.

## 날짜별 학습 이력

- [[summaries/2026-02-26-orientation|2026-02-26]]: IntelliJ, 프로젝트/패키지/클래스, 첫 출력
- [[summaries/2026-02-27-java-basic-types-operators|2026-02-27]]: 변수, 자료형, 산술/대입/증감 연산자, GitHub 초기 설정
- [[summaries/2026-03-03-java-logic-ternary|2026-03-03]]: 비교·논리·부정·삼항 연산자와 형변환 감각
- [[summaries/2026-03-04-java-control-flow|2026-03-04]]: `if`, `else`, `switch`로 실행 흐름 분기
- [[summaries/2026-03-05-java-for-while|2026-03-05]]: `for`, `while`, 누적 합계와 홀짝 합계
- [[summaries/2026-03-06-java-while-array|2026-03-06]]: `Scanner`, 무한 반복, 배열 생성/초기화
- [[summaries/2026-03-09-java-class-object|2026-03-09]]: 클래스, 객체, 필드, 메서드, getter/setter
- [[summaries/2026-03-10-java-constructor-overloading-inheritance|2026-03-10]]: 생성자, `this`, 오버로딩, 객체 배열, 상속 입문
- [[summaries/2026-03-11-java-inheritance-polymorphism|2026-03-11]]: 상속, `super`, 오버라이딩, 참조 형변환, `instanceof`
- [[summaries/2026-03-12-java-abstract-interface-static|2026-03-12]]: 추상 클래스, 인터페이스, 향상된 for, `static`, `final`
- [[summaries/2026-03-13-java-project-oracle-start|2026-03-13]]: Java 팀 프로젝트 후 Oracle 학습으로 전환
- [[summaries/2026-03-13-java-subject-review|Java 총정리]]: Java 입문 전체를 과목 단위로 다시 묶은 복습 허브

## 핵심 기능 / 특징

- 클래스와 객체를 중심으로 코드를 구성한다.
- 기본 자료형과 참조 자료형을 구분한다.
- `if`, `switch`, `for`, `while`로 실행 흐름을 제어한다.
- 배열과 객체 배열로 여러 값을 묶어 처리한다.
- 접근 지정자, getter/setter, 생성자로 객체 상태를 통제한다.
- 상속, 오버라이딩, 다형성으로 공통 구조를 재사용한다.
- 추상 클래스와 인터페이스로 강제 규격과 기능 분리를 설계한다.
- `static`/`final`로 클래스 소속 멤버와 상수를 구분한다.

## 복습 경로

1. 문법 기초가 헷갈리면 [[concepts/java-basic-types|Java 기본 자료형]], [[concepts/java-operators|Java 연산자]], [[concepts/java-conditional-logic|Java 조건 판단]]을 먼저 본다.
2. 반복/배열 문제가 헷갈리면 [[concepts/java-loop|Java 반복문]], [[concepts/java-array|Java 배열]], [[comparisons/array-vs-collection|배열 vs 컬렉션]]을 본다.
3. 객체 설계가 헷갈리면 [[concepts/java-class-object|Java 클래스와 객체]], [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]], [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]을 본다.
4. 상속 이후가 헷갈리면 [[concepts/java-inheritance|Java 상속]], [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]], [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]], [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]]을 본다.
5. 공유 값/상수가 헷갈리면 [[concepts/java-memory-static-final|Java 메모리, static, final]]을 본다.

## 다음 과목과의 연결

Java에서 객체를 설계하고 로직을 작성하는 법을 배운 뒤, [[entities/oracle-database|Oracle Database]]에서 그 객체들이 다루는 데이터를 테이블로 저장하는 법을 배웠다. 이후 [[entities/spring-boot|Spring Boot]]에서는 Java 객체와 DB 테이블이 Entity/Repository/Service/Controller 계층으로 연결된다.

## 관련 개념

- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/KoreaICT/1. Java` 사용자 정리 MD 전체
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
