---
title: 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱
created: 2026-07-02
updated: 2026-07-02
type: summary
tags: [linux, backend, spring-boot, curriculum, study-log]
sources:
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/로드 밸런싱.png
status: growing
confidence: high
---

# 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱

## 한 줄 요약

컨테이너 변경분을 이미지로 저장하는 `commit` 방식과 Dockerfile 빌드를 비교하고, Spring Boot + MySQL 컨테이너 연동과 nginx reverse proxy/load balancing까지 확장했다.

## 배운 내용

- `docker commit`은 실행 중인 컨테이너의 변경 상태를 이미지로 저장하는 방식이다.
- Dockerfile은 `FROM`, `COPY`, `ARG`, `EXPOSE`, `ENTRYPOINT`, `ENV` 등으로 이미지 생성 절차를 파일에 남긴다.
- `docker build -t ... -f Dockerfile ... .`에서 마지막 `.`은 build context이므로 누락하면 안 된다.
- Spring Boot 프로젝트를 Maven으로 패키징하고 `target/*.jar`를 컨테이너 안에 복사하는 Dockerfile을 확인했다.
- Spring Boot 컨테이너와 MySQL 컨테이너를 같은 network에 두고, 환경 변수로 DB URL/계정/비밀번호를 전달했다.
- MySQL 컨테이너에 접속해 `product` 테이블과 seed 데이터를 넣어 Spring Boot 화면에서 확인했다.
- `로드 밸런싱.png`의 상담원 비유처럼 요청을 여러 서버/컨테이너에 나눠 보내는 구조를 배웠다.
- nginx `upstream`과 `location`/`proxy_pass`로 Apache 그룹, nginx 그룹에 요청을 나누는 reverse proxy를 구성했다.

## 핵심 실습 / 예제

```dockerfile
FROM eclipse-temurin:17-jdk
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} docker_spring_mysql.jar
EXPOSE 9000
ENV JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF-8"
ENTRYPOINT ["java", "-jar", "/docker_spring_mysql.jar"]
```

```bash
docker build -t myspring-img -f Dockerfile01 .
docker network create spring-mysql-net
docker container run --net=spring-mysql-net --name=mysql-ctr -dit -e MYSQL_ROOT_PASSWORD=My@Sql01 -e MYSQL_DATABASE=coffee -e MYSQL_USER=gomdori -e MYSQL_PASSWORD=Spring@1234 mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
docker container run --name spring-ctr -d -i --net spring-mysql-net -v ~/images:/images -p 9000:9000 -e SPRING_PROFILES_ACTIVE=linux -e SPRING_DATASOURCE_URL=jdbc:mysql://mysql-ctr:3306/coffee -e SPRING_DATASOURCE_USERNAME=gomdori -e SPRING_DATASOURCE_PASSWORD=Spring@1234 myspring-img
```

```nginx
upstream backend_apache {
    server apache01:80;
    server apache02:80;
    server apache03:80;
}

server {
    listen 80;
    location /apache/ {
        proxy_pass http://backend_apache/;
    }
}
```

## 왜 중요한가

Dockerfile은 “우리 애플리케이션을 어떤 실행 환경으로 만들지”를 코드로 남긴다. reverse proxy와 load balancing은 컨테이너가 여러 개일 때 앞단에서 요청을 분배하고 장애·부하를 완화하는 서버 운영 개념이다.

## 헷갈린 점 / 질문

- `commit`은 수동 변경을 이미지로 굳히는 방식이라 재현성이 떨어질 수 있고, Dockerfile은 절차가 파일로 남아 재현성이 좋다.
- `ENTRYPOINT`는 컨테이너가 시작될 때 자동 실행할 명령이다.
- `SPRING_DATASOURCE_URL=jdbc:mysql://mysql-ctr:3306/coffee`에서 `mysql-ctr`는 같은 Docker network 안의 컨테이너 이름이다.
- reverse proxy는 사용자가 실제 backend 컨테이너와 직접 통신하지 않고 nginx 앞단을 거쳐 통신하게 만든다.

## 관련 페이지

- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]
- [[concepts/docker-image-container|Docker 이미지와 컨테이너]]

## 출처

- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — p.77~84 Dockerfile, p.84~100 Spring Boot+MySQL 컨테이너, p.100 전후 정리
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — Dockerfile/Compose 비교
- `raw/Study/5. Linux/교육 자료/로드 밸런싱.png`
