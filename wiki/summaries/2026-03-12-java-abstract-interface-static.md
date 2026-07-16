---
title: 2026-03-12 Java 추상 클래스, 인터페이스, static/final
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-12 Java 추상 클래스, 인터페이스, static/final

## 한 줄 요약

향상된 for, 다른 패키지 import, 추상 메서드, 인터페이스, `static`, `final`을 배우며 객체지향 설계를 마무리했다.

## 커리큘럼 위치

- Java 문법 수업의 객체지향 핵심 마무리 구간이다.
- 다음날 [[summaries/2026-03-13-java-project-oracle-start|팀 프로젝트와 Oracle 시작]]으로 넘어가며, Java 지식은 이후 Spring Boot 백엔드 학습의 기반이 된다.

## 배운 내용

- 향상된 for문은 배열/컬렉션 요소를 처음부터 끝까지 순차적으로 꺼낼 때 쓴다.
- 다른 패키지의 클래스를 쓰려면 `import`가 필요하고, 접근 대상이 `public`이어야 한다.
- 추상 메서드는 선언만 있고 구현은 하위 클래스에 맡긴다.
- 추상 클래스는 공통 상태와 일부 구현을 가질 수 있지만 직접 객체 생성은 할 수 없다.
- 인터페이스는 기능 규격을 정의하고, 클래스는 `implements`로 여러 인터페이스를 구현할 수 있다.
- `static`은 객체마다가 아니라 클래스 차원에 붙는 공용 멤버를 표현한다.
- `final`은 값 변경 금지, 오버라이딩 금지, 상속 금지 등 “변경 불가” 의미로 쓰인다.

## 핵심 실습 / 예제

- `for(String item : bts)` 형태의 향상된 for문
- `import ch04_class.Product01`로 다른 패키지 클래스 사용
- `Beverage05`에 `drink()` 추상 메서드를 두어 모든 구체 음료가 마시는 동작을 구현하도록 강제했다.
- `WaterAdjustable`, `ShotAddable`, `MilkAddable`로 물 조절·샷 추가·우유 추가/변경 기능을 분리하고, `SpecialCoffee05`처럼 필요한 인터페이스 여러 개를 구현했다.
- 음료 배열을 반복하면서 실제 타입을 확인해 `adjustWater`, `addShot`, `addMilk` 같은 자식 기능을 호출했고, 뒤의 `SpecialCoffee05` 실습에서는 `changeMilk` 규격으로 우유 타입 변경을 구현했다.
- 가게 이름이나 커피 잔수처럼 공통으로 공유할 값은 `static`, 바뀌면 안 되는 값·메서드·클래스는 `final`로 구분했다.
- `Beverage05` 생성자에서 `beverageCount++`를 실행해 자식 음료 객체가 만들어질 때마다 공용 주문 수가 증가하고, static getter로 객체 없이 조회하는 흐름을 확인했다.
- `Cappuccino05`와 `FoamAddable`을 추가해 새 음료 기능을 기존 계층에 확장하는 연습도 했다.

## 헷갈린 점 / 질문

- 향상된 for문은 인덱스가 중요하지 않을 때 간결하지만, 특정 위치를 수정해야 할 때는 일반 for문이 더 적합하다.
- Java 클래스 상속은 단일 상속이지만, 인터페이스 구현은 여러 개 가능하다.
- `static` 필드는 객체마다 따로 있는 값이 아니라 클래스가 공유하는 값이다.
- 이 날짜의 직접 실습은 음료 상속 계층과 기능 인터페이스다. Spring 서비스 인터페이스·의존성 주입은 같은 원리를 나중에 확장해 보는 관점이며 이날 구현 범위는 아니다.
- 인터페이스 메서드를 추상 계약으로만 작성한 것은 이날 수업 범위다. 현대 Java 인터페이스 전체를 설명할 때는 `default`, `static`, `private` 메서드도 있다는 점을 별도로 구분해야 한다.
- 이날 직접 확인한 `final`의 중심은 `static final` 상수다. final 메서드·클래스는 숙제 조사/확장 범위로 구분한다.

## 관련 페이지

- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
