---
title: MPA vs SPA
created: 2026-07-02
updated: 2026-07-16
type: comparison
tags: [frontend, react, spring-boot, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md
status: growing
confidence: high
---

# MPA vs SPA

## 비교 목적

MPA/SPA는 **화면을 누가 만들고 페이지 전환 때 무엇을 다시 받는가**를 비교하는 rendering architecture 축이다. Session/JWT는 인증 상태를 어디에 두고 어떻게 전달하는가를 비교하는 다른 축이다. 수업에서 SPA와 JWT가 같은 날 연결됐어도 `MPA=Session`, `SPA=JWT`로 고정하면 안 된다.

## 실제 수업에서 비교가 필요해진 이력

- **2026-03-31:** `FruitHtmlController`가 Model과 Thymeleaf template으로 완성 HTML을 반환하던 흐름을 `FruitController`의 REST JSON과 React Router 화면으로 바꾸면서 두 rendering 흐름의 실제 비교가 처음 필요해졌다.
- **2026-04-01:** React component가 axios로 JSON을 받고 state를 갱신하는 흐름과 다른 origin CORS 경계가 연결됐다.
- **2026-04-06:** 교안의 MPA/SPA 비교가 명시적으로 정리됐고, 같은 날 JWT 이론·구성 준비가 이어졌다.
- **2026-04-21:** CSR은 browser에서 화면 생성, SSR은 server에서 화면 생성이라는 용어 보충이 추가됐다. 이는 03-31의 실제 HTML/React 전환을 다시 분류하는 보조 축이다.

## 한눈에 보기

| 판단 항목 | MPA 중심 흐름 | SPA 중심 흐름 |
|---|---|---|
| 화면 생성 책임 | server가 요청마다 완성 HTML view를 반환 | 처음 받은 app shell 뒤 browser JavaScript가 component를 바꿈 |
| 화면 이동 결과 | 새 document/HTML 응답 중심 | React Router와 state에 따른 component rendering 중심 |
| server 응답 | HTML view와 필요한 model | API JSON·message·status 등 데이터 응답 비중이 큼 |
| 수업 artifact | `FruitHtmlController`, Model, Thymeleaf template | React `Routes`, `FruitOne`/`FruitList`, axios, REST `FruitController` |
| server 필요 여부 | 필요 | API·인증·DB를 위해 여전히 필요 |
| 인증 방식 | Session·JWT 모두 설계 가능 | Session·JWT 모두 설계 가능 |

## 실제 선택 상황 1 — 03-31 Fruit HTML 흐름

### 입력 → 처리 → 결과

1. browser가 Spring 9000의 `/fruit01` 또는 `/fruit01/list`를 요청한다.
2. `FruitHtmlController`가 Fruit 데이터를 Model에 담는다.
3. Thymeleaf template이 server에서 HTML로 완성된다.
4. browser가 완성된 HTML document를 받아 표시한다.

이 흐름에서는 Spring이 data뿐 아니라 view 선택과 HTML 생성까지 맡는다. 수업의 실제 artifact는 JSP가 아니라 Thymeleaf였으므로 대표 수업 예를 임의로 JSP로 바꾸지 않는다.

다만 이 artifact는 MPA 쪽의 **server-rendered HTML 응답 패턴**을 확인하는 근거다. 03-31 실습 전체가 완성된 MPA 애플리케이션이었다고 범위를 확대하지 않는다.

## 실제 선택 상황 2 — REST/React 전환

1. React Router가 `/fruit` 또는 `/fruit/list`에 맞는 component를 선택한다.
2. component가 Spring API에 axios 요청을 보낸다.
3. REST `FruitController`가 Fruit object/목록을 반환하고 HTTP에서는 JSON이 된다.
4. React가 JSON을 state에 넣고 필요한 component 부분을 render한다.

03-31에 구조가 시작됐고 04-01에 axios·state·CORS를 연결해 실제 browser↔API 왕복을 확장했다. SPA는 server가 없다는 뜻이 아니라 server의 중심 응답이 완성 HTML에서 API data로 바뀐 구조다.

## 실제 선택 상황 3 — 쇼핑몰 기능 확장

- Member/Product/Cart/Order/Page 화면은 React component와 Router에서 전환된다.
- 데이터 저장·조회·인증은 Spring API와 MySQL이 담당한다.
- page/search state 변경은 새 HTML document 전체를 받는 대신 API를 다시 호출하고 component를 갱신하는 방식으로 이어졌다.

04-21의 CSR/SSR 용어는 이 구조를 이해하는 데 보조가 되지만, MPA와 SSR·SPA와 CSR을 모든 경우에 완전히 같은 단어로 고정하지 않는다. 이 Vault의 직접 근거는 수업에서 구현한 Thymeleaf HTML 흐름과 React API 흐름이다.

## 함께 사용하는 관계

- server가 route마다 완성 HTML을 만들고 document 단위로 응답하는 기능은 MPA/server-rendered 흐름으로 추적한다.
- React가 화면 shell을 유지하고 Router·state로 component를 바꾸며 JSON API를 쓰는 기능은 SPA 흐름으로 추적한다.
- 한 서비스가 일부 server-rendered 페이지와 별도 SPA 화면/API를 함께 가질 수도 있다. 수업도 Fruit의 두 흐름을 비교하기 위해 같은 Spring project 안에서 전환했다.
- rendering architecture를 정한 뒤 인증 방식은 별도로 Session/JWT/Cookie 조합을 선택한다.

## 자주 헷갈리는 원인과 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| MPA는 Session만 쓴다 | HTML rendering 방식과 server-side 인증 상태는 다른 설계 축이다. |
| SPA는 JWT만 쓴다 | SPA도 cookie·Session을 사용할 수 있고 JWT도 다른 client 구조에서 쓸 수 있다. |
| JWT를 쓰면 SPA가 된다 | token 형식이 화면 rendering 책임을 바꾸지 않는다. |
| React Router 이동은 server page 이동이다 | browser app 안의 component 선택이며 API 호출과도 별개다. |
| SPA는 새로고침이 전혀 없다 | 일반 navigation과 app 내부 전환을 구분하고 수업 근거 이상으로 일반화하지 않는다. |

## 확인된 구현 범위와 실행 미확정 범위

- 확인: 03-31 Thymeleaf HTML 응답과 REST JSON Controller, React Router 자리표시 화면의 구조 전환.
- 확인: 04-01 React axios·state·CORS 연결.
- 확인: 04-06 MPA/SPA 이론과 JWT 구성 준비가 같은 날 이어짐.
- 미확정: 04-06 시점에 모든 인증 API가 실제 filter·SecurityContext까지 연결됐다는 주장. 실제 연결은 04-07이다.
- 미확정: production SSR framework나 hybrid rendering 구현. 04-21은 CSR/SSR 용어 보충 범위다.

## 선행 개념과 후속 기능 경계

- 선행 UI: [[concepts/html-css-basics|HTML/CSS 기본]], [[concepts/javascript-dom|JavaScript와 DOM]]
- 전체 구조: [[concepts/frontend-backend-architecture|Frontend/Backend 구조]], [[comparisons/react-router-vs-spring-api-url|React Router 주소 vs Spring API 주소]]
- 인증 비교: [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]], [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- 날짜 Summary: [[summaries/2026-03-31-spring-boot-controller-html|03-31 HTML→REST/React]], [[summaries/2026-04-01-react-router-spring-boot|04-01 axios·CORS]], [[summaries/2026-04-06-login-jwt-session-cookie|04-06 MPA/SPA·JWT]]
- Linux/AWS/CI/CD는 build·server·proxy·domain 배포로 이 구조를 운영하는 후속 범위다. Passwordless와 중간 프로젝트는 인증 선택 축의 후속이며 MPA/SPA를 자동 결정하지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.03.31(화)/2026.03.31(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.01(수)/2026.04.01(수).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.21(화)/2026.04.21(화).md`
