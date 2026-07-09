---
title: 2026-04-03 Member 데이터 준비와 React JSX 기초
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
status: growing
confidence: high
---

# 2026-04-03 Member 데이터 준비와 React JSX 기초

## 한 줄 요약

Member 테스트 데이터와 회원가입 화면을 준비하면서 JSX 주석, 이벤트, HTTP status code, Repository query method를 함께 학습했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

로그인/회원가입은 인증 흐름의 출발점이므로, DB에 저장될 Member 구조와 React 입력 화면, Spring Repository 조회 흐름을 먼저 잡아야 한다.

## 핵심 개념

- MemberTest에서 회원 데이터를 seed하고 passwordEncoder, role, regdate 같은 회원 속성을 확인했다.
- React JSX 주석, 한 줄 복사 단축키, XML 문법 제약을 복습했다.
- SignupPage.tsx, AppRoutes.tsx, Member.java를 연결해 회원가입 입력 항목을 맞췄다.
- HTTP status code와 Spring Data JPA query method를 회원 기능 구현 맥락에서 확인했다.

## 실습 / 예제

React 회원가입 페이지에서 입력 이벤트를 다루고, Spring MemberRepository를 통해 이메일/회원 정보 조회 흐름을 준비했다.

## 헷갈린 점 / 질문

JSX는 HTML처럼 보이지만 XML 규칙을 따르는 JavaScript 문법이다. 태그 닫기, 주석 형태, `className` 같은 차이를 계속 주의해야 한다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]], [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]], [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
