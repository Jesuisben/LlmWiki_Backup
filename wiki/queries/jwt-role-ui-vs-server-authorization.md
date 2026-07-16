---
title: JWT role UI와 서버 인가는 왜 다른가
created: 2026-07-16
updated: 2026-07-16
type: query
tags: [auth, react, spring-boot, frontend, backend]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
status: growing
confidence: high
---

# JWT role UI와 서버 인가는 왜 다른가

## 질문

React에서 `user.role`에 따라 메뉴·버튼을 숨기고 JWT에 role Claim을 넣은 뒤 Spring filter가 `GrantedAuthority`와 `Authentication`을 만들었다면, 관리자 기능의 서버 인가도 완성된 것인가?

## 짧은 답

아니다. **React UI 분기, localStorage의 user role, JWT role Claim, Spring `GrantedAuthority`, SecurityContext의 `Authentication`, endpoint authorization은 서로 다른 계층**이다. 04-07 원본에서는 공개 URL과 `anyRequest().authenticated()`가 확인되지만 endpoint별 `hasRole(...)` 정책은 확인되지 않는다. 04-17~20의 주문 기능도 client role/memberId와 role별 버튼은 확인되지만, 서버가 JWT authority·주문 소유자를 대조하는 코드는 확인되지 않는다.

## 실제 수업에서 질문이 필요해진 날짜와 확장 날짜

| 날짜 | 왜 질문이 생겼는가 | 확인된 artifact |
|---|---|---|
| [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06]] | login 응답의 role을 user object로 저장하고 메뉴를 ADMIN·USER로 분기했으며 JWT에도 role Claim을 넣었다. | `LoginResponse`, localStorage `user`, `MenuItems.renderMenu`, `JwtTokenProvider` |
| [[summaries/2026-04-07-member-api-string-token|2026-04-07]] | filter가 Claim을 `ROLE_...` authority로 바꿔 Authentication/SecurityContext를 구성했다. | `JwtAuthenticationFilter`, `SimpleGrantedAuthority`, `SecurityContextHolder`, `SecurityConfig` |
| [[summaries/2026-04-17-cart-total-array-some|2026-04-17]] | Order 목록 요청이 client의 memberId·role parameter로 조회 범위를 나눴다. | `OrderList`, `getOrderListByRole`, role별 Repository 조회 |
| [[summaries/2026-04-20-order-list-scenario|2026-04-20]] | ADMIN/USER별 완료·취소 버튼과 API가 연결됐지만 서버 role·소유자 검사 여부가 별도 문제로 남았다. | `makeStatusButton`, 완료 PUT, 취소 DELETE |

## 근거 artifact와 입력 → 처리 → 결과

| 계층 | 입력 | 처리 | 결과 |
|---|---|---|---|
| React role UI | login 응답에서 저장한 `user.role` | 메뉴·버튼을 조건부 렌더링 | 사용자에게 보이는 기능이 달라짐 |
| client user 저장 | login 응답의 id·name·email·role | token과 분리해 localStorage/user state에 저장 | 화면·request parameter 구성에 사용 |
| JWT role Claim | 로그인 성공 Member의 role | `JwtTokenProvider`가 token Claim에 포함 | 서명된 token 내부의 권한 정보 재료 |
| Spring authority | 유효 JWT의 role Claim | filter가 `ROLE_` prefix를 붙여 `GrantedAuthority` 생성 | Authentication의 authorities에 포함 |
| SecurityContext | email + authorities | `UsernamePasswordAuthenticationToken` 생성·저장 | 현재 요청의 인증 principal·authority |
| URL 인증 정책 | 요청 URL과 현재 Authentication | 공개 URL은 `permitAll`, 나머지는 `authenticated` | 인증 유무 기준의 접근 판단 |
| endpoint role·소유자 인가 | authority, principal, 요청 자원 | 원본에서 구체 role/ownership 검사 확인 필요 | 확인되지 않으면 서버 인가 완료로 단정 불가 |

