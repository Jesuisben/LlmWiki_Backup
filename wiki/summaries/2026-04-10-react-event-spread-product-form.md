---
title: 2026-04-10 React 이벤트 객체와 전개 연산자
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, typescript]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
status: growing
confidence: high
---

# 2026-04-10 React 이벤트 객체와 전개 연산자

## 한 줄 요약

React의 event object와 전개 연산자를 이용해 상품 등록/수정 Form state를 갱신하고 Spring Controller의 검증 오류 응답을 화면에 연결했다.

## 배운 내용

- 주제: 폼 상태 관리
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

상품 등록 화면은 여러 input 값을 하나의 객체 state로 모아야 하므로 이벤트와 전개 연산자가 실제 프로젝트 패턴으로 등장했다.

## 핵심 개념

`event.target`에서 name과 value를 꺼내 `setProduct({ ...product, [name]: value })` 형태로 해당 필드만 갱신했다. Spring Controller는 `@Valid`, `@RequestBody`, `BindingResult`로 오류를 모으고 React는 errors와 general message를 화면 오류 state에 반영했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

전개 연산자는 기존 객체를 복사한 뒤 바뀐 속성만 덮어쓰는 패턴이다. 직접 state 객체를 수정하면 React가 변경을 감지하지 못할 수 있다.

## 관련 페이지

- [[concepts/react-form-state-event|React 폼 상태와 이벤트]], [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
