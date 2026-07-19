---
title: 인증(Authentication) vs 인가(Authorization)
created: 2026-07-13
updated: 2026-07-18
type: comparison
tags: [auth, backend, spring-boot]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md
status: growing
confidence: high
---

# 인증(Authentication) vs 인가(Authorization)

## 비교 목적

FrontEnd_BackEnd 수업에서는 04-06의 로그인 입력·JWT 구성 준비, 04-07의 credential 인증·후속 Bearer 검증, 04-14의 인증 사용자 Cart 처리, 04-17~20의 client role 기반 주문 화면이 차례로 등장했다. Passwordless 05-19는 인증·인가·IDP·SSO·상호인증과 AAM/APE 조직 관리를, 05-20은 FilingBox의 RO/RW/AO/WORM 저장 동작 정책을 더했다. 이 흐름에서 **사용자를 확인해 현재 요청의 `Authentication`을 만드는 일**, **그 사용자가 endpoint·자원·관리 기능을 실행해도 되는지 판단하는 일**, **허용된 접근 뒤 저장소가 쓰기·추가·변경·삭제를 어떻게 제한하는지**를 같은 완료 상태로 합치지 않기 위해 비교한다.

## 처음 비교가 필요해진 날짜와 이후 확장

| 날짜 | 비교가 필요해진 이유 | 확인된 artifact |
|---|---|---|
| [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06]] | LoginPage가 email·password를 보내고 JWT provider와 role Claim을 준비했지만 실제 Spring login/filter chain은 다음 날 범위였다. | `LoginDto`, `LoginPage`, `JwtTokenProvider`, React `user.role` 메뉴 |
| [[summaries/2026-04-07-member-api-string-token|2026-04-07]] | login credential 인증과 발급 뒤 Bearer 요청 인증이 서로 다른 경로로 연결됐다. | `AuthenticationManager`, `MemberDetailsService`, `JwtAuthenticationFilter`, `SecurityContextHolder`, `SecurityConfig` |
| [[summaries/2026-04-14-cart-service|2026-04-14]] | Controller가 body의 회원 id 대신 현재 요청의 `Authentication.getName()`을 사용했다. | `CartController`, 인증 email |
| [[summaries/2026-04-17-cart-total-array-some|2026-04-17]]~[[summaries/2026-04-20-order-list-scenario|04-20]] | client role·회원 식별값으로 목록과 버튼을 나눴지만 server authority·소유자 대조는 확인되지 않았다. | `OrderList`, role·memberId parameter, 완료·취소 UI/API |
| [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19]] | 인증·인가·IDP·SSO·상호인증과 AAM/APE 조직 사용자·인증기 관리 책임을 구분했다. | 일부 service 상태·사용자 전달 확인 서술, 세부 role enforcement 결과 미보존 |
| [[summaries/2026-05-20-filingbox-giga-mega|2026-05-20]] | 인증·인가 뒤에도 저장소 operation 정책이 별도로 남는다는 경계를 학습했다. | RO/RW/AO/WORM 설정·명령, mode별 거부 결과 미보존 |

## 한눈에 보기

| 항목 | 인증(Authentication) | 인가(Authorization) |
|---|---|---|
| 핵심 질문 | 이 요청의 사용자는 누구이며 신뢰할 수 있는가? | 인증된 사용자가 이 기능·자원에 접근해도 되는가? |
| 로그인 시점 | email·password를 `AuthenticationManager`가 확인 | 로그인 성공 뒤 허용할 기능을 결정하는 별도 정책 |
| 후속 요청 | Bearer JWT 검증→email/role 추출→`Authentication` 구성 | `Authentication`의 authority·정책·소유자 조건으로 endpoint 접근 판단 |
| Spring 표현 | `UserDetails`, `Authentication`, `SecurityContext` | `requestMatchers`, `authenticated`, role/authority·소유자 규칙 |
| React 표현과 관계 | localStorage의 user/token은 인증 결과를 화면에서 보관·사용 | role별 메뉴·버튼은 UX 분기일 뿐 서버 인가 자체는 아님 |
| 조직 관리와 관계 | AAM/APE가 사용자·인증기 정보를 연결·확인 | 인증된 관리자가 조직·연동 서비스·사용자·인증기 관리 기능을 실행할 권한은 별도 정책 |
| 저장소 operation과 관계 | 사용자의 신원 확인만으로 file 변경 정책이 정해지지 않음 | 접근 허용 뒤 RO/RW/AO/WORM이 쓰기·추가·변경·삭제를 별도로 제한 |
| 실패 의미 | credential 또는 token을 신뢰할 수 없음 | 사용자는 확인됐지만 요청한 작업은 허용되지 않음 |

## 언제 무엇을 쓰는가

### 상황 1 — 로그인 credential을 확인할 때

04-07의 `/member/login` 흐름은 Login DTO의 email·password로 `UsernamePasswordAuthenticationToken`을 만들고 `AuthenticationManager.authenticate()`에 전달했다. `MemberDetailsService`는 email로 회원과 암호화된 password·role을 담은 `UserDetails`를 제공했다. 성공 뒤 Controller가 Member를 조회해 JWT와 사용자 정보를 응답했다. 이 경로의 중심은 **credential로 사용자를 인증하는 것**이다.

