---
title: 2026-04-01 React 라우팅과 Spring Boot 연동 흐름
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, typescript]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
status: growing
confidence: high
---

# 2026-04-01 React 라우팅과 Spring Boot 연동 흐름

## 한 줄 요약

React에서 MenuItems, AppRoutes, TypeScript 타입, useEffect를 이용해 Spring Boot API 데이터와 화면 라우팅을 연결하기 시작했다.

## 배운 내용

- 주제: React Router와 API 연결
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

전날 Spring Controller가 데이터를 내보냈다면, 이날은 React가 그 데이터를 화면 컴포넌트로 가져와 보여주는 쪽을 배웠다.

## 핵심 개념

`MenuItems.tsx`에 이동 메뉴를 추가하고 `AppRoutes.tsx`에서 URL path와 컴포넌트를 연결했다. `types/Fruit.ts`에는 Spring의 Fruit 데이터와 같은 필드 구조를 TypeScript interface로 선언했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

React Router의 화면 주소와 Spring API 주소는 역할이 다르다. `..` 경로는 현재 파일 위치 기준 상위 폴더를 의미하며, port가 다르면 origin도 달라 CORS를 고려해야 한다.

## 관련 페이지

- [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]], [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
