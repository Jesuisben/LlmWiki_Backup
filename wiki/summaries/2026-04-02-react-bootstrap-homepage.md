---
title: 2026-04-02 React Bootstrap과 HomePage 구성
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, typescript]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
status: growing
confidence: high
---

# 2026-04-02 React Bootstrap과 HomePage 구성

## 한 줄 요약

React Bootstrap의 Carousel·Card와 JSX 문법을 이용해 홈 화면을 구성하고 Spring Boot의 정적 이미지·DB 설정·보안 설정 흐름을 확인했다.

## 배운 내용

- 주제: 화면 구성과 Spring 설정
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

Spring이 이미지를 제공하고 React가 화면을 조립하는 구조를 확인하면서 풀스택 프로젝트가 서버 설정과 프론트 컴포넌트로 동시에 움직인다는 감각을 잡았다.

## 핵심 개념

`HomePage.tsx`를 만들고 React Bootstrap Carousel을 적용했다. JSX에서는 `class` 대신 `className`, JS 표현식에는 `{}`를 사용한다. Spring 쪽에서는 datasource, JPA ddl-auto, static image 경로, PasswordEncoder Bean 설정을 접했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

`ddl-auto=create`는 실행 시 테이블을 새로 만들 수 있어 데이터가 날아갈 수 있고, `update`는 기존 구조를 가능한 한 유지한다. PasswordEncoder는 비밀번호 평문 저장을 피하기 위한 Bean이다.

## 관련 페이지

- [[entities/react|React]], [[entities/spring-boot|Spring Boot]], [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
