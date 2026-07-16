---
title: 2026-03-30 FrontEnd/BackEnd 개발 환경과 Fruit 시작
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
status: growing
confidence: high
---

# 2026-03-30 FrontEnd/BackEnd 개발 환경과 Fruit 시작

## 한 줄 요약

MySQL·Node.js·VS Code와 Spring Boot 프로젝트를 준비하고, 정적 홈페이지와 Vite React를 각각 실행한 뒤 Spring의 MySQL 설정과 `Fruit` 클래스로 다음 날 요청·응답 실습의 기반을 만들었다.

## 왜 이 순서로 배웠는가

[[summaries/2026-03-27-uiux-subject-review|UI&UX 수업]]까지는 브라우저 화면 자체가 중심이었다. 이날은 화면을 만드는 React, 요청을 처리하는 Spring Boot, 데이터를 저장할 MySQL을 별도 프로그램과 포트로 먼저 실행해 보면서 풀스택 개발의 세 실행 영역을 분리했다. 그 뒤 공통 설정과 데이터 모양을 준비해야 다음 날 Controller가 실제 요청에 응답할 수 있었다.

## 교시 흐름

### 1. 도구의 역할 확인과 설치

- IntelliJ 동작을 확인하고 MySQL Server·Workbench, Node.js, Visual Studio Code를 설치했다.
- Node.js 설치는 `npm -version`으로 확인했다. 이 수업에서 Node.js의 직접 역할은 React/Vite 개발 도구를 실행하는 것이며 Spring Boot 백엔드를 실행하는 것이 아니다.
- MySQL은 3306, Spring Boot는 9000, React 개발 서버는 이후 Vite가 제시한 5173을 사용했다. 같은 `localhost`라도 포트가 다르면 서로 다른 프로그램으로 들어간다는 점을 Protocol·IP·Port 설명과 연결했다.

### 2. Spring Boot 초기 프로젝트와 첫 정적 응답

- Spring Initializr에서 Maven·Java 21·Jar·Properties를 선택하고 DevTools, Lombok, Spring Data JPA, MySQL Driver, Thymeleaf, Spring Web 등의 의존성을 포함한 `spring_cafe` 초기 파일을 만들었다.
- IntelliJ에서 JDK 21을 맞추고 `CoffeeApplication`과 `resources/templates`, `resources/static`의 위치를 확인했다.
- 서버 포트를 9000으로 지정하고 `static/index.html`을 만든 뒤 `CoffeeApplication`을 실행했다. 브라우저의 `localhost:9000` 요청에 Spring Boot가 정적 홈 페이지를 반환하는 결과를 확인했다.
- 포트를 80으로 바꾸면 주소에서 포트 표기를 생략할 수 있다는 실험으로 기본 포트와 명시 포트의 차이를 확인했다.

### 3. Vite React 프로젝트 생성과 실행 루틴

- `npm create vite@latest`로 `react_cafe`를 만들고 React의 `TypeScript + React Compiler` 변형을 선택했다.
- 프로젝트 폴더에서 `npm install`, `npm run dev`를 실행하고 Vite가 안내한 `localhost:5173`에서 초기 화면을 확인했다.
- axios, React Router DOM, Bootstrap, React Bootstrap을 설치하고 `npm list`로 모듈을 확인했다. 이후 반복 루틴은 `react_cafe`로 이동해 `npm run dev`를 실행하는 것이다.

### 4. MySQL·Spring 공통 설정

- MySQL Workbench에서 `coffee` 데이터베이스용 샘플 SQL을 실행했다.
- `pom.xml`은 Maven 의존성 설정, `application.properties`는 Spring 전반 설정이라는 역할을 구분했다.
- Spring 설정에 MySQL 3306의 `coffee` DB URL, 사용자, 수업용 비밀번호, MySQL dialect를 지정했다.
- DevTools restart/livereload와 IntelliJ 자동 빌드 옵션을 확인하고 Lombok 플러그인과 annotation processing을 활성화했다.

### 5. 다음 날 응답 데이터가 될 `Fruit`

- `Fruit.java`를 만들고 `id`, `name`, `price`, 기본 생성자와 전체 필드 생성자를 정의했다.
- Lombok의 `@Getter`, `@Setter`, `@ToString`으로 반복 메서드 생성을 맡겼다. 이 단계의 `Fruit`는 아직 JPA DB Entity가 아니라 과일 한 개를 표현하는 일반 Java 클래스다.

## 대표 artifact와 입력 → 처리 → 결과

| 구간 | 대표 artifact | 입력 | 처리 | 결과 |
|---|---|---|---|---|
| Spring 첫 실행 | `application.properties`, `static/index.html`, `CoffeeApplication` | 브라우저의 9000번 요청 | 지정 포트에서 정적 리소스를 찾음 | 홈 페이지 표시 |
| React 첫 실행 | `react_cafe`, Vite 개발 서버 | `npm run dev` | Node.js 환경에서 Vite가 개발 서버 실행 | 5173번 초기 화면 표시 |
| DB 준비 | MySQL Workbench, datasource 설정 | `coffee` DB와 접속 설정 | DB 위치·사용자·dialect 지정 | 후속 JPA 연동 준비 |
| 데이터 모양 | `Fruit.java` | 과일 id·이름·가격 | 생성자와 Lombok 접근 메서드로 객체 구성 | 03-31 Controller 응답 데이터 준비 |

## 실제 혼동 원인

- 원본의 “Node.js가 build해주는 프로그램”이라는 메모는 역할을 잡는 과정이었다. 이 수업에서 Node.js는 React/Vite 도구의 실행환경이고, Vite 개발 서버 실행과 배포용 build는 같은 말이 아니다.
- Spring Boot 정적 HTML과 React 화면은 각각 9000과 5173에서 독립 실행됐다. 이날 두 화면을 API로 연결하지는 않았다.
- `Fruit`라는 이름 때문에 JPA Entity로 오해하기 쉽지만 이날 코드에는 JPA 매핑 annotation이 없다. Member JPA 매핑은 [[summaries/2026-04-02-react-bootstrap-homepage|04-02]]에 시작한다.

## 이전·다음 연결과 범위 경계

- 이전: [[summaries/2026-03-27-uiux-subject-review|UI&UX 총정리]]의 화면 제작에서 서버·DB가 포함된 구조로 전환했다.
- 다음: [[summaries/2026-03-31-spring-boot-controller-html|03-31]]에는 `FruitHtmlController`가 `Fruit`를 Thymeleaf HTML에 전달하고, 이어 `FruitController`가 JSON으로 반환하며 React Router 화면을 준비한다.
- 직접 수업: 로컬 개발환경, Spring·React 각각의 첫 실행, MySQL 접속 설정, `Fruit` 작성까지다.
- 후속 확장: Member/JWT, Product/Cart/Order, Linux 서버 실행, AWS 배포와 CI/CD는 이후 수업 범위다.

## 관련 페이지

- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/react|React]]
- [[entities/mysql|MySQL]]
- [[entities/node-js|Node.js]]
- [[entities/visual-studio-code|Visual Studio Code]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
