---
title: AWS
created: 2026-07-03
updated: 2026-07-18
type: entity
tags: [aws]
sources:
  - raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
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

이 위키에서 AWS는 [[entities/linux|Linux]]와 [[entities/docker|Docker]] 다음 단계로 등장한다. 이전에는 VM이나 컨테이너 안에서 웹서비스를 실행했다면, AWS 05-06~08 과정에서는 VPC/Subnet에 EC2를 배치하고 RDS 연결 절차까지 수행했다. Route 53·ACM·Target Group·ALB·HTTPS는 05-12 CI/CD 후속 과정이다.

## 학습 이력

- [[summaries/2026-05-06-aws-cloud-vpc-ec2|2026-05-06]]: AWS 메뉴, On-Demand/On-Premise, Region/AZ/VPC/Subnet/CIDR, Security Group, EC2 입문.
- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07]]: VPC·Subnet·IGW·Route Table·Security Group·EC2·EIP·SSH와 자원 해제 실습.
- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08]]: ping/ICMP는 출력으로 성공을 확인했고, Nginx·Spring Boot jar·RDS MySQL/JDBC·자원 정리는 명령·절차와 완료 조건을 학습.
- [[summaries/2026-05-08-aws-subject-review|AWS 총정리]]: 비용·네트워크·서버·DB·자원 생명주기를 묶는 복습 허브.
- [[summaries/2026-05-12-route53-alb-https-review|2026-05-12]]: CI/CD 배포가 사용자에게 도달하기 위한 Route 53, ACM, Target Group, ALB, HTTPS 구성 절차를 복습. 실제 target health·browser 응답은 미보존.
- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13]]: Terraform의 VPC·Subnet·EC2 code 적용을 시도했으나 최종 apply 성공은 미보존. S3 upload 재시도 성공·bucket object 확인은 수업 메모의 관찰 서술이며 listing·응답·화면과 RDS query 결과는 없다.


## 핵심 기능 / 특징

- Compute: [[entities/amazon-ec2|Amazon EC2]]로 가상 서버를 생성한다.
- Network: VPC, Subnet, Route Table, Internet Gateway, Security Group으로 네트워크와 접근 경로를 만든다.
- Database: [[entities/amazon-rds|Amazon RDS]]로 관리형 관계형 DB를 사용한다.
- Storage: [[entities/amazon-s3|Amazon S3]]로 이미지와 첨부 파일 같은 객체 파일을 저장한다.
- DNS/배포: [[entities/amazon-route-53|Amazon Route 53]], ACM, Load Balancer로 도메인과 HTTPS를 연결한다.
- 운영 관점: Elastic IP, Security Group, RDS 삭제 확인, 의존성 기반 리소스 정리처럼 비용·접속·보안 관리를 함께 고려한다.

## 프로젝트/면접 관점

AWS는 “코드를 실행할 서버, 네트워크, DB를 클라우드 자원으로 구성하는 플랫폼”이라고 설명할 수 있다. 3일 직접 수업의 핵심은 VPC·EC2·RDS와 수동 접속/배포 절차이고, 도메인·HTTPS·ALB와 자동 배포는 CI/CD 후속에서 붙는다. 이렇게 날짜와 책임을 나누면 AWS 서비스의 기능과 수업에서 실제 확인한 결과를 과장하지 않고 설명할 수 있다.

## 관련 개념

- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[concepts/aws-s3-file-upload|AWS S3 파일 업로드 흐름]]
- [[concepts/terraform-infrastructure-as-code|Terraform과 Infrastructure as Code]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[comparisons/clb-vs-alb|CLB vs ALB]]


## 출처

- `raw/KoreaICT/6. AWS/2026.05.06(수) - 시작/2026.05.06(수) - 시작.md`
- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
- `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
- `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
