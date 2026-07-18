---
title: Amazon RDS
created: 2026-07-03
updated: 2026-07-18
type: entity
tags: [aws, backend]
sources:
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md
status: growing
confidence: high
---

# Amazon RDS

## 무엇인가

Amazon RDS(Relational Database Service)는 관계형 데이터베이스를 관리형 자원으로 제공하는 AWS 서비스다. 수업에서는 MySQL engine의 단일 AZ 실습 DB를 만들고 endpoint·Security Group·3306·JDBC 설정을 다뤘다.

## 이 위키에서의 맥락

Oracle/MySQL과 Spring Boot를 배운 뒤, AWS 수업에서는 DB 서버를 직접 설치하는 대신 RDS MySQL을 만들고 Spring Boot가 JDBC로 접속하는 흐름을 다뤘다. 이는 “애플리케이션 서버 EC2”와 “데이터베이스 RDS”를 분리하는 첫 클라우드 배포 구조다.

## 핵심 기능 / 특징

- DB Engine 선택: 직접 수업에서는 MySQL을 선택했다.
- 생성 상태: 상태가 `사용 가능`이 되어야 다음 연결 단계로 넘어간다.
- Endpoint: 애플리케이션과 DB client가 접속하는 DB 주소.
- VPC/Security Group 연결: EC2에서 3306 포트로 접근 가능해야 함.
- 삭제: 데이터 보존·최종 snapshot 관련 확인 항목을 검토해야 한다.

## 학습 이력

- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08]]: RDS MySQL 생성 설정, EC2 연결, MySQL client·DDL/DML·JDBC 수정 절차. 실제 상태·query·application 출력은 미보존.
- [[summaries/2026-05-13-terraform-s3-file-upload|2026-05-13]]: S3 object와 RDS 상품 행의 역할을 분리했다. S3 upload 성공·bucket object 확인은 수업 메모의 관찰 서술이고, S3 1차 결과와 Workbench query 결과가 없어 RDS 행 저장 성공은 미확정이다.

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
- `raw/KoreaICT/7. Ci&CD/2026.05.13(수)/2026.05.13(수).md`
