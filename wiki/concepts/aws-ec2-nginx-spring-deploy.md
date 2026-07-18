---
title: AWS EC2에서 Nginx와 Spring Boot 배포
created: 2026-07-03
updated: 2026-07-18
type: concept
tags: [aws, linux, spring-boot, backend]
sources:
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md
status: growing
confidence: high
---

# AWS EC2에서 Nginx와 Spring Boot 배포

## 정의

AWS EC2에서 Nginx와 Spring Boot를 배포한다는 것은 EC2 Linux 서버에 SSH로 접속해 웹서버 또는 Spring Boot 애플리케이션을 설치·빌드·실행하고 Public IP나 Elastic IP로 접근하게 만드는 과정이다. Load Balancer·도메인·HTTPS 연결은 05-12 CI/CD 후속 수업에서 확장했다.

## 수업에서 배운 흐름

1. EC2 Public IP 또는 Elastic IP와 Key Pair를 이용해 MobaXterm으로 SSH 접속했다.
2. 서로 다른 두 public subnet의 EC2에 Nginx를 설치했다.
3. 정적 홈페이지 저장소를 clone하고 `/var/www/html/`에 복사하는 명령을 기록했다. 실제 repository URL은 위키에 옮기지 않는다.
4. JDK 17과 Maven을 설치했다.
5. Spring Boot 예제 프로젝트를 clone하고 `mvn clean package -DskipTests`로 jar를 만드는 절차를 기록했다.
6. Spring Boot가 9000번에서 실행되므로, 실습에서는 80번 요청을 9000번으로 redirect했다.
7. 두 번째 EC2에서는 HTML 문구를 수정하고 다시 빌드해 두 서버의 응답을 구분하도록 했다.
8. 05-08 원본에는 Nginx·Spring Boot 웹 확인 칸이 비어 있어 browser 성공은 확정하지 않는다. 두 EC2를 Target Group과 ALB에 연결하는 절차는 05-12 CI/CD 후속 수업에 귀속하며, target health·browser 결과는 보존되지 않았다.

## 실행 단계와 완료 조건

| 단계 | 실제 기록 | 완료 판단 |
|---|---|---|
| Nginx | package 설치, service start/status, document root 복사·restart 명령 | 출력·browser 결과 미보존 |
| Java/Maven | JDK 17·Maven 설치와 version 확인 명령 | version 출력 미보존 |
| Spring build | project clone, `mvn clean package -DskipTests`, `target` 이동 | build log·artifact 목록 미보존 |
| port | Linux `iptables`로 80→9000 redirect | 규칙 조회·HTTP 결과 미보존 |
| application | `java -jar` 실행 명령과 두 번째 EC2의 template 수정·재빌드 절차 | process log·browser 결과 미보존 |

## Nginx와 Spring Boot의 역할 차이

- Nginx는 정적 파일을 빠르게 제공하거나, 앞단 reverse proxy로 요청을 받아 backend 서버로 넘기는 데 자주 쓰인다.
- Spring Boot는 Java 애플리케이션 로직, Controller, Service, Repository 흐름을 실행한다.
- 05-08 AWS 수업에서는 Nginx 정적 페이지 실습 후 Spring Boot jar 실행으로 넘어갔다. 05-12 CI/CD 후속 수업에서 두 EC2를 Target Group에 등록하고 ALB가 같은 서비스의 대상으로 다뤘다.

## 왜 중요한가

이 과정은 [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]의 클라우드 버전이다. Linux의 package·service·JAR process·`iptables` 책임은 그대로 남고, AWS에서는 EC2·Security Group·Elastic IP가 바깥 접속 경계를 추가한다. Load Balancer·Route 53은 05-12 후속 범위다.

## 자주 헷갈리는 점

- EC2는 서버 상품이고, 그 안의 운영체제는 AMI로 선택한다.
- SSH 접속 실패는 Key Pair, Security Group 22번, Public IP/EIP, 사용자명(`ubuntu`, `ec2-user`) 중 하나가 어긋난 경우가 많다.
- 80번 포트를 9000번으로 redirect하는 것은 실습 편의 방식이다. 실무에서는 ALB/Nginx가 앞단에서 80/443을 받고 backend 포트로 넘기는 구성이 더 자연스럽다.
- EC2가 두 대면 애플리케이션 파일과 설정을 두 서버에 모두 맞게 반영해야 한다. 05-08은 수동 명령 단계이고, 이후 CI/CD가 이 반복을 자동화한다.

## 관련 개념

- [[summaries/2026-05-08-aws-rds-resource-cleanup|2026-05-08 AWS RDS MySQL 연결과 자원 정리]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[summaries/2026-05-12-route53-alb-https-review|2026-05-12 Route 53, ALB, HTTPS]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/maven|Maven]]

## 출처
- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/7. Ci&CD/2026.05.12(화)/2026.05.12(화).md`