## 자세한 설명

### 1. React role UI는 사용자 경험 계층이다

04-06 `MenuItems`는 `user?.role`을 보고 ADMIN에는 상품 등록·주문 내역, USER에는 장바구니·주문 내역을 보였다. 04-20 `OrderList`도 ADMIN에 완료·취소, USER에 취소 버튼을 렌더링했다. 이는 사용자가 실수로 맞지 않는 기능을 누르지 않게 하는 UI 규칙이다.

하지만 browser code와 localStorage 값은 사용자가 관찰·변경하거나 UI를 거치지 않고 API를 직접 호출할 수 있는 영역이다. 따라서 버튼을 숨겼다는 사실은 server가 요청을 거부한다는 증거가 아니다.

### 2. localStorage user.role은 화면용 client 상태다

로그인 응답에서 `accessToken`과 나머지 userData를 분리해 각각 저장했다. user object의 role은 메뉴·route·request parameter를 만드는 데 사용됐고, accessToken은 Authorization header에 붙었다. 둘은 같은 응답에서 왔어도 동일 객체나 동일 보안 경계가 아니다.

### 3. JWT role Claim은 서명 token의 데이터다

04-06 `JwtTokenProvider`는 Member role을 Claim에 넣었다. role Claim이 있다는 것은 server가 발급한 token 안에 역할 정보가 포함됐다는 뜻이다. 그러나 Claim 자체가 “이 endpoint는 ADMIN만”이라는 정책을 선언하지는 않는다.

### 4. GrantedAuthority는 Spring이 판단에 사용할 표현이다

04-07 filter는 유효 token에서 role을 읽고 `ROLE_` prefix를 붙인 `SimpleGrantedAuthority`를 만들었다. 이것을 email과 함께 `UsernamePasswordAuthenticationToken`에 넣었다. 이 단계에서 Spring Security는 현재 요청의 사용자와 authority를 알 수 있다.

그러나 authority를 **만드는 일**과 endpoint에서 authority를 **검사하는 일**은 다르다. 확인된 SecurityConfig는 공개 URL을 `permitAll()`로 두고 나머지를 `authenticated()`로 요구했다. 지정 원본에는 endpoint별 `hasRole(...)`가 없다.

### 5. SecurityContext의 Authentication은 현재 요청의 인증 문맥이다

`SecurityContextHolder`는 filter가 만든 Authentication을 현재 요청 처리 동안 보관한다. Cart Controller는 이 객체의 이름(email)을 사용해 실제 회원 Cart를 찾았다. 이처럼 Controller/Service가 principal을 소비할 수 있지만, SecurityContext가 존재한다는 사실만으로 모든 자원 소유자·role 규칙이 자동 적용되지는 않는다.

### 6. Order의 client role/memberId는 서버 신뢰 근거와 다르다

04-17 Order 목록 Controller는 request parameter의 memberId·role을 받고 Service가 role에 따라 전체/본인 조회를 골랐다. 04-20 완료·취소 Controller/Service에는 ADMIN 또는 주문 당사자인지 다시 검사하는 코드가 확인되지 않는다. UI 시나리오상 역할은 나뉘었지만, client가 보낸 값을 JWT principal·authority와 대조하는 서버 보안 경계는 별도다.

## 확인된 구현과 실행 미확정 범위

### 확인됨

- 04-06 login 응답의 user.role 저장, role별 메뉴, JWT role Claim 작성.
- 04-07 Bearer token 검증, Claim→GrantedAuthority, Authentication→SecurityContext 저장.
- 04-07 공개 URL `permitAll()`과 나머지 `authenticated()` 정책.
- 04-17 client memberId·role 기반 Order 목록 요청과 Service 분기.
- 04-20 role별 버튼 및 완료·취소 요청·업무 처리.

### 확인되지 않음

