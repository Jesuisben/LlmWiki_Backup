---
title: 2026-04-01 React 라우팅과 Spring Boot 연동 흐름
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
status: growing
confidence: high
---

# 2026-04-01 React 라우팅과 Spring Boot 연동 흐름

## 한 줄 요약

React Router, MenuItems, TypeScript interface, axios, CORS 설정을 통해 React 화면이 Spring Boot REST API를 호출하는 기본 연결을 만들었다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

프론트와 백엔드가 다른 포트에서 실행되면 브라우저 보안 정책인 CORS가 등장한다. React 라우팅과 API 요청 주소를 구분해야 실제 데이터 화면을 만들 수 있다.

## 핵심 개념

- `MenuItems.tsx`와 `AppRoutes.tsx`에 상품/과일 페이지 주소를 추가했다.
- `types/Fruit.ts`로 Spring Entity와 대응되는 TypeScript interface를 만들었다.
- `FruitOne.tsx`에서 axios 응답 스키마를 확인하며 API 호출 결과를 화면 state와 연결했다.
- Spring 쪽 CORS 설정으로 React 포트와 백엔드 포트의 교차 출처 요청을 허용했다.

## 실습 / 예제

React 페이지 파일 생성 → 메뉴 등록 → 라우팅 등록 → axios로 Spring API 호출 → CORS 허용이라는 한 사이클을 과일 예제로 실습했다.

## 헷갈린 점 / 질문

React Router의 `/product/list`는 브라우저 화면 주소이고, Spring API URL은 데이터를 요청하는 서버 주소다. 둘 다 URL처럼 보이지만 역할이 다르다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]], [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
