---
title: 2026-04-17 장바구니 합계와 Array some
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: high
---

# 2026-04-17 장바구니 합계와 Array some

## 한 줄 요약

장바구니 품목에 stock 정보를 추가하고 JavaScript Array.some으로 재고 부족 여부를 판단한 뒤 주문 생성 Service/Controller 흐름을 보강했다.

## 배운 내용

- 주제: 주문 가능 여부 판단
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

장바구니에서 바로 주문하려면 선택된 품목 중 하나라도 재고가 부족한지 빠르게 판단해야 한다.

## 핵심 개념

CartItemDto와 React CartProduct 타입에 stock을 추가했다. `some()`은 배열 요소 중 조건을 만족하는 것이 하나라도 있으면 true를 반환하므로 선택 상품 중 재고 부족 항목이 있는지 검사하는 데 적합하다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

`map()`은 변환/렌더링, `some()`은 조건 존재 여부 확인에 가깝다. 장바구니 합계는 선택 상태와 수량·가격을 함께 보아야 한다.

## 관련 페이지

- [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]], [[entities/javascript|JavaScript]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
