---
title: 풀스택 프로젝트 흐름
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [frontend, backend, project, spring-boot, react]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
status: growing
confidence: medium
---

# 풀스택 프로젝트 흐름

## 정의

풀스택 프로젝트 흐름은 사용자의 화면 조작이 React 프론트엔드에서 시작해 Spring Boot 백엔드 API, Service, Repository, Database로 이어지고 다시 응답으로 돌아오는 전체 구조다.

## 왜 중요한가

학원 실습은 로그인, 상품, 장바구니, 주문처럼 기능이 이어진다. 각 파일을 따로 외우면 복잡하지만, 요청과 응답의 이동 경로로 보면 역할이 분리된다.

## 핵심 설명

1. React 화면에서 이벤트가 발생한다.
2. React가 필요한 데이터를 state/props로 모으고 API 요청을 보낸다.
3. Spring Boot Controller가 요청을 받는다.
4. Service가 업무 규칙을 처리한다.
5. Repository가 DB 조회/저장을 담당한다.
6. DTO나 응답 데이터가 다시 React로 돌아와 화면이 갱신된다.

## 예시

- 상품 목록: React `ProductList` → Spring Controller → Service → Repository → 상품 목록 응답
- 장바구니: React `CartList` → CartController → CartService/CartProductService → 장바구니 품목 저장·수량 변경
- 주문: 장바구니 선택 → 주문 생성 → 주문 목록 조회

## 자주 헷갈리는 점

- React Router의 페이지 주소와 Spring API 주소는 같은 URL처럼 보여도 역할이 다르다.
- Entity는 DB와 가까운 객체이고 DTO는 화면/API 전달 목적의 객체다.
- Controller에 모든 로직을 넣지 않고 Service로 분리하는 이유는 유지보수와 테스트 때문이다.

## 관련 개념

- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
