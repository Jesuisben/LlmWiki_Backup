---
title: 2026-03-06 Java 무한 while과 배열
created: 2026-07-02
updated: 2026-07-03
type: summary
tags: [java, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md
  - raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf
status: stable
confidence: high
---

# 2026-03-06 Java 무한 while과 배열

## 한 줄 요약

`Scanner` 입력, `while(true)`와 `break`, 배열 생성·초기화·`length`를 배우며 여러 값을 한 번에 다루기 시작했다.

## 커리큘럼 위치

- 반복문을 단순 카운트에서 사용자 입력 기반 반복으로 확장했다.
- 이후 [[summaries/2026-03-09-java-class-object|클래스와 객체]]에서 배열 요소가 기본값뿐 아니라 객체 참조가 될 수 있다는 흐름으로 이어진다.

## 배운 내용

- `Scanner scan = new Scanner(System.in);`
- `scan.nextInt()`로 정수 입력 받기
- `while(true)` 무한 반복과 `break` 종료
- 배열의 3요소: 이름, 타입, 요소 개수
- `new` 연산자 기법: `int[] arr = new int[3];`
- 초기화 기법: 값이 명확할 때 한 번에 배열 구성
- `배열이름.length`로 요소 개수 확인

## 핵심 실습 / 예제

- 1~100 사이 정답 맞히기 입력 반복
- 음수 입력 시 종료하고 총점/평균 계산
- `int[]`, `String[]` 배열 만들기
- 배열 인덱스는 0부터 시작한다는 점 확인

## 헷갈린 점 / 질문

- `while(true)` 자체는 끝나지 않으므로 종료 조건에서 반드시 `break` 또는 조건 변경이 필요하다.
- 배열의 “방 번호”는 1번이 아니라 0번부터 시작한다.
- `new int[3]`은 방을 3개 만드는 것이고, 실제 값 대입은 별도로 할 수 있다.

## 관련 페이지

- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-array|Java 배열]]
- [[comparisons/array-vs-collection|배열 vs 컬렉션]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
