---
title: EC2 vs RDS
created: 2026-07-03
updated: 2026-07-13
type: comparison
tags: [aws, backend]
sources:

  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
status: growing
confidence: high
---

# EC2 vs RDS

## 비교 목적

AWS 수업에서 EC2와 RDS는 모두 “클라우드에 있는 서버처럼 보이는 것”으로 등장하지만, 개발자가 관리해야 하는 범위와 사용 목적이 다르다. 이 차이를 이해해야 Spring Boot 애플리케이션 서버와 데이터베이스 서버를 분리해 설계할 수 있다.

## 한눈에 보기

| 항목 | EC2 | RDS |
|---|---|---|
| 기본 역할 | 가상 서버 | 관리형 관계형 데이터베이스 |
| 주 사용처 | Nginx, Spring Boot, 배치, 일반 Linux 작업 | MySQL/PostgreSQL/Oracle 등 DB |
| 개발자 관리 범위 | OS, 패키지, 런타임, 애플리케이션, 보안 설정 | DB 엔진 설정, 스키마, 계정, 접근 제어 중심 |
| 접속 방식 | SSH, HTTP/HTTPS | DB client/JDBC, 3306 등 DB 포트 |
| 수업 예시 | `EDU-PUBLIC-EC2-2A`, `EDU-PUBLIC-EC2-2C` | RDS MySQL, `shopping` DB |
| 장애/확장 | Auto Scaling, 이미지/인스턴스 관리 | Multi-AZ, Read Replica |
| 삭제/비용 주의 | 인스턴스 종료, EIP 릴리스 | DB 삭제, 스냅샷/백업 옵션 확인 |

## 언제 무엇을 쓰는가

- Spring Boot jar, Nginx, 정적 HTML, 배포 스크립트를 실행하려면 EC2를 쓴다.
- 애플리케이션 데이터 저장소가 필요하고 DB 운영 부담을 줄이고 싶으면 RDS를 쓴다.
- 수업의 쇼핑 예제에서는 EC2가 `/products` 요청을 처리하고, RDS가 `products` 테이블 데이터를 보관했다.
- EC2 두 대가 하나의 RDS를 공유하면, 로드밸런싱된 여러 애플리케이션 서버가 같은 데이터 계층을 바라보는 구조가 된다.

## 헷갈리기 쉬운 포인트

- EC2 안에 MySQL을 직접 설치할 수도 있지만, 그러면 DB 백업/패치/장애 관리를 직접 해야 한다.
- RDS는 SSH로 들어가서 OS를 마음대로 고치는 서버가 아니라 관리형 DB 서비스다.
- EC2와 RDS가 같은 AWS 안에 있어도 Security Group과 포트가 맞지 않으면 연결되지 않는다.
- RDS endpoint는 EC2 Public IP가 아니라 DB 접속용 주소다.
- 실습에서는 public access를 켤 수 있지만, 운영에서는 DB를 외부에 직접 노출하지 않는 쪽이 기본이다.

## 관련 페이지

- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]

## 출처


- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