### 상황 2 — 로그인 뒤 Bearer 요청을 받을 때

후속 요청에서는 React interceptor가 token을 붙이고 `JwtAuthenticationFilter`가 Bearer 접두어 제거→서명·유효성 검증→email/role Claim 추출→`GrantedAuthority`와 `Authentication` 생성→`SecurityContextHolder` 저장을 수행했다. 이 역시 현재 요청의 사용자를 만드는 **인증 경로**다. role이 들어 있어도 아직 특정 관리자 endpoint를 허용했다는 뜻은 아니다.

### 상황 3 — Cart와 Order 기능의 접근 범위를 판단할 때

04-14 Cart는 구성된 `Authentication`의 email로 사용자 Cart를 찾았다. 반면 04-17 Order 목록은 client가 보낸 memberId·role로 Service 분기를 했고, 04-20은 React `user.role`로 버튼을 나눴다. 후자의 화면·parameter 분기는 인가와 관련된 요구사항을 드러내지만, **client 값을 token authority와 대조하거나 완료·취소 endpoint에서 ADMIN·당사자 여부를 검사하는 코드**는 지정 원본에서 확인되지 않는다.

### 상황 4 — 조직 관리와 저장소 동작을 분리할 때

05-19의 AAM/APE에서 사용자 신원을 확인하고 조직·사용자·인증기 정보를 연결하는 일은 인증 관리다. 인증된 관리자가 어떤 관리 기능을 실행할 수 있는지는 인가 문제이며, 원본에는 세부 role enforcement 결과가 보존되지 않았다. 05-20의 FilingBox에서는 접근 뒤에도 RO/RW/AO/WORM이 저장 operation을 별도로 제한했다. 인증 성공, 최종 서비스 인가 성공, 저장소의 write/delete 허용은 세 개의 완료 상태다.

## 대표 artifact의 입력 → 처리 → 결과

| 구간 | 입력 | 처리 | 결과·판단 |
|---|---|---|---|
| login credential 인증 | email·password | `AuthenticationManager`→`MemberDetailsService`→password 확인 | 인증 성공 뒤 JWT 발급 경로로 이동 |
| 후속 Bearer 인증 | Authorization header의 JWT | filter가 검증하고 role Claim을 `ROLE_...` authority로 변환 | 현재 요청의 `Authentication`이 SecurityContext에 저장됨 |
| 공개/보호 URL 정책 | 요청 URL | `permitAll()` 또는 `anyRequest().authenticated()` | 공개 요청 허용 또는 인증 필요 판단 |
| role별 주문 UI | localStorage에서 복원한 `user.role` | React가 메뉴·완료/취소 버튼을 조건부 렌더링 | 사용자에게 보이는 화면만 달라짐 |
| 주문 API 접근 | memberId·role·Order id 등 | Controller/Service가 업무 처리 | 원본에서 endpoint별 role·소유자 인가가 확인되지 않아 완료로 단정 불가 |
| AAM/APE 조직 관리 | 조직·사용자·인증기·연동 정보 | 관리 server가 정보를 연결·전달 | 일부 전달 확인 서술은 있으나 세부 관리자 권한 집행 결과는 미보존 |
| FilingBox operation | 인증·접근 뒤 file operation | RO/RW/AO/WORM 정책 적용 | 설정·명령은 보존됐지만 mode별 거부·허용 결과는 미보존 |

## 함께 사용하는 관계

인증과 인가는 대체재가 아니라 순서상 함께 쓰는 책임이다. 먼저 credential 또는 token을 검증해 `Authentication`을 만들고, 그 다음 서버가 principal·authority와 요청 자원의 소유 관계를 이용해 인가해야 한다. Passwordless도 인증 방식을 앱 승인·외부 인증 서버 쪽으로 바꾸지만, 성공한 사용자가 어떤 Spring endpoint나 AAM/APE 관리 기능을 실행할 수 있는지는 여전히 별도 인가 정책이 필요하다. 그 뒤 file operation은 RO/RW/AO/WORM 같은 저장소 정책이 다시 제한한다.

## 확인된 구현 범위와 실행 미확정 범위

### 원본에서 확인됨

- 04-06에 React login/token 저장·role UI와 Spring JWT provider를 준비했다.
- 04-07에 credential 인증, JWT 발급, 후속 Bearer 검증, authority 생성, SecurityContext 저장을 연결했다.
- 같은 날 `SecurityConfig`는 지정 공개 URL을 `permitAll()`로, 나머지를 `authenticated()`로 두었다.
- 04-14 Cart Controller가 현재 요청의 인증 email을 사용했다.
- 04-17~20에 USER/ADMIN별 주문 목록·버튼·완료/취소 시나리오와 API가 등장했다.
- 05-19에 인증·인가·IDP·SSO·상호인증과 AAM/APE 조직 사용자·인증기 관리가 등장했고 일부 상태·전달 확인 서술이 남았다.
- 05-20에 FilingBox RO/RW/AO/WORM 설정·명령 절차가 등장했지만 mode별 실행 결과는 보존되지 않았다.

