---
title: 2026-04-03 Member 데이터 준비와 React JSX 기초
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, typescript]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
status: growing
confidence: high
---

# 2026-04-03 Member 데이터 준비와 React JSX 기초

## 한 줄 요약

Member 테스트 데이터를 추가하고 React JSX 주석·편집 단축키를 익힌 뒤 회원가입 API의 검증 흐름으로 넘어갔다.

## 배운 내용

- 주제: 회원 도메인 준비
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

로그인/회원가입 기능으로 가기 전 DB에 회원 데이터가 필요했고, React 화면에서는 JSX 문법과 컴포넌트 편집 습관을 익혀야 했다.

## 핵심 개념

Spring 테스트 코드에서 Member 객체를 만들고 저장했다. 이후 회원가입 Controller에서 JSON 요청 본문을 Entity/DTO로 받고 `@Valid`, `@RequestBody`, `BindingResult`로 검증 실패를 처리하는 형태를 확인했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

예제 원본에는 이메일·비밀번호 모양의 실습 데이터가 있지만 위키에서는 실제 값보다 역할만 기억하는 것이 안전하다. `save`는 Spring Data 상위 인터페이스에서 물려받은 메서드다.

## 관련 페이지

- [[comparisons/entity-vs-dto|Entity vs DTO]], [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]], [[entities/spring-boot|Spring Boot]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
