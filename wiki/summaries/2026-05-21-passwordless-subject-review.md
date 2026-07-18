---
title: Passwordless 총정리
created: 2026-07-18
updated: 2026-07-18
type: summary
tags: [auth, docker, spring-boot, linux, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/8. Passwordless/Passwordless 총정리/Passwordless 총정리.md
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBG/ITUD_FilingBox GIGA_Hans_On_EN.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBM/ITUD_FilingBox MEGA_Hands_On_EN.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/NAS_WORM_교육.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/랜섬웨어_교육_박규휘_202605.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/QPM 기본 기능 및 사용법 안내서_교육용_251209.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/Wordpress-Passwordless X1280 Plugin/PasswordlessX1280 - Wordpress plugin OVA install Test Guide.pdf
status: growing
confidence: high
---

# Passwordless 총정리

## 한 줄 요약

05-14의 보안 위협과 X1280 소개에서 시작해 서비스 등록·Docker 서버·Spring 샘플·AAM/APE·FilingBox/WORM·Postman REST API로 확장한 6일 수업을 한 경로로 다시 보는 복습 허브다.

## 이 페이지의 역할

이 페이지는 날짜별 학습을 찾아가는 지도다. `raw/.../Passwordless 총정리.md`와 교육자료는 전체 흐름을 복습하는 보조 source이며, 날짜별 명령·출력·관찰·미보존 결과를 대체하지 않는다. 실행 성공 여부는 반드시 각 날짜 Summary의 결과 경계를 우선한다.

## 날짜별 학습 흐름

| 날짜 | 질문 | 핵심 학습 | 직접 결과 경계 |
|---|---|---|---|
| [[summaries/2026-05-14-passwordless-x1280-intro|05-14]] | 왜 비밀번호 입력을 줄이는가? | 피싱·랜섬웨어·RCE·DDoS, Zero Trust, X1280·상호인증 | 이론·교육자료, 실행 결과 없음 |
| [[summaries/2026-05-15-passwordless-x1280-docker-service|05-15]] | 서비스와 인증 server를 어떻게 준비하는가? | Members, DNS 검증/test mode, `setting.ap`, Docker 세 server, WordPress | 일부 상태·plugin 성공 관찰, 개별 인증 화면 결과 미보존 |
| [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|05-18]] | 외부 인증을 Spring sample에 어떻게 연결하는가? | Docker server, MariaDB, Spring sample, 등록·로그인·해제, WAR/Tomcat | DB 결과·수업 메모 관찰, 단계별 API/screenshot 미보존 |
| [[summaries/2026-05-19-aam-ape-authentication-filingbox|05-19]] | 조직 차원 인증을 어떻게 관리하는가? | 인증·인가·IDP·SSO·상호인증, AAM/APE/DMZ, 사용자·인증기 | 일부 service 상태·전달 확인 서술, 전체 client 결과 미보존 |
| [[summaries/2026-05-20-filingbox-giga-mega|05-20]] | 인증 뒤 data는 어떻게 보호하는가? | NAS·WORM, GIGA/MEGA, RO/RW/AO, network drive·storage | 절차·명령만 보존, mode별 거부·용량·client 결과 미보존 |
| [[summaries/2026-05-21-passwordless-x1280-rest-api|05-21]] | UI 밖에서 API를 어떻게 분리 검증하는가? | Postman, 7개 POST request 재고, 등록 여부 JSON | 등록 여부 response 한 건 직접, 나머지는 교육 example |

## 하나의 인증 흐름으로 연결하기

1. 서비스가 Members에 등록되고 Auth Server가 해당 서비스 문맥을 준비한다.
2. User Connection·Push Request Server가 모바일 인증기 연결과 승인 요청 전달 경로를 제공한다.
3. 등록되지 않은 사용자는 QR 등으로 계정과 인증기를 연결한다.
4. 등록된 사용자는 앱에서 요청 출처와 내용을 확인하고 승인·거절한다.
5. application은 REST 결과를 자체 회원 DB와 로그인 상태에 연결한다.
6. 인증 뒤 endpoint authorization과 storage access policy는 별도 계층에서 판단한다.

자세한 책임은 [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]], 상태 전이는 [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]], Spring 연결은 [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]에서 나눠 본다.

## 제품·기술 책임 지도

