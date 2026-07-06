---
title: 2026-04-09 상품 삭제, 라우팅, JSX와 표
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
status: growing
confidence: high
---

# 2026-04-09 상품 삭제, 라우팅, JSX와 표

## 한 줄 요약

상품 삭제 기능을 구현하면서 관리자 role 조건부 렌더링, 라우팅 props 전달, JWT claim 수정, JSX 표현식과 table 병합 속성을 함께 다뤘다.

## 배운 내용

- 주제: 상품 삭제와 권한
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

상품 관리는 아무 사용자나 하면 안 되므로 프론트 화면과 백엔드 토큰 claim 모두에서 권한 정보를 다루기 시작했다.

## 핵심 개념

JwtTokenProvider에서 role을 claim으로 넣고 React ProductList에는 user props를 넘겨 ADMIN일 때만 삭제 버튼을 보이게 했다. 삭제 전 confirm, API 실패 시 error response alert 흐름도 확인했다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

프론트에서 버튼을 숨기는 것은 UX일 뿐 보안의 전부가 아니다. 실제 권한 검사는 백엔드에서도 필요하다. JSX에서 `{}`는 JS 표현식, `{{}}`는 JS 객체 리터럴을 넣을 때 사용된다.

## 관련 페이지

- [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
