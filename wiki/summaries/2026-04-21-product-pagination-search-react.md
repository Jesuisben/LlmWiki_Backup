---
title: 2026-04-21 상품 목록 페이징과 필드 검색
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: high
---

# 2026-04-21 상품 목록 페이징과 필드 검색

## 한 줄 요약

React 상품 목록에서 pageNumber, pageSize, 검색 조건 state를 추가하고 Spring Pageable 응답의 content/page 정보를 화면 페이징 컴포넌트와 연결했다.

## 배운 내용

- 주제: 프론트 페이징/검색
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

상품이 많아지면 전체를 한 번에 가져오지 않고 페이지 단위로 가져와야 한다. 검색 조건도 React state와 API query parameter로 관리된다.

## 핵심 개념

ProductList는 응답의 `response.data.content`를 상품 배열로 사용하고 pageable 정보에서 pageNumber/pageSize를 읽어 paging state를 갱신한다. optional chaining과 nullish coalescing으로 값이 없을 때 기본값을 둔다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

`?` 하나는 optional chaining, `??`는 null 또는 undefined일 때 기본값을 쓰는 연산자다. 페이징은 React 화면 상태와 Spring Pageable 요청/응답이 맞아야 동작한다.

## 관련 페이지

- [[concepts/pagination-search|페이징과 검색]], [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]], [[concepts/spring-product-search-flow|Spring 상품 검색 흐름]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