### 확인되지 않았거나 완료로 볼 수 없음

- 확인한 04-07 `SecurityConfig`에는 endpoint별 `hasRole(...)` 규칙이 없다.
- Order 목록의 client role/memberId가 JWT authority·principal과 대조되는 코드는 확인되지 않았다.
- 완료·취소 endpoint가 ADMIN 또는 주문 당사자인지 검사하는 코드는 확인되지 않았다.
- filter가 `Authentication`을 만든 사실만으로 모든 endpoint의 authorization이 완성됐다고 볼 수 없다.

## 헷갈리기 쉬운 포인트

- **login 성공=모든 API 허용:** login은 사용자 확인 결과다. 기능별 허용 범위는 별도다.
- **JWT에 role Claim=서버 인가 완료:** Claim은 authority 구성 재료다. endpoint 정책과 자원 소유자 검사가 추가로 필요하다.
- **React에서 ADMIN 버튼만 표시=ADMIN API 보호:** UI 숨김은 우회 호출을 막지 못한다.
- **`authenticated()`=ADMIN 검사:** 이는 인증된 요청을 요구하는 조건이며 특정 role 검사와 다르다.
- **SecurityContext=token 저장소:** 현재 요청의 인증 객체를 보관하는 문맥이지 localStorage나 영구 회원 DB가 아니다.
- **Passwordless=인가 기술:** Passwordless는 credential 확인 방식을 바꾸며 권한 정책을 자동 생성하지 않는다.
- **AAM/APE 사용자 전달 확인=관리 기능 인가 완료:** 정보 연결 관찰과 role별 관리 권한 집행은 별도다.
- **인증·인가 성공=WORM 보호 완료:** 저장소의 쓰기·추가·변경·삭제 정책과 실제 거부 결과를 따로 검증해야 한다.

## 잘못된 동일시와 올바른 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| localStorage에 user가 있다 → 인증됨 | 서버가 credential/token을 검증하고 현재 요청의 Authentication을 구성했는가 |
| JWT role Claim이 있다 → ADMIN endpoint가 보호됨 | SecurityConfig·method security·Service에서 해당 authority/소유자를 실제 검사하는가 |
| 버튼이 안 보인다 → 접근 불가 | endpoint를 직접 호출해도 서버가 거절하는 정책이 있는가 |
| 인증 성공 → 모든 데이터 조회 가능 | 요청 사용자가 해당 데이터의 소유자이거나 필요한 authority를 가졌는가 |

## 선행 개념과 후속 기능 연결

- token 생명주기: [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- login·후속 요청 인증 구성: [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- 화면 role과 서버 정책의 계층 분리: [[queries/jwt-role-ui-vs-server-authorization|JWT role UI와 서버 인가는 왜 다른가]]
- 인증 사용자 소비: [[concepts/shopping-cart-flow|장바구니 기능 흐름]]
- role·소유자 경계가 드러난 기능: [[concepts/order-flow|주문 기능 흐름]]

## 직접 수업·교안·후속 과목 경계

- **FrontEnd_BackEnd 직접 수업:** 04-06 구성 준비, 04-07 login credential 인증과 Bearer filter/SecurityContext 연결, 04-14 인증 email 소비, 04-17~20 role UI·parameter와 Order 업무 흐름이다.
- **교안:** P04 JWT 이론과 P08 Security 설명은 R06·R07 및 고도화 Summary에 필요한 내용이 전사되어 있어 이 페이지의 직접 source로 중복 추가하지 않았다.
- **Passwordless 직접 범위:** 05-19는 인증·인가 용어와 AAM/APE 조직 관리, 05-20은 FilingBox의 RO/RW/AO/WORM storage operation을 다룬다. X1280의 QR·앱 승인·외부 인증 서버 상세는 [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]에서 비교하며 FrontEnd_BackEnd 구현으로 소급하지 않는다.
- **Linux·AWS·CI/CD·중간 프로젝트:** 실행·배포·운영 또는 적용 설계 단계다. 그곳의 보안 설정을 04-07 endpoint 인가 완료로 되돌려 쓰지 않는다.

## 관련 페이지

- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 Cookie·Session·JWT 이론과 로그인 토큰 생성]]
- [[summaries/2026-04-07-member-api-string-token|2026-04-07 Bearer token과 Spring Security JWT 인증 흐름]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- [[entities/jwt|JWT]]
- [[queries/jwt-role-ui-vs-server-authorization|JWT role UI와 서버 인가는 왜 다른가]]
- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19 인증 기본과 AAM/APE 통합 설치]]
- [[entities/aam-ape|AAM과 APE]]
- [[summaries/2026-05-20-filingbox-giga-mega|2026-05-20 FilingBox GIGA/MEGA와 WORM]]
- [[concepts/nas-worm-storage-protection|NAS·WORM 저장소 보호]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md` — 후속 용어 학습 경계
- `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md` — storage operation 정책 경계
