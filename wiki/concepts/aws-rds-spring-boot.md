---
title: AWS RDS와 Spring Boot 연결
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [aws, spring-boot, backend]
sources:
  - raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
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
5. EC2에 `mysql-client`를 설치하고 RDS endpoint로 접속한다.
6. `shopping` DB를 선택하고 `products` 테이블과 샘플 데이터를 만든다.
7. Spring Boot의 `application.properties`에서 `localhost`를 RDS endpoint로 바꾸고 DB 계정 정보를 맞춘다.
8. jar를 다시 빌드·실행하고 상품 목록이 DB에서 조회되는지 확인한다.
9. 두 EC2가 하나의 RDS를 공유한다는 점을 확인한다.

## 핵심 예시

```bash
sudo apt update
sudo apt install mysql-client -y
mysql -h <rds-endpoint> -P 3306 -u <db-user> -p
```

```properties
spring.datasource.url=jdbc:mysql://<rds-endpoint>:3306/shopping?useSSL=false&serverTimezone=Asia/Seoul&allowPublicKeyRetrieval=true
spring.datasource.username=<db-user>
spring.datasource.password=<secret>
```

> 원본에는 실습용 endpoint와 비밀번호 예시가 있지만, 위키에는 보안상 placeholder로 보존한다. 실제 프로젝트에서는 비밀번호를 Git이나 공개 문서에 두지 않고 환경 변수, secret manager, 배포 환경 설정으로 분리한다.

## 왜 중요한가

RDS를 쓰면 개발자가 DB 서버 OS 설치, 패치, 백업, 장애 조치 일부를 직접 관리하지 않아도 된다. 대신 애플리케이션은 네트워크와 권한, 연결 문자열을 정확히 맞춰야 한다. Spring Boot 프로젝트가 단순 메모리/정적 데이터 예제에서 실제 DB 기반 서비스로 넘어가는 지점이다.

## 자주 헷갈리는 점

- RDS endpoint는 DB 서버 주소이고, EC2 Public IP와 다르다.
- RDS와 EC2가 같은 VPC에 있어도 Security Group에서 3306이 막혀 있으면 접속할 수 없다.
- RDS를 public access로 만들 수는 있지만, 실제 운영에서는 public 노출을 최소화하고 EC2/ALB/Security Group 경계를 엄격히 잡아야 한다.
- Multi-AZ는 장애 대비용 대기 DB에 가깝고, Read Replica는 읽기 부하 분산/복제 목적이 강하다.
- `useSSL=false` 같은 URL 파라미터는 실습 편의일 수 있으므로 운영 보안 설정과 구분해야 한다.

## 관련 개념

- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07 AWS EC2, Nginx, Spring Boot, RDS 연결]]
- [[summaries/2026-05-08-aws-route53-load-balancer-https|2026-05-08 AWS Route 53, Load Balancer, HTTPS]]
- [[entities/amazon-rds|Amazon RDS]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[concepts/spring-boot-rest-api|Spring Boot REST API]]
- [[concepts/dto-entity-service-controller|DTO, Entity, Service, Controller]]
- [[entities/mysql|MySQL]]

## 출처

- `raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `raw/Study/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
