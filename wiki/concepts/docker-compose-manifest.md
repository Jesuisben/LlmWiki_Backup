---
title: Docker Compose manifest
created: 2026-07-02
updated: 2026-07-02
type: concept
tags: [linux, backend]
sources:
  - raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf
  - raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf
  - raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md
status: growing
confidence: high
---

# Docker Compose manifest

## 정의

Docker Compose manifest는 여러 컨테이너와 그 주변 환경을 하나의 YAML 파일에 정의한 문서다. `docker compose up`은 이 파일을 읽어 service, network, volume, port, environment를 만든다.

## 왜 중요한가

MySQL + Spring Boot, MySQL + WordPress처럼 여러 컨테이너가 함께 필요한 구성은 `docker run`을 여러 번 손으로 치면 실수하기 쉽다. Compose는 실행 구성을 문서로 남겨 반복 가능하게 한다.

## 주요 항목

| 항목 | 의미 |
|---|---|
| `services` | 실행할 컨테이너/서비스 목록 |
| `image` | 사용할 이미지 |
| `container_name` | 실제 컨테이너 이름 |
| `ports` | 호스트 포트와 컨테이너 포트 연결 |
| `volumes` | volume/bind mount 연결 |
| `networks` | 연결할 Docker network |
| `environment` | 컨테이너 환경 변수 |
| `depends_on` | 다른 서비스와의 시작 순서 의존 |
| `restart` | 재시작 정책 |
| `command` | 기본 실행 명령/옵션 재정의 |

## 수업 예제 구조

```yaml
services:
  mysql-svc:
    container_name: mysql-ctr
    image: mysql:8.0
    networks:
      - spring-mysql-net
    volumes:
      - mysql-spring-vol:/var/lib/mysql
    restart: always
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    environment:
      MYSQL_ROOT_PASSWORD: My@Sql01
      MYSQL_DATABASE: coffee
      MYSQL_USER: spring
      MYSQL_PASSWORD: Spring@1234
    ports:
      - "3306:3306"

  spring-svc:
    container_name: spring-ctr
    depends_on:
      - mysql-svc
    image: myspring-img:latest
    networks:
      - spring-mysql-net
    ports:
      - "9000:9000"
    restart: always
    environment:
      SPRING_PROFILES_ACTIVE: docker
      SPRING_DATASOURCE_URL: jdbc:mysql://mysql-svc:3306/coffee
      SPRING_DATASOURCE_USERNAME: spring
      SPRING_DATASOURCE_PASSWORD: Spring@1234

networks:
  spring-mysql-net:

volumes:
  mysql-spring-vol:
```

## 실행과 삭제

```bash
docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml up -d
docker container ps -a --format "table {{.Names}}	{{.Status}}"
docker compose -p hello -f ~/docker/compose01/compose_mysql_springboot.yml down
docker volume rm hello_mysql-spring-vol
```

## 수업에서 나온 주의점

- YAML 들여쓰기는 tab이 아니라 space를 사용한다.
- `services` 아래의 이름(`mysql-svc`)은 Compose 내부에서 참조되는 service 이름이다.
- `container_name`은 실제 컨테이너 이름이다.
- `SPRING_DATASOURCE_URL`에서는 같은 Compose network의 service 이름을 host처럼 쓸 수 있다.
- `down`은 기본적으로 image와 volume까지 모두 지우지 않는다.
- 사용자 메모에는 WordPress+MySQL compose 자료의 들여쓰기/설정값 오류를 직접 수정한 경험이 남아 있다.

## 관련 페이지

- [[summaries/2026-05-01-docker-compose|2026-05-01 Docker Compose와 다중 컨테이너 실행]]
- [[concepts/dockerfile-vs-compose|Dockerfile vs Docker Compose]]
- [[concepts/docker-network-volume|Docker 네트워크와 볼륨]]
- [[comparisons/docker-cp-vs-bind-mount-vs-volume|docker cp vs bind mount vs volume]]

## 출처

- `raw/Study/5. Linux/2026.05.01(금)/2026.05.01(금).md`
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(이론).pdf` — Compose 개념, up/down, Dockerfile과 Compose 비교
- `raw/Study/5. Linux/교육 자료/Docker/Docker 교안(실습).pdf` — MySQL+Spring Boot Compose
- `raw/Study/5. Linux/교육 자료/도커 컴포즈 종합 실습.md`
