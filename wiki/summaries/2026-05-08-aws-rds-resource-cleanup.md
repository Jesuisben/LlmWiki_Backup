---
title: 2026-05-08 AWS RDS MySQL 연결과 자원 정리
created: 2026-07-03
updated: 2026-07-13
type: summary
tags: [aws, linux, spring-boot, backend, curriculum, study-log]
sources:
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md
status: growing
confidence: high
---

# 2026-05-08 AWS RDS MySQL 연결과 자원 정리

## 한 줄 요약

두 EC2의 통신 문제를 Security Group의 ICMP 규칙으로 해결하고, Nginx 정적 페이지와 Spring Boot jar를 실행한 뒤, 하나의 RDS MySQL을 두 애플리케이션 서버가 공유하도록 연결하고 실습 자원을 정리한 날이다.

## 배운 내용

- Public2A와 Public2C 사이 `ping`은 처음 실패했고, 두 Security Group에 모든 ICMP IPv4 인바운드 규칙을 추가한 뒤 성공했다.
- 두 EC2에 Nginx를 설치하고 Git 저장소의 서로 다른 정적 페이지를 `/var/www/html/`에 배치했다.
- Nginx를 중지한 뒤 JDK 17·Maven을 설치하고 Spring Boot 프로젝트를 `mvn clean package -DskipTests`로 빌드해 jar를 실행했다.
- 실습에서는 `iptables`로 외부 80번 요청을 Spring Boot 9000번 포트로 redirect했다.
- RDS MySQL을 만들고 EC2 연결 설정·Security Group을 맞춘 뒤 `mysql-client`로 접속해 `shopping.products` 테이블과 샘플 데이터를 만들었다.
- `application.properties`의 DB 호스트를 `localhost`에서 RDS endpoint로 바꿔, 두 EC2가 하나의 RDS를 바라보게 했다.
- 도메인 등록은 다음 단계 준비로만 언급됐고, Route 53/ACM/ALB 실습은 이 날짜 원본에 없다. 해당 실제 실습은 [[summaries/2026-05-12-route53-alb-https-review|2026-05-12 CI/CD Route 53, ALB, HTTPS]]에서 다룬다.

## 핵심 실습 / 예제

```text
Public2A ── ICMP 허용 ── Public2C
   │                       │
   ├─ Nginx / Spring Boot  ┤
   │         ↓ JDBC 3306   │
   └────── RDS MySQL ──────┘
```

```shell
sudo apt install -y nginx
sudo systemctl start nginx

sudo apt install -y openjdk-17-jdk
sudo apt install -y maven
mvn clean package -DskipTests
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 9000
java -jar <생성된_jar>.jar
```

```properties
spring.datasource.url=jdbc:mysql://<RDS_ENDPOINT>:3306/<DATABASE_NAME>
spring.datasource.username=<DB_USERNAME>
spring.datasource.password=<DB_PASSWORD>
```

## 헷갈린 점 / 질문

- `ping`은 HTTP/SSH와 다른 ICMP 트래픽이므로 22·80·443을 열어도 실패할 수 있다.
- Nginx 정적 페이지 실습과 Spring Boot jar 실행은 순차적으로 수행한 서로 다른 서버 역할 확인이다.
- RDS endpoint는 EC2의 Public IP가 아니며, 같은 VPC여도 DB Security Group의 3306 규칙이 필요하다.
- `application.properties`에 실제 DB 비밀번호를 남기지 않는다. 원본의 접속값은 위키에서 재노출하지 않는다.
- 삭제는 EIP·EC2·RDS처럼 먼저 참조되는 자원을 정리한 뒤 Security Group·VPC로 진행해야 한다.

## 관련 페이지

- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[concepts/aws-resource-lifecycle-cost-management|AWS 자원 생명주기와 비용 관리]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/AWS 총정리/AWS 총정리.md`
