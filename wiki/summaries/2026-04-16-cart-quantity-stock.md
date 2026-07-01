---
title: 2026-04-16 장바구니 수량 변경과 재고 검증
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [spring-boot, backend, react, typescript, project]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
status: growing
confidence: medium
---

# 2026-04-16 장바구니 수량 변경과 재고 검증

## 한 줄 요약

CartProductService와 CartController를 수정해 장바구니 품목 찾기, 수량 변경, 재고 부족 처리를 다뤘다.

## 배운 내용

- CartProductService 수정
- CartController 수정
- Optional과 품목 조회
- 재고 수량 검증
- 오류 메시지 반환

## 원본에서 확인한 세부 주제

- CartProductService / CartController (스프링) 수정
- CartList.tsx (리액트) 수정
- 정규화에 대해서 (디비버(Dbeaver) 사용법(version 2.0) PDF (P.24~))
- 제07장-01. 주문하기
- 열거형(OrderStatus) (스프링) (07.주문.txt)
- 연관 관계 매핑 - 영속성 전이 (SpringBoot 교안 PDF (P.158))
- 주문 엔터티(Order) 신규 작성 (스프링) (07.주문.txt)
- 주문 상품(OrderProduct) (스프링) (07.주문.txt)

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
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
