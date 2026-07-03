---
title: 2026-05-08 AWS Route 53, Load Balancer, HTTPS
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [aws, backend, auth, curriculum, study-log]
sources:
  - raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: high
---

# 2026-05-08 AWS Route 53, Load Balancer, HTTPS

## 한 줄 요약

두 EC2에 올린 웹 애플리케이션을 도메인, Route 53, Load Balancer, ACM 인증서, HTTPS로 묶어 실제 서비스 주소에 가까운 배포 구조로 확장한 날이다.

## 배운 내용

- 전날 만든 `Public2A`, `Public2C` EC2에 접속 가능한 상태를 확인했다.
- EC2 간 ping 실패 원인을 Security Group의 ICMP 허용 여부로 파악했다.
- Nginx 설치, 정적 홈페이지 교체, Spring Boot jar 실행을 두 EC2에서 반복했다.
- RDS MySQL을 만들고 두 EC2의 Spring Boot가 하나의 RDS를 공유하는 구조를 확인했다.
- 도메인 등록기관에서 도메인을 준비하고, Route 53 hosted zone의 NS를 등록기관 쪽에 반영하는 흐름을 배웠다.
- Route 53 record를 통해 도메인이 Load Balancer DNS 이름을 가리키게 했다.
- Classic Load Balancer(CLB)와 Application Load Balancer(ALB)를 모두 다뤘다.
- ACM(AWS Certificate Manager)으로 SSL/TLS 인증서를 요청하고 DNS 검증용 CNAME을 Route 53에 추가했다.
- ALB의 HTTPS 443 Listener에 ACM 인증서를 연결해 `https://...` 접속 구조를 만들었다.

## 핵심 실습 / 예제

최종 배포 흐름은 다음처럼 정리할 수 있다.

```text
사용자 브라우저
  ↓ https://도메인
Route 53 Hosted Zone
  ↓ A/Alias 또는 CNAME record
ALB 또는 CLB
  ↓ Listener 80/443
Target Group 또는 등록된 EC2
  ↓ HTTP/Spring Boot
EDU-PUBLIC-EC2-2A, EDU-PUBLIC-EC2-2C
  ↓ JDBC
RDS MySQL
```

도메인과 HTTPS 적용 순서는 다음과 같다.

1. 도메인 등록기관에서 도메인을 준비한다.
2. Route 53 hosted zone을 만들고, 발급된 NS record를 도메인 등록기관에 반영한다.
3. Load Balancer를 만들고 두 EC2를 대상으로 등록한다.
4. ACM에서 인증서를 요청한다.
5. ACM DNS 검증용 CNAME record를 Route 53에 추가한다.
6. ALB Listener 443에 인증서를 연결한다.
7. Route 53 record가 Load Balancer DNS 이름을 가리키게 한다.
8. 브라우저에서 root domain과 `www` domain의 HTTP/HTTPS 접속을 확인한다.

## 왜 중요한가

EC2 Public IP로 접속하는 것은 실습 단계에서는 충분하지만, 실제 웹서비스는 사람이 기억할 수 있는 도메인, 장애/부하를 대비한 로드밸런싱, 인증 정보를 보호하는 HTTPS가 필요하다. 이 날의 내용은 이후 CI/CD와 Passwordless/auth 배포에서 “어디로 사용자가 접속하고, HTTPS가 어디서 끝나며, 요청이 어떤 서버로 흘러가는가”를 이해하는 기반이 된다.

## 헷갈린 점 / 질문

- Route 53은 서버가 아니라 DNS 서비스다. 요청을 직접 처리하지 않고 “이 도메인은 어느 Load Balancer로 가야 하는지”를 알려준다.
- Load Balancer는 실제 HTTP/HTTPS 요청을 받아 여러 EC2로 분산한다.
- ACM 인증서를 만들었다고 HTTPS가 자동 적용되는 것은 아니며, ALB의 HTTPS Listener에 인증서를 연결해야 한다.
- DNS 검증용 CNAME record와 서비스 접속용 A/Alias record는 목적이 다르다.
- CLB는 로드밸런싱의 기초 구조를 익히기 좋고, ALB는 Target Group, Listener, Health Check, host/path 기반 라우팅 등 웹서비스 운영에 더 가까운 모델이다.

## 관련 페이지

- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]
- [[entities/amazon-route-53|Amazon Route 53]]
- [[entities/aws|AWS]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]

## 출처

- `raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md` — EC2 확인, ping/ICMP, Nginx/Spring Boot, RDS, 도메인/로드밸런서 흐름 메모
- `raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf` — DNS, Route 53, ACM, Load Balancer 용어
- `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf` — Route 53, ACM, CLB, ALB, Target Group, Listener 실습
- `raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf` — Domain/DNS/RDS/Load Balancer 관련 이론
- `raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf` — ALB/CLB와 EC2 연결 구조 요약
- `raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md` — CLB/ALB/Target Group/Security Group 실습 리소스 이름
