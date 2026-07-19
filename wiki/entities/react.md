---
title: React
created: 2026-07-02
updated: 2026-07-19
type: entity
tags: [react, typescript, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.03(금)/2026.04.03(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.08(수)/2026.04.08(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.15(수)/2026.04.15(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# React

## 정의

React는 화면을 component 단위로 구성하고 props와 state의 변화에 따라 필요한 UI를 다시 렌더링하는 JavaScript library다. 이 페이지는 문법 설명보다, 이 수업에서 React 화면이 Fruit에서 Product·Cart·Order·Paging/Search로 확장된 이력을 추적한다.

## 왜 중요한가

UI&UX 과목의 정적 HTML·JavaScript DOM 화면을 데이터 중심 component로 바꾸고, Spring Boot API 응답을 state에 넣어 같은 화면을 갱신할 수 있게 했다. 기능별 page를 만들면서 입력 control, 이벤트, loading/error, 목록 배열, 로그인 user와 page metadata가 하나의 UI runtime 안에서 어떻게 이어지는지 배웠다.

## 첫 등장과 주변 도구 구분

- [[summaries/2026-03-30-fullstack-environment-setup|03-30]]에 Vite에서 `TypeScript + React Compiler` variant로 React 프로젝트를 생성하고 개발 서버를 실행했다.
- 같은 날 설치한 React Router, axios, Bootstrap, React Bootstrap은 React 자체가 아니라 각각 화면 routing, HTTP client, CSS/UI component 도구다.
- 03-31에는 component·JSX/TSX·Router 화면 구조를 만들었지만, Spring API 응답이 화면까지 왕복한 것은 [[summaries/2026-04-01-react-router-spring-boot|04-01]]의 axios·state/effect·CORS 연결이다.

## 대표 artifact와 입력 → 처리 → 결과

| 구간 | 대표 React artifact | 입력 | React의 처리 | 결과 |
|---|---|---|---|---|
| Fruit | `AppRoutes`, `MenuItems`, `FruitOne`, `FruitList` | route 선택과 GET 응답 | component 선택, `useState`, `useEffect`, 목록 `map` | Fruit 한 개/목록 표 |
| Member/JWT | `SignupPage`, `LoginPage`, `App`, `MenuItems` | form event와 login 응답 | controlled state, token/user 분리, user state·메뉴 분기 | 가입 오류·로그인 상태·logout 이동 |
| Product | `ProductList`, `ProductInsertForm`, `ProductUpdateForm`, `ProductDetail` | 클릭, form, 파일, API 응답 | event/spread/FileReader, 목록·상세 state, route id | CRUD·상세 UI와 오류 표시 |
| Cart | `CartList` | user props, 품목 배열, checkbox·수량 | 선택·합계·재고 검사, PATCH/DELETE/POST handler | 사용자별 장바구니와 주문 요청 |
| Order | `OrderList` | 역할별 주문 배열과 버튼 | card 렌더링, 완료·취소 요청 뒤 재조회 | PENDING 목록과 상태 반영 |
| Paging/Search | `Paging`, `FieldSearch`, `ProductList` | page·기간·category·mode·keyword | dependency에 따른 재요청, `content`와 metadata 분리 | page card·상태·검색 parameter |

React의 state/event와 조회 시점 원리는 [[concepts/react-form-state-event|React 폼 상태와 이벤트]], [[concepts/react-useeffect-data-fetching|React useEffect와 데이터 요청]]에 위임한다.

## 실제 수업에서 확인된 완료 범위와 미확정 범위

### 확인된 구현

- Fruit 한 개/목록은 04-01에 CORS를 통과한 API 응답을 state에 넣어 렌더링했다.
- 회원가입·로그인, Product CRUD/상세, Cart 추가·목록·선택·수량·삭제, Order 목록·상태, page 왕복 화면을 날짜별로 확장했다.
- 04-21에는 검색 control·state·request parameter와 `Page`의 `content`·metadata 처리를 작성했다.

### 날짜를 합치면 안 되는 부분

- 03-31의 Router/component 구조만으로 API 왕복 완료를 주장하지 않는다.
- Cart·Order·Paging·검색 control은 먼저 표시된 뒤 handler와 backend 연결이 후속 교시나 다음 날짜에 완성됐다.
- 04-21 검색 화면과 parameter는 확인되지만, 04-22 backend 검색 코드의 runtime 성공은 별도 미확정이다.
- ADMIN/USER에 따라 버튼을 보이는 client UI는 사용성 분기이지 서버 endpoint authorization의 증거가 아니다.

## 자주 헷갈리는 원인

- **React vs React Router:** React는 component/state/rendering을, Router는 화면 path와 component 선택을 맡는다.
- **React vs axios:** axios가 HTTP 요청을 보내고 React는 그 응답을 state로 관리해 렌더링한다.
- **React vs Bootstrap:** Bootstrap/React Bootstrap은 화면 스타일·UI component를 제공하며 React의 상태 모델과 다르다.
- **React vs TypeScript:** React는 runtime UI library이고 TypeScript type은 compile-time 검사 도구다.
- **화면 path vs API URL:** Router 주소와 Spring API 주소는 모두 문자열 URL처럼 보이지만 실행 주체가 다르다. [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]에서 비교한다.

## 이전 개념과 이후 기능 연결

- 선행: [[entities/html|HTML]], [[entities/css|CSS]], [[entities/javascript|JavaScript]], [[concepts/javascript-dom|JavaScript와 DOM]]에서 정적 구조와 직접 DOM 변경을 배웠다.
- 과목 내부: Fruit의 작은 component/state 왕복이 Product·Cart·Order의 배열·form·role UI와 Paging/Search metadata로 확장됐다.
- 후속: Linux/AWS/CI/CD는 주로 Spring Boot 배포를 다뤘고, 중간 프로젝트에서 React UI를 실제 서비스 화면으로 확장한다. Passwordless는 별도 인증 기술이므로 이 과목의 JWT UI와 합치지 않는다.
- 단계 9 가이드는 환경별 API/proxy, frontend Dockerfile·workflow, multipart file UI와 Passwordless 선택·등록/해제·polling snippet을 제시한다. 독립 TypeScript/CSS source, build artifact, browser/network 결과가 없으므로 화면 통합 완료로 확정하지 않는다.

## 날짜별 학습 이력

- **03-30:** Vite React 프로젝트와 개발 서버, 주변 library 설치.
- **03-31~04-01:** component·JSX/TSX·Router→axios·state/effect·CORS 첫 왕복.
- **04-02~04-07:** HomePage/Carousel→회원가입·로그인 user/token state와 logout.
- **04-08~04-13:** Product 목록→삭제·등록→수정·상세.
- **04-14~04-17:** Cart 목록·선택·수량·주문 요청→OrderList 시작.
- **04-20~04-21:** 주문 상태 UI→대표 상품→Paging과 FieldSearch 화면·request parameter.

## 관련 페이지

- [[summaries/2026-04-03-frontend-backend-subject-review|FrontEnd_BackEnd 총정리]]
- [[concepts/react-typescript-basics|React와 TypeScript 기본]]
- [[concepts/product-domain-flow|상품 도메인 기능 흐름]]
- [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- [[concepts/order-flow|주문 기능 흐름]]
- [[concepts/pagination-search|페이징과 검색]]
- [[comparisons/props-vs-state|props vs state]]
- [[entities/typescript|TypeScript]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.30(월) - 시작/2026.03.30(월) - 시작.md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`부터 `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`까지 React 구현이 등장한 날짜 MD
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`