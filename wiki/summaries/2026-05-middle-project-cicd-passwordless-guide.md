---
title: 중간 프로젝트 CI/CD·배포·Passwordless 가이드
created: 2026-07-03
updated: 2026-07-19
type: summary
tags: [project, ci-cd, aws, auth, spring-boot, react]
sources:
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md
  - raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md
status: stable
confidence: high
---

# 중간 프로젝트 CI/CD·배포·Passwordless 가이드

## 한 줄 요약

중간 프로젝트용 문서 4개는 Spring Boot·React를 AWS와 Docker 위에 배포하고 Passwordless를 연결하는 **구현·운영 가이드와 설정 목록**이다. 일부 shell·인증서·container 출력, 거부 HTTP 응답, 성공·실패 관찰 서술은 Markdown 안에 보존돼 있다. 그러나 독립 project source, workflow run log, end-to-end browser·API·DB 결과 artifact는 없으므로 전체 통합 완료 기록으로 읽지 않는다.

## 자료별 역할

| 자료 | 소유하는 내용 | 소유하지 않는 증거 |
|---|---|---|
| CI/CD·배포 가이드 | backend→Docker/AWS→Actions→frontend/Nginx→file/S3→domain/ALB 순서, embedded code/config와 짧은 성공·연결 관찰 서술 | 실제 repository file, Actions run, image digest, 재현 가능한 배포 log·cloud 상태 |
| GitHub Secrets 예시 | registry·server·DB·JWT·object storage 설정의 역할 목록 | 실제 Secret 값, 등록 화면, workflow 주입 성공 |
| RS256 생성 방법 | private/public key 생성·인코딩 절차 | 생성된 key file·encoded value, application 서명/검증 결과 |
| Passwordless 적용 가이드 | 인증 server 준비, 서비스 등록, Spring REST 계층, React polling UI, 배포 점검 절차·embedded snippet·일부 인프라 출력과 초기 실패 관찰 | 독립 project source/build, 최종 승인·JWT 로그인·배포 시나리오 결과 |

네 문서는 모두 학습자가 프로젝트에 옮겨 적용하기 위한 설계·절차 자료다. Markdown 안의 Java·TypeScript·YAML·Dockerfile·Nginx·shell 조각은 구체적이지만, 별도 source/config/script artifact가 아니며 현재 repository에 실제 배치·실행됐다는 증거도 아니다.

## 전체 흐름

### 1. 기존 프로젝트를 배포 가능한 구조로 정리

가이드는 Spring의 CORS·properties·JWT key loading과 build 이름, backend Dockerfile을 정리하고 local 실행을 선행 조건으로 둔다. 이후 AWS network·server·database를 준비하고 Docker를 설치한 뒤, GitHub Secrets와 backend CI/CD workflow를 연결하는 순서다. 문서 초반에는 관리형 DB 계획이 섞여 있지만 상세 절차와 마지막 연결은 VM 내부 DB container·SSH tunnel을 사용하므로, 최종 채택 토폴로지는 raw만으로 확정할 수 없다. 이 순서는 [[summaries/2026-05-11-cicd-github-actions-spring-boot|05-11 CI/CD 수업]]을 중간 프로젝트의 backend/frontend·DB·JWT·file 요구사항으로 확장한다.

### 2. backend image와 server 갱신 자동화

CI는 source를 checkout해 application artifact와 Docker image를 만들고 registry에 전달하도록 설계됐다. backend Dockerfile의 package 과정은 test를 생략하므로 별도 test 성공 근거가 아니다. CD는 server에 접속해 새 image를 받아 container를 교체하도록 설명한다. DB URL은 workflow에서 주입하지만 제시된 application 설정의 소비 표현과 맞지 않는다. 이 폴더에는 Actions run, test report, registry digest, 재현 가능한 원격 배포 log와 API 응답이 없으므로 workflow 정의와 run·application 성공을 분리해야 한다.

### 3. React·Nginx를 같은 서비스 접점에 연결

