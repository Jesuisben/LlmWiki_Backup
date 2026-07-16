---
title: Node.js
created: 2026-07-01
updated: 2026-07-16
type: entity
tags: [javascript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
status: growing
confidence: high
---

# Node.js

## 무엇인가

Node.js는 브라우저 밖에서 JavaScript를 실행하는 runtime이다. 이 과목에서는 Spring Boot 서버용 runtime이 아니라, npm과 Vite 같은 React 개발 도구를 실행할 기반으로 설치했다.

## 왜 중요한가

UI&UX 과목의 브라우저 JavaScript에서 React/TypeScript 프로젝트 개발로 넘어가려면 package 설치, project scaffold, development server 실행을 담당할 도구 환경이 필요했다. Node.js는 그 환경의 실행 기반이었고, 실제 package 관리는 npm, React project 생성·development server·build 도구 역할은 Vite가 맡았다.

## 이 위키에서의 맥락

첫 등장은 [[summaries/2026-03-30-fullstack-environment-setup|2026-03-30 개발환경 구성]]이다. Node.js를 설치하고 `npm -version`으로 npm 11.11.0이 보이는 것을 확인한 뒤, npm을 통해 Vite React project를 만들고 package를 설치하고 development server를 실행했다. 03-31에는 VS Code에서 그 project를 열어 `node_modules`가 전날 `npm install`로 설치한 package를 담는 폴더임을 확인했다.

## 대표 artifact와 입력 → 처리 → 결과

| 구간 | 대표 artifact | 입력 | 처리 주체 | 확인된 결과 |
|---|---|---|---|---|
| 설치 확인 | npm version 확인 | 관리자 명령창에서 npm version 조회 | 설치된 Node.js 환경에서 npm 실행 | 11.11.0 표시 확인 |
| project 생성 | `react_cafe` | Vite 생성 명령과 React·TypeScript variant 선택 | npm이 Vite 실행을 중개하고 Vite가 scaffold 생성 | project 폴더와 후속 실행 안내 생성 |
| package 준비 | `node_modules` | package 설치 | npm이 dependency 설치 | 03-31에 `node_modules` 내용의 용도 확인 |
| 개발 화면 | Vite development server | project 폴더에서 dev script 실행 | Node.js 환경에서 Vite 실행 | Vite 8.0.3 안내와 5173번 초기 화면 확인 |

## 확인된 범위와 미확정 범위

- 확인됨: Node.js 설치, npm version 표시, Vite scaffold, npm package 설치·목록 확인, Vite development server와 초기 React 화면 실행.
- 확인됨: axios, React Router DOM, Bootstrap, React Bootstrap 설치는 npm이 수행한 package 관리 작업이다.
- 미확정: 원본은 배포용 Vite build 산출물을 실제 생성·검증한 결과를 기록하지 않는다. project 생성과 development server 성공을 production build 성공으로 확대하지 않는다.
- 범위 밖: Spring Boot의 Java 실행, Maven build, React component rendering, 브라우저에서의 UI 실행은 Node.js 자체 기능으로 설명하지 않는다.

## 자주 헷갈리는 원인

- **Node.js와 npm:** Node.js는 JavaScript runtime이고 npm은 package manager다. npm 명령이 실행됐다는 사실을 Node.js가 package를 직접 관리한다고 합치지 않는다.
- **Node.js와 Vite:** Vite는 React project 생성·development server·build를 담당하는 별도 도구다. 수업에서 확인한 5173 화면은 Vite development server의 결과다.
- **Node.js와 React:** React component는 browser에서 UI를 rendering한다. 개발 도구가 Node.js 환경에서 실행된 것과 완성 UI가 Node.js에서 rendering된다는 말은 다르다.
- **개발 실행과 배포 build:** `npm run dev` 성공은 development server 확인이다. production build artifact 생성은 이 원본에서 확인되지 않는다.

## 관련 개념

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[entities/react|React]]
- [[entities/typescript|TypeScript]]
- [[entities/visual-studio-code|Visual Studio Code]]

## 학습 이력

- **2026-03-30:** 설치→npm version 확인→Vite React/TypeScript project 생성→package 설치→development server 실행까지 직접 확인했다.
- **2026-03-31:** VS Code에서 `react_cafe`를 열고 `node_modules`를 npm 설치 결과로 확인했다. 이후 날짜의 React/TypeScript 코드 작성은 이 환경 위에서 이어졌지만, 날짜마다 Node.js 자체 기능을 새로 학습한 것은 아니다.

## 과목 경계

- 직접 수업: 로컬 React 개발 도구 환경 준비와 실행 확인이다.
- 교안 보충: P06 `NodeJs.pdf`의 설치 내용은 03-30 날짜 MD에 필요한 절차가 전사되어 있어 별도 source로 추가하지 않았다.
- 후속 Linux/AWS/CI/CD: Maven·jar·Docker·EC2·GitHub Actions 배포는 별도 실행·배포 계층이다. 이 페이지는 해당 작업을 Node.js 기능으로 소급하지 않는다.
- Passwordless·중간 프로젝트: React client가 후속 인증·배포 기능을 가질 수 있지만, 그 기능 자체가 Node.js의 역할은 아니다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
