---
title: DBeaver
created: 2026-07-02
updated: 2026-07-15
type: entity
tags: [oracle, sql]
sources:
  - raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md
  - raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf
status: growing
confidence: high
---

# DBeaver

## 무엇인가

DBeaver는 Oracle/MySQL 같은 DBMS에 접속해 SQL을 실행하고, 테이블·스키마·시퀀스·ERD를 확인하는 데이터베이스 IDE다.

## 이 위키에서의 맥락

2026-03-13에 Oracle 학습용 도구로 설치했고, 2026-03-16부터 관리자 접속과 `oraman` 일반 사용자 접속을 만들어 SQL 실습을 진행했다. Java 수업의 IntelliJ처럼 SQL을 쓰는 화면이지만, DBeaver 자체가 DBMS는 아니다.

## 수업에서 사용한 기능

- 새 데이터베이스 연결: Host `localhost`, Database `xe`, Username `sys` 또는 `oraman`
- Role: 관리자 접속은 `SYSDBA`, 일반 사용자는 `Normal`
- SQL 실행: `Ctrl + Enter`, 전체 실행 `Alt + X`
- 객체 생성: `Alt + Insert`
- View/Table/Column 보기: `F4`
- 새로고침: `F5`
- DDL 생성: 스키마/테이블 우클릭 후 SQL 생성
- ERD 확인: 스키마의 엔티티 관계도
- Auto Commit 설정: 트랜잭션 실습 전 Manual Commit 필요

## 날짜별 학습 이력

- 03-13: Community 버전을 설치하며 Java/IntelliJ에서 Oracle/SQL 환경으로 전환했다.
- 03-16: `SYSDBA` 관리자 연결과 `oraman` 일반 연결을 분리하고 SQL Editor·테이블 UI·SQL Preview를 사용했다.
- 03-17: schema DDL을 생성해 객체를 삭제·복구하고, Auto Commit 때문에 `ROLLBACK` 결과가 달라질 수 있음을 확인했다.
- 03-18: DDL 스크립트와 DQL을 반복 실행하며 오류 코드와 결과 grid를 확인했다.
- 03-20: ERD로 FK 관계를 보고 View와 다른 schema의 조회 권한을 실습했다.

## 구현 역할과 면접 관점

DBeaver는 DB를 대신하는 서버가 아니라 Oracle에 접속하는 클라이언트다. 연결 오류라면 host/database/user/role을 확인하고, SQL 오류라면 Oracle이 반환한 ORA 코드와 제약조건 이름을 확인한다. 면접이나 프로젝트 설명에서는 “DBeaver를 사용했다”보다 **관리자/일반 연결 분리, SQL Preview로 DDL 확인, Manual Commit으로 트랜잭션 검증, ERD로 관계 확인**을 실제 사용 맥락으로 말할 수 있다.

## 자주 헷갈리는 점

- UI로 테이블을 만들더라도 Oracle에는 DDL이 실행된다. DBeaver UI와 SQL은 서로 다른 데이터 구조가 아니다.
- DBeaver를 종료해도 Oracle DBMS의 테이블이 사라지는 것은 아니다.
- Auto Commit은 편집기 편의 설정이지만, 켜진 상태에서는 트랜잭션 학습의 `ROLLBACK` 결과를 오해할 수 있다.

## 관련 개념

- [[entities/oracle-database|Oracle Database]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]

## 출처

- `raw/KoreaICT/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
- `raw/KoreaICT/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/KoreaICT/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/KoreaICT/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
- `raw/KoreaICT/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf`
