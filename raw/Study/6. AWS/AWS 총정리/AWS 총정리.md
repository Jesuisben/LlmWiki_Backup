---
title: AWS 총정리
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [aws, backend, ci-cd, study-log]
sources:
  - D:/Study_LLM_Wiki/raw/Study/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md
  - D:/Study_LLM_Wiki/raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - D:/Study_LLM_Wiki/raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - D:/Study_LLM_Wiki/raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: medium
---

AWS 총정리 (2026.05.06(수) ~ 2026.05.08(금))



#### \# 한 줄 요약

AWS에서 VPC/EC2/RDS/Route 53/Load Balancer/HTTPS를 연결해 웹서비스 배포 구조를 만든 과정을 묶은 총정리다.



#### \# 학습 흐름

2026-05-06에는 Cloud 기본 용어, Region/AZ, VPC/Subnet/CIDR, EC2, Security Group을 잡았다. 05-07에는 EC2 2대, Nginx, Spring Boot, RDS MySQL 연결을 실습했다. 05-08에는 Route 53, ACM 인증서, Load Balancer, Target Group, Listener를 통해 도메인과 HTTPS 흐름까지 확장했다.



#### \# 핵심 개념

- VPC/Subnet/CIDR: 클라우드 안의 네트워크 범위와 서버 배치 위치를 정한다.
- Security Group: EC2/RDS 접근 허용 포트와 출발지를 제어한다.
- EC2: 애플리케이션 서버 또는 Nginx 서버를 직접 운영하는 가상 서버다.
- RDS: DB 설치/운영 일부를 AWS가 관리하는 데이터베이스 서비스다.
- Route 53/ACM/Load Balancer: 도메인, 인증서, 트래픽 분산을 연결해 HTTPS 배포를 구성한다.



#### \# 실습 / 예제 흐름

EC2에 SSH로 접속해 Nginx와 JDK/Maven/Spring Boot 실행 환경을 준비하고, RDS MySQL을 생성해 Spring Boot `application.properties`에서 JDBC 연결을 구성한다. 이후 Target Group과 Load Balancer를 통해 여러 EC2 인스턴스로 요청을 분산하고 Route 53 도메인/ACM 인증서를 연결한다. 실습 원본에 포함된 IP·endpoint·비밀번호류는 위키에서는 placeholder로 일반화해야 한다.



#### \# 자주 헷갈릴 점

- EC2는 서버를 직접 관리하고, RDS는 DB 운영 일부를 AWS가 관리한다.
- Security Group은 방화벽처럼 보이지만 리소스 단위 인바운드/아웃바운드 규칙이다.
- Route 53은 DNS이고, Load Balancer는 실제 트래픽 분산 계층이다.
- CLB와 ALB는 모두 로드밸런서지만 Target Group/Listener 중심의 HTTP/HTTPS 구성은 ALB에서 더 명확하다.



#### \# 관련 위키 페이지

- [[entities/aws|AWS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]
- [[entities/amazon-route-53|Amazon Route 53]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]



#### \# 출처

- `D:/Study_LLM_Wiki/raw/Study/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md`
- `D:/Study_LLM_Wiki/raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `D:/Study_LLM_Wiki/raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `D:/Study_LLM_Wiki/raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
