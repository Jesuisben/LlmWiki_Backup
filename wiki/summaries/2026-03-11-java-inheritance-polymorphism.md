---
title: 2026-03-11 Java 상속과 참조 형변환
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-11 Java 상속과 참조 형변환

## 한 줄 요약

상속에서 `private` 필드를 다루는 방법, `super(...)` 생성자 호출, 업캐스팅/다운캐스팅, `instanceof`, 오버라이딩을 배웠다.

## 커리큘럼 위치

- 전날 시작한 상속을 실제 설계·실행 흐름으로 확장했다.
- 다음날 [[summaries/2026-03-12-java-abstract-interface-static|추상 클래스·인터페이스·static/final]]에서 다형성과 추상화가 더 설계 중심으로 발전한다.

## 배운 내용

- 하위 패키지를 만들고 상속 예제를 구조화했다.
- `private` 멤버는 하위 클래스에서도 직접 접근할 수 없으므로 getter/setter, `protected`, 생성자 전달 등을 고려한다.
- 하위 클래스 생성자의 첫 줄에는 기본적으로 `super();`가 숨어 있다.
- 부모에 기본 생성자가 없으면 자식 생성자에서 `super(매개변수)`를 명시해야 한다.
- 업캐스팅은 자식 객체를 부모 타입 참조로 바라보는 것이다.
- 다운캐스팅은 다시 자식 타입으로 좁히는 것이며, 안전 확인에 `instanceof`를 쓴다.
- 오버라이딩으로 부모 메서드를 자식 클래스 상황에 맞게 재정의한다.

## 핵심 실습 / 예제

- `Beverage03` 수퍼클래스에 공통 필드 배치
- `Americano03`, `Espresso03` 등 하위 클래스에서 `super(...)`로 부모 생성자 호출
- 부모 타입 배열에 여러 음료 객체를 담고 반복문/조건문으로 구분
- `toString()` 오버라이딩으로 객체 출력 결과를 사람이 읽기 좋게 변경

## 헷갈린 점 / 질문

- 상속받았다는 말이 모든 필드를 직접 만질 수 있다는 뜻은 아니다. `private`은 클래스 내부에서만 직접 접근 가능하다.
- 다운캐스팅은 실제 객체가 그 타입일 때만 안전하다.
- `Object → 부모 → 자식` 순서로 메서드가 계속 오버라이딩될 수 있다.

## 관련 페이지

- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]
- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]

## 출처

- `raw/Study/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
