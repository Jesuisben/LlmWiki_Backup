---
title: 2026-04-06 로그인, JWT, 세션과 쿠키
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf
status: growing
confidence: high
---
# 2026-04-06 로그인, JWT, 세션과 쿠키

## 한 줄 요약

로그인 상태 유지 방식을 쿠키·세션·JWT 관점에서 비교하고, React SPA에서 JWT를 쓰는 이유를 배웠다.

## 커리큘럼 위치와 흐름

회원 기능에서 인증으로 넘어간 날이다. 이전까지는 API를 호출해 데이터를 보여주는 구조였다면, 이제는 “누가 요청했는가”를 서버가 판단해야 하므로 인증 상태 전달 방식이 핵심이 된다.

## 배운 내용

- IT 관련 용어 p.48~49에서 쿠키는 브라우저/PC에 저장되는 값, 세션은 서버 쪽 상태와 `JSESSIONID` 같은 식별자로 연결되는 구조로 설명된다.
- JWT 이론 p.2~4는 React 같은 SPA 구조에서 HTML은 프론트가 담당하고 API 서버는 JSON 데이터를 주며, 인증 정보 전달에 JWT를 많이 쓰는 흐름을 보여준다.
- MPA와 SPA의 차이가 로그인 구조 선택에 영향을 준다.

## 핵심 실습 / 예제

- 로그인 후 발급받은 토큰을 프론트에서 보관하고, 이후 API 요청에 Bearer 토큰으로 붙이는 흐름을 준비했다.
- 쿠키/세션/JWT는 서로 대체어가 아니라 저장 위치와 책임이 다른 인증 구성 요소다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- 쿠키는 저장 수단, 세션은 서버 상태 관리 방식, JWT는 서명된 토큰 형식이다.
- SPA에서는 화면 전환을 React가 담당하므로 서버가 HTML 페이지를 계속 내려주는 MPA와 인증 흐름이 다르다.
- JWT를 쓰더라도 보안상 저장 위치와 만료 시간, 탈취 위험을 함께 생각해야 한다.

## 관련 페이지

- [[concepts/jwt-session-cookie-auth]]
- [[comparisons/session-vs-cookie-vs-jwt]]
- [[comparisons/mpa-vs-spa]]
- [[entities/jwt]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/IT 관련 용어.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf`
