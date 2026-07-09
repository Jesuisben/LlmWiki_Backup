---
title: 2026-04-15 장바구니 목록과 TypeScript props
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
status: growing
confidence: high
---

# 2026-04-15 장바구니 목록과 TypeScript props

## 한 줄 요약

CartList에서 전체 선택·개별 선택·수량 변경·삭제 함수를 만들고, URL parameter와 Spring Service/Controller 수정 흐름을 연결했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

장바구니 화면은 체크박스 선택, 수량 변경, 삭제처럼 사용자 이벤트가 많다. React state와 백엔드 변경 API가 동시에 맞아야 한다.

## 핵심 개념

- CartList에서 전체 선택과 개별 선택 상태를 관리했다.
- MenuItems/AppRoutes에 장바구니 메뉴와 경로를 연결했다.
- CartProductService/CartController를 수정해 수량 변경과 삭제 API를 만들었다.
- URL parameter를 React에서 변수로 받아 API 요청에 사용하는 흐름을 확인했다.

## 실습 / 예제

선택된 품목 id 목록을 state로 관리하고, 수량 변경/삭제 버튼이 Spring API를 호출한 뒤 목록을 갱신하는 패턴을 실습했다.

## 헷갈린 점 / 질문

React의 선택 상태는 화면 상태이고, Spring의 장바구니 품목 수량은 서버/DB 상태다. 버튼 클릭 후 API 성공 시 두 상태를 다시 동기화해야 한다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/react-form-state-event|React 폼 상태와 이벤트]], [[concepts/react-typescript-basics|React와 TypeScript 기본]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
