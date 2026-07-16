---
title: React Router 주소 vs Spring API 주소
created: 2026-07-02
updated: 2026-07-16
type: comparison
tags: [react, spring-boot, frontend, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png
status: growing
confidence: high
---

# React Router 주소 vs Spring API 주소

## 비교 목적

수업에서는 `/fruit`, `/fruit/list`, `/cart/list`, `/product/list`처럼 같은 문자열이 browser 화면 경로와 Spring API 경로 양쪽에 쓰였다. 문자열만 보면 같은 route처럼 보이지만, **요청을 처리하는 runtime·port·요청 주체·결과**가 다르다.

이 페이지는 path의 소유자를 판별하는 기준만 다룬다. 전체 HTTP 왕복은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], method·입력·status/body는 [[concepts/spring-boot-rest-api|Spring Boot REST API]]에 맡긴다.

## 실제 수업에서 비교가 필요해진 이력

- **2026-03-31:** React `navigate`/`Route`의 `/fruit`·`/fruit/list`와 Spring `@GetMapping`의 같은 문자열이 함께 등장해 첫 구분이 필요해졌다. 다만 이날 React component는 자리표시 화면이고 API 호출은 아직 연결되지 않았다.
- **2026-04-01:** React component가 `API_BASE_URL`을 붙여 Spring에 axios 요청을 보내고, 5173 origin에서 9000 API를 호출하며 CORS 오류가 발생해 두 실행 위치가 실제 왕복으로 드러났다.
- **2026-04-06~07:** `/member/login` 화면 path와 login API가 같은 문자열로 등장했고, CORS 설정도 MVC `WebConfig`에서 Security의 `CorsConfig` 연결로 이동했다. 화면 route, API, CORS, JWT 인증은 각각 다른 책임이다.
- **2026-04-14~15:** `/cart/list`가 Router의 CartList 화면 path이면서 axios와 `CartController`의 목록 API path로도 사용됐다.
- **2026-04-21~22:** ProductList 화면은 `/product/list`에 머무르면서 page·size·검색 조건을 Spring `/product/list` 요청 parameter로 보내고 `Page<Product>`를 받는 구조로 확장됐다.

## 한눈에 보기

| 판단 항목 | React Router path | Spring API URL |
|---|---|---|
| 실행 주체 | browser의 React Router | Spring Boot web server·Controller |
| 수업 개발 port | React/Vite 5173 | Spring Boot 9000 |
| 시작 원인 | 주소 이동, `navigate`, `Link`, browser history | axios HTTP 요청, browser 직접 요청, form/API 호출 |
| 매칭 artifact | `Routes`, `Route`, 화면 component | `@RequestMapping`, `@GetMapping` 등 Controller mapping |
| 직접 결과 | 어떤 React component를 render할지 선택 | JSON/message/status/image 같은 HTTP 응답 |
| DB 접근 | path 선택 자체는 DB에 접근하지 않음 | Service·Repository 호출이 연결된 API일 수 있음 |
| 같은 문자열 가능성 | 가능 | 가능하지만 같은 route가 되지는 않음 |

## 실제 선택 상황 1 — Fruit

### 입력 → 처리 → 결과

| 단계 | 확인된 동작 |
|---|---|
| browser 화면 선택 | React Router의 `/fruit`는 `FruitOne`, `/fruit/list`는 `FruitList` component를 선택한다. |
| component의 데이터 요청 | 04-01부터 선택된 component가 `API_BASE_URL`에 `/fruit` 또는 `/fruit/list`를 붙여 axios 요청을 보낸다. |
| Spring 처리 | `FruitController`의 대응 `@GetMapping`이 요청을 받고 데이터를 반환한다. |
| 결과 | axios가 JSON을 받고 state setter 뒤 React가 화면을 다시 그린다. |

주소창의 browser path와 axios가 호출한 API path가 우연히 같아도, 전자는 5173의 React 앱 안에서 화면을 고르고 후자는 9000의 Spring 서버에 데이터를 요구한다.

## 실제 선택 상황 2 — Cart의 같은 `/cart/list`

- `Route path='/cart/list'`는 `CartList user={user}` component를 선택한다.
- CartList 내부 `${API_BASE_URL}/cart/list` 요청은 Spring `@RequestMapping("/cart")`와 `@GetMapping("/list")`에 도달한다.
- Controller는 인증 email로 회원을 찾고 Service가 만든 `CartItemDto` 목록을 반환한다.
- React는 받은 JSON을 Cart state에 넣어 table을 render한다.

