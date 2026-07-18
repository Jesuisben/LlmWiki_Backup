---
title: AAM과 APE
created: 2026-07-13
updated: 2026-07-18
type: entity
tags: [auth, linux, project]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf
status: growing
confidence: high
---

# AAM과 APE

## 무엇인가

AAM(Autopassword Access Manager)과 APE(Autopassword Enterprise)는 05-19에 함께 설치·연동한 기업형 인증 관리 제품군이다. 수업에서는 AAM·APE·DMZ server, 조직 사용자·인증기, license와 연동 설정, 모바일·Windows client 흐름을 다뤘다.

## 이 위키에서의 맥락

X1280 수업이 한 서비스의 QR 등록·앱 승인·REST API에 초점을 맞췄다면 AAM/APE 수업은 조직 차원의 사용자·인증기·연동 서비스 관리로 범위를 넓혔다. 둘은 같은 Passwordless 과목에서 등장하지만 AAM/APE를 X1280 Docker 통합 server의 하위 process로 보지 않는다.

## 구성요소 책임

| 구성요소 | 수업에서 다룬 책임 |
|---|---|
| AAM | 접근·인증 server 설정, 사용자·client와의 연결 관리 |
| APE | 조직·연동 서비스·사용자·인증기 정보 관리 |
| DMZ server | 외부·내부 연결을 분리하는 배치 경계 |
| 모바일 Enterprise 앱 | 계정 등록과 인증 요청 확인 절차 |
| Windows Client | desktop 환경의 계정 연결·로그인 절차 |

제품별 세부 기능을 이 표보다 넓게 일반화하지 않는다. 수업의 직접 근거는 설치·관리자 설정·사용자 전달 확인 절차다.

## 학습 이력

1. Authentication·Authorization·IDP·SSO·Mutual Authentication을 구분했다.
2. server와 client VM을 준비하고 SSH·network 상태를 확인했다.
3. AAM/APE/DMZ package와 DB를 설치하고 process 확인 절차를 수행했다.
4. license를 적용하고 APE와 AAM의 대응 연동 설정을 비교·수정했다.
5. 조직·부서·사용자를 만들고 APE에서 사용자·인증기 정보 전달 여부를 확인했다.
6. 모바일 앱과 Windows Client 절차로 확장했다.

원본에는 일부 service 상태와 사용자 전달 확인의 수업 메모가 있지만, 모든 process output·API response·client login screenshot은 보존돼 있지 않다. 교육 PDF의 화면도 사용자 환경 성공 증거로 세지 않는다.

## 프로젝트·면접 설명 관점

AAM/APE를 설명할 때는 “인증 제품”이라는 한 문장보다 조직 정보·연동 서비스·인증기·client가 어느 관리 지점에서 이어지는지 말해야 한다. 실제 license·token·조직·service 식별자는 문서나 repository에 노출하지 않는 것도 운영 책임이다.

## 관련 개념

- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19 인증 기본과 AAM/APE 통합 설치]]
- [[comparisons/authentication-vs-authorization|인증(Authentication) vs 인가(Authorization)]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[concepts/nas-worm-storage-protection|NAS·WORM 저장소 보호]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/1. 인증 기본 교육_20260512.pptx.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/2. AAM&APE/2. AAM_APE_설치 (서버 및 클라이언트).pptx.pdf`