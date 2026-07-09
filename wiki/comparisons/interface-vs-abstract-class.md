---
title: 인터페이스 vs 추상 클래스
created: 2026-07-02
updated: 2026-07-03
type: comparison
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
  - raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 인터페이스 vs 추상 클래스

## 비교 목적

Java에서 둘 다 “직접 완성 객체를 만들기보다 하위 클래스/구현 클래스에 규격을 주는 도구”라 헷갈리기 쉽다. 핵심은 추상 클래스는 공통 부모, 인터페이스는 기능 계약이라는 점이다.

## 한눈에 보기

| 항목 | 추상 클래스 | 인터페이스 |
|---|---|---|
| 핵심 의미 | 공통 부모 설계도 | 기능 규격/계약 |
| 키워드 | `abstract class` | `interface`, `implements` |
| 객체 생성 | 직접 생성 불가 | 직접 생성 불가 |
| 필드/상태 | 공통 필드와 생성자 가능 | 주로 상수/규격 중심 |
| 메서드 | 일반 메서드 + 추상 메서드 | 구현해야 할 기능 선언 중심 |
| 다중 사용 | 클래스는 하나만 상속 | 여러 인터페이스 구현 가능 |
| 수업 맥락 | 음료 공통 구조 | 음료가 할 수 있는 기능 분리 |

## 언제 무엇을 쓰는가

- 여러 클래스가 공통 상태와 기본 구현을 공유해야 하면 추상 클래스가 적합하다.
- 서로 다른 계층의 클래스에 같은 기능 규격을 붙이고 싶으면 인터페이스가 적합하다.

## 헷갈리기 쉬운 포인트

- 인터페이스를 “다중상속”이라고 표현할 수는 있지만, 실제로는 여러 부모 구현을 물려받는다기보다 여러 기능 계약을 구현한다고 이해하는 편이 안전하다.
- 추상 클래스는 상속 계층을 설계하고, 인터페이스는 기능 가능성을 표현한다.
- Java 클래스 상속은 하나만 가능하므로 기능 조합은 인터페이스로 분리한다.

## 관련 페이지

- [[concepts/java-abstract-interface|Java 추상 클래스와 인터페이스]]
- [[concepts/java-interface-capability-design|Java 인터페이스 기능 설계]]
- [[concepts/java-inheritance|Java 상속]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
- `raw/KoreaICT/1. Java/숙제/클래스 숙제 완료.md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
