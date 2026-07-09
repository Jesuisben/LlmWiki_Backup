---
title: 2026-04-20 주문 목록과 테스트 시나리오
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: high
---

# 2026-04-20 주문 목록과 테스트 시나리오

## 한 줄 요약

OrderList 화면에서 주문 상태 변경·완료 처리·취소 처리와 MySQL 테스트 시나리오를 다루고, 홈 대표 상품/페이징 기능으로 넘어갔다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

주문은 생성 이후에도 완료/취소 같은 상태 변경이 필요하다. 프론트 버튼, REST 매핑, 서비스 로직, DB 상태가 같은 시나리오로 검증되어야 한다.

## 핵심 개념

- OrderList.tsx에서 주문 내역 표시, 상태 변경 버튼, 테스트 시나리오를 다뤘다.
- OrderRepository/OrderService/OrderController에서 주문 상품 완료 처리와 취소 처리를 구현했다.
- ProductService도 주문 취소 시 재고 복구 같은 흐름과 연결되었다.
- 홈페이지 대표 상품 캐러셀과 ProductRepository/ProductService/ProductController를 통해 상품 노출 기능으로 확장했다.

## 실습 / 예제

관리자/사용자 시나리오에 따라 주문 목록에서 상태를 변경하고, MySQL에서 결과 데이터가 맞는지 확인하는 방식으로 검증했다.

## 헷갈린 점 / 질문

REST 매핑은 URL 이름을 예쁘게 정하는 문제가 아니라 어떤 자원/order와 어떤 행위/status change를 어떤 HTTP method로 표현할지 정하는 문제다.

## 관련 페이지

- [[concepts/order-flow|주문 기능 흐름]], [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
