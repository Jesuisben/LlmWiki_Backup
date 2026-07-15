---
title: Java 인터페이스 기능 설계
created: 2026-07-02
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
status: stable
confidence: high
---

# Java 인터페이스 기능 설계

## 정의

인터페이스 기능 설계는 클래스의 부모-자식 계층과 별개로 “어떤 기능을 수행할 수 있는가”를 작은 규격으로 나누어 붙이는 방식이다.

## 왜 중요한가

상속은 “무엇인가”의 관계를 표현하는 데 좋지만, 기능은 여러 방향으로 섞일 수 있다. Java는 클래스 다중 상속을 허용하지 않으므로 여러 기능 조합에는 인터페이스가 필요하다.

## 핵심 설명

```java
public interface WaterAdjustable {
    void adjustWater(double amount);
}

public interface ShotAddable {
    void addShot(int count);
}

public class SpecialCoffee05 extends Beverage05
        implements WaterAdjustable, ShotAddable, MilkAddable {
    public void adjustWater(double amount) { }
    public void addShot(int count) { }
    public void changeMilk(String milkType) { }
}
```

이런 식으로 음료가 공통적으로 `Beverage05` 계열에 속하면서도, 물 조절·샷 추가·우유 추가/변경처럼 제품별로 가능한 기능은 별도 인터페이스로 표현할 수 있다.

## 수업 예시

[[summaries/2026-03-12-java-abstract-interface-static|2026-03-12]]에는 한 개의 수퍼클래스와 `WaterAdjustable`, `ShotAddable`, `MilkAddable`을 함께 사용하는 예제가 등장했다. `SpecialCoffee05`처럼 여러 기능을 가진 클래스와, 일부 기능만 가진 음료 클래스를 같은 상속 계층 안에서 구분하는 연습이었다.

## 학습 연결과 범위

- **선행 개념:** [[concepts/java-inheritance|Java 상속]]과 [[concepts/java-polymorphism-casting|참조 형변환]]을 먼저 알아야 “공통 타입”과 “추가 기능 타입”을 구분할 수 있다.
- **Java 수업에서 직접 학습:** 음료별 기능 인터페이스 선언, `implements`, 메서드 오버라이딩, 인터페이스 타입 확인과 다운캐스팅.
- **이후 확장 관점:** Spring의 의존성 주입을 설명할 때도 “구현 클래스보다 계약을 먼저 본다”는 관점이 재등장하지만, 이 페이지의 코드는 03-12 음료 실습에 한정한다.

## 자주 헷갈리는 점

- 인터페이스는 “부모 클래스가 여러 개”라는 의미라기보다 “여러 기능 계약을 구현한다”는 의미로 이해하는 편이 안전하다.
- 인터페이스 타입으로 바라보면 그 인터페이스에 선언된 기능만 바로 사용할 수 있다.
- 실제 구현 클래스의 고유 기능이 필요하면 타입 확인과 형변환이 필요할 수 있다.

## 관련 개념

- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-polymorphism-casting|Java 다형성과 참조 형변환]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
