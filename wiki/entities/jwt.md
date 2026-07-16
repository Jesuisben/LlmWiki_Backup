---
title: JWT
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [auth, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
status: growing
confidence: high
---

# JWT

## 정의

JWT(JSON Web Token)는 Header·Payload·Signature로 구성된 서명 token 형식이다. 이 수업에서는 로그인 성공 시 서버가 token을 만들고, React가 저장·전달하며, Spring filter가 후속 요청에서 검증해 인증 정보를 구성하는 데 사용했다.

## 왜 중요한가

React SPA와 Spring REST API가 서로 다른 요청으로 통신하므로 로그인 이후의 요청마다 사용자를 식별할 근거가 필요했다. JWT 수업은 token 하나만 보는 것이 아니라 **생성→저장→Bearer 전달→검증→SecurityContext→삭제**를 client와 server에 나누어 연결했다.

## 첫 등장과 날짜별 확장

### 2026-04-06 — 개념과 구성 준비

[[summaries/2026-04-06-login-jwt-session-cookie|04-06]]에는 Cookie·Session, MPA·SPA, stateful/stateless와 JWT 구조·Claims를 비교했다. 이어서 다음 구성요소를 작성했다.

- React `axiosInstance`: localStorage의 `accessToken`을 읽어 요청의 Authorization header에 Bearer 형식으로 붙이고, 로그인 요청 이외의 401에서 token을 삭제하도록 구성.
- `User`·`LoginResponse`와 `LoginPage`: 로그인 응답을 accessToken과 userData로 분리해 localStorage와 React user state에 저장.
- Spring `LoginDto`와 JWT dependency 3개.
- `JwtTokenProvider`: token 생성·Claims 해석·email 추출·유효성 검사 메서드 작성.

이날은 구성요소를 준비한 날이며, Spring Security login·filter chain과 실제 보호 요청 연결은 04-07에 이어졌다.

### 2026-04-07 — 로그인과 후속 Bearer 인증 연결

[[summaries/2026-04-07-member-api-string-token|04-07]]에는 다음 두 경로를 분리해 연결했다.

1. **로그인 요청:** `AuthenticationManager`가 자격정보를 인증하고 `MemberDetailsService`가 사용자를 조회한 뒤 `MemberController`가 `JwtTokenProvider.createToken()`으로 token을 만들어 user 정보와 응답한다.
2. **로그인 후 요청:** `JwtAuthenticationFilter`가 Authorization header의 Bearer prefix를 제거하고 token을 검증한다. email과 role Claim으로 Authentication을 만들어 `SecurityContextHolder`에 저장한 뒤 다음 filter/Controller로 넘긴다.

같은 날 React logout에서 user와 accessToken을 localStorage에서 삭제하고 로그인 화면으로 이동했다. token secret/expiration을 `application.properties`에서 주입하도록 코드를 바꿨지만, 원본에도 환경변수 사용은 후속 공부 항목으로 남아 있다.

## 대표 artifact와 입력 → 처리 → 결과

| 단계 | 입력 | 처리 주체·artifact | 결과 |
|---|---|---|---|
| 생성 | email/password login body | `AuthenticationManager`, `MemberDetailsService`, `JwtTokenProvider` | accessToken과 user 응답 |
| 저장 | login response | `LoginPage`, localStorage, React user state | 후속 요청에 쓸 token과 화면용 user 분리 |
| 전달 | API request | axios request interceptor | Authorization Bearer header |
| 검증 | Bearer token | `JwtAuthenticationFilter`, `JwtTokenProvider` | 유효 token의 email·role Claim 추출 |
| 인증 문맥 | email·authority | Authentication, `SecurityContextHolder` | 후속 Controller가 인증 사용자 식별 가능 |
| 삭제 | logout 또는 로그인 외 401 | React logout/axios response interceptor | localStorage token 제거와 login 이동 |

## 구현 완료 범위와 미확정 경계

### 원본에서 확인됨

- JWT dependency, provider, login Controller, filter, SecurityConfig 등록, localStorage 저장·삭제, Bearer interceptor 코드를 작성했다.
- 올바른/올바르지 않은 로그인 계정 테스트를 진행하도록 기록했다.
- `SecurityConfig`에는 공개 URL과 그 밖의 authenticated 요청 규칙을 작성했다.

### 합치거나 과장하면 안 됨

- localStorage에 token 문자열이 있다는 사실만으로 server 검증·인증·인가가 완료된 것은 아니다.
- React `user.role`에 따른 메뉴/버튼과 token Claim authority, Spring endpoint authorization은 서로 다른 층이다.
- filter가 Authentication을 만들었다는 사실과 특정 업무 자원에 대한 세부 권한 정책은 같은 증거가 아니다.
- logout은 client 저장값 삭제와 화면 이동으로 구현했다. 서버 token 폐기 목록이나 refresh token은 원본에서 확인되지 않는다.
- 설정값을 properties로 옮겼다는 사실만으로 운영 secret 관리가 완료된 것은 아니다.

## 자주 헷갈리는 원인

- **Cookie·Session·JWT의 층위:** Cookie는 브라우저 저장/전달 수단, Session은 서버 상태 방식, JWT는 서명 token 형식이다. [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]에서 비교한다.
- **인증 vs 인가:** token 검증으로 사용자 신원을 구성하는 것과 해당 사용자가 특정 기능을 실행할 권한이 있는지는 별도 판단이다.
- **client role vs server authority:** React UI 분기는 보안 경계가 아니며 서버의 authority/authorization이 필요하다.
- **token vs user object:** accessToken 문자열, token Claims, Security Authentication, React user state는 동일 객체가 아니다.

## 이전 개념과 이후 기능 연결

- 선행: Member 회원가입·비밀번호 인코딩과 [[concepts/spring-boot-rest-api|Spring Boot REST API]]가 로그인 입력과 응답 기반이 됐다.
- 과목 내부: JWT 인증 정보는 Product·Cart·Order 요청에서 사용자 식별에 연결됐다. 상세 filter 원리는 [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]], 생명주기 비교는 [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]에 위임한다.
- 후속: Passwordless X1280은 별도 인증 서버·QR/앱 승인 흐름이며 이 JWT 구현과 같은 기술로 합치지 않는다. Linux/AWS/CI/CD의 운영 secret·배포도 04-06~04-07 직접 구현에 소급하지 않는다.

## 관련 페이지

- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 Cookie·Session·JWT와 token 생성 준비]]
- [[summaries/2026-04-07-member-api-string-token|2026-04-07 Bearer token과 Spring Security 인증]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[comparisons/authentication-vs-authorization|인증 vs 인가]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[queries/jwt-role-ui-vs-server-authorization|JWT role UI와 서버 인가는 왜 다른가]]
- [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`