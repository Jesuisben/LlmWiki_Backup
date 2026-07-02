---
title: 2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/IntelliJ 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/My-Sql 설치&설정.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/NodeJs.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/VisualStudioCode.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---
# 2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환

## 한 줄 요약

FrontEnd_BackEnd 과정 첫날로, Spring Boot와 React/TypeScript를 함께 쓰는 풀스택 실습 환경을 준비했다.

## 커리큘럼 위치와 흐름

HTML/CSS/JavaScript 기초에서 한 단계 올라가, 브라우저 화면만 만드는 것이 아니라 Spring Boot API 서버와 React 화면을 분리해 개발하는 단계로 전환했다. MySQL, Node.js, VS Code, IntelliJ, Spring Initializr가 이후 모든 실습의 기반이 된다.

## 배운 내용

- MySQL과 Workbench 설치·설정 흐름을 확인했다.
- Node.js와 npm이 React/Vite 개발 서버를 실행하는 기반이라는 점을 배웠다.
- VS Code는 React/TypeScript 코드를 작성하는 프론트엔드 편집기로, IntelliJ는 Spring Boot 백엔드 프로젝트를 다루는 IDE로 사용했다.
- Spring Initializr에서 Maven, Lombok, Spring Web, Spring Data JPA 등 초기 의존성을 고르는 흐름을 확인했다.

## 핵심 실습 / 예제

- `D:\FrontEnd&BackEnd\spring_cafe` 같은 실습 폴더를 만들고 Spring Boot 프로젝트 초기 구조를 준비했다.
- SpringBoot 교안 p.11~12의 Initializr 설명처럼 `pom.xml`, `application.properties`, `Entity`, `Repository`, `Controller` 등이 이후 프로젝트 구성 요소가 된다.
- NodeJs 교안은 Node.js를 V8 기반 런타임, npm을 Node 패키지 관리자이자 React 개발 도구 설치 기반으로 설명한다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- Node.js는 React 자체가 아니라 React 개발 서버와 패키지 관리를 실행하는 런타임이다.
- IntelliJ와 VS Code는 경쟁 도구라기보다 각각 백엔드/프론트엔드 실습에 맞게 나눠 썼다.
- Spring Initializr에서 고른 의존성은 이후 코드에서 `@RestController`, JPA Repository, Lombok 같은 기능으로 드러난다.

## 관련 페이지

- [[concepts/frontend-backend-architecture]]
- [[entities/intellij-idea]]
- [[entities/node-js]]
- [[entities/visual-studio-code]]
- [[entities/spring-boot]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/IntelliJ 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/My-Sql 설치&설정.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/NodeJs.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/VisualStudioCode.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
