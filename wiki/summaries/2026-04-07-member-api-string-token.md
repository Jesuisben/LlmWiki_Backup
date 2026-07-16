---
title: 2026-04-07 Bearer token과 Spring Security JWT 인증 흐름
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
status: growing
confidence: high
---

# 2026-04-07 Bearer token과 Spring Security JWT 인증 흐름

## 한 줄 요약

Java `String`으로 `Bearer ` 접두어를 확인·제거하는 연습에서 출발해 `JwtAuthenticationFilter`의 token 검증·인증 객체 저장, `MemberDetailsService`의 회원 조회, CORS·`SecurityConfig`, `MemberController.login()`과 로그인·로그아웃 테스트까지 JWT 인증 흐름을 연결했다.

## 수업 위치와 날짜 연결

- 이전: [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06]]에 React LoginPage·axios interceptor와 Spring `JwtTokenProvider`를 준비했다.
- 오늘: token 발급 전 로그인 인증 경로와 발급 후 요청 인증 경로를 Spring Security에 연결했다.
- 다음: [[summaries/2026-04-08-product-domain-oci|2026-04-08]]에는 인증 기반 위에서 Category·Product 상품 도메인과 목록 기능을 시작한다.

## 실제 교시 흐름

### 1교시 — String에서 Bearer token 처리 원리 익히기

- `Bearer hello world` 문자열로 `toLowerCase`, `toUpperCase`, `contains`, `startsWith`, `endsWith`, `length`, `String.format`, `substring`, `replace`를 실습했다.
- 특히 `"Bearer ".length()`와 `substring()`을 연결해 Authorization header에서 접두어 뒤의 token만 꺼내는 데 필요한 문자열 처리를 준비했다.

### 2교시 — JwtAuthenticationFilter

- 모든 요청에서 Controller보다 먼저 한 번 실행되는 `OncePerRequestFilter` 기반 filter를 만들었다.
- Authorization header를 읽고 null이 아니면서 `Bearer `로 시작하는지 확인했다.
- 접두어 길이 이후 문자열을 token으로 추출하고 `JwtTokenProvider.validateToken()`으로 검증했다.
- 유효한 token에서 email과 Claims의 role을 꺼내 `GrantedAuthority` 목록과 `UsernamePasswordAuthenticationToken`을 만들었다.
- 이 인증 객체를 `SecurityContextHolder`의 context에 저장하고, 마지막에는 `filterChain.doFilter()`로 다음 filter 또는 Controller에 요청을 넘겼다.
- `Authentication`이 `SecurityContext` 안에 있고 이를 `SecurityContextHolder`가 다룬다는 구조를 교안에서 함께 확인했다.

### 3교시 — CORS 설정을 Spring Security 쪽으로 이동

- 기존 `WebConfig.addCorsMappings()` 설정을 주석 처리했다.
- 별도 `CorsConfig`에서 허용 origin, HTTP method, `Authorization`·`Content-Type`·`Accept` header, credentials 여부를 구성했다.
- 이 설정을 `CorsConfigurationSource` Bean으로 만들어 Spring Security가 사용하도록 준비했다.

### 4교시 — 사용자 조회와 SecurityConfig

- `MemberDetailsService`가 `UserDetailsService`를 구현하고 `loadUserByUsername(email)`에서 `MemberRepository.findByEmail()`로 회원을 조회하도록 했다.
- 회원이 없으면 `UsernameNotFoundException`을 발생시키고, 있으면 email·암호화된 password·role을 가진 Spring Security `UserDetails`를 반환했다.
- `SecurityConfig`에서는 CORS 설정을 연결하고 CSRF를 비활성화했으며 session policy를 `STATELESS`로 두었다.
- 공개 URL은 허용하고 나머지는 인증을 요구했으며, `JwtAuthenticationFilter`를 `UsernamePasswordAuthenticationFilter` 앞에 등록했다.
- `AuthenticationManager` Bean도 제공해 Controller login 인증에 사용할 준비를 했다.

### 5교시 — MemberController 로그인 API

- `/member`를 공통 mapping으로 묶고 `/login`, `/signup`으로 나눴다.
- `login()`은 `LoginDto`의 email·password로 `UsernamePasswordAuthenticationToken`을 만들고 `AuthenticationManager.authenticate()`에 전달했다.
- 인증 처리 뒤 `MemberService.findByEmail()`로 응답에 사용할 회원 정보를 조회했다.
- 회원이 없으면 `UNAUTHORIZED` 응답을, 있으면 `JwtTokenProvider.createToken()`으로 token을 만들고 accessToken·id·name·email·role을 응답했다.
- 회원가입 endpoint는 전날의 Validation·중복 확인·저장 흐름을 유지했다.

### 6교시 — 로그인 테스트