화면 component 선택과 Cart 목록 조회는 함께 사용되지만 서로 대체되지 않는다. Router가 Service를 호출하거나 DB를 읽는 것이 아니며, API 응답이 자동으로 화면 component를 선택하는 것도 아니다.

## 실제 선택 상황 3 — Product paging/search

ProductList 화면 path가 바뀌지 않아도 page·size·검색 조건이 달라질 때 axios 요청 parameter는 바뀔 수 있다. 04-21에는 frontend state와 parameter·단순 Page 왕복 및 검색 준비가, 04-22에는 Controller의 `SearchDto` 구성과 Service·Repository 호출 코드가 이어졌다.

따라서 browser path의 “현재 화면”과 API query의 “현재 검색 조건”을 하나의 route state로 합치지 않는다. 04-22는 Repository 호출 코드와 MySQL 검색 시나리오는 확인되지만 실제 Specification API 성공 응답은 미확정이다.

## CORS는 두 URL의 정의가 아니다

04-01에는 `http://localhost:5173`에서 `http://localhost:9000/fruit`를 요청해 port가 다른 origin 간 browser 정책인 CORS 오류가 발생했다. `WebConfig`가 허용 origin·method를 설정한 뒤 요청이 가능해졌다.

04-07에는 기존 MVC CORS 설정을 주석 처리하고 `CorsConfig` bean을 `SecurityConfig.cors(...)`에 연결하는 코드로 이동했다. 이는 CORS 설정 위치의 확장이지 React Router path와 Spring API URL이 하나가 됐다는 뜻이 아니다.

- CORS는 React Router path를 Spring API path로 바꾸는 기능이 아니다.
- CORS는 두 path 문자열이 같은지 판단하는 규칙도 아니다.
- browser가 다른 origin의 API 응답을 읽도록 허용할지 제어하는 정책이다.

## 함께 사용하는 관계와 I03 그림

I03은 `Audience`를 `Router`가 ticket에 맞는 `Theater 1~3`으로 안내하는 그림이다. 이는 URL에 맞는 화면 component를 선택하는 React Router의 비유까지만 뒷받침한다. 그림에는 Spring server·Controller·API·DB가 없으므로 API URL의 처리 근거로 확대하지 않는다.

일반적인 함께 사용 순서는 `browser path → Router가 component 선택 → component가 API URL 호출 → Spring 응답 → state 갱신 → component render`다.

## 확인된 구현 범위와 실행 미확정 범위

- 확인: Fruit·Cart·Product에서 Router path와 Spring mapping/axios URL이 별도 artifact로 작성됨.
- 확인: React 5173과 Spring 9000 사이 CORS 오류 및 Spring CORS 설정.
- 확인: 04-07 CORS 설정을 Spring Security chain에 연결하는 코드.
- 확인: `/cart/list`·`/product/list`처럼 문자열이 같은 화면/API 쌍.
- 미확정: production 배포에서 같은 domain·port·proxy가 사용됐다는 주장. 이는 후속 Linux/AWS/CI/CD 범위다.
- 미확정: 04-22 검색 API runtime 성공과 확정 결과 건수.

## 자주 헷갈리는 원인과 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| 문자열이 같으면 같은 route다 | 어느 runtime과 port가 path를 해석하는지 본다. |
| Router가 API 데이터를 가져온다 | Router는 component를 선택하고 axios가 HTTP 요청을 보낸다. |
| Spring API가 React 화면을 직접 바꾼다 | API는 응답을 주고 React state/rendering이 화면을 갱신한다. |
| CORS가 route 연결 기능이다 | 다른 origin 간 browser 요청 허용 정책이다. |
| browser path가 같으면 검색 조건도 같다 | API query parameter와 frontend state를 별도로 추적한다. |

## 선행 개념과 후속 기능 경계

- 선행: [[concepts/react-typescript-basics|React와 TypeScript 기본]], [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- 전체 경계: [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[concepts/fullstack-project-flow|풀스택 프로젝트 흐름]]
- 기능 연결: [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/pagination-search|페이징과 검색]]
- 날짜 Summary: [[summaries/2026-03-31-spring-boot-controller-html|03-31 Fruit HTML→REST/Router]], [[summaries/2026-04-01-react-router-spring-boot|04-01 axios·CORS]], [[summaries/2026-04-14-cart-service|04-14 Cart]], [[summaries/2026-04-21-product-pagination-search-react|04-21 Paging/Search]]
- Linux/AWS/CI/CD의 reverse proxy·domain·배포 URL은 후속 운영 topology다. Passwordless·중간 프로젝트의 인증 endpoint도 이 페이지의 직접 구현 범위가 아니다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.22(수)/2026.04.22(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/교육 자료/라우터 설명 그림.png`
