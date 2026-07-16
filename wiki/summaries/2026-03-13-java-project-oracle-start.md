---
title: 2026-03-13 Java 팀 프로젝트와 Oracle 시작
created: 2026-07-02
updated: 2026-07-15
type: summary
tags: [java, oracle, curriculum, study-log]
sources:
  - raw/KoreaICT/1. Java/2026.03.13(금)/2026.03.13(금).md
  - raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md
status: stable
confidence: high
---

# 2026-03-13 Java 팀 프로젝트와 Oracle 시작

## 한 줄 요약

Java 1~5교시 팀 프로젝트로 객체지향 문법을 복습하고, 마지막 교시에 DBeaver 설치를 시작하며 Oracle/SQL 과정으로 전환했다.

## 커리큘럼 위치

- Java 문법 단원의 마무리이자 Oracle 수업으로 넘어가는 연결일이다.
- Java에서 배운 클래스/객체/메서드 사고는 이후 [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]와 Spring Boot 계층 학습의 바탕이 된다.

## 배운 내용

- 팀 프로젝트를 통해 Java 문법을 기능 단위로 묶어보는 시간을 가졌다.
- 기억해야 할 사항을 정리하며 Java 객체지향 문법을 마무리했다.
- DBeaver Community 다운로드로 Oracle DB 실습 환경을 준비했다.

## 왜 이 순서로 배웠나

Java에서는 프로그램이 실행되는 동안 객체와 로직을 다뤘다. 이 날은 그 학습을 팀 프로젝트와 코드 리뷰로 닫은 뒤, 다음 주부터 **프로그램이 사용할 데이터를 영구 저장하는 영역**으로 이동하기 위해 Oracle과 DBeaver를 준비한 전환일이다. 다만 03-13 원본에는 Java 객체와 Oracle 테이블을 직접 매핑한 실습은 없다. 그 연결은 뒤의 Spring/JPA 과정에서 확장된 관점이며, 이 날 직접 확인한 것은 설치와 도구 전환까지다.

## 핵심 실습 / 예제

- Java 팀 프로젝트를 1~5교시에 진행하고 6교시에 코드 리뷰했다.
- **원본에는 프로젝트 주제·코드·실행 결과가 남아 있지 않다.** 따라서 어떤 기능을 구현했는지 추정하지 않고 “팀 프로젝트와 코드 리뷰를 수행했다”는 경계까지만 보존한다.
- 7~8교시에는 Oracle 설치를 시작하고 DBeaver Community를 준비했다. DBeaver를 Java의 IntelliJ처럼 SQL 작성·실행을 돕는 개발 환경으로 연결해 이해했다.

## 헷갈린 점 / 질문

- Java에서 IntelliJ가 코드 작성·실행을 돕는 IDE라면, Oracle 단계에서 DBeaver는 SQL 작성·실행·DB 확인을 돕는 데이터베이스 IDE다.
- Java 과정이 끝난 뒤에도 Java 지식은 사라지는 것이 아니라 Spring Boot 백엔드에서 계속 사용된다.

## 관련 페이지

- [[entities/java|Java]]
- [[entities/dbeaver|DBeaver]]
- [[entities/oracle-database|Oracle Database]]
- [[summaries/2026-03-16-oracle-dbms-sql-dbeaver|2026-03-16 Oracle DBMS, SQL, DBeaver 입문]]

## 이전·다음 흐름

- 이전: [[summaries/2026-03-13-java-subject-review|Java 총정리]]에서 문법과 객체지향을 마무리했다.
- 다음: 03-16에는 DBeaver를 실제 Oracle DBMS에 연결하고 SQL 분류와 `MEMBERS` 테이블을 시작한다.

## 출처

- `raw/KoreaICT/1. Java/2026.03.13(금)/2026.03.13(금).md`
- `raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
