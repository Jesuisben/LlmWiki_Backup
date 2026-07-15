---
title: 2026-03-31 Spring HTML 응답에서 REST/React Router로 전환
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
status: growing
confidence: high
---

# 2026-03-31 Spring HTML 응답에서 REST/React Router로 전환

## 한 줄 요약

`FruitHtmlController`와 Thymeleaf template으로 서버가 완성 HTML을 만드는 흐름을 먼저 실습하고, 같은 `Fruit` 데이터를 `FruitController`의 JSON으로 바꾼 뒤 React 컴포넌트·메뉴·Router가 화면을 선택하는 구조로 전환했다.

## 왜 이 순서로 배웠는가

전날 만든 `Fruit`가 요청에 어떻게 쓰이는지 확인하려면 Spring 안에서 Controller→Model→template의 왕복을 먼저 완성하는 편이 단순하다. View 생성을 React에 맡기려면 Spring이 HTML 대신 데이터만 반환해야 하므로 REST/JSON으로 바꿨다. 마지막으로 React에서 URL에 맞는 화면을 고르는 Router를 붙여 다음 날 JSON 요청을 연결할 자리까지 만들었다.

## 교시 흐름

### 1. `FruitHtmlController`로 과일 한 개 전달

- `@Controller`와 `@GetMapping`으로 `/fruit01` GET 요청을 받는 `FruitHtmlController`를 만들었다.
- 메서드에서 바나나 `Fruit`를 만들고 Model에 `fruit`라는 속성명으로 넣은 뒤 `fruit` view 이름을 반환했다.
- 지역변수 `bean`을 template에서 바로 볼 수 없기 때문에 Model이라는 전달 저장소와 속성명이 필요하다는 점을 “캐비닛과 물품 식별자”로 설명했다.

### 2. Thymeleaf template으로 한 개·목록 HTML 생성

- `resources/templates/fruit.html`에 Thymeleaf namespace와 `th:text`를 사용해 id·name·price를 표시했다.
- `List<Fruit>`에 사과·배·포도를 담아 `fruitList` 속성으로 Model에 전달했다.
- `fruitList.html`은 `th:each`로 목록을 순회해 표 행을 만들었다. 전체 왕복은 클라이언트 요청→Controller→Model→template→완성 HTML 응답이다.

### 3. HTML 응답에서 REST/JSON 응답으로 전환

- `@RestController`인 `FruitController`를 만들고 `/fruit`에서 과일 한 개, `/fruit/list`에서 목록을 직접 반환했다.
- 브라우저에서 두 URL을 열어 각각 JSON object와 JSON array가 나오는 것을 확인했다.
- template 이름을 반환하던 방식과 달리 반환 객체가 JSON 표현으로 바뀌며, 이 데이터는 React 화면의 재료가 된다.

### 4. React 공통 구성과 컴포넌트 조립

- `config.tsx`에 Spring Boot host와 9000 포트를 조합한 `API_BASE_URL`을 두었다.
- `main.tsx`에서 `BrowserRouter`로 `App`을 감싸고 Bootstrap CSS를 공통 import했다.
- `App.tsx`가 `MenuItems`를 포함하도록 구성하며 화면의 각 부분을 파일로 나누고 조립·재사용하는 방식을 배웠다.

### 5. 메뉴와 React Router 화면 연결

- React Bootstrap Navbar에 `useNavigate`를 붙여 “과일 1개”와 “과일 목록” 메뉴가 각각 `/fruit`, `/fruit/list`로 이동하게 했다.
- `FruitOne.tsx`, `FruitList.tsx`는 이날 우선 자리표시 화면으로 만들었다.
- `AppRoutes.tsx`가 두 path를 두 컴포넌트에 연결했다. 메뉴 클릭→주소 변경→Routes의 path 비교→해당 컴포넌트 표시를 확인했다.

## 대표 artifact와 입력 → 처리 → 결과

| 구간 | 대표 artifact | 입력 | 처리 | 결과 |
|---|---|---|---|---|
| 서버 HTML | `FruitHtmlController`, `fruit.html`, `fruitList.html` | `/fruit01` 계열 GET | Fruit 객체/List를 Model에 저장하고 Thymeleaf가 HTML 생성 | 데이터가 채워진 HTML 화면 |
| REST 데이터 | `FruitController` | `/fruit` 계열 GET | Java 객체/List를 응답 본문으로 반환 | JSON object/array |
| React 화면 선택 | `MenuItems`, `AppRoutes`, `FruitOne`, `FruitList` | Navbar 메뉴 클릭 | `navigate`가 URL을 바꾸고 Routes가 element 선택 | 한 개 또는 목록 컴포넌트 |

## 실제 혼동 원인

- `return "fruit"`는 문자열 본문이 아니라 `@Controller` 문맥에서 `fruit.html` view를 선택하는 이름이다. `@RestController`에서 `Fruit`를 반환하면 JSON 데이터가 된다.
- Spring API `/fruit`와 React Router `/fruit`는 같아 보여도 실행 서버와 역할이 다르다. 이날 React 화면은 아직 API를 호출하지 않았고 연결은 [[summaries/2026-04-01-react-router-spring-boot|04-01]]에 수행한다.
- 수업의 라우터 그림은 관객을 알맞은 상영관으로 안내하듯 URL을 알맞은 화면으로 연결하는 비유다. 네트워크 장비 구현을 한 것은 아니다.

## 이전·다음 연결과 범위 경계

- 이전: [[summaries/2026-03-30-fullstack-environment-setup|03-30]]의 `Fruit`와 Spring/React 실행환경을 실제 응답과 화면 구조에 사용했다.
- 다음: [[summaries/2026-04-01-react-router-spring-boot|04-01]]에는 `Fruit` TypeScript interface, axios, state/effect, CORS와 `WebConfig`로 React가 Spring JSON을 실제로 받아 표시한다.
- 직접 수업: Thymeleaf HTML 응답, REST/JSON 응답, React 컴포넌트와 Router 초기 연결이다.
- 후속 확장: Member/JWT, Product/Cart/Order, Linux·AWS 배포는 이날 구현하지 않았다.

## 관련 페이지

- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/react|React]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
