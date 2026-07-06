---
title: Axios interceptor와 API 오류 처리
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [react, typescript, frontend, auth]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# Axios interceptor와 API 오류 처리

## 정의

Axios interceptor는 React 앱에서 API 요청이나 응답을 공통으로 가로채 처리하는 장치다. 수업에서는 JWT 로그인 후 401 응답이 오면 토큰을 삭제하고 로그인 페이지로 보내는 흐름, 상품 등록/수정 실패 시 서버 검증 오류를 화면 오류 state에 반영하는 흐름에서 등장했다.

## 왜 중요한가

로그인 만료, 권한 없음, 검증 실패는 여러 화면에서 반복된다. 각 컴포넌트마다 같은 코드를 쓰면 중복이 커지므로 공통 axios 인스턴스와 interceptor로 인증 Header·오류 처리를 모아두는 것이 유지보수에 좋다.

## 핵심 설명

- 요청 interceptor: 저장된 JWT를 Authorization Header에 붙이는 데 사용한다.
- 응답 interceptor: 서버가 401을 반환하면 토큰 삭제, 사용자 상태 초기화, 로그인 페이지 이동 같은 공통 처리를 한다.
- 컴포넌트 내부 오류 처리: 상품 등록/수정처럼 필드별 오류가 필요한 화면은 `error.response?.data?.errors`를 읽어 local state에 넣는다.

## 예시

2026-04-06 노트에는 로그인 요청 자체인지 검사한 뒤, 로그인 요청이 아닌 API에서 401이 발생하면 잘못된 토큰을 삭제하고 로그인 페이지로 유도하는 흐름이 나온다. 2026-04-10 상품 등록/수정 노트에는 서버의 `errors`와 `message`를 React form 오류 표시로 연결하는 예시가 나온다.

## 자주 헷갈리는 점

- 공통 인증 오류는 interceptor, 화면별 입력 검증 오류는 해당 form component에서 처리한다.
- optional chaining(`?.`)은 중간 값이 없을 때 앱이 터지지 않도록 막아 준다.
- 401은 인증 문제이고, 400대 검증 오류는 입력값 문제일 수 있으므로 사용자 안내 문구도 달라야 한다.

## 관련 개념

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[concepts/react-form-state-event|React 폼 상태와 이벤트]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/Study/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/Study/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md`
