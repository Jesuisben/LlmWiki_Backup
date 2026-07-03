---
title: 2026-05-07 AWS EC2, Nginx, Spring Boot, RDS 연결
created: 2026-07-03
updated: 2026-07-03
type: summary
tags: [aws, linux, spring-boot, backend, curriculum, study-log]
sources:
  - raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf
  - raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
  - raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md
status: growing
confidence: high
---

# 2026-05-07 AWS EC2, Nginx, Spring Boot, RDS 연결

## 한 줄 요약

VPC와 두 public subnet을 실제로 만들고, EC2 두 대에 SSH로 접속해 Nginx와 Spring Boot를 실행한 뒤, RDS MySQL과 Spring Boot를 연결하는 배포 흐름을 실습한 날이다.

## 배운 내용

- `EDU-VPC 10.250.0.0/16`을 만들고, Internet Gateway, Route Table, Public Subnet, Security Group을 순서대로 구성했다.
- `EDU-PUBLIC-SBN-2A`, `EDU-PUBLIC-SBN-2C` 두 subnet을 만들고 각각 EC2를 배치했다.
- Security Group에는 HTTP 80, HTTPS 443, SSH 22, Spring Boot용 사용자 지정 TCP 9000 포트를 열었다.
- Key Pair로 `.pem` 파일을 내려받아 MobaXterm SSH 접속에 사용했다.
- EC2 Public IP가 바뀔 수 있으므로 Elastic IP를 할당하고 EC2에 연결했다.
- EC2 간 `ping`이 처음에는 실패했고, Security Group에 ICMP 규칙을 추가한 뒤 성공했다.
- 두 EC2에 Nginx를 설치하고, GitHub에서 받은 정적 홈페이지를 `/var/www/html/`에 복사했다.
- JDK 17과 Maven을 설치한 뒤 Spring Boot 예제를 clone, package, jar 실행했다.
- Spring Boot가 9000번에서 실행되므로 실습에서는 `iptables`로 80번 요청을 9000번으로 redirect했다.
- RDS MySQL을 만들고 EC2에서 `mysql-client`로 접속해 `shopping` DB와 `products` 테이블을 준비했다.
- Spring Boot의 `application.properties`를 RDS endpoint, DB 계정, DB 이름 기준으로 수정해 EC2 애플리케이션이 RDS를 바라보게 했다.

## 핵심 실습 / 예제

VPC/EC2 구성 순서는 다음처럼 정리된다.

```text
VPC 생성
→ Internet Gateway 생성/연결
→ VPC DNS hostnames 활성화
→ Subnet 생성
→ Route Table 생성 및 0.0.0.0/0 → IGW 라우팅 추가
→ Route Table과 Subnet 연결
→ Security Group 생성 및 Inbound 규칙 추가
→ Key Pair 생성
→ EC2 인스턴스 생성
→ Elastic IP 연결
→ MobaXterm SSH 접속
```

EC2 내부 서버 구성은 다음 흐름으로 이어졌다.

```bash
sudo apt install -y nginx
sudo systemctl start nginx
sudo systemctl status nginx

git clone https://github.com/seoljinuk/ec2_homepage.git
cd ec2_homepage/Public-2A/
sudo cp -r ./* /var/www/html/
sudo systemctl restart nginx

sudo apt update
sudo apt install -y openjdk-17-jdk
sudo apt install -y maven

git clone https://github.com/seoljinuk/shopping_01_no_database.git
cd shopping_01_no_database/
mvn clean package -DskipTests
cd target/
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 9000
java -jar shopping-0.0.1-SNAPSHOT.jar
```

RDS 연결 흐름은 다음처럼 정리할 수 있다.

```text
브라우저
  ↓ HTTP 80 또는 9000
EC2(Spring Boot)
  ↓ JDBC 3306
RDS MySQL / shopping DB / products table
```

> 원본 날짜 MD에는 실습용 공개 IP, RDS endpoint, DB 계정/비밀번호 예시가 들어 있다. 위키에는 구조 이해에 필요한 흐름만 남기고, 실제 비밀번호·접속 정보는 그대로 재노출하지 않는다.

## 왜 중요한가

이 날은 [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]을 AWS로 옮긴 핵심 실습이다. 단순히 jar를 실행하는 데서 끝나지 않고, VPC/Subnet/Route Table/Security Group/EIP/RDS까지 맞아야 외부 사용자가 접속하고 애플리케이션이 DB를 조회할 수 있다.

## 헷갈린 점 / 질문

- EC2끼리 같은 VPC에 있어도 ICMP가 보안그룹에서 막히면 `ping`이 실패한다.
- Nginx와 Spring Boot는 둘 다 웹 요청에 응답할 수 있지만 역할이 다르다. Nginx는 정적 파일 제공/프록시 앞단에 자주 쓰이고, Spring Boot는 Java 애플리케이션 로직을 실행한다.
- `iptables` redirect는 실습 편의 방식이다. 운영 구조에서는 Load Balancer나 Nginx reverse proxy로 80/443을 받아 backend 포트로 넘기는 구성이 더 자연스럽다.
- RDS가 만들어져도 EC2와 연결하려면 VPC, Security Group, 3306 포트, DB 계정, JDBC URL이 모두 맞아야 한다.
- RDS를 public으로 열어 실습할 수는 있지만, 실제 운영에서는 public 접근과 비밀번호 노출을 매우 조심해야 한다.
- AWS 리소스는 비용이 발생할 수 있으므로 EIP 연결 해제/릴리스, EC2 종료, RDS 삭제, 보안그룹/VPC 삭제 순서를 알아야 한다.

## 관련 페이지

- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-ec2-nginx-spring-deploy|AWS EC2에서 Nginx와 Spring Boot 배포]]
- [[concepts/aws-rds-spring-boot|AWS RDS와 Spring Boot 연결]]
- [[comparisons/ec2-vs-rds|EC2 vs RDS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[entities/amazon-rds|Amazon RDS]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 출처

- `raw/Study/6. AWS/2026.05.07(목)/2026.05.07(목).md` — VPC/EC2 생성, ping/ICMP, Nginx, Spring Boot, RDS 실습 메모
- `raw/Study/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf` — EC2 SSH, Nginx, JDK/Maven, Spring Boot, RDS MySQL, JDBC URL 실습
- `raw/Study/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf` — Security Group, RDS, Load Balancer 관련 이론
- `raw/Study/6. AWS/교육 자료/cloud.01.AWS 교안(이론_미니파일).pdf` — VPC/RDS/EC2 구성 요약
- `raw/Study/6. AWS/교육 자료/실습 관리 대장(텍스트).md` — EC2, RDS, Security Group, Load Balancer 리소스 이름
