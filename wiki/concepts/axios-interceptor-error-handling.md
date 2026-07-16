---
title: Axios interceptor와 API 오류 처리
created: 2026-07-06
updated: 2026-07-16
type: concept
tags: [react, typescript, frontend, auth]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md
status: growing
confidence: high
---

# Axios interceptor와 API 오류 처리

## 정의

이 수업에서 Axios interceptor는 **React의 여러 API 요청에 공통 설정을 적용하고, 로그인 요청이 아닌 응답에서 401이 발생하면 공통으로 인증 실패를 처리하는 통신 경계**다. 반면 회원가입·상품 등록/수정의 필드별 Validation 오류는 각 form이 자신의 오류 state로 받아 표시했다. 두 처리를 분리해야 인증 실패와 잘못된 입력을 같은 오류로 취급하지 않는다.

## 왜 중요한가

04-06 이후 한 React 앱이 Member 로그인뿐 아니라 Product 조회·관리, Cart 추가·수량·삭제, Order 생성·조회·상태 변경 요청을 계속 보낸다. 각 화면이 토큰 조회와 Bearer header 구성을 반복하는 대신 `axiosInstance.tsx`가 공통 요청 설정을 맡으면 화면은 자기 기능에 집중할 수 있다. 동시에 필드 오류까지 interceptor가 모두 소비하지 않게 해야 사용자가 어느 입력을 고쳐야 하는지 form에서 확인할 수 있다.

## 이 수업에서 등장하고 확장된 날짜

| 날짜 | 실제 확장 | 대표 artifact |
|---|---|---|
| [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06]] | 공통 axios instance, request/response interceptor, LoginPage의 token 저장을 준비 | `axiosInstance.tsx`, `LoginPage.tsx`, `LoginResponse` |
| [[summaries/2026-04-07-member-api-string-token|2026-04-07]] | Bearer 문자열을 Spring filter가 해석하고 로그인·로그아웃을 실제 API와 연결 | `JwtAuthenticationFilter`, `MemberController.login()`, `handleLogout()` |
| [[summaries/2026-04-09-product-delete-routing-jsx-table|2026-04-09]]~[[summaries/2026-04-13-product-detail-useeffect-service|04-13]] | Product 목록·삭제·등록·수정·상세 요청에서 공통 instance를 사용하고, 등록/수정 오류는 form state에 남김 | `ProductList`, `ProductInsertForm`, `ProductUpdateForm`, `ProductDetail` |
| [[summaries/2026-04-14-cart-service|2026-04-14]]~[[summaries/2026-04-16-cart-quantity-stock|04-16]] | 인증 사용자의 Cart 추가·목록·수량·삭제와 선택 품목 Order 요청에 공통 통신 경계를 재사용 | `CartList`, `CartController`, `OrderController` |

## 공통 요청과 401 처리

### 요청 전

`axiosInstance.tsx`는 `localStorage`의 `accessToken`을 확인한다. token이 있으면 요청 설정의 `Authorization` header에 `Bearer ` 접두어와 함께 붙인다. 04-07의 Spring `JwtAuthenticationFilter`는 같은 header에서 접두어를 확인·제거하고 JWT를 검증해 인증 객체를 `SecurityContextHolder`에 넣는다.

이 연결에서 React axios 요청 함수와 Spring Service는 같은 계층이 아니다.

- React의 요청 함수는 URL·method·parameter/body를 만들고 브라우저 state를 갱신한다.
- interceptor는 그 HTTP 요청 설정과 공통 인증 실패를 가로챈다.
- Spring filter는 Controller 전에 Bearer token을 인증 정보로 바꾼다.
- Controller·Service·Repository는 인증을 통과한 뒤 각 Member·Product·Cart·Order use case를 처리한다.

### 응답 후

응답 interceptor는 status가 401인지와 요청 URL이 로그인 요청인지 함께 확인한다. 로그인 요청 자체의 실패까지 다시 로그인 화면으로 보내는 반복을 피하고, **로그인 요청이 아닌 401**에서 `accessToken`을 지우고 로그인 화면으로 이동한다. 수동 로그아웃에서는 React가 user와 token을 직접 제거한 뒤 로그인 화면으로 이동한다.

