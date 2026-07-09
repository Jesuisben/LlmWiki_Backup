---
title: 오버로딩 vs 오버라이딩
created: 2026-07-02
updated: 2026-07-03
type: comparison
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 오버로딩 vs 오버라이딩

## 비교 목적

두 용어 모두 “같은 이름”과 관련되어 헷갈리기 쉽다. 오버로딩은 같은 클래스 안에서 이름을 여러 방식으로 정의하는 것이고, 오버라이딩은 상속받은 메서드를 자식 클래스에서 다시 정의하는 것이다.

## 한눈에 보기

| 항목 | 오버로딩 | 오버라이딩 |
|---|---|---|
| 위치 | 같은 클래스 안 | 부모-자식 상속 관계 |
| 기준 | 매개변수 개수·타입·순서 차이 | 부모 메서드 시그니처와 호환 |
| 목적 | 다양한 입력 방식 제공 | 자식 클래스 상황에 맞게 동작 변경 |
| 수업 예 | 생성자 여러 개 | `toString()` 재정의, 음료별 출력 |
| 연결 개념 | 생성자, 메서드 | 상속, 다형성 |

## 언제 무엇을 쓰는가

- 객체를 여러 방식으로 만들고 싶으면 생성자 오버로딩을 쓴다.
- 부모의 기본 동작을 자식 객체에 맞게 바꾸고 싶으면 오버라이딩을 쓴다.

## 헷갈리기 쉬운 포인트

- 오버로딩은 반환 타입만 다르게 해서는 성립하지 않는다.
- 오버라이딩은 부모 메서드와 이름·매개변수 구조가 맞아야 한다.
- 다형성에서는 부모 타입으로 호출해도 실제 자식 객체의 오버라이딩 메서드가 실행될 수 있다.

## 관련 페이지

- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
