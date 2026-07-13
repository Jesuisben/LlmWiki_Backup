---
title: 인증(Authentication) vs 인가(Authorization)
created: 2026-07-13
updated: 2026-07-13
type: comparison
tags: [auth, backend, spring-boot]
sources:
  - raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md
  - raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md
status: growing
confidence: high
---

# 인증(Authentication) vs 인가(Authorization)

## 비교 목적

로그인에 성공했는지와 로그인한 사용자가 특정 기능을 수행할 수 있는지는 다른 질문이다. Passwordless 수업의 AAM/APE 실습과 Spring/JWT 학습을 연결하기 위해 두 책임을 구분한다.

## 한눈에 보기

| 항목 | 인증(Authentication) | 인가(Authorization) |
|---|---|---|
| 확인 질문 | 당신은 누구인가? | 당신은 무엇을 할 수 있는가? |
| 처리 시점 | 로그인·인증기 등록·토큰 검증 등 | 인증 이후 특정 URL·기능·데이터 접근 시 |
| Passwordless 수업 예 | 앱 승인, 인증기 등록, AAM/APE 사용자 확인 | 사용자·부서·정책에 따른 관리 범위 설정 |
| Spring 프로젝트 예 | JWT 또는 외부 인증 결과 검증 | 관리자 상품 수정, 일반 사용자 주문 조회 같은 권한 판단 |

## 언제 무엇을 쓰는가

인증은 비밀번호, 앱 승인, OTP, 토큰처럼 사용자가 주장한 신원을 확인할 때 쓴다. 인가는 인증이 끝난 뒤 역할(role), 정책(policy), 소유자 여부를 기준으로 요청을 허용하거나 거절할 때 쓴다.

예를 들어 Passwordless 앱 승인이 성공해도 모든 관리자 기능을 수정할 수 있는 것은 아니다. 로그인 성공은 인증 결과이고, 상품 가격 수정 가능 여부는 인가 규칙의 결과다.

## 헷갈리기 쉬운 포인트

- 인증과 인가는 순서상 자주 이어지지만 같은 기능이 아니다.
- Passwordless는 인증 방식을 바꾸는 기술이다. 그것만으로 권한 정책이 생기지는 않는다.
- AAM/APE 수업의 사용자·부서·정책 관리 흐름은 인증기 등록뿐 아니라 인증 이후 관리 체계를 생각하게 하는 연결점이다. 다만 원본에 없는 세부 권한 모델을 추정하지 않는다.

## 관련 페이지

- [[summaries/2026-05-19-aam-ape-authentication-filingbox|2026-05-19 인증 기본과 AAM/APE 통합 설치]]
- [[entities/aam-ape|AAM과 APE]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/spring-security-jwt-filter|Spring Security JWT Filter]]

## 출처

- `raw/KoreaICT/8. Passwordless/2026.05.19(화)/2026.05.19(화).md`
- `raw/KoreaICT/4. FrontEnd_BackEnd/2026.04.06(월)/2026.04.06(월).md`