frontend는 API 주소를 환경별로 나누고, local Vite proxy와 배포 Nginx proxy를 별도 설정한다. React image용 Dockerfile과 CI/CD workflow도 문서 안에 제시된다. `/api`와 file 경로를 proxy하는 설정은 **요청 경로 설계**이며, 실제 React build·image push·Nginx reload·browser 왕복 결과는 보존되지 않았다.

### 4. file 저장을 local에서 object storage로 확장

가이드는 Spring dependency·properties·file service·multipart controller/service와 React file form을 연결한 뒤, local file 저장에서 object storage로 전환하는 절차를 제시한다. object URL을 DB에 보관하는 역할도 설명하지만 실제 object listing, HTTP response, DB row는 없다. [[concepts/aws-s3-file-upload|S3 파일 업로드 흐름]]의 05-13 수업 관찰도 이 프로젝트의 실행 결과를 대신하지 않는다.

### 5. domain·HTTPS·load balancer로 외부 접점 설계

DNS, certificate, Target Group, ALB, record 연결 순서가 이어진다. 이는 [[summaries/2026-05-12-route53-alb-https-review|05-12 수업]]의 후속 설계다. 문서의 생성·확인 절차만으로 certificate 발급, healthy target, DNS 조회, HTTPS browser 응답이 실제 완료됐다고 판단하지 않는다.

### 6. Passwordless를 기존 회원·JWT 흐름에 삽입

Passwordless 가이드는 별도 인증 server를 준비하고 서비스를 등록한 뒤, Spring의 설정→Member 등록 상태→REST client/common response→DTO→Service→Controller→SecurityConfig 순서와 React API helper→로그인 선택 UI→등록/해제→결과 polling을 제시한다. 원격 shell·인증서·container 파일 출력, 외부 REST 경로의 거부 응답, MIME 처리 실패 관찰도 남아 있다. 이는 인프라 도달·초기 연동 문제의 부분 증거이며 최종 인증 성공이 아니다. 외부 callback 구현은 없고, 승인 결과를 사용자·hash/random·challenge/session·만료와 결속한 뒤 JWT를 발급했다는 runtime 증거도 없다.

## 핵심 개념

- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]
- [[concepts/passwordless-x1280-auth-flow|Passwordless X1280 인증 흐름]]
- [[concepts/passwordless-qr-app-approval|Passwordless QR/앱 승인 흐름]]
- [[concepts/spring-boot-passwordless-integration|Spring Boot Passwordless 인증 연동]]
- [[concepts/github-actions-secrets-deploy|GitHub Actions Secrets 기반 배포]]
- [[concepts/jwt-rs256-key-flow|JWT RS256 키 흐름]]

## 실습 / 예제

| 단계 | 문서에 있는 것 | 완료를 위해 별도로 남겨야 할 결과 |
|---|---|---|
| source·config 준비 | Java/TypeScript/properties/XML/Dockerfile/Nginx snippet | 실제 project file과 local test 결과 |
| CI | workflow template와 Secret 역할 | job log, test/build 결과, image digest |
| CD | server 접속·container 교체 절차 | remote log, container/port 상태, API 응답 |
| frontend | React build·proxy·workflow 설계 | build artifact, Nginx 상태, browser 왕복 |
| file/S3 | multipart·service·storage 전환 snippet | object·HTTP response·DB row |
| Passwordless | REST 계층·Member 상태·SecurityConfig·polling UI snippet | API response, 등록/승인/해제 시나리오, JWT/session, protected endpoint 결과 |
| cloud 접점 | network·DNS·certificate·ALB 절차 | resource 상태, target health, DNS/HTTPS 응답 |

따라서 이 Summary가 보존하는 핵심 artifact는 **네 Markdown 설계 문서와 그 안의 연속 snippet·부분 출력·관찰 서술**이다. Docker image, JAR, frontend build, workflow run, key file, cloud resource export, screenshot 같은 독립 실행 artifact는 0개다.

## 증거 수준별 재분류

