---
title: Spring Security JWT Filter
created: 2026-07-02
updated: 2026-07-16
type: concept
tags: [spring-boot, auth, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.02(목)/2026.04.02(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: high
---
# Spring Security JWT Filter

## 정의

이 페이지는 **React가 전달한 Bearer token을 Spring Security filter가 검증해 현재 요청의 `Authentication`을 `SecurityContextHolder`에 구성하는 순서**를 정리한다. token의 생성·저장·삭제 생명주기는 [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]], HTTP method·body·status는 [[concepts/spring-boot-rest-api|Spring Boot REST API]]에 위임한다.

## 왜 중요한가

Cart Controller가 client body의 member id 대신 `Authentication.getName()`으로 email을 얻으려면, Controller보다 앞에서 인증 객체가 만들어져야 한다. 또한 React의 role 기반 버튼 표시나 query의 role 값만으로 서버 authorization이 완성된 것처럼 보지 않으려면 filter의 인증 구성과 endpoint 권한 규칙을 따로 확인해야 한다.

## 처음 등장하고 확장된 날짜

| 날짜 | 구성 단계 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-02-react-bootstrap-homepage|04-02]] | password 저장 기반과 Security 설정 시작 | `SecurityConfig`, `BCryptPasswordEncoder` |
| [[summaries/2026-04-06-login-jwt-session-cookie|04-06]] | React interceptor·`LoginDto`·JWT 생성/검증 provider 작성 | `axiosInstance`, `JwtTokenProvider` |
| [[summaries/2026-04-07-member-api-string-token|04-07]] | filter·CORS·Security chain·AuthenticationManager·login Controller를 실제 연결 | `JwtAuthenticationFilter`, `SecurityFilterChain`, `MemberController.login()` |
| [[summaries/2026-04-14-cart-service|04-14]] | 보호 요청에서 구성된 Authentication을 업무 입구가 소비 | `CartController` |
| [[summaries/2026-04-17-cart-total-array-some|04-17]] | role별 Order 목록이 등장해 UI role과 서버 권한 경계를 드러냄 | `OrderList`, `OrderController` |

## artifact별 책임

| artifact | 수업에서 맡은 책임 | 맡지 않는 책임 |
|---|---|---|
| `BCryptPasswordEncoder` | Signup password를 일방향 encoding하고 login 인증에서 비교할 기반 제공 | JWT 생성·header 부착 |
| `AuthenticationManager` | login의 email/password 인증 요청 처리 | 후속 Bearer header 직접 파싱 |
| `JwtTokenProvider` | Member 기반 token 생성, token 검증, claims/email 추출 | React 저장·Controller 업무 처리 |
| React request interceptor | localStorage token을 읽어 Authorization header 부착 | token 유효성 판정·SecurityContext 생성 |
| `JwtAuthenticationFilter` | header 확인→prefix 제거→provider 검증→Authentication 생성 | login form 인증·Cart/Order 업무 규칙 |
| `SecurityContextHolder` | 현재 요청 security context에 Authentication 보관 | 영구 user 저장소·localStorage 대체 |
| Controller/Service | 인증 객체의 email 등을 사용해 업무 수행 | Bearer parsing과 서명 검증 |

## 04-06 작성과 04-07 실제 연결

- **04-06:** request/response interceptor, `LoginDto`, `JwtTokenProvider`를 작성했다. LoginPage 저장 코드도 준비했지만 Spring login Controller와 filter chain 전체 왕복을 아직 같은 날 완성했다고 보지 않는다.
- **04-07:** `JwtAuthenticationFilter`, 새 CORS bean, stateless `SecurityFilterChain`, permit URL, `anyRequest().authenticated()`, filter 등록, `AuthenticationManager`, `/member/login`을 연결했다. 이 날 실제 login/logout과 후속 요청의 토큰 경로가 맞물렸다.

## 로그인 요청 순서

1. React가 `/member/login`에 email·password body를 보낸다.
2. 공개 URL인 login 요청은 token이 없어도 filter chain을 계속 지나 Controller에 도달할 수 있다.
3. Controller는 `AuthenticationManager.authenticate()`에 `UsernamePasswordAuthenticationToken(email, password)`를 넘긴다.
4. `MemberDetailsService`가 email로 Member를 찾고, `BCryptPasswordEncoder` 기반 인증 구성이 password를 확인한다.
5. 인증 뒤 Controller가 Member를 조회하고 `JwtTokenProvider.createToken(member)`로 token을 만든다.
6. Controller가 accessToken과 회원 정보를 응답하고 React가 localStorage/user state에 저장한다.

JWT filter는 이 login form의 password 검증을 대신하지 않는다. login 요청에 기존 Bearer token이 없으면 header 분기를 건너뛰고 `filterChain.doFilter()`로 계속 진행한다.

## 후속 보호 요청 순서

