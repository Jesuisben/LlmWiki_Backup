---
title: JWT RS256 키 흐름
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [auth, spring-boot, backend]
sources:
  - D:/Study_LLM_Wiki/raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md
  - D:/Study_LLM_Wiki/raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
status: growing
confidence: medium
---

# JWT RS256 키 흐름

## 정의

JWT RS256은 RSA 비대칭키를 사용해 JWT에 서명하고 검증하는 방식이다. 개인키(private key)로 토큰을 서명하고 공개키(public key)로 검증한다.

## 왜 중요한가

HS256처럼 하나의 비밀키를 공유하는 방식과 달리, RS256은 서명 권한과 검증 권한을 분리할 수 있다. 인증 서버가 토큰을 발급하고 여러 서버가 공개키로 검증하는 구조에 어울린다.

## 핵심 설명

- private key: 토큰 발급자가 보관하며 외부에 노출하면 안 된다.
- public key: 검증자가 사용할 수 있는 키다.
- GitHub Secrets나 서버 환경 변수에는 실제 키 값을 안전하게 저장해야 한다.
- 위키에는 키 생성 절차와 역할만 남기고 실제 키 본문은 남기지 않는다.

## 예시 구조

```text
사용자 로그인/승인 → 인증 서버가 private key로 JWT 서명 → 애플리케이션 서버가 public key로 JWT 검증
```

## 자주 헷갈리는 점

- 공개키는 공개 가능하다는 뜻이지, 아무렇게나 관리해도 된다는 뜻은 아니다.
- 개인키를 저장소에 올리면 즉시 폐기/재발급해야 한다.
- JWT 서명 알고리즘은 프론트엔드 화면 기능이 아니라 백엔드 인증 신뢰 구조와 관련된다.

## 관련 개념

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]

## 출처

- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
