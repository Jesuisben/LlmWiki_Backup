---
title: 2026-04-10 React 이벤트 객체와 전개 연산자
created: 2026-07-06
updated: 2026-07-09
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
status: growing
confidence: high
---

# 2026-04-10 React 이벤트 객체와 전개 연산자

## 한 줄 요약

React Event Object와 전개 연산자로 ProductInsertForm state를 관리하고, Spring ProductService/ProductController의 등록·수정 API와 연결했다.

## 배운 내용

- 커리큘럼 위치: 4과목은 Spring Boot와 React를 연결해 실제 쇼핑몰 기능을 만드는 단계이고, 5과목은 그 결과물을 Linux/Docker/GitHub 운영·협업 환경으로 옮기는 단계다.
- 이전 흐름: 4과목은 [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]] 이후, 5과목은 [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]] 이후의 운영 단계다.
- 다음 흐름: 이 내용은 이후 [[entities/aws|AWS]], [[concepts/ci-cd-automation|CI/CD 자동화]], 중간 프로젝트 배포·인증 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

입력 폼은 여러 필드를 동시에 다루기 때문에 이벤트 객체에서 name/value를 꺼내 기존 state를 보존하며 일부만 바꾸는 패턴이 중요하다.

## 핵심 개념

- React Event Object와 전개 연산자(`...`)를 상품 등록 폼 입력값 갱신에 적용했다.
- ProductInsertForm.tsx에서 상품명·가격·재고·카테고리·이미지 같은 입력 상태를 관리했다.
- Spring ProductService/ProductController의 등록 처리와 React 폼 제출을 맞췄다.
- 상품 수정은 등록과 비슷하지만 기존 데이터를 먼저 불러오고 id 기준으로 PUT 요청을 보낸다는 차이를 확인했다.

## 실습 / 예제

`setForm({...form, [name]: value})` 형태의 사고방식으로 여러 input을 하나의 객체 state에 반영하는 패턴을 익혔다.

## 헷갈린 점 / 질문

전개 연산자는 객체를 “깊은 복사”하는 만능 도구가 아니라 기존 1단계 속성을 펼쳐 새 객체를 만드는 문법이다. 중첩 객체는 별도 처리가 필요하다.

## 관련 페이지

- [[concepts/react-form-state-event|React 폼 상태와 이벤트]], [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[comparisons/props-vs-state|props vs state]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
