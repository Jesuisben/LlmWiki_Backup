---
title: 2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환
created: 2026-07-06
updated: 2026-07-06
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
status: growing
confidence: high
---

# 2026-03-30 FrontEnd/BackEnd 개발 환경과 커리큘럼 전환

## 한 줄 요약

Spring Boot·React·TypeScript·MySQL·Node.js·VS Code를 설치하고 Java/Oracle/UI&UX 이후 풀스택 프로젝트 과정으로 넘어갈 실행 환경을 만든 날이다.

## 배운 내용

- 주제: 환경 준비
- 커리큘럼 위치: Java/Oracle/UI&UX 다음 단계에서 React 화면과 Spring Boot API를 실제 기능 단위로 연결하는 FrontEnd_BackEnd 과정이다.
- 이전 흐름: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]에서 HTML/CSS/JavaScript/Bootstrap/jQuery로 브라우저 화면을 만들었다.
- 다음 흐름: 이 날짜의 내용은 이후 Linux/AWS/CI/CD에서 Spring Boot 애플리케이션을 서버에 올리고 배포하는 흐름으로 이어진다.

## 왜 이 흐름으로 배웠는가

백엔드 IDE, DB, 프론트 런타임, 편집기를 모두 맞춰야 같은 예제 코드를 실행할 수 있었다.

## 핵심 개념

MySQL Installer, Node.js, VS Code, IntelliJ/Spring Initializr 설정을 확인했다. React 쪽에서는 Vite build, `npm install`, `npm run dev`가 앞으로 화면 개발의 반복 루프가 된다는 점을 잡았다.

## 실습 / 예제

- 원본 노트의 코드는 대부분 Spring Boot `controller/service/repository/entity/dto/config`와 React `pages/types/api/routes` 파일을 실제로 수정하는 형태다.
- 실습을 복습할 때는 파일명 전체를 외우기보다 “요청 URL → Controller → Service → Repository/DB → DTO/응답 → React state/render” 순서로 따라가면 된다.
- 실습 데이터나 비밀번호 형태의 예시는 위키에 그대로 재노출하지 않고 역할 중심으로만 정리했다.

## 헷갈린 점 / 질문

`build`는 React/Vite 파일을 배포 가능한 묶음으로 만드는 과정이고, `npm`은 Node 생태계의 패키지 설치·실행 도구다. 설치 도구가 많아 보여도 역할은 DB, 백엔드 실행, 프론트 실행, 코드 편집으로 나뉜다.

## 관련 페이지

- [[entities/mysql|MySQL]], [[entities/node-js|Node.js]], [[entities/visual-studio-code|Visual Studio Code]], [[entities/spring-boot|Spring Boot]], [[entities/react|React]]
- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