| 수준 | 단계 9 raw에 남은 것 | 해석 한계 |
|---|---|---|
| Embedded 구현안 | workflow·Dockerfile·properties·Java·TypeScript·Nginx·SQL·명령 snippet | 실제 repository file·compile/build를 증명하지 않음 |
| 구체 출력 | 일부 원격 shell, 인증서·container 파일, 거부 HTTP 응답 | 특정 단계 도달·파일 존재·거부 상태만 증명 |
| 관찰·성공 서술 | 단일 접점·local file·DB client 연결 등 짧은 문장 | 재현 log·응답·listing이 없어 end-to-end 증거가 아님 |
| 실패 관찰 | Spring MIME 처리 문제 | 문제 발생은 보존됐지만 수정 후 성공은 미보존 |
| 조건·확인 지시 | Actions·container·API·S3·DNS/ALB·Passwordless 시나리오 대부분 | 실제 수행 결과가 아님 |

원본 내부에도 불일치가 있다. DB는 관리형 계획과 VM container 절차가 섞이고, object 삭제 snippet과 “삭제되지 않는다”는 설명이 충돌하며, Passwordless Secret 등록 목록과 container 전달 항목도 완전히 맞지 않는다. 실제 project source와 실행 결과가 없으므로 한쪽을 최종 구현으로 확정하지 않는다.

## 헷갈린 점 / 질문

- **작성됨 vs 적용됨:** 가이드에 완성형처럼 보이는 code가 있어도 실제 project file·commit·build가 없으면 적용 완료가 아니다.
- **workflow 정의 vs run 성공:** YAML과 Secrets 항목이 있어도 checkout·test/build·registry·SSH·container 단계의 실제 결과는 별도다.
- **container 실행 vs 서비스 성공:** container 상태는 application readiness·API·browser·DB 성공을 자동 보장하지 않는다.
- **외부 인증 성공 vs project login:** 앱 승인 결과 뒤 JWT/session 생성과 endpoint 인가는 application이 별도로 완료해야 한다.
- **단계 8 vs 단계 9:** 05-14~21 Passwordless 실습 결과를 중간 프로젝트 결과로 소급하지 않고, 단계 9 가이드 snippet도 05월 날짜 수업의 직접 구현으로 되돌려 쓰지 않는다.
- **HS256 vs RS256:** RS256은 private key 서명과 public key 검증을 분리하지만, 생성 명령이 있다는 사실만으로 project token 발급·검증 성공을 확정하지 않는다.

## 선행·후속 학습 경계

- **Linux 선행:** process/service/port, Docker image/container/network, Nginx proxy, Git/GitHub가 실행 기반이다.
- **AWS 직접 수업:** VPC·EC2·RDS와 비용·자원 생명주기를 배웠다.
- **CI/CD 직접 수업:** Actions/Maven·image·EC2 CD, DNS/HTTPS/ALB, Terraform/S3 절차와 제한된 관찰을 배웠다.
- **Passwordless 직접 수업:** 인증 제품·server·sample·REST contract를 배웠다.
- **단계 9 직접 범위:** 위 선행 내용을 하나의 중간 프로젝트에 적용하기 위한 설계·snippet·점검 순서다.
- **후속 확정점:** 실제 repository의 file, workflow run, container/cloud/API/browser/DB 관찰을 확보해야 구현·배포·통합 완료를 선언할 수 있다.

## 관련 페이지

- [[entities/aws|AWS]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/react|React]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]
- [[summaries/2026-05-14-passwordless-x1280-intro|2026-05-14 Passwordless X1280 소개와 보안 배경]]
- [[summaries/2026-05-21-passwordless-x1280-rest-api|2026-05-21 Passwordless X1280 REST API와 Postman]]

## 출처

- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/중간 프로젝트 cicd 및 배포 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/패스워드리스 적용/중간 프로젝트 패스워드리스 적용 가이드.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/Github_Secrets 예시.md`
- `raw/KoreaICT/9. 중간 프로젝트 공부/CICD/JWT(RS256)생성 방법.md`
