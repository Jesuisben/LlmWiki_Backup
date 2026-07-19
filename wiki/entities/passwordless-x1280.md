---
title: Passwordless X1280
created: 2026-07-03
updated: 2026-07-19
type: entity
tags: [auth, backend, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
status: growing
confidence: high
---

# Passwordless X1280

## 무엇인가

Passwordless X1280은 서비스 계정과 모바일 인증기를 연결하고 앱 승인 결과를 외부 인증 server와 application이 확인해 비밀번호 입력을 줄이는 인증 제품·기술로 수업에 등장했다.

## 이 위키에서의 첫 등장과 위치

05-14에 피싱·RCE·Zero Trust와 함께 처음 등장했다. Java/Oracle/UI 구현이나 AWS/CI/CD 배포 도구가 아니라, 앞서 만든 Spring·React 서비스의 인증 경계를 확장하는 후속 과목이다. [[concepts/jwt-session-cookie-auth|JWT·Session·Cookie]]는 로그인 상태 전달, X1280은 비밀번호 없이 사용자를 확인하는 과정에 초점이 있다.

## 학습 이력

| 날짜 | 학습 역할 | 근거 수준 |
|---|---|---|
| [[summaries/2026-05-14-passwordless-x1280-intro|05-14]] | 보안 위협, Passwordless·상호인증 개념 | 이론·교육자료, 실행 결과 없음 |
| [[summaries/2026-05-15-passwordless-x1280-docker-service|05-15]] | Members, `setting.ap`, Docker 세 서버, WordPress 적용 | 명령·일부 상태와 plugin 성공 관찰, 개별 인증 화면 결과 미보존 |
| [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|05-18]] | MariaDB·Spring sample·WAR/Tomcat, 등록·로그인·해제 | DB 결과와 수업 메모 관찰, 단계별 API/screenshot 미보존 |
| [[summaries/2026-05-19-aam-ape-authentication-filingbox|05-19]] | 인증 개념과 AAM/APE 제품군 경계 | X1280 하위 구성요소가 아님 |
| [[summaries/2026-05-21-passwordless-x1280-rest-api|05-21]] | Postman REST contract | 등록 여부 JSON 한 건 직접 보존, 나머지는 교육 example |
| 단계 9 | 인증 server 준비→서비스 등록→Spring REST 계층→React polling UI→배포 점검 가이드 | 인프라 일부 출력·초기 REST/MIME 실패 관찰과 구체 snippet 보존; 독립 project source·build·end-to-end 결과는 없음 |

## 핵심 구성과 제품 경계

- Members는 서비스 등록·설정 자료 발급 흐름을 제공한다.
- Auth Server는 서비스와 사용자 인증 request를 처리한다.
- User Connection Server와 Push Request Server는 모바일 인증기 연결과 승인 요청 전달 경로를 담당한다.
- Spring sample/application은 외부 response를 자체 회원과 로그인 상태에 연결한다.
- AAM/APE는 조직 사용자·인증기·연동 서비스를 관리하는 별도 제품군이다.
- FilingBox GIGA/MEGA와 WORM은 저장 data 보호 계층이며 X1280 server 구성요소가 아니다.

## 면접·프로젝트 설명 관점

“X1280을 썼다”보다 서비스 등록 → 인증 server 구성 → API contract 확인 → application 회원·session/JWT 연결 → authorization이라는 책임 경계를 설명하는 것이 중요하다. 또한 교육 collection의 예시 response, 날짜 메모의 관찰 서술, 단계 9 Markdown의 embedded snippet, 단계 9에 포함된 부분 출력·실패 관찰, 실제 project artifact와 end-to-end 결과를 구분해야 한다.

## 관련 개념

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[entities/aam-ape|AAM과 APE]]
- [[concepts/nas-worm-storage-protection|NAS·WORM 저장소 보호]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md` — 단계 9 후속 설계