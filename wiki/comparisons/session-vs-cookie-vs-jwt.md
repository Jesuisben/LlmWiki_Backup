---
title: Session vs Cookie vs JWT
created: 2026-07-02
updated: 2026-07-16
type: comparison
tags: [auth, backend, frontend, spring-boot, react]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
status: growing
confidence: high
---

# Session vs Cookie vs JWT

## 비교 목적

Cookie·Session·JWT는 셋 다 로그인 문맥에 등장하지만 같은 종류가 아니다.

- **Cookie:** browser가 값을 저장하고 HTTP 요청에 전달할 수 있는 수단
- **Session:** server가 사용자 상태를 보관하고 식별자로 찾는 상태 유지 방식
- **JWT:** claim을 담고 서명된 token을 client가 요청마다 전달하는 방식

이 비교는 저장·전달 수단과 인증 상태 설계를 분리한다. token 생성·저장·삭제 생명주기는 [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]], Bearer 검증과 Spring Security 연결은 [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]에 맡긴다.

## 실제 수업에서 비교가 필요해진 이력

- **2026-04-06 이론·준비:** Cookie와 Session의 저장 층위, MPA/SPA, Session/JWT·stateful/stateless를 비교하고 `axiosInstance`, LoginPage, `LoginDto`, JWT dependency, `JwtTokenProvider`를 작성했다.
- **2026-04-07 실제 연결:** login 인증 뒤 token 응답, localStorage 저장, request interceptor의 Bearer 부착, `JwtAuthenticationFilter`의 검증·claim 추출·`Authentication` 생성·`SecurityContext` 저장, logout 삭제 흐름을 연결했다.
- **2026-04-14:** Cart API가 `Authentication.getName()`으로 인증된 사용자의 email을 업무 기능에서 소비했다.
- **2026-04-17:** Order 요청이 `customAxios`와 client의 memberId·role을 사용하며 확장됐지만, 이 값들이 server endpoint authorization으로 교차 검증됐는지는 확인되지 않는다.

04-06에 provider와 frontend 준비 코드가 있다는 사실을 04-07의 filter·SecurityContext 연결 완료로 소급하지 않는다.

## 한눈에 보기

| 판단 항목 | Cookie | Session | JWT |
|---|---|---|---|
| 층위 | browser 저장·HTTP 전달 수단 | server-side 상태 유지 방식 | 서명된 token 형식·상태 전달 방식 |
| 상태 본체 | cookie 값 자체 | server의 session 저장소 | token 안의 subject/claim |
| client가 들고 다니는 것 | cookie | 보통 session 식별자 cookie | token 문자열 |
| server 처리 | cookie를 읽음 | 식별자로 session 상태 조회 | 서명·유효기간 등을 검증하고 claim 해석 |
| 수업 artifact | `withCredentials`, `JSESSIONID` 설명 | server session 저장소 조회 설명 | `accessToken`, Bearer header, provider/filter |
| 서로 함께 사용 | Session id를 cookie로 전달 가능 | Cookie와 함께 쓰는 경우가 일반적 | JWT도 cookie에 담을 수 있으나 수업 구현은 localStorage+header |

## 인접 개념도 별도 층위로 보기

| 개념 | 수업에서 확인된 역할 | Cookie/Session/JWT와의 관계 |
|---|---|---|
| localStorage | `accessToken`·user를 browser에 저장 | Cookie가 아니며, 수업 JWT 문자열을 보관한 장소 |
| Authorization header | `Bearer <token>` 전달 | JWT를 API 요청에 싣는 HTTP header |
| request interceptor | localStorage token을 읽어 header에 부착 | 저장소·token·인증 결과 자체가 아닌 요청 전처리 |
| `SecurityContext` | 검증 뒤 만든 `Authentication`을 현재 요청 처리에서 보관 | JWT 저장소가 아니라 Spring Security 인증 결과 context |
| role UI | React에서 ADMIN/USER 버튼을 표시·숨김 | server authorization과 동일하지 않음 |
| endpoint authorization | server가 요청 권한을 결정 | client role 표시나 token 존재만으로 완료되지 않음 |

## 실제 선택 상황 1 — Session 방식

04-06 설명에서 browser는 `JSESSIONID` 같은 식별자를 보내고 server는 session 저장소에서 사용자 상태를 찾는다. 여러 기기의 같은 계정도 서로 다른 식별자로 구분하는 설명이 이어졌다.

### 입력 → 처리 → 결과

1. browser가 session 식별자를 cookie로 전달한다.
2. server가 식별자에 대응하는 session 상태를 조회한다.
3. 요청 처리에서 로그인 사용자 상태를 사용한다.

이 페이지는 원본에 없는 session 저장소 제품·물리 위치, cookie option, timeout 값을 만들지 않는다. 4과목 쇼핑몰이 Session 방식으로 실제 완성됐다는 근거도 없다.

