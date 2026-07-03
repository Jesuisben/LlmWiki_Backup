---
title: DBeaver
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [oracle, sql]
sources:
  - raw/Study/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md
  - raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md
  - raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md
  - raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf
  - raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf
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

## 관련 개념

- [[entities/oracle-database|Oracle Database]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]
- [[concepts/oracle-ddl-dml-transaction|Oracle DDL, DML, 트랜잭션]]
- [[concepts/database-modeling-normalization|데이터 모델링과 정규화]]

## 출처

- `raw/Study/2. Oracle/2026.03.13(금) - 시작/2026.03.13(금) - 시작.md`
- `raw/Study/2. Oracle/2026.03.16(월)/2026.03.16(월).md`
- `raw/Study/2. Oracle/2026.03.17(화)/2026.03.17(화).md`
- `raw/Study/2. Oracle/2026.03.20(금)/2026.03.20(금).md`
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법.pdf`
- `raw/Study/2. Oracle/교육 자료/디비버(Dbeaver) 사용법(version 2.0).pdf`
