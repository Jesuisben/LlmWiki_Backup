---
title: AAM과 APE
created: 2026-07-13
updated: 2026-07-13
type: entity
tags: [auth, linux, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
status: growing
confidence: high
---

# AAM과 APE

## 무엇인가

AAM(Autopassword Access Manager)과 APE(Autopassword Enterprise)는 2026-05-19 수업에서 함께 설치·연동한 기업형 인증 관리 제품군이다. 수업에서는 Rocky Linux VM 환경에 AAM/APE/DMZ 서버를 통합 설치하고, 관리자 화면에서 라이선스와 연동 설정, 사용자·인증기 정보를 다뤘다.

## 이 위키에서의 맥락

X1280은 서비스 로그인에서 모바일 앱 승인 흐름을 다룬 반면, AAM/APE는 조직의 사용자·인증기·연동 설정을 관리하는 별도 실습으로 등장했다. 같은 Passwordless 과목의 보안 확장 흐름이지만 X1280 Docker 통합 서버의 구성 요소로 동일시하지 않는다.

## 핵심 기능 / 특징

- AAM/APE/DMZ 서버 패키지를 Rocky Linux VM에 통합 설치
- APE 관리자 웹에서 라이선스와 연동 서비스 정보 설정
- AAM 콘솔/관리자 웹에서 인증 서버 연동값 확인·수정
- 부서와 사용자 생성 뒤 APE에서 사용자·인증기 정보 전달 여부 확인
- Enterprise 모바일 앱과 Windows Client에서 계정 추가·로그인 흐름 확인

수업에서는 APE의 Corp ID·관리자 토큰·AAM용 키가 AAM 인증 서버 설정의 대응 값과 일치해야 한다는 점을 확인했다. 실제 값은 wiki에 기록하지 않는다.

## 관련 개념

- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19 인증 기본과 AAM/APE 통합 설치]]
- [[comparisons/authentication-vs-authorization|인증(Authentication) vs 인가(Authorization)]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[entities/passwordless-x1280|Passwordless X1280]]

## 학습 이력

- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19]] — 인증·인가·IDP·SSO·상호인증을 구분하고 AAM/APE/DMZ 통합 설치, 라이선스, 연동 설정, 사용자·인증기 관리를 실습했다.

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