## 실제 선택 상황 2 — 수업 JWT 방식

### 04-06 준비

- `axiosInstance`가 localStorage의 `accessToken`을 읽어 요청에 붙이도록 작성됐다.
- LoginPage·`LoginDto`·JWT dependency와 `JwtTokenProvider`의 생성·해석·검증 기능이 준비됐다.
- JWT를 쓸 때 session 방식의 `withCredentials: true`를 제거한다는 수업 코드 설명이 있었다.

### 04-07 연결

1. login 요청을 `AuthenticationManager`가 인증한다.
2. Controller가 `Member`를 조회하고 token·user 정보를 응답한다.
3. React가 token을 localStorage에 저장한다.
4. 후속 요청에서 interceptor가 `Authorization: Bearer ...`를 붙인다.
5. filter가 prefix를 제거하고 token을 검증한 뒤 email·role claim을 읽는다.
6. filter가 authority와 `Authentication`을 만들고 `SecurityContextHolder`에 저장한다.
7. logout은 localStorage의 user·accessToken을 삭제한다.

이 단계는 login의 credential 인증과 후속 API 요청의 Bearer 검증을 분리해 읽어야 한다.

## 함께 사용하는 관계

- server가 사용자별 상태를 직접 관리하고 식별자로 찾는 설계는 Session 축에서 판단한다.
- client가 서명 token을 들고 API마다 전달하고 server가 검증하는 설계는 JWT 축에서 판단한다.
- browser 저장·전달 수단을 고를 때 Cookie와 localStorage/header를 별도로 판단한다.
- Cookie와 Session은 경쟁하는 같은 종류가 아니다. Session id를 Cookie로 전달하며 함께 쓸 수 있다.
- JWT도 Cookie에 저장할 수 있지만, 이 수업의 확인된 구현은 localStorage와 Authorization header다.
- MPA/SPA 선택은 [[comparisons/mpa-vs-spa|MPA vs SPA]]의 rendering 축에서 따로 판단한다.

## 확인된 구현 범위와 실행 미확정 범위

- 확인: 04-06 Cookie/Session/JWT 이론과 provider·frontend 구성 준비.
- 확인: 04-07 login→token 응답 코드→localStorage 저장 코드→Bearer filter→`SecurityContext` 연결 코드와 logout 삭제 코드.
- 확인: provider가 email·role claim을 구성하고 filter가 email·role을 읽어 authority와 `Authentication`을 만드는 코드.
- 확인: 04-14 Cart Controller가 `Authentication.getName()`을 실제 업무 입력으로 소비함.
- 미확정: 작성된 token의 실제 runtime claim 내용과 login/filter의 관찰된 성공 응답·출력. 코드 연결과 실행 결과를 분리한다.
- 미확정: cookie의 `HttpOnly`·`Secure`·`SameSite` 설정, 실제 session 저장소 위치·운영 구성.
- 미확정: localStorage 사용의 운영 보안 적합성이나 production 배포 방식.
- 미확정: 모든 endpoint의 server authorization 정책. React role UI, client query의 role, token authority를 하나의 완료 상태로 합치지 않는다.

## 자주 헷갈리는 원인과 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| Cookie·Session·JWT는 모두 저장소다 | Cookie는 전달/저장 수단, Session은 server 상태 방식, JWT는 token 형식이다. |
| JWT = localStorage | JWT는 token이고 localStorage는 수업에서 token을 둔 browser 저장 장소다. |
| Bearer = JWT | Bearer는 header에서 credential을 전달하는 방식이고 뒤 값이 수업의 JWT다. |
| JWT 검증 = login | login credential 인증과 후속 요청 token 검증을 분리한다. |
| role UI = authorization | button 표시와 server endpoint 접근 결정은 다른 계층이다. |
| JWT = SPA, Session = MPA | 인증 상태 축과 rendering architecture 축을 분리한다. |
| `SecurityContext` = session/JWT 저장소 | 현재 요청의 Spring Security 인증 결과 context로 본다. |

## 선행 개념과 후속 기능 경계

- 선행: [[comparisons/authentication-vs-authorization|인증 vs 인가]], [[comparisons/mpa-vs-spa|MPA vs SPA]]
- token 생명주기: [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]], [[entities/jwt|JWT]]
- 검증 연결: [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]], [[concepts/axios-interceptor-error-handling|Axios interceptor와 API 오류 처리]]
- 날짜 Summary: [[summaries/2026-04-06-login-jwt-session-cookie|04-06 이론·구성 준비]], [[summaries/2026-04-07-member-api-string-token|04-07 login·Bearer·SecurityContext]]
- Linux/AWS/CI/CD의 secret·HTTPS·배포 topology는 후속 운영 범위다. Passwordless와 중간 프로젝트는 외부 인증 서버·QR/앱 승인 등 별도 인증 흐름이며 JWT/Session의 단순 대체라고 소급하지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
