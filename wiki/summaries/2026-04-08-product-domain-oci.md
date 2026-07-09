---
title: 2026-04-08 상품 도메인과 OCI 소개
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, backend, frontend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
status: growing
confidence: high
---

# 2026-04-08 상품 도메인과 OCI 소개

## 한 줄 요약

상품 기능 구현을 시작하며 Category enum, Product Entity, Repository, GenerateData, 단위 테스트를 만들고 OCI를 AWS와 비슷한 클라우드 맥락으로 소개받았다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

쇼핑몰 프로젝트에서 상품은 장바구니와 주문의 기준 데이터다. 상품 도메인을 먼저 만들면 이후 기능들이 Product를 참조해 확장된다.

## 핵심 개념

- Category enum으로 상품 카테고리를 정의했다.
- Product Entity를 작성하고 애플리케이션 실행 후 MySQL 테이블 생성/데이터 확인 흐름을 봤다.
- 이미지 파일을 Spring 정적 리소스 영역에 복사하고 상품 데이터와 연결할 준비를 했다.
- ProductRepository, GenerateData, 단위 테스트로 상품 seed 데이터와 조회 흐름을 확인했다.

## 실습 / 예제

Category/Product 작성 → DB 확인 → GenerateData로 테스트 데이터 생성 → ProductRepository 단위 테스트 순서로 백엔드 상품 기반을 만들었다.

## 헷갈린 점 / 질문

Category enum은 DB 테이블과 1:1로 같은 개념이 아니라 Java 코드에서 허용된 카테고리 값을 제한하는 타입이다. 실제 저장 방식은 Entity 매핑 설정에 따라 달라진다.

## 관련 페이지

- [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]], [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
