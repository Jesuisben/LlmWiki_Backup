---
title: 2026-04-13 상품 상세와 useEffect, 서비스 계층
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
status: growing
confidence: high
---

# 2026-04-13 상품 상세와 useEffect, 서비스 계층

## 한 줄 요약

상품 상세/수정 조회를 위해 ProductService, ProductController, React useEffect를 연결하고 JPA 연관관계와 MVC/JDBC 복습 질문까지 확장했다.

## 배운 내용

- 주제: 상세 조회와 Service 계층
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

목록에서 특정 상품을 클릭하면 id로 상세 데이터를 다시 가져와야 한다. 이때 React 생명주기, URL parameter, Service 조회 로직이 함께 필요하다.

## 핵심 개념

ProductService의 `findById` 기반 조회, Controller의 path variable, React의 useEffect dependency를 연결했다. 원본에는 JPA 일대일/일대다/다대일, JoinColumn, 다대다 관계에 대한 질문도 함께 남아 있다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

useEffect의 dependency 배열을 비워 두면 최초 렌더링 중심이고 id/state를 넣으면 그 값이 바뀔 때 다시 실행된다. JPA 관계에서는 FK를 가진 쪽이 연관관계의 주인이라는 점이 중요하다.

## 관련 페이지

- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]], [[concepts/jpa-relationship-mapping|JPA 연관관계 매핑]], [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
