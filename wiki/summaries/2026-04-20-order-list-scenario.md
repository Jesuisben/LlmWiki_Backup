---
title: 2026-04-20 주문 목록과 테스트 시나리오
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [react, typescript, spring-boot, project, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: medium
---

# 2026-04-20 주문 목록과 테스트 시나리오

## 한 줄 요약

주문 기능으로 넘어가 OrderList 화면을 만들고 관리자/일반 사용자 기준 테스트 시나리오를 정리했다.

## 배운 내용

- OrderList.tsx
- 주문 상태 표시
- 최신 주문 우선 조회
- 관리자/일반 사용자 테스트
- 주문 도메인 흐름

## 원본에서 확인한 세부 주제

- 주문 목록(OrderLIst.tsx) (리액트) (07.주문.txt)
- 테스트 시나리오 (리액트) (07.주문.txt)
- 상태 변경 버튼 생성 (리액트) (07.주문.txt)
- 제07장-03. 주문 상품 완료 처리
- 주문 목록(완료 처리) (리액트) (07.주문.txt)
- 리포지터리(OrderRepository) (스프링) (07.주문.txt)
- 서비스(OrderService) (스프링) (07.주문.txt)
- 컨트롤러(OrderController) (스프링) (07.주문.txt)

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
- [[concepts/order-flow|주문 기능 흐름]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
