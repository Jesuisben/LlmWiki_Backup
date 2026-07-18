---
title: Passwordless X1280 인증 흐름
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [auth, project, backend, frontend, spring-boot]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless X1280 인증 흐름

## 정의

Passwordless X1280 인증 흐름은 사용자가 서비스에 비밀번호를 직접 입력하는 대신, 서비스 애플리케이션·X1280 인증 서버·모바일 인증기가 등록과 승인 상태를 교환해 사용자를 확인하는 구조다.

## 왜 중요한가

FrontEnd_BackEnd 수업의 기존 로그인은 email/password를 검증하고 JWT를 발급·전달했다. X1280은 그보다 앞선 “사용자가 정말 계정 주인인가”를 외부 인증 서버와 모바일 승인으로 확인한다. 로그인 상태 유지와 endpoint 인가는 여전히 애플리케이션 책임이므로 [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]을 자동 대체한다고 보면 안 된다.

## 구성요소와 책임

| 구성요소 | 수업에서 확인한 책임 | 소유하지 않는 책임 |
|---|---|---|
| 사용자·브라우저 | 사용자 ID 입력, 등록·로그인·해제 시작 | 인증 결과의 최종 신뢰 판단 |
| 웹 애플리케이션 | 화면 제공, 사용자 DB와 외부 인증 결과 연결 | X1280 내부 인증기 상태 관리 |
| Auth Server | 서비스 정보와 등록·인증 요청 처리 | browser session/JWT의 자동 발급 |
| User Connection Server | 모바일 인증기 연결 경로 | 서비스 business authorization |
| Push Request Server | 앱 승인 요청 전달 경로 | 저장소의 RO/RW/WORM 정책 |
| 모바일 앱 | QR 등록, 요청 출처·내용 확인, 승인·거절 | 서비스 DB의 회원 row 관리 |

## 상태 전이

1. **등록 여부 확인:** 사용자에게 인증기가 연결돼 있는지 조회한다. 05-21의 `data.exist`는 이 상태다.
2. **등록:** 등록되지 않은 계정과 모바일 인증기를 QR 등으로 연결한다.
3. **인증 요청:** 등록된 사용자에게 앱 승인 요청을 보낸다.
4. **결과 확인:** 승인·거절·대기·취소 같은 결과를 확인한다.
5. **서비스 로그인 연결:** 성공 결과를 서비스의 session/JWT·회원 상태와 연결한다. 이 단계 전체는 8과목 샘플에서 구조를 배웠고, 중간 프로젝트 구현은 단계 9 후속이다.
6. **등록 해제:** 계정과 인증기 연결을 끊어 재등록 또는 일반 로그인 복귀 조건을 만든다.

## 수업에서의 등장

- [[summaries/2026-05-14-passwordless-x1280-intro|05-14]]: 피싱·RCE·Zero Trust에서 Passwordless 필요성으로 이동했다. 실행 결과는 없다.
- [[summaries/2026-05-15-passwordless-x1280-docker-service|05-15]]: Members·`setting.ap`·Docker 세 서버·WordPress 절차를 연결했다.
- [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|05-18]]: MariaDB·Spring 샘플에서 등록·로그인·해제 상태 전이를 관찰했다.
- [[summaries/2026-05-21-passwordless-x1280-rest-api|05-21]]: Postman으로 등록 여부 response를 직접 읽었다. 교육 collection의 나머지 saved response는 실행 증거가 아니다.

## 직접 수업과 후속 설계 경계

05-15·05-18·05-21은 서비스 등록, server 구성, 샘플 application, Postman API를 직접 다룬다. React polling·callback, Member 상태 column, DTO·Service·Controller·SecurityConfig, JWT/session 발급을 포함한 실제 프로젝트 orchestration은 `raw/KoreaICT/9. 중간 프로젝트 공부/`의 후속 설계다. 이 페이지는 그 연결을 안내하지만 단계 8 직접 구현으로 소급하지 않는다.

## 자주 헷갈리는 점

- **Passwordless = 로그인 상태 유지:** 아니다. 외부 인증 성공 후 서비스가 session/JWT를 어떻게 만들지는 별도다.
- **QR = 로그인 성공:** QR은 주로 계정과 인증기를 연결하는 등록 매개다.
- **API 처리 성공 = 인증기 등록됨:** `result`와 `data.exist`는 서로 다른 층위의 상태다.
- **서비스 credential = 사용자 password:** 서비스 서버가 Auth Server와 통신하기 위한 비밀값이며 사용자 credential과 다르다.
- **인증 성공 = 인가 완료:** 성공한 사용자가 어떤 endpoint·data에 접근할지는 [[comparisons/authentication-vs-authorization|인증 vs 인가]]의 별도 판단이다.

## 관련 개념

- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md` — 단계 9 후속 설계