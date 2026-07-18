---
title: EC2 vs RDS
created: 2026-07-03
updated: 2026-07-18
type: comparison
tags: [aws, backend]
sources:
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
status: stable
confidence: high
---

# EC2 vs RDS

## 비교 목적

AWS 수업에서 EC2와 RDS는 모두 network 안에 놓인 원격 자원이지만 책임이 다르다. EC2는 Linux·Nginx·Spring Boot를 직접 운영하는 compute이고, RDS는 endpoint와 DB port로 접속하는 관리형 관계형 데이터베이스다. 이 차이를 알아야 애플리케이션 실행과 데이터 저장을 분리하고, 연결 실패를 어느 계층에서 점검할지 정할 수 있다.

## 한눈에 보기

| 항목 | EC2 | RDS |
|---|---|---|
| 기본 역할 | Linux 기반 가상 서버에서 process를 실행 | 관계형 DB engine을 관리형 서비스로 제공 |
| 수업의 실제 작업 | Ubuntu instance 생성, EIP·SSH, Nginx, JDK/Maven, Spring Boot | MySQL DB instance 설정, endpoint 확인, EC2 연결 설정, client/JDBC 절차 |
| 개발자가 직접 관리 | OS, package, file, process/service, application runtime | schema·table·data, DB account, datasource와 접근 정책 |
| AWS가 제공하는 관리 경계 | instance·AMI·VPC 연결·상태와 가상 hardware | DB instance·engine 운영 기반·endpoint·상태 관리 |
| network 진입점 | SSH 22, HTTP 80, Spring Boot 9000 등 목적별 port와 EC2 Security Group | DB endpoint, MySQL 3306과 EC2/RDS Security Group 관계 |
| 애플리케이션 연결 | Spring Boot JAR가 실행되는 쪽 | Spring datasource가 `localhost` 대신 endpoint를 바라보는 쪽 |
| 비용·삭제 | EIP 연결 해제/release, instance 종료, SG·network 의존성 확인 | DB 삭제 조건과 snapshot/backup 선택을 확인한 뒤 SG·VPC 정리 |
| 05-08 결과 보존 범위 | 설치·build·JAR 실행 명령은 있으나 build log·browser 응답은 미보존 | client 명령·DDL/DML·datasource 수정은 있으나 DB prompt·query output·Spring 응답은 미보존 |

## 수업에서 실제로 연결한 흐름

1. 05-07에 VPC·Subnet·Route Table·Security Group을 구성하고 Ubuntu EC2 두 대에 EIP와 SSH 접속을 연결했다.
2. 05-08에는 EC2에서 Nginx와 Spring Boot를 실행하기 위한 package·build·port redirect·JAR 명령을 기록했다.
3. RDS MySQL을 만들고 EC2 연결 설정과 Security Group 관계를 준비했다.
4. EC2의 MySQL client가 RDS endpoint·3306으로 접속하는 명령과 table 생성·sample DML을 기록했다.
5. Spring Boot datasource의 host·username·password를 RDS 기준으로 바꾸고 재build·실행하는 명령을 기록했다.

이 흐름에서 EC2는 요청을 처리할 application process의 실행 위치이고, RDS는 두 application server가 공유하도록 설계한 data 계층이다. 다만 원본에 보존된 것은 설정·명령과 “공유한다”는 수업 설명까지이며, 실제 query output이나 application response로 공유 결과를 검증한 기록은 없다.

## 언제 무엇을 선택하는가

- OS package·web server·Spring Boot JAR처럼 원하는 process를 직접 설치하고 실행해야 하면 EC2 역할이다.
- 관계형 table과 transaction data를 별도 DB service에 저장하고 endpoint/JDBC로 연결하려면 RDS 역할이다.
- EC2에 MySQL을 직접 설치할 수도 있지만, 그 경우 OS부터 DB engine의 patch·backup·process 운영까지 사용자가 맡는다.
- EC2와 RDS를 함께 쓸 때는 “같은 AWS 안”이라는 사실보다 VPC 경로, Security Group source/destination, 3306, endpoint, datasource 설정을 각각 확인해야 한다.

## 비용과 삭제 조건

- EC2 쪽은 사용하지 않는 EIP의 연결 해제·release, instance 종료, 연결된 Security Group과 VPC 의존성을 확인한다.
- RDS 쪽은 DB 삭제 화면의 snapshot/backup 관련 선택과 삭제 조건을 확인하고, DB가 참조하는 Security Group을 먼저 지우지 않는다.
- 05-07~08 원본에는 정리 순서가 있지만 최종 resource 목록이나 삭제 완료 상태는 보존되지 않았다. 따라서 “삭제했다”가 아니라 “삭제 절차와 완료 조건을 기록했다”고 표현한다.

## 일반 AWS 기능과 수업 직접 범위

RDS가 여러 DB engine을 지원하고 Multi-AZ·Read Replica 같은 기능을 제공한다는 설명은 일반적인 AWS 기능이다. 그러나 05-08 직접 실습은 **MySQL 단일 AZ 설정**이었고, Multi-AZ 전환·Read Replica 생성·장애 조치 결과는 없다. 이 페이지는 실제 선택 판단에 필요하지 않은 일반 확장을 비교표의 수업 결과처럼 섞지 않는다.

## 헷갈리기 쉬운 포인트

- EC2 안에 MySQL을 직접 설치할 수도 있지만, 그러면 DB 백업/패치/장애 관리를 직접 해야 한다.
- RDS는 SSH로 들어가서 OS를 마음대로 고치는 서버가 아니라 관리형 DB 서비스다.
- EC2와 RDS가 같은 AWS 안에 있어도 Security Group과 3306 규칙이 맞지 않으면 연결되지 않는다.
- RDS endpoint는 EC2 Public IP가 아니라 DB 접속용 주소다.
- 실습에서는 public access를 켤 수 있지만, 운영에서는 DB를 외부에 직접 노출하지 않는 쪽이 기본이다.
- MySQL client prompt, `SELECT` 결과, Spring Boot 응답은 서로 다른 완료 증거다. 명령을 기록한 사실만으로 세 결과를 성공 처리하지 않는다.

## 관련 페이지

- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md` — EC2·EIP·SSH와 비용·정리 절차
- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md` — EC2 server, RDS MySQL, 3306, client/SQL, datasource와 결과 미보존 경계
- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md` — EC2 application 계층과 RDS data 계층의 과목 복습 연결