1. React request interceptor가 localStorage의 accessToken을 읽어 `Authorization: Bearer ...`를 붙인다.
2. `JwtAuthenticationFilter`가 Authorization header를 읽고 `Bearer `로 시작하는지 확인한다.
3. prefix 길이만큼 잘라 token 문자열만 추출한다.
4. `JwtTokenProvider.validateToken()`으로 검증하고 email·claims의 role을 읽는다.
5. role에 `ROLE_` prefix를 붙인 `SimpleGrantedAuthority` 목록과 email로 `UsernamePasswordAuthenticationToken`을 만든다.
6. `SecurityContextHolder.getContext().setAuthentication(auth)`로 현재 요청의 인증을 구성한다.
7. filter chain이 계속되고 Controller가 `Authentication.getName()` 같은 방식으로 email을 사용한 뒤 Service가 업무를 처리한다.

## 입력 → 처리 → 결과

| 입력 | 보안 계층 처리 | 결과 |
|---|---|---|
| login email/password | AuthenticationManager→MemberDetailsService/password encoder | 인증 성공 뒤 JWT 발급 경로 |
| Bearer header 없는 공개 요청 | filter의 token 분기 건너뜀→chain 계속 | permit URL Controller 도달 가능 |
| 유효 Bearer header | prefix 제거→provider 검증→email/role 추출→Authentication 생성 | SecurityContext에 현재 요청 사용자/authority 설정 |
| 보호 API 요청 | `anyRequest().authenticated()`와 구성된 context | Controller가 인증 객체를 사용할 수 있음 |

## role·memberId·authorization 경계

- 04-07 filter는 token claim의 role로 authority를 만들었다.
- 같은 날 SecurityConfig는 일부 URL을 `permitAll()`로 두고 나머지는 `authenticated()`로 요구했다.
- 확인한 설정에는 endpoint별 `hasRole(...)` 규칙이 없다. 따라서 authority 생성만으로 관리자 기능의 서버측 role authorization이 완성됐다고 단정하지 않는다.
- 04-17 OrderList는 React user role로 버튼/요청을 분기하고 memberId·role을 query로 보냈다. Service도 전달된 role로 조회 메서드를 골랐다. client가 보낸 값과 token에서 구성된 authority의 서버 검증이 연결됐는지는 별도 점검 대상이다.
- UI에서 버튼이 안 보이는 것은 UX 조건이지 API 접근 통제 자체가 아니다.

## 자주 헷갈리는 원인

- **Bearer와 token:** Bearer는 header scheme 표시이고 실제 JWT 문자열은 prefix 뒤 부분이다.
- **interceptor와 filter:** React interceptor는 붙이고, Spring filter는 제거·검증한다.
- **AuthenticationManager와 JWT filter:** 전자는 login credential 인증, 후자는 발급 뒤 후속 요청 인증 구성이다.
- **SecurityContext와 client user:** SecurityContext의 principal/authority와 localStorage user object는 다른 계층이다.
- **인증과 인가:** `authenticated()` 통과와 ADMIN 전용 기능 허용은 같은 조건이 아니다.
- **Controller와 filter:** filter는 사용자 context를 준비하고, Controller/Service는 업무를 처리한다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]의 token 생명주기와 [[concepts/axios-interceptor-error-handling|Axios interceptor]]의 client header 처리.
- HTTP 입구: [[concepts/spring-boot-rest-api|Spring Boot REST API]]의 공개/보호 endpoint.
- 후속 소비: [[concepts/shopping-cart-flow|Cart]]가 인증 email을 사용하고 [[concepts/order-flow|Order]]가 role/ownership 경계를 드러낸다.
- password 저장: [[summaries/2026-04-03-spring-member-seed-react-comments|04-03 Member 저장]]의 BCrypt encoding 흐름을 이어받는다.

## 직접 수업·교안·후속 경계

- **직접 수업:** 04-02 BCrypt 기반, 04-06 Security/JWT 구성 작성, 04-07 login/filter/SecurityContext 연결, 04-14 이후 보호 API의 Authentication 사용이다.
- **교안 보충:** P08·JWT 이론의 보안 개념은 날짜 MD에 필요한 코드와 설명이 전사돼 있어 PDF를 source에 추가하지 않았다.
- **후속 과목:** Linux·AWS·CI/CD는 이 filter chain의 배포 환경이다. Passwordless·중간 프로젝트에서 별도 role/ownership 규칙이 구현됐더라도 4과목 authorization 완성으로 소급하지 않는다.

## 관련 페이지

- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 로그인과 JWT·세션·쿠키]]
- [[summaries/2026-04-07-member-api-string-token|2026-04-07 회원 API와 문자열·token]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[comparisons/authentication-vs-authorization|인증 vs 인가]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[queries/jwt-role-ui-vs-server-authorization|JWT role UI와 서버 인가는 왜 다른가]]

## 출처

- 위 frontmatter의 04-02·04-06·04-07 구성 및 04-14·04-17 후속 사용 MD
