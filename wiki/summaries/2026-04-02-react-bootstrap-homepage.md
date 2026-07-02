---
title: 2026-04-02 React Bootstrap과 HomePage 구성
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/VisualStudioCode.pdf
status: growing
confidence: high
---
# 2026-04-02 React Bootstrap과 HomePage 구성

## 한 줄 요약

React Bootstrap의 Carousel/Card 같은 컴포넌트로 홈 화면을 구성하고, API 이미지 경로를 화면에 연결했다.

## 커리큘럼 위치와 흐름

라우팅과 타입 파일을 만든 뒤 실제 홈 화면 UI를 꾸미는 단계다. 기존 HTML/CSS/Bootstrap 지식이 React 컴포넌트 구조 안으로 들어오며, `className`, 컴포넌트 import, 이미지 URL 연결을 함께 배웠다.

## 배운 내용

- React Bootstrap 컴포넌트를 참고해 `HomePage.tsx`, template 페이지 등을 구성했다.
- `API_BASE_URL`을 이용해 Spring 서버의 이미지 경로를 React 화면에 연결했다.
- JSX에서는 HTML의 `class` 대신 `className`을 쓴다는 차이를 확인했다.

## 핵심 실습 / 예제

- `src={`${API_BASE_URL}/images/...`}` 형태로 서버 정적 이미지 URL을 화면에 연결했다.
- Bootstrap Carousel/Card는 직접 CSS를 많이 쓰지 않아도 반응형 UI를 빠르게 만들 수 있게 해준다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- JSX는 HTML처럼 보이지만 JavaScript/TypeScript 안에서 해석되는 문법이라 속성명이 다를 수 있다.
- 이미지 파일은 React 프로젝트 내부 asset일 수도 있고, Spring 서버가 제공하는 정적 리소스 URL일 수도 있다.
- Bootstrap 컴포넌트는 UI 구조를 도와주지만 데이터 흐름 자체를 해결해주지는 않는다.

## 관련 페이지

- [[concepts/react-typescript-basics]]
- [[entities/bootstrap]]
- [[entities/react]]
- [[concepts/frontend-backend-architecture]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/React 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/VisualStudioCode.pdf`
