---
title: Spring Boot Passwordless 인증 연동
created: 2026-07-03
updated: 2026-07-19
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

## server는 동작하지만 Spring 로그인이 되지 않을 때의 진단 checklist

이 checklist는 05-15·05-18·05-21의 설치·연결·샘플·API 절차를 재사용한 진단 순서다. 특정 사용자 장애의 원인과 해결 이력이 완결된 것은 아니므로 독립 Query가 아니라 이 연동 Concept가 책임을 가진다.

1. Docker container와 각 server process가 실행 중인지 확인한다.
2. host firewall과 host↔container port mapping이 요청 경로를 막지 않는지 확인한다.
3. Members에 서비스가 등록돼 있고 application이 해당 서비스의 `setting.ap`를 읽는지 확인한다.
4. Auth·User Connection·Push Request 역할별 연결값이 서로 뒤바뀌지 않았는지 확인한다.
5. server 연동용 service credential과 최종 사용자의 password를 구분한다. 실제 값은 code·wiki·log에 남기지 않는다.
6. 같은 환경의 Postman REST API를 단위 호출해 HTTP 처리, `result`·`code`·`msg`, 기능별 `data`를 나눠 읽는다.
7. MariaDB에 필요한 user row가 있는지 확인하되 local 회원 row와 X1280 사용자·인증기 등록 상태를 같은 것으로 보지 않는다.
8. Spring properties의 DB·역할별 server·service 설정이 실행 profile과 일치하는지 확인한다.
9. REST DTO·client·Service가 protocol 응답을 application 상태로 어떻게 해석하는지 확인한다. 단계 9 가이드에는 이 계층과 Controller·Member 상태·SecurityConfig의 Java snippet이 있지만 독립 source와 build/API 결과는 없다.
10. WAR 생성과 Tomcat 배치·재시작·HTTP 응답을 각각 확인한다. build 성공만으로 browser login 성공을 단정하지 않는다.
11. 외부 인증 성공 뒤 application이 session/JWT 등 자체 로그인 상태를 실제로 만드는지 확인한다.
12. 마지막으로 protected endpoint의 role·ownership authorization을 별도로 검증한다.

## 원본 API 재고와 근거 수준

교육 collection은 등록 여부, 등록, 일회용 token, 인증 요청, 승인 결과, 취소, 해제의 7개 POST request를 정의한다. 완성형 collection에는 saved response example이 있지만 교육 입력자료다. 05-21 날짜 원본이 직접 보존한 실행 response는 등록 여부 확인 한 건이다. 따라서 나머지 request를 Spring sample이 모두 성공했다고 단정하지 않는다.

## 중간 프로젝트 후속 경계

DTO·REST client·Service·Controller·Member 상태·SecurityConfig·React API helper·로그인 UI·polling은 단계 9 가이드가 제시한 연속 snippet 묶음이다. 8과목의 sample application과 API contract를 중간 프로젝트 모양으로 옮기는 설계 근거는 되지만, 별도 Java/TypeScript artifact가 없으므로 실제 source tree에 wired됐다고 확정하지 않는다.

| 증거 단계 | 단계 9 raw 판정 |
|---|---|
| Written | properties·Member·Client·DTO·Service·Controller·SecurityConfig·JWT 호출·React snippet 보존 |
| Snippet-level wired | Client→Service→Controller→React 호출 관계가 문서상 연결됨 |
| 부분 인프라 결과 | 원격 shell, 인증서·container 파일 출력, 외부 REST 경로 거부 응답 보존 |
| 초기 Spring 관찰 | 등록 상태 호출의 MIME 처리 문제 서술 보존 |
| 실제 project source·compile/build | 미보존 |
| MIME 수정 후 최종 API 성공 | 조건만 있고 결과 미보존 |
| QR 등록·모바일 승인·JWT 로그인 | 미보존 |
| React·CI/CD·protected endpoint 전체 성공 | 미보존 |

## 단계 9 구현안의 검토 지점

- 승인 상태만 보지 말고 protocol 결과·사용자 일치·hash/random·challenge/session 소유권·만료를 결합한 뒤 JWT를 발급한다.
- 로그인 전 공개 endpoint는 사용자 식별값만으로 상태를 노출·변경하지 않도록 challenge binding, rate limit, enumeration 방지, 재인증을 설계한다.
- 정상 대기와 HTTP·network·serialization·만료 오류를 구분한다. 오류를 무조건 polling 대기로 바꾸지 않는다.
- local `passwordlessEnabled`를 source of truth로 둘지 외부 상태의 projection으로 둘지 정하고 drift 복구 규칙을 둔다.
- Controller가 참조하는 응답 DTO, WebClient dependency, Member setter, JWT utility signature와 repository method가 실제 project code와 맞는지 확인한다.
- Secret 등록 목록과 container 전달 항목이 일치하는지, runtime property가 실제 환경변수를 소비하는지 검증한다.

## 자주 헷갈리는 점

- 외부 server의 service credential은 사용자 password가 아니며 code·wiki·log에 실제 값을 남기지 않는다.
- WAR 생성은 build 결과이고 Tomcat 실행·HTTP 응답·로그인 성공과 다르다.
- Postman response 성공은 Spring serialization·service logic·session/JWT 발급 성공을 보장하지 않는다.
- 로그인 시작 endpoint와 결과 확인·해제 endpoint의 공개 범위는 같을 필요가 없다. 다만 구체 SecurityConfig는 단계 9 판단 대상이다.
- 외부 REST 경로의 거부 응답은 network/API 경로 도달의 단서이지 인증 성공이 아니다.

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