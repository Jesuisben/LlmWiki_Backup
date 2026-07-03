---
title: CLB vs ALB
created: 2026-07-03
updated: 2026-07-03
type: comparison
tags: [aws, backend]
sources:
  - raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: high
---

# CLB vs ALB

## 비교 목적

AWS 수업에서는 Classic Load Balancer(CLB)와 Application Load Balancer(ALB)가 모두 등장했다. 둘 다 여러 EC2로 요청을 나누지만, 실무적으로는 HTTP/HTTPS 애플리케이션 트래픽을 다루는 ALB의 Listener/Target Group 구조를 이해하는 것이 중요하다.

## 한눈에 보기

| 항목 | CLB | ALB |
|---|---|---|
| 이름 | Classic Load Balancer | Application Load Balancer |
| 수업 리소스 | `EDU-CLB` | `EDU-ALB`, `EDU-ALB-TG` |
| 주요 관점 | 기본 로드밸런서 실습 | HTTP/HTTPS 애플리케이션 요청 처리 |
| 대상 연결 | EC2 중심 | Target Group 중심 |
| HTTPS | 가능하지만 구조가 단순 | Listener 443 + ACM 인증서 연결 흐름이 명확 |
| 실무 학습 포인트 | 로드밸런싱의 기초 | path/host 기반 라우팅, Target Group, Health Check |
| Route 53 연결 | LB DNS 이름을 도메인과 연결 | LB DNS 이름/Alias를 도메인과 연결 |

## 언제 무엇을 쓰는가

- CLB는 “로드밸런서가 두 EC2에 요청을 나눠 보낸다”는 기초 개념을 잡을 때 도움이 된다.
- ALB는 HTTP/HTTPS 웹서비스에서 도메인, 인증서, Target Group, Listener를 함께 구성할 때 더 중요한 모델이다.
- 수업의 후반 구조는 Route 53 도메인이 ALB/CLB를 가리키고, Load Balancer가 `EDU-PUBLIC-EC2-2A`, `EDU-PUBLIC-EC2-2C`로 요청을 분산하는 형태다.

## 헷갈리기 쉬운 포인트

- Load Balancer는 DNS 이름을 가지며, EC2 Public IP를 직접 외우지 않게 해 준다.
- ALB의 Target Group은 “요청을 보낼 대상 EC2 묶음”이다.
- Listener는 80/443 같은 포트로 들어온 요청을 어떤 Target Group으로 보낼지 정한다.
- ACM 인증서는 ALB의 HTTPS Listener에 연결해야 브라우저에서 HTTPS가 동작한다.
- Load Balancer Security Group이 80/443을 열어도, 뒤쪽 EC2 Security Group이 대상 포트를 허용하지 않으면 요청이 실패할 수 있다.

## 관련 페이지

- [[summaries/2026-05-08-aws-route53-load-balancer-https|2026-05-08 AWS Route 53, Load Balancer, HTTPS]]
- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[entities/amazon-route-53|Amazon Route 53]]
- [[entities/aws|AWS]]

## 출처

- `raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
