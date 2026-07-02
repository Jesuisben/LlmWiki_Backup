---
title: 2026-04-07 회원 API와 문자열/토큰 처리
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [spring-boot, react, typescript, frontend, backend, curriculum, study-log]
sources:
  - raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf
  - raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf
status: growing
confidence: high
---
# 2026-04-07 회원 API와 문자열/토큰 처리

## 한 줄 요약

회원 API 구현 중 Bearer 토큰 문자열 처리와 Spring Security 인증 컨텍스트 흐름을 배웠다.

## 커리큘럼 위치와 흐름

전날 JWT 개념을 배운 뒤, 실제 Spring Boot 코드에서 토큰을 꺼내 인증 객체로 연결하는 단계다. 문자열 메서드와 보안 필터가 함께 등장해 단순 문법 지식이 인증 구현으로 이어진다.

## 배운 내용

- `JwtAuthenticationFilter`를 만들고 요청 헤더에서 `Bearer ` 접두사를 제거해 JWT 본문만 추출하는 흐름을 다뤘다.
- SpringBoot 교안 p.164~165는 `Authentication`과 `SecurityContextHolder`가 인증 사용자, 권한, 인증 여부를 보관하는 구조임을 설명한다.
- `SecurityContextHolder.getContext()` 안의 Authentication이 현재 요청의 로그인 사용자 정보를 담는 핵심 위치다.

## 핵심 실습 / 예제

- `OncePerRequestFilter` 기반 필터에서 토큰을 검사하고, 유효하면 Authentication을 만들어 SecurityContext에 넣는 흐름으로 이해할 수 있다.
- Bearer 토큰 처리는 `String` 메서드 사용 예제이면서 동시에 API 인증의 첫 관문이다.

## 교육자료 대조 메모

- 사용자 정리 MD를 주 자료로 삼고, MD에서 언급한 교육자료를 실제 확인해 출처에 추가했다.
- 이번 과목의 큰 흐름은 [[concepts/frontend-backend-architecture|Frontend/Backend 구조]] → [[concepts/spring-boot-rest-api|Spring Boot REST API]] → [[concepts/react-typescript-basics|React와 TypeScript 기본]] → 인증·상품·장바구니·주문·검색 기능 구현으로 이어진다.

## 헷갈린 점 / 질문

- `Bearer `는 토큰 자체가 아니라 Authorization 헤더에서 인증 방식과 토큰을 구분하기 위한 접두사다.
- JWT 검증과 SecurityContext 설정은 Controller에 도달하기 전 필터 단계에서 처리된다.
- Authentication 객체는 “사용자 이름 문자열”만이 아니라 principal, credentials, authorities, authenticated 여부를 함께 가진다.

## 관련 페이지

- [[concepts/spring-security-jwt-filter]]
- [[concepts/jwt-session-cookie-auth]]
- [[entities/jwt]]
- [[concepts/spring-boot-rest-api]]

## 출처

- `raw/Study/4. FrontEnd_BackEnd/2026.04.07(화)/2026.04.07(화).md`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/SpringBoot 교안.pdf`
- `raw/Study/4. FrontEnd_BackEnd/교육 자료/JWT(이론).pdf`
