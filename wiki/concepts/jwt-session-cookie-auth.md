---
title: JWT, 세션, 쿠키 인증
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [auth, backend, frontend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: high
---

# JWT, 세션, 쿠키 인증

## 정의

이 페이지는 **HTTP의 무상태성 위에서 로그인 상태를 어떤 방식으로 이어 가며, 수업의 JWT 문자열이 생성·저장·전달·삭제되는지**를 정리한다. Bearer token을 Spring Security가 검증해 `SecurityContext`를 만드는 내부 절차는 [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]에 위임한다.

## 왜 중요한가

04-06에는 HTTP 요청이 서로 독립적이라는 문제에서 Session·Cookie·JWT를 비교하고 React 로그인 화면과 token 저장 코드를 준비했다. 04-07에는 실제 `/member/login` 응답, localStorage 저장·삭제, request interceptor와 JWT filter를 연결했다. 이 둘을 한 날짜의 완성 구현처럼 합치면 “작성한 단계”와 “실제 API 왕복이 붙은 단계”가 흐려진다.

## 처음 등장하고 확장된 날짜

| 날짜 | 단계 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-06-login-jwt-session-cookie|04-06]] | HTTP 무상태성, Session/Cookie/JWT 비교, `LoginPage`, localStorage·interceptor·`LoginDto`·`JwtTokenProvider` 작성 | `LoginPage.tsx`, `axiosInstance.tsx`, `LoginDto`, `JwtTokenProvider` |
| [[summaries/2026-04-07-member-api-string-token|04-07]] | 로그인 Controller·Security filter 연결, 성공 user/token 저장, logout 삭제 | `/member/login`, `JwtAuthenticationFilter`, logout handler |
| [[summaries/2026-04-14-cart-service|04-14]] | token이 붙은 후속 Cart 요청에서 인증 email 사용 | `Authentication.getName()` |
| [[summaries/2026-04-17-cart-total-array-some|04-17]] | token이 붙는 Order 목록 요청과 client의 memberId/role query가 함께 등장 | `customAxios.get`, Order list API |

## Session·Cookie·JWT 비교와 수업 구현 범위

| 방식 | 상태/값이 머무는 중심 | 요청에서 이어지는 방식 | 이 수업의 범위 |
|---|---|---|---|
| Session | 서버 | 보통 session id를 통해 서버 상태를 찾음 | 개념 비교 |
| Cookie | 브라우저 | cookie 규칙에 따라 요청에 포함 | 저장소·전달 개념 비교 및 CORS credential 설정 언급 |
| JWT | client에 저장한 token 문자열, 서버는 서명 검증 | `Authorization: Bearer <token>` | React·Spring 실제 구현 |

04-06 설명에서 Session과 Cookie를 비교했지만, 이 쇼핑몰 실습에서 Session login과 Cookie 기반 auth를 JWT와 같은 수준으로 구현했다고 확대하지 않는다. 실제 연결 중심은 localStorage의 `accessToken`과 Authorization header다.

## JWT 문자열의 생명주기

### 1. 생성

04-07 `MemberController.login()`은 email·password를 `AuthenticationManager`에 넘겨 인증한 뒤 Member를 조회하고 `JwtTokenProvider.createToken(member)`를 호출했다. 성공 body에는 accessToken과 id·name·email·role이 함께 들어갔다.

### 2. 저장

React `LoginPage`는 응답에서 accessToken을 꺼내 localStorage의 `accessToken`에 저장하고, 나머지 user data는 JSON 문자열로 만들어 `user` key에 저장했다. TypeScript `User`/`LoginResponse` 선언은 이 값을 다루기 위한 모양이지 token 자체나 Java DTO가 아니다.

### 3. 전달

request interceptor는 localStorage에서 token을 읽고 값이 있으면 `Authorization`에 `Bearer ${token}`을 넣는다. Cart·Order 같은 후속 `customAxios` 요청이 이 설정을 재사용한다. React 요청 함수는 header를 붙일 뿐 token 유효성이나 서버 권한을 확정하지 않는다.

### 4. 소비

