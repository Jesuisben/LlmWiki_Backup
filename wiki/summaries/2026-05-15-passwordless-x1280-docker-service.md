---
title: 2026-05-15 Passwordless X1280 Docker 통합 서버와 서비스 등록
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [auth, docker, backend, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md
  - raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/Wordpress-Passwordless X1280 Plugin/PasswordlessX1280 - Wordpress plugin OVA install Test Guide.pdf
status: growing
confidence: high
---

# 2026-05-15 Passwordless X1280 Docker 통합 서버와 서비스 등록

## 한 줄 요약

서비스 등록 → X1280 인증 서버 설치 → 웹 애플리케이션 적용이라는 큰 순서를 익히고, Docker 통합 서버와 WordPress 플러그인 실습으로 등록·앱 승인·로그인 절차를 따라간 날이다.

## 왜 이 순서로 배웠는가

05-14가 “왜 Passwordless가 필요한가”를 다뤘다면, 이날은 서비스를 인증 서버가 식별할 수 있게 등록한 뒤 서버를 실행하고 마지막에 애플리케이션을 연결하는 운영 순서를 배웠다. 웹 화면만 먼저 붙이면 어느 서비스가 어떤 인증 서버와 통신하는지 검증할 수 없기 때문이다.

## 배운 내용

1. Members에서 모바일 앱 계정을 준비하고 서비스의 도메인·네트워크 정보를 등록한다.
2. 일반 모드의 DNS TXT 검증과 교육용 테스트 모드의 간소화된 승인 절차를 구분한다.
3. Docker를 설치하고 Auth Server·User Connection Server·Push Request Server가 포함된 통합 구성을 실행한다.
4. 컨테이너 port mapping과 Docker Host의 `firewalld` 허용이 서로 다른 계층임을 확인한다.
5. Auth 관리자 화면에 `setting.ap`를 적용하고 서비스 서버용 식별정보를 발급한다.
6. UI 제공 방식과 REST API 제공 방식이라는 애플리케이션 연동 선택지를 살폈다.
7. WordPress 교육 환경에서 플러그인 활성화, 사용자 등록, QR 앱 등록, Passwordless 로그인, 등록 해제 순서를 따라갔다.

## 직접 보존된 결과와 미보존 결과

| 구간 | 원본에 보존된 것 | 완료로 확정하지 않는 것 |
|---|---|---|
| Docker 준비 | 설치·service·container 확인에 사용한 명령과 일부 상태 출력 | 세 서버의 모든 외부 URL이 실제 응답했다는 화면 증거 |
| 서비스 등록 | 입력 항목, 테스트 모드와 승인 상태 확인 절차 | 일반 모드 DNS TXT 검증의 실제 전파·승인 결과 |
| 관리자 설정 | `setting.ap` 적용 위치와 식별정보 발급 절차 | 발급값 자체와 운영 환경 설정 성공 |
| WordPress | 플러그인 활성화 성공이라는 수업 메모의 관찰 서술 | 등록·로그인·해제 각각의 독립 응답·화면 캡처 |

교육 PDF와 WordPress 설치 가이드는 절차를 제공하는 교육 입력자료다. 날짜 메모에 없는 실행 성공을 추가로 증명하지 않는다.

## 대표 실습 흐름

Members 서비스 등록과 승인 상태 확인 후 Docker Host에 통합 서버를 구성하고, Auth 관리자 화면에서 설정 파일과 서비스 연결 정보를 준비했다. 이후 WordPress 관리 화면에서 플러그인을 활성화하고 일반 사용자 화면에서 QR 등록과 앱 로그인 절차를 진행했다. 값 자체보다 서비스 등록 정보·서버 설정·애플리케이션 설정이 같은 서비스 문맥을 가리키는지가 핵심이다.

## 헷갈린 점 / 질문

- `setting.ap`는 웹 애플리케이션 코드가 아니라 Auth 관리자 화면에 적용하는 서비스 설정·라이선스 자료다.
- 컨테이너 port를 publish했다고 Host 방화벽까지 자동 허용되는 것은 아니다.
- Auth, User Connection, Push Request 주소는 모두 서버 주소처럼 보여도 인증 판단·앱 연결·승인 요청 전달이라는 책임이 다르다.
- QR 등록은 계정과 인증기를 묶는 단계이고, 이미 등록된 계정의 앱 로그인 승인과 다르다.

## 이전·다음 연결

- 이전: [[summaries/2026-05-14-passwordless-x1280-intro|05-14]]의 위협 모델과 Passwordless 개념.
- 다음: [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|05-18]]에서 같은 구성을 다시 만들고 MariaDB·Spring 샘플·Tomcat까지 연결한다.
- 선행 기반: [[entities/docker|Docker]]와 [[concepts/linux-process-service-port-firewall|Linux process·service·port·firewall 진단]].

## 관련 페이지

- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[entities/passwordless-x1280|Passwordless X1280]]
- [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.15(금)/2026.05.15(금).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/Passwordless 강의자료_Docker_ICT학원교육_20260514.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/Wordpress-Passwordless X1280 Plugin/PasswordlessX1280 - Wordpress plugin OVA install Test Guide.pdf`