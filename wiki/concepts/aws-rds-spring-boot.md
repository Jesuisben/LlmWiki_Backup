---
title: AWS RDS와 Spring Boot 연결
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [aws, spring-boot, backend]
sources:
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
status: growing
confidence: high
---

# AWS RDS와 Spring Boot 연결

## 정의

AWS RDS와 Spring Boot 연결은 Spring Boot 애플리케이션이 EC2 내부 로컬 DB가 아니라 AWS의 관리형 MySQL 데이터베이스 인스턴스에 JDBC URL, 계정, 비밀번호, 포트 3306으로 접속하게 만드는 과정이다.

## 수업에서 배운 흐름

1. Amazon RDS에서 MySQL DB 인스턴스를 만든다.
2. DB 인스턴스 식별자, 마스터 사용자, 비밀번호, 초기 DB 이름을 지정한다.
3. RDS가 EC2와 통신 가능한 VPC/AZ/Security Group 설정을 갖게 한다.
4. AWS의 “EC2 연결 설정” 또는 Security Group 규칙으로 EC2에서 RDS 3306번 포트에 접근하게 한다.
5. EC2에 `mysql-client`를 설치하고 RDS endpoint로 접속하는 명령을 기록한다.
6. 수업용 DB를 선택하고 `products` 테이블과 샘플 데이터를 만드는 SQL을 기록한다.
7. Spring Boot의 `application.properties`에서 `localhost`를 RDS endpoint로 바꾸고 DB 계정 정보를 맞춘다.
8. jar를 다시 빌드·실행하는 명령을 기록한다.
9. 두 EC2가 하나의 RDS를 공유한다는 수업 결론을 정리한다. 다만 MySQL 접속 출력, `SELECT` 결과, Spring Boot 응답은 원본에 보존되지 않았다.

## 연결 경계와 완료 조건

| 경계 | 필요한 값·규칙 | 원본의 완료 증거 |
|---|---|---|
| RDS 생성 | MySQL, 단일 AZ 실습 설정, DB 식별자·관리자 계정·초기 DB, VPC/SG | `사용 가능`이어야 한다는 기준만 있고 실제 상태 출력은 없음 |
| EC2→RDS network | RDS endpoint, 3306, EC2/RDS Security Group 연결 | 자동 생성 SG 확인 지시, 연결 성공 출력은 없음 |
| MySQL client | endpoint·port·username·password | 설치·접속 명령과 SQL만 있고 prompt 이후 결과는 생략 |
| Spring JDBC | datasource URL·username·password를 RDS 기준으로 변경 | 수정·재빌드·jar 명령만 있고 browser/조회 결과는 없음 |

원본에는 실제 endpoint·계정·비밀번호가 있으나 이 페이지에는 옮기지 않는다. 실제 프로젝트에서는 비밀번호를 Git·공개 문서에 두지 않고 환경 변수나 배포 secret으로 분리한다.

## 왜 중요한가

RDS는 EC2에 MySQL을 직접 설치하는 경로와 달리 DB 인스턴스의 생성·상태·endpoint를 AWS 서비스로 다루게 한다. 대신 애플리케이션은 VPC·Security Group·3306·JDBC 연결 정보를 정확히 맞춰야 한다. Spring Boot의 로컬 `localhost` DB 설정을 외부 관리형 DB 주소로 바꾸는 첫 클라우드 연결 사례다.

## 자주 헷갈리는 점

- RDS endpoint는 DB 서버 주소이고, EC2 Public IP와 다르다.
- RDS와 EC2가 같은 VPC에 있어도 Security Group에서 3306이 막혀 있으면 접속할 수 없다.
- RDS를 public access로 만들 수는 있지만, 실제 운영에서는 public 노출을 최소화하고 EC2/ALB/Security Group 경계를 엄격히 잡아야 한다.
- `퍼블릭 액세스: 예`는 수업 설정이다. 이를 운영 DB의 기본 공개 원칙으로 일반화하지 않는다.
- 설정값을 적었다는 사실과 실제 DB/JDBC 왕복이 성공했다는 사실은 다르다. client prompt·query 결과·application response를 각각 확인해야 한다.

## 관련 개념

- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]
- [[entities/amazon-rds|Amazon RDS]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[entities/mysql|MySQL]]

## 출처
- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
