---
title: 2026-05-19 인증 기본과 AAM/APE 통합 설치
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [auth, linux, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf
status: growing
confidence: high
---

# 2026-05-19 인증 기본과 AAM/APE 통합 설치

## 한 줄 요약

인증·인가·IDP·SSO·상호인증의 책임을 구분한 뒤, AAM/APE/DMZ 서버와 client를 준비해 조직 사용자·인증기·연동 설정이 전달되는 흐름을 따라간 날이다.

## 왜 이 순서로 배웠는가

앞선 X1280 샘플이 한 서비스의 등록·로그인에 초점을 맞췄다면, 이날은 기업 환경에서 여러 사용자·인증기·정책·연동 서비스를 어떻게 관리하는지로 범위를 넓혔다. 설치 전에 인증과 인가, SSO와 IDP를 구분해 어떤 제품 책임을 보고 있는지 먼저 정리했다.

## 배운 내용

- Authentication은 사용자가 누구인지 확인하고, Authorization은 확인된 사용자가 무엇을 할 수 있는지 판단한다.
- MFA는 지식·소지·생체 요소 중 둘 이상을 조합하는 관점이고, SSO는 한 번 받은 인증 ticket/token으로 연결 서비스의 재로그인 부담을 줄인다.
- IDP는 디지털 신원 정보를 발급·관리하는 주체이며, 상호인증은 서비스도 사용자가 신뢰할 수 있는 대상인지 확인하는 관점이다.
- Rocky Linux 서버 환경과 Windows client 환경을 나눠 준비했다.
- AAM·APE·DMZ 서버 package를 설치하고 DB·process·license 적용 절차를 진행했다.
- APE와 AAM 관리자 화면의 조직·서비스 연동 항목을 맞춘 뒤 부서·사용자를 생성하고 사용자·인증기 정보 전달을 확인했다.
- Enterprise 모바일 앱과 Windows Client의 계정 등록·로그인 절차를 살폈다.

## 직접 보존된 결과와 미보존 결과

| 구간 | 원본에 보존된 것 | 완료로 과확정하지 않는 것 |
|---|---|---|
| VM·SSH | service의 active 상태와 network 확인 명령·출력 | 전체 server package의 지속 실행 상태 |
| 통합 설치 | 설치 script 입력 순서와 process 상태 확인 절차 | 모든 AAM·APE·DMZ process의 완전한 출력 |
| 관리자 설정 | license 적용, 대응 연동값 비교·수정, 사용자 생성 절차 | 실제 식별자·license·token·credential 값 |
| 사용자 전달 | AAM에서 만든 사용자 정보가 APE에 전달됐는지 확인했다는 수업 메모 | 독립 API response·screenshot·Windows 로그인 결과 |

교육 PDF는 설치·화면 순서를 제공하는 입력자료이며 실행 결과를 대신하지 않는다.

## 대표 실습 흐름

서버 설치 뒤 APE에서 조직·연동 서비스 정보를 준비하고, AAM의 인증 서버 설정이 같은 조직 문맥을 가리키는지 비교했다. 이후 AAM에서 사용자·인증기 관련 항목을 만들고 APE에서 전달 여부를 확인했다. 중요한 것은 제품 이름 암기가 아니라 AAM 쪽 접근·인증 관리와 APE 쪽 기업 사용자·정책 관리가 일치하는 설정으로 연결된다는 점이다.

## 헷갈린 점 / 질문

- 로그인 성공(Authentication)과 관리자 기능 실행 허용(Authorization)은 다른 판단이다.
- SSO는 모든 서비스가 같은 비밀번호를 저장한다는 뜻이 아니라 신뢰된 인증 결과를 재사용하는 구조다.
- AAM/APE는 05-15의 X1280 Auth/User Connection/Push Request 세 서버와 동일한 구성요소가 아니다.
- DMZ는 네트워크 배치 경계이며 제품 간 secret·license·조직 식별자를 공개해도 된다는 뜻이 아니다.

## 이전·다음 연결

- 이전: [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|05-18 X1280 Spring 샘플]].
- 다음: [[summaries/2026-05-20-filingbox-giga-mega|05-20 FilingBox/NAS/WORM]]에서 인증 이후 데이터 보호로 이동한다.
- 선행: [[comparisons/authentication-vs-authorization|인증 vs 인가]]는 FrontEnd_BackEnd JWT 구현과 이날의 용어 학습을 연결한다.

## 관련 페이지

- [[entities/aam-ape|AAM과 APE]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[concepts/nas-worm-storage-protection|NAS·WORM 저장소 보호]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf`