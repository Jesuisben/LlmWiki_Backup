---
title: 2026-04-03 Member 데이터 준비와 React JSX 기초
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/My-Sql 설치&설정.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---
# 2026-04-03 Member 데이터 준비와 React JSX 기초

## 한 줄 요약

회원 데이터와 React JSX 기초를 다루면서 REST, HTTP 상태 코드, 이벤트, 쿼리 메서드 같은 API 개발 기본 용어를 연결했다.

## 커리큘럼 위치와 흐름

상품/회원 기능을 본격 구현하기 전, 회원 테이블 데이터 준비와 React 편집 방식, API 용어를 정리한 날이다. MySQL safe update, REST API, HTTP 상태 코드, React event, Spring Data JPA query method가 이후 로그인/회원 API 구현의 기반이 된다.

## 배운 내용

- MySQL Workbench 안전 모드 해제와 `SQL_SAFE_UPDATES` 개념을 확인했다.
- IT 관련 용어 p.35~36에서 REST는 URL로 Resource를 표현하고 HTTP Method로 CRUD를 수행하는 방식임을 확인했다.
- HTTP 상태 코드 p.54는 100/200/300/400/500대 응답 의미를 구분한다.
- React 교안 p.72~73은 이벤트 이름 camelCase, event object의 `target`, `preventDefault`, `stopPropagation`을 설명한다.
- SpringBoot 교안 p.89~90은 Spring Data JPA 쿼리 메서드 규칙을 소개한다.

## 핵심 실습 / 예제

- Member 테이블 seed 데이터를 준비하고, 삭제/수정 시 MySQL safe update 오류를 만날 수 있음을 확인했다.
- React JSX 주석과 편집 단축키를 익히고, 이벤트 핸들러 작성으로 이어질 준비를 했다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- REST는 “그냥 JSON”이 아니라 Resource URL + HTTP Method 중심의 설계 방식이다.
- 400/500 상태 코드는 프론트 오류인지 서버 오류인지 디버깅 방향을 나누는 실마리다.
- Spring Data JPA query method는 메서드 이름을 쿼리 조건으로 해석하므로 이름 규칙이 중요하다.

## 관련 페이지

- [[concepts/spring-boot-rest-api]]
- [[concepts/react-form-state-event]]
- [[concepts/spring-data-jpa-repository]]
- [[entities/mysql]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/My-Sql 설치&설정.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
