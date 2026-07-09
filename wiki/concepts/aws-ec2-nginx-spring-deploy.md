---
title: AWS EC2에서 Nginx와 Spring Boot 배포
created: 2026-07-03
updated: 2026-07-03
type: concept
tags: [aws, linux, spring-boot, backend]
sources:
  - raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md
  - raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md
  - raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf
  - raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf
status: growing
confidence: high
---

# AWS EC2에서 Nginx와 Spring Boot 배포

## 정의

AWS EC2에서 Nginx와 Spring Boot를 배포한다는 것은 EC2 Linux 서버에 SSH로 접속해 웹서버 또는 Spring Boot 애플리케이션을 설치·빌드·실행하고, Public IP, Elastic IP, Load Balancer, 도메인을 통해 외부에서 접근하게 만드는 과정이다.

## 수업에서 배운 흐름

1. EC2 Public IP 또는 Elastic IP와 Key Pair를 이용해 MobaXterm으로 SSH 접속했다.
2. `Public-2A`, `Public-2C` 두 EC2에 Nginx를 설치했다.
3. GitHub에서 정적 홈페이지를 clone하고 `/var/www/html/`에 복사했다.
4. JDK 17과 Maven을 설치했다.
5. Spring Boot 예제 프로젝트를 clone하고 `mvn clean package -DskipTests`로 jar를 만들었다.
6. Spring Boot가 9000번에서 실행되므로, 실습에서는 80번 요청을 9000번으로 redirect했다.
7. 2C 서버에서는 HTML 문구를 수정해 2A/2C 응답을 구분했다.
8. 브라우저에서 각 EC2 주소와 Load Balancer 주소로 응답을 확인했다.

## 핵심 명령어

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

## Nginx와 Spring Boot의 역할 차이

- Nginx는 정적 파일을 빠르게 제공하거나, 앞단 reverse proxy로 요청을 받아 backend 서버로 넘기는 데 자주 쓰인다.
- Spring Boot는 Java 애플리케이션 로직, Controller, Service, Repository 흐름을 실행한다.
- 수업에서는 Nginx 정적 페이지 실습 후 Spring Boot jar 실행으로 넘어갔고, Load Balancer 단계에서 두 EC2를 같은 서비스의 대상처럼 묶었다.

## 왜 중요한가

이 과정은 [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]의 클라우드 버전이다. 로컬 VM에서는 서버 IP와 방화벽 정도를 보면 됐지만, AWS에서는 EC2, Security Group, Elastic IP, Load Balancer, Route 53까지 함께 연결된다.

## 자주 헷갈리는 점

- EC2는 서버 상품이고, 그 안의 운영체제는 AMI로 선택한다.
- SSH 접속 실패는 Key Pair, Security Group 22번, Public IP/EIP, 사용자명(`ubuntu`, `ec2-user`) 중 하나가 어긋난 경우가 많다.
- 80번 포트를 9000번으로 redirect하는 것은 실습 편의 방식이다. 실무에서는 ALB/Nginx가 앞단에서 80/443을 받고 backend 포트로 넘기는 구성이 더 자연스럽다.
- EC2가 두 대면 애플리케이션 파일과 설정이 두 서버에 모두 맞게 반영되어야 한다. 이후 CI/CD가 필요한 이유와 연결된다.

## 관련 개념

- [[summaries/2026-05-07-aws-ec2-nginx-rds|2026-05-07 AWS EC2, Nginx, Spring Boot, RDS 연결]]
- [[summaries/2026-05-08-aws-route53-load-balancer-https|2026-05-08 AWS Route 53, Load Balancer, HTTPS]]
- [[entities/amazon-ec2|Amazon EC2]]
- [[concepts/aws-cloud-vpc-networking|AWS Cloud와 VPC 네트워킹]]
- [[concepts/aws-route53-load-balancer-https|AWS Route 53, Load Balancer, HTTPS 흐름]]
- [[entities/spring-boot|Spring Boot]]
- [[entities/maven|Maven]]

## 출처

- `raw/KoreaICT/6. AWS/2026.05.07(목)/2026.05.07(목).md`
- `raw/KoreaICT/6. AWS/2026.05.08(금)/2026.05.08(금).md`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.02.AWS 교안(실습).pdf`
- `raw/KoreaICT/6. AWS/교육 자료/cloud.03.AWS 교안(이론).pdf`
