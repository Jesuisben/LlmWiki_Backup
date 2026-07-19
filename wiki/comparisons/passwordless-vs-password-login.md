---
title: Passwordless 로그인 vs 비밀번호 로그인
created: 2026-07-03
updated: 2026-07-19
type: comparison
tags: [auth, project, spring-boot]
sources:
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless 로그인 vs 비밀번호 로그인

## 비교 목적

FrontEnd_BackEnd 수업에서 직접 구현한 **email/password→`AuthenticationManager`→JWT** 로그인을 기준선으로 두고, 후속 Passwordless 과목의 **QR 등록·모바일 앱 승인·외부 X1280 인증 서버** 흐름과 책임을 비교한다. “비밀번호를 입력하느냐”만 보지 않고 credential 입력 위치, 승인 주체, token 발급·검증, frontend/backend 책임, 직접 구현 범위를 나눈다.

## 처음 비교가 필요해진 날짜와 이후 확장

| 날짜 | 비교 이력 | 확인된 범위 |
|---|---|---|
| [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06]] | 비밀번호 로그인 화면·JWT provider와 client 저장/전달을 준비 | `LoginPage`, `LoginDto`, `JwtTokenProvider`, localStorage |
| [[summaries/2026-04-07-member-api-string-token|2026-04-07]] | credential 인증→JWT 발급과 후속 Bearer 검증을 실제 연결 | `AuthenticationManager`, `MemberDetailsService`, login Controller, JWT filter |
| [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14]] | 비밀번호 입력 탈취 위험과 X1280 앱 승인 개념을 학습 | Passwordless 보안 배경·개념 |
| [[summaries/2026-05-15-passwordless-x1280-docker-service|2026-05-15]] | Members 서비스 등록과 Docker 세 server·WordPress를 준비하고 QR 등록·앱 승인 절차를 진행 | 일부 상태·plugin 성공 관찰, 개별 인증 응답 미보존 |
| [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|2026-05-18]] | 외부 인증 서버·MariaDB·Spring 샘플에서 등록/로그인/해제를 관찰 | 수업 메모의 관찰 서술, 단계별 API 응답·화면 미보존 |
| [[summaries/2026-05-21-passwordless-x1280-rest-api|2026-05-21]] | Postman으로 등록 상태 조회 API 계약을 분리 확인 | 당일 등록 상태 조회 응답 1건; 나머지 기능은 교육 예시 또는 미보존 |
| [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 가이드]] | 기존 React/Spring 로그인에 REST client·DTO·Service·Controller·SecurityConfig를 붙이는 적용 설계 | 후속 프로젝트 설계이며 4과목 직접 구현이 아님 |

## 한눈에 보기

| 항목 | 비밀번호 로그인 | Passwordless X1280 로그인 |
|---|---|---|
| 사용자 credential 입력 | React에 email·password 입력 | 서비스 계정 식별 뒤 QR 등록 또는 앱 승인 흐름 사용; 브라우저 비밀번호 입력을 줄임 |
| 인증 판단 주체 | Spring Security와 회원 DB의 password 정보 | 외부 X1280 인증 서버와 모바일 앱 승인 결과를 서비스가 해석 |
| 서비스 사전 준비 | 프로젝트 Spring/MySQL 중심 | Members의 서비스 등록, 역할별 server·연결 설정이 먼저 필요 |
| 사용자·인증기 등록 | 회원 DB row가 있어도 별도 인증기 등록 단계는 없음 | X1280 사용자 등록 여부와 QR을 통한 모바일 인증기 연결을 구분 |
| frontend 책임 | 입력 state→login POST→JWT/user 저장→후속 Bearer 전달 | 등록 필요·QR·승인 대기·성공/실패·해제 같은 다단계 상태 표시 |
| backend 책임 | `AuthenticationManager`·`MemberDetailsService`로 credential 확인→JWT 발급 | X1280 REST client·응답 DTO·Service 조립→승인 결과를 서비스 로그인에 연결 |
| 외부 시스템 의존 | 수업 구현은 프로젝트 Spring/MySQL 중심 | X1280 Auth Server·서비스 등록 정보·모바일 앱·연결 설정 필요 |
| token 관계 | 로그인 성공 뒤 프로젝트 JWT 발급, 후속 filter 검증 | X1280 승인 결과가 곧 프로젝트 JWT라는 근거는 없음; 적용 설계에서 기존 로그인 상태와 연결 필요 |
| 대표 위험·실패 | 피싱·재사용·입력 탈취, credential 불일치 | 등록/승인 상태 오해, 외부 서버·앱·연동 설정 실패, 연동 credential 노출 |
| 직접 구현 범위 | 04-06 준비, 04-07 login/filter/SecurityContext 직접 연결 | 05-14 개념, 05-15 구성·등록 절차, 05-18 샘플 관찰, 05-21 등록 상태 조회 응답 1건; 전체 React/Spring 통합은 후속 가이드 |

