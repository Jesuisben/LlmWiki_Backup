---
title: 2026-05-21 Passwordless X1280 REST API와 Postman
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [auth, backend, spring-boot, project, curriculum]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json
  - raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json
status: growing
confidence: high
---

# 2026-05-21 Passwordless X1280 REST API와 Postman

## 한 줄 요약

X1280 server를 다시 준비하고 Postman에서 사용자 등록 여부 확인 요청을 보내 실제 JSON response를 읽어, UI 전체 흐름과 API 단위 계약 검증의 차이를 배운 날이다.

## 왜 이 순서로 배웠는가

05-18에는 Spring 샘플이 여러 구성요소를 한꺼번에 연결했다. 이날은 API client인 Postman으로 외부 인증 server request/response를 따로 확인해, 문제가 생겼을 때 X1280 API 자체와 Spring 로그인 연결을 분리해 진단하는 기준을 만들었다.

## 배운 내용

1. 기존 VM snapshot을 이용해 교육용 X1280 server 환경을 다시 준비했다.
2. Docker network·volume·container, Host 방화벽, server process 확인 절차를 반복했다.
3. Auth 관리자 화면에 설정 파일을 적용하고 서비스 연동 정보를 준비했다.
4. 교육용 Postman collection을 import하고 Variables에 환경별 server·user·credential 값을 넣었다.
5. 사용자 등록 여부 확인 API를 POST로 호출하고 JSON response의 `result`, `code`, `msg`, `data.exist`를 읽었다.

## request/response 재고

두 Postman collection은 등록 여부 확인, 등록 요청, 일회용 token 요청, 인증 요청, 모바일 승인 결과 확인, 인증 취소, 등록 해제의 **7개 POST request**를 정의한다. 빈칸 교육용 collection에는 saved response가 없고, 완성형 교육 collection에는 각 request의 예시 response가 들어 있다. 이 saved example은 교육 입력자료이지 이번 사용자 환경의 실행 결과가 아니다.

날짜 원본에는 등록 여부 확인 호출 뒤 다음 JSON이 연속 단위로 보존돼 있다.

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

이 결과는 API 요청 처리 성공과 “해당 사용자의 인증기 등록 상태가 false”를 함께 보여준다. Passwordless 로그인 성공이나 Spring session/JWT 발급을 뜻하지 않는다.

## 직접 보존된 결과와 미보존 결과

- 직접 결과: 위 등록 여부 확인 JSON response 1건.
- 교육자료 예시: 완성형 collection의 7개 request 및 saved response 구조.
- 미보존: 등록·일회용 token·인증 요청·승인 결과·취소·해제의 당일 실제 response, 모바일 화면, Spring application의 최종 로그인 결과.

## 헷갈린 점 / 질문

- HTTP 200이나 `result: true`는 business state인 `data.exist`와 같은 뜻이 아니다.
- 등록되지 않음은 로그인 password 오류와 다르다. 다음 단계가 등록 flow라는 뜻이다.
- Postman API 성공은 Spring DTO·REST client·Service·Controller·로그인 상태 처리가 완성됐다는 증거가 아니다.
- collection의 saved response는 문서화된 예시이며 사용자가 직접 실행한 결과로 세지 않는다.

## 이전·다음 연결

- 이전 직접 연결: [[summaries/2026-05-18-passwordless-x1280-server-spring-sample|05-18 Spring 샘플]]과 [[concepts/spring-boot-rest-api|Spring Boot REST API]].
- 과목 복습: [[summaries/2026-05-21-passwordless-subject-review|Passwordless 총정리]].
- 후속 설계: 단계 9에서 실제 프로젝트의 REST client·로그인 상태·인가 연결을 판단한다.

## 관련 페이지

- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.21(목)/2026.05.21(목).md`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/0.Passwordless_X1280_인증서버_REST_API_20260511.pdf`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR]Passwordless X1280 API v1.postman_collection.json`
- `raw/KoreaICT/8. Passwordless/교육 자료/4. PX1280 Extra/[KR][교육용 빈칸] Passwordless X1280 API v1.postman_collection.json`