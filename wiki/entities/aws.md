---
title: AWS
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [aws]
sources:
  - raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
  - raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
status: growing
confidence: high
---

# AWS

## 무엇인가

AWS(Amazon Web Services)는 서버, 네트워크, 데이터베이스, 스토리지, DNS, 인증서 같은 IT 자원을 Cloud Service로 제공하는 플랫폼이다. 수업에서는 “필요한 만큼 빌려 쓰고 사용량에 따라 비용을 지불하는 On-Demand 인프라”로 On-Premise와 대비해 이해했다.

## 이 위키에서의 맥락

이 위키에서 AWS는 [[entities/linux|Linux]]와 [[entities/docker|Docker]] 다음 단계로 등장한다. 이전에는 VM이나 컨테이너 안에서 웹서비스를 실행했다면, AWS 과정에서는 VPC/Subnet에 EC2를 배치하고, RDS를 연결하고, Route 53과 Load Balancer로 도메인 기반 배포를 구성한다.

## 학습 이력

- [[summaries/2026-05-06-aws-cloud-vpc-ec2|2026-05-06]]: AWS 메뉴, On-Demand/On-Premise, Region/AZ/VPC/Subnet/CIDR, Security Group, EC2 입문.
- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07]]: VPC와 EC2 2대 생성, SSH, ping/ICMP, Nginx, Spring Boot, RDS MySQL 연결.
- [[summaries/2026-05-08-aws-route53-load-balancer-https|2026-05-08]]: Route 53, DNS, ACM, CLB/ALB, HTTPS, Target Group, Load Balancer 배포 주소 구성.
- [[summaries/2026-05-08-aws-subject-review|AWS 총정리]]: VPC/EC2/RDS/Route 53/ACM/Load Balancer/HTTPS를 클라우드 배포 구조로 다시 묶는 복습 허브.
- [[summaries/2026-05-12-route53-alb-https-review|2026-05-12]]: CI/CD 배포가 사용자에게 도달하기 위한 Route 53, ACM, ALB, HTTPS 앞단을 복습.
- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13]]: Terraform으로 인프라를 코드화하고, S3 bucket으로 Spring Boot 이미지 업로드 파일을 분리.
- [[summaries/2026-05-middle-project-cicd-passwordless-guide|중간 프로젝트 CI/CD·배포·Passwordless 가이드]] 및 Passwordless 적용에서는 인증 서버, 서비스 도메인, 보안 그룹/포트, HTTPS 같은 배포 인프라가 X1280 연동의 운영 배경이 된다.

## 핵심 기능 / 특징

- Compute: [[entities/amazon-ec2|Amazon EC2]]로 가상 서버를 생성한다.
- Network: VPC, Subnet, Route Table, Internet Gateway, Security Group으로 네트워크와 접근 경로를 만든다.
- Database: [[entities/amazon-rds|Amazon RDS]]로 관리형 관계형 DB를 사용한다.
- Storage: [[entities/amazon-s3|Amazon S3]]로 이미지와 첨부 파일 같은 객체 파일을 저장한다.
- DNS/배포: [[entities/amazon-route-53|Amazon Route 53]], ACM, Load Balancer로 도메인과 HTTPS를 연결한다.
- 운영 관점: Elastic IP, Security Group, Health Check, 리소스 삭제 순서처럼 비용·접속·보안 관리를 함께 고려한다.

## 프로젝트/면접 관점

AWS는 “코드를 클라우드에서 실제 서비스처럼 운영하기 위한 인프라”라고 설명할 수 있다. Spring Boot 프로젝트를 EC2에 배포하고, DB는 RDS로 분리하며, 외부 사용자는 Route 53 도메인과 HTTPS Load Balancer를 통해 접속하게 만드는 흐름이 핵심이다. 이후 CI/CD를 붙이면 EC2 두 대에 수동으로 접속해 빌드/배포하던 반복 작업을 자동화하는 방향으로 이어진다.

## 관련 개념

- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[concepts/aws-s3-file-upload|AWS S3 파일 업로드 흐름]]
- [[concepts/terraform-infrastructure-as-code|Terraform과 Infrastructure as Code]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]
- [[entities/passwordless-x1280|Passwordless X1280]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md`
- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/교육 자료/AWS 기초 용어.pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/실습 관리 대장(텍스트).md`
- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
- `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
- `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
