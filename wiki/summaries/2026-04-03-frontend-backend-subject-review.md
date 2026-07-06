---
title: FrontEnd_BackEnd 총정리
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# FrontEnd_BackEnd 총정리

## 한 줄 요약

2026-03-30~2026-04-22 풀스택 과정 전체를 환경 세팅, Spring/React 연결, 회원/JWT, 상품, 장바구니, 주문, 페이징/검색 흐름으로 묶은 복습 허브다.

## 배운 내용

- 주제: 과목 복습 허브
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

이 파일은 날짜별 노트를 다시 이어 붙이는 역할을 한다. 단순 문법 복습이 아니라 React 화면 → Spring API → Service/Repository → DB가 기능 단위로 반복되는 구조를 보는 것이 핵심이다.

## 핵심 개념

초반에는 MySQL/Node/VS Code/Spring Boot 환경과 Fruit 예제를 다뤘다. 중반에는 회원가입·로그인·JWT·Bearer 토큰·SecurityContext를 다뤘다. 후반에는 Product/Cart/Order 도메인, DTO, Service, Controller, React state, useEffect, axios 요청, 페이징/검색까지 이어졌다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

파일명보다 책임을 먼저 잡는 것이 좋다. Controller는 요청 입구, Service는 업무 규칙, Repository는 DB 접근, React component는 화면 상태와 이벤트를 담당한다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
