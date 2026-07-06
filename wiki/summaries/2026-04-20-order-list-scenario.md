---
title: 2026-04-20 주문 목록과 테스트 시나리오
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: high
---

# 2026-04-20 주문 목록과 테스트 시나리오

## 한 줄 요약

주문 목록 화면을 만들고 관리자/사용자 role에 따라 주문 상태 변경 버튼을 표시하며 JPQL 업데이트 쿼리와 테스트 시나리오를 정리했다.

## 배운 내용

- 주제: 주문 목록과 상태 관리
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

장바구니에서 주문이 생성된 뒤에는 주문 내역 조회와 상태 변경이 필요하다. 관리자와 일반 사용자가 보는 기능도 달라진다.

## 핵심 개념

React OrderList는 orders 배열을 map으로 렌더링하고 주문 번호, 주문 상품, 상태를 카드 형태로 보여준다. 관리자는 상태 변경 버튼을 볼 수 있으며 `/order/update/{id}?status=...` API로 주문 상태를 바꾼다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

JPQL과 SQL은 비슷해 보여도 대상이 다르다. JPQL은 Entity와 필드명을 기준으로 쓰고 SQL은 실제 테이블과 컬럼명을 기준으로 쓴다.

## 관련 페이지

- [[concepts/order-flow|주문 기능 흐름]], [[comparisons/jpql-vs-sql|JPQL vs SQL]], [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
