---
title: FrontEnd_BackEnd 총정리
type: summary
created: 2026-07-03
updated: 2026-07-03
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# FrontEnd_BackEnd 총정리

## 한 줄 요약

`FrontEnd_BackEnd 총정리`는 2026-03-30부터 2026-04-03까지의 초기 풀스택 세팅과 Spring Boot ↔ React 연결 흐름을 “환경 준비 → 백엔드 API → 프론트엔드 프로젝트 → axios/useEffect/CORS 연결” 순서로 복습하는 문서다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-03-27-jquery-ui-interaction|UI&UX/jQuery 상호작용]]까지는 정적 HTML/CSS/JS 중심이었다.
- 중심 기간: [[summaries/2026-03-30-fullstack-environment-setup|2026-03-30]] ~ [[summaries/2026-04-03-spring-member-seed-react-comments|2026-04-03]] 초기 풀스택 전환 구간
- 다음 흐름: [[summaries/2026-04-06-login-jwt-session-cookie|로그인/JWT]], 상품·장바구니·주문 기능 구현으로 확장
- 주의: 파일명은 과목 총정리지만 첫 줄 기준 기간은 2026-03-30~2026-04-03이며, 이후 장바구니/주문/페이징 전체를 모두 덮는 문서는 아니다.

## 배운 내용

### 1. 웹페이지를 만들기 위한 전체 절차

총정리는 풀스택 웹페이지 제작을 프로그램 설치, Spring `application.properties` 설정, Entity 생성, Repository/Controller/Service 구성, React 페이지와 라우터 구성, `useState`/`useEffect`, axios, CORS 설정, 연결 성공의 순서로 정리한다. 이 목록은 [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]의 초기 버전이다.

### 2. 개발 환경과 도구

MySQL, Node.js, Visual Studio Code, Spring Boot, Vite 기반 React 프로젝트, IntelliJ 설정이 한꺼번에 등장한다. 이 시기에는 “하나의 언어만 쓰는 단계”에서 벗어나 백엔드 서버, 프론트엔드 개발 서버, DB, 이미지 경로, API 주소가 동시에 움직이기 시작한다.

### 3. Spring Boot 초기 백엔드

Spring 쪽에서는 `application.properties`, Lombok, Entity, Controller, HTML 응답, JSON 응답, REST API 개념이 정리된다. `@Controller + Model`로 HTML에 데이터를 넘기는 방식과 JSON API로 React에 데이터를 넘기는 방식의 차이가 초기 혼동 포인트다.

### 4. React 초기 프론트엔드

React 쪽에서는 Vite 프로젝트 생성, `App.tsx`, `MenuItems.tsx`, 페이지 구성, Router, `useState`, `useEffect`, axios 응답 스키마가 등장한다. UI&UX에서 배운 HTML/CSS/JS 지식을 컴포넌트와 상태(state) 중심으로 재구성하는 단계다.

### 5. Spring ↔ React 연결: axios와 CORS

React가 Spring API를 호출하려면 axios로 요청을 보내고, Spring은 JSON을 응답하며, 서로 다른 포트의 개발 서버를 허용하기 위해 CORS 설정이 필요하다. 총정리의 `WebConfig`, `allowedOrigins`, resource handler, 이미지 경로 설명은 이후 상품 이미지/파일 업로드 흐름의 바탕이다.

## 헷갈린 점 / 질문

- React Router 주소는 “프론트 화면 이동 주소”이고, Spring API 주소는 “데이터 요청 주소”다. 차이는 [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]] 참고.
- `@Controller + Model + HTML`은 서버가 화면을 만들어주는 방식에 가깝고, `@RestController + JSON + React`는 프론트가 데이터를 받아 화면을 구성하는 방식에 가깝다.
- `useEffect`는 화면이 렌더링되는 시점과 API 호출 시점을 연결하는 Hook이므로, 단순 함수 호출처럼 아무 곳에서나 반복 호출하면 안 된다.
- CORS 오류는 “코드가 완전히 틀렸다”기보다 브라우저 보안 정책상 서로 다른 출처의 요청을 서버가 허용하지 않았다는 신호일 수 있다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/react|React]]
- [[entities/typescript|TypeScript]]
- [[entities/node-js|Node.js]]
- [[entities/mysql|MySQL]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