## Member·Product·Cart·Order에서의 실제 역할

| 기능 | 화면이 맡는 일 | interceptor가 맡는 일 | Spring 쪽 처리 |
|---|---|---|---|
| Member login | email·password POST, 성공 응답의 `accessToken`과 user 분리·저장, 실패 message 표시 | 로그인 요청은 공통 401 redirect 대상에서 제외 | `AuthenticationManager` 인증→Member 조회→JWT·회원 정보 응답 |
| Product | 목록/상세 GET, 관리자 삭제, 등록 POST, 수정 PUT과 화면 state 갱신 | `customAxios` 요청에만 공통 설정을 적용. 04-09 삭제는 일반 `axios.delete`라 interceptor 적용을 귀속할 수 없음 | Product Controller→Service→Repository, form 요청에는 Validation과 image 저장 처리 |
| Cart | 로그인 사용자 조건에서 추가·목록·수량·삭제 요청 | 저장된 token을 공통 header에 첨부 | 인증 객체의 email로 사용자 Cart를 찾고 CartProduct를 처리 |
| Order | 선택 Cart 품목 또는 상세 상품을 POST하고 역할별 목록·완료·취소 요청 | 보호 API 요청의 공통 인증 설정과 401 처리 | 주문 생성·재고 차감·Cart 삭제, 역할별 PENDING 조회와 상태 처리 |

Product 목록은 공개 경로로 확인한 시점도 있고, 04-09 `ProductList`는 `customAxios`와 일반 `axios`를 함께 import해 목록은 전자, 삭제는 후자의 `delete`를 사용했다. 따라서 “Product 요청”이라는 도메인 이름만으로 token 첨부·공통 401 처리가 모두 적용됐다고 단정하지 않는다. 화면에서 role에 따라 관리 버튼을 숨긴 것과 백엔드 인가 정책의 완성도도 별개다.

## 입력 → 처리 → 결과

| 입력 | 처리 | 결과 |
|---|---|---|
| 로그인 성공 응답의 user 필드와 `accessToken` | LoginPage가 둘을 분리해 localStorage에 저장 | 다음 요청에서 공통 token을 사용할 준비 |
| Product·Cart·Order의 `customAxios` 요청 | request interceptor가 token 확인→Bearer header 설정 | Spring Security filter가 읽을 Authorization 요청 |
| 로그인 요청이 아닌 API의 401 | response interceptor가 token 삭제→로그인 화면 이동 | 만료·잘못된 인증을 공통 종료 |
| Signup의 잘못된 필드·중복 email | Spring `@Valid`·`BindingResult`가 필드 map 자체를 400 body로 반환→SignupPage가 오류 state에 반영 | 각 회원 control의 invalid feedback |
| Product form의 잘못된 필드·처리 예외 | Spring `@Valid`·`BindingResult`·`FieldError`가 `{message, errors}` 형태의 400 body 또는 처리별 오류를 반환→form이 오류 state에 반영 | 상품 field feedback 또는 general 오류 표시 |

## 전역 인증 오류와 필드 Validation 오류의 경계

| 구분 | 공통 interceptor | 화면별 form state |
|---|---|---|
| 중심 질문 | 이 요청을 인증된 사용자 요청으로 계속 처리할 수 있는가 | 사용자가 어느 입력을 고쳐야 하는가 |
| 수업 사례 | 로그인 외 API의 401, token 제거와 로그인 이동 | SignupPage의 회원 필드, ProductInsertForm/ProductUpdateForm의 상품 필드와 general message |
| 데이터 | HTTP status·request URL·localStorage token | Signup은 field map 자체, Product는 `{message, errors}`의 중첩 shape |
| 결과 | 인증 흐름 종료·재로그인 유도 | form 유지·필드별 feedback 표시 |

04-10 Product form에서 React는 서버의 `errors`와 `message`를 오류 state에 합쳤다. 이 오류를 interceptor가 모두 로그인 문제로 바꾸면 field 이름과 화면 control의 연결이 사라진다. 반대로 401을 각 form의 필드 오류로 넣으면 token 문제를 사용자가 상품명이나 가격 입력 문제로 오해하게 된다.

