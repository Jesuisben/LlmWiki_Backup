---
title: 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱
created: 2026-07-02
updated: 2026-07-06
type: summary
tags: [linux, docker, spring-boot, backend, curriculum]
sources:
  - raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md
  - raw/Study/5. Linux/교육 자료/로드 밸런싱.png
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
status: growing
confidence: high
---

# 2026-04-30 Dockerfile, Spring Boot 컨테이너, 로드 밸런싱

## 한 줄 요약

`docker commit`보다 재현 가능한 Dockerfile을 작성하고, Spring Boot jar를 이미지로 만든 뒤 nginx reverse proxy와 load balancing 구조를 실습한 날이다.

## 배운 내용

- Dockerfile의 `FROM`, `COPY`, `RUN`, `EXPOSE`, `ENTRYPOINT`를 배웠다.
- `docker build -t 이미지명 -f Dockerfile경로 .`로 사용자 정의 이미지를 만들었다.
- Maven package로 만든 Spring Boot jar를 Docker image에 포함했다.
- 여러 Apache/nginx backend 컨테이너를 만들고, 앞단 nginx reverse proxy에서 분산했다.
- `nginx.conf`의 `upstream`과 `proxy_pass`로 load balancing 구성을 작성했다.
- 로드 밸런싱 이미지를 통해 여러 상담자가 요청을 나눠 처리하는 비유로 이해했다.

## 핵심 개념

- [[comparisons/docker-commit-vs-dockerfile|docker commit vs Dockerfile]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-reverse-proxy-load-balancing|Docker reverse proxy와 로드 밸런싱]]
- [[concepts/linux-spring-boot-server-deploy|Linux에서 Spring Boot 서버 실행]]

## 실습 / 예제

```dockerfile
FROM eclipse-temurin:17-jdk
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
EXPOSE 9000
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

```bash
docker build -t myspring-img .
docker run --name myspring-ctr -d -p 9000:9000 myspring-img
docker network create proxy-net
docker run --name reverse-proxy -d -p 80:80 --network proxy-net -v ./nginx.conf:/etc/nginx/nginx.conf nginx
```

## 헷갈린 점 / 질문

- Dockerfile은 “컨테이너 여러 개 실행 파일”이 아니라 이미지를 만드는 레시피다.
- nginx reverse proxy 컨테이너만 외부 포트를 열고 backend 컨테이너들은 같은 Docker network 안에서만 통신하게 할 수 있다.
- load balancing은 속도 향상뿐 아니라 한 서버 장애가 전체 장애로 번지는 위험을 줄이는 관점도 있다.

## 관련 페이지

- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose와 다중 컨테이너 실행]]
- [[entities/docker|Docker]]
- [[entities/maven|Maven]]

## 출처

- `raw/Study/5. Linux/2026.04.30(목)/2026.04.30(목).md`
- `raw/Study/5. Linux/교육 자료/로드 밸런싱.png`
