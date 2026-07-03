---
title: Amazon Route 53
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [aws, backend]
sources:
  - raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
status: growing
confidence: high
---

# Amazon Route 53

## 무엇인가

Amazon Route 53은 AWS의 DNS 서비스다. 도메인 이름을 IP 주소나 AWS Load Balancer 같은 리소스 주소로 연결하고, hosted zone과 record를 관리한다.

## 이 위키에서의 맥락

EC2 Public IP로 직접 접속하던 실습을 실제 서비스 주소 형태로 바꾸기 위해 Route 53이 등장했다. 수업에서는 외부 도메인 등록기관의 NS를 Route 53으로 연결하고, root domain과 `www` subdomain이 CLB/ALB를 가리키도록 설정했다.

## 핵심 기능 / 특징

- Hosted Zone: 도메인의 DNS record를 관리하는 공간.
- NS Record: 어떤 Name Server가 도메인을 담당하는지 지정.
- A Record: 도메인을 IPv4 또는 AWS alias 대상에 연결.
- CNAME Record: 별칭 도메인을 다른 도메인 이름에 연결.
- Alias Record: AWS Load Balancer 같은 리소스에 도메인을 연결할 때 자주 쓰는 Route 53 기능.
- DNS 검증: ACM 인증서 발급 시 CNAME record로 도메인 소유를 증명.

## 학습 이력

- [[summaries/2026-05-08-aws-route53-load-balancer-https|2026-05-08]]: Route 53 hosted zone, 도메인 등록기관 NS 변경, ACM DNS 검증, Load Balancer record 연결.

## 관련 개념

- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]
- [[entities/aws|AWS]]
- [[concepts/jwt-session-cookie-auth|JWT, 세션, 쿠키 인증]]

## 출처

- `raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf`
- `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
