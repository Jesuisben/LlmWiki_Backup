---
title: 2026-03-12 Java 추상 클래스, 인터페이스, static/final
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/Study/1. Java/Java 총정리/Java 총정리.md
  - raw/Study/1. Java/숙제/클래스 숙제 완료.md
  - raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf
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
- 음료 예제에서 추상 메서드와 인터페이스를 이용해 기능 규격 분리
- 가게 이름 같은 공통 값을 `static` 변수로 두고, 변하지 않는 값은 `final`로 고정

## 헷갈린 점 / 질문

- 향상된 for문은 인덱스가 중요하지 않을 때 간결하지만, 특정 위치를 수정해야 할 때는 일반 for문이 더 적합하다.
- Java 클래스 상속은 단일 상속이지만, 인터페이스 구현은 여러 개 가능하다.
- `static` 필드는 객체마다 따로 있는 값이 아니라 클래스가 공유하는 값이다.

## 관련 페이지

- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]]
- [[concepts/java-memory-static-final|Java 메모리, static, final]]
- [[comparisons/interface-vs-abstract-class|인터페이스 vs 추상 클래스]]

## 출처

- `raw/Study/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/Study/1. Java/Java 총정리/Java 총정리.md`
- `raw/Study/1. Java/숙제/클래스 숙제 완료.md`
- `raw/Study/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
