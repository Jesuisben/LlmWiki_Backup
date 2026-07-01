---
title: 2026-04-02 React Bootstrap과 HomePage 구성
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [react, typescript, bootstrap, frontend, spring-boot]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
status: growing
confidence: medium
---

# 2026-04-02 React Bootstrap과 HomePage 구성

## 한 줄 요약

React Bootstrap의 Carousel·Card 등 UI 컴포넌트를 이용해 홈 화면을 구성하고 Spring/React 프로젝트 구조를 보강했다.

## 배운 내용

- template.tsx와 HomePage.tsx
- React Bootstrap Carousel
- 컴포넌트 import 문제 해결
- JDBC/DB 연결 언급
- 화면 구성 재사용

## 원본에서 확인한 세부 주제

- 특정 주소 입력시 사진 나오는 것을 확인
- 이름 바꾸는 단축키
- 빨간줄이 뜰때 해결법
- VSC에 pages폴더 안에 template.tsx파일 생성
- VSC에 pages폴더 안에 HomePage.tsx파일 생성
- React Bootstrap에서 Carousels 클릭
- JSX에는 class 선택자를 사용못함
- JSX에 그 안에 JS문법을 적으려면 {}를 쓰고 그 안에 써야 함

## 핵심 개념

- 백엔드의 Controller/Service/Repository/DTO/Entity 역할을 나누어 생각한다.
- 프론트엔드는 React 컴포넌트, props, state, Hook, 라우팅으로 화면과 상태를 관리한다.
- 실습 기능은 단독 문법보다 로그인, 상품, 장바구니, 주문처럼 이어지는 업무 흐름 안에서 이해해야 한다.

## 헷갈린 점 / 질문

- 같은 데이터가 백엔드 Entity, DTO, 프론트 TypeScript 타입에서 각각 어떻게 표현되는지 구분할 필요가 있다.
- React 라우팅 주소와 Spring Boot API 주소는 역할이 다르므로 혼동하지 않아야 한다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
