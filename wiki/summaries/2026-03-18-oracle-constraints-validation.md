---
title: 2026-03-18 Oracle 제약조건 테스트와 유효성 검사
created: 2026-06-30
updated: 2026-07-01
type: summary
tags: [oracle, sql]
sources: ["raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md"]
status: growing
confidence: medium
---

# 2026-03-18 Oracle 제약조건 테스트와 유효성 검사

## 한 줄 요약

Oracle 사용자 재설정, 제약조건 테스트, 폼 유효성 검사 개념을 연결한 날이다.

## 배운 내용

- 실습 환경을 다시 세팅하고 스크립트로 사용자를 만들었다.
- 제약조건이 데이터 입력 오류를 어떻게 막는지 테스트했다.
- 폼 유효성 검사(validation check)는 프론트엔드/백엔드 입력 검증과 DB 제약조건으로 이어지는 개념이다.
- 데이터 품질을 지키는 규칙이 화면, 서버, DB 여러 층에 있을 수 있음을 확인했다.

## 핵심 개념

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]

## 실습 / 예제

- 원본 수업 노트의 시간대별 실습 흐름을 기준으로 정리했다.
- 자세한 코드와 실행 결과는 원본 `raw` 파일을 출처로 다시 확인한다.

## 헷갈린 점 / 질문

- 원본에 `추가 공부`, `중요`, `????????`로 표시된 부분은 추후 개념 페이지에서 더 보강할 후보로 남긴다.

## 관련 페이지

- [[concepts/oracle-constraints-sequence|Oracle 제약조건과 시퀀스]]
- [[concepts/oracle-sql-basics|Oracle SQL 기본]]


## 원본 수정 반영 (2026-07-01)

- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`에서 확인한 추가/정리 주제: 오라맨사용자 삭제 후 선생님이 보내주신 A03스크립트로 다시 오라맨 만들고 세팅하기
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`에서 확인한 추가/정리 주제: 제약 조건 테스트
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`에서 확인한 추가/정리 주제: 폼 유효성 검사 (Validation Check)
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`에서 확인한 추가/정리 주제: 오류코드 설명
- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`에서 확인한 추가/정리 주제: 우리가 하는 작업은 데이터 모델링

> 이 항목은 기존에 한 번 ingest된 원본이 이후 수정된 상태였음을 반영하기 위한 보강 메모다. 세부 개념은 관련 개념 페이지에서 계속 보강한다.

## 출처

- `raw/Study/2. Oracle/2026.03.18(수)/2026.03.18(수).md`
