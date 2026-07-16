---
title: Visual Studio Code
created: 2026-07-01
updated: 2026-07-16
type: entity
tags: [frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
status: growing
confidence: high
---

# Visual Studio Code

## 무엇인가

Visual Studio Code(VS Code)는 source folder와 text file을 열어 편집하는 code editor다. 이 과목에서는 `react_cafe`를 열고 React/TypeScript의 component·type·route·설정 파일을 작성한 frontend 작업 공간이었다.

## 왜 중요한가

03-30에 Spring Boot backend와 Vite React frontend를 별도 project로 만든 뒤, 03-31부터 React 쪽 파일을 지속적으로 찾아 만들고 수정할 editor가 필요했다. VS Code는 그 편집·탐색 환경을 제공했지만 npm package 설치, Vite server 실행, React rendering은 각각 npm·Vite·React가 수행했다.

## 이 위키에서의 맥락

[[summaries/2026-03-30-fullstack-environment-setup|2026-03-30]]에 설치했고, [[summaries/2026-03-31-spring-boot-controller-html|03-31]]에 `react_cafe` folder를 처음 열어 `src/config/config.tsx`, component, route와 page file을 작성하기 시작했다. [[summaries/2026-04-01-react-router-spring-boot|04-01]]에는 `Fruit.ts`와 Fruit 화면·Router를 편집하고 tree indent를 24로 조정했다. 04-02 HomePage와 04-03 SignupPage로 frontend artifact가 확장됐다.

## 대표 artifact와 입력 → 처리 → 결과

| 날짜 | 대표 artifact | 입력 | editor에서 한 작업 | 결과 |
|---|---|---|---|---|
| 03-30 | VS Code 설치 | 설치 프로그램 | editor 설치 | 실제 project open·build 성공과는 별도 |
| 03-31 | `react_cafe`, `config.tsx`, `MenuItems.tsx`, `AppRoutes.tsx` | Vite가 만든 project folder | folder open, 파일·폴더 생성과 React/TypeScript 편집 | Router 자리표시 화면과 frontend 구조 작성 |
| 04-01 | `Fruit.ts`, `FruitOne.tsx`, `FruitList.tsx` | Spring JSON shape와 API URL | interface·component·axios 요청 코드 편집 | 실제 요청·CORS 해결 뒤 Fruit 화면 표시 |
| 04-02~03 | `HomePage.tsx`, `SignupPage.tsx` | 이미지 URL과 회원 입력 항목 | Carousel·form·event·오류 표시 코드 편집 | HomePage와 회원가입 frontend 확장 |

## 확인된 범위와 미확정 범위

- 확인됨: 설치, project folder open, `src` 아래 folder/file 생성, React/TypeScript 코드 편집, F2 rename, `Ctrl + Space`, `Ctrl + ,`, tree indent 24, 한 줄 복사와 JSX 주석 단축키 사용.
- 확인됨: 04-01 Fruit 화면과 04-02 HomePage의 실행 결과는 VS Code에서 작성한 코드가 npm/Vite·browser·Spring과 함께 동작한 결과다.
- 미확정: P09에 있을 수 있는 날짜 MD 미전사 extension·plugin·설정은 직접 사용 근거로 추가하지 않았다.
- 구분: project를 editor로 열었다는 사실과 npm install, Vite development server, React rendering, API 성공을 같은 editor 기능으로 합치지 않는다.

## 자주 헷갈리는 원인

- VS Code는 editor이고 [[entities/node-js|Node.js]]는 runtime이다.
- npm이 package를 설치하고 Vite가 development server를 실행하며 React가 browser UI를 rendering한다. VS Code가 이 기능들을 대신 수행한 것이 아니다.
- `Fruit.ts`의 type 검사와 React component 동작은 [[entities/typescript|TypeScript]]·[[entities/react|React]] 책임이다. VS Code의 자동 완성·편집 보조와 언어 자체의 규칙을 구분한다.
- 03-30 설치와 03-31 project open, 04-01 API 화면 동작은 서로 다른 확인 시점이다.

## 관련 개념

- [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]
- [[entities/node-js|Node.js]]
- [[entities/react|React]]
- [[entities/typescript|TypeScript]]

## 학습 이력

- **2026-03-30:** 설치만 확인했다.
- **2026-03-31:** `react_cafe`를 열고 frontend folder 구조·config·component·Router 파일을 작성했다.
- **2026-04-01:** Fruit type·한 개/목록 component와 설정을 편집하고 frontend-backend 첫 왕복을 완성했다.
- **2026-04-02:** HomePage Carousel을 작성하고 backend 작업은 IntelliJ로 전환했다.
- **2026-04-03:** SignupPage event·Validation 오류 표시를 작성했다. 이후에도 frontend 편집기는 계속 사용됐지만 이 페이지는 R01~R05 중심의 확인 가능한 도구 이력만 source로 선언한다.

## 과목 경계

- 직접 수업: local React/TypeScript project의 편집·파일 탐색·일부 editor 설정이다.
- 교안 보충: P09 `VisualStudioCode.pdf`의 설치 내용은 03-30 날짜 MD에, 실제 project 작업은 03-31~04-03 날짜 MD에 충분히 전사되어 있어 PDF를 별도 source로 추가하지 않았다.
- 후속 Linux/AWS/CI/CD: server shell, build, container, cloud deployment와 workflow 실행은 editor 자체 기능이 아니다.
- Passwordless·중간 프로젝트: 후속 frontend code도 editor에서 작성할 수 있지만 인증·배포 기능의 구현 주체는 해당 library·application·service다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md`
