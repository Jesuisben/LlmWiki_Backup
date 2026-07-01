---
title: 2026-04-03 Member 데이터 준비와 React JSX 기초
created: 2026-07-01
updated: 2026-07-01
type: summary
tags: [spring-boot, react, typescript, backend, frontend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
status: growing
confidence: medium
---

# 2026-04-03 Member 데이터 준비와 React JSX 기초

## 한 줄 요약

Spring Boot 쪽 Member 데이터를 준비하고 React/JSX에서 주석, 단축키, 기본 편집 흐름을 익혔다.

## 배운 내용

- Member 엔티티 샘플 데이터
- Role과 regdate 설정
- JSX 주석
- VS Code 편집 단축키
- React 화면과 백엔드 데이터 연결

## 원본에서 확인한 세부 주제

- VSC 한줄 복사 단축키
- JSX에서 주석 넣는 법
- Member 테이블에 다른 데이터들 추가
- (IT 관련 용어 PDF (P.35))
- (IT 관련 용어 PDF (P.36))
- 회원가입 (04.회원.txt)
- 라우팅 설정 : AppRouters.tsx (04.회원.txt)
- Member.java (Spring) 보고 회원 가입에 필요한 사항 체크하기

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

- `raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
