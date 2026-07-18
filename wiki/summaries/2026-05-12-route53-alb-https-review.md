---
title: 2026-05-12 Route 53, ALB, HTTPS 복습과 도메인 배포
author: Hermes Agent
created: 2026-07-03
updated: 2026-07-18
type: summary
tags: [aws, ci-cd, backend, curriculum]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
  - raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf
status: growing
confidence: high
---

# 2026-05-12 Route 53, ALB, HTTPS 복습과 도메인 배포

## 한 줄 요약

CI/CD 배포의 앞단 인프라가 되는 도메인, Route 53 hosted zone, ACM 인증서, ALB/Target Group, HTTPS 접속 구성 절차를 기록한 날이다.

## 커리큘럼 위치

전날 [[summaries/2026-05-11-cicd-github-actions-spring-boot|CI/CD와 GitHub Actions]]로 자동 배포 흐름을 다룬 뒤, 이날은 사용자가 접속하는 “서비스 주소” 쪽을 다시 정리했다. 즉, 배포 자동화가 서버 내부 컨테이너를 갱신한다면, Route 53/ALB/HTTPS는 외부 사용자가 안정적인 도메인으로 접속하게 해 주는 앞단 구조다.

## 배운 내용

### 1. 도메인과 Route 53 hosted zone

가비아에서 구매한 도메인을 AWS Route 53 hosted zone과 연결하는 순서를 정리했다.

도메인 신청 → Route 53 hosted zone 생성 → NS record 확인 → 등록기관 name server 연결 → ACM 인증서 요청 → DNS 검증 CNAME 생성 → 인증서 상태 확인 순서로 정리했다. 원본은 각 console 절차와 확인할 상태를 자세히 적지만, 실제 NS 전파 결과나 인증서 세부 상태 출력은 보존하지 않는다.

원본에서는 record를 “도메인 이름과 IP 주소 사이의 연결 정보를 저장하는 단위”로 이해했다. NS record는 도메인의 이름 해석 권한을 AWS Route 53으로 넘기는 데 사용되고, SOA record는 hosted zone의 메타데이터 역할을 한다.

### 2. ACM 인증서와 HTTPS

HTTP보다 HTTPS를 사용하는 이유는 인증 정보와 요청 데이터 보호 때문이다. ACM에서 루트 도메인과 wildcard 도메인(`*.도메인`)을 포함해 인증서를 요청하고, DNS 검증용 CNAME record를 Route 53에 추가한 뒤 인증서 상태가 `발급됨`인지 확인하는 절차를 적었다.

### 3. Load Balancer와 Target Group

Load Balancer는 여러 EC2로 요청을 나누고, 한 서버에 문제가 생겨도 다른 서버가 응답할 수 있게 하는 부하 분산 장치다. 수업에서는 서로 다른 가용 영역의 EC2를 준비하고 Target Group·ALB를 구성하는 순서를 기록했다.

- Target Group: ALB가 요청을 보낼 대상 EC2 묶음.
- ALB Security Group: 외부에서 80/443 접근 허용.
- Listener: HTTP/HTTPS 요청을 받아 Target Group으로 전달.
- ACM 인증서: HTTPS listener에 연결.

### 4. Route 53 A/Alias record

Route 53 hosted zone에서 루트 도메인과 `www` subdomain 각각에 A/Alias record를 만들어 ALB로 연결하는 절차를 적었다. 네 가지 HTTP/HTTPS URL은 확인 대상으로 나열되어 있지만 실제 응답 본문이나 browser 화면은 보존되지 않았다.

### 5. 삭제 순서

실습 종료 후 비용과 리소스 잔존을 막기 위해 Elastic IP, EC2, Load Balancer, Target Group, RDS, Security Group, VPC, ACM 인증서, Route 53 record/hosted zone 등의 삭제 순서를 따로 기록했다.

## 실습 / 예제

1. Route 53 hosted zone과 등록기관 NS 연결 절차를 기록했다.
2. ACM 인증서 요청·DNS 검증 CNAME·`발급됨` 상태 확인 지점을 기록했다.
3. EC2 두 대에 Nginx 정적 페이지를 배치하는 명령을 기록했지만 service/browser 출력은 없다.
4. Target Group·ALB Security Group·ALB·HTTPS Listener·ACM 인증서 연결 순서를 기록했다. Target health 결과는 없다.
5. Route 53 A/Alias record를 ALB에 연결하고 확인할 URL 네 개를 적었다. 실제 HTTP 응답은 보존되지 않았다.
6. 마지막에는 의존 자원 삭제 순서를 적었지만 삭제 완료 상태는 남지 않았다.

### 보존된 결과와 미보존 경계

| 단계 | 원본에 남은 증거 | 판단 |
|---|---|---|
| DNS·ACM | console 입력값과 확인할 상태 | 전파·발급 결과 출력 미보존 |
| EC2 Nginx | install·clone·copy·start 명령 | service·browser 결과 미보존 |
| Target Group·ALB | 생성·등록·HTTPS Listener 절차 | target health·ALB 상태 출력 미보존 |
| Route 53 Alias | 네 가지 확인 URL | 실제 HTTP/HTTPS 응답 미보존 |
| 정리 | 삭제 순서 | 최종 삭제 완료 상태 미보존 |

## 헷갈린 점 / 질문

- Route 53은 웹 서버가 아니라 DNS다. 실제 요청 처리는 ALB와 EC2가 담당한다.
- ACM 인증서를 만들기만 해서는 HTTPS가 되지 않는다. ALB HTTPS listener에 연결해야 한다.
- DNS 검증 CNAME record와 서비스 접속용 A/Alias record는 목적이 다르다.
- CI/CD가 성공해도 도메인/ALB/Target Group/Health Check가 틀리면 사용자는 서비스에 접속하지 못한다.

## 관련 페이지

- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/spring-boot-cicd-docker-ec2-flow|Spring Boot CI/CD Docker-EC2 배포 흐름]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]
- [[entities/aws|AWS]]
- [[entities/amazon-route-53|Amazon Route 53]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/KoreaICT/7. Ci&CD/교육 자료/cloud.03.AWS 교안(이론).pdf`
