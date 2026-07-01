---
title: 2026-04-08 상품 도메인과 OCI 소개
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [spring-boot, react, backend, frontend, aws]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
status: growing
confidence: medium
---

# 2026-04-08 상품 도메인과 OCI 소개

## 한 줄 요약

상품 기능 구현을 시작하며 Category, Product 도메인과 Spring/React 상품 구조, OCI 개념을 배웠다.

## 배운 내용

- OCI 개념
- 상품 공통 사항
- Category 열거형
- Product 엔티티
- Spring/React 상품 기능 분리

## 원본에서 확인한 세부 주제

- 오픈 채팅에 파일 2개 다운
- OCI
- 제05장-01. 상품 공통 사항 (스프링) (05.상품.txt)
- Category.java (05.상품.txt)
- Product 작성 (스프링) (05.상품.txt)
- 애플리케이션 실행 (스프링) (05.상품.txt)
- 데이터 베이스 확인 (MySQL) (05.상품.txt)
- 제05장-02. 상품 등록(단위 테스트)

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
