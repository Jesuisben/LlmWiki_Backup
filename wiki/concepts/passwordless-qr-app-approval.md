---
title: Passwordless QR/앱 승인 흐름
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [auth, frontend, backend, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless QR/앱 승인 흐름

## 정의

QR/앱 승인 흐름은 계정과 모바일 인증기를 **등록**하고, 이후 로그인 요청을 앱에서 **확인·승인**하며, 필요하면 연결을 **해제**하는 세 상태를 구분하는 Passwordless 사용자 경험이다.

## 왜 중요한가

화면에서는 모두 Passwordless 버튼으로 보이기 쉽지만 server 상태는 다르다. 등록 전 사용자에게 바로 승인 요청을 보내거나, 이미 등록된 사용자를 다시 등록시키거나, 대기 중 요청을 로그인 실패로 처리하면 흐름이 꼬인다. UI는 현재 상태와 다음 행동을 분명히 보여줘야 한다.

## 세 흐름의 책임

| 흐름 | 시작 조건 | 사용자 행동 | 완료 조건 |
|---|---|---|---|
| 등록 | 인증기 미등록 | QR을 앱으로 읽고 계정 연결 확인 | server가 등록 상태를 반환 |
| 로그인 승인 | 인증기 등록 | 앱에서 요청 출처·내용 확인 후 승인·거절 | 승인 결과를 application이 확인 |
| 해제 | 인증기 등록 | 연결 해제 요청 확인 | server가 미등록 상태로 전환 |

05-15 WordPress와 05-18 Spring 샘플은 위 순서를 화면에서 따라갔다. 05-18에는 이 샘플에서 Passwordless 등록 뒤 기존 비밀번호 로그인이 달라지고, 해제 뒤 일반 로그인을 다시 시도한 관찰이 있다. 제품 전체의 보편 동작으로 일반화하지 않는다.

## 결과 상태를 읽는 법

- **미등록:** 등록 flow로 안내한다. password 오류가 아니다.
- **대기:** 모바일 사용자의 확인을 기다리는 상태다. 당장 실패로 단정하지 않는다.
- **승인:** 외부 인증 결과가 성공했다는 뜻이다. 서비스 session/JWT 생성은 다음 책임이다.
- **거절·취소·timeout:** 서로 다른 사용자 경험과 재시도 정책이 필요하지만, 8과목 날짜 원본에는 이 모든 상태의 실제 response가 보존돼 있지 않다.

## 직접 수업과 후속 프로젝트 경계

8과목에서 직접 확인한 것은 WordPress·Spring 샘플의 등록/승인/해제 절차와 05-21 등록 여부 API response다. React polling·callback, 상세 loading/error 화면, timeout 처리와 JWT 연결은 단계 9 중간 프로젝트 가이드의 확장 설계다. 유용한 설계라고 해서 05-15·05-18 직접 구현 결과로 쓰지 않는다.

## 자주 헷갈리는 점

- QR image 자체가 인증 결과는 아니다. 등록 데이터를 앱으로 전달하는 매개다.
- 앱에 계정이 보인다는 사실과 서비스 application이 로그인 상태를 만든 것은 다르다.
- 등록 해제는 단순 logout이 아니다. 계정과 인증기의 연결 상태를 바꾼다.
- 승인 request를 보냈다는 사실과 사용자가 승인했다는 결과는 다르다.

## 선행·후속 연결

- 선행: [[summaries/2026-05-14-passwordless-x1280-intro|X1280 소개와 상호인증 배경]].
- 함께 보기: [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]과 [[summaries/2026-05-21-passwordless-x1280-rest-api|REST API 상태 확인]].
- 후속: 단계 9에서 React 화면·Spring 상태 처리와 기존 JWT 로그인을 실제 프로젝트 관점으로 판단한다.

## 관련 개념

- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md` — 단계 9 후속 설계