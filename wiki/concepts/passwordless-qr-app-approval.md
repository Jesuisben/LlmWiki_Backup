---
title: Passwordless QR/앱 승인 흐름
created: 2026-07-03
updated: 2026-07-19
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

8과목에서 직접 확인한 것은 WordPress·Spring 샘플의 등록/승인/해제 절차와 05-21 등록 여부 API response다. 단계 9 가이드에는 React API helper, 로그인 선택 UI, QR·등록/해제 화면, 일정 간격 결과 확인과 CSS snippet이 연속 단위로 문서화돼 있다. 원격 접속·인증서·container 파일과 외부 REST 경로의 거부 응답 같은 부분 출력도 보존됐지만, 독립 TypeScript/CSS file, 최종 browser 승인, JWT 로그인, timeout·거절·재시도 성공 결과는 없다. 작성용 snippet과 부분 인프라 관찰을 05-15·05-18 직접 구현이나 중간 프로젝트 통합 성공으로 바꾸어 읽지 않는다.

## 단계 9 polling 구현안의 공백

- raw의 인증 결과 수신 방식은 React의 주기적 **polling**이다. 외부 인증 server가 Spring으로 보내는 webhook/callback 구현은 없다.
- 화면 countdown이 0이 되어도 polling 중단·backend 취소·session 초기화·timeout 안내로 이어지는 동작은 보존되지 않았다.
- polling 오류를 다음 주기까지 무시하므로 정상 대기와 network·server·serialization·만료 오류가 같은 화면으로 보일 수 있다.
- 등록 상태 polling에도 명시적인 timeout이 없다. 따라서 “polling snippet written”과 “요청 생명주기 검증 완료”를 분리한다.

## 자주 헷갈리는 점

- QR image 자체가 인증 결과는 아니다. 등록 데이터를 앱으로 전달하는 매개다.
- 앱에 계정이 보인다는 사실과 서비스 application이 로그인 상태를 만든 것은 다르다.
- 등록 해제는 단순 logout이 아니다. 계정과 인증기의 연결 상태를 바꾼다.
- 승인 request를 보냈다는 사실과 사용자가 승인했다는 결과는 다르다.
- polling code가 있다는 사실과 외부 callback·timeout·component cleanup이 구현·검증됐다는 사실은 다르다. 이 raw에서 외부 callback은 미구현이다.

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