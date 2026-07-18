---
title: 2026-05-18 Passwordless 서버 설치와 Spring 샘플 연동
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [auth, spring-boot, docker, backend, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
status: growing
confidence: high
---

# 2026-05-18 Passwordless 서버 설치와 Spring 샘플 연동

## 한 줄 요약

X1280 Docker 서버를 다시 구성한 뒤 MariaDB·Java/Spring 샘플·Tomcat을 연결해 계정 생성, Passwordless 등록·로그인·해제와 일반 로그인 복귀를 단계별로 관찰한 날이다.

## 왜 이 순서로 배웠는가

05-15의 서비스·서버 구성만으로 사용자가 서비스에 로그인할 수는 없다. 이날은 인증 서버 준비 → 샘플 사용자 DB → 애플리케이션 설정 → 로컬 실행 → Linux/Tomcat 배포 순서로 범위를 넓혀, 외부 인증 결과가 실제 웹서비스 계정 흐름과 만나는 지점을 배웠다.

## 배운 내용

1. VM 네트워크와 원격 접속을 준비하고 Members에서 교육용 서비스를 등록했다.
2. Docker network·volume·통합 container를 만들고 Host 방화벽, container 상태, 내부 서버 프로세스를 확인했다.
3. Auth 관리자 화면에 `setting.ap`를 적용하고 REST 연동용 서비스 정보를 준비했다.
4. Windows에 MariaDB·JDK·Spring Tools 환경을 만들고 `userinfo` 테이블과 샘플 사용자를 준비했다.
5. 샘플의 properties 설정에서 Auth REST, 사용자 연결, Push 요청에 필요한 역할별 주소와 서비스 credential을 연결했다.
6. 로컬 샘플에서 계정 생성 → Passwordless 등록 → 앱 승인 로그인 → 등록 해제 → 일반 비밀번호 로그인 복귀를 진행했다.
7. Maven 산출물(WAR)을 Rocky Linux Tomcat에 배치하고 서버 설정·DB·애플리케이션 설정을 맞추는 절차로 확장했다.

## 직접 보존된 결과와 미보존 결과

| 구간 | 원본에 보존된 직접 근거 | 경계 |
|---|---|---|
| 서버 기반 | service/container 확인 명령과 상태 출력, 세 서버 process 확인 절차 | 모든 외부 화면의 성공 응답은 별도 보존되지 않음 |
| MariaDB | DB 접속·table/row 준비에 사용한 연속 SQL과 조회 결과 | 운영 DB나 X1280 내부 DB의 상태를 뜻하지 않음 |
| 로컬 샘플 | 등록 후 기존 비밀번호 로그인이 달라지고, 해제 뒤 일반 로그인을 다시 시도한 관찰 서술 | X1280 전체 제품의 보편 규칙이 아니라 이 샘플의 동작 |
| WAR/Tomcat | WAR 생성 경로, 복사·설정·재시작 절차와 첫 시도 실패 후 재시도 성공이라는 수업 메모 | 브라우저별 등록·로그인·해제 응답과 화면 캡처는 미보존 |

따라서 “등록·로그인·해제를 실습했다”는 날짜 메모의 관찰은 보존하되, 각 단계가 독립 API 응답이나 screenshot으로 증명됐다고 확대하지 않는다.

## 대표 데이터 흐름

브라우저의 샘플 계정 요청은 Spring 애플리케이션과 로컬 사용자 DB를 거치고, Passwordless 관련 판단은 X1280 Auth Server 및 앱 연결 서버로 전달된다. 사용자 DB의 비밀번호·회원 row와 X1280의 사용자 등록·승인 상태는 같은 데이터가 아니다. 설정에서 두 영역을 잘못 섞으면 서버는 동작해도 서비스 로그인이 이어지지 않을 수 있다.

## 헷갈린 점 / 질문

- 등록·로그인·해제는 하나의 버튼 기능이 아니라 서로 다른 사용자 상태 전이다.
- 서비스 연동 credential은 사용자 비밀번호가 아니며 source code와 wiki에 실제 값을 남기지 않는다.
- 로컬 MariaDB, X1280 container 내부 저장소, Tomcat에 배포된 애플리케이션은 각각 다른 책임을 가진다.
- WAR가 생성되거나 Tomcat이 실행됐다는 사실만으로 브라우저 로그인 성공이 보장되지는 않는다.

## 이전·다음 연결

- 이전: [[summaries/2026-05-15-passwordless-x1280-docker-service|05-15 서비스 등록과 Docker 통합 서버]].
- 다음: [[summaries/2026-05-19-aam-ape-authentication-filingbox|05-19 인증 기본과 AAM/APE]], 이어서 [[summaries/2026-05-21-passwordless-x1280-rest-api|05-21 REST API 단위 확인]].
- 후속: React·JWT·SecurityConfig를 포함한 실제 중간 프로젝트 설계는 단계 9에서 다룬다.

## 관련 페이지

- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.18(월)/2026.05.18(월).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`