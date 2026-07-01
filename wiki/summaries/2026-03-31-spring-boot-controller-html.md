---
title: 2026-03-31 Spring Boot Controller와 HTML 응답
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [spring-boot, backend, frontend, html]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
status: growing
confidence: medium
---

# 2026-03-31 Spring Boot Controller와 HTML 응답

## 한 줄 요약

Spring Boot에서 Entity와 Controller를 만들고, 브라우저 요청에 HTML 문자열 또는 데이터를 응답하는 기본 흐름을 배웠다.

## 배운 내용

- Fruit 엔티티 작성
- Controller 메서드와 요청 매핑
- HTML 문자열 응답
- React/Bootstrap과의 연결 준비
- 서버가 화면에 데이터를 보내는 방식

## 원본에서 확인한 세부 주제

- 그림 (SpringBoot 교안 PDF (P.56))
- 03.기본기 다지기 텍스트 파일 121번 줄
- FruitHtmlController.java 생성 후 작성
- FruitHtmlController.java 생성 후 작성하고 내용 추가
- resources - templates에 HTML만들기
- 컬렉션에 대해서 공부하기 (Java 교안(이론_20260226) (P.153))
- 여러개 HTML로 보내기
- 데이터를 보낼 fruitList라는 HTML만들기

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

- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
