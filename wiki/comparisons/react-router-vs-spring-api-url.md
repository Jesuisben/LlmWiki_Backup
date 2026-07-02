---
title: React Router 주소 vs Spring API 주소
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [react, spring-boot, frontend, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/FrontEnd&BackEnd.pdf
status: growing
confidence: high
---

# React Router 주소 vs Spring API 주소

## 비교 목적

React 화면 전환 주소와 Spring Boot 데이터 요청 주소를 구분한다.

## 한눈에 보기

| 항목 | React Router 주소 | Spring API 주소 |
|---|---|---|
| 담당 | 프론트 화면 전환 | 백엔드 데이터 요청 |
| 실행 위치 | 브라우저/React 앱 | Spring Boot 서버 |
| 관련 파일 | App.tsx, MenuItems, 화면 컴포넌트 | Controller, Service, Repository |
| 결과 | 컴포넌트 화면 | JSON/응답 데이터 |

## 언제 무엇을 쓰는가

수업 예제에서 실제 기능을 추적할 때는 먼저 '어느 계층의 문제인가'를 본다. 화면 상태인지, 서버 인증인지, DB 저장인지에 따라 선택지가 달라진다.

## 헷갈리기 쉬운 포인트

둘 다 URL처럼 보이지만 React Router는 프론트 앱 내부의 페이지 선택이고, Spring API는 서버 통신이다.

## 관련 페이지

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]


## 교육자료 대조 보강

라우터 설명 이미지는 Router가 관객을 알맞은 극장으로 안내하듯 URL에 맞는 화면 컴포넌트를 선택하는 역할임을 보여준다. 반면 Spring API URL은 서버의 Controller 메서드와 연결되어 데이터 조회/등록/수정/삭제를 수행한다. 따라서 같은 `/products`처럼 보여도 “화면 경로”인지 “API 경로”인지 먼저 구분해야 한다.

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
