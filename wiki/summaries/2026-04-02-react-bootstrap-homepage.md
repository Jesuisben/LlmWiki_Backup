---
title: 2026-04-02 React Bootstrap과 HomePage 구성
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
status: growing
confidence: high
---

# 2026-04-02 React Bootstrap과 HomePage 구성

## 한 줄 요약

Spring Boot 정적 이미지 응답을 확인하고 React Bootstrap Carousel/Card로 HomePage를 구성한 뒤, Member/JPA/MySQL 설정으로 회원 기능의 DB 기반을 준비했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

초기 화면을 예쁘게 구성하는 일과 DB 기반 회원 기능 준비가 함께 진행되면서 “화면 구성”과 “데이터 저장”이 동시에 필요한 풀스택 감각을 익히는 단계다.

## 핵심 개념

- `localhost:9000/images/...`로 Spring Boot 정적 리소스가 잘 제공되는지 확인했다.
- React Bootstrap Carousel/Card를 사용해 HomePage를 만들고 `className`, JSX `{}` 사용법을 복습했다.
- 템플릿용 TSX 파일을 만들어 반복되는 기본 구조를 빠르게 가져올 수 있게 했다.
- JPA 설정과 Member 테이블/Entity 준비로 회원 기능 구현의 DB 기반을 잡았다.

## 실습 / 예제

HomePage.tsx에서 Carousel 이미지 경로를 API base URL과 조합하고, AppRoutes에 홈 화면 라우팅을 추가했다.

## 헷갈린 점 / 질문

JSX에서는 HTML의 `class` 대신 `className`을 쓴다. 문자열 경로와 JavaScript 표현식을 섞을 때는 `{}`와 template literal의 역할을 구분해야 한다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]], [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[comparisons/props-vs-state|props vs state]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