## 언제 무엇을 쓰는가

### 상황 1 — FrontEnd_BackEnd의 직접 로그인 기준선을 설명할 때

사용자는 LoginPage에 email·password를 입력했다. Spring Controller는 이를 `AuthenticationManager`에 전달했고 `MemberDetailsService`가 회원 정보를 제공했다. 성공 뒤 JWT와 id·name·email·role을 응답했으며, React는 token과 user를 나눠 저장했다. 후속 요청은 Bearer JWT를 filter가 검증해 `Authentication`을 만들었다. 이 흐름은 비밀번호 credential 확인과 JWT 기반 후속 요청 인증을 함께 사용한 직접 구현이다.

### 상황 2 — 브라우저 비밀번호 입력을 앱 승인으로 이동할 때

후속 X1280 수업에서는 서비스 등록, 인증 서버, 모바일 앱, QR 등록, 앱 승인, 등록 해제와 REST 응답 확인이 등장했다. Passwordless는 단지 password 필드를 삭제하는 것이 아니라 **승인 주체와 신뢰 경로를 외부 인증 서버·앱까지 확장하는 선택**이다.

### 상황 3 — 기존 프로젝트에 Passwordless를 붙일 때

중간 프로젝트 가이드는 외부 인증 서버 설정, REST client, DTO, Service, Controller, SecurityConfig, React 상태 연결을 제안한다. 이때 X1280 승인 성공을 기존 서비스의 로그인 상태·JWT/세션과 어떻게 연결할지 별도로 설계해야 한다. 단계 9 raw의 결과 확인 방식은 React polling이며 외부 인증 server→Spring callback은 없다. 또한 승인 상태뿐 아니라 요청·응답 사용자, hash/random, server-side challenge/session 소유권과 만료를 검증한 뒤 서비스 로그인 상태를 만들어야 한다. 이 전체 설계를 04-06~07 또는 05-18 날짜 수업의 직접 구현으로 소급하지 않는다.

## 대표 artifact의 입력 → 처리 → 결과

| 방식 | 입력 | 처리 | 결과·근거 수준 |
|---|---|---|---|
| 비밀번호 login | email·password | `AuthenticationManager`→회원/password 확인→JWT 생성 | accessToken·사용자 정보 응답 |
| 비밀번호 login 후 요청 | Bearer JWT | filter 검증→email/role→Authentication/SecurityContext | 인증된 요청으로 Controller 진행 |
| Passwordless 등록 | 사용자 식별·등록 요청 | 서비스/샘플→X1280 서버→QR로 앱·계정 연결 | 등록된 인증기 상태 |
| Passwordless login | 사용자 식별·승인 요청 | X1280 서버가 앱 승인 흐름을 중개하고 결과 제공 | 서비스가 승인 결과를 해석해야 함 |
| 프로젝트 통합 | 승인 상태·외부 API 응답 | REST client·DTO·Service·Controller·SecurityConfig와 frontend 상태 연결 | 기존 서비스 로그인 상태와 연결하는 단계 9 설계 산출물—단계 8 실행 결과 아님 |

## 함께 사용할 수 있는 관계

두 방식은 개념상 비교되지만 반드시 서로 배타적인 배치라고 단정할 수 없다. 다만 이 Vault의 확인 범위에서는 04-06~07 비밀번호/JWT 로그인은 직접 구현됐고, 05월 X1280은 별도 후속 과목과 샘플·API 실습으로 다뤄졌다. 병행 로그인·완전 대체·2차 인증 중 무엇을 채택했는지는 원본에 확정된 운영 정책이 없으므로 프로젝트 선택지로만 본다.

## 확인된 구현 범위와 실행 미확정 범위

### 확인됨

- 비밀번호 흐름: LoginPage 입력, Spring credential 인증, JWT 발급, localStorage 저장, Bearer 전달, filter 검증, logout 삭제.
- Passwordless 흐름: 05-14 개념, 05-15 서비스·server 구성과 등록 절차, 05-18 Spring 샘플의 등록·로그인·해제 관찰, 05-21 등록 상태 조회 JSON 응답 1건.
- 중간 프로젝트 가이드: REST client·DTO·Service·Controller·SecurityConfig·React 연결의 적용 절차가 문서화됨.

### 완료로 단정할 수 없음