수업의 실제 status도 한 종류가 아니다. 04-07 회원가입 Validation·이메일 중복과 04-10/04-13 Product Validation은 400, 인증 실패는 401, 04-13 상품 없음은 404, 상품 image/저장 예외는 500으로 응답했다. interceptor의 공통 분기와 form/detail의 local catch가 서로 다른 status/body를 이어서 처리했으며, 04-13 `ProductDetail`에는 `customAxios`를 쓰면서도 local catch에서 401을 다시 확인하는 중복도 남아 있었다.

## 자주 헷갈리는 원인

- **401과 모든 4xx를 같은 오류로 보는 경우:** 수업의 공통 분기는 401 인증 실패다. Product Validation은 `BindingResult`의 필드 오류 map을 form이 처리한다.
- **Bearer token을 Service가 붙인다고 생각하는 경우:** header는 React request interceptor가 구성하고 Spring filter가 해석한다. ProductService·CartService·OrderService는 HTTP client가 아니다.
- **로그인 실패와 만료된 후속 요청을 합치는 경우:** 로그인 POST 실패는 LoginPage의 message로 남기고, 로그인 외 요청의 401만 공통 redirect 대상으로 삼았다.
- **optional chaining을 오류 처리 정책으로 보는 경우:** `?.`는 중간 값이 없을 때 안전하게 읽는 TypeScript 문법일 뿐, 어떤 오류를 전역/지역에서 맡을지는 별도 설계다.
- **버튼 숨김을 인가 완료로 보는 경우:** role 기반 조건부 렌더링은 UI 제어다. 실제 보호 API의 서버 인가와 동일하다고 확대하지 않는다.
- **모든 axios 호출이 interceptor를 지난다고 보는 경우:** 공통 instance를 import한 파일도 일반 `axios`를 따로 사용할 수 있다. 04-09 Product 삭제가 실제 예다.

## 이전 개념과 이후 기능 연결

- 선행: [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]이 token 기반 인증 방식을 설명하고, [[concepts/react-form-state-event|React 폼 상태와 이벤트]]가 local form/error state를 맡는다.
- 통신·계층 경계: [[concepts/frontend-backend-architecture|Frontend/Backend 구조]]에서 axios→Controller→Service→Repository 왕복을 확인한다.
- 후속 기능: [[concepts/product-domain-flow|상품 도메인 기능 흐름]], [[concepts/shopping-cart-flow|장바구니 기능 흐름]], [[concepts/order-flow|주문 기능 흐름]]이 공통 통신 경계를 사용하지만 각 도메인의 업무 책임은 해당 페이지가 설명한다.
- 인증 backend: [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]는 header 이후의 token 검증·SecurityContext 구성을 맡는다.

## 직접 수업·교안·후속 확장 경계

- **직접 수업:** 04-06 `axiosInstance`·LoginPage, 04-07 Bearer filter·login/logout, 04-09~04-16 Product/Cart/Order 요청과 Product field Validation 오류 표시다.
- **교안 보충:** HTTP status·REST·CORS·React event/axios·Spring Security/Validation 용어는 P03·P07·P08에서 보충됐지만, 필요한 구현은 날짜 MD와 Summary에 충분히 전사되어 있어 PDF를 별도 source로 추가하지 않았다.
- **R19 범위:** 총정리 원본은 axios/Member/Product/Cart를 복습하지만 실제 본문이 04-15 Cart 삭제에서 끝난다. 04-16 이후 Order 생성·상태 처리·검색을 R19 내용으로 소급하지 않는다.
- **후속 과목:** Linux·AWS·CI/CD는 실행·배포·운영 설정, Passwordless는 다른 인증 방식, 중간 프로젝트는 실제 적용 단계다. 운영 refresh token·전역 재시도 정책까지 이 수업에서 구현했다고 확대하지 않는다.

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.09(목)/2026.04.09(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.10(금)/2026.04.10(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.13(월)/2026.04.13(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.14(화)/2026.04.14(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.16(목)/2026.04.16(목).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.17(금)/2026.04.17(금).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.20(월)/2026.04.20(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/FrontEnd_BackEnd 총정리/FrontEnd_BackEnd 총정리.md` — 04-15 Cart 삭제까지의 복습 범위
