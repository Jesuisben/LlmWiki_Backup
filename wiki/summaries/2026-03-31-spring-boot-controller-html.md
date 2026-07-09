---
title: 2026-03-31 Spring Boot Controller와 HTML/REST 응답
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
status: growing
confidence: high
---

# 2026-03-31 Spring Boot Controller와 HTML/REST 응답

## 한 줄 요약

Fruit Entity를 기준으로 Spring MVC Controller, HTML 응답, REST API/JSON 응답의 차이를 실습하고 React 시작 구조로 넘어갔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

백엔드가 단순 문자열/HTML을 돌려주는 방식과 React가 소비할 JSON 데이터를 돌려주는 방식의 차이를 먼저 알아야 프론트·백엔드 분리가 이해된다.

## 핵심 개념

- `Fruit.java` Entity를 만들고 `FruitHtmlController`에서 HTML 형태 응답을 구성했다.
- templates 아래 HTML로 데이터를 보내는 흐름과 Java Collection/List를 화면에 전달하는 흐름을 확인했다.
- `FruitController`를 통해 REST API와 JSON 응답 개념을 접했다.
- VS Code에서 React `main.tsx`, `App.tsx` 구조를 확인하며 프론트 프로젝트 흐름을 시작했다.

## 실습 / 예제

요청 URL이 Controller 메서드로 들어오고, Entity/List 데이터가 HTML 또는 JSON 형태로 응답되는 흐름을 과일 예제로 따라갔다.

## 헷갈린 점 / 질문

`@Controller`는 주로 View/HTML 응답과 연결되고, `@RestController`는 JSON 데이터 응답과 연결된다. React와 붙일 때는 보통 REST API 형태가 중심이 된다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]], [[concepts/spring-boot-rest-api|Spring Boot REST API]], [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