- FrontEnd_BackEnd 프로젝트에서 X1280을 직접 구현했다는 근거는 없다.
- 05-21 등록 상태 조회 API 응답 1건만으로 프로젝트 login이 완성된 것은 아니다.
- X1280 승인 결과가 자동으로 FrontEnd_BackEnd JWT를 발급한다는 근거는 없다.
- React polling의 timeout·중단·오류/대기 구분과 승인 결과의 사용자·challenge/session 결속이 runtime에서 검증됐다는 근거는 없다.
- 병행/대체/2차 인증 중 실제 최종 정책과 전체 runtime 검증 결과는 이번 범위에서 확정하지 않는다.

## 헷갈리기 쉬운 포인트

- **Passwordless=인증 없음:** 인증은 남고 credential 확인 경로가 바뀐다.
- **차이는 password 필드 유무뿐:** 승인 주체·외부 서버·앱·상태 처리·실패 지점이 달라진다.
- **QR=매번 로그인:** 수업에서는 주로 계정과 앱/인증기를 연결하는 등록 단계다.
- **앱 승인=X1280 결과=프로젝트 JWT:** 외부 승인 결과와 서비스 token 발급·세션 생성은 연결 설계가 필요하다.
- **polling=callback:** 단계 9 raw에는 React가 결과를 주기적으로 조회하는 구현안만 있고, 외부 인증 server가 Spring으로 결과를 밀어 주는 callback 구현은 없다. 두 전달 방식을 이 프로젝트의 대칭적인 완료 결과로 비교하지 않는다.
- **Postman 성공=Spring/React 통합 완료:** API 계약 한 단계만 확인한 것이다.
- **serverKey=사용자 password:** 이는 서비스 서버와 인증 서버 연동 credential이며 별도 비밀 관리 대상이다.
- **05-18 샘플 동작=모든 Passwordless 제품 규칙:** 해당 샘플에서 등록 해제 뒤 비밀번호 로그인 복귀를 관찰했을 뿐 일반화하지 않는다.

## 잘못된 동일시와 올바른 판단 기준

| 잘못된 동일시 | 올바른 판단 기준 |
|---|---|
| password input이 없다 → 인증도 없다 | 누가 어떤 증거·승인 결과로 사용자를 확인하는가 |
| QR을 봤다 → login 성공 | 등록 완료인지, 승인 요청인지, 서비스 로그인 연결까지 됐는지 나눠 확인 |
| 외부 인증 성공 → endpoint 인가 완료 | 프로젝트가 로그인 상태를 만들고 별도 authorization 정책을 적용했는가 |
| REST API 호출 성공 → 전체 기능 완료 | frontend 상태·backend 조립·SecurityConfig·runtime 시나리오가 연결됐는가 |

## 선행 개념과 후속 기능 연결

- 기준선 token 생명주기: [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- credential login과 Bearer 검증: [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]
- X1280 구성요소·등록·승인: [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- QR·앱 상태: [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- 프로젝트 backend 연결: [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- 인증 뒤 권한 분리: [[comparisons/authentication-vs-authorization|인증 vs 인가]]

## 직접 수업·교안·후속 과목 경계

- **FrontEnd_BackEnd 직접 수업:** 04-06~07 email/password→AuthenticationManager→JWT→Bearer filter/SecurityContext다.
- **P04 JWT 교안:** 필요한 JWT 이론은 R06·R07과 고도화 Summary에 전사되어 있어 직접 source로 중복 추가하지 않았다.
- **Passwordless 직접 수업:** 05-14 개념, 05-15 서비스·Docker·등록 절차, 05-18 서버·샘플 관찰, 05-21 등록 상태 조회 응답 1건이다. 이 페이지는 당일 미보존 API·화면 결과를 성공으로 확대하지 않는다.
- **중간 프로젝트:** 실제 프로젝트 적용을 위한 후속 가이드다. FrontEnd_BackEnd 직접 구현이나 Passwordless 날짜 수업의 완료 결과로 소급하지 않는다.
- **Linux·AWS·CI/CD:** 외부 인증 서버와 애플리케이션을 실행·배포하는 환경이지만 두 인증 방식의 credential 책임 자체와 같은 층위는 아니다.

## 관련 페이지

- [[summaries/2026-04-06-login-jwt-session-cookie|2026-04-06 Cookie·Session·JWT 이론과 로그인 토큰 생성]]
- [[summaries/2026-04-07-member-api-string-token|2026-04-07 Bearer token과 Spring Security JWT 인증 흐름]]
- [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14 Passwordless X1280 소개와 보안 배경]]
- [[summaries/2026-05-15-passwordless-x1280-docker-service|2026-05-15 Passwordless X1280 Docker 통합 서버와 서비스 등록]]
- [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|2026-05-18 Passwordless 서버와 Spring 샘플 연동]]
- [[summaries/2026-05-21-passwordless-x1280-rest-api|2026-05-21 Passwordless X1280 REST API와 Postman]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]

## 출처

- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md` — 후속 프로젝트 적용 설계
