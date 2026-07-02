---
title: 2026-04-08 상품 도메인과 OCI 소개
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---
# 2026-04-08 상품 도메인과 OCI 소개

## 한 줄 요약

회원 기능 이후 상품 도메인으로 넘어가 Category/Product Entity와 상품 기능의 기본 구조를 만들기 시작했다.

## 커리큘럼 위치와 흐름

로그인/회원 기반을 만든 뒤 쇼핑몰의 핵심 도메인인 상품으로 전환했다. Category와 Product는 이후 목록, 상세, 등록, 삭제, 검색, 장바구니와 모두 연결되는 중심 데이터다.

## 배운 내용

- `Category.java`, `Product.java`를 작성하고 Spring 애플리케이션 실행과 DB 테이블 확인 흐름을 다뤘다.
- OCI 가입 자료가 언급되지만 현재 교육자료 폴더에는 별도 OCI PDF가 없어, 이번 백필에서는 raw MD의 언급만 출처로 남긴다.
- Spring Boot 프로젝트 구성 관점에서 Entity는 JPA와 DB 테이블 연결의 중심이다.

## 핵심 실습 / 예제

- 상품 Entity에는 이름, 설명, 가격, 재고, 이미지 같은 화면/DB 양쪽에서 필요한 정보가 들어간다.
- Category는 상품 분류를 담당하며, 이후 검색/필터링과 연결된다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- Entity는 React 화면용 타입과 비슷해 보이지만 DB/JPA와 더 가까운 객체다.
- 상품 도메인은 단순 목록 표시가 아니라 장바구니·주문·재고 검증의 출발점이다.
- 클라우드 OCI 언급은 이후 AWS/Linux/배포 흐름과 연결될 수 있지만, 이 날짜의 핵심은 상품 도메인 시작이다.

## 관련 페이지

- [[concepts/product-domain-flow]]
- [[comparisons/entity-vs-dto]]
- [[concepts/dto-entity-service-controller]]
- [[entities/spring-boot]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
