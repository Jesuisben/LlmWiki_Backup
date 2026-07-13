---
title: Amazon RDS
created: 2026-07-03
updated: 2026-07-13
type: entity
tags: [aws, backend]
sources:

  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
  - raw/KoreaICT/7. Ci&CD/Ci&CD 총정리/Ci&CD 총정리.md
status: growing
confidence: high
---

# Amazon RDS

## 무엇인가

Amazon RDS(Relational Database Service)는 MySQL, PostgreSQL, MariaDB, Oracle Database, SQL Server 등 관계형 데이터베이스를 관리형 서비스로 제공하는 AWS 서비스다.

## 이 위키에서의 맥락

Oracle/MySQL과 Spring Boot를 배운 뒤, AWS 수업에서는 DB 서버를 직접 설치하는 대신 RDS MySQL을 만들고 Spring Boot가 JDBC로 접속하는 흐름을 다뤘다. 이는 “애플리케이션 서버 EC2”와 “데이터베이스 RDS”를 분리하는 첫 클라우드 배포 구조다.

## 핵심 기능 / 특징

- DB Engine 선택: MySQL, PostgreSQL, MariaDB, Oracle DB 등.
- Instance Class 선택: `db.t3.micro` 같은 CPU/메모리 규모.
- Storage 선택: gp2/gp3, 할당 용량, IOPS 개념.
- Endpoint: 애플리케이션과 DB client가 접속하는 DB 주소.
- VPC/Security Group 연결: EC2에서 3306 포트로 접근 가능해야 함.
- Multi-AZ / Read Replica: 장애 대비와 읽기 확장 개념.

## 학습 이력

- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08]]: RDS MySQL 생성, EC2에서 mysql-client 접속, `shopping.products` 구성, Spring Boot JDBC URL 연결과 두 EC2의 공유 DB 확인.
- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13]]: S3에 파일을 저장하고 RDS MySQL `coffee.product`에는 상품 정보와 `image_url`을 저장하는 역할 분리를 확인.

## 보안 메모

수업 원본에는 실습 편의를 위해 RDS endpoint, 계정, 비밀번호 예시가 직접 등장한다. 위키에서는 구조와 설정 위치만 보존하고 실제 비밀번호는 마스킹한다. 실제 프로젝트에서는 DB 비밀번호를 Git, Notion, 공개 wiki, 프론트엔드 코드에 두지 않는다.

## 관련 개념

- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[entities/mysql|MySQL]]
- [[entities/oracle-database|Oracle Database]]
- [[concepts/spring-data-jpa-repository|Spring Data JPA Repository]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
