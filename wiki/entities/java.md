---
title: Java
created: 2026-06-30
updated: 2026-07-02
type: entity
tags: [java, backend, curriculum]
sources:
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
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---

# Java

## 무엇인가

Java는 객체지향 프로그래밍 언어이며, 이 위키에서는 국비지원 웹서비스 풀스택 과정의 첫 번째 주요 학습 언어다. 이후 Spring, Spring Boot, JPA, 백엔드 API 구현을 배우기 위한 기반 언어로 쓰인다.

## 이 위키에서의 맥락

Java는 2026-02-26 오리엔테이션과 개발 도구 준비에서 시작해, 2026-03-13 Oracle 학습으로 넘어가기 전까지 프로그래밍 기초와 객체지향의 핵심 문법을 익히는 구간이었다.

처음에는 변수, 자료형, 연산자처럼 “코드 한 줄이 어떻게 계산되는가”를 배웠고, 이후 조건문/반복문/배열로 “실행 흐름과 데이터 묶음”을 다뤘다. 마지막에는 클래스, 객체, 생성자, 상속, 추상 클래스, 인터페이스, static/final을 배우며 Spring 백엔드로 이어질 객체지향 기초를 만들었다.

## 학습 이력

| 날짜 | 학습 흐름 | 관련 페이지 |
|---|---|---|
| 2026-02-26 | 교육 과정 OT와 IntelliJ IDEA 설치 준비 | [[summaries/2026-02-26-orientation|오리엔테이션과 개발 환경 준비]] |
| 2026-02-27 | 기본 자료형, 변수 선언/대입, 출력, 연산자 | [[summaries/2026-02-27-java-basic-types-operators|Java 기본 자료형과 연산자]] |
| 2026-03-03 | 비교/논리/조건 연산자, 삼항 연산자 | [[summaries/2026-03-03-java-logic-ternary|Java 논리 연산자와 조건 연산자]] |
| 2026-03-04 | `if`, `if-else`, `switch` 조건 분기 | [[summaries/2026-03-04-java-control-flow|Java 제어문과 조건문]] |
| 2026-03-05 | `for`, `while`, 누적 합계 | [[summaries/2026-03-05-java-for-while|Java for문과 while문]] |
| 2026-03-06 | 무한 while, `Scanner`, 배열 | [[summaries/2026-03-06-java-while-array|Java 무한 while과 배열]] |
| 2026-03-09 | 클래스, 객체, 멤버 변수/메서드, getter/setter | [[summaries/2026-03-09-java-class-object|Java 클래스와 객체]] |
| 2026-03-10 | 생성자, 오버로딩, 객체 배열, 상속 입문 | [[summaries/2026-03-10-java-constructor-overloading-inheritance|Java 생성자, 오버로딩, 상속 입문]] |
| 2026-03-11 | 상속, `super`, 참조 형변환, 오버라이딩 | [[summaries/2026-03-11-java-inheritance-polymorphism|Java 상속과 참조 형변환]] |
| 2026-03-12 | 추상 클래스, 인터페이스, static/final | [[summaries/2026-03-12-java-abstract-interface-static|Java 추상 클래스, 인터페이스, static/final]] |
| 2026-03-13 | Java 팀 프로젝트와 Oracle 전환 | [[summaries/2026-03-13-java-project-oracle-start|Java 팀 프로젝트와 Oracle 시작]] |

## Java 총정리/숙제에서 추가로 보강된 관점

`Java 총정리.md`는 문장 끝 세미콜론, 출력, 형변환, 조건/반복/배열, 객체 생성, 생성자, `this`, 오버로딩, 상속, 오버라이딩, `super`, 참조 형변환, `instanceof`, 추상 메서드, 인터페이스, static/final을 한 번에 복습한다.

`클래스 숙제 완료.md`는 클래스 학습에 필요한 배경지식으로 static/stack/heap, 접근 지정자, getter/setter, 생성자, 상속, 추상 클래스, 인터페이스, 컬렉션을 조사했다. 이 내용은 Java 문법을 단순 암기에서 “왜 이런 구조가 필요한가”로 끌어올리는 복습 자료다.

## 관련 개념

- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-operators|Java 연산자]]
- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-array|Java 배열]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]
- [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]
- [[comparisons/array-vs-collection|배열 vs 컬렉션]]

## 프로젝트/면접에서 설명할 관점

1. 기본 문법: 타입, 변수, 연산자, 조건문, 반복문으로 코드 실행 흐름을 만들었다.
2. 자료 묶음: 배열로 같은 타입의 값을 묶고, 클래스/객체로 여러 속성과 동작을 하나의 타입으로 만들었다.
3. 객체지향: 생성자, 캡슐화, 상속, 오버라이딩, 추상 클래스, 인터페이스로 재사용성과 확장성을 배웠다.
4. 백엔드 연결: 이 객체지향 감각이 Spring Boot의 DTO, Entity, Service, Repository 구조로 이어진다.

## 출처

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
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
