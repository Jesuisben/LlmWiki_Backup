---
title: AWS 총정리
type: summary
created: 2026-07-03
updated: 2026-07-13
tags: [aws, backend, ci-cd, curriculum, study-log]
sources:
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
status: growing
confidence: high
---

# AWS 총정리

## 한 줄 요약

`AWS 총정리`는 2026-05-06부터 2026-05-08까지 배운 클라우드 배포 흐름을 “비용 관점 → VPC/EC2 네트워크 → Nginx/Spring Boot/RDS → 의존성 기반 자원 정리” 순서로 묶는 복습 허브다.

## 이 자료의 위치

- 앞 자료: [[summaries/2026-05-06-aws-cloud-vpc-ec2|2026-05-06 AWS Cloud, VPC, EC2 입문]]부터 [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]까지의 날짜별 AWS 수업 노트
- 이전 흐름: [[entities/linux|Linux]]와 [[entities/docker|Docker]]에서 웹서비스를 서버/컨테이너 환경에 올리는 법을 배움
- 다음 흐름: GitHub Actions와 서버 배포 스크립트를 연결하는 [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]으로 확장
- 역할: 날짜별 AWS 실습 요약을 대체하지 않고, 클라우드 구성요소의 관계를 한 번에 복습하기 위한 허브

## 배운 내용

### 1. Cloud 기본 관점과 VPC 네트워크

AWS는 서버를 직접 구매·운영하는 On-Premise와 달리 필요한 인프라를 빌려 쓰는 Cloud Service로 이해했다. Region, Availability Zone, VPC, Subnet, CIDR, Internet Gateway, Route Table, Security Group은 EC2가 외부와 통신할 수 있는 네트워크 틀을 만든다. 이 내용은 [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]의 중심이다.

### 2. EC2와 서버 운영

[[entities/amazon-ec2|Amazon EC2]]는 애플리케이션 서버나 Nginx 서버를 직접 운영하는 가상 서버다. SSH 접속, Security Group 포트 허용, ping/ICMP, Nginx 설치, Spring Boot `.jar` 실행 흐름은 Linux에서 배운 서버 운영 지식을 AWS 가상 서버 위로 옮기는 과정이다.

### 3. RDS와 Spring Boot DB 연결

[[entities/amazon-rds|Amazon RDS]]는 MySQL 같은 DB를 AWS 관리형 서비스로 제공한다. 수업에서는 RDS endpoint, username/password, DB 이름을 Spring Boot JDBC 설정과 연결했다. 다만 원본에 실습용 IP·endpoint·비밀번호가 있더라도 wiki에서는 보안상 placeholder로 일반화해야 한다. 관련 페이지는 [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]이다.

### 4. 자원 정리와 비용 관리

AWS는 자원을 만든 뒤 남겨두는 것도 비용과 연결된다. Elastic IP는 연결 해제 후 release하고, EC2·RDS 같은 실행 자원을 먼저 정리한 뒤 참조가 풀린 Security Group·IGW·Subnet·Route Table·VPC를 확인한다. 이 흐름은 [[concepts/aws-resource-lifecycle-cost-management|AWS 자원 생명주기와 비용 관리]]에 정리한다.

### 5. 이후 CI/CD·도메인 배포로 이어지는 이유

AWS 수업 단계에서는 EC2 접속, 빌드, 서버 실행, Nginx/Load Balancer 설정을 사람이 직접 수행한다. 이후 CI/CD에서는 GitHub에 push하면 GitHub Actions가 빌드와 배포 절차를 반복 가능하게 실행하는 방향으로 발전한다. 그래서 AWS 총정리는 CI/CD 이전의 “수동 클라우드 배포 구조”를 복습하는 위치에 있다.

## 헷갈린 점 / 질문

- EC2는 애플리케이션 서버를 직접 관리하는 가상 머신이고, RDS는 DB 운영 일부를 AWS가 대신 관리하는 서비스다. 비교는 [[comparisons/ec2-vs-rds|EC2 vs RDS]] 참고.
- Security Group은 “서버 안의 설정 파일”이 아니라 AWS 리소스 단위의 네트워크 접근 규칙이다.
- Route 53·ACM·ALB의 실제 구성은 AWS 3일 수업이 아니라 이후 [[summaries/2026-05-12-route53-alb-https-review|CI/CD 2026-05-12]]에서 복습·실습했다.

## 관련 페이지

- [[entities/aws|AWS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]

- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/aws-resource-lifecycle-cost-management|AWS 자원 생명주기와 비용 관리]]
- [[concepts/middle-project-cicd-deploy-flow|중간 프로젝트 CI/CD 배포 흐름]]

## 출처

- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
