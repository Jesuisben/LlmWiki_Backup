---
title: Java 접근 지정자와 캡슐화
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.09(월)/2026.03.09(월).md
  - raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
status: stable
confidence: high
---

# Java 접근 지정자와 캡슐화

## 정의

접근 지정자(access modifier)는 클래스·필드·메서드를 어느 범위에서 사용할 수 있는지 정한다. 캡슐화(encapsulation)는 객체의 내부 상태를 무조건 공개하지 않고, 공개한 메서드를 통해 읽기·쓰기 규칙을 관리하는 설계 원칙이다.

## 왜 중요한가

03-09 `Product` 실습에서 필드를 `private`으로 바꾸자 main에서 직접 접근할 수 없었고 getter/setter가 필요해졌다. 03-11 상속에서는 부모의 `private` 필드를 자식도 직접 사용할 수 없어 생성자와 공개 메서드로 값을 전달했다. 접근 범위는 클래스 한 파일의 문제가 아니라 객체 설계와 상속을 연결한다.

## 핵심 설명

| 지정자 | 같은 클래스 | 같은 패키지 | 다른 패키지의 자식 | 그 밖의 외부 |
|---|---:|---:|---:|---:|
| `public` | O | O | O | O |
| `protected` | O | O | O | 상속 관계에서 제한적으로 접근 |
| package-private | O | O | X | X |
| `private` | O | X | X | X |

package-private는 별도 키워드를 쓰는 것이 아니라 접근 지정자를 생략한 상태다.

## 수업 예시

```java
public class Product03 {
    private String name;
    private int price;

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
}
```

- `private price`: 외부 코드가 필드에 직접 쓰지 못하게 한다.
- `getPrice()`: 공개 메서드가 현재 값을 반환한다.
- `setPrice(int price)`: 외부 값을 받아 객체 내부 필드에 저장한다.
- `this.price = price`: 왼쪽은 현재 객체의 필드, 오른쪽은 메서드가 받은 매개변수다.

setter는 단순 대입만 해야 하는 문법이 아니다. 필요하면 음수 가격 거부처럼 유효성 검사 지점으로 사용할 수 있다. 다만 이 검증 코드는 수업에서 직접 구현한 결과가 아니라 캡슐화의 후속 설계 관점이다.

## 상속에서의 접근

부모 객체의 `private` 필드는 자식 객체에도 상태로 존재할 수 있지만, 자식 클래스 소스에서 직접 접근할 수는 없다. 03-11 음료 실습처럼 `super(name, price)`로 부모 생성자에 값을 전달하고, 부모가 제공한 getter나 메서드를 이용한다.

## 자주 헷갈리는 점

- `private`은 값을 없애는 키워드가 아니라 직접 접근 가능한 범위를 같은 클래스로 제한한다.
- getter가 private 값을 public 값으로 “변환”하는 것이 아니다. 공개 메서드가 해당 값을 반환하는 것이다.
- 모든 필드에 setter를 자동으로 만들면 캡슐화가 완성되는 것이 아니다. 변경을 허용할 값과 규칙을 결정해야 한다.
- `protected`는 “모든 자식이 어디서나 자유 접근”이라는 뜻으로 단순화하면 안 된다. 같은 패키지 여부와 다른 패키지 상속 접근 규칙을 함께 본다.
- 필드와 지역 변수의 자동 초기화 규칙은 다르다. 지역 변수는 사용 전에 직접 초기화해야 한다.

## 학습 연결과 범위

- **선행:** [[concepts/java-class-object|Java 클래스와 객체]]
- **직접 수업:** 03-09 `Product`의 `private`·getter/setter, 03-11 부모 `private` 필드와 생성자 전달.
- **후속:** [[concepts/java-inheritance|Java 상속]], Spring Entity/DTO의 공개 범위와 객체 상태 변경 규칙.
- Spring의 Entity 설계는 후속 확장 관점이며, 이 페이지의 직접 근거는 Java `Product`와 음료 상속 실습이다.

## 관련 개념

- [[concepts/java-method-constructor-overloading|Java 메서드, 생성자, this, 오버로딩]]
- [[concepts/java-inheritance|Java 상속]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]
- [[summaries/java-homework-research-review|Java 클래스 숙제와 사전조사 정리]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.09(월)/2026.03.09(월).md`
- `raw/KoreaICT/1. Java/2026.03.11(수)/2026.03.11(수).md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
