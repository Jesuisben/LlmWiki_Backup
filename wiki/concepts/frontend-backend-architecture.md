---
title: Frontend/Backend 구조
created: 2026-07-02
updated: 2026-07-03
type: concept
tags: [frontend, backend, spring-boot, react]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
status: growing
confidence: high
---
# Frontend/Backend 구조

## 정의

Frontend는 사용자가 보는 화면과 상호작용을 담당하고, Backend는 데이터 처리·업무 로직·DB 접근·인증을 담당한다. 이 과정에서는 [[entities/react|React]]가 프론트엔드, [[entities/spring-boot|Spring Boot]]가 백엔드의 중심이다.

## 왜 중요한가

HTML/CSS/JavaScript만 배울 때는 브라우저 안의 화면 구성에 집중했다. FrontEnd_BackEnd 과정부터는 사용자의 클릭이 React 컴포넌트 상태를 바꾸고, API 요청이 Spring Controller로 들어가며, Service/Repository를 거쳐 DB와 연결되는 전체 왕복 흐름을 이해해야 한다.

## 핵심 설명

SpringBoot 교안의 프로젝트 구성 그림은 요청/응답이 View 또는 template, Controller, Service, Repository, Entity, Database로 이어지는 구조를 보여준다. 이 수업에서는 View/template 역할의 상당 부분을 React가 맡고, Spring Boot는 REST API와 업무 로직을 제공하는 쪽으로 확장된다.

```text
사용자 클릭/입력
→ React Router 또는 컴포넌트 이벤트
→ API 요청(fetch/axios 등)
→ Spring Controller
→ Service 업무 규칙
→ Repository/JPA
→ MySQL DB
→ JSON 응답
→ React state 갱신
→ 화면 렌더링
```

## 수업 예시

- [[summaries/2026-03-30-fullstack-environment-setup|2026-03-30]] — MySQL, Node.js, VS Code, IntelliJ, Spring Boot 프로젝트 준비
- [[summaries/2026-03-31-spring-boot-controller-html|2026-03-31]] — Controller가 브라우저 요청을 받아 응답하는 기본 구조 확인
- [[summaries/2026-04-14-cart-service|2026-04-14]] — 장바구니 기능에서 Controller/Service/DTO/Entity가 연결됨

## 자주 헷갈리는 점

- React Router 주소는 화면 선택이고, Spring API URL은 서버 데이터 요청이다.
- Entity는 DB/JPA와 가까운 객체이고, TypeScript interface는 프론트가 기대하는 데이터 모양이다.
- 프론트에서 검증해도 백엔드에서 업무 규칙과 권한 검증을 다시 해야 한다.

## 관련 개념

- [[concepts/fullstack-project-flow]]
- [[comparisons/react-router-vs-spring-api-url]]
- [[comparisons/controller-service-repository]]
- [[concepts/spring-boot-rest-api]]
- [[concepts/react-typescript-basics]]
- [[concepts/passwordless-qr-app-approval]]
- [[concepts/spring-boot-passwordless-integration]]

## Passwordless 흐름으로 본 확장 예시

Passwordless를 붙이면 React는 QR 표시·승인 대기·결과 polling 같은 상태를 맡고, Spring Boot는 X1280 인증 서버 REST API 호출과 결과 해석을 맡는다. 즉 기존 Frontend/Backend 왕복 흐름에 외부 인증 서버와 모바일 앱 승인 단계가 추가된다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/Study/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/프로그램 흐름 그림.png`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
