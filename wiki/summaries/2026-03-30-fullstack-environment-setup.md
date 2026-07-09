---
title: 2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
status: growing
confidence: high
---

# 2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환

## 한 줄 요약

Spring Boot·React·TypeScript·MySQL·Node.js·VS Code를 준비하고, “React 화면 → Spring API → DB”로 이어지는 풀스택 개발 흐름을 잡기 시작했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

이전 UI&UX 수업은 브라우저 화면 자체를 만드는 단계였다. 이 날부터는 화면이 백엔드 API와 DB를 만나야 실제 웹서비스가 된다는 흐름으로 넘어갔다.

## 핵심 개념

- Spring Boot, React IDE, Node.js, Visual Studio Code, MySQL, IntelliJ 등 사용 프로그램의 역할을 구분했다.
- MySQL 설치·설정과 Spring Boot 초기 구성을 통해 DB와 백엔드 연결 준비를 했다.
- Vite 기반 React 프로젝트 생성, `localhost` 접속, Spring 포트·파일 경로·URL 설정처럼 이후 매일 반복될 개발 루틴을 세웠다.
- 홈페이지 구성 절차를 “환경 준비 → 백엔드 설정 → 프론트 프로젝트 생성 → 실행 확인” 순서로 이해했다.

## 실습 / 예제

Spring Initializr/IntelliJ로 Spring Boot 프로젝트를 만들고, Node/Vite/VS Code로 React 프로젝트를 준비한 뒤 MySQL Workbench에서 샘플 DB를 확인하는 식의 초기 세팅 실습이 중심이었다.

## 헷갈린 점 / 질문

Node.js는 React 자체가 아니라 React 개발 도구와 빌드 도구가 돌아가는 실행 환경이다. Spring Boot는 API 서버, React는 브라우저 화면, MySQL은 데이터 저장소라는 역할 분리가 중요하다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]], [[entities/mysql|MySQL]], [[entities/node-js|Node.js]], [[entities/visual-studio-code|Visual Studio Code]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
