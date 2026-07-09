---
title: 2026-02-26 오리엔테이션과 개발 환경 준비
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.02.26(목)/2026.02.26(목).md
  - raw/KoreaICT/1. Java/교육 자료/IntelliJ 교안.pdf
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-02-26 오리엔테이션과 개발 환경 준비

## 한 줄 요약

국비지원 과정 첫날에는 수업 운영 규칙을 확인한 뒤 IntelliJ IDEA에서 Java 프로젝트·패키지·클래스를 만들고 `System.out.println()`으로 첫 출력을 실행했다.

## 커리큘럼 위치

- Java 과정의 출발점이다.
- 이후 [[summaries/2026-02-27-java-basic-types-operators|2026-02-27 변수·자료형·연산자]]로 이어지며, “프로젝트 → 패키지 → 클래스 → main 메서드” 구조가 모든 Java 실습의 기본 틀이 된다.

## 배운 내용

- 출결, 조퇴·외출·휴가 규칙, 시험/프로젝트 반영 방식 등 과정 운영 방식을 확인했다.
- Chrome, IntelliJ IDEA, Git 관련 도구 등 개발 환경을 준비했다.
- IntelliJ에서 `New Project`, `Package`, `Java Class`를 만들고 첫 Java 파일을 실행했다.
- Java 프로그램은 최소한 클래스 안에 `main` 메서드가 있어야 실행 출발점을 가진다는 점을 확인했다.
- 세미콜론은 문장의 끝에 붙지만 클래스/메서드 바디 `{}` 자체 뒤에는 붙이지 않는다는 규칙을 익혔다.

## 핵심 실습 / 예제

- 프로젝트: `MyJava`
- 패키지: `ch01_variable_operator`
- 클래스: `MyPrint`, `YourPrint`
- 출력: `System.out.println("hello")`, `System.out.println("world")`

이날 실습은 단순 출력이지만, 이후 모든 수업 코드가 “패키지 안의 클래스, 클래스 안의 `main`, `main` 안의 실행문” 구조로 작성된다는 점에서 중요하다.

## 헷갈린 점 / 질문

- 원본에는 `static void main()`처럼 `String[] args`가 빠진 예시도 등장한다. 실제 IntelliJ 자동 생성 기본형은 `public static void main(String[] args)`이며, 학습 초기에는 “실행 시작점”이라는 의미를 먼저 잡는 단계로 보면 된다.
- `String`은 교안/노트에서 문자열형처럼 다루지만, Java 문법상 기본 자료형이 아니라 클래스 기반 참조 자료형이다. 이 차이는 [[comparisons/primitive-vs-reference-types|기본 자료형 vs 참조 자료형]]에서 다시 정리한다.

## 관련 페이지

- [[entities/intellij-idea|IntelliJ IDEA]]
- [[entities/java|Java]]
- [[concepts/java-basic-types|Java 기본 자료형]]
- [[concepts/java-class-object|Java 클래스와 객체]]

## 출처

- `raw/KoreaICT/1. Java/2026.02.26(목)/2026.02.26(목).md`
- `raw/KoreaICT/1. Java/교육 자료/IntelliJ 교안.pdf`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
