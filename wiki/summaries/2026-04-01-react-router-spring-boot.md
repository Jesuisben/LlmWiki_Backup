---
title: 2026-04-01 React 라우팅과 Spring Boot 연동 흐름
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png
status: growing
confidence: high
---
# 2026-04-01 React 라우팅과 Spring Boot 연동 흐름

## 한 줄 요약

React에서 페이지 구조와 라우팅을 만들고, Spring Boot API와 프론트 화면 주소를 분리해서 생각하기 시작했다.

## 커리큘럼 위치와 흐름

Spring Boot Controller의 URL 매핑을 배운 뒤, React 쪽에서는 `App.tsx`, `MenuItems.tsx`, 타입 파일을 통해 화면 내부 경로와 컴포넌트 구성을 다뤘다. 이때부터 “브라우저 주소가 React 화면을 바꾸는 경우”와 “Spring API에 데이터를 요청하는 경우”를 구분해야 한다.

## 배운 내용

- React 프로젝트에서 `App.tsx`, `MenuItems.tsx`, `types/Fruit.ts`를 수정해 화면 메뉴와 타입 구조를 잡았다.
- React Router는 관객을 알맞은 극장으로 안내하는 라우터 이미지처럼, URL에 맞는 컴포넌트를 선택한다.
- Spring Boot 교안 p.55의 프로젝트 구성도와 연결해 프론트 화면과 백엔드 API가 서로 다른 역할을 갖는다는 점을 확인했다.

## 핵심 실습 / 예제

- `Fruit` 인터페이스를 만들어 API 데이터의 모양을 TypeScript로 표현했다.
- React Router 경로는 화면 컴포넌트를 보여주고, Spring API URL은 서버 데이터 요청에 쓰인다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- `/products`가 React Router 경로인지, Spring Controller API 경로인지 혼동하기 쉽다.
- TypeScript 인터페이스는 실제 DB 테이블이 아니라 프론트 코드가 기대하는 데이터 형태를 설명한다.
- 라우터는 요청을 “처리”한다기보다 적절한 화면 컴포넌트로 “안내”한다.

## 관련 페이지

- [[comparisons/react-router-vs-spring-api-url]]
- [[concepts/react-typescript-basics]]
- [[concepts/frontend-backend-architecture]]
- [[entities/react]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png`
