---
title: JWT RS256 키 흐름
created: 2026-07-03
updated: 2026-07-19
type: concept
tags: [auth, spring-boot, backend]
sources:
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
status: stable
confidence: high
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

## 단계 9 가이드에서의 적용 위치

1. 별도 짧은 문서는 RSA private/public key를 생성하고 application 설정에 넣기 위한 문자열 형태로 준비하는 명령 절차를 제시한다.
2. CI/CD 가이드는 Spring의 JWT utility가 배포 환경에서 주입된 key를 읽어 private key로 서명하고 public key로 검증하도록 바꾸는 Java snippet을 제시한다.
3. GitHub Secrets 예시는 두 key의 **역할 이름**을 배포 설정 목록에 포함한다.

이 세 문서는 생성→보관→주입→application parsing이라는 설계를 연결하지만, 생성된 key file·encoded 값·독립 Java source·실제 JWT·검증 log는 보존하지 않는다. 따라서 “RS256 적용 절차가 문서화됨”과 “중간 프로젝트가 RS256 token을 발급·검증함”을 구분한다.

## 신뢰 흐름과 완료 조건

| 단계 | 책임 | 확인해야 할 결과 |
|---|---|---|
| key 생성 | private/public key pair 준비 | 실제 file 존재와 권한; 값은 출력하지 않음 |
| Secret 저장 | 배포 환경에 key material 보관 | 이름·형식·line break가 consumer 요구와 일치 |
| 서명 | 발급 component가 private key 사용 | token header의 algorithm과 signature 생성 |
| 검증 | 검증 component가 public key 사용 | 유효 token 통과, 변조·잘못된 key token 거절 |
| application 인증 | Claim을 Authentication으로 변환 | SecurityContext 구성 |
| 인가 | endpoint·resource 정책 평가 | 허용/거절 시나리오 |

외부 Passwordless 승인 결과가 있더라도 이 표의 서명·검증·application 인증·인가는 자동 완료되지 않는다.

## 자주 헷갈리는 점

- 공개키는 공개 가능하다는 뜻이지, 아무렇게나 관리해도 된다는 뜻은 아니다.
- 개인키를 저장소에 올리면 즉시 폐기/재발급해야 한다.
- JWT 서명 알고리즘은 프론트엔드 화면 기능이 아니라 백엔드 인증 신뢰 구조와 관련된다.
- RS256 key pair를 만들었다는 사실과 Spring이 올바른 algorithm으로 token을 발급·검증했다는 사실은 다르다.
- public key 검증이 성공해도 token의 Claim이 곧바로 모든 endpoint 권한을 주는 것은 아니다.

## 관련 개념

- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]

## 출처

- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
