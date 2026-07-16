---
title: 2026-04-06 Cookie·Session·JWT 이론과 로그인 토큰 생성
created: 2026-07-06
updated: 2026-07-15
type: summary
tags: [spring-boot, react, frontend, backend, curriculum, study-log, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
status: growing
confidence: high
---

# 2026-04-06 Cookie·Session·JWT 이론과 로그인 토큰 생성

## 한 줄 요약

Cookie·Session·JWT와 MPA·SPA, stateful·stateless의 층위를 구분한 뒤 React `axiosInstance`·`LoginPage`가 토큰을 저장·전달할 준비를 하고 Spring `LoginDto`·`JwtTokenProvider`가 로그인 데이터와 JWT 생성·검증을 담당하도록 구성했다.

## 수업 위치와 날짜 연결

- 이전: [[summaries/2026-04-03-spring-member-seed-react-comments|2026-04-03]]에 회원가입 요청의 검증·중복 확인·저장을 완성했다.
- 오늘: 가입된 회원의 로그인 화면과 JWT 발급 양쪽을 React와 Spring에서 준비했다.
- 다음: [[summaries/2026-04-07-member-api-string-token|2026-04-07]]에는 Bearer 토큰을 요청에서 추출해 Spring Security 인증 정보로 바꾸는 필터와 실제 로그인 API를 연결한다.

## 실제 교시 흐름

### 1교시 — Cookie와 Session

- Cookie는 브라우저가 관리하는 작은 클라이언트 측 데이터로, 팝업의 “오늘 하루 보지 않기” 같은 예를 들었다.
- Session은 웹 서버가 저장하는 사용자 상태 정보이며, 브라우저가 보낸 `JSESSIONID`로 서버의 session 저장소에서 사용자를 구분하는 흐름을 확인했다.
- session 유효기간과 여러 기기의 로그인 구분을 보며, 로그인 상태를 어디에서 관리하는지가 보안·운영 방식에 영향을 준다는 배경을 잡았다.

### 2교시 — MPA·SPA와 Session·JWT 인증

- MPA는 이동할 때 서버가 전체 HTML을 다시 만들고 브라우저가 새로 고치는 구조로 설명했다.
- SPA는 처음 받은 HTML 위에서 JavaScript가 화면을 바꾸고 서버와 JSON을 주고받는 구조로 설명했다.
- Session 인증은 서버가 로그인 사용자 정보를 직접 저장하고, JWT 인증은 로그인 시 발급한 token을 매 요청에 전달해 사용자를 구분하는 방식으로 비교했다.
- JWT의 Header·Payload·Signature와 Claims를 간단히 보고, token 생성은 Java library를 사용한다는 점을 확인했다.
- 이론을 곧바로 React `axiosInstance.tsx`로 연결해, request interceptor가 localStorage의 `accessToken`을 `Authorization: Bearer ...`에 붙이고 response interceptor가 로그인 요청이 아닌 401 응답에서 token을 지운 뒤 로그인 화면으로 이동하도록 했다.
- `User.ts`와 `LoginResponse` interface로 사용자 필드와 `accessToken`이 포함된 서버 응답의 형태를 나눴다.

### 3교시 — MIME type과 JSON 요청

- MIME type이 데이터 형식을 알려 주는 표준 문자열임을 확인했다.
- 로그인 JSON을 보낼 때 HTTP header의 `Content-Type`을 `application/json`으로 지정하는 형태를 살폈다.

### 4교시 — React LoginPage

- email·password·errors를 state로 관리하고 submit event에서 기본 동작을 막았다.
- `/member/login`으로 email과 password를 POST하고, 응답의 `accessToken`과 나머지 사용자 데이터를 전개 연산자로 분리했다.
- token은 localStorage의 `accessToken`, 사용자 객체는 JSON 문자열로 바꿔 `user`에 저장하고 로그인 성공 callback 뒤 `/`로 이동했다.
- 실패 시 서버 응답 message 또는 `Server Error`를 화면 오류 state에 넣었다.

### 5~6교시 — Routing·메뉴·App 상태 연결

- `AppRouters.tsx`가 `LoginPage`에 `handleLoginSuccess`를 `onLogin` props로 전달했다.
- `MenuItems.tsx`는 `user?.role`에 따라 ADMIN·USER·미로그인 메뉴를 나누었다.
- `App.tsx`에서 React 로그인 부분을 마무리하고 Spring 작업으로 넘어갔다.

### 6교시 후반 — Spring 직렬화와 JWT 의존성

- `LocalDate`를 JSON으로 다룰 때를 대비해 Jackson JSR-310 의존성과 `@JsonFormat`을 확인했다.
- JWT API·구현체·Jackson 연동 의존성을 `pom.xml`에 추가했다.

### 7~8교시 — LoginDto와 JwtTokenProvider

- 로그인 요청 전용 `LoginDto`에 email과 password를 두어 클라이언트 입력을 받도록 했다.
- Claims의 subject·expiration·issued-at 같은 항목과 role 같은 사용자 정보를 확인했다.
- `JwtTokenProvider`를 만들어 서명 key 생성, `createToken(Member)`, Claims 추출, email 추출, token 검증의 책임을 모았다.
- `createToken()`은 Member의 email과 role을 token 정보로 사용하고 발급·만료 시간을 설정한 JWT 문자열을 만들도록 작성했다.

## 대표 artifact

| 구간 | 대표 artifact | 역할 |
|---|---|---|
| React 공통 통신 | `axiosInstance.tsx` | token 자동 첨부, 401 후 token 제거·로그인 이동 |
| React 데이터 | `User.ts`, `LoginResponse` | 로그인 응답의 사용자 정보와 accessToken 형태 선언 |
| React 화면 | `LoginPage.tsx` | 로그인 입력, POST, 응답 분리·저장, 화면 이동 |
| Spring 요청 | `LoginDto` | email·password 로그인 입력 전용 객체 |
| Spring token | `JwtTokenProvider` | JWT 생성·Claims 해석·email 추출·유효성 검사 |

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| LoginPage의 email·password | JSON으로 `/member/login` POST | Spring이 받을 로그인 요청 준비 |
| 로그인 성공 응답의 사용자 필드와 `accessToken` | 전개 연산자로 분리 | token과 사용자 정보를 localStorage에 각각 저장 |
| 이후 axios 요청 | request interceptor가 `accessToken` 확인 | `Authorization` header에 Bearer token 첨부 |
| 로그인 요청이 아닌 API의 401 응답 | response interceptor가 token 제거 | `/member/login`으로 이동 |
| 인증된 `Member` | `JwtTokenProvider.createToken()`이 email·role·시간·서명을 구성 | JWT 문자열 생성 |

## 실제로 헷갈리기 쉬운 지점

- **Cookie와 Session은 단순 대체재가 아니다.** Cookie는 클라이언트 저장·전달 수단이고, Session은 서버가 사용자 상태를 보관하는 방식이다.
- **MPA/SPA와 Session/JWT는 비교 축이 다르다.** 앞은 화면 구성·전환 구조이고, 뒤는 인증 상태를 관리·증명하는 방식이다.
- **stateless는 아무 정보도 없다는 뜻이 아니다.** 수업에서는 JWT처럼 서버 session 상태에 의존하지 않고 요청 token으로 인증 정보를 확인하는 방향을 배웠다.
- **JWT Payload를 비밀 저장소처럼 보면 안 된다.** 수업에서도 Signature를 위변조 방지용으로 설명했고, `SECRET_KEY`는 노출되지 않게 관리해야 한다고 메모했다.
- **React 저장과 Spring 발급은 서로 다른 절반이다.** 오늘은 양쪽 artifact를 준비했으며, 실제 인증·회원 조회·로그인 응답 연결은 다음 날 완성한다.

## 직접 수업과 후속 확장 경계

- 직접 학습·구현: Cookie/Session/JWT, MPA/SPA, stateful/stateless 이론, axios interceptor, LoginPage, localStorage, LoginDto, JwtTokenProvider.
- 다음 날 직접 확장: Bearer token parsing, JWT filter, SecurityContext, MemberDetailsService, SecurityConfig, MemberController login, 로그인 테스트.
- 후속 범위: Product·Cart·Order는 인증된 사용자와 역할을 기능에 적용한다. Linux·AWS·CI/CD는 실행·배포 단계이고, Passwordless는 별도 후속 인증 방식이다.

## 관련 페이지

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]
- [[comparisons/mpa-vs-spa|MPA vs SPA]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- [[entities/jwt|JWT]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`