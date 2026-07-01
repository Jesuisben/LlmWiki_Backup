---
title: 2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리
created: 2026-06-30
updated: 2026-07-01
type: summary
tags: [oracle, sql]
sources: ["raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md"]
status: growing
confidence: medium
---

# 2026-03-19 Oracle 함수, GROUP BY, JOIN, 서브쿼리

## 한 줄 요약

Oracle의 단일행 함수, 그룹 함수, 조인, 서브쿼리를 폭넓게 다룬 날이다.

## 배운 내용

- `dual` 테이블은 간단한 계산이나 함수 검증에 쓰는 1행 1열 테스트용 테이블로 소개되었다.
- 문자열, 숫자, 날짜 함수와 함수 중첩을 실습했다.
- `GROUP BY`와 `HAVING`으로 집계 결과를 그룹 단위로 필터링했다.
- JOIN과 서브쿼리로 여러 테이블 또는 쿼리 결과를 연결하는 방법을 배웠다.

## 핵심 개념

- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]

## 실습 / 예제

- 원본 수업 노트의 시간대별 실습 흐름을 기준으로 정리했다.
- 자세한 코드와 실행 결과는 원본 `raw` 파일을 출처로 다시 확인한다.

## 헷갈린 점 / 질문

- 원본에 `추가 공부`, `중요`, `????????`로 표시된 부분은 추후 개념 페이지에서 더 보강할 후보로 남긴다.

## 관련 페이지

- [[concepts/oracle-functions-join-subquery|Oracle 함수·조인·서브쿼리]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]


## 원본 수정 반영 (2026-07-01)

- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`에서 확인한 추가/정리 주제: 함수 (Java에서의 메소드)
- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`에서 확인한 추가/정리 주제: dual 테이블 (Oracle 교안 P.217) (A06스크립트)
- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`에서 확인한 추가/정리 주제: 자바의 String 클래스가 갖고 있는 메소드 공부하기!!
- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`에서 확인한 추가/정리 주제: length() 함수
- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`에서 확인한 추가/정리 주제: substr() 함수 (Oracle 교안 P.225)

> 이 항목은 기존에 한 번 ingest된 원본이 이후 수정된 상태였음을 반영하기 위한 보강 메모다. 세부 개념은 관련 개념 페이지에서 계속 보강한다.

## 출처

- `raw/Study/2. Oracle/2026.03.19(목)/2026.03.19(목).md`
