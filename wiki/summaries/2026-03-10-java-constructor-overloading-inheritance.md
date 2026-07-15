---
title: 2026-03-10 Java 생성자, 오버로딩, 상속 입문
created: 2026-07-02
updated: 2026-07-15
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

- `new Product03("신라면", 100, "2026/03/01")`의 세 값이 생성자 매개변수로 이동하고, `this.name = name`처럼 현재 객체의 필드에 저장되는 경로를 추적했다.
- 기본 생성자와 매개변수 생성자를 함께 두어 생성자 오버로딩을 확인했다. 매개변수 개수나 타입이 다른 호출이 알맞은 생성자를 선택했다.
- `Product03[] itemlist = new Product03[2]`로 참조 칸을 만든 뒤 각 칸에 `new Product03(...)`를 대입하고, 반복문에서 `display()`를 호출했다. 두 번째 상품은 생성자 오버로딩을 통해 기본 단가 `500`을 사용했다.
- 마지막에는 `Animal`에 공통 필드를 올리고 `Dog`, `Cat`이 `extends Animal`로 상속받아 `display()`와 `toString()`을 재정의했다. 음료 계층과 `super(...)`의 본격 실습은 다음날 진행됐다.

## 헷갈린 점 / 질문

- 생성자는 메서드처럼 생겼지만 반환 타입이 없고 `new` 때 한 번 호출된다.
- 오버로딩은 “같은 클래스 안에서 같은 이름을 여러 방식으로 쓰는 것”이고, 오버라이딩은 “상속받은 메서드를 자식 클래스에서 다시 쓰는 것”이다.
- 객체 배열은 객체 자체를 통째로 복사해 담는 것이 아니라 객체의 참조를 담는다.
- 두 매개변수 생성자의 `this.price = price`는 같은 이름의 매개변수가 없어 사실상 필드 자기 대입이다. 단가 `500`은 필드 초기값에서 왔다.
- `productArray`를 순회하면서 조건에 `itemlist.length`를 사용한 원본 코드와 3개 출력 기록은 서로 맞지 않는다. 정제 위키에서는 코드와 출력이 일치한다고 단정하지 않는다.
- 생성자는 일반 메서드가 아니며, 상속받아 오버라이딩하는 대상도 아니다.

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
