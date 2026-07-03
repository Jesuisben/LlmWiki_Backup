---
title: AWS Route 53, Load Balancer, HTTPS 흐름
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [aws, backend, auth]
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

# AWS Route 53, Load Balancer, HTTPS 흐름

## 정의

AWS Route 53, Load Balancer, HTTPS 흐름은 사용자가 도메인으로 접속하면 DNS가 Load Balancer 주소를 알려주고, Load Balancer가 여러 EC2 중 하나로 요청을 보내며, ACM 인증서를 통해 HTTPS 통신을 제공하는 배포 구조다.

## 전체 흐름

```text
사용자
  ↓ 도메인 입력
Route 53 DNS
  ↓ Load Balancer DNS 이름 반환
ALB/CLB
  ↓ Listener 80/443
Target EC2로 요청 분산
  ↓ 필요 시 JDBC
RDS MySQL
```

## 구성요소별 역할

| 구성요소 | 역할 | 수업 예시 |
|---|---|---|
| Domain | 사람이 읽는 서비스 주소 | root domain, `www` subdomain |
| Route 53 | DNS hosted zone과 record 관리 | NS, A/Alias, CNAME |
| ACM | SSL/TLS 인증서 발급·DNS 검증 | HTTPS 443 Listener에 연결 |
| CLB | 기본적인 로드밸런서 실습 | `EDU-CLB` |
| ALB | HTTP/HTTPS 애플리케이션 로드밸런서 | `EDU-ALB`, `EDU-ALB-TG` |
| Target Group | ALB가 요청을 보낼 EC2 묶음 | 2A/2C EC2 |
| Security Group | Load Balancer/EC2 포트 제어 | 80, 443 허용 |

## DNS와 HTTPS 적용 순서

1. 도메인 등록기관에서 도메인을 준비한다.
2. Route 53 hosted zone을 생성한다.
3. Route 53의 NS record를 도메인 등록기관의 name server 설정에 반영한다.
4. Load Balancer를 만들고 EC2 대상 또는 Target Group을 연결한다.
5. ACM에서 인증서를 요청한다.
6. ACM DNS 검증용 CNAME record를 Route 53에 추가한다.
7. ALB Listener 443에 인증서를 연결한다.
8. Route 53 A/Alias 또는 CNAME record로 도메인을 Load Balancer에 연결한다.

## 왜 중요한가

IP 주소로 서버에 접속하는 단계는 개발/실습 단계에 가깝다. 실제 웹서비스는 도메인, HTTPS, 로드밸런싱, 헬스체크가 필요하다. 특히 로그인·토큰·쿠키를 다루는 웹서비스는 HTTPS가 없으면 인증 정보가 노출될 수 있어 [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]과도 연결된다.

## 자주 헷갈리는 점

- Route 53은 요청을 직접 처리하지 않고 이름을 해석한다.
- Load Balancer는 실제 요청을 받아 EC2로 분산한다.
- ACM 인증서는 발급 후 ALB Listener에 연결해야 HTTPS가 동작한다.
- DNS 검증용 CNAME과 서비스 접속용 A/Alias record는 목적이 다르다.
- CLB도 쓸 수 있지만, HTTP/HTTPS 서비스에서는 ALB의 Listener/Target Group 구조를 이해하는 것이 더 중요하다.
- Load Balancer의 Security Group과 EC2의 Security Group은 각각 따로 확인해야 한다.

## 관련 개념

- [[summaries/2026-05-08-aws-route53-load-balancer-https|2026-05-08 AWS Route 53, Load Balancer, HTTPS]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]
- [[entities/amazon-route-53|Amazon Route 53]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]

## 출처

- `raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf`
- `raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
- `raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
