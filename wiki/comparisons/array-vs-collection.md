---
title: 배열 vs 컬렉션
created: 2026-07-02
updated: 2026-07-03
type: comparison
tags: [java]
sources:
  - raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md
  - raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md
status: stable
confidence: high
---

# 배열 vs 컬렉션

## 비교 목적

Java 수업에서는 먼저 배열을 배우고, 총정리에서 컬렉션으로 이어질 가능성을 남겼다. 두 자료구조는 여러 값을 담는다는 점은 같지만 크기와 기능에서 차이가 크다.

## 한눈에 보기

| 항목 | 배열 | 컬렉션 |
|---|---|---|
| 크기 | 생성 시 고정 | 보통 동적으로 변경 |
| 문법 예 | `int[] arr = new int[3]` | `List<String> list = new ArrayList<>()` |
| 인덱스 | 0부터 시작 | List는 인덱스, Set/Map은 구조별로 다름 |
| 수업 사용 | 점수, 이름, 객체 배열 | 이후 Java/Spring에서 목록 데이터 처리 |
| 장점 | 단순하고 빠른 기본 구조 | 추가/삭제/검색 등 편의 기능 풍부 |

## 언제 무엇을 쓰는가

- 요소 개수가 고정되어 있고 단순 반복 처리면 배열이 적합하다.
- 요소 개수가 변하거나 추가/삭제가 자주 일어나면 컬렉션이 더 자연스럽다.

## 헷갈리기 쉬운 포인트

- 배열은 `length` 속성을 쓰고, 컬렉션은 보통 `size()` 메서드를 쓴다.
- 배열은 기본 문법이고, 컬렉션은 Java 라이브러리의 자료구조다.
- 객체 배열은 배열이지만, 각 칸에는 객체 참조가 들어간다는 점에서 참조 자료형 이해가 필요하다.

## 관련 페이지

- [[concepts/java-array|Java 배열]]
- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-object-array-memory|Java 객체 배열과 메모리 관점]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/KoreaICT/1. Java/2026.03.12(목)/2026.03.12(목).md`
- `raw/KoreaICT/1. Java/Java 총정리/Java 총정리.md`
