---
title: 2026-03-31 Spring Boot Controller와 HTML 응답
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png
status: growing
confidence: high
---
# 2026-03-31 Spring Boot Controller와 HTML 응답

## 한 줄 요약

Spring Boot의 Controller가 브라우저 요청을 받아 문자열 HTML 또는 데이터를 응답하는 가장 기본적인 흐름을 실습했다.

## 커리큘럼 위치와 흐름

전날 만든 Spring Boot 환경 위에서 “브라우저 요청 → Controller → 응답” 구조를 직접 확인했다. 아직 React와 완전히 연결하기 전이므로, Controller가 View/HTML 응답과 REST API 응답 사이에서 어떤 역할을 하는지 감을 잡는 단계다.

## 배운 내용

- `FruitHtmlController.java`를 만들고 `@GetMapping`으로 URL을 메서드에 연결했다.
- SpringBoot 교안 p.55~60의 프로젝트 구성 그림은 Controller-Service-Repository와 Entity/View/Config/application.properties/pom.xml의 위치를 보여준다.
- `@Controller`와 `@RestController`, `@GetMapping`, `@PathVariable`의 역할을 구분하기 시작했다.

## 핵심 실습 / 예제

- `/fruit01` 같은 경로로 브라우저가 요청하면 Controller 메서드가 실행되고 HTML 문자열 또는 데이터를 응답한다.
- 프로그램 흐름 그림은 사용자 요청이 화면/Controller/Service/Repository/DB 방향으로 내려갔다가 응답으로 되돌아오는 구조를 시각화한다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- Controller는 “화면 그 자체”가 아니라 요청을 받아 어느 로직으로 보낼지 결정하는 입구다.
- `@Controller`는 보통 View 반환과 연결되고, `@RestController`는 JSON/XML 같은 데이터 응답에 더 직접적으로 연결된다.
- 처음에는 HTML 문자열 응답으로 시작하지만, 이후 React와 연결되면 Controller는 API 데이터 제공자로 더 많이 쓰인다.

## 관련 페이지

- [[concepts/spring-boot-rest-api]]
- [[comparisons/controller-service-repository]]
- [[concepts/dto-entity-service-controller]]
- [[concepts/frontend-backend-architecture]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png`
