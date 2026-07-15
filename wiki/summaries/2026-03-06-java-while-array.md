---
title: 2026-03-06 Java 무한 while과 배열
created: 2026-07-02
updated: 2026-07-15
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

- 정답 맞히기: `Scanner`로 입력 → `answer == input`이면 `break` → 작거나 크면 힌트를 출력하고 다시 입력받는 흐름으로 실행했다. 원본 출력에서는 `50 → 30 → 45 → 40` 순으로 입력해 마지막에 `정답입니다.`로 종료했다.
- 점수 누적: 음수가 들어오기 전까지 `counter++`, `total += jumsu`를 수행한 뒤 `(double) total / counter`로 평균을 계산했다. 정수끼리 먼저 나누지 않도록 형변환 위치가 중요하다.
- 배열: `int[] arr = new int[3]`에 `4`, `11`, `7`을 계산해 넣고 `arr.length`를 조건으로 반복 출력했다. 값과 개수를 이미 알 때는 `int[] brr = {15, 30, 22}` 초기화 기법을 사용했다.
- 입력 배열: 크기를 입력받아 `new int[size]`를 만들고, 각 인덱스에 정수를 저장하면서 조건문으로 `odd`·`even` 합계를 나눈 뒤 반복 종료 후 출력했다.

```text
Scanner → 배열 크기 입력 → new int[size]
→ for로 인덱스별 입력 → 홀짝 판정·누적 → 결과 출력
```

## 헷갈린 점 / 질문

- `while(true)` 자체는 끝나지 않으므로 종료 조건에서 반드시 `break` 또는 조건 변경이 필요하다.
- 배열의 “방 번호”는 1번이 아니라 0번부터 시작한다.
- `new int[3]`은 방을 3개 만드는 것이고, 실제 값 대입은 별도로 할 수 있다.
- 학생 점수 문제의 요구사항은 국어·영어·수학 점수를 정수형 배열에 저장하는 것이었지만, 원본에 남은 구현은 `String[] subject`와 지역 변수 `input`으로 즉시 누적했다. 요구와 기록된 구현이 일치한다고 단정하지 않는다.
- 음수까지 홀수로 판정하려면 `value % 2 == 1`보다 `value % 2 != 0`이 안전하다.

## 관련 페이지

- [[concepts/java-loop|Java 반복문]]
- [[concepts/java-array|Java 배열]]
- [[comparisons/array-vs-collection|배열 vs 컬렉션]]

## 출처

- `raw/KoreaICT/1. Java/2026.03.06(금)/2026.03.06(금).md`
- `raw/KoreaICT/1. Java/교육 자료/Java 교안(이론_20260226).pdf`