| 제품·기술 | 이 과목의 책임 | 같은 것으로 보면 안 되는 것 |
|---|---|---|
| [[entities/passwordless-x1280|Passwordless X1280]] | 서비스 계정의 등록·앱 승인·REST 인증 흐름 | 서비스 session/JWT·endpoint 인가 전체 |
| [[entities/aam-ape|AAM/APE]] | 조직·연동 서비스·사용자·인증기 관리 | X1280 Docker 세 server의 하위 process |
| [[concepts/nas-worm-storage-protection|FilingBox·NAS·WORM]] | 인증 이후 file 접근·변경·보존 | 사용자 신원을 확인하는 인증 server |
| [[entities/docker|Docker]]·Linux | server process·network·port·storage 실행 기반 | 인증 업무 규칙 자체 |
| MariaDB·Spring·Tomcat | 사용자 data와 sample web application 실행 | 모바일 인증기 상태의 유일한 저장소 |
| Postman | REST request/response 단위 확인 | 전체 browser 로그인 성공 증거 |

## 선행·후속 커리큘럼

- 선행 인증 구현: FrontEnd_BackEnd의 [[concepts/jwt-session-cookie-auth|JWT·Session·Cookie]]와 [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]].
- 선행 실행 기반: Linux의 process·service·port, Docker image/container/network/volume과 CI/CD의 EC2·domain·HTTPS 배포 흐름.
- 이번 직접 범위: 05-14~05-21 Passwordless 날짜 수업과 과목 교육자료.
- 후속 범위: 단계 9 중간 프로젝트에서 React·Spring·JWT·SecurityConfig와 X1280을 실제 설계로 조합하는 작업. 이번 허브가 그 구현 완료를 주장하지 않는다.

## 반복 혼동 체크

- Passwordless는 인증 제거가 아니라 비밀번호 입력을 다른 인증 요소·승인으로 바꾸는 것이다.
- 등록, 로그인 승인, 등록 해제는 서로 다른 상태 전이다.
- API `result`, business state, HTTP status, service login state를 하나로 합치지 않는다.
- 인증과 인가는 함께 쓰지만 책임이 다르다.
- 강한 인증과 WORM storage는 서로 보완하지만 같은 보안 계층이 아니다.
- 교육 PDF·완성형 Postman collection의 화면과 saved response는 사용자 환경 실행 증거가 아니다.

## Comparison·Query 다음 세션 판단점

기존 [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]과 [[comparisons/authentication-vs-authorization|인증 vs 인가]]는 다음 최종 세션에서 직접 source와 다시 대조한다. 등록 vs 로그인 vs 해제, AAM vs APE, 인증 보안 vs WORM, REST 등록 확인 vs 실제 사용자 인증은 독립 검색 가치와 반복 혼동이 기존 Concept로 충분히 흡수되는지 판단한 뒤에만 Comparison으로 만든다.

“Passwordless server는 동작하는데 Spring 로그인이 되지 않으면 어디부터 확인해야 하는가?”는 진단 가치가 있지만 실제 사용자 장애·해결 이력이 독립 Query 기준을 충족하는지는 다음 세션에서 최종 판단한다.

## 관련 페이지

- [[_meta/passwordless-rehighquality-inventory-plan|Passwordless 내용 재고도화 전수 재고와 실용형 실행 계획]]
- [[comparisons/passwordless-vs-password-login|Passwordless 로그인 vs 비밀번호 로그인]]
- [[comparisons/authentication-vs-authorization|인증(Authentication) vs 인가(Authorization)]]
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.14(목) - 시작/2026.05.14(목) - 시작.md`
- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
- `raw/KoreaICT/8. Passwordless/2026.05.20(수)/2026.05.20(수).md`
- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/8. Passwordless/Passwordless 총정리/Passwordless 총정리.md`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBG/ITUD_FilingBox GIGA_Hans_On_EN.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/FBM/ITUD_FilingBox MEGA_Hands_On_EN.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/NAS_WORM_교육.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/3. Filingbox MEGA & GIGA/랜섬웨어_교육_박규휘_202605.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_X1280 기술 소개 및 제품소개_20260514.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/QPM 기본 기능 및 사용법 안내서_교육용_251209.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/Wordpress-Passwordless X1280 Plugin/PasswordlessX1280 - Wordpress plugin OVA install Test Guide.pdf`
