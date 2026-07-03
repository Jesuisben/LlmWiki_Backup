---
title: Amazon EC2
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [aws, linux, backend]
sources:
  - raw/Study/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md
  - raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: high
---

# Amazon EC2

## 무엇인가

Amazon EC2(Elastic Compute Cloud)는 AWS에서 가상 서버 인스턴스를 빌려 쓰는 Compute 서비스다. AMI로 운영체제 템플릿을 고르고, 인스턴스 타입으로 CPU/메모리 규모를 정하며, Key Pair로 SSH 접속한다.

## 이 위키에서의 맥락

EC2는 Linux 수업에서 다룬 서버 운영 지식을 AWS 위로 옮기는 중심 서비스다. 수업에서는 `EDU-PUBLIC-EC2-2A`, `EDU-PUBLIC-EC2-2C` 두 인스턴스를 만들어 Nginx, Spring Boot, RDS 연결, Load Balancer 대상 등록을 실습했다.

## 핵심 기능 / 특징

- AMI: EC2를 만들 때 사용하는 OS/소프트웨어 템플릿.
- Key Pair: SSH 접속에 쓰는 공개키/개인키 쌍. `.pem` 파일은 노출되면 안 된다.
- Public IP / Private IP: 외부 접속 주소와 VPC 내부 주소.
- Elastic IP: EC2에 고정해 붙일 수 있는 공인 IP. 연결하지 않고 방치하면 비용 문제가 생길 수 있다.
- Security Group: EC2 인바운드/아웃바운드 포트 제어.
- Target 등록: Load Balancer나 Target Group이 요청을 보낼 대상 서버가 된다.

## 학습 이력

- [[summaries/2026-05-06-aws-cloud-vpc-ec2|2026-05-06]]: EC2 메뉴, AMI, Key Pair, Security Group, Public/Private IP 개념을 VPC 학습과 함께 확인.
- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07]]: 두 EC2 생성, SSH 접속, ping/ICMP, Nginx 설치, Spring Boot 실행, RDS 접속.
- [[summaries/2026-05-08-aws-route53-load-balancer-https|2026-05-08]]: 두 EC2를 CLB/ALB 대상 서버로 등록하고 도메인/HTTPS 구조 뒤에 배치.

## 관련 개념

- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[entities/linux|Linux]]
- [[entities/aws|AWS]]

## 출처

- `raw/Study/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md`
- `raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/Study/6. AWS/교육 자료/AWS 기초 용어.pdf`
- `raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
- `raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
