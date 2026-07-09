---
title: 2026-04-09 상품 삭제, 라우팅, JSX와 표
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
status: growing
confidence: high
---

# 2026-04-09 상품 삭제, 라우팅, JSX와 표

## 한 줄 요약

JWT claim 설정을 보정하고 상품 삭제·등록/수정/삭제 버튼·라우팅·ProductService/ProductController를 구현하며 JSX 표현식과 table 병합 속성을 함께 익혔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

상품 목록은 단순 조회에서 끝나지 않고 관리자 권한에 따라 수정/삭제/등록으로 이어진다. 화면 버튼과 백엔드 API가 같은 기능 단위로 맞아야 한다.

## 핵심 개념

- JwtTokenProvider에서 `setClaims` 대신 `claim`을 써서 기존 claim 덮어쓰기 문제를 피하는 관점을 확인했다.
- ProductList에 user props를 넘겨 관리자 조건부 버튼 표시를 준비했다.
- `rowSpan`, `colSpan`, JSX `{}` 표현식, 이벤트 버블링 방지를 상품 목록 화면에서 학습했다.
- ProductService/ProductController에서 삭제와 등록 API 흐름을 작성했다.

## 실습 / 예제

React 라우팅에 상품 등록/수정 페이지를 연결하고, Service/Controller에서 상품 삭제 요청을 처리하는 흐름을 맞췄다.

## 헷갈린 점 / 질문

프론트에서 버튼을 숨기는 것은 UX 보조일 뿐이다. 실제 권한 검사는 백엔드 API에서도 반드시 필요하다.

## 관련 페이지

- [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/react-form-state-event|React 폼 상태와 이벤트]], [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
