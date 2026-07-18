---
title: Spring Boot Passwordless 인증 연동
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [spring-boot, auth, backend, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Spring Boot Passwordless 인증 연동

## 정의

Spring Boot Passwordless 인증 연동은 Spring 계열 application이 X1280 REST API의 등록·인증·해제 상태를 호출·해석하고, 그 결과를 자체 회원 DB와 서비스 로그인 상태에 연결하는 작업이다.

## 왜 중요한가

X1280 server가 정상이어도 application 설정·DB·REST contract·로그인 상태 연결 중 하나가 맞지 않으면 사용자는 로그인할 수 없다. 따라서 “외부 API 호출 성공”과 “Spring 서비스 로그인 성공”을 단계별 완료 조건으로 나눠야 한다.

## 8과목에서 직접 확인한 구성

| 계층 | 05-18·05-21 직접 범위 | 확인 경계 |
|---|---|---|
| X1280 server | Docker server, 관리자 설정, REST 사용 준비 | 일부 status 출력·절차 보존 |
| local user DB | MariaDB `userinfo` table과 sample row | 연속 SQL·조회 결과 보존 |
| sample application | properties의 역할별 연결값, 로컬 실행, 등록·로그인·해제 화면 절차 | 수업 메모의 관찰 서술, 단계별 screenshot 없음 |
| application server | WAR 생성·Tomcat 배치·설정·재시작 | browser별 최종 응답 미보존 |
| REST contract | Postman 등록 여부 POST와 JSON response | 해당 response만 당일 직접 결과 |

## request/response를 application에 연결하는 판단 순서

1. Auth Server와 앱 연결 server가 실행 중인지 확인한다.
2. application이 올바른 역할의 base URL과 service credential을 읽는지 확인한다.
3. Postman에서 같은 환경의 API request가 response를 반환하는지 확인한다.
4. `result`·`code`·`msg`와 기능별 `data`를 분리해 해석한다.
5. local 회원 row와 X1280 사용자 등록 상태를 같은 것으로 취급하지 않는다.
6. 외부 인증 성공 뒤 application이 session/JWT 등 자체 로그인 상태를 만드는지 확인한다.
7. protected endpoint의 authorization은 별도로 검증한다.

## 원본 API 재고와 근거 수준

교육 collection은 등록 여부, 등록, 일회용 token, 인증 요청, 승인 결과, 취소, 해제의 7개 POST request를 정의한다. 완성형 collection에는 saved response example이 있지만 교육 입력자료다. 05-21 날짜 원본이 직접 보존한 실행 response는 등록 여부 확인 한 건이다. 따라서 나머지 request를 Spring sample이 모두 성공했다고 단정하지 않는다.

## 중간 프로젝트 후속 경계

DTO·REST client·Service·Controller·Member 상태·SecurityConfig·React polling/callback·JWT 연결은 단계 9 가이드가 제시한 확장 설계다. 8과목에서 sample application과 API contract를 학습한 근거는 되지만, 중간 프로젝트 source code를 직접 구현·실행했다는 근거는 아니다.

## 자주 헷갈리는 점

- 외부 server의 service credential은 사용자 password가 아니며 code·wiki·log에 실제 값을 남기지 않는다.
- WAR 생성은 build 결과이고 Tomcat 실행·HTTP 응답·로그인 성공과 다르다.
- Postman response 성공은 Spring serialization·service logic·session/JWT 발급 성공을 보장하지 않는다.
- 로그인 시작 endpoint와 결과 확인·해제 endpoint의 공개 범위는 같을 필요가 없다. 다만 구체 SecurityConfig는 단계 9 판단 대상이다.

## 관련 개념

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md` — 단계 9 후속 설계