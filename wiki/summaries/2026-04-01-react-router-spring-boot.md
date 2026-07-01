---
title: 2026-04-01 React 라우팅과 Spring Boot 연동 흐름
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [react, typescript, spring-boot, frontend, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
status: growing
confidence: medium
---

# 2026-04-01 React 라우팅과 Spring Boot 연동 흐름

## 한 줄 요약

React의 페이지 구성과 라우팅을 App/MenuItems 구조로 정리하고 Spring Boot Controller 학습을 이어갔다.

## 배운 내용

- React 페이지 이동 구조
- App.tsx와 MenuItems
- TypeScript 컴포넌트 작성
- Spring Boot Controller 복습
- 프론트 라우팅과 백엔드 주소 구분

## 원본에서 확인한 세부 주제

- SpringBoot 교안 PDF (P.55)
- react의 웹페이지 만드는 과정 (MenuItems에 내용 추가하기)
- App.tsx의 코드 수정하기
- MenuItems.tsx의 코드 교체하기 (03.기본기 다지기.txt 247번째 줄 이용)
- VSC에 src폴더 안에 types폴더 생성 후 Fruit.ts파일 생성
- Fruit.ts 타입 스크립트 인터페이스 파일에 코드 작성
- VSC 추가 설정하기 (좌측 파일 탐색기 영역 조금 더 편하게 보기)
- 03.기본기 다지기.txt 파일 교체하기

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