Spring filter가 Bearer prefix를 제거하고 token을 검증해 인증 객체를 만든 뒤에야 Controller가 `Authentication.getName()`으로 email을 읽을 수 있다. 이 내부 단계는 [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]에서 설명한다.

### 5. 삭제

04-07 logout handler는 React user state를 null로 만들고 localStorage의 `user`와 `accessToken`을 삭제했다. response interceptor도 **로그인 요청이 아닌** 401에서 accessToken을 삭제하고 로그인 경로로 이동하도록 작성됐다. localStorage 삭제는 client 상태 제거이며 이미 발급된 token의 서버측 blacklist/revocation 구현이 확인된 것은 아니다.

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| email·password login body | Spring 인증→Member 조회→JWT 생성 | token+회원 정보 응답 |
| login 성공 응답 | React가 token/user를 분리 | localStorage `accessToken`, `user` 저장과 App user state 갱신 |
| 후속 `customAxios` 요청 | interceptor가 Bearer header 추가→Spring filter 검증 | 인증 정보가 구성되면 보호 API가 사용자 email 사용 |
| logout 클릭 | user state null→두 localStorage key 삭제 | client가 로그아웃 상태로 전환 |
| 로그인 외 401 | response interceptor가 token 삭제·이동 | 만료/무효 token 이후 재로그인 경로 |

## 로그인 실패와 후속 API 401

- **로그인 요청 실패:** email/password 인증 자체가 실패하는 단계다. interceptor 코드는 login URL인지 검사해 일반 보호 API 401 처리와 분리했다.
- **Controller 코드의 401:** 인증 호출 뒤 Member 재조회가 null인 분기에 `{error: ...}` body를 반환한다.
- **로그인 외 401:** 저장 token이 없거나 무효·만료된 후속 보호 요청에서 발생할 수 있으며, response interceptor가 accessToken을 지우고 이동한다.

같은 401 숫자라도 발생 위치와 body가 같다고 가정하지 않는다. 원본에 없는 Spring Security 예외 응답 body를 만들어 적지 않는다.

## 자주 헷갈리는 원인

- **user와 accessToken:** user는 화면 표시·조건 분기에 쓰는 client 데이터이고 accessToken은 header로 전달할 인증 문자열이다.
- **저장과 인증:** localStorage에 값이 있다는 사실은 token 유효성이나 현재 서버 인증 성공을 보장하지 않는다.
- **Cookie와 localStorage:** 둘 다 브라우저 쪽 저장과 관련되지만 같은 저장소·자동 전달 규칙이 아니다.
- **로그아웃과 token 폐기:** client 삭제와 서버의 강제 무효화는 다른 기능이다.
- **role 표시와 authorization:** React가 role로 버튼을 감춘 것, client가 role을 query로 보낸 것, 서버가 접근 권한을 강제한 것은 서로 다른 단계다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]의 HTTP 요청·응답 경계와 header 개념.
- API 경계: [[concepts/spring-boot-rest-api|Spring Boot REST API]]의 login·보호 endpoint.
- client 공통 처리: [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]].
- 서버 인증 구성: [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]].
- 후속 기능: [[concepts/shopping-cart-flow|Cart]]는 인증 email을 사용하고, [[concepts/order-flow|Order]] 목록은 client id/role과 서버 검증 경계를 드러낸다.

## 직접 수업·교안·후속 경계

- **직접 수업:** 04-06 개념·구성 작성과 04-07 JWT login/logout·후속 header/filter 연결이다.
- **교안 보충:** P03·P04·P08의 HTTP/Cookie/Security 설명은 날짜 MD에 필요한 내용이 전사돼 있어 PDF를 source에 추가하지 않았다.
- **후속 과목:** Linux·AWS·CI/CD는 auth가 동작할 실행·배포 환경이고, Passwordless는 JWT와 다른 인증 절차의 확장이다. 중간 프로젝트의 실제 authorization을 이 수업 구현에 소급하지 않는다.

## 관련 페이지

- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 로그인과 JWT·세션·쿠키]]
- [[summaries/2026-04-07-member-api-string-token|2026-04-07 회원 API와 문자열·token]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 출처

- 위 frontmatter의 04-06·04-07 직접 구현 및 04-14·04-17 후속 사용 MD
