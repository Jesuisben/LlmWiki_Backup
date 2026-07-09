---
title: 2026-03-10 Java 생성자, 오버로딩, 상속 입문
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-10 Java 생성자, 오버로딩, 상속 입문

## 한 줄 요약

객체 초기화를 담당하는 생성자, 매개변수 차이로 같은 이름을 여러 번 정의하는 오버로딩, 공통 속성을 부모 클래스로 일반화하는 상속을 배웠다.

## 커리큘럼 위치

- [[summaries/2026-03-09-java-class-object|클래스와 객체]]를 실제 설계 문법으로 확장한 날이다.
- 다음날 [[summaries/2026-03-11-java-inheritance-polymorphism|상속과 참조 형변환]]에서 `super`, 다운캐스팅, 오버라이딩으로 깊어진다.

## 배운 내용

- 기본 생성자는 눈에 보이지 않지만, 개발자가 생성자를 만들면 자동 기본 생성자는 사라진다.
- 생성자는 클래스 이름과 같고 반환 타입이 없다.
- 생성자의 목적은 멤버 변수 초기화다.
- 오버로딩은 같은 이름의 메서드/생성자를 매개변수 개수·타입·순서 차이로 여러 개 정의하는 것이다.
- 객체 배열은 `Product[] products = new Product[3]`처럼 객체 참조를 배열에 담는 구조다.
- 상속은 공통 속성과 동작을 수퍼클래스로 올려 중복을 줄이는 일반화 과정이다.

## 핵심 실습 / 예제

- `Product03()` 기본 생성자 작성
- 매개변수 있는 생성자로 필드 초기화
- `Product03[]` 배열에 여러 상품 객체 저장
- 음료 예제를 통해 `Beverage`를 부모로 두고 `Americano`, `Espresso` 같은 하위 클래스를 만드는 흐름 확인

## 헷갈린 점 / 질문

- 생성자는 메서드처럼 생겼지만 반환 타입이 없고 `new` 때 한 번 호출된다.
- 오버로딩은 “같은 클래스 안에서 같은 이름을 여러 방식으로 쓰는 것”이고, 오버라이딩은 “상속받은 메서드를 자식 클래스에서 다시 쓰는 것”이다.
- 객체 배열은 객체 자체를 통째로 복사해 담는 것이 아니라 객체의 참조를 담는다.

## 관련 페이지

- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]
- [[concepts/java-inheritance|Java 상속]]
- [[comparisons/overloading-vs-overriding|오버로딩 vs 오버라이딩]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.10(화)/2026.03.10(화).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
