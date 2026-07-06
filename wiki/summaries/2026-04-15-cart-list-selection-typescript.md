---
title: 2026-04-15 장바구니 목록과 TypeScript props
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, typescript]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
status: growing
confidence: high
---

# 2026-04-15 장바구니 목록과 TypeScript props

## 한 줄 요약

React 장바구니 목록에서 전체 선택/개별 선택, 총 주문 금액 계산, props 구조 분해, TypeScript 타입 지정, 수량 변경 API 준비를 학습했다.

## 배운 내용

- 주제: 장바구니 화면 상태
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

장바구니는 서버 데이터만 보여주는 것이 아니라 체크 여부, 총액, 수량 변경 같은 화면 상태를 계속 계산해야 한다.

## 핵심 개념

orderTotalPrice state, refreshOrderTotalPrice, toggleAllCheckBox, 개별 체크 토글 함수로 선택 상태와 총 금액을 갱신했다. props로 받은 user는 구조 분해와 optional chaining으로 안전하게 접근했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

체크 여부는 DB 핵심 데이터라기보다 주문 대상을 고르기 위한 UI state다. TypeScript interface는 API 응답 구조와 화면에서 추가한 checked 같은 필드를 함께 명확히 해 준다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/react-form-state-event|React 폼 상태와 이벤트]], [[comparisons/props-vs-state|props vs state]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
