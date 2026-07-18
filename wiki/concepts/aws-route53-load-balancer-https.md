---
title: AWS Route 53, Load Balancer, HTTPS 흐름
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [aws, backend, auth]
sources:
  - raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
status: growing
confidence: high
---

# AWS Route 53, Load Balancer, HTTPS 흐름

## 정의

AWS Route 53, Load Balancer, HTTPS 흐름은 6. AWS의 VPC·EC2 기반 위에, 7. CI/CD 2026-05-12에 절차를 기록한 도메인·DNS·ACM·ALB 앞단 배포 구조다.

## 전체 흐름

사용자가 도메인을 입력하면 Route 53 DNS가 ALB alias 대상으로 안내하고, ALB의 HTTPS Listener가 요청을 Target Group의 EC2로 전달한다. RDS는 애플리케이션이 필요할 때 JDBC로 접근하는 데이터 계층이지 DNS·로드밸런싱 경로 자체의 다음 홉은 아니다.

## 구성요소별 역할

| 구성요소 | 역할 | 수업 예시 |
|---|---|---|
| Domain | 사람이 읽는 서비스 주소 | root domain, `www` subdomain |
| Route 53 | DNS hosted zone과 record 관리 | NS, A/Alias, CNAME |
| ACM | SSL/TLS 인증서 발급·DNS 검증 | HTTPS 443 Listener에 연결 |
| CLB | 기존형 로드밸런서 비교 항목 | 날짜 원본의 관리 표에 이름만 기록 |
| ALB | HTTP/HTTPS 애플리케이션 로드밸런서 | Target Group·HTTPS Listener 구성 절차 기록 |
| Target Group | ALB가 요청을 보낼 EC2 묶음 | 2A/2C EC2 |
| Security Group | Load Balancer/EC2 포트 제어 | 80, 443 허용 |

## DNS와 HTTPS 적용 순서

1. 도메인 등록기관에서 도메인을 준비한다.
2. Route 53 hosted zone을 생성한다.
3. Route 53의 NS record를 도메인 등록기관의 name server 설정에 반영한다.
4. ACM에서 인증서를 요청하고 DNS 검증용 CNAME record를 Route 53에 추가한다.
5. 인증서 상태가 `발급됨`인지 확인한다.
6. Target Group과 ALB를 만들고 EC2 대상을 연결한다.
7. ALB HTTPS Listener 443에 ACM 인증서를 연결한다.
8. Route 53 A/Alias record로 루트 도메인과 `www` 이름을 Load Balancer에 연결한다. 이 수업의 CNAME은 ACM DNS 검증용이므로 서비스 Alias와 목적을 섞지 않는다.

## 수업 증거의 경계

05-12 원본에는 hosted zone·NS·ACM CNAME·Target Group·ALB·Alias 생성 절차와 확인할 URL이 있다. 그러나 DNS 전파, 인증서 발급 상세, target health, ALB 상태, HTTP/HTTPS 응답 본문은 출력이나 화면으로 보존되지 않았다. 따라서 이 페이지는 구성 순서와 완료 조건을 설명하되 실제 운영 성공을 확정하지 않는다.

## 왜 중요한가

IP 주소로 서버에 접속하는 단계는 개발/실습 단계에 가깝다. 실제 웹서비스는 도메인, HTTPS, 로드밸런싱, 헬스체크가 필요하다. 특히 로그인·토큰·쿠키를 다루는 웹서비스는 HTTPS가 없으면 인증 정보가 노출될 수 있어 [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]과도 연결된다.

## 자주 헷갈리는 점

- Route 53은 요청을 직접 처리하지 않고 이름을 해석한다.
- Load Balancer는 실제 요청을 받아 EC2로 분산한다.
- ACM 인증서는 DNS 검증을 통과해 발급된 뒤 ALB HTTPS Listener에 연결해야 HTTPS가 동작한다.
- DNS 검증용 CNAME과 서비스 접속용 A/Alias record는 목적이 다르다.
- CLB도 쓸 수 있지만, HTTP/HTTPS 서비스에서는 ALB의 Listener/Target Group 구조를 이해하는 것이 더 중요하다.
- Load Balancer의 Security Group과 EC2의 Security Group은 각각 따로 확인해야 한다.

## 관련 개념

- [[summaries/2026-05-12-route53-alb-https-review|2026-05-12 Route 53, ALB, HTTPS 복습과 도메인 배포]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]
- [[entities/amazon-route-53|Amazon Route 53]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]

## 출처

- `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
- `raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md`
