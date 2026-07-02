---
title: GET vs POST
created: 2026-07-02
updated: 2026-07-02
type: comparison
tags: [html, javascript, backend, auth]
sources:
  - raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md
  - raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf
status: growing
confidence: high
---

# GET vs POST

## 비교 목적

2026-03-26 수업에서는 로그인 URL 예시를 통해 parameter, query string, GET/POST 전송 방식을 배웠다. 이 구분은 이후 Spring Controller, REST API, 로그인/보안 수업으로 이어진다.

## 한눈에 보기

| 항목 | GET | POST |
|---|---|---|
| 데이터 위치 | URL query string | HTTP body |
| 주소창 노출 | 보임 | 보통 보이지 않음 |
| 수업 비유 | 엽서처럼 내용이 보임 | 봉투처럼 body에 담김 |
| 주 사용 | 조회, 검색, 페이지 이동 | 등록, 수정, 로그인, 파일 업로드 |
| 예시 | `/login?username=hong&password=hello` | `/login` + body 데이터 |

## 핵심 설명

GET은 URL 뒤의 `?` 이후에 `key=value` 형태로 parameter가 붙는다. 여러 parameter는 `&`로 구분한다.

```text
http://localhost:63342/login?username=hong&password=hello
```

수업에서는 `?`가 query string의 시작점이고, `&`가 parameter 구분자이며, `=`가 이름과 값을 나누는 기호라고 정리했다. ^[raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf]

POST는 데이터를 HTTP body에 담아 보내므로 주소창에 username/password 같은 값이 직접 드러나지 않는다. 그렇다고 POST만으로 보안이 완성되는 것은 아니며, 실제 서비스에서는 HTTPS와 서버 검증이 함께 필요하다.

## 헷갈리기 쉬운 포인트

- GET은 “항상 나쁘다”가 아니라 조회/검색처럼 주소로 공유해도 되는 요청에 적합하다.
- 비밀번호처럼 주소창에 보이면 안 되는 값은 GET query string에 두면 안 된다.
- HTML form의 `method`와 JavaScript의 `location.href` 이동은 이후 Spring API 요청 방식과 연결된다.

## 관련 페이지

- [[summaries/2026-03-26-javascript-dom-product-pages|2026-03-26 JavaScript DOM과 상품 목록/상세 페이지]]
- [[concepts/javascript-dom|JavaScript와 DOM]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[comparisons/session-vs-cookie-vs-jwt|Session vs Cookie vs JWT]]

## 출처

- `raw/Study/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/Study/3. UI&UX/교육 자료/IT 관련 용어.pdf` p.26~27
