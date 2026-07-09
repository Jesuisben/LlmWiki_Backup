---
title: GET vs POST
created: 2026-07-02
updated: 2026-07-06
type: comparison
tags: [frontend, backend, javascript]
sources:
  - "raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md"
  - "raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어.pdf"
status: growing
confidence: high
---

# GET vs POST

## 비교 목적

상품 상세 페이지 이동과 form 전송 흐름에서 GET/POST가 등장했다. 이 구분은 이후 Spring Controller, REST API, 로그인/상품 등록 요청을 이해하는 기초다.

## 한눈에 보기

| 항목 | GET | POST |
|---|---|---|
| 데이터 위치 | URL query string | HTTP body |
| 주소창 노출 | 보임 | 보통 보이지 않음 |
| 수업 예 | `ProductDetail.html?id=1` | form 제출, 등록 요청 |
| 주 용도 | 조회, 검색, 상세 보기 | 생성, 등록, 로그인, 변경 |

## 핵심 설명

GET은 URL 뒤에 `?id=1`처럼 parameter가 붙는다. 상품 목록에서 상세 페이지로 이동할 때 id를 전달하는 흐름이 이에 해당한다.

POST는 HTTP body에 데이터를 담아 보낸다. 원본은 POST 방식은 parameter가 body에 붙어서 주소창에 직접 보이지 않는다고 설명한다.

## 헷갈리기 쉬운 포인트

- POST라고 해서 무조건 안전한 것은 아니다. 주소창에 안 보일 뿐, HTTPS와 서버 검증이 필요하다.
- GET은 조회에 적합하고, POST는 등록/변경처럼 서버 상태가 바뀌는 요청에 적합하다.
- HTML form의 `method`와 JavaScript/Spring API의 HTTP method는 같은 HTTP 개념으로 이어진다.

## 관련 페이지

- [[concepts/javascript-dom]]
- [[concepts/spring-boot-rest-api]]
- [[comparisons/react-router-vs-spring-api-url]]
- [[summaries/2026-03-26-javascript-dom-product-pages]]

## 출처

- `raw/KoreaICT/3. UI&UX/2026.03.26(목)/2026.03.26(목).md`
- `raw/KoreaICT/3. UI&UX/교육 자료/IT 관련 용어.pdf`
