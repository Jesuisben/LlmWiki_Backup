---
title: DTO, Entity, Service, Controller
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [spring-boot, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/쇼핑 카트 데이터 구조 다이어그램.png
status: growing
confidence: high
---

# DTO, Entity, Service, Controller

## 정의

Spring Boot 백엔드에서 데이터를 표현하고 요청을 처리하는 역할 구분이다.

## 왜 중요한가

FrontEnd_BackEnd 단계에서는 문법 하나보다 화면, API, 업무 규칙, DB가 어떻게 연결되는지가 중요하다. 이 개념은 사용자의 쇼핑몰형 실습에서 반복 등장하는 흐름을 복원하기 위한 기준점이다.

## 핵심 설명

- Entity는 DB 테이블과 가까운 도메인 객체다.
- DTO는 요청/응답에 필요한 데이터만 담는 전달 객체다.
- Controller는 HTTP 요청을 받아 응답을 반환한다.
- Service는 업무 규칙을 처리한다.
- Repository는 DB 조회/저장을 담당한다.

## 수업 예시

- Fruit Entity와 Controller
- CartProductDto, CartProductService, CartService, CartController
- ProductRepository, ProductService, ProductController의 페이징/검색 처리

## 자주 헷갈리는 점

비슷한 이름의 파일이나 URL이 여러 계층에 존재한다. React의 화면 상태, Spring의 요청 처리, DB 저장 상태를 같은 것으로 보지 말고 역할별로 나누어 추적해야 한다.

## 관련 개념

- [[comparisons/entity-vs-dto|Entity vs DTO]]
- [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]


## 교육자료 대조 보강

SpringBoot 교안의 프로젝트 구성도는 Controller/Service/Repository/Entity의 위치를, 장바구니 다이어그램은 Cart/CartProduct/Product 관계를 보여준다. 이를 바탕으로 DTO는 API 입출력 모양, Entity는 JPA/DB 관계, Service는 업무 규칙, Controller는 HTTP 요청 입구라는 구분을 보강했다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
