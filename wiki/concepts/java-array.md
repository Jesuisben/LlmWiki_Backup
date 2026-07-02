---
title: Java 배열
created: 2026-06-30
updated: 2026-07-02
type: concept
tags: [java]
sources:
  - raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
status: growing
confidence: high
---

# Java 배열

## 정의

Java 배열은 같은 타입의 여러 값을 순서가 있는 하나의 묶음으로 관리하는 자료구조다. 수업에서는 “방이 여러 개 있는 하나의 이름”처럼 설명되었고, 배열의 3요소를 이름, 타입, 요소 개수로 정리했다.

## 왜 중요한가

변수 하나에는 값 하나만 담을 수 있다. 학생 점수 3개, BTS 멤버 7명, 주문한 음료 여러 개처럼 같은 성격의 값이 여러 개 있으면 변수 이름을 계속 늘리는 것보다 배열로 묶는 편이 낫다. 배열을 배우면 [[concepts/java-loop|Java 반복문]]으로 여러 값을 한 번에 처리할 수 있고, 이후 객체 배열·컬렉션·JavaScript 배열·React 목록 렌더링으로 이어진다.

## 핵심 설명

### 배열은 0번부터 시작한다

수업에서 가장 먼저 강조한 점은 배열 인덱스가 1이 아니라 0부터 시작한다는 것이다.

```java
int[] arr = new int[3];

arr[0] = 4;
arr[1] = 11;
arr[2] = 7;
```

요소 개수가 3개이면 사용할 수 있는 인덱스는 `0`, `1`, `2`다. `arr[3]`은 네 번째 칸을 의미하므로 이 배열에는 존재하지 않는다. ^[raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md]

### 생성 방식 1: new 연산자

요소 개수는 알지만 값이 아직 정해지지 않았거나, 입력을 받아 채울 때는 `new` 연산자를 쓴다.

```java
// 타입[] 배열이름 = new 타입[요소개수];
int[] arr = new int[3];
```

수업에서는 `arr[0]`, `arr[2]`, `arr[1]` 순서로 값을 넣고 반복문으로 출력했다.

```java
int x = 3;
int y = 5;
int[] arr = new int[3];

arr[0] = x - y + 6;       // 4
arr[2] = arr[0] + 3;      // 7
arr[1] = arr[0] + arr[2]; // 11

for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

출력 순서는 대입한 순서가 아니라 인덱스 순서이므로 `4`, `11`, `7`이 출력된다. ^[raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md]

### 생성 방식 2: 초기화 기법

요소의 개수와 값이 이미 명확하면 중괄호로 바로 만들 수 있다.

```java
int[] brr = {15, 30, 22};
String[] bts = {"진", "뷔", "정국", "rm", "지민", "슈가", "제이홉"};
```

수업에서는 BTS 멤버 목록을 `new String[7]`로 하나씩 넣는 방식과, 초기화 기법으로 한 번에 만드는 방식을 비교했다. 값이 고정되어 있으면 초기화 기법이 훨씬 짧다. ^[raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md]

### `length`는 반복문과 함께 쓴다

배열 요소 개수는 `배열이름.length`로 확인한다.

```java
for (int i = 0; i < bts.length; i++) {
    System.out.println(bts[i]);
}
```

배열 길이를 직접 숫자로 쓰면 배열 크기가 바뀔 때 반복문도 같이 고쳐야 한다. 그래서 수업 예제처럼 `length`를 쓰는 습관이 중요하다.

### 입력값을 배열에 담고 동시에 계산할 수 있다

배열 문제에서는 사용자가 입력한 개수만큼 정수 배열을 만들고, 각 값을 입력받으며 홀수/짝수 합계를 나눴다.

```java
Scanner scan = new Scanner(System.in);
System.out.print("배열 요소 개수 입력 : ");
int size = scan.nextInt();

int[] jumsu = new int[size];
int odd = 0, even = 0;

for (int i = 0; i < jumsu.length; i++) {
    System.out.print(i + "번째 정수 입력 : ");
    jumsu[i] = scan.nextInt();

    if (jumsu[i] % 2 == 1) {
        odd += jumsu[i];
    } else {
        even += jumsu[i];
    }
}
```

이 예제는 배열, 반복문, 조건문, 입력 함수가 한 번에 결합된 중요한 실습이다. ^[raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md]

### 배열은 객체도 담을 수 있다

뒤 수업에서는 `Beverage05[] orderList`처럼 부모 타입 배열에 여러 자식 객체를 담았다.

```java
Beverage05[] orderList = {
    new Americano05("아메리카노", 4000.0, 200),
    new Espresso05("에스프레소", 3000.0, 1),
    new Latte05("라떼", 6000.0, "아몬드 우유")
};
```

이 예제는 배열이 단순히 숫자나 문자열만 담는 것이 아니라 객체 참조도 담을 수 있음을 보여준다. 동시에 [[concepts/java-inheritance|Java 상속]]의 업캐스팅, [[concepts/java-abstract-interface|추상 클래스와 인터페이스]]와도 연결된다. ^[raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md]

## 자주 헷갈리는 점

### 배열의 “요소 개수”와 “마지막 인덱스”는 다르다

요소 개수가 7개이면 마지막 인덱스는 6이다. 그래서 반복 조건은 보통 `i <= arr.length`가 아니라 `i < arr.length`다.

### new 방식과 초기화 기법은 목적이 다르다

- `new int[3]`: 칸 수를 먼저 정하고 값은 나중에 채운다.
- `{15, 30, 22}`: 값과 개수가 이미 정해져 있을 때 한 번에 만든다.

### 배열은 같은 타입만 담는다

`int[]`에는 정수만, `String[]`에는 문자열만 담는다. 여러 종류의 정보를 함께 묶고 싶다면 이후에 배우는 클래스와 객체를 사용해야 한다.

## 이전/이후 학습과의 연결

- 이전: [[concepts/java-loop|Java 반복문]]으로 여러 값을 반복 처리하는 방법을 배웠다.
- 이후: [[concepts/java-class-object|Java 클래스와 객체]]에서는 여러 필드를 하나의 객체로 묶는다.
- 이후: 객체 배열과 향상된 for문은 [[concepts/java-inheritance|Java 상속]]과 다형성 예제에서 중요해진다.
- 프론트엔드: JavaScript 배열과 `forEach`는 상품 목록을 화면에 렌더링할 때 다시 등장한다.

## 관련 개념

- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-conditional-logic|Java 조건 판단]]
- [[concepts/java-class-object|Java 클래스와 객체]]
- [[concepts/java-inheritance|Java 상속]]
- [[summaries/2026-03-06-java-while-array|2026-03-06 Java 무한 while과 배열]]
- [[summaries/2026-03-12-java-abstract-interface-static|2026-03-12 Java 추상 클래스, 인터페이스, static/final]]

## 출처

- `raw/Study/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
