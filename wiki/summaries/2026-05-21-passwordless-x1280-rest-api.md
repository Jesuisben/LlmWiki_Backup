---
title: 2026-05-21 Passwordless X1280 REST API와 Postman
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [auth, backend, spring-boot, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json
status: growing
confidence: high
---

# 2026-05-21 Passwordless X1280 REST API와 Postman

## 한 줄 요약

X1280 인증 서버를 다시 구성하고 Postman collection으로 REST API를 호출해 사용자 등록 여부 같은 응답을 확인하면서, Spring Boot 연동 전 API 단위 검증 방법을 배운 날이다.

## 배운 내용

- API 사용 실습을 위해 Postman을 설치하고 교육용 collection JSON을 import했다.
- VM을 clone해 PX1280 서버를 준비하고 Docker 통합 컨테이너를 다시 실행했다.
- Auth 관리자 페이지에서 `setting.ap`를 업로드하고 서버 아이디/서버키를 발급했다.
- Postman Variables에 인증 서버 IP, 사용자 ID, serverKey 같은 값을 넣고 API 요청을 보냈다.
- 사용자 등록 여부 확인 API(`isAP`) 응답에서 `result`, `code`, `msg`, `data.exist` 같은 JSON 구조를 확인했다.

## 핵심 개념

- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]

## 실습 / 예제

원본의 실제 IP와 서버키는 wiki에 남기지 않는다. API 검증 흐름은 다음과 같다.

```text
X1280 Docker 서버 실행
→ Auth 관리자 페이지에서 setting.ap 업로드
→ 서버 아이디/서버키 발급
→ Postman collection import
→ Variables에 AuthServerIP/userId/serverKey 설정
→ isAP 등 API 호출
→ JSON 응답의 result/code/data 확인
```

예시 응답 구조는 다음처럼 읽는다.

```json
{
  "result": true,
  "msg": "OK.",
  "code": "000.0",
  "data": {
    "exist": false
  }
}
```

## 헷갈린 점 / 질문

- Postman에서 직접 API가 성공해도 Spring Boot 연동이 자동으로 끝나는 것은 아니다. 백엔드에서는 API 호출 client, DTO, 서비스 로직, 컨트롤러, 보안 설정을 별도로 연결해야 한다.
- `exist: false`는 사용자가 Passwordless에 아직 등록되지 않았다는 의미로 읽어야 하며, 로그인 실패와 같은 의미가 아니다.
- serverKey와 같은 연동 비밀값은 원본 실습 파일에는 있어도 wiki나 Git 저장소에 남기면 안 된다.

## 관련 페이지

- [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|2026-05-18 Passwordless 서버와 Spring 샘플 연동]]
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json`
