---
title: Spring Security JWT Filter
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [spring-boot, auth, backend]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf
status: growing
confidence: high
---
# Spring Security JWT Filter

## 정의

Spring Security JWT Filter는 API 요청이 Controller에 도달하기 전에 Authorization 헤더의 Bearer 토큰을 검사하고, 유효한 사용자 정보를 SecurityContext에 넣는 필터 흐름이다.

## 왜 중요한가

로그인 이후의 API 요청은 “이 사용자가 누구인지”를 알아야 장바구니, 주문, 관리자 기능을 안전하게 처리할 수 있다. JWT 필터는 매 요청마다 토큰을 확인해 현재 요청의 인증 상태를 구성한다.

## 핵심 설명

수업에서는 `JwtAuthenticationFilter`를 작성하고 `Bearer ` 접두사를 제거해 JWT 토큰만 추출하는 흐름을 다뤘다. SpringBoot 교안 p.164~165는 `Authentication`과 `SecurityContextHolder`를 설명한다.

```text
HTTP 요청 Authorization: Bearer <token>
→ JwtAuthenticationFilter
→ Bearer 접두사 제거
→ JwtTokenProvider로 검증
→ Authentication 생성
→ SecurityContextHolder.getContext().setAuthentication(...)
→ Controller/Service에서 현재 사용자 활용
```

## 수업 예시

- [[summaries/2026-04-07-member-api-string-token|2026-04-07]] — `JwtAuthenticationFilter`, `SecurityContextHolder`, `Authentication` 흐름을 다뤘다.

## 자주 헷갈리는 점

- Bearer는 토큰의 일부가 아니라 인증 방식 표시다.
- SecurityContext는 전역 사용자 저장소가 아니라 현재 보안 컨텍스트에서 인증 정보를 꺼내는 통로로 이해해야 한다.
- JWT 검증에 성공해도 권한(`authorities`)이 부족하면 특정 API 접근은 막힐 수 있다.

## 관련 개념

- [[concepts/jwt-session-cookie-auth]]
- [[comparisons/session-vs-cookie-vs-jwt]]
- [[entities/jwt]]
- [[concepts/spring-boot-rest-api]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf`