- 올바른 계정과 올바르지 않은 계정으로 로그인 동작을 테스트했다.

### 7~8교시 — 로그아웃과 JWT 설정값 분리

- React `handleLogout()`에서 user와 accessToken을 localStorage에서 제거하고 로그인 화면으로 이동하도록 했다.
- `JwtTokenProvider`의 secret과 expiration을 코드에 직접 둔 형태에서 `@Value`로 설정을 받는 형태로 바꿨다.
- `application.properties`에 JWT secret·expiration 항목을 두었고, 수업 마지막에는 환경변수로 가져오는 방법을 추가 학습 대상으로 남겼다.

## 두 인증 경로를 구분하기

| 경로 | 시작 | 핵심 처리 | 결과 |
|---|---|---|---|
| 로그인 시도 | email·password POST | `AuthenticationManager`가 `MemberDetailsService.loadUserByUsername()`을 통해 회원을 찾고 자격 증명을 인증 | 성공한 Member로 JWT 생성·로그인 응답 |
| 로그인 후 API 요청 | `Authorization: Bearer ...` | `JwtAuthenticationFilter`가 접두어 제거→검증→email/role 추출→인증 객체 생성 | `SecurityContextHolder`에 인증 저장 후 요청 계속 |

`JwtAuthenticationFilter`가 Repository를 직접 호출한 것은 아니다. 회원 조회는 로그인 인증 과정의 `MemberDetailsService`와 응답 구성 과정의 `MemberService`에서 나타났고, filter는 이미 발급된 token의 email·role을 인증 객체로 바꾸었다.

## 대표 artifact

| artifact | 역할 |
|---|---|
| `StringTest` | Bearer 접두어 확인·길이 계산·부분 문자열 추출 연습 |
| `JwtAuthenticationFilter` | 요청 token 검증과 `SecurityContextHolder` 인증 저장 |
| `MemberDetailsService` | email로 회원을 찾아 Spring Security `UserDetails` 구성 |
| `CorsConfig` | React 요청 origin·method·header 정책 제공 |
| `SecurityConfig` | stateless 정책, 공개/인증 URL, JWT filter 순서, AuthenticationManager 구성 |
| `MemberController.login()` | 로그인 인증, 회원 조회, JWT 생성, 사용자 정보 응답 |

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| Authorization header의 Bearer 문자열 | `startsWith()` 확인 후 `substring()`으로 token 추출 | JWT 검증 입력 확보 |
| 유효한 token | email·role Claims → authority·Authentication 생성 | `SecurityContextHolder`에 인증 정보 저장 |
| LoginDto의 email·password | `AuthenticationManager.authenticate()`와 사용자 조회 | 성공 시 JWT·회원 정보 응답, 회원 정보 부재 시 `UNAUTHORIZED` |
| 로그아웃 event | React user state와 localStorage의 user·accessToken 제거 | 로그인 화면으로 이동 |

## 실제로 헷갈리기 쉬운 지점

- **Bearer는 token 내용이 아니다.** Authorization header에서 인증 scheme을 표시하는 접두어이며 실제 JWT는 그 뒤 문자열이다.
- **로그인 인증과 후속 요청 인증은 실행 시점이 다르다.** `MemberDetailsService`는 login 자격 증명 확인 쪽이고, JWT filter는 발급된 token이 붙은 후속 요청 쪽이다.
- **CORS와 인증은 같은 검사가 아니다.** CORS는 browser origin·method·header 허용 정책이고, JWT filter는 token으로 사용자를 인증한다. `SecurityConfig`에서 함께 연결되지만 책임은 다르다.
- **`SecurityContextHolder`는 token 저장소가 아니다.** 검증된 요청에 대해 만들어진 `Authentication`을 현재 security context에 보관한다.
- **설정 파일 이동이 최종 secret 관리라는 뜻은 아니다.** 수업 마지막에 환경변수 사용을 추가 학습 대상으로 남겼으므로 운영 secret 관리까지 완료한 것으로 확대하지 않는다.

## 직접 수업과 후속 확장 경계

- 직접 구현: String/Bearer parsing, JWT filter, SecurityContext, CORS Bean, MemberDetailsService, SecurityConfig, login Controller, 로그인·로그아웃 테스트, JWT 설정 property 전환.
- 다음 직접 확장: Product 목록은 공개 URL로 시작하고 이후 역할·인증이 Product·Cart·Order 기능과 만난다.
- 후속 범위: Linux·AWS·CI/CD는 배포와 운영 설정이며, Passwordless는 JWT 수업과 구분되는 후속 인증 과목이다.

## 관련 페이지

- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[entities/jwt|JWT]]
- [[comparisons/authentication-vs-authorization|인증(Authentication) vs 인가(Authorization)]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`