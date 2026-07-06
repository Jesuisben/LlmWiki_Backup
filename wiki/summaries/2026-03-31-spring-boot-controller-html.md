---
title: 2026-03-31 Spring Boot Controller와 HTML 응답
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
status: growing
confidence: high
---

# 2026-03-31 Spring Boot Controller와 HTML 응답

## 한 줄 요약

Spring Boot에서 Fruit Entity, HTML Controller, REST Controller를 만들며 브라우저 요청이 Controller를 거쳐 응답으로 바뀌는 흐름을 처음 구현했다.

## 배운 내용

- 주제: Spring Controller 입문
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

UI&UX까지는 브라우저 안의 HTML/JS가 중심이었다면, 이날부터는 서버가 URL 요청을 받아 HTML 또는 JSON 데이터를 돌려주는 구조를 배웠다.

## 핵심 개념

`FruitHtmlController`는 `@Controller`와 `@GetMapping("/fruit")`로 HTML 화면을 반환하고, REST Controller는 과일 데이터를 JSON으로 반환한다. `resources/templates`에는 서버가 조립해 보여줄 HTML을 두고, JSON은 React가 데이터로 받아 화면을 구성하는 기반이 된다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

`@Controller`와 `@RestController`를 헷갈리기 쉽다. 전자는 화면 이름/HTML 응답 중심, 후자는 데이터 응답 중심이다. URL 안의 추가 주소는 `@GetMapping` 경로와 대응된다.

## 관련 페이지

- [[concepts/spring-boot-rest-api|Spring Boot REST API]], [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]], [[comparisons/controller-service-repository|Controller vs Service vs Repository]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
