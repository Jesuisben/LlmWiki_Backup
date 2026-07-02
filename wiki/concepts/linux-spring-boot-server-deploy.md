---
title: Linux에서 Spring Boot 서버 실행
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, spring-boot, backend]
sources:
  - raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
status: growing
confidence: high
---

# Linux에서 Spring Boot 서버 실행

## 정의

Linux에서 Spring Boot 서버를 실행한다는 것은 IDE 실행 버튼이 아니라 서버 터미널에서 프로젝트를 clone하고, Maven으로 `.jar`를 만들고, `java -jar`로 실행하며, 포트·방화벽·웹서버 충돌을 확인하는 과정이다.

## 수업에서 배운 흐름

1. Apache/Nginx 같은 기존 웹 서버가 포트를 점유하지 않도록 중지했다.
2. GitHub에서 Spring Boot 프로젝트를 clone했다.
3. `application.properties`에서 `server.port=9000`을 확인했다.
4. 필요하면 80번 포트를 9000번으로 redirect했다.
5. UFW에서 Spring Boot 포트를 허용했다.
6. Maven을 설치하고 `pom.xml`이 있는 위치에서 package를 수행했다.
7. `target/` 아래 `.jar`를 확인하고 `java -jar`로 실행했다.
8. 브라우저에서 VM IP 또는 포트 매핑 주소로 접속했다.

## 핵심 명령어

```bash
sudo systemctl stop nginx
sudo systemctl disable nginx
sudo systemctl stop apache2
sudo systemctl disable apache2
git clone https://github.com/Jesuisben/git_sample_02.git
cd git_sample_02
grep port src/main/resources/application.properties
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 9000
sudo iptables -t nat -L -n | grep 9000
sudo ufw allow 9000/tcp
sudo apt install -y maven
mvn -v
mvn clean package -DskipTests
cd target
ls *.jar
java -jar shopping-0.0.1-SNAPSHOT.jar
```

## Apache/Nginx와의 관계

04/27에는 Apache/Nginx를 직접 설치하고 `/var/www/html/`에 정적 파일을 배치했다. 04/28에는 Spring Boot 자체가 9000번 포트에서 웹 서버처럼 응답하는 구조를 다뤘다. 따라서 포트 충돌과 방화벽 설정을 같이 봐야 한다.

## 왜 중요한가

Spring Boot를 개발 PC에서 실행하는 것과 서버에서 운영하는 것은 다르다. 서버에서는 빌드 산출물, 포트, 방화벽, 프로세스, 로그, 기존 서비스 충돌을 직접 확인해야 한다. 이 과정이 Dockerfile과 CI/CD의 출발점이다.

## 자주 헷갈리는 점

- Maven 명령은 `pom.xml`이 있는 위치에서 실행해야 한다.
- `mvn clean package`는 빌드이고, `java -jar`는 실행이다.
- 포트가 열려 있어도 UFW, VirtualBox NAT/Bridge, iptables 설정이 맞지 않으면 브라우저 접근이 안 될 수 있다.
- nginx/apache2가 같은 포트를 쓰고 있으면 Spring Boot 확인이 꼬일 수 있다.
- `-DskipTests`는 테스트 생략이므로 실무에서는 의미를 알고 써야 한다.

## 관련 페이지

- [[summaries/2026-04-27-linux-archive-java-alias|2026-04-27 Linux 압축, 다운로드, Java 실행 준비]]
- [[summaries/2026-04-28-maven-spring-boot-docker-intro|2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/maven|Maven]]
- [[entities/spring-boot|Spring Boot]]

## 출처

- `raw/Study/5. Linux/2026.04.27(월)/2026.04.27(월).md`
- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
- `raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf` — Apache/Nginx, Maven, Spring Boot 서버 실행 실습
