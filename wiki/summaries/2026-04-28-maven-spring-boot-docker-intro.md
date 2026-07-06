---
title: 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, docker, spring-boot, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md
  - raw/Study/5. Linux/교육 자료/Linux/Linux 실습(MobaXterm, VirtualBox, 실습).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# 2026-04-28 Maven, Spring Boot 서버 실행, Docker 입문

## 한 줄 요약

GitHub에서 Spring Boot 프로젝트를 Linux 서버로 가져와 Maven으로 `.jar`를 만들고 실행한 뒤, Docker 설치와 기본 컨테이너 실행으로 넘어간 날이다.

## 배운 내용

- Spring Boot 프로젝트를 GitHub에서 Linux로 clone하고, 포트와 방화벽을 확인했다.
- Maven을 설치하고 `mvn clean package -DskipTests`로 jar를 만들었다.
- `java -jar`로 IDE 밖 Linux 터미널에서 Spring Boot 서버를 실행했다.
- Apache/Nginx 같은 웹 서버를 설치·중지하고 포트 충돌을 점검했다.
- Docker의 이미지/컨테이너 개념을 배우고 httpd, nginx, MySQL 컨테이너를 실행했다.
- `docker ps`, `docker stop`, `docker rm`, `docker images`, `docker rmi`로 컨테이너/이미지 생명주기를 확인했다.

## 핵심 개념

- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/linux-web-server-apache-nginx|Linux Apache/Nginx 웹서버]]
- [[concepts/docker-install-permission-setup|Docker 설치와 권한 설정]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]
- [[entities/maven|Maven]], [[entities/docker|Docker]]

## 실습 / 예제

```bash
sudo apt install -y maven
mvn -v
mvn clean package -DskipTests
java -jar target/*.jar

sudo ufw allow 9000
sudo systemctl stop nginx
sudo systemctl stop apache2

docker run --name apache01 -d -p 8080:80 httpd
docker ps
docker stop apache01
docker rm apache01
```

## 헷갈린 점 / 질문

- Maven은 Spring Boot 프로젝트를 “실행”하는 도구라기보다 의존성 관리와 빌드/패키징 도구다.
- `java -jar`는 이미 만들어진 jar를 실행하는 단계이고, `mvn package`는 jar를 만드는 단계다.
- Docker image는 실행 환경의 템플릿이고, container는 그 이미지에서 실제로 실행 중인 단위다.
- 포트가 열리지 않으면 Spring 코드보다 VM IP, 방화벽, 기존 웹서버 점유, Docker port mapping을 함께 봐야 한다.

## 관련 페이지

- [[summaries/2026-04-29-docker-network-volume-image|2026-04-29 Docker 네트워크, 볼륨, 사용자 정의 이미지]]
- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[entities/spring-boot|Spring Boot]]

## 출처

- `raw/Study/5. Linux/2026.04.28(화)/2026.04.28(화).md`