- 04-07 SecurityConfig의 endpoint별 ADMIN/USER `hasRole(...)` 규칙.
- Order 목록의 memberId·role을 JWT principal·authority와 대조하는 로직.
- 완료 endpoint가 ADMIN인지 확인하는 서버측 role 검사.
- 취소 endpoint가 ADMIN 또는 해당 Order 소유자인지 확인하는 서버측 ownership 검사.
- 위 미확정 사항의 runtime 우회 호출 테스트 결과.

## 복잡한 오해를 단계별로 해소하기

1. **버튼이 보이는가?** React UI 조건이다.
2. **client가 어떤 role을 들고 있는가?** localStorage/user state다.
3. **token에 어떤 role이 서명돼 있는가?** JWT Claim이다.
4. **Spring이 어떤 authority를 만들었는가?** Authentication의 권한 표현이다.
5. **현재 요청에 Authentication이 있는가?** SecurityContext의 인증 상태다.
6. **요청 endpoint가 그 authority를 실제 검사하는가?** 서버 authorization 정책이다.
7. **요청 자원이 현재 principal 소유인가?** role과 별도로 필요한 ownership 인가다.

앞 단계가 존재한다고 다음 단계가 자동으로 완성되지 않는다.

## 잘못된 동일시와 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| `user.role === 'ADMIN'` → 관리자 보안 완성 | 서버 endpoint가 authority를 검사하는가 |
| localStorage role → 신뢰 가능한 권한 | 서명 token과 서버 인증 문맥에서 나온 authority인가 |
| JWT role Claim → 접근 허용 | SecurityConfig/method/Service가 해당 Claim 기반 authority를 실제 검사하는가 |
| GrantedAuthority 생성 → 모든 API 인가 | endpoint별 규칙과 자원 소유자 검사가 존재하는가 |
| SecurityContext 존재 → 관리자 | authenticated user인지와 필요한 role은 별도인가 |
| memberId·role parameter → 요청자 신원 | JWT principal과 대조해 위조 가능한 client 값을 배제하는가 |
| UI에서 취소 버튼 표시 → 본인 주문만 취소 가능 | 서버가 Order.member와 현재 principal을 비교하는가 |

## 참고한 위키 페이지

- Summary: [[summaries/2026-04-06-login-jwt-session-cookie|04-06]], [[summaries/2026-04-07-member-api-string-token|04-07]], [[summaries/2026-04-17-cart-total-array-some|04-17]], [[summaries/2026-04-20-order-list-scenario|04-20]]
- Concept: [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]], [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]], [[concepts/order-flow|주문 기능 흐름]]
- Comparison: [[comparisons/authentication-vs-authorization|인증 vs 인가]], [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]
- Entity: [[entities/jwt|JWT]], [[entities/react|React]], [[entities/spring-boot|Spring Boot]]

## 후속 과목과 직접 수업의 경계

- 직접 범위는 04-06~07의 login/JWT/Security 연결과 04-17~20의 Order role UI/API다.
- P04 JWT 이론은 R06·R07과 고도화 Summary에 필요한 내용이 전사되어 있어 이 페이지 source에 중복 추가하지 않았다.
- Passwordless는 credential 인증 방식을 확장하지만 이 Order endpoint의 authorization 완료 근거가 아니다.
- Linux·AWS·CI/CD는 배포·운영 환경이며, 중간 프로젝트의 후속 보안 설계를 4과목 직접 구현에 소급하지 않는다.

## 구체적인 raw sources

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`

## 다음에 볼 것

1. [[comparisons/authentication-vs-authorization|인증 vs 인가]]에서 credential 인증·Bearer 인증·endpoint 인가를 비교한다.
2. [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]에서 04-06 준비와 04-07 실제 연결을 추적한다.
3. [[concepts/order-flow|주문 기능 흐름]]에서 role별 목록·완료·취소의 확인 범위와 ownership 공백을 본다.
4. [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]에서 인증 방식이 바뀌어도 인가가 별도로 남는 이유를 연결한다.
