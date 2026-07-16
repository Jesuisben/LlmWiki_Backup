---
title: 2026-04-01 React axios와 Spring CORS 연결
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
status: growing
confidence: high
---

# 2026-04-01 React axios와 Spring CORS 연결

## 한 줄 요약

`MenuItems`와 Router로 선택한 `FruitOne`·`FruitList`가 `Fruit` type에 맞춰 axios로 Spring API를 호출하고, CORS 차단을 `WebConfig`에서 허용한 뒤 state에 저장해 표로 렌더링하는 첫 프론트↔백엔드 왕복을 완성했다.

## 왜 이 순서로 배웠는가

전날에는 React Router가 화면만 바꿨고 Spring JSON은 별도 URL에서만 확인했다. 이날은 프론트가 기대하는 데이터 모양을 선언하고 화면이 열릴 때 API를 호출해 state를 갱신했다. 실제 브라우저에서 CORS 오류가 난 뒤 Spring 허용 설정을 추가함으로써 서버 정책도 연결의 일부임을 확인했다.

## 교시 흐름

### 1. 메뉴·라우트 구조 정리와 `Fruit` type 선언

- `App.tsx`가 `MenuItems`, `AppRoutes`, footer를 조립하도록 정리하고 Navbar 메뉴를 과일 한 개·목록 화면에 연결했다.
- `types/Fruit.ts`에 `id: string`, `name: string`, `price: number`인 interface를 만들었다. 이는 Spring 응답을 React에서 어떤 shape로 다룰지 선언한 설계도다.

### 2. `FruitOne`의 요청과 state 갱신

- `FruitOne`은 초기값이 `null`인 `Fruit` state를 만들고, 첫 render 뒤 한 번 실행되는 `useEffect` 안에서 `${API_BASE_URL}/fruit`를 axios GET으로 요청했다.
- axios response의 `data`를 setter에 전달하고 optional chaining으로 아직 데이터가 없을 때의 접근 오류를 피하며 id·상품명·가격을 표시했다.
- HTTP method는 React가 임의로 정하는 것이 아니라 Spring Controller의 `@GetMapping`과 맞춰야 한다는 점을 확인했다.

### 3. 실제 CORS 실패와 `WebConfig` 해결

- React 5173에서 Spring 9000으로 요청하자 브라우저가 서로 다른 origin으로 판단해 `Access-Control-Allow-Origin`이 없다는 오류를 냈다.
- Spring의 `WebConfig`가 모든 path에 대해 5173·3000 origin, GET부터 PATCH까지의 method, credential 전송을 허용하도록 설정했다.
- 설정 뒤 같은 axios 요청이 통과해 React 화면에 Spring JSON 값이 표시됐다.

### 4. 목록 응답을 `map`으로 표시

- `FruitList`는 빈 배열인 `Fruit[]` state로 시작해 `${API_BASE_URL}/fruit/list`를 요청했다.
- JSON array를 state에 넣고 JSX의 `map`으로 각 Fruit를 table row로 만들었다. 각 row에는 `key={fruit.id}`를 지정했다.

### 5. 이미지 경로·props로 다음 화면 준비

- `WebConfig`에 `/images/**` 요청을 로컬 업로드 경로로 연결하는 resource handler를 추가해 다음 날 HomePage 이미지 제공을 준비했다.
- `App.tsx`의 `appName`을 `MenuItems`에 props로 전달하고 자식은 매개변수와 `MenuItemsProps` type을 선언했다.
- 수업은 props를 부모가 자식에게 주는 값, `Fruit` interface를 서버 데이터 model의 shape로 설명했다.

## 대표 artifact와 입력 → 처리 → 결과

| 구간 | 대표 artifact | 입력 | 처리 | 결과 |
|---|---|---|---|---|
| 한 개 조회 | `Fruit.ts`, `FruitOne.tsx` | `/fruit` GET | 응답 `data`를 `Fruit | null` state에 저장 | 한 개의 과일 표 표시 |
| CORS 허용 | `WebConfig` | 5173 origin의 API 요청 | origin·method·credential 허용 규칙 적용 | 브라우저 차단 해소 |
| 목록 조회 | `FruitList.tsx` | `/fruit/list` GET | JSON array를 `Fruit[]` state에 저장하고 `map` 순회 | 여러 과일 행 표시 |
| 자식 구성 | `App.tsx`, `MenuItems.tsx` | 부모의 `appName` | typed props로 자식에 전달 | Navbar brand에 사이트명 표시 |

## 실제 혼동 원인

- `response`는 JSON 파일명이 아니라 status·header·data 등을 포함한 axios 응답 객체이며 실제 Spring 반환 데이터는 `response.data`에 있다.
- `useEffect`는 “백엔드 전용 함수”가 아니라 render 이후 side effect를 실행하는 Hook이다. 이날 빈 dependency array로 첫 화면 진입 시 한 번 조회했다.
- 비동기 요청은 결과를 무시한다는 뜻이 아니다. `await`로 해당 async 함수 안에서 응답을 기다린 뒤 state를 갱신했다.
- Router path는 React 컴포넌트를 고르고 axios URL은 9000번 Spring Controller에 데이터를 요청한다.
- CORS는 파일 경로 문제가 아니라 브라우저의 same-origin policy에 따른 네트워크 허용 문제다.

## 이전·다음 연결과 범위 경계

- 이전: [[summaries/2026-03-31-spring-boot-controller-html|03-31]]의 REST JSON과 Router 자리표시 화면을 실제 axios 요청으로 연결했다.
- 다음: [[summaries/2026-04-02-react-bootstrap-homepage|04-02]]에는 `/images/**` 응답을 React Bootstrap Carousel에 사용하고 오후에는 Member JPA/MySQL/Spring Security로 이동한다.
- 직접 수업: Fruit type, state/effect, axios GET, CORS, 한 개·목록 렌더링, resource handler와 props 입문이다.
- 후속 확장: Member/JWT 인증, Product/Cart/Order, Linux·AWS 운영은 이날 완성한 기능이 아니다.

## 관련 페이지

- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]
- [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]
- [[comparisons/props-vs-state|props vs state]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
